import sqlite3
import os

DATABASE_FILE = "activation.db"

def get_connection():
    """الحصول على اتصال بقاعدة البيانات"""
    conn = sqlite3.connect(DATABASE_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """تهيئة قاعدة البيانات"""
    conn = get_connection()
    cur = conn.cursor()
    
    # إنشاء جدول أكواد التفعيل
    cur.execute('''
        CREATE TABLE IF NOT EXISTS activation_codes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT UNIQUE NOT NULL,
            is_active BOOLEAN DEFAULT 1,
            usage_count INTEGER DEFAULT 0,
            expires_at TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # إنشاء جدول لتسجيل استخدام الأكواد
    cur.execute('''
        CREATE TABLE IF NOT EXISTS code_usage_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code_id INTEGER NOT NULL,
            ip_address TEXT,
            user_agent TEXT,
            endpoint TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (code_id) REFERENCES activation_codes (id)
        )
    ''')
    
    # إنشاء جدول لتسجيل المحاولات الفاشلة
    cur.execute('''
        CREATE TABLE IF NOT EXISTS failed_attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip_address TEXT NOT NULL,
            code_attempted TEXT,
            user_agent TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    
    print(f"✅ قاعدة البيانات '{DATABASE_FILE}' جاهزة")

def log_code_usage(code_id, ip_address, user_agent, endpoint):
    """تسجيل استخدام الكود"""
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute('''
        INSERT INTO code_usage_log (code_id, ip_address, user_agent, endpoint)
        VALUES (?, ?, ?, ?)
    ''', (code_id, ip_address, user_agent, endpoint))
    
    conn.commit()
    conn.close()

def log_failed_attempt(ip_address, code_attempted, user_agent):
    """تسجيل محاولة فاشلة"""
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute('''
        INSERT INTO failed_attempts (ip_address, code_attempted, user_agent)
        VALUES (?, ?, ?)
    ''', (ip_address, code_attempted, user_agent))
    
    conn.commit()
    conn.close()

def get_failed_attempts_count(ip_address, hours=24):
    """الحصول على عدد المحاولات الفاشلة في الساعات المحددة"""
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute('''
        SELECT COUNT(*) as count
        FROM failed_attempts
        WHERE ip_address = ? 
        AND created_at >= datetime('now', ?)
    ''', (ip_address, f'-{hours} hours'))
    
    result = cur.fetchone()
    conn.close()
    
    return result['count'] if result else 0