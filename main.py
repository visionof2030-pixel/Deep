# key_rotator.py - نظام تدوير المفاتيح السبعة
import os
import time
import hashlib
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import itertools
import random

class GeminiKeyRotator:
    """مدير تدوير المفاتيح السبعة للاستخدام الأمثل"""
    
    def __init__(self):
        self.keys = self.load_keys()
        self.key_stats = self.initialize_stats()
        self.current_index = 0
        self.key_cycle = itertools.cycle(range(len(self.keys)))
        
    def load_keys(self) -> List[str]:
        """تحميل المفاتيح السبعة من متغيرات البيئة"""
        keys = []
        for i in range(1, 8):  # من 1 إلى 7
            key = os.getenv(f"GEMINI_API_KEY_{i}", "").strip()
            if key and len(key) > 10:  # التحقق من صحة المفتاح
                keys.append(key)
        
        if len(keys) == 0:
            print("⚠️  تحذير: لم يتم العثور على أي مفاتيح Gemini API")
            return [""]
        
        print(f"✅ تم تحميل {len(keys)} مفاتيح Gemini API")
        return keys
    
    def initialize_stats(self) -> Dict[int, Dict]:
        """تهيئة إحصائيات المفاتيح"""
        stats = {}
        for i in range(len(self.keys)):
            stats[i] = {
                'total_requests': 0,
                'failed_requests': 0,
                'last_used': None,
                'daily_requests': 0,
                'last_reset': datetime.now().date(),
                'is_active': True,
                'consecutive_failures': 0,
                'average_response_time': 0,
                'last_response_times': []
            }
        return stats
    
    def get_next_key(self) -> str:
        """الحصول على المفتاح التالي مع تدوير ذكي"""
        
        # 1. التحقق من إعادة تعيين العداد اليومي
        self.reset_daily_counts_if_needed()
        
        # 2. اختيار المفتاح الأمثل
        key_index = self.select_optimal_key()
        
        # 3. تحديث الإحصائيات
        self.update_stats(key_index, 'selected')
        
        # 4. إرجاع المفتاح
        return self.keys[key_index]
    
    def select_optimal_key(self) -> int:
        """اختيار المفتاح الأمثل بناءً على الإحصائيات"""
        
        active_keys = []
        for idx, stats in self.key_stats.items():
            if (stats['is_active'] and 
                stats['daily_requests'] < 1500 and  # الحد اليومي 1500 طلب
                (stats['consecutive_failures'] < 3 or 
                 (datetime.now() - (stats['last_used'] or datetime.min)).seconds > 300)):
                active_keys.append(idx)
        
        if not active_keys:
            # إذا لم توجد مفاتيح نشطة، أعد تفعيل الجميع
            self.reactivate_all_keys()
            active_keys = list(self.key_stats.keys())
        
        # اختيار المفتاح الذي له أقل استخدام اليومي
        selected_key = min(active_keys, 
                          key=lambda x: self.key_stats[x]['daily_requests'])
        
        return selected_key
    
    def reset_daily_counts_if_needed(self):
        """إعادة تعيين العدادات اليومية إذا مر يوم"""
        today = datetime.now().date()
        for idx, stats in self.key_stats.items():
            if stats['last_reset'] != today:
                stats['daily_requests'] = 0
                stats['consecutive_failures'] = 0
                stats['last_reset'] = today
    
    def update_stats(self, key_index: int, action: str, response_time: float = None):
        """تحديث إحصائيات المفتاح"""
        stats = self.key_stats[key_index]
        
        if action == 'selected':
            stats['total_requests'] += 1
            stats['daily_requests'] += 1
            stats['last_used'] = datetime.now()
            
        elif action == 'success':
            stats['consecutive_failures'] = 0
            if response_time:
                stats['last_response_times'].append(response_time)
                if len(stats['last_response_times']) > 10:
                    stats['last_response_times'].pop(0)
                if stats['last_response_times']:
                    stats['average_response_time'] = sum(stats['last_response_times']) / len(stats['last_response_times'])
        
        elif action == 'failure':
            stats['failed_requests'] += 1
            stats['consecutive_failures'] += 1
            
            # إذا فشل المفتاح 3 مرات متتالية، عطله مؤقتاً
            if stats['consecutive_failures'] >= 3:
                stats['is_active'] = False
                print(f"⚠️  تم تعطيل المفتاح {key_index+1} مؤقتاً بسبب 3 فشل متتالي")
    
    def reactivate_all_keys(self):
        """إعادة تفعيل جميع المفاتيح"""
        for idx in self.key_stats:
            self.key_stats[idx]['is_active'] = True
            self.key_stats[idx]['consecutive_failures'] = 0
    
    def get_key_status(self) -> Dict:
        """الحصول على حالة جميع المفاتيح"""
        status = {}
        for i in range(len(self.keys)):
            stats = self.key_stats[i]
            status[f'key_{i+1}'] = {
                'is_active': stats['is_active'],
                'daily_requests': stats['daily_requests'],
                'total_requests': stats['total_requests'],
                'failed_requests': stats['failed_requests'],
                'last_used': stats['last_used'].isoformat() if stats['last_used'] else None,
                'remaining_requests': max(0, 1500 - stats['daily_requests']),
                'consecutive_failures': stats['consecutive_failures'],
                'average_response_time': stats['average_response_time']
            }
        return status
    
    def get_available_requests(self) -> int:
        """الحصول على عدد الطلبات المتاحة اليوم"""
        total_available = 0
        for stats in self.key_stats.values():
            total_available += max(0, 1500 - stats['daily_requests'])
        return total_available

# إنشاء مثول عالمي للمدول
key_rotator = GeminiKeyRotator()