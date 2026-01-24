# database.py
import sqlite3
from datetime import datetime

DATABASE = "database.db"

def get_connection():
    return sqlite3.connect(DATABASE, check_same_thread=False)

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    
    # جدول الأكواد الرئيسي - موحد ومحسن
    cur.execute("""
    CREATE TABLE IF NOT EXISTS activation_codes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT UNIQUE NOT NULL,
        is_active INTEGER DEFAULT 1,
        max_uses INTEGER DEFAULT 1,
        used_count INTEGER DEFAULT 0,
        expires_at TEXT,  -- تاريخ الانتهاء بصيغة YYYY-MM-DD
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        last_used_at TEXT,
        customer_email TEXT,
        customer_name TEXT
    )
    """)
    
    # جدول سجل الاستخدامات
    cur.execute("""
    CREATE TABLE IF NOT EXISTS code_usage_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code_id INTEGER NOT NULL,
        device_hash TEXT,
        ip_address TEXT,
        usage_time TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (code_id) REFERENCES activation_codes (id)
    )
    """)
    
    conn.commit()
    conn.close()