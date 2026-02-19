# -*- coding: utf-8 -*-

# قائمة المعايير الرئيسية (الجدارات القيادية) للمشرف التربوي
ES_CRITERIA = [
    {"id": "es_c1", "name": "المسؤولية", "order": 1},
    {"id": "es_c2", "name": "العمل الجماعي", "order": 2},
    {"id": "es_c3", "name": "المرونة والتكيف مع التغيير", "order": 3},
    {"id": "es_c4", "name": "المبادرة", "order": 4},
    {"id": "es_c5", "name": "قيادة التغيير", "order": 5},
    {"id": "es_c6", "name": "تطوير وتمكين العاملين", "order": 6},
    {"id": "es_c7", "name": "التوجه الاستراتيجي", "order": 7},
    {"id": "es_c8", "name": "اتخاذ القرارات", "order": 8}
]

# التصنيفات الفرعية للمشرف التربوي (نفس الجدارات مع تركيز إشرافي)
ES_SUBCATEGORIES = [
    # es_c1
    {"id": "es_c1_s1", "criterion_id": "es_c1", "name": "تحمل المسؤولية عن نتائج الإشراف", "order": 1},
    {"id": "es_c1_s2", "criterion_id": "es_c1", "name": "الالتزام بتحقيق الأهداف الإشرافية في الوقت المحدد", "order": 2},
    {"id": "es_c1_s3", "criterion_id": "es_c1", "name": "الالتزام بمعايير الجودة المهنية", "order": 3},
    # es_c2
    {"id": "es_c2_s1", "criterion_id": "es_c2", "name": "تعزيز روح الفريق مع المعلمين", "order": 1},
    {"id": "es_c2_s2", "criterion_id": "es_c2", "name": "بناء علاقات مهنية إيجابية مع المدارس", "order": 2},
    {"id": "es_c2_s3", "criterion_id": "es_c2", "name": "إدارة الخلافات بموضوعية", "order": 3},
    # es_c3
    {"id": "es_c3_s1", "criterion_id": "es_c3", "name": "الاستجابة للمتغيرات التعليمية", "order": 1},
    {"id": "es_c3_s2", "criterion_id": "es_c3", "name": "تقبل وجهات النظر المختلفة من المعلمين", "order": 2},
    {"id": "es_c3_s3", "criterion_id": "es_c3", "name": "تعديل الخطط الإشرافية وفق المستجدات", "order": 3},
    # es_c4
    {"id": "es_c4_s1", "criterion_id": "es_c4", "name": "اقتراح أفكار تطويرية للمناهج", "order": 1},
    {"id": "es_c4_s2", "criterion_id": "es_c4", "name": "استباق المشكلات التعليمية", "order": 2},
    {"id": "es_c4_s3", "criterion_id": "es_c4", "name": "تنفيذ حلول مبتكرة في الإشراف", "order": 3},
    # es_c5
    {"id": "es_c5_s1", "criterion_id": "es_c5", "name": "إدارة عمليات التطوير التربوي", "order": 1},
    {"id": "es_c5_s2", "criterion_id": "es_c5", "name": "تحفيز المعلمين لتبني التغيير", "order": 2},
    {"id": "es_c5_s3", "criterion_id": "es_c5", "name": "معالجة مقاومة التغيير", "order": 3},
    {"id": "es_c5_s4", "criterion_id": "es_c5", "name": "تحقيق الرؤية التربوية", "order": 4},
    # es_c6
    {"id": "es_c6_s1", "criterion_id": "es_c6", "name": "تحديد الاحتياجات المهنية للمعلمين", "order": 1},
    {"id": "es_c6_s2", "criterion_id": "es_c6", "name": "دعم النمو المهني", "order": 2},
    {"id": "es_c6_s3", "criterion_id": "es_c6", "name": "تفويض الصلاحيات بفاعلية", "order": 3},
    {"id": "es_c6_s4", "criterion_id": "es_c6", "name": "إعداد قيادات تعليمية", "order": 4},
    # es_c7
    {"id": "es_c7_s1", "criterion_id": "es_c7", "name": "تحليل مؤشرات الأداء التعليمي", "order": 1},
    {"id": "es_c7_s2", "criterion_id": "es_c7", "name": "استشراف التحديات المستقبلية في التعليم", "order": 2},
    {"id": "es_c7_s3", "criterion_id": "es_c7", "name": "مواءمة الخطط مع الأهداف الوطنية", "order": 3},
    {"id": "es_c7_s4", "criterion_id": "es_c7", "name": "بناء خطط إشرافية طويلة المدى", "order": 4},
    # es_c8
    {"id": "es_c8_s1", "criterion_id": "es_c8", "name": "دراسة البدائل المتاحة", "order": 1},
    {"id": "es_c8_s2", "criterion_id": "es_c8", "name": "المفاضلة بين الحلول", "order": 2},
    {"id": "es_c8_s3", "criterion_id": "es_c8", "name": "اتخاذ قرارات مبنية على معايير واضحة", "order": 3},
    {"id": "es_c8_s4", "criterion_id": "es_c8", "name": "تحمل مسؤولية نتائج القرار", "order": 4}
]

