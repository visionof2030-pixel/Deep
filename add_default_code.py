import sqlite3
import os

def add_default_codes():
    """إضافة أكواد تفعيل افتراضية"""
    
    # قم بتغيير هذه القائمة لأكوادك الخاصة
    DEFAULT_CODES = [
        ("cc253d31-4b6e-4abf-a7f3-5104ad38f7c1", "2025-12-31"),
        ("12345678-1234-1234-1234-123456789abc", "2025-06-30"),
        ("abcdef12-3456-7890-abcd-ef1234567890", "2026-01-01")
    ]
    
    conn = sqlite3.connect('activation.db')
    cur = conn.cursor()
    
    print("=" * 60)
    print("إضافة أكواد التفعيل الافتراضية")
    print("=" * 60)
    
    added_codes = []
    
    for code, expires_at in DEFAULT_CODES:
        try:
            # التحقق إذا كان الكود موجوداً
            cur.execute("SELECT id FROM activation_codes WHERE code = ?", (code,))
            if cur.fetchone():
                print(f"⚠️  الكود موجود بالفعل: {code}")
                continue
            
            # إضافة الكود الجديد
            cur.execute('''
                INSERT INTO activation_codes (code, is_active, expires_at) 
                VALUES (?, 1, ?)
            ''', (code.lower(), expires_at))
            
            added_codes.append(code)
            print(f"✅ تم إضافة: {code}")
            
        except Exception as e:
            print(f"❌ خطأ في إضافة {code}: {e}")
    
    conn.commit()
    
    # عرض جميع الأكواد
    print("\n" + "=" * 60)
    print("جميع أكواد التفعيل في قاعدة البيانات:")
    print("=" * 60)
    
    cur.execute("SELECT code, is_active, expires_at FROM activation_codes ORDER BY created_at DESC")
    all_codes = cur.fetchall()
    
    for code in all_codes:
        status = "✅ مفعل" if code[1] else "❌ معطل"
        print(f"{status} | {code[0]} | ينتهي: {code[2]}")
    
    print("=" * 60)
    print(f"✅ تم إضافة {len(added_codes)} أكواد جديدة")
    
    conn.close()

def test_connection():
    """اختبار اتصال قاعدة البيانات"""
    try:
        conn = sqlite3.connect('activation.db')
        cur = conn.cursor()
        
        # اختبار الاستعلام
        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cur.fetchall()
        
        print("\n📊 جداول قاعدة البيانات:")
        for table in tables:
            print(f"  - {table[0]}")
        
        # عد الأكواد
        cur.execute("SELECT COUNT(*) FROM activation_codes")
        count = cur.fetchone()[0]
        print(f"\n📊 عدد أكواد التفعيل: {count}")
        
        conn.close()
        return True
    except Exception as e:
        print(f"❌ خطأ في الاتصال: {e}")
        return False

if __name__ == "__main__":
    print("🔧 إعداد قاعدة البيانات للأكواد الافتراضية")
    
    # اختبار الاتصال
    if test_connection():
        # إضافة الأكواد
        add_default_codes()
        
        print("\n🎯 اختبار الوصول إلى الأكواد:")
        conn = sqlite3.connect('activation.db')
        cur = conn.cursor()
        
        test_code = "cc253d31-4b6e-4abf-a7f3-5104ad38f7c1"
        cur.execute("SELECT * FROM activation_codes WHERE code = ?", (test_code.lower(),))
        result = cur.fetchone()
        
        if result:
            print(f"✅ الكود {test_code} موجود وجاهز للاستخدام")
            print(f"   الحالة: {'مفعل' if result[2] else 'معطل'}")
            print(f"   عدد مرات الاستخدام: {result[3]}")
            print(f"   تاريخ الانتهاء: {result[4]}")
        else:
            print(f"❌ الكود {test_code} غير موجود")
        
        conn.close()
    else:
        print("❌ فشل في الاتصال بقاعدة البيانات")
    
    input("\nاضغط Enter للخروج...")