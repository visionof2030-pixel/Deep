# security.py
from fastapi import Header, HTTPException
from database import get_connection
from datetime import datetime

def activation_required(
    x_activation_code: str = Header(...),
    x_device_id: str = Header(...)
):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, is_active, expires_at, usage_limit, usage_count, device_id
        FROM activation_codes
        WHERE code=?
    """, (x_activation_code,))
    row = cur.fetchone()

    if not row:
        conn.close()
        raise HTTPException(status_code=401, detail="Invalid code")

    code_id, active, expires, limit, used, device_id = row

    if not active:
        conn.close()
        raise HTTPException(status_code=401, detail="Code disabled")

    if expires and datetime.fromisoformat(expires) < datetime.utcnow():
        conn.close()
        raise HTTPException(status_code=401, detail="Code expired")

    if device_id is None:
        cur.execute(
            "UPDATE activation_codes SET device_id=? WHERE id=?",
            (x_device_id, code_id)
        )
        conn.commit()
    elif device_id != x_device_id:
        conn.close()
        raise HTTPException(status_code=401, detail="Code already used on another device")

    if limit and used >= limit:
        conn.close()
        raise HTTPException(status_code=401, detail="Usage limit reached")

    cur.execute(
        "UPDATE activation_codes SET usage_count = usage_count + 1 WHERE id=?",
        (code_id,)
    )
    conn.commit()
    conn.close()