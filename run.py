#!/usr/bin/env python3
import os
import sys
import subprocess
from datetime import datetime

def setup_environment():
    """إعداد متغيرات البيئة"""
    required_envs = {
        'ADMIN_TOKEN': 'ChangeThisToVerySecureToken@2024',
        'GEMINI_API_KEY_1': 'your_gemini_api_key_here'
    }
    
    for key, default_value in required_envs.items():
        if key not in os.environ:
            os.environ[key] = default_value
            print(f"⚠️  تم تعيين {key} إلى القيمة الافتراضية")

def print_banner():
    """طباعة شعار النظام"""
    banner = """
    ============================================
    🚀 نظام التقارير التربوية - النسخة التجارية
    ============================================
    📌 المميزات:
      • أكواد تفعيل 6 خانات
      • حماية متعددة المستويات
      • جهاز واحد لكل كود
      • مراقبة وتتبع كاملة
    
    🔒 النظام محمي بتفعيل تجاري
    💰 للإصدارات التجارية: تواصل مع المطور
    
    ============================================
    """
    print(banner)

def main():
    """الدالة الرئيسية للتشغيل"""
    
    print_banner()
    setup_environment()
    
    # تشغيل الخادم
    print("🔄 جاري تشغيل الخادم...")
    print("🌐 افتح: http://localhost:8000")
    print("🔧 لوحة الإدارة: http://localhost:8000/admin")
    print("⏸️  اوقف بـ: Ctrl+C")
    print("=" * 50)
    
    try:
        import uvicorn
        import backend
        uvicorn.run("backend:app", host="0.0.0.0", port=8000, reload=True)
    except KeyboardInterrupt:
        print("\n🛑 تم إيقاف النظام")
    except Exception as e:
        print(f"❌ خطأ: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()