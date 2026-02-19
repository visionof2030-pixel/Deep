# -*- coding: utf-8 -*-

# قائمة المعايير الرئيسية (الجدارات القيادية) لمدير المدرسة
SP_CRITERIA = [
    {"id": "sp_c1", "name": "المسؤولية", "order": 1},
    {"id": "sp_c2", "name": "العمل الجماعي", "order": 2},
    {"id": "sp_c3", "name": "المرونة والتكيف مع التغيير", "order": 3},
    {"id": "sp_c4", "name": "المبادرة", "order": 4},
    {"id": "sp_c5", "name": "قيادة التغيير", "order": 5},
    {"id": "sp_c6", "name": "تطوير وتمكين العاملين", "order": 6},
    {"id": "sp_c7", "name": "التوجه الاستراتيجي", "order": 7},
    {"id": "sp_c8", "name": "اتخاذ القرارات", "order": 8}
]

# التصنيفات الفرعية للمدير (نفس الجدارات ولكن بصيغة قيادية)
SP_SUBCATEGORIES = [
    # sp_c1
    {"id": "sp_c1_s1", "criterion_id": "sp_c1", "name": "تحمل المسؤولية عن النتائج", "order": 1},
    {"id": "sp_c1_s2", "criterion_id": "sp_c1", "name": "الالتزام بتحقيق الأهداف في الوقت المحدد", "order": 2},
    {"id": "sp_c1_s3", "criterion_id": "sp_c1", "name": "الالتزام بمعايير الجودة المهنية", "order": 3},
    # sp_c2
    {"id": "sp_c2_s1", "criterion_id": "sp_c2", "name": "تعزيز روح الفريق", "order": 1},
    {"id": "sp_c2_s2", "criterion_id": "sp_c2", "name": "بناء علاقات مهنية إيجابية", "order": 2},
    {"id": "sp_c2_s3", "criterion_id": "sp_c2", "name": "إدارة الخلافات بموضوعية", "order": 3},
    # sp_c3
    {"id": "sp_c3_s1", "criterion_id": "sp_c3", "name": "الاستجابة للمتغيرات", "order": 1},
    {"id": "sp_c3_s2", "criterion_id": "sp_c3", "name": "تقبل وجهات النظر المختلفة", "order": 2},
    {"id": "sp_c3_s3", "criterion_id": "sp_c3", "name": "تعديل الخطط وفق المستجدات", "order": 3},
    # sp_c4
    {"id": "sp_c4_s1", "criterion_id": "sp_c4", "name": "اقتراح أفكار تطويرية", "order": 1},
    {"id": "sp_c4_s2", "criterion_id": "sp_c4", "name": "استباق المشكلات", "order": 2},
    {"id": "sp_c4_s3", "criterion_id": "sp_c4", "name": "تنفيذ حلول مبتكرة", "order": 3},
    # sp_c5
    {"id": "sp_c5_s1", "criterion_id": "sp_c5", "name": "إدارة عمليات التطوير المؤسسي", "order": 1},
    {"id": "sp_c5_s2", "criterion_id": "sp_c5", "name": "تحفيز العاملين لتبني التغيير", "order": 2},
    {"id": "sp_c5_s3", "criterion_id": "sp_c5", "name": "معالجة مقاومة التغيير", "order": 3},
    {"id": "sp_c5_s4", "criterion_id": "sp_c5", "name": "تحقيق الرؤية الاستراتيجية", "order": 4},
    # sp_c6
    {"id": "sp_c6_s1", "criterion_id": "sp_c6", "name": "تحديد الاحتياجات المهنية", "order": 1},
    {"id": "sp_c6_s2", "criterion_id": "sp_c6", "name": "دعم النمو الوظيفي", "order": 2},
    {"id": "sp_c6_s3", "criterion_id": "sp_c6", "name": "تفويض الصلاحيات بفاعلية", "order": 3},
    {"id": "sp_c6_s4", "criterion_id": "sp_c6", "name": "إعداد قيادات بديلة", "order": 4},
    # sp_c7
    {"id": "sp_c7_s1", "criterion_id": "sp_c7", "name": "تحليل المؤشرات والبيانات", "order": 1},
    {"id": "sp_c7_s2", "criterion_id": "sp_c7", "name": "استشراف التحديات المستقبلية", "order": 2},
    {"id": "sp_c7_s3", "criterion_id": "sp_c7", "name": "مواءمة الخطط مع الأهداف الوطنية", "order": 3},
    {"id": "sp_c7_s4", "criterion_id": "sp_c7", "name": "بناء خطط طويلة المدى قابلة للقياس", "order": 4},
    # sp_c8
    {"id": "sp_c8_s1", "criterion_id": "sp_c8", "name": "دراسة البدائل المتاحة", "order": 1},
    {"id": "sp_c8_s2", "criterion_id": "sp_c8", "name": "المفاضلة بين الحلول", "order": 2},
    {"id": "sp_c8_s3", "criterion_id": "sp_c8", "name": "اتخاذ قرارات مبنية على معايير واضحة", "order": 3},
    {"id": "sp_c8_s4", "criterion_id": "sp_c8", "name": "تحمل مسؤولية نتائج القرار", "order": 4}
]

