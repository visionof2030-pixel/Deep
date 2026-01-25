#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
نظام التقارير التربوية - النسخة التجارية
معد خصيصاً للنشر على Render.com
"""

import os
import json
import logging
import time
import hashlib
import secrets
import random
import string
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from functools import wraps
import psycopg2
from psycopg2.extras import RealDictCursor
import urllib.parse

from fastapi import FastAPI, HTTPException, Depends, Header, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import google.generativeai as genai

# ========== إعدادات Render ==========
app = FastAPI(
    title="نظام التقارير التربوية - النسخة التجارية",
    version="5.0",
    description="نظام محمي بأكواد تفعيل مكونة من 6 خانات",
    docs_url="/docs" if os.getenv("ENVIRONMENT") == "development" else None,
    redoc_url=None
)

# CORS للسماح بجميع الأصول (يمكن تقييدها لاحقاً)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========== إدارة المفاتيح السبعة على Render ==========
class GeminiKeyManager:
    """مدير المفاتيح السبعة مع تدوير ذكي"""
    
    def __init__(self):
        self.keys = self.load_keys_from_env()
        self.key_stats = {i: self.init_key_stats(i) for i in range(len(self.keys))}
        self.current_index = 0
        
    def load_keys_from_env(self):
        """تحميل المفاتيح السبعة من متغيرات Render"""
        keys = []
        for i in range(1, 8):
            key = os.getenv(f"GEMINI_API_KEY_{i}", "").strip()
            if key and len(key) > 20:  # مفتاح Gemini عادةً أطول من 20 حرف
                keys.append(key)
                print(f"✅ تم تحميل المفتاح {i}")
        
        if not keys:
            print("⚠️  تحذير: لم يتم العثور على مفاتيح Gemini")
            keys = [""]
        
        print(f"🔑 إجمالي المفاتيح المحملة: {len(keys)}")
        return keys
    
    def init_key_stats(self, idx):
        return {
            'total_requests': 0,
            'failed_requests': 0,
            'last_used': None,
            'daily_requests': 0,
            'last_reset': datetime.now().date(),
            'is_active': True,
            'consecutive_failures': 0,
            'last_success': None
        }
    
    def get_next_key(self):
        """الحصول على المفتاح الأنسب"""
        self.reset_daily_counts()
        
        # البحث عن مفتاح نشط مع أقل استخدام
        available_keys = []
        for idx, stats in self.key_stats.items():
            if (stats['is_active'] and 
                stats['daily_requests'] < 1490 and  # ترك هامش 10 طلبات
                (stats['consecutive_failures'] < 3 or 
                 (datetime.now() - (stats['last_used'] or datetime.min)).seconds > 600)):
                available_keys.append((idx, stats['daily_requests']))
        
        if not available_keys:
            # إعادة تفعيل جميع المفاتيح
            self.reactivate_all_keys()
            available_keys = [(idx, stats['daily_requests']) 
                             for idx, stats in self.key_stats.items()]
        
        # اختيار المفتاح الأقل استخداماً
        selected_idx = min(available_keys, key=lambda x: x[1])[0]
        self.key_stats[selected_idx]['last_used'] = datetime.now()
        self.key_stats[selected_idx]['daily_requests'] += 1
        self.key_stats[selected_idx]['total_requests'] += 1
        
        self.current_index = selected_idx
        return self.keys[selected_idx]
    
    def reset_daily_counts(self):
        """إعادة تعيين العدادات اليومية"""
        today = datetime.now().date()
        for stats in self.key_stats.values():
            if stats['last_reset'] != today:
                stats['daily_requests'] = 0
                stats['consecutive_failures'] = 0
                stats['last_reset'] = today
    
    def reactivate_all_keys(self):
        """إعادة تفعيل جميع المفاتيح"""
        for stats in self.key_stats.values():
            stats['is_active'] = True
            stats['consecutive_failures'] = 0
    
    def mark_success(self):
        """تسجيل نجاح الاستخدام"""
        stats = self.key_stats[self.current_index]
        stats['consecutive_failures'] = 0
        stats['last_success'] = datetime.now()
    
    def mark_failure(self):
        """تسجيل فشل الاستخدام"""
        stats = self.key_stats[self.current_index]
        stats['failed_requests'] += 1
        stats['consecutive_failures'] += 1
        
        if stats['consecutive_failures'] >= 3:
            stats['is_active'] = False
            print(f"⚠️  تم تعطيل المفتاح {self.current_index + 1} مؤقتاً")
    
    def get_status(self):
        """الحصول على حالة المفاتيح"""
        status = {}
        total_available = 0
        
        for i in range(len(self.keys)):
            stats = self.key_stats[i]
            remaining = max(0, 1500 - stats['daily_requests'])
            total_available += remaining
            
            status[f'key_{i+1}'] = {
                'is_active': stats['is_active'],
                'daily_used': stats['daily_requests'],
                'remaining': remaining,
                'total_used': stats['total_requests'],
                'failed': stats['failed_requests'],
                'last_used': stats['last_used'].isoformat() if stats['last_used'] else None
            }
        
        return {
            'keys_status': status,
            'total_available': total_available,
            'active_keys': sum(1 for stats in self.key_stats.values() if stats['is_active']),
            'total_keys': len(self.keys)
        }

# إنشاء مدول المفاتيح
key_manager = GeminiKeyManager()

# ========== قاعدة بيانات PostgreSQL على Render ==========
def get_db_connection():
    """الاتصال بقاعدة بيانات PostgreSQL على Render"""
    database_url = os.getenv('DATABASE_URL')
    
    if not database_url:
        # للتنمية المحلية
        return psycopg2.connect(
            host="localhost",
            database="reports_db",
            user="reports_user",
            password="reports_pass"
        )
    
    # على Render
    parsed_url = urllib.parse.urlparse(database_url)
    
    conn = psycopg2.connect(
        database=parsed_url.path[1:],
        user=parsed_url.username,
        password=parsed_url.password,
        host=parsed_url.hostname,
        port=parsed_url.port,
        sslmode='require' if 'render.com' in database_url else 'prefer'
    )
    
    return conn

def init_database():
    """تهيئة قاعدة البيانات على Render"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    # جدول الأكواد
    cur.execute("""
    CREATE TABLE IF NOT EXISTS activation_codes (
        id SERIAL PRIMARY KEY,
        code VARCHAR(6) UNIQUE NOT NULL,
        is_active BOOLEAN DEFAULT TRUE,
        max_uses INTEGER DEFAULT 1,
        used_count INTEGER DEFAULT 0,
        expires_at DATE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_used_at TIMESTAMP,
        device_hash VARCHAR(64) UNIQUE,
        ip_address VARCHAR(45),
        is_blocked BOOLEAN DEFAULT FALSE,
        customer_name VARCHAR(100),
        customer_email VARCHAR(100),
        plan_type VARCHAR(20) DEFAULT 'basic',
        remaining_days INTEGER,
        reseller_id INTEGER
    )
    """)
    
    # جدول التجار
    cur.execute("""
    CREATE TABLE IF NOT EXISTS resellers (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password_hash VARCHAR(64) NOT NULL,
        company_name VARCHAR(100),
        email VARCHAR(100) UNIQUE,
        phone VARCHAR(20),
        balance DECIMAL(10,2) DEFAULT 0,
        commission_rate DECIMAL(5,2) DEFAULT 0.30,
        total_sales INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        is_active BOOLEAN DEFAULT TRUE
    )
    """)
    
    # جدول المبيعات
    cur.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id SERIAL PRIMARY KEY,
        code_id INTEGER REFERENCES activation_codes(id),
        reseller_id INTEGER REFERENCES resellers(id),
        sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        amount_paid DECIMAL(10,2),
        payment_method VARCHAR(50),
        transaction_id VARCHAR(100) UNIQUE
    )
    """)
    
    # جدول الإحصائيات
    cur.execute("""
    CREATE TABLE IF NOT EXISTS system_stats (
        id SERIAL PRIMARY KEY,
        date DATE UNIQUE NOT NULL,
        total_requests INTEGER DEFAULT 0,
        successful_requests INTEGER DEFAULT 0,
        failed_requests INTEGER DEFAULT 0,
        new_codes INTEGER DEFAULT 0,
        active_users INTEGER DEFAULT 0,
        revenue DECIMAL(10,2) DEFAULT 0
    )
    """)
    
    # إضافة التاجر الافتراضي
    cur.execute("SELECT COUNT(*) FROM resellers WHERE username = 'admin'")
    if cur.fetchone()[0] == 0:
        password_hash = hashlib.sha256("Admin@123".encode()).hexdigest()
        cur.execute(
            """
            INSERT INTO resellers 
            (username, password_hash, company_name, email, commission_rate)
            VALUES (%s, %s, %s, %s, %s)
            """,
            ("admin", password_hash, "الإدارة العامة", "admin@system.com", 0.0)
        )
    
    conn.commit()
    cur.close()
    conn.close()
    print("✅ قاعدة بيانات Render جاهزة")

# ========== توليد الأكواد ==========
def generate_6_digit_code():
    """توليد كود 6 خانات فريد"""
    chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'  # أزلنا الأحرف المربكة
    while True:
        code = ''.join(random.choices(chars, k=6))
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM activation_codes WHERE code = %s", (code,))
        exists = cur.fetchone()
        cur.close()
        conn.close()
        
        if not exists:
            return code

# ========== التحقق من الأكواد ==========
def verify_activation_code(code: str, request: Request):
    """التحقق من كود التفعيل"""
    
    # التحقق من التنسيق
    if not code or len(code) != 6 or not code.isalnum():
        return {"valid": False, "reason": "تنسيق غير صحيح"}
    
    ip_address = request.client.host if request.client else "unknown"
    
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    try:
        cur.execute("""
            SELECT * FROM activation_codes 
            WHERE code = %s
        """, (code,))
        
        row = cur.fetchone()
        
        if not row:
            log_attempt(ip_address, code, "غير موجود", False)
            return {"valid": False, "reason": "كود غير موجود"}
        
        # التحقق من الحظر
        if row['is_blocked']:
            log_attempt(ip_address, code, "محظور", False)
            return {"valid": False, "reason": "كود محظور"}
        
        # التحقق من التفعيل
        if not row['is_active']:
            log_attempt(ip_address, code, "معطل", False)
            return {"valid": False, "reason": "كود معطل"}
        
        # التحقق من تاريخ الانتهاء
        if row['expires_at'] and row['expires_at'] < datetime.now().date():
            cur.execute("UPDATE activation_codes SET is_active = FALSE WHERE id = %s", 
                       (row['id'],))
            conn.commit()
            log_attempt(ip_address, code, "منتهي", False)
            return {"valid": False, "reason": "كود منتهي الصلاحية"}
        
        # التحقق من حد الاستخدام
        if row['max_uses'] and row['used_count'] >= row['max_uses']:
            log_attempt(ip_address, code, "مستهلك", False)
            return {"valid": False, "reason": "تجاوز حد الاستخدام"}
        
        # التحقق من الأيام المتبقية
        if row['remaining_days'] is not None and row['remaining_days'] <= 0:
            log_attempt(ip_address, code, "انتهت المدة", False)
            return {"valid": False, "reason": "انتهت مدة الاشتراك"}
        
        # إنشاء بصمة الجهاز
        device_hash = generate_device_hash(request)
        
        # إذا كان الكود جديداً
        if not row['device_hash']:
            cur.execute("""
                UPDATE activation_codes 
                SET device_hash = %s, ip_address = %s, last_used_at = %s
                WHERE id = %s
            """, (device_hash, ip_address, datetime.now(), row['id']))
        
        # التحقق من مطابقة الجهاز
        elif row['device_hash'] != device_hash:
            log_attempt(ip_address, code, "جهاز مختلف", False)
            return {"valid": False, "reason": "الكود مفعل على جهاز آخر"}
        
        # تحديث الاستخدام
        new_remaining = (row['remaining_days'] - 1) if row['remaining_days'] else None
        
        cur.execute("""
            UPDATE activation_codes 
            SET used_count = used_count + 1, 
                last_used_at = %s,
                remaining_days = %s
            WHERE id = %s
        """, (datetime.now(), new_remaining, row['id']))
        
        conn.commit()
        log_attempt(ip_address, code, "ناجح", True)
        
        return {
            "valid": True,
            "code_id": row['id'],
            "customer": row['customer_name'],
            "plan": row['plan_type'],
            "remaining_uses": row['max_uses'] - row['used_count'] - 1 if row['max_uses'] else None,
            "remaining_days": new_remaining
        }
        
    except Exception as e:
        conn.rollback()
        log_attempt(ip_address, code, f"خطأ: {str(e)}", False)
        return {"valid": False, "reason": "خطأ في النظام"}
        
    finally:
        cur.close()
        conn.close()

def generate_device_hash(request: Request):
    """توليد بصمة الجهاز"""
    user_agent = request.headers.get('user-agent', '')
    accept_language = request.headers.get('accept-language', '')
    
    # إضافة بعض المعلومات الفريدة
    info = f"{user_agent}:{accept_language}:{request.headers.get('accept-encoding', '')}"
    return hashlib.sha256(info.encode()).hexdigest()

def log_attempt(ip: str, code: str, reason: str, success: bool):
    """تسجيل محاولات الدخول"""
    print(f"{'✅' if success else '❌'} {ip} -> {code}: {reason}")

# ========== اعتماد التفعيل ==========
def activation_required(request: Request, x_activation_code: str = Header(...)):
    """اعتماد مشروط بالتفعيل"""
    if not x_activation_code:
        raise HTTPException(401, "مطلوب كود تفعيل")
    
    result = verify_activation_code(x_activation_code, request)
    
    if not result["valid"]:
        raise HTTPException(401, result["reason"])
    
    return result

# ========== نماذج البيانات ==========
class AIRequest(BaseModel):
    prompt: str
    model: Optional[str] = "gemini-2.5-flash-lite"

class VerifyRequest(BaseModel):
    code: str

class GenerateCodeRequest(BaseModel):
    plan_type: str = "basic"  # basic, premium, pro
    duration_days: int = 30
    customer_name: Optional[str] = None
    customer_email: Optional[str] = None
    max_uses: Optional[int] = 1

# ========== نقاط نهاية API ==========

@app.get("/")
async def root():
    return {
        "service": "نظام التقارير التربوية",
        "version": "5.0",
        "environment": os.getenv("ENVIRONMENT", "production"),
        "status": "نشط",
        "docs": "/docs" if os.getenv("ENVIRONMENT") == "development" else "مخفية"
    }

@app.get("/health")
async def health_check():
    """فحص صحة النظام على Render"""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1")
        cur.close()
        conn.close()
        
        return {
            "status": "healthy",
            "timestamp": datetime.now().isoformat(),
            "database": "connected",
            "keys_status": key_manager.get_status(),
            "environment": os.getenv("ENVIRONMENT", "production")
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }, 500

@app.post("/api/verify")
async def verify_code_api(data: VerifyRequest, request: Request):
    """التحقق من كود التفعيل"""
    result = verify_activation_code(data.code, request)
    return result

@app.post("/api/ask")
async def ask_ai_api(
    request_data: AIRequest,
    auth: dict = Depends(activation_required)
):
    """طلب من الذكاء الاصطناعي"""
    
    start_time = time.time()
    
    try:
        # الحصول على مفتاح
        api_key = key_manager.get_next_key()
        
        if not api_key:
            key_manager.mark_failure()
            raise HTTPException(503, "الخدمة غير متاحة حالياً")
        
        # استخدام Gemini
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(request_data.model)
        
        # تحسين الطلب
        enhanced_prompt = f"""
        {request_data.prompt}
        
        [معلومات العميل]
        - نوع الاشتراك: {auth.get('plan', 'basic')}
        - الاسم: {auth.get('customer', 'مستخدم النظام')}
        
        يرجى تقديم إجابة متخصصة ومناسبة للاستخدام التربوي.
        """
        
        response = model.generate_content(enhanced_prompt)
        response_time = time.time() - start_time
        
        # تسجيل النجاح
        key_manager.mark_success()
        update_daily_stats(True)
        
        return {
            "answer": response.text,
            "response_time": round(response_time, 2),
            "plan": auth.get('plan'),
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        key_manager.mark_failure()
        update_daily_stats(False)
        
        if "quota" in str(e).lower():
            raise HTTPException(429, "تم تجاوز الحد المسموح، حاول لاحقاً")
        
        raise HTTPException(500, f"خطأ في المعالجة: {str(e)}")

def update_daily_stats(success: bool):
    """تحديث إحصائيات اليوم"""
    today = datetime.now().date()
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        # إدخال أو تحديث سجل اليوم
        cur.execute("""
            INSERT INTO system_stats (date, total_requests, successful_requests, failed_requests)
            VALUES (%s, 1, %s, %s)
            ON CONFLICT (date) DO UPDATE SET
                total_requests = system_stats.total_requests + 1,
                successful_requests = system_stats.successful_requests + %s,
                failed_requests = system_stats.failed_requests + %s
        """, (today, 1 if success else 0, 0 if success else 1, 
              1 if success else 0, 0 if success else 1))
        
        conn.commit()
    finally:
        cur.close()
        conn.close()

# ========== واجهة الإدارة ==========
@app.post("/admin/generate")
async def generate_code_admin(
    data: GenerateCodeRequest,
    admin_token: str = Header(...)
):
    """إنشاء كود جديد (للمشرف)"""
    
    # التحقق من رمز المشرف
    if admin_token != os.getenv("ADMIN_TOKEN"):
        raise HTTPException(401, "غير مصرح")
    
    # توليد الكود
    code = generate_6_digit_code()
    
    # حساب تاريخ الانتهاء
    expires_at = (datetime.now() + timedelta(days=data.duration_days)).date()
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        cur.execute("""
            INSERT INTO activation_codes 
            (code, expires_at, plan_type, customer_name, customer_email, max_uses, remaining_days)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        """, (code, expires_at, data.plan_type, data.customer_name, 
              data.customer_email, data.max_uses, data.duration_days))
        
        code_id = cur.fetchone()[0]
        
        # تحديث الإحصائيات
        cur.execute("""
            UPDATE system_stats 
            SET new_codes = COALESCE(new_codes, 0) + 1
            WHERE date = %s
        """, (datetime.now().date(),))
        
        conn.commit()
        
        return {
            "success": True,
            "code": code,
            "expires_at": expires_at.isoformat(),
            "plan": data.plan_type,
            "duration": data.duration_days,
            "max_uses": data.max_uses
        }
        
    except Exception as e:
        conn.rollback()
        raise HTTPException(500, f"خطأ في إنشاء الكود: {str(e)}")
        
    finally:
        cur.close()
        conn.close()

@app.get("/admin/stats")
async def admin_stats(admin_token: str = Header(...)):
    """إحصائيات النظام"""
    
    if admin_token != os.getenv("ADMIN_TOKEN"):
        raise HTTPException(401, "غير مصرح")
    
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    try:
        # إحصائيات اليوم
        cur.execute("""
            SELECT * FROM system_stats 
            WHERE date = %s
        """, (datetime.now().date(),))
        
        today_stats = cur.fetchone() or {}
        
        # إجمالي الأكواد
        cur.execute("""
            SELECT 
                COUNT(*) as total,
                COUNT(CASE WHEN is_active THEN 1 END) as active,
                COUNT(CASE WHEN NOT is_active THEN 1 END) as inactive,
                COUNT(CASE WHEN expires_at < CURRENT_DATE THEN 1 END) as expired
            FROM activation_codes
        """)
        
        codes_stats = cur.fetchone()
        
        # آخر الأكواد المضافة
        cur.execute("""
            SELECT code, created_at, customer_name, plan_type, expires_at
            FROM activation_codes
            ORDER BY created_at DESC
            LIMIT 10
        """)
        
        recent_codes = cur.fetchall()
        
        return {
            "today": today_stats,
            "codes": codes_stats,
            "recent_codes": recent_codes,
            "keys_status": key_manager.get_status(),
            "server_time": datetime.now().isoformat()
        }
        
    finally:
        cur.close()
        conn.close()

# ========== صفحات الويب ==========
@app.get("/dashboard")
async def dashboard_page():
    """لوحة التحكم"""
    return FileResponse("templates/dashboard.html")

@app.get("/activation")
async def activation_page():
    """صفحة التفعيل"""
    return FileResponse("templates/activation.html")

# ========== بدء التشغيل ==========
@app.on_event("startup")
async def startup_event():
    """أحداث بدء التشغيل"""
    print("🚀 بدء تشغيل نظام التقارير التربوية...")
    print(f"🌐 البيئة: {os.getenv('ENVIRONMENT', 'production')}")
    print(f"🔑 المفاتيح المحملة: {len(key_manager.keys)}")
    
    # تهيئة قاعدة البيانات
    init_database()
    
    print("✅ النظام جاهز للاستخدام")
    print(f"📊 حالة المفاتيح: {key_manager.get_status()['active_keys']}/{len(key_manager.keys)} نشطة")

# ========== نقطة الدخول الرئيسية ==========
if __name__ == "__main__":
    import uvicorn
    
    port = int(os.getenv("PORT", 8000))
    
    print("=" * 60)
    print("نظام التقارير التربوية - النسخة التجارية")
    print("معد للنشر على Render.com")
    print("=" * 60)
    print(f"🌐 http://localhost:{port}")
    print("🔒 محمي بأكواد 6 خانات")
    print(f"🔑 {len(key_manager.keys)} مفاتيح Gemini")
    print("=" * 60)
    
    uvicorn.run(app, host="0.0.0.0", port=port)