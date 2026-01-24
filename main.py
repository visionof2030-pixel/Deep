# main.py - النسخة الكاملة المعدلة
from fastapi import FastAPI, HTTPException, Depends, Header, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, timedelta
import os
import itertools

# استيراد الملفات المعدلة
import google.generativeai as genai
from database import init_db, get_connection
from create_key import create_key, generate_secure_code, validate_date_format
from security import activation_required
from key_logic import check_code_status

# إعدادات النظام
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN", "DEFAULT_ADMIN_TOKEN_CHANGE_ME")

app = FastAPI(title="نظام التفعيل الآمن", version="2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# تهيئة قاعدة البيانات عند البدء
init_db()

# نماذج البيانات
class Req(BaseModel):
    prompt: str
    model: Optional[str] = "gemini-2.5-flash-lite"

class GenerateKeyReq(BaseModel):
    expires_at: Optional[str] = None
    usage_limit: Optional[int] = None
    days_valid: Optional[int] = 30
    customer_email: Optional[str] = None
    customer_name: Optional[str] = None

class UpdateCodeReq(BaseModel):
    is_active: Optional[bool] = None
    expires_at: Optional[str] = None
    max_uses: Optional[int] = None

# قائمة مفاتيح Gemini API
api_keys = [
    os.getenv("GEMINI_API_KEY_1", ""),
    os.getenv("GEMINI_API_KEY_2", ""),
    os.getenv("GEMINI_API_KEY_3", ""),
    os.getenv("GEMINI_API_KEY_4", ""),
    os.getenv("GEMINI_API_KEY_5", ""),
    os.getenv("GEMINI_API_KEY_6", ""),
    os.getenv("GEMINI_API_KEY_7", ""),
]

# تصفية المفاتيح الفارغة
api_keys = [k for k in api_keys if k and k.strip()]

if not api_keys:
    print("⚠️  تحذير: لم يتم العثور على مفاتيح GEMINI API")
    api_keys = [""]  # قيمة افتراضية

key_cycle = itertools.cycle(api_keys)

def get_api_key():
    """الحصول على المفتاح التالي من الدوران"""
    return next(key_cycle)

# مصادقة المشرف
def admin_auth(x_admin_token: str = Header(...)):
    """التحقق من صلاحية المشرف"""
    if x_admin_token != ADMIN_TOKEN:
        raise HTTPException(status_code=401, detail="غير مصرح - رمز المشرف غير صحيح")
    return True

# ========== نقاط نهاية API العامة ==========

@app.get("/")
def root():
    """الصفحة الرئيسية"""
    return {
        "message": "نظام التفعيل الآمن",
        "version": "2.0",
        "endpoints": {
            "health": "/health",
            "ask": "/ask (POST - يتطلب كود التفعيل)",
            "admin": "/admin",
            "docs": "/docs"
        }
    }

@app.get("/health")
def health():
    """فحص صحة النظام"""
    return {
        "status": "operational",
        "timestamp": datetime.now().isoformat(),
        "database": "connected",
        "gemini_keys": len([k for k in api_keys if k])
    }

@app.post("/ask")
def ask(req: Req, _: None = Depends(activation_required)):
    """نقطة النهاية الرئيسية للذكاء الاصطناعي (تتطلب تفعيل)"""
    try:
        current_key = get_api_key()
        if not current_key:
            raise HTTPException(status_code=503, detail="لا توجد مفاتيح API متاحة")
        
        genai.configure(api_key=current_key)
        model = genai.GenerativeModel(req.model)
        response = model.generate_content(req.prompt)
        
        return {
            "answer": response.text,
            "model": req.model,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"خطأ في الذكاء الاصطناعي: {str(e)}")

# ========== نقاط نهاية الإدارة ==========

@app.post("/admin/generate", dependencies=[Depends(admin_auth)])
def admin_generate(req: GenerateKeyReq):
    """إنشاء كود تفعيل جديد"""
    try:
        # التحقق من صحة التاريخ إذا تم توفيره
        if req.expires_at and not validate_date_format(req.expires_at):
            raise HTTPException(status_code=400, detail="تنسيق التاريخ غير صحيح. استخدم YYYY-MM-DD")
        
        # التحقق من حد الاستخدام
        if req.usage_limit and (req.usage_limit < 1 or req.usage_limit > 1000):
            raise HTTPException(status_code=400, detail="حد الاستخدام يجب أن يكون بين 1 و 1000")
        
        # التحقق من عدد الأيام
        if req.days_valid and (req.days_valid < 1 or req.days_valid > 3650):
            raise HTTPException(status_code=400, detail="عدد الأيام يجب أن يكون بين 1 و 3650")
        
        code = create_key(
            expires_at=req.expires_at,
            usage_limit=req.usage_limit,
            days_valid=req.days_valid
        )
        
        # حفظ معلومات العميل إذا وجدت
        if req.customer_email or req.customer_name:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                "UPDATE activation_codes SET customer_email = ?, customer_name = ? WHERE code = ?",
                (req.customer_email, req.customer_name, code)
            )
            conn.commit()
            conn.close()
        
        return {
            "code": code,
            "message": "تم إنشاء الكود بنجاح",
            "expires_at": req.expires_at or f"بعد {req.days_valid} يوم",
            "usage_limit": req.usage_limit or "مرة واحدة"
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"خطأ في إنشاء الكود: {str(e)}")

