# config.py
import os

# إعدادات النظام
class Config:
    # إعدادات الأمان
    ADMIN_TOKEN = os.getenv("ADMIN_TOKEN", "CHANGE_THIS_TO_SECURE_TOKEN")
    
    # مفاتيح Gemini API (يمكنك إضافة ما تريد)
    GEMINI_API_KEYS = [
        os.getenv("GEMINI_API_KEY_1", ""),
        os.getenv("GEMINI_API_KEY_2", ""),
        os.getenv("GEMINI_API_KEY_3", ""),
        os.getenv("GEMINI_API_KEY_4", ""),
        os.getenv("GEMINI_API_KEY_5", ""),
        os.getenv("GEMINI_API_KEY_6", ""),
        os.getenv("GEMINI_API_KEY_7", ""),
    ]
    
    # إعدادات قاعدة البيانات
    DATABASE_PATH = "database.db"
    
    # إعدادات النظام
    MAX_CODE_LENGTH = 50
    MIN_CODE_LENGTH = 10
    DEFAULT_EXPIRY_DAYS = 30
    MAX_USAGE_LIMIT = 1000
    
    # إعدادات السجل
    LOG_SUSPICIOUS_ATTEMPTS = True

# دالة للتحقق من الإعدادات
def validate_config():
    if Config.ADMIN_TOKEN == "CHANGE_THIS_TO_SECURE_TOKEN":
        print("⚠️  تحذير: يجب تغيير ADMIN_TOKEN في config.py")
    
    valid_keys = [k for k in Config.GEMINI_API_KEYS if k]
    if len(valid_keys) == 0:
        print("⚠️  تحذير: لم يتم إضافة أي مفاتيح Gemini API")
    
    return {
        "has_admin_token": Config.ADMIN_TOKEN != "CHANGE_THIS_TO_SECURE_TOKEN",
        "gemini_keys_count": len(valid_keys)
    }