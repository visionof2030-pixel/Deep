import sqlite3
import sys

def add_activation_code():
    """
    إضافة كود تفعيل يدوياً إلى قاعدة البيانات
    """
    # الاتصال بقاعدة البيانات
    conn = sqlite3.connect('activation.db')
    cur = conn.cursor()
    
    # إنشاء جدول إذا لم يكن موجوداً
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
    
    # الكود المطلوب إضافته
    activation_code = "cc253d31-4b6e-4abf-a7f3-5104ad38f7c1"  # UUID الخاص بك
    expires_date = "2025-12-31"  # تاريخ انتهاء
    
    print("=" * 50)
    print("إضافة كود التفعيل إلى قاعدة البيانات")
    print("=" * 50)
    print(f"الكود: {activation_code}")
    print(f"تاريخ الانتهاء: {expires_date}")
    print("=" * 50)
    
    try:
        # التحقق أولاً إذا كان الكود موجوداً
        cur.execute("SELECT * FROM activation_codes WHERE code = ?", (activation_code,))
        existing_code = cur.fetchone()
        
        if existing_code:
            print("⚠️  هذا الكود موجود بالفعل في قاعدة البيانات!")
            print(f"   الحالة: {'مفعل' if existing_code[2] else 'معطل'}")
            print(f"   عدد مرات الاستخدام: {existing_code[3]}")
            print(f"   تاريخ الانتهاء: {existing_code[4]}")
            
            # تحديث الكود الموجود ليكون مفعلاً
            cur.execute('''
                UPDATE activation_codes 
                SET is_active = 1, expires_at = ?
                WHERE code = ?
            ''', (expires_date, activation_code))
            print("✅ تم تحديث الكود الموجود ليكون مفعلاً")
        else:
            # إضافة الكود الجديد
            cur.execute('''
                INSERT INTO activation_codes (code, is_active, expires_at) 
                VALUES (?, 1, ?)
            ''', (activation_code, expires_date))
            print("✅ تم إضافة الكود الجديد بنجاح")
        
        # حفظ التغييرات
        conn.commit()
        
        # عرض جميع الأكواد
        print("\n" + "=" * 50)
        print("جميع أكواد التفعيل في قاعدة البيانات:")
        print("=" * 50)
        
        cur.execute("SELECT id, code, is_active, usage_count, expires_at FROM activation_codes ORDER BY created_at DESC")
        all_codes = cur.fetchall()
        
        if all_codes:
            for code in all_codes:
                status = "✅ مفعل" if code[2] else "❌ معطل"
                print(f"ID: {code[0]} | الكود: {code[1]} | {status} | الاستخدام: {code[3]} | الانتهاء: {code[4]}")
        else:
            print("لا توجد أكواد في قاعدة البيانات")
        
        print("=" * 50)
        
    except Exception as e:
        print(f"❌ خطأ: {e}")
        conn.rollback()
    finally:
        conn.close()

def test_activation_code():
    """
    اختبار الكود المضافة
    """
    activation_code = "cc253d31-4b6e-4abf-a7f3-5104ad38f7c1"
    
    conn = sqlite3.connect('activation.db')
    cur = conn.cursor()
    
    try:
        cur.execute('''
            SELECT id, code, is_active, expires_at 
            FROM activation_codes 
            WHERE code = ?
        ''', (activation_code,))
        
        result = cur.fetchone()
        
        if result:
            print("\n" + "=" * 50)
            print("نتيجة اختبار الكود:")
            print("=" * 50)
            print(f"✅ تم العثور على الكود!")
            print(f"   ID: {result[0]}")
            print(f"   الكود: {result[1]}")
            print(f"   الحالة: {'✅ مفعل' if result[2] else '❌ معطل'}")
            print(f"   تاريخ الانتهاء: {result[3]}")
            
            # اختبار نمط UUID
            import re
            uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
            
            if re.match(uuid_pattern, activation_code.lower()):
                print(f"   ✅ نمط UUID صحيح")
            else:
                print(f"   ❌ نمط UUID غير صحيح")
            
        else:
            print("❌ الكود غير موجود في قاعدة البيانات!")
            
    except Exception as e:
        print(f"❌ خطأ في الاختبار: {e}")
    finally:
        conn.close()

def create_test_database():
    """
    إنشاء قاعدة بيانات جديدة للاختبار
    """
    import os
    
    # حذف ملف قاعدة البيانات القديم إذا كان موجوداً
    if os.path.exists('activation.db'):
        backup_name = f"activation_backup_{os.path.getmtime('activation.db')}.db"
        os.rename('activation.db', backup_name)
        print(f"⚠️  تم نسخ قاعدة البيانات القديمة إلى: {backup_name}")
    
    # إنشاء قاعدة بيانات جديدة
    conn = sqlite3.connect('activation.db')
    cur = conn.cursor()
    
    # إنشاء الجدول
    cur.execute('''
        CREATE TABLE activation_codes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT UNIQUE NOT NULL,
            is_active BOOLEAN DEFAULT 1,
            usage_count INTEGER DEFAULT 0,
            expires_at TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # إضافة بعض الأكواد الاختبارية
    test_codes = [
        ("cc253d31-4b6e-4abf-a7f3-5104ad38f7c1", "2025-12-31"),
        ("test-uuid-code-1234567890abcdef", "2024-12-31"),
        ("another-test-uuid-for-validation", "2026-06-30")
    ]
    
    for code, expires in test_codes:
        cur.execute('''
            INSERT INTO activation_codes (code, is_active, expires_at) 
            VALUES (?, 1, ?)
        ''', (code, expires))
    
    conn.commit()
    conn.close()
    
    print("✅ تم إنشاء قاعدة بيانات جديدة للاختبار")
    print("✅ تم إضافة 3 أكواد اختبارية")

if __name__ == "__main__":
    print("أداة إدارة أكواد التفعيل")
    print("=" * 50)
    print("1. إضافة كود التفعيل الرئيسي")
    print("2. اختبار الكود المضاف")
    print("3. إنشاء قاعدة بيانات جديدة للاختبار")
    print("4. الخروج")
    
    choice = input("\nاختر الخيار (1-4): ").strip()
    
    if choice == "1":
        add_activation_code()
    elif choice == "2":
        test_activation_code()
    elif choice == "3":
        create_test_database()
    elif choice == "4":
        print("إلى اللقاء!")
    else:
        print("❌ خيار غير صحيح")
    
    input("\nاضغط Enter للخروج...")