# قائمة التقارير (تقريران لكل تصنيف فرعي)
SP_REPORTS = [
    # sp_c1_s1
    {"id": "sp_c1_s1_r001", "subcategory_id": "sp_c1_s1", "name": "تقرير تحمل المسؤولية عن النتائج المدرسية", "order": 1},
    {"id": "sp_c1_s1_r002", "subcategory_id": "sp_c1_s1", "name": "تقرير متابعة تنفيذ القرارات وتحقيق الأهداف", "order": 2},
    # sp_c1_s2
    {"id": "sp_c1_s2_r001", "subcategory_id": "sp_c1_s2", "name": "تقرير الالتزام بتحقيق الأهداف في الوقت المحدد", "order": 1},
    {"id": "sp_c1_s2_r002", "subcategory_id": "sp_c1_s2", "name": "تقرير إنجاز المشاريع ضمن الجداول الزمنية", "order": 2},
    # sp_c1_s3
    {"id": "sp_c1_s3_r001", "subcategory_id": "sp_c1_s3", "name": "تقرير الالتزام بمعايير الجودة المهنية", "order": 1},
    {"id": "sp_c1_s3_r002", "subcategory_id": "sp_c1_s3", "name": "تقرير تطبيق معايير الجودة في الأداء المدرسي", "order": 2},

    # sp_c2_s1
    {"id": "sp_c2_s1_r001", "subcategory_id": "sp_c2_s1", "name": "تقرير تعزيز روح الفريق بين العاملين", "order": 1},
    {"id": "sp_c2_s1_r002", "subcategory_id": "sp_c2_s1", "name": "تقرير أنشطة بناء الفريق بالمدرسة", "order": 2},
    # sp_c2_s2
    {"id": "sp_c2_s2_r001", "subcategory_id": "sp_c2_s2", "name": "تقرير بناء علاقات مهنية إيجابية", "order": 1},
    {"id": "sp_c2_s2_r002", "subcategory_id": "sp_c2_s2", "name": "تقرير التواصل الفعال مع جميع الأطراف", "order": 2},
    # sp_c2_s3
    {"id": "sp_c2_s3_r001", "subcategory_id": "sp_c2_s3", "name": "تقرير إدارة الخلافات بموضوعية", "order": 1},
    {"id": "sp_c2_s3_r002", "subcategory_id": "sp_c2_s3", "name": "تقرير حل النزاعات بين الموظفين", "order": 2},

    # sp_c3_s1
    {"id": "sp_c3_s1_r001", "subcategory_id": "sp_c3_s1", "name": "تقرير الاستجابة للمتغيرات", "order": 1},
    {"id": "sp_c3_s1_r002", "subcategory_id": "sp_c3_s1", "name": "تقرير التعامل مع الأزمات والتحديات", "order": 2},
    # sp_c3_s2
    {"id": "sp_c3_s2_r001", "subcategory_id": "sp_c3_s2", "name": "تقرير تقبل وجهات النظر المختلفة", "order": 1},
    {"id": "sp_c3_s2_r002", "subcategory_id": "sp_c3_s2", "name": "تقرير تشجيع الاقتراحات والرأي الآخر", "order": 2},
    # sp_c3_s3
    {"id": "sp_c3_s3_r001", "subcategory_id": "sp_c3_s3", "name": "تقرير تعديل الخطط وفق المستجدات", "order": 1},
    {"id": "sp_c3_s3_r002", "subcategory_id": "sp_c3_s3", "name": "تقرير مرونة الخطط التشغيلية", "order": 2},

    # sp_c4_s1
    {"id": "sp_c4_s1_r001", "subcategory_id": "sp_c4_s1", "name": "تقرير اقتراح أفكار تطويرية", "order": 1},
    {"id": "sp_c4_s1_r002", "subcategory_id": "sp_c4_s1", "name": "تقرير المبادرات الإبداعية المقدمة", "order": 2},
    # sp_c4_s2
    {"id": "sp_c4_s2_r001", "subcategory_id": "sp_c4_s2", "name": "تقرير استباق المشكلات", "order": 1},
    {"id": "sp_c4_s2_r002", "subcategory_id": "sp_c4_s2", "name": "تقرير التحليل الاستباقي للمخاطر", "order": 2},
    # sp_c4_s3
    {"id": "sp_c4_s3_r001", "subcategory_id": "sp_c4_s3", "name": "تقرير تنفيذ حلول مبتكرة", "order": 1},
    {"id": "sp_c4_s3_r002", "subcategory_id": "sp_c4_s3", "name": "تقرير تطبيق ممارسات غير تقليدية ناجحة", "order": 2},

    # sp_c5_s1
    {"id": "sp_c5_s1_r001", "subcategory_id": "sp_c5_s1", "name": "تقرير إدارة عمليات التطوير المؤسسي", "order": 1},
    {"id": "sp_c5_s1_r002", "subcategory_id": "sp_c5_s1", "name": "تقرير قيادة مشاريع التطوير الشامل", "order": 2},
    # sp_c5_s2
    {"id": "sp_c5_s2_r001", "subcategory_id": "sp_c5_s2", "name": "تقرير تحفيز العاملين لتبني التغيير", "order": 1},
    {"id": "sp_c5_s2_r002", "subcategory_id": "sp_c5_s2", "name": "تقرير برامج التأهيل للتغيير", "order": 2},
    # sp_c5_s3
    {"id": "sp_c5_s3_r001", "subcategory_id": "sp_c5_s3", "name": "تقرير معالجة مقاومة التغيير", "order": 1},
    {"id": "sp_c5_s3_r002", "subcategory_id": "sp_c5_s3", "name": "تقرير إشراك المعارضين في عملية التغيير", "order": 2},
    # sp_c5_s4
    {"id": "sp_c5_s4_r001", "subcategory_id": "sp_c5_s4", "name": "تقرير تحقيق الرؤية الاستراتيجية", "order": 1},
    {"id": "sp_c5_s4_r002", "subcategory_id": "sp_c5_s4", "name": "تقرير ترجمة الرؤية إلى خطط تنفيذية", "order": 2},

    # sp_c6_s1
    {"id": "sp_c6_s1_r001", "subcategory_id": "sp_c6_s1", "name": "تقرير تحديد الاحتياجات المهنية", "order": 1},
    {"id": "sp_c6_s1_r002", "subcategory_id": "sp_c6_s1", "name": "تقرير تحليل الفجوات التدريبية", "order": 2},
    # sp_c6_s2
    {"id": "sp_c6_s2_r001", "subcategory_id": "sp_c6_s2", "name": "تقرير دعم النمو الوظيفي للموظفين", "order": 1},
    {"id": "sp_c6_s2_r002", "subcategory_id": "sp_c6_s2", "name": "تقرير مسارات الترقي والتطوير", "order": 2},
    # sp_c6_s3
    {"id": "sp_c6_s3_r001", "subcategory_id": "sp_c6_s3", "name": "تقرير تفويض الصلاحيات بفاعلية", "order": 1},
    {"id": "sp_c6_s3_r002", "subcategory_id": "sp_c6_s3", "name": "تقرير تمكين فرق العمل", "order": 2},
    # sp_c6_s4
    {"id": "sp_c6_s4_r001", "subcategory_id": "sp_c6_s4", "name": "تقرير إعداد قيادات بديلة", "order": 1},
    {"id": "sp_c6_s4_r002", "subcategory_id": "sp_c6_s4", "name": "تقرير برنامج توريث القيادة", "order": 2},

    # sp_c7_s1
    {"id": "sp_c7_s1_r001", "subcategory_id": "sp_c7_s1", "name": "تقرير تحليل المؤشرات والبيانات", "order": 1},
    {"id": "sp_c7_s1_r002", "subcategory_id": "sp_c7_s1", "name": "تقرير استخدام البيانات في تحسين الأداء", "order": 2},
    # sp_c7_s2
    {"id": "sp_c7_s2_r001", "subcategory_id": "sp_c7_s2", "name": "تقرير استشراف التحديات المستقبلية", "order": 1},
    {"id": "sp_c7_s2_r002", "subcategory_id": "sp_c7_s2", "name": "تقرير دراسة الاتجاهات المستقبلية في التعليم", "order": 2},
    # sp_c7_s3
    {"id": "sp_c7_s3_r001", "subcategory_id": "sp_c7_s3", "name": "تقرير مواءمة الخطط مع الأهداف الوطنية", "order": 1},
    {"id": "sp_c7_s3_r002", "subcategory_id": "sp_c7_s3", "name": "تقرير مساهمة المدرسة في رؤية 2030", "order": 2},
    # sp_c7_s4
    {"id": "sp_c7_s4_r001", "subcategory_id": "sp_c7_s4", "name": "تقرير بناء خطط طويلة المدى قابلة للقياس", "order": 1},
    {"id": "sp_c7_s4_r002", "subcategory_id": "sp_c7_s4", "name": "تقرير مؤشرات قياس أداء الخطط", "order": 2},

    # sp_c8_s1
    {"id": "sp_c8_s1_r001", "subcategory_id": "sp_c8_s1", "name": "تقرير دراسة البدائل المتاحة", "order": 1},
    {"id": "sp_c8_s1_r002", "subcategory_id": "sp_c8_s1", "name": "تقرير تحليل الخيارات قبل اتخاذ القرار", "order": 2},
    # sp_c8_s2
    {"id": "sp_c8_s2_r001", "subcategory_id": "sp_c8_s2", "name": "تقرير المفاضلة بين الحلول", "order": 1},
    {"id": "sp_c8_s2_r002", "subcategory_id": "sp_c8_s2", "name": "تقرير تقييم الحلول المطروحة", "order": 2},
    # sp_c8_s3
    {"id": "sp_c8_s3_r001", "subcategory_id": "sp_c8_s3", "name": "تقرير اتخاذ قرارات مبنية على معايير واضحة", "order": 1},
    {"id": "sp_c8_s3_r002", "subcategory_id": "sp_c8_s3", "name": "تقرير الشفافية في القرارات", "order": 2},
    # sp_c8_s4
    {"id": "sp_c8_s4_r001", "subcategory_id": "sp_c8_s4", "name": "تقرير تحمل مسؤولية نتائج القرار", "order": 1},
    {"id": "sp_c8_s4_r002", "subcategory_id": "sp_c8_s4", "name": "تقرير متابعة تنفيذ القرارات", "order": 2}
]

