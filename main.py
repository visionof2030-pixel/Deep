from fastapi import FastAPI, HTTPException, Depends, Header, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime, timedelta
import os
import itertools
import google.generativeai as genai
import sqlite3
import secrets
import uuid
import time
import re

app = FastAPI(title="نظام التقارير التربوية الذكي")

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# متغيرات النظام
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN", "admin12345")
DATABASE_FILE = "activation.db"

# 7 مفاتيح Gemini - تأكد من إضافتها في متغيرات البيئة
GEMINI_KEYS = [
    os.getenv("GEMINI_API_KEY_1", ""),
    os.getenv("GEMINI_API_KEY_2", ""),
    os.getenv("GEMINI_API_KEY_3", ""),
    os.getenv("GEMINI_API_KEY_4", ""),
    os.getenv("GEMINI_API_KEY_5", ""),
    os.getenv("GEMINI_API_KEY_6", ""),
    os.getenv("GEMINI_API_KEY_7", "")
]

# تصفية المفاتيح الفارغة
GEMINI_KEYS = [key for key in GEMINI_KEYS if key and len(key) > 10]

if not GEMINI_KEYS:
    print("⚠️ تحذير: لم يتم العثور على مفاتيح Gemini API")
    GEMINI_KEYS = ["dummy_key_for_testing"]

key_cycle = itertools.cycle(GEMINI_KEYS)

def get_gemini_key():
    return next(key_cycle)

# نماذج البيانات
class ActivationRequest(BaseModel):
    code: str

class AIRequest(BaseModel):
    prompt: str

class GenerateKeyRequest(BaseModel):
    expires_at: str = None
    usage_limit: int = None

# ==================== إدارة قاعدة البيانات ====================

def init_database():
    """تهيئة قاعدة البيانات"""
    conn = sqlite3.connect(DATABASE_FILE)
    cur = conn.cursor()
    
    # جدول أكواد التفعيل
    cur.execute('''
        CREATE TABLE IF NOT EXISTS activation_codes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT UNIQUE NOT NULL,
            is_active BOOLEAN DEFAULT 1,
            usage_count INTEGER DEFAULT 0,
            expires_at TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # جدول تسجيل النشاط
    cur.execute('''
        CREATE TABLE IF NOT EXISTS activity_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip_address TEXT,
            endpoint TEXT,
            method TEXT,
            user_agent TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print(f"✅ قاعدة البيانات '{DATABASE_FILE}' تم تهيئتها")

def get_db_connection():
    """الحصول على اتصال بقاعدة البيانات"""
    conn = sqlite3.connect(DATABASE_FILE)
    conn.row_factory = sqlite3.Row
    return conn

# ==================== وظائف المساعدة ====================

def log_activity(ip_address: str, endpoint: str, method: str, user_agent: str = None):
    """تسجيل النشاط"""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO activity_logs (ip_address, endpoint, method, user_agent) VALUES (?, ?, ?, ?)",
        (ip_address, endpoint, method, user_agent)
    )
    conn.commit()
    conn.close()

