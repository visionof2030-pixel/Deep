# run.py
import os
import subprocess
import sys

def setup_environment():
    """إعداد متغيرات البيئة الضرورية"""
    os.environ['ADMIN_TOKEN'] = 'YOUR_SECURE_ADMIN_TOKEN_HERE'
    os.environ['GEMINI_API_KEY_1'] = 'your_gemini_key_1_here'
    
    print("✅ تم إعداد متغيرات البيئة")

def install_requirements():
    """تثبيت المتطلبات"""
    print("📦 جارٍ تثبيت المتطلبات...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("✅ تم تثبيت المتطلبات")

def init_database():
    """تهيئة قاعدة البيانات"""
    print("🗄️ جارٍ تهيئة قاعدة البيانات...")
    import database
    database.init_db()
    print("✅ قاعدة البيانات جاهزة")

def start_server():
    """تشغيل الخادم"""
    print("🚀 جارٍ تشغيل الخادم...")
    print("📱 افتح المتصفح واذهب إلى: http://localhost:8000")
    print("🔧 لوحة الإدارة: http://localhost:8000/admin")
    print("⏸️  لوقف الخادم: اضغط Ctrl+C")
    
    # تشغيل uvicorn
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    try:
        setup_environment()
        install_requirements()
        init_database()
        start_server()
    except KeyboardInterrupt:
        print("\n🛑 تم إيقاف الخادم")
    except Exception as e:
        print(f"❌ خطأ: {e}")