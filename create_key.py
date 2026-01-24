# create_key.py
import uuid
import re
from datetime import datetime, timedelta
from database import get_connection

def create_key(expires_at=None, usage_limit=None, days_valid=30):
    """
    إنشاء كود تفعيل جديد مع صلاحية
    Args:
        expires_at: تاريخ انتهاء محدد (YYYY-MM-DD)
        usage_limit: عدد مرات الاستخدام (إذا لم يتم تحديد، يستخدم القيمة الافتراضية)
        days_valid: عدد الأيام الصالحة إذا لم يتم تحديد تاريخ
    """
    code = generate_secure_code()
    
    conn = get_connection()
    cur = conn.cursor()
    
    # معالجة تاريخ الانتهاء
    if expires_at:
        # التحقق من صحة التاريخ
        if not validate_date_format(expires_at):
            raise ValueError("تنسيق التاريخ غير صحيح. استخدم YYYY-MM-DD")
        expiry_date = expires_at
    else:
        # تاريخ افتراضي بعد X يوم
        expiry_date = (datetime.now() + timedelta(days=days_valid)).strftime('%Y-%m-%d')
    
    # معالجة حد الاستخدام
    max_uses = int(usage_limit) if usage_limit else 1
    
    # إدخال الكود
    cur.execute(
        """
        INSERT INTO activation_codes 
        (code, is_active, max_uses, used_count, expires_at, created_at)
        VALUES (?, 1, ?, 0, ?, ?)
        """,
        (
            code,
            max_uses,
            expiry_date,
            datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )
    )
    
    conn.commit()
    conn.close()
    return code

def generate_secure_code():
    """إنشاء كود آمن عشوائي"""
    code = str(uuid.uuid4()).replace('-', '')[:20].upper()
    # إضافة بعض الأرقام للتأكد من القوة
    import random
    code = code + str(random.randint(10, 99))
    return code

def validate_date_format(date_str):
    """التحقق من صحة تنسيق التاريخ"""
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    if not re.match(pattern, date_str):
        return False
    
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False