def create_activation_code(expires_at=None, usage_limit=None):
    """إنشاء كود تفعيل جديد"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    # توليد UUID
    new_code = str(uuid.uuid4()).lower()
    
    # إدخال في قاعدة البيانات
    cur.execute(
        "INSERT INTO activation_codes (code, expires_at) VALUES (?, ?)",
        (new_code, expires_at)
    )
    
    conn.commit()
    
    # جلب تفاصيل الكود
    cur.execute("SELECT * FROM activation_codes WHERE code = ?", (new_code,))
    code_data = cur.fetchone()
    conn.close()
    
    return {
        "code": new_code,
        "id": code_data['id'],
        "expires_at": code_data['expires_at']
    }

# ==================== نظام الأمان ====================

activation_attempts = {}
MAX_ATTEMPTS_PER_IP = 5
LOCKOUT_MINUTES = 15

def check_ip_lock(ip_address: str):
    """التحقق من قفل عنوان IP"""
    if ip_address in activation_attempts:
        attempts = activation_attempts[ip_address]
        
        # التحقق من القفل المؤقت
        if "lock_until" in attempts and attempts["lock_until"] > time.time():
            remaining = int((attempts["lock_until"] - time.time()) / 60)
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail=f"تم تجاوز عدد المحاولات. الرجاء المحاولة بعد {remaining} دقيقة"
            )
        
        # التحقق من عدد المحاولات
        if attempts.get("count", 0) >= MAX_ATTEMPTS_PER_IP:
            # قفل لمدة 15 دقيقة
            attempts["lock_until"] = time.time() + (LOCKOUT_MINUTES * 60)
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail=f"تم تجاوز عدد المحاولات. تم القفل لمدة {LOCKOUT_MINUTES} دقيقة"
            )
    
    return True

def record_attempt(ip_address: str, success: bool):
    """تسجيل محاولة تفعيل"""
    if ip_address not in activation_attempts:
        activation_attempts[ip_address] = {"count": 0, "success": 0, "first_attempt": time.time()}
    
    attempts = activation_attempts[ip_address]
    
    if success:
        attempts["success"] = attempts.get("success", 0) + 1
        # إعادة تعيين عند النجاح
        attempts["count"] = 0
        if "lock_until" in attempts:
            del attempts["lock_until"]
    else:
        attempts["count"] = attempts.get("count", 0) + 1

# ==================== وسيط التحقق من التفعيل ====================

async def verify_activation_code(x_activation_code: str = Header(...)):
    """التحقق من صحة كود التفعيل"""
    
    # تنظيف الكود
    code = x_activation_code.strip().lower()
    
    # التحقق من نمط UUID
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
    
    if not re.match(uuid_pattern, code):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="تنسيق كود التفعيل غير صحيح. يجب أن يكون بصيغة UUID"
        )
    
    # التحقق في قاعدة البيانات
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        cur.execute(
            "SELECT id, is_active, expires_at FROM activation_codes WHERE code = ?",
            (code,)
        )
        code_data = cur.fetchone()
        
        if not code_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="كود التفعيل غير موجود"
            )
        
        # التحقق من الحالة
        if not code_data['is_active']:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="كود التفعيل غير مفعل"
            )
        
        # التحقق من تاريخ الانتهاء
        if code_data['expires_at']:
            expires_date = datetime.strptime(code_data['expires_at'], "%Y-%m-%d")
            if datetime.now() > expires_date:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="كود التفعيل منتهي الصلاحية"
                )
        
        # تحديث عدد مرات الاستخدام
        cur.execute(
            "UPDATE activation_codes SET usage_count = usage_count + 1 WHERE id = ?",
            (code_data['id'],)
        )
        conn.commit()
        
        return {"code": code, "code_id": code_data['id']}
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"خطأ في التحقق: {str(e)}"
        )
    finally:
        conn.close()

# ==================== نقاط النهاية ====================

@app.on_event("startup")
async def startup_event():
    """الأحداث عند بدء التشغيل"""
    init_database()
    print("🚀 الخادم يعمل بنجاح")
    print(f"🔑 عدد مفاتيح Gemini المتاحة: {len(GEMINI_KEYS)}")

@app.get("/")
async def root():
    """الصفحة الرئيسية"""
    return {
        "message": "مرحباً بك في نظام التقارير التربوية الذكي",
        "version": "2.0.0",
        "status": "active",
        "endpoints": {
            "health": "/health",
            "verify": "/verify",
            "ask": "/ask",
            "admin": "/admin"
        }
    }

@app.get("/health")
async def health_check():
    """فحص صحة الخادم"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "database": "connected",
        "gemini_keys": len(GEMINI_KEYS),
        "uptime": "running"
    }

