from fastapi import HTTPException, Header, Request
from database import get_connection
from datetime import datetime

async def activation_required(
    request: Request,
    x_activation_code: str = Header(...)
):
    """
    متوسّط للتحقق من صحة كود التفعيل
    """
    # التحقق من وجود الكود في الطلب
    if not x_activation_code:
        raise HTTPException(
            status_code=401,
            detail="كود التفعيل مطلوب"
        )
    
    # تنظيف الكود
    code = x_activation_code.strip().lower()
    
    # التحقق من نمط UUID
    import re
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
    
    if not re.match(uuid_pattern, code):
        raise HTTPException(
            status_code=400,
            detail="تنسيق كود التفعيل غير صحيح"
        )
    
    # التحقق من قاعدة البيانات
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        cur.execute(
            "SELECT id, is_active, expires_at FROM activation_codes WHERE code = ?",
            (code,)
        )
        row = cur.fetchone()
        
        if not row:
            raise HTTPException(
                status_code=404,
                detail="كود التفعيل غير موجود"
            )
        
        code_id, is_active, expires_at = row
        
        # التحقق من حالة التنشيط
        if not is_active:
            raise HTTPException(
                status_code=403,
                detail="كود التفعيل غير مفعل"
            )
        
        # التحقق من تاريخ الانتهاء
        if expires_at:
            expires_date = datetime.strptime(expires_at, "%Y-%m-%d")
            if datetime.now() > expires_date:
                raise HTTPException(
                    status_code=403,
                    detail="كود التفعيل منتهي الصلاحية"
                )
        
        # تسجيل استخدام الكود
        cur.execute(
            "UPDATE activation_codes SET usage_count = usage_count + 1 WHERE id = ?",
            (code_id,)
        )
        conn.commit()
        
        # إضافة معلومات الكود إلى حالة الطلب
        request.state.activation_code = code
        request.state.activation_code_id = code_id
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"خطأ في التحقق: {str(e)}"
        )
    finally:
        conn.close()
    
    return True