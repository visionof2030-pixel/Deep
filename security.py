# security.py
from fastapi import Header, Depends, Request
from key_logic import verify_code

def activation_required(
    request: Request,
    x_activation_code: str = Header(...)
):
    """
    اعتماد تحقق من التفعيل مع تسجيل معلومات الطلب
    """
    verify_code(x_activation_code, request)