from datetime import datetime, timedelta
from fastapi import Header, HTTPException
from database import get_connection


def activation_required(x_activation_code: str = Header(...)):
    """
    التحقق من صلاحية كود التفعيل فقط.

    ✅ يبدأ الوقت عند أول تسجيل دخول
    ✅ يتحقق من انتهاء الوقت
    ✅ يتحقق من عدد الاستخدامات
    ❌ لا يخصم الاستخدام هنا
    """

    conn = get_connection()
    cur = conn.cursor()

    # البحث عن الكود
    cur.execute("""
        SELECT
            id,
            is_active,
            started_at,
            expires_at,
            duration_minutes,
            duration_days,
            usage_limit,
            usage_count
        FROM activation_codes
        WHERE code = ?
    """, (x_activation_code,))

    row = cur.fetchone()

    # الكود غير موجود
    if not row:
        conn.close()

        raise HTTPException(
            status_code=403,
            detail="كود التفعيل غير صحيح"
        )

    (
        code_id,
        active,
        started_at,
        expires_at,
        duration_minutes,
        duration_days,
        usage_limit,
        usage_count
    ) = row

    # التحقق من تفعيل الكود
    if not active:
        conn.close()

        raise HTTPException(
            status_code=403,
            detail="تم إيقاف الاشتراك"
        )

    now = datetime.utcnow()

    # ✅ بدء الوقت عند أول تسجيل دخول فقط
    if not started_at:

        delta = timedelta(
            minutes=duration_minutes or 0,
            days=duration_days or 0
        )

        new_expiry = now + delta

        cur.execute("""
            UPDATE activation_codes
            SET
                started_at = ?,
                expires_at = ?
            WHERE id = ?
        """, (
            now.isoformat(),
            new_expiry.isoformat(),
            code_id
        ))

        conn.commit()

        # تحديث القيم محليًا
        started_at = now.isoformat()
        expires_at = new_expiry.isoformat()

    # ✅ التحقق من انتهاء الوقت
    if expires_at:

        expiry_date = datetime.fromisoformat(expires_at)

        if now > expiry_date:
            conn.close()

            raise HTTPException(
                status_code=403,
                detail="انتهت مدة الاشتراك"
            )

    # ✅ التحقق من عدد الاستخدامات
    if usage_limit is not None:

        if usage_count >= usage_limit:
            conn.close()

            raise HTTPException(
                status_code=403,
                detail="تم استهلاك جميع الاستخدامات المسموحة"
            )

    conn.close()

    # نرجع ID الكود لاستخدامه لاحقًا
    return code_id


def consume_usage(code_id):
    """
    خصم استخدام واحد بعد نجاح الطلب الحقيقي
    """

    conn = get_connection()
    cur = conn.cursor()

    # جلب العدد الحالي
    cur.execute("""
        SELECT usage_count
        FROM activation_codes
        WHERE id = ?
    """, (code_id,))

    row = cur.fetchone()

    if not row:
        conn.close()
        return

    current_usage = row[0] or 0

    # تحديث عدد الاستخدامات
    cur.execute("""
        UPDATE activation_codes
        SET
            usage_count = ?,
            last_used_at = ?
        WHERE id = ?
    """, (
        current_usage + 1,
        datetime.utcnow().isoformat(),
        code_id
    ))

    conn.commit()
    conn.close()