@app.post("/verify")
async def verify_code(request: Request, activation_req: ActivationRequest):
    """التحقق من كود التفعيل"""
    ip_address = request.client.host
    user_agent = request.headers.get("user-agent", "unknown")
    
    # تسجيل النشاط
    log_activity(ip_address, "/verify", "POST", user_agent)
    
    # التحقق من قفل IP
    try:
        check_ip_lock(ip_address)
    except HTTPException as e:
        record_attempt(ip_address, False)
        raise e
    
    # تنظيف الكود
    code = activation_req.code.strip().lower()
    
    # التحقق من نمط UUID
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
    
    if not re.match(uuid_pattern, code):
        record_attempt(ip_address, False)
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "valid": False,
                "message": "تنسيق كود التفعيل غير صحيح. مثال: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
            }
        )
    
    # التحقق في قاعدة البيانات
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        cur.execute(
            "SELECT id, is_active, usage_count, expires_at FROM activation_codes WHERE code = ?",
            (code,)
        )
        code_data = cur.fetchone()
        
        if not code_data:
            record_attempt(ip_address, False)
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={
                    "valid": False,
                    "message": "كود التفعيل غير موجود"
                }
            )
        
        # التحقق من الحالة
        if not code_data['is_active']:
            record_attempt(ip_address, False)
            return JSONResponse(
                status_code=status.HTTP_403_FORBIDDEN,
                content={
                    "valid": False,
                    "message": "كود التفعيل غير مفعل"
                }
            )
        
        # التحقق من تاريخ الانتهاء
        if code_data['expires_at']:
            expires_date = datetime.strptime(code_data['expires_at'], "%Y-%m-%d")
            if datetime.now() > expires_date:
                record_attempt(ip_address, False)
                return JSONResponse(
                    status_code=status.HTTP_403_FORBIDDEN,
                    content={
                        "valid": False,
                        "message": "كود التفعيل منتهي الصلاحية"
                    }
                )
        
        # تحديث عدد مرات الاستخدام
        new_usage_count = code_data['usage_count'] + 1
        cur.execute(
            "UPDATE activation_codes SET usage_count = ? WHERE id = ?",
            (new_usage_count, code_data['id'])
        )
        conn.commit()
        
        # تسجيل النجاح
        record_attempt(ip_address, True)
        
        return {
            "valid": True,
            "message": "تم التحقق من كود التفعيل بنجاح",
            "code": code,
            "usage_count": new_usage_count,
            "expires_at": code_data['expires_at'],
            "is_active": bool(code_data['is_active'])
        }
        
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "valid": False,
                "message": f"خطأ في الخادم: {str(e)}"
            }
        )
    finally:
        conn.close()

@app.post("/ask")
async def ask_ai(
    request: Request,
    ai_req: AIRequest,
    activation_data: dict = Depends(verify_activation_code)
):
    """طلب من الذكاء الاصطناعي"""
    ip_address = request.client.host
    user_agent = request.headers.get("user-agent", "unknown")
    
    # تسجيل النشاط
    log_activity(ip_address, "/ask", "POST", user_agent)
    
    try:
        # الحصول على مفتاح Gemini
        api_key = get_gemini_key()
        
        # تكوين Gemini
        genai.configure(api_key=api_key)
        
        # استخدام النموذج المناسب
        model = genai.GenerativeModel("models/gemini-2.5-flash-lite")
        
        # إضافة سياق عربي
        arabic_context = """
        أنت مساعد عربي متخصص في الكتابة التربوية والتعليمية.
        يجب أن تكون إجاباتك باللغة العربية الفصحى.
        كن دقيقاً واحترافياً في صياغة التقارير التربوية.
        """
        
        full_prompt = arabic_context + "\n\n" + ai_req.prompt
        
        # توليد الاستجابة
        response = model.generate_content(full_prompt)
        
        return {
            "success": True,
            "answer": response.text,
            "model": "gemini-2.5-flash-lite",
            "tokens": len(response.text.split())
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"خطأ في الذكاء الاصطناعي: {str(e)}"
        )

# ==================== واجهة الإدارة ====================

def verify_admin_token(x_admin_token: str = Header(...)):
    """التحقق من رمز المسؤول"""
    if x_admin_token != ADMIN_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="رمز المسؤول غير صحيح"
        )
    return True