# قائمة التقارير (تقريران لكل تصنيف فرعي)
ES_REPORTS = [
    # es_c1_s1
    {"id": "es_c1_s1_r001", "subcategory_id": "es_c1_s1", "name": "تقرير تحمل المسؤولية عن نتائج الإشراف", "order": 1},
    {"id": "es_c1_s1_r002", "subcategory_id": "es_c1_s1", "name": "تقرير متابعة تنفيذ الخطط الإشرافية", "order": 2},
    # es_c1_s2
    {"id": "es_c1_s2_r001", "subcategory_id": "es_c1_s2", "name": "تقرير الالتزام بتحقيق الأهداف الإشرافية", "order": 1},
    {"id": "es_c1_s2_r002", "subcategory_id": "es_c1_s2", "name": "تقرير إنجاز الزيارات في المواعيد المحددة", "order": 2},
    # es_c1_s3
    {"id": "es_c1_s3_r001", "subcategory_id": "es_c1_s3", "name": "تقرير الالتزام بمعايير الجودة المهنية", "order": 1},
    {"id": "es_c1_s3_r002", "subcategory_id": "es_c1_s3", "name": "تقرير تطبيق معايير التميز الإشرافي", "order": 2},

    # es_c2_s1
    {"id": "es_c2_s1_r001", "subcategory_id": "es_c2_s1", "name": "تقرير تعزيز روح الفريق مع المعلمين", "order": 1},
    {"id": "es_c2_s1_r002", "subcategory_id": "es_c2_s1", "name": "تقرير بناء مجتمعات تعلم مهنية", "order": 2},
    # es_c2_s2
    {"id": "es_c2_s2_r001", "subcategory_id": "es_c2_s2", "name": "تقرير بناء علاقات مهنية إيجابية مع المدارس", "order": 1},
    {"id": "es_c2_s2_r002", "subcategory_id": "es_c2_s2", "name": "تقرير التواصل الفعال مع قادة المدارس", "order": 2},
    # es_c2_s3
    {"id": "es_c2_s3_r001", "subcategory_id": "es_c2_s3", "name": "تقرير إدارة الخلافات بموضوعية", "order": 1},
    {"id": "es_c2_s3_r002", "subcategory_id": "es_c2_s3", "name": "تقرير حل النزاعات بين المعلمين", "order": 2},

    # es_c3_s1
    {"id": "es_c3_s1_r001", "subcategory_id": "es_c3_s1", "name": "تقرير الاستجابة للمتغيرات التعليمية", "order": 1},
    {"id": "es_c3_s1_r002", "subcategory_id": "es_c3_s1", "name": "تقرير التكيف مع تحديثات المناهج", "order": 2},
    # es_c3_s2
    {"id": "es_c3_s2_r001", "subcategory_id": "es_c3_s2", "name": "تقرير تقبل وجهات النظر المختلفة من المعلمين", "order": 1},
    {"id": "es_c3_s2_r002", "subcategory_id": "es_c3_s2", "name": "تقرير مراعاة آراء المعلمين في التطوير", "order": 2},
    # es_c3_s3
    {"id": "es_c3_s3_r001", "subcategory_id": "es_c3_s3", "name": "تقرير تعديل الخطط الإشرافية وفق المستجدات", "order": 1},
    {"id": "es_c3_s3_r002", "subcategory_id": "es_c3_s3", "name": "تقرير مرونة البرامج الإشرافية", "order": 2},

    # es_c4_s1
    {"id": "es_c4_s1_r001", "subcategory_id": "es_c4_s1", "name": "تقرير اقتراح أفكار تطويرية للمناهج", "order": 1},
    {"id": "es_c4_s1_r002", "subcategory_id": "es_c4_s1", "name": "تقرير المساهمة في تطوير الخطط الدراسية", "order": 2},
    # es_c4_s2
    {"id": "es_c4_s2_r001", "subcategory_id": "es_c4_s2", "name": "تقرير استباق المشكلات التعليمية", "order": 1},
    {"id": "es_c4_s2_r002", "subcategory_id": "es_c4_s2", "name": "تقرير الكشف المبكر عن صعوبات التعلم", "order": 2},
    # es_c4_s3
    {"id": "es_c4_s3_r001", "subcategory_id": "es_c4_s3", "name": "تقرير تنفيذ حلول مبتكرة في الإشراف", "order": 1},
    {"id": "es_c4_s3_r002", "subcategory_id": "es_c4_s3", "name": "تقرير توظيف التقنية في الإشراف", "order": 2},

    # es_c5_s1
    {"id": "es_c5_s1_r001", "subcategory_id": "es_c5_s1", "name": "تقرير إدارة عمليات التطوير التربوي", "order": 1},
    {"id": "es_c5_s1_r002", "subcategory_id": "es_c5_s1", "name": "تقرير قيادة مشاريع تطوير المناهج", "order": 2},
    # es_c5_s2
    {"id": "es_c5_s2_r001", "subcategory_id": "es_c5_s2", "name": "تقرير تحفيز المعلمين لتبني التغيير", "order": 1},
    {"id": "es_c5_s2_r002", "subcategory_id": "es_c5_s2", "name": "تقرير برامج التوعية بأهمية التطوير", "order": 2},
    # es_c5_s3
    {"id": "es_c5_s3_r001", "subcategory_id": "es_c5_s3", "name": "تقرير معالجة مقاومة التغيير", "order": 1},
    {"id": "es_c5_s3_r002", "subcategory_id": "es_c5_s3", "name": "تقرير إشراك المعلمين في التخطيط للتغيير", "order": 2},
    # es_c5_s4
    {"id": "es_c5_s4_r001", "subcategory_id": "es_c5_s4", "name": "تقرير تحقيق الرؤية التربوية", "order": 1},
    {"id": "es_c5_s4_r002", "subcategory_id": "es_c5_s4", "name": "تقرير ربط الممارسات الإشرافية بالرؤية", "order": 2},

    # es_c6_s1
    {"id": "es_c6_s1_r001", "subcategory_id": "es_c6_s1", "name": "تقرير تحديد الاحتياجات المهنية للمعلمين", "order": 1},
    {"id": "es_c6_s1_r002", "subcategory_id": "es_c6_s1", "name": "تقرير تشخيص الفجوات التدريبية", "order": 2},
    # es_c6_s2
    {"id": "es_c6_s2_r001", "subcategory_id": "es_c6_s2", "name": "تقرير دعم النمو المهني", "order": 1},
    {"id": "es_c6_s2_r002", "subcategory_id": "es_c6_s2", "name": "تقرير تنظيم برامج تنمية مهنية", "order": 2},
    # es_c6_s3
    {"id": "es_c6_s3_r001", "subcategory_id": "es_c6_s3", "name": "تقرير تفويض الصلاحيات بفاعلية", "order": 1},
    {"id": "es_c6_s3_r002", "subcategory_id": "es_c6_s3", "name": "تقرير تمكين المعلمين من اتخاذ القرارات", "order": 2},
    # es_c6_s4
    {"id": "es_c6_s4_r001", "subcategory_id": "es_c6_s4", "name": "تقرير إعداد قيادات تعليمية", "order": 1},
    {"id": "es_c6_s4_r002", "subcategory_id": "es_c6_s4", "name": "تقرير برنامج إعداد معلمين متميزين", "order": 2},

    # es_c7_s1
    {"id": "es_c7_s1_r001", "subcategory_id": "es_c7_s1", "name": "تقرير تحليل مؤشرات الأداء التعليمي", "order": 1},
    {"id": "es_c7_s1_r002", "subcategory_id": "es_c7_s1", "name": "تقرير استخدام البيانات في تحسين الممارسات", "order": 2},
    # es_c7_s2
    {"id": "es_c7_s2_r001", "subcategory_id": "es_c7_s2", "name": "تقرير استشراف التحديات المستقبلية في التعليم", "order": 1},
    {"id": "es_c7_s2_r002", "subcategory_id": "es_c7_s2", "name": "تقرير دراسة متطلبات التعليم القادم", "order": 2},
    # es_c7_s3
    {"id": "es_c7_s3_r001", "subcategory_id": "es_c7_s3", "name": "تقرير مواءمة الخطط مع الأهداف الوطنية", "order": 1},
    {"id": "es_c7_s3_r002", "subcategory_id": "es_c7_s3", "name": "تقرير دعم أولويات وزارة التعليم", "order": 2},
    # es_c7_s4
    {"id": "es_c7_s4_r001", "subcategory_id": "es_c7_s4", "name": "تقرير بناء خطط إشرافية طويلة المدى", "order": 1},
    {"id": "es_c7_s4_r002", "subcategory_id": "es_c7_s4", "name": "تقرير مؤشرات قياس الخطط الإشرافية", "order": 2},

    # es_c8_s1
    {"id": "es_c8_s1_r001", "subcategory_id": "es_c8_s1", "name": "تقرير دراسة البدائل المتاحة", "order": 1},
    {"id": "es_c8_s1_r002", "subcategory_id": "es_c8_s1", "name": "تقرير تحليل الخيارات الإشرافية", "order": 2},
    # es_c8_s2
    {"id": "es_c8_s2_r001", "subcategory_id": "es_c8_s2", "name": "تقرير المفاضلة بين الحلول", "order": 1},
    {"id": "es_c8_s2_r002", "subcategory_id": "es_c8_s2", "name": "تقرير تقييم فاعلية الحلول المقترحة", "order": 2},
    # es_c8_s3
    {"id": "es_c8_s3_r001", "subcategory_id": "es_c8_s3", "name": "تقرير اتخاذ قرارات مبنية على معايير واضحة", "order": 1},
    {"id": "es_c8_s3_r002", "subcategory_id": "es_c8_s3", "name": "تقرير قرارات الإشراف الميداني", "order": 2},
    # es_c8_s4
    {"id": "es_c8_s4_r001", "subcategory_id": "es_c8_s4", "name": "تقرير تحمل مسؤولية نتائج القرار", "order": 1},
    {"id": "es_c8_s4_r002", "subcategory_id": "es_c8_s4", "name": "تقرير متابعة تنفيذ القرارات الإشرافية", "order": 2}
]

