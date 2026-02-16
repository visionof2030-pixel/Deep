import sqlite3
import os
from datetime import datetime

DB_PATH = "/tmp/database.db"

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def init_db():
    os.makedirs("/tmp", exist_ok=True)
    conn = get_connection()
    cur = conn.cursor()

    # إنشاء الجدول بالهيكل الجديد (إذا لم يكن موجوداً)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS activation_codes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT UNIQUE,
        is_active INTEGER,
        created_at TEXT,
        started_at TEXT,
        expires_at TEXT,
        duration_minutes INTEGER,
        duration_days INTEGER,
        usage_limit INTEGER,
        usage_count INTEGER,
        last_used_at TEXT
    )
    """)

    # ترقية الجداول القديمة: إضافة الأعمدة الجديدة إذا لم تكن موجودة
    try:
        cur.execute("ALTER TABLE activation_codes ADD COLUMN started_at TEXT")
    except sqlite3.OperationalError:
        pass  # العمود موجود مسبقاً

    try:
        cur.execute("ALTER TABLE activation_codes ADD COLUMN duration_minutes INTEGER")
    except sqlite3.OperationalError:
        pass

    try:
        cur.execute("ALTER TABLE activation_codes ADD COLUMN duration_days INTEGER")
    except sqlite3.OperationalError:
        pass

    conn.commit()
    conn.close()