@app.post("/admin/generate", dependencies=[Depends(verify_admin_token)])
async def generate_code(gen_req: GenerateKeyRequest):
    """إنشاء كود تفعيل جديد"""
    code_data = create_activation_code(gen_req.expires_at, gen_req.usage_limit)
    
    return {
        "success": True,
        "message": "تم إنشاء كود التفعيل بنجاح",
        "code": code_data["code"],
        "expires_at": code_data["expires_at"],
        "id": code_data["id"]
    }

@app.get("/admin/codes", dependencies=[Depends(verify_admin_token)])
async def list_codes():
    """قائمة جميع أكواد التفعيل"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute("""
        SELECT id, code, is_active, usage_count, expires_at, created_at 
        FROM activation_codes 
        ORDER BY created_at DESC
    """)
    
    codes = cur.fetchall()
    conn.close()
    
    return {
        "success": True,
        "count": len(codes),
        "codes": [
            {
                "id": code['id'],
                "code": code['code'],
                "is_active": bool(code['is_active']),
                "usage_count": code['usage_count'],
                "expires_at": code['expires_at'],
                "created_at": code['created_at']
            }
            for code in codes
        ]
    }

@app.put("/admin/code/{code_id}/toggle", dependencies=[Depends(verify_admin_token)])
async def toggle_code(code_id: int):
    """تبديل حالة الكود"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute(
        "UPDATE activation_codes SET is_active = NOT is_active WHERE id = ?",
        (code_id,)
    )
    
    conn.commit()
    
    # التحقق من التحديث
    cur.execute("SELECT code, is_active FROM activation_codes WHERE id = ?", (code_id,))
    updated_code = cur.fetchone()
    conn.close()
    
    if updated_code:
        status_text = "مفعل" if updated_code['is_active'] else "معطل"
        return {
            "success": True,
            "message": f"تم {status_text} الكود {updated_code['code']}",
            "code": updated_code['code'],
            "is_active": bool(updated_code['is_active'])
        }
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="الكود غير موجود"
    )

@app.delete("/admin/code/{code_id}", dependencies=[Depends(verify_admin_token)])
async def delete_code(code_id: int):
    """حذف كود التفعيل"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    # الحصول على معلومات الكود قبل الحذف
    cur.execute("SELECT code FROM activation_codes WHERE id = ?", (code_id,))
    code_info = cur.fetchone()
    
    if not code_info:
        conn.close()
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="الكود غير موجود"
        )
    
    # حذف الكود
    cur.execute("DELETE FROM activation_codes WHERE id = ?", (code_id,))
    conn.commit()
    conn.close()
    
    return {
        "success": True,
        "message": f"تم حذف الكود {code_info['code']} بنجاح",
        "deleted_code": code_info['code']
    }

@app.get("/admin/stats", dependencies=[Depends(verify_admin_token)])
async def get_stats():
    """إحصائيات النظام"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    # إحصائيات الأكواد
    cur.execute("SELECT COUNT(*) as total FROM activation_codes")
    total_codes = cur.fetchone()['total']
    
    cur.execute("SELECT COUNT(*) as active FROM activation_codes WHERE is_active = 1")
    active_codes = cur.fetchone()['active']
    
    cur.execute("SELECT COUNT(*) as used FROM activation_codes WHERE usage_count > 0")
    used_codes = cur.fetchone()['used']
    
    # إحصائيات النشاط
    cur.execute("SELECT COUNT(*) as logs FROM activity_logs")
    total_logs = cur.fetchone()['logs']
    
    conn.close()
    
    return {
        "success": True,
        "statistics": {
            "codes": {
                "total": total_codes,
                "active": active_codes,
                "inactive": total_codes - active_codes,
                "used": used_codes,
                "unused": total_codes - used_codes
            },
            "activity": {
                "total_logs": total_logs
            },
            "security": {
                "locked_ips": len([ip for ip, data in activation_attempts.items() 
                                  if data.get("lock_until", 0) > time.time()]),
                "total_attempts": sum(data.get("count", 0) for data in activation_attempts.values())
            },
            "system": {
                "gemini_keys": len(GEMINI_KEYS),
                "server_time": datetime.now().isoformat()
            }
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)