@app.get("/admin/codes", dependencies=[Depends(admin_auth)])
def admin_codes():
    """الحصول على قائمة جميع الأكواد"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            id,
            code,
            is_active,
            max_uses,
            used_count,
            expires_at,
            created_at,
            last_used_at,
            customer_email,
            customer_name,
            CASE 
                WHEN expires_at IS NOT NULL AND date(expires_at) < date('now') THEN 'منتهي'
                WHEN is_active = 0 THEN 'معطل'
                WHEN max_uses IS NOT NULL AND used_count >= max_uses THEN 'مستهلك'
                ELSE 'نشط'
            END as status
        FROM activation_codes 
        ORDER BY created_at DESC
    """)
    rows = cur.fetchall()
    conn.close()
    
    return [
        {
            "id": r[0],
            "code": r[1],
            "is_active": bool(r[2]),
            "max_uses": r[3],
            "used_count": r[4],
            "expires_at": r[5],
            "created_at": r[6],
            "last_used_at": r[7],
            "customer_email": r[8],
            "customer_name": r[9],
            "status": r[10],
            "remaining_uses": r[3] - r[4] if r[3] else None,
            "is_expired": r[5] and datetime.strptime(r[5], '%Y-%m-%d') < datetime.now() if r[5] else False
        }
        for r in rows
    ]

@app.get("/admin/code/{code}", dependencies=[Depends(admin_auth)])
def admin_get_code(code: str):
    """الحصول على معلومات كود معين"""
    status_info = check_code_status(code)
    if not status_info:
        raise HTTPException(status_code=404, detail="الكود غير موجود")
    return status_info

@app.put("/admin/code/{code_id}/toggle", dependencies=[Depends(admin_auth)])
def admin_toggle(code_id: int):
    """تبديل حالة الكود (تفعيل/تعطيل)"""
    conn = get_connection()
    cur = conn.cursor()
    
    # التحقق من وجود الكود
    cur.execute("SELECT id FROM activation_codes WHERE id = ?", (code_id,))
    if not cur.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail="الكود غير موجود")
    
    cur.execute(
        "UPDATE activation_codes SET is_active = CASE WHEN is_active = 1 THEN 0 ELSE 1 END WHERE id = ?",
        (code_id,)
    )
    conn.commit()
    
    # الحصول على الحالة الجديدة
    cur.execute("SELECT is_active FROM activation_codes WHERE id = ?", (code_id,))
    new_status = bool(cur.fetchone()[0])
    
    conn.close()
    
    return {
        "status": "success",
        "message": f"تم {'تفعيل' if new_status else 'تعطيل'} الكود",
        "is_active": new_status
    }

@app.put("/admin/code/{code_id}", dependencies=[Depends(admin_auth)])
def admin_update_code(code_id: int, req: UpdateCodeReq):
    """تحديث معلومات الكود"""
    conn = get_connection()
    cur = conn.cursor()
    
    # التحقق من وجود الكود
    cur.execute("SELECT id FROM activation_codes WHERE id = ?", (code_id,))
    if not cur.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail="الكود غير موجود")
    
    # بناء استعلام التحديث الديناميكي
    updates = []
    params = []
    
    if req.is_active is not None:
        updates.append("is_active = ?")
        params.append(1 if req.is_active else 0)
    
    if req.expires_at is not None:
        if not validate_date_format(req.expires_at):
            conn.close()
            raise HTTPException(status_code=400, detail="تنسيق التاريخ غير صحيح. استخدم YYYY-MM-DD")
        updates.append("expires_at = ?")
        params.append(req.expires_at)
    
    if req.max_uses is not None:
        if req.max_uses < 1 or req.max_uses > 1000:
            conn.close()
            raise HTTPException(status_code=400, detail="حد الاستخدام يجب أن يكون بين 1 و 1000")
        updates.append("max_uses = ?")
        params.append(req.max_uses)
    
    if not updates:
        conn.close()
        raise HTTPException(status_code=400, detail="لم يتم توفير بيانات للتحديث")
    
    params.append(code_id)
    query = f"UPDATE activation_codes SET {', '.join(updates)} WHERE id = ?"
    
    cur.execute(query, params)
    conn.commit()
    conn.close()
    
    return {
        "status": "success",
        "message": "تم تحديث الكود بنجاح"
    }

@app.delete("/admin/code/{code_id}", dependencies=[Depends(admin_auth)])
def admin_delete(code_id: int):
    """حذف كود"""
    conn = get_connection()
    cur = conn.cursor()
    
    # التحقق من وجود الكود
    cur.execute("SELECT id, code FROM activation_codes WHERE id = ?", (code_id,))
    row = cur.fetchone()
    if not row:
        conn.close()
        raise HTTPException(status_code=404, detail="الكود غير موجود")
    
    # تسجيل المعلومات قبل الحذف (لأغراض التدقيق)
    deleted_code = row[1]
    
    # الحذف
    cur.execute("DELETE FROM activation_codes WHERE id = ?", (code_id,))
    conn.commit()
    conn.close()
    
    return {
        "status": "deleted",
        "message": f"تم حذف الكود: {deleted_code[:10]}..."
    }

@app.get("/admin/stats", dependencies=[Depends(admin_auth)])
def admin_stats():
    """إحصائيات النظام"""
    conn = get_connection()
    cur = conn.cursor()
    
    # إجمالي الأكواد
    cur.execute("SELECT COUNT(*) FROM activation_codes")
    total_codes = cur.fetchone()[0]
    
    # الأكواد النشطة
    cur.execute("""
        SELECT COUNT(*) FROM activation_codes 
        WHERE is_active = 1 
        AND (expires_at IS NULL OR date(expires_at) >= date('now'))
        AND (max_uses IS NULL OR used_count < max_uses)
    """)
    active_codes = cur.fetchone()[0]
    
    # الأكواد المستخدمة بالكامل
    cur.execute("""
        SELECT COUNT(*) FROM activation_codes 
        WHERE max_uses IS NOT NULL AND used_count >= max_uses
    """)
    used_codes = cur.fetchone()[0]
    
    # الأكواد المنتهية الصلاحية
    cur.execute("""
        SELECT COUNT(*) FROM activation_codes 
        WHERE expires_at IS NOT NULL AND date(expires_at) < date('now')
    """)
    expired_codes = cur.fetchone()[0]
    
    # الأكواد المعطلة يدوياً
    cur.execute("SELECT COUNT(*) FROM activation_codes WHERE is_active = 0")
    inactive_codes = cur.fetchone()[0]
    
    # إجمالي الاستخدامات
    cur.execute("SELECT COALESCE(SUM(used_count), 0) FROM activation_codes")
    total_uses = cur.fetchone()[0]
    
    # اليوم الأخير
    cur.execute("""
        SELECT COUNT(*) FROM activation_codes 
        WHERE date(created_at) = date('now')
    """)
    today_codes = cur.fetchone()[0]
    
    conn.close()
    
    return {
        "total_codes": total_codes,
        "active_codes": active_codes,
        "used_codes": used_codes,
        "expired_codes": expired_codes,
        "inactive_codes": inactive_codes,
        "total_uses": total_uses,
        "today_codes": today_codes,
        "timestamp": datetime.now().isoformat()
    }