# قالب البرومبت الخاص بالمشرف التربوي
EDUCATIONAL_SUPERVISOR_PROMPT_TEMPLATE = """أنت مشرف تربوي خبير وقائد تعليمي، مسؤول عن تطوير الأداء المهني للمعلمين وتحسين الممارسات التعليمية وفق الرؤى الوطنية.

المطلوب:
- عرض الجدارة القيادية الرئيسية.
- عرض التصنيف الفرعي.
- كتابة تقرير مهني يوضح الممارسات الإشرافية المرتبطة بهذا التصنيف.

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
- لغة إشرافية مهنية واستراتيجية.
- إبراز دورك في التوجيه والتدريب والتقويم.
- توضيح كيفية تطبيق الجدارة في العلاقة مع المعلمين.
- الإشارة إلى تحليل البيانات واستخدامها في التطوير.
- بيان أثر الإشراف على تحسين نواتج التعلم.
- تقديم أمثلة عملية تعكس الممارسات الفعالة.
- صياغة عملية دقيقة من 5–7 أسطر.

**الحقول المطلوبة:**
1. الهدف الإشرافي
2. نبذة مختصرة
3. إجراءات التنفيذ
4. الاستراتيجيات والأساليب الإشرافية
5. نقاط القوة
6. نقاط التحسين
7. التوصيات

يرجى تقديم الإجابة باللغة العربية الفصحى، وتنظيمها بحيث يكون كل حقل في سطر منفصل يبدأ برقمه فقط دون ذكر العنوان."""