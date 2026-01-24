# key_logic.py
from datetime import datetime
import hashlib
import re
from fastapi import HTTPException, Request
from database import get_connection

def verify_code(code: str, request: Request = None):
    """
    التحقق من صحة كود التفعيل مع تعزيزات أمنية
    """
    # 1. التحقق الأساسي من صحة تنسيق الكود
    if not is_valid_code_format(code):
        raise HTTPException(status_code=401, detail="تنسيق الكود غير صالح")
    
    conn = get_connection()
    cur = conn.cursor()
    
    # 2. البحث عن الكود
    cur.execute(
        """
        SELECT id, is_active, expires_at, max_uses, used_count 
        FROM activation_codes 
        WHERE code = ?
        """,
        (code,)
    )
    row = cur.fetchone()
    
    if not row:
        log_suspicious_attempt(code, request, "كود غير موجود")
        raise HTTPException(status_code=401, detail="كود التفعيل غير صالح")
    
    code_id, is_active, expires_at, max_uses, used_count = row
    
    # 3. التحقق من حالة التفعيل
    if not is_active:
        log_suspicious_attempt(code, request, "كود معطل")
        raise HTTPException(status_code=401, detail="كود التفعيل معطل")
    
    # 4. التحقق من تاريخ الانتهاء
    if expires_at:
        try:
            expiry_date = datetime.strptime(expires_at, '%Y-%m-%d')
            current_date = datetime.now()
            
            if current_date > expiry_date:
                # تحديث حالة الكود إلى غير فعال عند انتهاء الصلاحية
                cur.execute(
                    "UPDATE activation_codes SET is_active = 0 WHERE id = ?",
                    (code_id,)
                )
                conn.commit()
                log_suspicious_attempt(code, request, "كود منتهي الصلاحية")
                raise HTTPException(status_code=401, detail="كود التفعيل منتهي الصلاحية")
        except ValueError:
            # في حالة خطأ في تنسيق التاريخ
            log_suspicious_attempt(code, request, "تاريخ غير صالح في قاعدة البيانات")
            raise HTTPException(status_code=401, detail="خطأ في بيانات الكود")
    
    # 5. التحقق من حد الاستخدام
    if max_uses is not None and used_count >= max_uses:
        log_suspicious_attempt(code, request, f"تجاوز حد الاستخدام ({used_count}/{max_uses})")
        raise HTTPException(status_code=401, detail="تم تجاوز عدد مرات الاستخدام المسموح بها")
    
    # 6. زيادة عداد الاستخدام وتحديث وقت الاستخدام
    cur.execute(
        """
        UPDATE activation_codes 
        SET used_count = used_count + 1, 
            last_used_at = ?
        WHERE id = ?
        """,
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), code_id)
    )
    
    # 7. تسجيل الاستخدام في السجل
    if request:
        device_hash = generate_device_hash(request)
        ip_address = get_client_ip(request)
        
        cur.execute(
            """
            INSERT INTO code_usage_log (code_id, device_hash, ip_address, usage_time)
            VALUES (?, ?, ?, ?)
            """,
            (code_id, device_hash, ip_address, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        )
    
    conn.commit()
    conn.close()

def is_valid_code_format(code: str) -> bool:
    """التحقق من تنسيق الكود (يجب أن يكون نصاً وليس فارغاً)"""
    if not code or not isinstance(code, str):
        return False
    
    # طول معقول للكود (بين 10 و 50 حرف)
    if len(code) < 10 or len(code) > 50:
        return False
    
    # يسمح بحروف وأرقام وشرطات فقط
    if not re.match(r'^[A-Za-z0-9\-_]+$', code):
        return False
    
    return True

def generate_device_hash(request: Request) -> str:
    """إنشاء بصمة فريدة للجهاز"""
    user_agent = request.headers.get('user-agent', '')
    accept_language = request.headers.get('accept-language', '')
    
    # دمج المعلومات وإنشاء هاش
    device_info = f"{user_agent}:{accept_language}"
    return hashlib.sha256(device_info.encode()).hexdigest()[:32]

def get_client_ip(request: Request) -> str:
    """الحصول على IP العميل"""
    if request.client:
        return request.client.host
    return "unknown"

def log_suspicious_attempt(code: str, request: Request, reason: str):
    """تسجيل محاولات الاشتباه"""
    if request:
        ip = get_client_ip(request)
        print(f"[SUSPICIOUS] Code: {code[:10]}..., IP: {ip}, Reason: {reason}")
    else:
        print(f"[SUSPICIOUS] Code: {code[:10]}..., Reason: {reason}")

def check_code_status(code: str):
    """فحص حالة الكود (للواجهة الإدارية)"""
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute(
        """
        SELECT 
            code,
            is_active,
            expires_at,
            max_uses,
            used_count,
            created_at,
            last_used_at,
            CASE 
                WHEN expires_at IS NOT NULL AND date(expires_at) < date('now') THEN 'منتهي'
                WHEN is_active = 0 THEN 'معطل'
                WHEN max_uses IS NOT NULL AND used_count >= max_uses THEN 'مستهلك'
                ELSE 'نشط'
            END as status
        FROM activation_codes 
        WHERE code = ?
        """,
        (code,)
    )
    
    row = cur.fetchone()
    conn.close()
    
    if not row:
        return None
    
    return {
        'code': row[0],
        'is_active': bool(row[1]),
        'expires_at': row[2],
        'max_uses': row[3],
        'used_count': row[4],
        'created_at': row[5],
        'last_used_at': row[6],
        'status': row[7]
    }