@app.get("/admin/usage/{code_id}", dependencies=[Depends(admin_auth)])
def admin_code_usage(code_id: int):
    """سجل استخدامات كود معين"""
    conn = get_connection()
    cur = conn.cursor()
    
    # التحقق من وجود الكود
    cur.execute("SELECT code FROM activation_codes WHERE id = ?", (code_id,))
    row = cur.fetchone()
    if not row:
        conn.close()
        raise HTTPException(status_code=404, detail="الكود غير موجود")
    
    code = row[0]
    
    # الحصول على سجل الاستخدامات
    cur.execute("""
        SELECT 
            device_hash,
            ip_address,
            usage_time
        FROM code_usage_log 
        WHERE code_id = ?
        ORDER BY usage_time DESC
        LIMIT 100
    """, (code_id,))
    
    usage_log = cur.fetchall()
    conn.close()
    
    return {
        "code": code,
        "code_id": code_id,
        "total_uses": len(usage_log),
        "usage_log": [
            {
                "device_hash": log[0][:20] + "..." if log[0] else None,
                "ip_address": log[1] or "غير معروف",
                "usage_time": log[2]
            }
            for log in usage_log
        ]
    }

# ========== واجهة المستخدم الإدارية ==========

@app.get("/admin", response_class=HTMLResponse)
def admin_page():
    """لوحة التحكم الإدارية"""
    return """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>لوحة تحكم نظام التفعيل</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', 'Cairo', sans-serif;
        }
        
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
            color: #333;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
            overflow: hidden;
        }
        
        .header {
            background: linear-gradient(135deg, #2c3e50 0%, #4a6491 100%);
            color: white;
            padding: 30px;
            text-align: center;
            border-bottom: 5px solid #667eea;
        }
        
        .header h1 {
            font-size: 32px;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 15px;
        }
        
        .header p {
            font-size: 18px;
            opacity: 0.9;
        }
        
        .admin-panel {
            padding: 30px;
        }
        
        .panel-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px;
            margin-bottom: 30px;
        }
        
        .card {
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
            border: 2px solid #e8e8e8;
            transition: all 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.15);
            border-color: #667eea;
        }
        
        .card h3 {
            color: #2c3e50;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 2px solid #f0f0f0;
            font-size: 22px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .card h3 i {
            color: #667eea;
            font-size: 24px;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 8px;
            color: #555;
            font-weight: 600;
            font-size: 16px;
        }
        
        .form-group input,
        .form-group select,
        .form-group textarea {
            width: 100%;
            padding: 14px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 16px;
            transition: all 0.3s;
            background: #f9f9f9;
        }
        
        .form-group input:focus,
        .form-group select:focus,
        .form-group textarea:focus {
            outline: none;
            border-color: #667eea;
            background: white;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        
        .btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 16px 30px;
            border-radius: 10px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            width: 100%;
            margin-top: 10px;
        }
        
        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 7px 20px rgba(102, 126, 234, 0.4);
        }
        
        .btn-success {
            background: linear-gradient(135deg, #38b2ac 0%, #319795 100%);
        }
        
        .btn-warning {
            background: linear-gradient(135deg, #ed8936 0%, #dd6b20 100%);
        }
        
        .btn-danger {
            background: linear-gradient(135deg, #f56565 0%, #e53e3e 100%);
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        
        .stat-card {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            border: 2px solid #dee2e6;
        }
        
        .stat-number {
            font-size: 36px;
            font-weight: 800;
            color: #2c3e50;
            margin-bottom: 10px;
        }
        
        .stat-label {
            font-size: 16px;
            color: #6c757d;
            font-weight: 600;
        }
        
        .table-container {
            overflow-x: auto;
            margin-top: 30px;
            background: white;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            min-width: 1000px;
        }
        
        th {
            background: linear-gradient(135deg, #4a6491 0%, #2c3e50 100%);
            color: white;
            padding: 18px 15px;
            text-align: right;
            font-weight: 600;
            font-size: 16px;
        }
        
        td {
            padding: 15px;
            border-bottom: 1px solid #e8e8e8;
            text-align: right;
            font-size: 15px;
        }
        
        tr:hover {
            background: #f8f9fa;
        }
        
        .code-cell {
            font-family: monospace;
            font-size: 14px;
            direction: ltr;
            text-align: center;
        }
        
        .status-badge {
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 600;
            display: inline-block;
        }
        
        .status-active {
            background: #d1fae5;
            color: #065f46;
        }
        
        .status-inactive {
            background: #fee2e2;
            color: #991b1b;
        }
        
        .status-expired {
            background: #fef3c7;
            color: #92400e;
        }
        
        .status-used {
            background: #dbeafe;
            color: #1e40af;
        }
        
        .action-buttons {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }
        
        .action-btn {
            padding: 8px 15px;
            border: none;
            border-radius: 6px;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            gap: 5px;
        }
        
        .action-btn:hover {
            opacity: 0.9;
            transform: translateY(-2px);
        }
        
        .btn-toggle {
            background: #38b2ac;
            color: white;
        }
        
        .btn-edit {
            background: #ed8936;
            color: white;
        }
        
        .btn-delete {
            background: #f56565;
            color: white;
        }
        
        .btn-info {
            background: #4299e1;
            color: white;
        }
        
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.7);
            z-index: 1000;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .modal-content {
            background: white;
            border-radius: 15px;
            padding: 30px;
            width: 100%;
            max-width: 500px;
            max-height: 90vh;
            overflow-y: auto;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        }
        
        .notification {
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 15px 25px;
            border-radius: 10px;
            color: white;
            font-weight: 600;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            z-index: 1001;
            animation: slideIn 0.3s ease-out;
        }
        
        .notification.success {
            background: linear-gradient(135deg, #38b2ac 0%, #319795 100%);
        }
        
        .notification.error {
            background: linear-gradient(135deg, #f56565 0%, #e53e3e 100%);
        }
        
        .notification.warning {
            background: linear-gradient(135deg, #ed8936 0%, #dd6b20 100%);
        }
        
        @keyframes slideIn {
            from {
                transform: translateX(100%);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }
        
        @media (max-width: 768px) {
            .panel-grid {
                grid-template-columns: 1fr;
            }
            
            .stats-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            
            .header h1 {
                font-size: 24px;
            }
            
            .header p {
                font-size: 16px;
            }
            
            .admin-panel {
                padding: 20px;
            }
        }
        
        .token-input-section {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 30px;
            border: 2px solid #dee2e6;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1><i class="fas fa-shield-alt"></i> لوحة تحكم نظام التفعيل الآمن</h1>
            <p>إدارة أكواد التفعيل - تتبع الاستخدامات - صلاحية زمنية</p>
        </div>
        
        <div class="admin-panel">
            <!-- إدخال رمز المشرف -->
            <div class="token-input-section" id="tokenSection">
                <h3><i class="fas fa-key"></i> مصادقة المشرف</h3>
                <div class="form-group">
                    <label>رمز المشرف</label>
                    <input type="password" id="adminToken" placeholder="أدخل رمز المشرف">
                </div>
                <button class="btn" onclick="setAdminToken()">
                    <i class="fas fa-sign-in-alt"></i> دخول
                </button>
            </div>
            
            <!-- الإحصائيات -->
            <div id="statsSection" style="display: none;">
                <div class="stats-grid" id="statsGrid">
                    <!-- سيتم ملؤها بالجافاسكربت -->
                </div>
            </div>
            
            <!-- لوحة التحكم -->
            <div id="dashboardSection" style="display: none;">
                <div class="panel-grid">
                    <!-- إنشاء كود جديد -->
                    <div class="card">
                        <h3><i class="fas fa-plus-circle"></i> إنشاء كود جديد</h3>
                        <div class="form-group">
                            <label>تاريخ الانتهاء (YYYY-MM-DD)</label>
                            <input type="date" id="expiryDate" min="2024-01-01" max="2030-12-31">
                            <small style="color: #666; display: block; margin-top: 5px;">اترك فارغاً للاستخدام الافتراضي (30 يوم)</small>
                        </div>
                        <div class="form-group">
                            <label>عدد مرات الاستخدام</label>
                            <input type="number" id="usageLimit" min="1" max="1000" placeholder="1 (مرة واحدة)">
                        </div>
                        <div class="form-group">
                            <label>الصلاحية بالأيام (إذا لم تحدد تاريخاً)</label>
                            <select id="daysValid">
                                <option value="7">7 أيام</option>
                                <option value="30" selected>30 يوم</option>
                                <option value="90">90 يوم</option>
                                <option value="180">6 أشهر</option>
                                <option value="365">سنة واحدة</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label>بريد العميل (اختياري)</label>
                            <input type="email" id="customerEmail" placeholder="email@example.com">
                        </div>
                        <div class="form-group">
                            <label>اسم العميل (اختياري)</label>
                            <input type="text" id="customerName" placeholder="اسم العميل">
                        </div>
                        <button class="btn" onclick="generateCode()">
                            <i class="fas fa-key"></i> إنشاء كود تفعيل
                        </button>
                    </div>
                    
                    <!-- فحص كود -->
                    <div class="card">
                        <h3><i class="fas fa-search"></i> فحص وتعديل كود</h3>
                        <div class="form-group">
                            <label>الكود المراد فحصه</label>
                            <input type="text" id="checkCodeInput" placeholder="أدخل الكود هنا..." style="font-family: monospace;">
                        </div>
                        <button class="btn btn-success" onclick="checkCode()">
                            <i class="fas fa-search"></i> فحص الحالة
                        </button>
                        <div id="codeStatusResult" style="margin-top: 20px; display: none;">
                            <!-- سيتم ملؤها بالجافاسكربت -->
                        </div>
                    </div>
                    
                    <!-- عمليات جماعية -->
                    <div class="card">
                        <h3><i class="fas fa-cogs"></i> عمليات النظام</h3>
                        <button class="btn btn-warning" onclick="refreshAll()" style="margin-bottom: 10px;">
                            <i class="fas fa-sync-alt"></i> تحديث كل شيء
                        </button>
                        <button class="btn btn-info" onclick="exportCodes()" style="margin-bottom: 10px;">
                            <i class="fas fa-download"></i> تصدير الأكواد
                        </button>
                        <button class="btn btn-danger" onclick="clearExpired()">
                            <i class="fas fa-trash"></i> حذف الأكواد المنتهية
                        </button>
                        <div style="margin-top: 20px; padding: 15px; background: #f8f9fa; border-radius: 8px;">
                            <h4 style="margin-bottom: 10px; color: #2c3e50;"><i class="fas fa-info-circle"></i> معلومات النظام</h4>
                            <div id="systemInfo">
                                <!-- سيتم ملؤها بالجافاسكربت -->
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- قائمة الأكواد -->
                <div class="table-container">
                    <h3 style="padding: 20px 20px 10px; color: #2c3e50;"><i class="fas fa-list"></i> قائمة الأكواد</h3>
                    <div style="padding: 0 20px 10px; display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <input type="text" id="searchInput" placeholder="🔍 بحث في الأكواد..." style="padding: 10px; width: 300px; border: 2px solid #e0e0e0; border-radius: 8px;">
                        </div>
                        <div>
                            <select id="filterStatus" onchange="filterCodes()" style="padding: 10px; border: 2px solid #e0e0e0; border-radius: 8px;">
                                <option value="">جميع الحالات</option>
                                <option value="active">نشطة فقط</option>
                                <option value="expired">منتهية</option>
                                <option value="inactive">معطلة</option>
                                <option value="used">مستهلكة</option>
                            </select>
                        </div>
                    </div>
                    <table id="codesTable">
                        <thead>
                            <tr>
                                <th>الكود</th>
                                <th>الحالة</th>
                                <th>الاستخدام</th>
                                <th>تاريخ الانتهاء</th>
                                <th>تاريخ الإنشاء</th>
                                <th>آخر استخدام</th>
                                <th>العميل</th>
                                <th>الإجراءات</th>
                            </tr>
                        </thead>
                        <tbody id="codesTableBody">
                            <!-- سيتم ملؤها بالجافاسكربت -->
                        </tbody>
                    </table>
                    <div style="padding: 20px; text-align: center; color: #666;">
                        <div id="paginationInfo"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <!-- نافذة تعديل الكود -->
    <div class="modal" id="editModal">
        <div class="modal-content">
            <h3><i class="fas fa-edit"></i> تعديل الكود</h3>
            <div class="form-group">
                <label>الكود</label>
                <input type="text" id="editCode" readonly style="background: #f0f0f0;">
            </div>
            <div class="form-group">
                <label>الحالة</label>
                <select id="editIsActive">
                    <option value="true">نشط</option>
                    <option value="false">معطل</option>
                </select>
            </div>
            <div class="form-group">
                <label>تاريخ الانتهاء (YYYY-MM-DD)</label>
                <input type="date" id="editExpiresAt">
            </div>
            <div class="form-group">
                <label>حد الاستخدام الأقصى</label>
                <input type="number" id="editMaxUses" min="1" max="1000">
            </div>
            <div class="form-group">
                <label>بريد العميل</label>
                <input type="email" id="editCustomerEmail">
            </div>
            <div class="form-group">
                <label>اسم العميل</label>
                <input type="text" id="editCustomerName">
            </div>
            <input type="hidden" id="editCodeId">
            <button class="btn btn-success" onclick="updateCode()">
                <i class="fas fa-save"></i> حفظ التعديلات
            </button>
            <button class="btn btn-warning" onclick="closeModal('editModal')" style="margin-top: 10px;">
                <i class="fas fa-times"></i> إلغاء
            </button>
        </div>
    </div>
    
    <!-- نافذة معلومات الكود -->
    <div class="modal" id="infoModal">
        <div class="modal-content">
            <h3><i class="fas fa-info-circle"></i> معلومات مفصلة</h3>
            <div id="detailedInfo">
                <!-- سيتم ملؤها بالجافاسكربت -->
            </div>
            <button class="btn" onclick="closeModal('infoModal')" style="margin-top: 20px;">
                <i class="fas fa-times"></i> إغلاق
            </button>
        </div>
    </div>
    
    <!-- الإشعارات -->
    <div id="notificationContainer"></div>
    
    <script>
        const API_BASE = window.location.origin;
        let adminToken = localStorage.getItem('admin_token');
        let currentPage = 1;
        const itemsPerPage = 20;
        let allCodes = [];
        
        // عند تحميل الصفحة
        window.onload = function() {
            if (adminToken) {
                document.getElementById('adminToken').value = adminToken;
                setAdminToken();
            }
            loadSystemInfo();
        };
        
        // تعيين رمز المشرف
        function setAdminToken() {
            adminToken = document.getElementById('adminToken').value.trim();
            if (!adminToken) {
                showNotification('الرجاء إدخال رمز المشرف', 'error');
                return;
            }
            
            localStorage.setItem('admin_token', adminToken);
            
            // اختبار الرمز
            fetch(`${API_BASE}/admin/stats`, {
                headers: { 'X-Admin-Token': adminToken }
            })
            .then(response => {
                if (response.ok) {
                    document.getElementById('tokenSection').style.display = 'none';
                    document.getElementById('statsSection').style.display = 'block';
                    document.getElementById('dashboardSection').style.display = 'block';
                    loadStats();
                    loadCodes();
                    showNotification('تم الدخول بنجاح', 'success');
                } else {
                    localStorage.removeItem('admin_token');
                    showNotification('رمز المشرف غير صحيح', 'error');
                }
            })
            .catch(() => {
                showNotification('خطأ في الاتصال بالخادم', 'error');
            });
        }
        
        // تحميل الإحصائيات
        function loadStats() {
            fetch(`${API_BASE}/admin/stats`, {
                headers: { 'X-Admin-Token': adminToken }
            })
            .then(response => response.json())
            .then(data => {
                const statsGrid = document.getElementById('statsGrid');
                statsGrid.innerHTML = `
                    <div class="stat-card">
                        <div class="stat-number">${data.total_codes}</div>
                        <div class="stat-label">إجمالي الأكواد</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">${data.active_codes}</div>
                        <div class="stat-label">أكواد نشطة</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">${data.used_codes}</div>
                        <div class="stat-label">أكواد مستخدمة</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">${data.expired_codes}</div>
                        <div class="stat-label">أكواد منتهية</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">${data.total_uses}</div>
                        <div class="stat-label">إجمالي الاستخدامات</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">${data.today_codes}</div>
                        <div class="stat-label">أكواد اليوم</div>
                    </div>
                `;
            })
            .catch(error => {
                console.error('خطأ في تحميل الإحصائيات:', error);
            });
        }
        
        // إنشاء كود جديد
        function generateCode() {
            const expiryDate = document.getElementById('expiryDate').value;
            const usageLimit = document.getElementById('usageLimit').value;
            const daysValid = document.getElementById('daysValid').value;
            const customerEmail = document.getElementById('customerEmail').value;
            const customerName = document.getElementById('customerName').value;
            
            if (usageLimit && (usageLimit < 1 || usageLimit > 1000)) {
                showNotification('حد الاستخدام يجب أن يكون بين 1 و 1000', 'error');
                return;
            }
            
            fetch(`${API_BASE}/admin/generate`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Admin-Token': adminToken
                },
                body: JSON.stringify({
                    expires_at: expiryDate || null,
                    usage_limit: usageLimit ? parseInt(usageLimit) : null,
                    days_valid: parseInt(daysValid),
                    customer_email: customerEmail || null,
                    customer_name: customerName || null
                })
            })
            .then(async response => {
                const data = await response.json();
                if (response.ok) {
                    // إعادة تعيين الحقول
                    document.getElementById('expiryDate').value = '';
                    document.getElementById('usageLimit').value = '';
                    document.getElementById('customerEmail').value = '';
                    document.getElementById('customerName').value = '';
                    
                    // عرض الكود
                    showNotification(`تم إنشاء الكود: ${data.code}`, 'success');
                    alert(`✅ تم إنشاء الكود بنجاح!\n\nالكود: ${data.code}\nالصلاحية: ${data.expires_at}\nحد الاستخدام: ${data.usage_limit}`);
                    
                    // تحديث القائمة والإحصائيات
                    loadStats();
                    loadCodes();
                } else {
                    showNotification(data.detail || 'خطأ في إنشاء الكود', 'error');
                }
            })
            .catch(error => {
                showNotification('خطأ في الاتصال بالخادم', 'error');
            });
        }
        
        // تحميل قائمة الأكواد
        function loadCodes() {
            fetch(`${API_BASE}/admin/codes`, {
                headers: { 'X-Admin-Token': adminToken }
            })
            .then(response => response.json())
            .then(codes => {
                allCodes = codes;
                displayCodes(allCodes);
            })
            .catch(error => {
                console.error('خطأ في تحميل الأكواد:', error);
                showNotification('خطأ في تحميل الأكواد', 'error');
            });
        }
        
        // عرض الأكواد في الجدول
        function displayCodes(codes) {
            const tbody = document.getElementById('codesTableBody');
            tbody.innerHTML = '';
            
            // التصفية حسب البحث
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();
            const filterStatus = document.getElementById('filterStatus').value;
            
            let filteredCodes = codes.filter(code => {
                // البحث
                if (searchTerm && !code.code.toLowerCase().includes(searchTerm) && 
                    !(code.customer_email && code.customer_email.toLowerCase().includes(searchTerm)) &&
                    !(code.customer_name && code.customer_name.toLowerCase().includes(searchTerm))) {
                    return false;
                }
                
                // التصفية حسب الحالة
                if (filterStatus) {
                    if (filterStatus === 'active' && code.status !== 'نشط') return false;
                    if (filterStatus === 'expired' && code.status !== 'منتهي') return false;
                    if (filterStatus === 'inactive' && code.status !== 'معطل') return false;
                    if (filterStatus === 'used' && code.status !== 'مستهلك') return false;
                }
                
                return true;
            });
            
            // التقسيم إلى صفحات
            const totalPages = Math.ceil(filteredCodes.length / itemsPerPage);
            const startIndex = (currentPage - 1) * itemsPerPage;
            const endIndex = startIndex + itemsPerPage;
            const pageCodes = filteredCodes.slice(startIndex, endIndex);
            
            // عرض الأكواد
            pageCodes.forEach(code => {
                const row = document.createElement('tr');
                
                // تحديد فئة الحالة
                let statusClass = 'status-active';
                if (code.status === 'منتهي') statusClass = 'status-expired';
                else if (code.status === 'معطل') statusClass = 'status-inactive';
                else if (code.status === 'مستهلك') statusClass = 'status-used';
                
                // تنسيق التاريخ
                const formatDate = (dateStr) => {
                    if (!dateStr) return '---';
                    return new Date(dateStr).toLocaleDateString('ar-SA');
                };
                
                row.innerHTML = `
                    <td class="code-cell">${code.code}</td>
                    <td><span class="status-badge ${statusClass}">${code.status}</span></td>
                    <td>${code.used_count}/${code.max_uses || '∞'}</td>
                    <td>${formatDate(code.expires_at)}</td>
                    <td>${formatDate(code.created_at)}</td>
                    <td>${formatDate(code.last_used_at)}</td>
                    <td>${code.customer_name || '---'}<br><small>${code.customer_email || ''}</small></td>
                    <td>
                        <div class="action-buttons">
                            <button class="action-btn btn-toggle" onclick="toggleCode(${code.id})" title="${code.is_active ? 'تعطيل' : 'تفعيل'}">
                                <i class="fas fa-power-off"></i>
                            </button>
                            <button class="action-btn btn-info" onclick="showCodeInfo(${code.id})" title="معلومات">
                                <i class="fas fa-info-circle"></i>
                            </button>
                            <button class="action-btn btn-edit" onclick="editCode(${code.id}, '${code.code}')" title="تعديل">
                                <i class="fas fa-edit"></i>
                            </button>
                            <button class="action-btn btn-delete" onclick="deleteCode(${code.id})" title="حذف">
                                <i class="fas fa-trash"></i>
                            </button>
                        </div>
                    </td>
                `;
                tbody.appendChild(row);
            });
            
            // عرض معلومات الصفحة
            const paginationInfo = document.getElementById('paginationInfo');
            paginationInfo.innerHTML = `
                الصفحة ${currentPage} من ${totalPages} | إجمالي ${filteredCodes.length} كود
                ${totalPages > 1 ? `
                    <div style="margin-top: 10px;">
                        <button onclick="changePage(${currentPage - 1})" ${currentPage <= 1 ? 'disabled' : ''} style="padding: 5px 15px; margin: 0 5px; border: 1px solid #ddd; border-radius: 5px; background: ${currentPage <= 1 ? '#f0f0f0' : 'white'}; color: ${currentPage <= 1 ? '#999' : '#333'};">السابق</button>
                        <button onclick="changePage(${currentPage + 1})" ${currentPage >= totalPages ? 'disabled' : ''} style="padding: 5px 15px; margin: 0 5px; border: 1px solid #ddd; border-radius: 5px; background: ${currentPage >= totalPages ? '#f0f0f0' : 'white'}; color: ${currentPage >= totalPages ? '#999' : '#333'};">التالي</button>
                    </div>
                ` : ''}
            `;
        }
        
        // تغيير الصفحة
        function changePage(page) {
            if (page < 1) return;
            const totalPages = Math.ceil(allCodes.length / itemsPerPage);
            if (page > totalPages) return;
            
            currentPage = page;
            displayCodes(allCodes);
        }
        
        // تصفية الأكواد
        function filterCodes() {
            currentPage = 1;
            displayCodes(allCodes);
        }
        
        // فحص كود
        function checkCode() {
            const code = document.getElementById('checkCodeInput').value.trim();
            const resultDiv = document.getElementById('codeStatusResult');
            
            if (!code) {
                showNotification('الرجاء إدخال كود للفحص', 'error');
                return;
            }
            
            fetch(`${API_BASE}/admin/code/${encodeURIComponent(code)}`, {
                headers: { 'X-Admin-Token': adminToken }
            })
            .then(async response => {
                const data = await response.json();
                if (response.ok) {
                    resultDiv.style.display = 'block';
                    resultDiv.innerHTML = `
                        <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; border-right: 5px solid #38b2ac;">
                            <h4 style="color: #2c3e50; margin-bottom: 15px;"><i class="fas fa-key"></i> معلومات الكود</h4>
                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                                <div><strong>الكود:</strong> ${data.code}</div>
                                <div><strong>الحالة:</strong> <span class="status-badge status-${data.status === 'نشط' ? 'active' : data.status === 'منتهي' ? 'expired' : data.status === 'مستهلك' ? 'used' : 'inactive'}">${data.status}</span></div>
                                <div><strong>الاستخدام:</strong> ${data.used_count}/${data.max_uses || 'غير محدد'}</div>
                                <div><strong>تاريخ الانتهاء:</strong> ${data.expires_at || 'غير محدد'}</div>
                                <div><strong>تاريخ الإنشاء:</strong> ${data.created_at}</div>
                                <div><strong>آخر استخدام:</strong> ${data.last_used_at || 'لم يستخدم بعد'}</div>
                            </div>
                        </div>
                    `;
                } else {
                    showNotification(data.detail || 'الكود غير صالح', 'error');
                }
            })
            .catch(error => {
                showNotification('خطأ في الاتصال بالخادم', 'error');
            });
        }
        
        // تبديل حالة الكود
        function toggleCode(codeId) {
            if (!confirm('هل أنت متأكد من تغيير حالة الكود؟')) return;
            
            fetch(`${API_BASE}/admin/code/${codeId}/toggle`, {
                method: 'PUT',
                headers: { 'X-Admin-Token': adminToken }
            })
            .then(response => response.json())
            .then(data => {
                showNotification(data.message, 'success');
                loadStats();
                loadCodes();
            })
            .catch(error => {
                showNotification('خطأ في تغيير حالة الكود', 'error');
            });
        }
        
        // عرض معلومات الكود
        function showCodeInfo(codeId) {
            fetch(`${API_BASE}/admin/usage/${codeId}`, {
                headers: { 'X-Admin-Token': adminToken }
            })
            .then(response => response.json())
            .then(data => {
                const modal = document.getElementById('infoModal');
                const infoDiv = document.getElementById('detailedInfo');
                
                let usageHTML = '';
                if (data.usage_log && data.usage_log.length > 0) {
                    usageHTML = data.usage_log.map(log => `
                        <div style="padding: 10px; background: #f8f9fa; border-radius: 5px; margin-bottom: 5px;">
                            <div><strong>الوقت:</strong> ${new Date(log.usage_time).toLocaleString('ar-SA')}</div>
                            <div><strong>IP:</strong> ${log.ip_address}</div>
                            <div><strong>جهاز:</strong> ${log.device_hash}</div>
                        </div>
                    `).join('');
                } else {
                    usageHTML = '<div style="text-align: center; color: #666; padding: 20px;">لا يوجد سجل استخدامات</div>';
                }
                
                infoDiv.innerHTML = `
                    <div style="margin-bottom: 20px;">
                        <h4 style="color: #2c3e50; margin-bottom: 10px;">معلومات الكود</h4>
                        <div><strong>الكود:</strong> ${data.code}</div>
                        <div><strong>إجمالي الاستخدامات:</strong> ${data.total_uses}</div>
                    </div>
                    <div>
                        <h4 style="color: #2c3e50; margin-bottom: 10px;">سجل الاستخدامات</h4>
                        <div style="max-height: 300px; overflow-y: auto;">
                            ${usageHTML}
                        </div>
                    </div>
                `;
                
                modal.style.display = 'flex';
            })
            .catch(error => {
                showNotification('خطأ في تحميل معلومات الكود', 'error');
            });
        }
        
        // تعديل الكود
        function editCode(codeId, code) {
            // تحميل بيانات الكود الحالية
            fetch(`${API_BASE}/admin/code/${code}`, {
                headers: { 'X-Admin-Token': adminToken }
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('editCodeId').value = codeId;
                document.getElementById('editCode').value = data.code;
                document.getElementById('editIsActive').value = data.is_active ? 'true' : 'false';
                document.getElementById('editExpiresAt').value = data.expires_at || '';
                document.getElementById('editMaxUses').value = data.max_uses || '';
                document.getElementById('editCustomerEmail').value = data.customer_email || '';
                document.getElementById('editCustomerName').value = data.customer_name || '';
                
                document.getElementById('editModal').style.display = 'flex';
            })
            .catch(error => {
                showNotification('خطأ في تحميل بيانات الكود', 'error');
            });
        }
        
        // تحديث الكود
        function updateCode() {
            const codeId = document.getElementById('editCodeId').value;
            const isActive = document.getElementById('editIsActive').value === 'true';
            const expiresAt = document.getElementById('editExpiresAt').value || null;
            const maxUses = document.getElementById('editMaxUses').value ? parseInt(document.getElementById('editMaxUses').value) : null;
            
            fetch(`${API_BASE}/admin/code/${codeId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Admin-Token': adminToken
                },
                body: JSON.stringify({
                    is_active: isActive,
                    expires_at: expiresAt,
                    max_uses: maxUses
                })
            })
            .then(response => response.json())
            .then(data => {
                showNotification(data.message, 'success');
                closeModal('editModal');
                loadStats();
                loadCodes();
            })
            .catch(error => {
                showNotification('خطأ في تحديث الكود', 'error');
            });
        }
        
        // حذف كود
        function deleteCode(codeId) {
            if (!confirm('⚠️  تحذير: سيتم حذف الكود نهائياً ولا يمكن استعادته.\n\nهل أنت متأكد؟')) {
                return;
            }
            
            fetch(`${API_BASE}/admin/code/${codeId}`, {
                method: 'DELETE',
                headers: { 'X-Admin-Token': adminToken }
            })
            .then(response => response.json())
            .then(data => {
                showNotification(data.message, 'success');
                loadStats();
                loadCodes();
            })
            .catch(error => {
                showNotification('خطأ في حذف الكود', 'error');
            });
        }
        
        // تصدير الأكواد
        function exportCodes() {
            const csv = [
                ['الكود', 'الحالة', 'الاستخدام', 'تاريخ الانتهاء', 'تاريخ الإنشاء', 'آخر استخدام', 'العميل', 'البريد'],
                ...allCodes.map(code => [
                    code.code,
                    code.status,
                    `${code.used_count}/${code.max_uses || '∞'}`,
                    code.expires_at || 'غير محدد',
                    code.created_at,
                    code.last_used_at || '---',
                    code.customer_name || '---',
                    code.customer_email || '---'
                ])
            ].map(row => row.join(',')).join('\n');
            
            const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
            const link = document.createElement('a');
            const url = URL.createObjectURL(blob);
            link.setAttribute('href', url);
            link.setAttribute('download', `activation_codes_${new Date().toISOString().split('T')[0]}.csv`);
            link.style.visibility = 'hidden';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            
            showNotification('تم تصدير الأكواد', 'success');
        }
        
        // حذف الأكواد المنتهية
        function clearExpired() {
            if (!confirm('سيتم حذف جميع الأكواد المنتهية الصلاحية.\nهل أنت متأكد؟')) {
                return;
            }
            
            // يمكن إضافة API endpoint خاص لهذا الغرض
            showNotification('هذه الميزة تحت التطوير', 'warning');
        }
        
        // تحديث كل شيء
        function refreshAll() {
            loadStats();
            loadCodes();
            showNotification('تم تحديث البيانات', 'success');
        }
        
        // تحميل معلومات النظام
        function loadSystemInfo() {
            fetch(`${API_BASE}/health`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('systemInfo').innerHTML = `
                    <div><i class="fas fa-server"></i> الخادم: ${data.status}</div>
                    <div><i class="fas fa-database"></i> قاعدة البيانات: ${data.database}</div>
                    <div><i class="fas fa-key"></i> مفاتيح Gemini: ${data.gemini_keys}</div>
                    <div><i class="fas fa-clock"></i> آخر تحديث: ${new Date(data.timestamp).toLocaleTimeString('ar-SA')}</div>
                `;
            });
        }
        
        // إغلاق النافذة المنبثقة
        function closeModal(modalId) {
            document.getElementById(modalId).style.display = 'none';
        }
        
        // عرض الإشعارات
        function showNotification(message, type = 'success') {
            const container = document.getElementById('notificationContainer');
            const notification = document.createElement('div');
            notification.className = `notification ${type}`;
            notification.innerHTML = `<i class="fas fa-${type === 'success' ? 'check-circle' : type === 'error' ? 'exclamation-circle' : 'info-circle'}"></i> ${message}`;
            
            container.appendChild(notification);
            
            setTimeout(() => {
                notification.remove();
            }, 5000);
        }
        
        // البحث أثناء الكتابة
        document.getElementById('searchInput').addEventListener('input', function() {
            currentPage = 1;
            displayCodes(allCodes);
        });
        
        // تحديث معلومات النظام كل دقيقة
        setInterval(loadSystemInfo, 60000);
        
        // تحديث الإحصائيات كل 30 ثانية
        setInterval(loadStats, 30000);
    </script>
</body>
</html>
"""