# قالب البرومبت الخاص بمدير المدرسة
SCHOOL_PRINCIPAL_PROMPT_TEMPLATE = """أنت مدير مدرسة خبير وقائد تربوي، مسؤول عن تحقيق الرؤية الاستراتيجية وقيادة عمليات التطوير المؤسسي وتمكين العاملين.

المطلوب:
- عرض الجدارة القيادية الرئيسية.
- عرض التصنيف الفرعي.
- كتابة تقرير مهني يوضح الممارسات القيادية المرتبطة بهذا التصنيف.

التقرير المطلوب: "{report_name}"
وهو يندرج تحت التصنيف الفرعي: "{subcategory_name}"
ضمن الجدارة القيادية: "{criterion_name}"

{subject_line}
{lesson_line}
{grade_line}
{target_line}
{place_line}
{count_line}

ضوابط الكتابة:
- لغة قيادية رسمية وإستراتيجية.
- إبراز دورك في التخطيط والتنظيم والمتابعة.
- توضيح كيفية تطبيق الجدارة في سياق العمل المدرسي.
- الإشارة إلى التعامل مع الفريق والمجتمع المدرسي.
- بيان أثر القيادة على تحسين الأداء والنتائج.
- استخدام مؤشرات وأمثلة واقعية.
- صياغة عملية دقيقة من 5–7 أسطر.

**الحقول المطلوبة:**
1. الهدف القيادي
2. نبذة مختصرة
3. إجراءات التنفيذ
4. الاستراتيجيات والأساليب القيادية
5. نقاط القوة
6. نقاط التحسين
7. التوصيات

يرجى تقديم الإجابة باللغة العربية الفصحى، وتنظيمها بحيث يكون كل حقل في سطر منفصل يبدأ برقمه فقط دون ذكر العنوان."""