# -*- coding: utf-8 -*-

# =========================
# المعايير الرئيسية (الجدارات القيادية) لمدير المدرسة
# =========================

PRINCIPAL_CRITERIA = [
    {"id": "sp_c1", "name": "المسؤولية", "order": 1},
    {"id": "sp_c2", "name": "العمل الجماعي", "order": 2},
    {"id": "sp_c3", "name": "المرونة والتكيف مع التغيير", "order": 3},
    {"id": "sp_c4", "name": "المبادرة", "order": 4},
    {"id": "sp_c5", "name": "قيادة التغيير", "order": 5},
    {"id": "sp_c6", "name": "تطوير وتمكين العاملين", "order": 6},
    {"id": "sp_c7", "name": "التوجه الاستراتيجي", "order": 7},
    {"id": "sp_c8", "name": "اتخاذ القرارات", "order": 8}
]

# =========================
# التصنيفات الفرعية
# =========================

PRINCIPAL_SUBCATEGORIES = [
    {"id": "sp_c1_s1", "criterion_id": "sp_c1", "name": "تحمل المسؤولية عن النتائج", "order": 1},
    {"id": "sp_c1_s2", "criterion_id": "sp_c1", "name": "الالتزام بتحقيق الأهداف في الوقت المحدد", "order": 2},
    {"id": "sp_c1_s3", "criterion_id": "sp_c1", "name": "الالتزام بمعايير الجودة المهنية", "order": 3},

    {"id": "sp_c2_s1", "criterion_id": "sp_c2", "name": "تعزيز روح الفريق", "order": 1},
    {"id": "sp_c2_s2", "criterion_id": "sp_c2", "name": "بناء علاقات مهنية إيجابية", "order": 2},
    {"id": "sp_c2_s3", "criterion_id": "sp_c2", "name": "إدارة الخلافات بموضوعية", "order": 3},

    {"id": "sp_c3_s1", "criterion_id": "sp_c3", "name": "الاستجابة للمتغيرات", "order": 1},
    {"id": "sp_c3_s2", "criterion_id": "sp_c3", "name": "تقبل وجهات النظر المختلفة", "order": 2},
    {"id": "sp_c3_s3", "criterion_id": "sp_c3", "name": "تعديل الخطط وفق المستجدات", "order": 3},

    {"id": "sp_c4_s1", "criterion_id": "sp_c4", "name": "اقتراح أفكار تطويرية", "order": 1},
    {"id": "sp_c4_s2", "criterion_id": "sp_c4", "name": "استباق المشكلات", "order": 2},
    {"id": "sp_c4_s3", "criterion_id": "sp_c4", "name": "تنفيذ حلول مبتكرة", "order": 3},

    {"id": "sp_c5_s1", "criterion_id": "sp_c5", "name": "إدارة عمليات التطوير المؤسسي", "order": 1},
    {"id": "sp_c5_s2", "criterion_id": "sp_c5", "name": "تحفيز العاملين لتبني التغيير", "order": 2},
    {"id": "sp_c5_s3", "criterion_id": "sp_c5", "name": "معالجة مقاومة التغيير", "order": 3},
    {"id": "sp_c5_s4", "criterion_id": "sp_c5", "name": "تحقيق الرؤية الاستراتيجية", "order": 4},

    {"id": "sp_c6_s1", "criterion_id": "sp_c6", "name": "تحديد الاحتياجات المهنية", "order": 1},
    {"id": "sp_c6_s2", "criterion_id": "sp_c6", "name": "دعم النمو الوظيفي", "order": 2},
    {"id": "sp_c6_s3", "criterion_id": "sp_c6", "name": "تفويض الصلاحيات بفاعلية", "order": 3},
    {"id": "sp_c6_s4", "criterion_id": "sp_c6", "name": "إعداد قيادات بديلة", "order": 4},

    {"id": "sp_c7_s1", "criterion_id": "sp_c7", "name": "تحليل المؤشرات والبيانات", "order": 1},
    {"id": "sp_c7_s2", "criterion_id": "sp_c7", "name": "استشراف التحديات المستقبلية", "order": 2},
    {"id": "sp_c7_s3", "criterion_id": "sp_c7", "name": "مواءمة الخطط مع الأهداف الوطنية", "order": 3},
    {"id": "sp_c7_s4", "criterion_id": "sp_c7", "name": "بناء خطط طويلة المدى قابلة للقياس", "order": 4},

    {"id": "sp_c8_s1", "criterion_id": "sp_c8", "name": "دراسة البدائل المتاحة", "order": 1},
    {"id": "sp_c8_s2", "criterion_id": "sp_c8", "name": "المفاضلة بين الحلول", "order": 2},
    {"id": "sp_c8_s3", "criterion_id": "sp_c8", "name": "اتخاذ قرارات مبنية على معايير واضحة", "order": 3},
    {"id": "sp_c8_s4", "criterion_id": "sp_c8", "name": "تحمل مسؤولية نتائج القرار", "order": 4}
]

# =========================
# التقارير
# =========================

PRINCIPAL_REPORTS = [
    {"id": "sp_r001", "subcategory_id": "sp_c1_s1", "name": "تقرير تحمل المسؤولية عن النتائج المدرسية", "order": 1},
    {"id": "sp_r002", "subcategory_id": "sp_c2_s1", "name": "تقرير تعزيز روح الفريق بين العاملين", "order": 1},
    {"id": "sp_r003", "subcategory_id": "sp_c5_s1", "name": "تقرير إدارة عمليات التطوير المؤسسي", "order": 1},
    {"id": "sp_r004", "subcategory_id": "sp_c7_s1", "name": "تقرير تحليل المؤشرات والبيانات", "order": 1},
    {"id": "sp_r005", "subcategory_id": "sp_c8_s3", "name": "تقرير اتخاذ قرارات مبنية على معايير واضحة", "order": 1}
]

# =========================
# قالب البرومبت
# =========================

PRINCIPAL_PROMPT_TEMPLATE = """أنت مدير مدرسة خبير وقائد تربوي، مسؤول عن تحقيق الرؤية الاستراتيجية وقيادة عمليات التطوير المؤسسي وتمكين العاملين.

التقرير المطلوب: "{report_name}"
يندرج تحت التصنيف الفرعي: "{subcategory_name}"
ضمن الجدارة القيادية: "{criterion_name}"

{subject_line}
{lesson_line}
{grade_line}
{target_line}
{place_line}
{count_line}

اكتب تقريرًا قياديًا يتضمن:

1. الهدف القيادي
2. نبذة مختصرة
3. إجراءات التنفيذ
4. الاستراتيجيات والأساليب القيادية
5. نقاط القوة
6. نقاط التحسين
7. التوصيات

ضوابط:
- لغة قيادية رسمية واستراتيجية.
- إبراز دور القيادة في التخطيط والتنظيم والمتابعة.
- توضيح أثر القرارات على تحسين الأداء المدرسي.
- كل بند يبدأ برقمه فقط دون كتابة عنوانه.
"""