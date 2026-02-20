# -*- coding: utf-8 -*-

# ==========================================================
# المعايير الرئيسية (الجدارات القيادية) للمشرف التربوي
# ==========================================================

SUPERVISOR_CRITERIA = [
    {"id": "su_c1", "name": "المسؤولية (15%)", "order": 1, "percentage": 15},
    {"id": "su_c2", "name": "العمل الجماعي (10%)", "order": 2, "percentage": 10},
    {"id": "su_c3", "name": "المرونة والتكيف مع التغيير (10%)", "order": 3, "percentage": 10},
    {"id": "su_c4", "name": "المبادرة (10%)", "order": 4, "percentage": 10},
    {"id": "su_c5", "name": "قيادة التغيير (20%)", "order": 5, "percentage": 20},
    {"id": "su_c6", "name": "تطوير وتمكين العاملين (10%)", "order": 6, "percentage": 10},
    {"id": "su_c7", "name": "التوجه الاستراتيجي (10%)", "order": 7, "percentage": 10},
    {"id": "su_c8", "name": "اتخاذ القرارات (15%)", "order": 8, "percentage": 15}
]

# ==========================================================
# التصنيفات الفرعية
# ==========================================================

SUPERVISOR_SUBCATEGORIES = [

    # المسؤولية
    {"id": "su_c1_s1", "criterion_id": "su_c1", "name": "تحمل المسؤولية عن نتائج الإشراف", "order": 1},
    {"id": "su_c1_s2", "criterion_id": "su_c1", "name": "الالتزام بتحقيق الأهداف الإشرافية", "order": 2},
    {"id": "su_c1_s3", "criterion_id": "su_c1", "name": "الالتزام بمعايير الجودة المهنية", "order": 3},

    # العمل الجماعي
    {"id": "su_c2_s1", "criterion_id": "su_c2", "name": "تعزيز روح الفريق مع المعلمين", "order": 1},
    {"id": "su_c2_s2", "criterion_id": "su_c2", "name": "بناء علاقات مهنية إيجابية مع المدارس", "order": 2},
    {"id": "su_c2_s3", "criterion_id": "su_c2", "name": "إدارة الخلافات بموضوعية", "order": 3},

    # المرونة
    {"id": "su_c3_s1", "criterion_id": "su_c3", "name": "الاستجابة للمتغيرات التعليمية", "order": 1},
    {"id": "su_c3_s2", "criterion_id": "su_c3", "name": "تعديل الخطط الإشرافية وفق المستجدات", "order": 2},
    {"id": "su_c3_s3", "criterion_id": "su_c3", "name": "التكيف مع تحديثات المناهج", "order": 3},

    # المبادرة
    {"id": "su_c4_s1", "criterion_id": "su_c4", "name": "اقتراح مبادرات تطويرية", "order": 1},
    {"id": "su_c4_s2", "criterion_id": "su_c4", "name": "استباق المشكلات التعليمية", "order": 2},
    {"id": "su_c4_s3", "criterion_id": "su_c4", "name": "تنفيذ حلول إشرافية مبتكرة", "order": 3},

    # قيادة التغيير
    {"id": "su_c5_s1", "criterion_id": "su_c5", "name": "إدارة عمليات التطوير التربوي", "order": 1},
    {"id": "su_c5_s2", "criterion_id": "su_c5", "name": "تحفيز المعلمين لتبني التغيير", "order": 2},
    {"id": "su_c5_s3", "criterion_id": "su_c5", "name": "معالجة مقاومة التغيير", "order": 3},
    {"id": "su_c5_s4", "criterion_id": "su_c5", "name": "تحقيق الرؤية التربوية", "order": 4},

    # تطوير وتمكين العاملين
    {"id": "su_c6_s1", "criterion_id": "su_c6", "name": "تحديد الاحتياجات المهنية للمعلمين", "order": 1},
    {"id": "su_c6_s2", "criterion_id": "su_c6", "name": "دعم النمو المهني", "order": 2},
    {"id": "su_c6_s3", "criterion_id": "su_c6", "name": "إعداد قيادات تعليمية", "order": 3},

    # التوجه الاستراتيجي
    {"id": "su_c7_s1", "criterion_id": "su_c7", "name": "تحليل مؤشرات الأداء التعليمي", "order": 1},
    {"id": "su_c7_s2", "criterion_id": "su_c7", "name": "مواءمة الخطط مع الأهداف الوطنية", "order": 2},
    {"id": "su_c7_s3", "criterion_id": "su_c7", "name": "بناء خطط إشرافية طويلة المدى", "order": 3},

    # اتخاذ القرارات
    {"id": "su_c8_s1", "criterion_id": "su_c8", "name": "دراسة البدائل المتاحة", "order": 1},
    {"id": "su_c8_s2", "criterion_id": "su_c8", "name": "اتخاذ قرارات مبنية على بيانات", "order": 2},
    {"id": "su_c8_s3", "criterion_id": "su_c8", "name": "تحمل مسؤولية نتائج القرار", "order": 3},
]

# ==========================================================
# التقارير (10 تقارير لكل تصنيف فرعي)
# ==========================================================

SUPERVISOR_REPORTS = [
    # المسؤولية - تحمل المسؤولية عن نتائج الإشراف (su_c1_s1)
    {"id": "su_r001", "subcategory_id": "su_c1_s1", "name": "تقرير متابعة تنفيذ الخطة الإشرافية الشهرية", "order": 1},
    {"id": "su_r002", "subcategory_id": "su_c1_s1", "name": "تقرير تحليل نتائج الطلاب في المواد الأساسية", "order": 2},
    {"id": "su_r003", "subcategory_id": "su_c1_s1", "name": "تقرير تقييم أداء المعلمين بعد الزيارات الصفية", "order": 3},
    {"id": "su_r004", "subcategory_id": "su_c1_s1", "name": "تقرير متابعة تنفيذ البرامج العلاجية للطلاب", "order": 4},
    {"id": "su_r005", "subcategory_id": "su_c1_s1", "name": "تقرير الإنجاز في المشاريع التطويرية بالمدارس", "order": 5},
    {"id": "su_r006", "subcategory_id": "su_c1_s1", "name": "تقرير مسؤولية التوجيه المهني للمعلمين الجدد", "order": 6},
    {"id": "su_r007", "subcategory_id": "su_c1_s1", "name": "تقرير مدى الالتزام بمعايير المناهج المطورة", "order": 7},
    {"id": "su_r008", "subcategory_id": "su_c1_s1", "name": "تقرير نتائج تقييم الأداء الإشرافي الذاتي", "order": 8},
    {"id": "su_r009", "subcategory_id": "su_c1_s1", "name": "تقرير متابعة خطط تحسين المدارس", "order": 9},
    {"id": "su_r010", "subcategory_id": "su_c1_s1", "name": "تقرير فاعلية الاجتماعات الإشرافية", "order": 10},

    # المسؤولية - الالتزام بتحقيق الأهداف الإشرافية (su_c1_s2)
    {"id": "su_r011", "subcategory_id": "su_c1_s2", "name": "تقرير إنجاز مؤشرات الأداء للخطة التشغيلية", "order": 11},
    {"id": "su_r012", "subcategory_id": "su_c1_s2", "name": "تقرير تحقيق المستهدفات في البرامج التدريبية", "order": 12},
    {"id": "su_r013", "subcategory_id": "su_c1_s2", "name": "تقرير نسبة إنجاز الزيارات الإشرافية المجدولة", "order": 13},
    {"id": "su_r014", "subcategory_id": "su_c1_s2", "name": "تقرير التزام المدارس بتطبيق المبادرات", "order": 14},
    {"id": "su_r015", "subcategory_id": "su_c1_s2", "name": "تقرير متابعة المواعيد النهائية للتسليم", "order": 15},
    {"id": "su_r016", "subcategory_id": "su_c1_s2", "name": "تقرير تحقيق أهداف تحسين نواتج التعلم", "order": 16},
    {"id": "su_r017", "subcategory_id": "su_c1_s2", "name": "تقرير الالتزام بتنفيذ خطط الدعم", "order": 17},
    {"id": "su_r018", "subcategory_id": "su_c1_s2", "name": "تقرير إنجاز مشاريع التقويم الخارجي", "order": 18},
    {"id": "su_r019", "subcategory_id": "su_c1_s2", "name": "تقرير تحقيق الأهداف المهنية للمعلمين", "order": 19},
    {"id": "su_r020", "subcategory_id": "su_c1_s2", "name": "تقرير الالتزام بخطة تطوير القيادات المدرسية", "order": 20},

    # المسؤولية - الالتزام بمعايير الجودة المهنية (su_c1_s3)
    {"id": "su_r021", "subcategory_id": "su_c1_s3", "name": "تقرير مدى تطبيق معايير الجودة في الدروس", "order": 21},
    {"id": "su_r022", "subcategory_id": "su_c1_s3", "name": "تقرير تقييم الأداء المهني وفق المعايير الوطنية", "order": 22},
    {"id": "su_r023", "subcategory_id": "su_c1_s3", "name": "تقرير الالتزام بمعايير التقويم المستمر", "order": 23},
    {"id": "su_r024", "subcategory_id": "su_c1_s3", "name": "تقرير متابعة جودة الخطط التعليمية الفردية", "order": 24},
    {"id": "su_r025", "subcategory_id": "su_c1_s3", "name": "تقرير فاعلية أدوات القياس المستخدمة", "order": 25},
    {"id": "su_r026", "subcategory_id": "su_c1_s3", "name": "تقرير الالتزام بمعايير الصحة النفسية للطلاب", "order": 26},
    {"id": "su_r027", "subcategory_id": "su_c1_s3", "name": "تقرير جودة التغذية الراجعة للمعلمين", "order": 27},
    {"id": "su_r028", "subcategory_id": "su_c1_s3", "name": "تقرير مراجعة مخرجات التعلم وفق المعايير", "order": 28},
    {"id": "su_r029", "subcategory_id": "su_c1_s3", "name": "تقرير تطبيق معايير السلامة في المختبرات", "order": 29},
    {"id": "su_r030", "subcategory_id": "su_c1_s3", "name": "تقرير جودة الأنشطة المدرسية", "order": 30},

    # العمل الجماعي - تعزيز روح الفريق مع المعلمين (su_c2_s1)
    {"id": "su_r031", "subcategory_id": "su_c2_s1", "name": "تقرير فعالية اجتماعات فريق التطوير المهني", "order": 31},
    {"id": "su_r032", "subcategory_id": "su_c2_s1", "name": "تقرير المشاركة في مجتمعات التعلم", "order": 32},
    {"id": "su_r033", "subcategory_id": "su_c2_s1", "name": "تقرير مبادرات التعاون بين المعلمين", "order": 33},
    {"id": "su_r034", "subcategory_id": "su_c2_s1", "name": "تقرير قياس روح الفريق في الأنشطة المشتركة", "order": 34},
    {"id": "su_r035", "subcategory_id": "su_c2_s1", "name": "تقرير تأثير التحفيز الجماعي على الأداء", "order": 35},
    {"id": "su_r036", "subcategory_id": "su_c2_s1", "name": "تقرير تنظيم ورش عمل تعاونية", "order": 36},
    {"id": "su_r037", "subcategory_id": "su_c2_s1", "name": "تقرير تقييم العمل الجماعي في المشاريع", "order": 37},
    {"id": "su_r038", "subcategory_id": "su_c2_s1", "name": "تقرير بناء فرق عمل متخصصة", "order": 38},
    {"id": "su_r039", "subcategory_id": "su_c2_s1", "name": "تقرير مشاركة المعلمين في اتخاذ القرارات", "order": 39},
    {"id": "su_r040", "subcategory_id": "su_c2_s1", "name": "تقرير تنمية الروابط الاجتماعية المهنية", "order": 40},

    # العمل الجماعي - بناء علاقات مهنية إيجابية مع المدارس (su_c2_s2)
    {"id": "su_r041", "subcategory_id": "su_c2_s2", "name": "تقرير مستوى التواصل مع قادة المدارس", "order": 41},
    {"id": "su_r042", "subcategory_id": "su_c2_s2", "name": "تقرير تنسيق الزيارات المتبادلة بين المدارس", "order": 42},
    {"id": "su_r043", "subcategory_id": "su_c2_s2", "name": "تقرير فاعلية الشراكات مع المجتمع المدرسي", "order": 43},
    {"id": "su_r044", "subcategory_id": "su_c2_s2", "name": "تقرير قياس رضا المدارس عن الدعم الإشرافي", "order": 44},
    {"id": "su_r045", "subcategory_id": "su_c2_s2", "name": "تقرير تنمية الثقة بين المشرف والمعلمين", "order": 45},
    {"id": "su_r046", "subcategory_id": "su_c2_s2", "name": "تقرير حل المشكلات بالتعاون مع المدرسة", "order": 46},
    {"id": "su_r047", "subcategory_id": "su_c2_s2", "name": "تقرير تبادل الخبرات بين المدارس", "order": 47},
    {"id": "su_r048", "subcategory_id": "su_c2_s2", "name": "تقرير متابعة تنفيذ توصيات الإشراف", "order": 48},
    {"id": "su_r049", "subcategory_id": "su_c2_s2", "name": "تقرير دعم ثقافة الحوار المهني", "order": 49},
    {"id": "su_r050", "subcategory_id": "su_c2_s2", "name": "تقرير بناء شبكات تعاون إقليمية", "order": 50},

    # العمل الجماعي - إدارة الخلافات بموضوعية (su_c2_s3)
    {"id": "su_r051", "subcategory_id": "su_c2_s3", "name": "تقرير تحليل أسباب الخلافات المهنية", "order": 51},
    {"id": "su_r052", "subcategory_id": "su_c2_s3", "name": "تقرير أساليب فض النزاعات بين المعلمين", "order": 52},
    {"id": "su_r053", "subcategory_id": "su_c2_s3", "name": "تقرير قياس أثر الوساطة في تحسين العلاقات", "order": 53},
    {"id": "su_r054", "subcategory_id": "su_c2_s3", "name": "تقرير ورش إدارة الخلافات للمعلمين", "order": 54},
    {"id": "su_r055", "subcategory_id": "su_c2_s3", "name": "تقرير متابعة حالات الخلاف المزمنة", "order": 55},
    {"id": "su_r056", "subcategory_id": "su_c2_s3", "name": "تقرير فاعلية بروتوكولات التواصل", "order": 56},
    {"id": "su_r057", "subcategory_id": "su_c2_s3", "name": "تقرير استطلاع رأي حول المناخ المدرسي", "order": 57},
    {"id": "su_r058", "subcategory_id": "su_c2_s3", "name": "تقرير تأثير الخلافات على الأداء", "order": 58},
    {"id": "su_r059", "subcategory_id": "su_c2_s3", "name": "تقرير تدريب المعلمين على الحوار", "order": 59},
    {"id": "su_r060", "subcategory_id": "su_c2_s3", "name": "تقرير تحسين العلاقات بعد التدخل", "order": 60},

    # المرونة - الاستجابة للمتغيرات التعليمية (su_c3_s1)
    {"id": "su_r061", "subcategory_id": "su_c3_s1", "name": "تقرير التكيف مع تغيير المناهج الدراسية", "order": 61},
    {"id": "su_r062", "subcategory_id": "su_c3_s1", "name": "تقرير تعديل خطط الإشراف أثناء الأزمات", "order": 62},
    {"id": "su_r063", "subcategory_id": "su_c3_s1", "name": "تقرير استجابة المدارس للتعليم عن بعد", "order": 63},
    {"id": "su_r064", "subcategory_id": "su_c3_s1", "name": "تقرير مرونة تطبيق استراتيجيات تدريس جديدة", "order": 64},
    {"id": "su_r065", "subcategory_id": "su_c3_s1", "name": "تقرير التعامل مع تغيرات السياسات التعليمية", "order": 65},
    {"id": "su_r066", "subcategory_id": "su_c3_s1", "name": "تقرير تكييف أدوات التقويم مع الظروف", "order": 66},
    {"id": "su_r067", "subcategory_id": "su_c3_s1", "name": "تقرير مرونة الموارد التعليمية", "order": 67},
    {"id": "su_r068", "subcategory_id": "su_c3_s1", "name": "تقرير الاستجابة للاحتياجات الطارئة للطلاب", "order": 68},
    {"id": "su_r069", "subcategory_id": "su_c3_s1", "name": "تقرير تعديل أولويات الإشراف", "order": 69},
    {"id": "su_r070", "subcategory_id": "su_c3_s1", "name": "تقرير مرونة إدارة الوقت", "order": 70},

    # المرونة - تعديل الخطط الإشرافية وفق المستجدات (su_c3_s2)
    {"id": "su_r071", "subcategory_id": "su_c3_s2", "name": "تقرير تحديث خطة الإشراف بعد التقويم الأول", "order": 71},
    {"id": "su_r072", "subcategory_id": "su_c3_s2", "name": "تقرير إعادة جدولة الزيارات وفق الظروف", "order": 72},
    {"id": "su_r073", "subcategory_id": "su_c3_s2", "name": "تقرير تعديل البرامج التدريبية بناء على الاحتياج", "order": 73},
    {"id": "su_r074", "subcategory_id": "su_c3_s2", "name": "تقرير مراجعة الأولويات بعد نتائج الاختبارات", "order": 74},
    {"id": "su_r075", "subcategory_id": "su_c3_s2", "name": "تقرير تكييف خطة الدعم للمعلمين", "order": 75},
    {"id": "su_r076", "subcategory_id": "su_c3_s2", "name": "تقرير تعديل استراتيجيات المتابعة", "order": 76},
    {"id": "su_r077", "subcategory_id": "su_c3_s2", "name": "تقرير إعادة توزيع المهام الإشرافية", "order": 77},
    {"id": "su_r078", "subcategory_id": "su_c3_s2", "name": "تقرير مرونة خطط التحسين", "order": 78},
    {"id": "su_r079", "subcategory_id": "su_c3_s2", "name": "تقرير تعديل خطة الزيارات بعد التغذية الراجعة", "order": 79},
    {"id": "su_r080", "subcategory_id": "su_c3_s2", "name": "تقرير تكييف مشاريع التطوير", "order": 80},

    # المرونة - التكيف مع تحديثات المناهج (su_c3_s3)
    {"id": "su_r081", "subcategory_id": "su_c3_s3", "name": "تقرير استعداد المعلمين لتحديث المناهج", "order": 81},
    {"id": "su_r082", "subcategory_id": "su_c3_s3", "name": "تقرير تدريب المعلمين على المناهج المطورة", "order": 82},
    {"id": "su_r083", "subcategory_id": "su_c3_s3", "name": "تقرير تقييم تكيف الطلاب مع المناهج الجديدة", "order": 83},
    {"id": "su_r084", "subcategory_id": "su_c3_s3", "name": "تقرير مراجعة مصادر التعلم بعد التحديث", "order": 84},
    {"id": "su_r085", "subcategory_id": "su_c3_s3", "name": "تقرير دمج مهارات القرن 21 في المناهج", "order": 85},
    {"id": "su_r086", "subcategory_id": "su_c3_s3", "name": "تقرير متابعة تطبيق استراتيجيات تدريس المناهج الجديدة", "order": 86},
    {"id": "su_r087", "subcategory_id": "su_c3_s3", "name": "تقرير قياس أثر تحديث المناهج على النواتج", "order": 87},
    {"id": "su_r088", "subcategory_id": "su_c3_s3", "name": "تقرير تكييف خطط الدروس مع التحديثات", "order": 88},
    {"id": "su_r089", "subcategory_id": "su_c3_s3", "name": "تقرير تحديث أدوات التقويم", "order": 89},
    {"id": "su_r090", "subcategory_id": "su_c3_s3", "name": "تقرير مرونة المناهج في الفصول", "order": 90},

    # المبادرة - اقتراح مبادرات تطويرية (su_c4_s1)
    {"id": "su_r091", "subcategory_id": "su_c4_s1", "name": "تقرير مبادرة تحسين القراءة في المرحلة الابتدائية", "order": 91},
    {"id": "su_r092", "subcategory_id": "su_c4_s1", "name": "تقرير مشروع تطوير مهارات الكتابة", "order": 92},
    {"id": "su_r093", "subcategory_id": "su_c4_s1", "name": "تقرير مبادرة التعلم القائم على المشاريع", "order": 93},
    {"id": "su_r094", "subcategory_id": "su_c4_s1", "name": "تقرير ابتكار برنامج إرشاد مهني", "order": 94},
    {"id": "su_r095", "subcategory_id": "su_c4_s1", "name": "تقرير مبادرة دمج التكنولوجيا في التعليم", "order": 95},
    {"id": "su_r096", "subcategory_id": "su_c4_s1", "name": "تقرير مشروع تحسين البيئة الصفية", "order": 96},
    {"id": "su_r097", "subcategory_id": "su_c4_s1", "name": "تقرير مبادرة تنمية المهارات الحياتية", "order": 97},
    {"id": "su_r098", "subcategory_id": "su_c4_s1", "name": "تقرير ابتكار نظام متابعة إلكتروني", "order": 98},
    {"id": "su_r099", "subcategory_id": "su_c4_s1", "name": "تقرير مبادرة التعلم النشط", "order": 99},
    {"id": "su_r100", "subcategory_id": "su_c4_s1", "name": "تقرير مشروع تعزيز القيم", "order": 100},

    # المبادرة - استباق المشكلات التعليمية (su_c4_s2)
    {"id": "su_r101", "subcategory_id": "su_c4_s2", "name": "تقرير استباق ضعف التحصيل في الرياضيات", "order": 101},
    {"id": "su_r102", "subcategory_id": "su_c4_s2", "name": "تقرير تحديد مؤشرات التسرب المبكر", "order": 102},
    {"id": "su_r103", "subcategory_id": "su_c4_s2", "name": "تقرير تحليل صعوبات التعلم قبل التفاقم", "order": 103},
    {"id": "su_r104", "subcategory_id": "su_c4_s2", "name": "تقرير استباق مشكلات السلوك", "order": 104},
    {"id": "su_r105", "subcategory_id": "su_c4_s2", "name": "تقرير توقع تحديات المناهج الجديدة", "order": 105},
    {"id": "su_r106", "subcategory_id": "su_c4_s2", "name": "تقرير استباق نقص الموارد", "order": 106},
    {"id": "su_r107", "subcategory_id": "su_c4_s2", "name": "تقرير تحليل فجوات الأداء المبكر", "order": 107},
    {"id": "su_r108", "subcategory_id": "su_c4_s2", "name": "تقرير استباق مقاومة التغيير", "order": 108},
    {"id": "su_r109", "subcategory_id": "su_c4_s2", "name": "تقرير توقع احتياجات التدريب", "order": 109},
    {"id": "su_r110", "subcategory_id": "su_c4_s2", "name": "تقرير استباق مشكلات الاندماج", "order": 110},

    # المبادرة - تنفيذ حلول إشرافية مبتكرة (su_c4_s3)
    {"id": "su_r111", "subcategory_id": "su_c4_s3", "name": "تقرير تطبيق منصة إلكترونية للتواصل", "order": 111},
    {"id": "su_r112", "subcategory_id": "su_c4_s3", "name": "تقرير استخدام الذكاء الاصطناعي في تحليل الأداء", "order": 112},
    {"id": "su_r113", "subcategory_id": "su_c4_s3", "name": "تقرير تصميم ألعاب تعليمية", "order": 113},
    {"id": "su_r114", "subcategory_id": "su_c4_s3", "name": "تقرير تطبيق نظام الإشراف عن بعد", "order": 114},
    {"id": "su_r115", "subcategory_id": "su_c4_s3", "name": "تقرير ابتكار نموذج تقويم بديل", "order": 115},
    {"id": "su_r116", "subcategory_id": "su_c4_s3", "name": "تقرير توظيف الواقع المعزز في التدريس", "order": 116},
    {"id": "su_r117", "subcategory_id": "su_c4_s3", "name": "تقرير تطبيق مجتمعات التعلم الافتراضية", "order": 117},
    {"id": "su_r118", "subcategory_id": "su_c4_s3", "name": "تقرير استخدام تحليلات التعلم", "order": 118},
    {"id": "su_r119", "subcategory_id": "su_c4_s3", "name": "تقرير تصميم أدوات تقويم تفاعلية", "order": 119},
    {"id": "su_r120", "subcategory_id": "su_c4_s3", "name": "تقرير تطبيق نظام تحفيز مبتكر", "order": 120},

    # قيادة التغيير - إدارة عمليات التطوير التربوي (su_c5_s1)
    {"id": "su_r121", "subcategory_id": "su_c5_s1", "name": "تقرير خطة تطوير الأداء المدرسي", "order": 121},
    {"id": "su_r122", "subcategory_id": "su_c5_s1", "name": "تقرير تنفيذ مشروع تطوير المناهج", "order": 122},
    {"id": "su_r123", "subcategory_id": "su_c5_s1", "name": "تقرير إدارة برنامج تدريب المدربين", "order": 123},
    {"id": "su_r124", "subcategory_id": "su_c5_s1", "name": "تقرير متابعة تطبيق استراتيجيات التدريس الحديثة", "order": 124},
    {"id": "su_r125", "subcategory_id": "su_c5_s1", "name": "تقرير تقييم مشروع التطوير المهني", "order": 125},
    {"id": "su_r126", "subcategory_id": "su_c5_s1", "name": "تقرير إدارة مراجعة السياسات التعليمية", "order": 126},
    {"id": "su_r127", "subcategory_id": "su_c5_s1", "name": "تقرير تنفيذ مبادرات التحول الرقمي", "order": 127},
    {"id": "su_r128", "subcategory_id": "su_c5_s1", "name": "تقرير إدارة مشروع تحسين البيئة المدرسية", "order": 128},
    {"id": "su_r129", "subcategory_id": "su_c5_s1", "name": "تقرير متابعة دمج ذوي الاحتياجات", "order": 129},
    {"id": "su_r130", "subcategory_id": "su_c5_s1", "name": "تقرير تقييم أثر التطوير على النواتج", "order": 130},

    # قيادة التغيير - تحفيز المعلمين لتبني التغيير (su_c5_s2)
    {"id": "su_r131", "subcategory_id": "su_c5_s2", "name": "تقرير استراتيجيات تحفيز المعلمين للتجديد", "order": 131},
    {"id": "su_r132", "subcategory_id": "su_c5_s2", "name": "تقرير برنامج تقدير المعلمين المبدعين", "order": 132},
    {"id": "su_r133", "subcategory_id": "su_c5_s2", "name": "تقرير ورش تحفيز روح المبادرة", "order": 133},
    {"id": "su_r134", "subcategory_id": "su_c5_s2", "name": "تقرير قياس رضا المعلمين عن التغيير", "order": 134},
    {"id": "su_r135", "subcategory_id": "su_c5_s2", "name": "تقرير تأثير القدوة في تبني التغيير", "order": 135},
    {"id": "su_r136", "subcategory_id": "su_c5_s2", "name": "تقرير مشاركة المعلمين في صنع القرار", "order": 136},
    {"id": "su_r137", "subcategory_id": "su_c5_s2", "name": "تقرير تحفيز الابتكار في الفصول", "order": 137},
    {"id": "su_r138", "subcategory_id": "su_c5_s2", "name": "تقرير قصص نجاح في التغيير", "order": 138},
    {"id": "su_r139", "subcategory_id": "su_c5_s2", "name": "تقرير تحفيز التعلم الذاتي", "order": 139},
    {"id": "su_r140", "subcategory_id": "su_c5_s2", "name": "تقرير بناء ثقافة الابتكار", "order": 140},

    # قيادة التغيير - معالجة مقاومة التغيير (su_c5_s3)
    {"id": "su_r141", "subcategory_id": "su_c5_s3", "name": "تقرير تحليل أسباب مقاومة التغيير", "order": 141},
    {"id": "su_r142", "subcategory_id": "su_c5_s3", "name": "تقرير استراتيجيات التعامل مع المعارضين", "order": 142},
    {"id": "su_r143", "subcategory_id": "su_c5_s3", "name": "تقرير ورش التوعية بفوائد التغيير", "order": 143},
    {"id": "su_r144", "subcategory_id": "su_c5_s3", "name": "تقرير قياس مستويات التقبل", "order": 144},
    {"id": "su_r145", "subcategory_id": "su_c5_s3", "name": "تقرير دعم المتبنين الأوائل", "order": 145},
    {"id": "su_r146", "subcategory_id": "su_c5_s3", "name": "تقرير إشراك المقاومين في التخطيط", "order": 146},
    {"id": "su_r147", "subcategory_id": "su_c5_s3", "name": "تقرير معالجة المخاوف المهنية", "order": 147},
    {"id": "su_r148", "subcategory_id": "su_c5_s3", "name": "تقرير تأثير القيادة على تقبل التغيير", "order": 148},
    {"id": "su_r149", "subcategory_id": "su_c5_s3", "name": "تقرير تحسين التواصل أثناء التغيير", "order": 149},
    {"id": "su_r150", "subcategory_id": "su_c5_s3", "name": "تقرير متابعة تحول المقاومين إلى داعمين", "order": 150},

    # قيادة التغيير - تحقيق الرؤية التربوية (su_c5_s4)
    {"id": "su_r151", "subcategory_id": "su_c5_s4", "name": "تقرير مواءمة الخطط مع رؤية 2030", "order": 151},
    {"id": "su_r152", "subcategory_id": "su_c5_s4", "name": "تقرير ترجمة الرؤية إلى ممارسات صفية", "order": 152},
    {"id": "su_r153", "subcategory_id": "su_c5_s4", "name": "تقرير قياس مساهمة المدارس في الرؤية", "order": 153},
    {"id": "su_r154", "subcategory_id": "su_c5_s4", "name": "تقرير بناء خطط استراتيجية مدرسية", "order": 154},
    {"id": "su_r155", "subcategory_id": "su_c5_s4", "name": "تقرير مؤشرات تحقيق الرؤية", "order": 155},
    {"id": "su_r156", "subcategory_id": "su_c5_s4", "name": "تقرير نشر ثقافة الرؤية", "order": 156},
    {"id": "su_r157", "subcategory_id": "su_c5_s4", "name": "تقرير تكامل جهود الإشراف مع الرؤية", "order": 157},
    {"id": "su_r158", "subcategory_id": "su_c5_s4", "name": "تقرير مشاريع تحقيق الرؤية في المدارس", "order": 158},
    {"id": "su_r159", "subcategory_id": "su_c5_s4", "name": "تقرير قياس أثر الرؤية على الطلاب", "order": 159},
    {"id": "su_r160", "subcategory_id": "su_c5_s4", "name": "تقرير تحديث الرؤية المستقبلية", "order": 160},

    # تطوير وتمكين العاملين - تحديد الاحتياجات المهنية للمعلمين (su_c6_s1)
    {"id": "su_r161", "subcategory_id": "su_c6_s1", "name": "تقرير تحليل الاحتياجات التدريبية", "order": 161},
    {"id": "su_r162", "subcategory_id": "su_c6_s1", "name": "تقرير استطلاع احتياجات المعلمين", "order": 162},
    {"id": "su_r163", "subcategory_id": "su_c6_s1", "name": "تقرير تحديد الفجوات المهنية", "order": 163},
    {"id": "su_r164", "subcategory_id": "su_c6_s1", "name": "تقرير أولويات التطوير حسب المرحلة", "order": 164},
    {"id": "su_r165", "subcategory_id": "su_c6_s1", "name": "تقرير احتياجات المعلمين الجدد", "order": 165},
    {"id": "su_r166", "subcategory_id": "su_c6_s1", "name": "تقرير احتياجات التخصصات المختلفة", "order": 166},
    {"id": "su_r167", "subcategory_id": "su_c6_s1", "name": "تقرير متطلبات تطوير القيادات", "order": 167},
    {"id": "su_r168", "subcategory_id": "su_c6_s1", "name": "تقرير احتياجات التدريب عن بعد", "order": 168},
    {"id": "su_r169", "subcategory_id": "su_c6_s1", "name": "تقرير تحليل نتائج تقييم الأداء", "order": 169},
    {"id": "su_r170", "subcategory_id": "su_c6_s1", "name": "تقرير احتياجات الدعم الفني", "order": 170},

    # تطوير وتمكين العاملين - دعم النمو المهني (su_c6_s2)
    {"id": "su_r171", "subcategory_id": "su_c6_s2", "name": "تقرير تنفيذ برامج التطوير المهني", "order": 171},
    {"id": "su_r172", "subcategory_id": "su_c6_s2", "name": "تقرير متابعة خطط النمو الفردية", "order": 172},
    {"id": "su_r173", "subcategory_id": "su_c6_s2", "name": "تقرير فعالية الإرشاد المهني", "order": 173},
    {"id": "su_r174", "subcategory_id": "su_c6_s2", "name": "تقرير دعم المعلمين في البحث الإجرائي", "order": 174},
    {"id": "su_r175", "subcategory_id": "su_c6_s2", "name": "تقرير توفير مصادر التعلم", "order": 175},
    {"id": "su_r176", "subcategory_id": "su_c6_s2", "name": "تقرير تحفيز الدراسات العليا", "order": 176},
    {"id": "su_r177", "subcategory_id": "su_c6_s2", "name": "تقرير المشاركة في المؤتمرات", "order": 177},
    {"id": "su_r178", "subcategory_id": "su_c6_s2", "name": "تقرير تنمية المهارات القيادية", "order": 178},
    {"id": "su_r179", "subcategory_id": "su_c6_s2", "name": "تقرير متابعة أثر التدريب", "order": 179},
    {"id": "su_r180", "subcategory_id": "su_c6_s2", "name": "تقرير دعم الشهادات المهنية", "order": 180},

    # تطوير وتمكين العاملين - إعداد قيادات تعليمية (su_c6_s3)
    {"id": "su_r181", "subcategory_id": "su_c6_s3", "name": "تقرير برنامج إعداد قادة المستقبل", "order": 181},
    {"id": "su_r182", "subcategory_id": "su_c6_s3", "name": "تقرير تحديد المرشحين للقيادة", "order": 182},
    {"id": "su_r183", "subcategory_id": "su_c6_s3", "name": "تقرير تدريب القيادات المدرسية", "order": 183},
    {"id": "su_r184", "subcategory_id": "su_c6_s3", "name": "تقرير متابعة أداء القيادات الجديدة", "order": 184},
    {"id": "su_r185", "subcategory_id": "su_c6_s3", "name": "تقرير الإعداد لخلافات القيادة", "order": 185},
    {"id": "su_r186", "subcategory_id": "su_c6_s3", "name": "تقرير برنامج التظليل الوظيفي", "order": 186},
    {"id": "su_r187", "subcategory_id": "su_c6_s3", "name": "تقرير تقييم جاهزية القيادات", "order": 187},
    {"id": "su_r188", "subcategory_id": "su_c6_s3", "name": "تقرير دمج القيادات في المشاريع", "order": 188},
    {"id": "su_r189", "subcategory_id": "su_c6_s3", "name": "تقرير بناء خطط تعاقب", "order": 189},
    {"id": "su_r190", "subcategory_id": "su_c6_s3", "name": "تقرير أثر إعداد القيادات على المدارس", "order": 190},

    # التوجه الاستراتيجي - تحليل مؤشرات الأداء التعليمي (su_c7_s1)
    {"id": "su_r191", "subcategory_id": "su_c7_s1", "name": "تقرير تحليل نتائج الاختبارات الوطنية", "order": 191},
    {"id": "su_r192", "subcategory_id": "su_c7_s1", "name": "تقرير مؤشرات الأداء المدرسي", "order": 192},
    {"id": "su_r193", "subcategory_id": "su_c7_s1", "name": "تقرير تحليل نسب النجاح والرسوب", "order": 193},
    {"id": "su_r194", "subcategory_id": "su_c7_s1", "name": "تقرير تطور أداء المعلمين", "order": 194},
    {"id": "su_r195", "subcategory_id": "su_c7_s1", "name": "تقرير تحليل بيانات الحضور", "order": 195},
    {"id": "su_r196", "subcategory_id": "su_c7_s1", "name": "تقرير مؤشرات الانضباط المدرسي", "order": 196},
    {"id": "su_r197", "subcategory_id": "su_c7_s1", "name": "تقرير تحليل نتائج الأنشطة", "order": 197},
    {"id": "su_r198", "subcategory_id": "su_c7_s1", "name": "تقرير قياس رضا المستفيدين", "order": 198},
    {"id": "su_r199", "subcategory_id": "su_c7_s1", "name": "تقرير تحليل الفجوات", "order": 199},
    {"id": "su_r200", "subcategory_id": "su_c7_s1", "name": "تقرير اتجاهات الأداء عبر السنوات", "order": 200},

    # التوجه الاستراتيجي - مواءمة الخطط مع الأهداف الوطنية (su_c7_s2)
    {"id": "su_r201", "subcategory_id": "su_c7_s2", "name": "تقرير تكامل خطط الإشراف مع رؤية المملكة", "order": 201},
    {"id": "su_r202", "subcategory_id": "su_c7_s2", "name": "تقرير مواءمة المناهج مع الأهداف الوطنية", "order": 202},
    {"id": "su_r203", "subcategory_id": "su_c7_s2", "name": "تقرير دعم برامج تنمية القدرات", "order": 203},
    {"id": "su_r204", "subcategory_id": "su_c7_s2", "name": "تقرير مساهمة المدارس في الأولويات الوطنية", "order": 204},
    {"id": "su_r205", "subcategory_id": "su_c7_s2", "name": "تقرير تكامل المبادرات مع الاستراتيجيات", "order": 205},
    {"id": "su_r206", "subcategory_id": "su_c7_s2", "name": "تقرير قياس أثر التوجهات الوطنية", "order": 206},
    {"id": "su_r207", "subcategory_id": "su_c7_s2", "name": "تقرير توافق خطط التدريب مع الاحتياج الوطني", "order": 207},
    {"id": "su_r208", "subcategory_id": "su_c7_s2", "name": "تقرير دعم الهوية الوطنية في المدارس", "order": 208},
    {"id": "su_r209", "subcategory_id": "su_c7_s2", "name": "تقرير مواءمة مشاريع التحول", "order": 209},
    {"id": "su_r210", "subcategory_id": "su_c7_s2", "name": "تقرير مؤشرات تحقيق الأولويات", "order": 210},

    # التوجه الاستراتيجي - بناء خطط إشرافية طويلة المدى (su_c7_s3)
    {"id": "su_r211", "subcategory_id": "su_c7_s3", "name": "تقرير الخطة الاستراتيجية للإشراف", "order": 211},
    {"id": "su_r212", "subcategory_id": "su_c7_s3", "name": "تقرير تحليل البيئة المستقبلية", "order": 212},
    {"id": "su_r213", "subcategory_id": "su_c7_s3", "name": "تقرير تحديد الأولويات طويلة المدى", "order": 213},
    {"id": "su_r214", "subcategory_id": "su_c7_s3", "name": "تقرير بناء مؤشرات قياس للخطط", "order": 214},
    {"id": "su_r215", "subcategory_id": "su_c7_s3", "name": "تقرير استشراف التحديات المستقبلية", "order": 215},
    {"id": "su_r216", "subcategory_id": "su_c7_s3", "name": "تقرير مراجعة خطط التنمية", "order": 216},
    {"id": "su_r217", "subcategory_id": "su_c7_s3", "name": "تقرير تكامل الخطط مع الميزانيات", "order": 217},
    {"id": "su_r218", "subcategory_id": "su_c7_s3", "name": "تقرير تحديث الخطط بناء على المتغيرات", "order": 218},
    {"id": "su_r219", "subcategory_id": "su_c7_s3", "name": "تقرير قياس التقدم في الخطط", "order": 219},
    {"id": "su_r220", "subcategory_id": "su_c7_s3", "name": "تقرير إشراك المعنيين في التخطيط", "order": 220},

    # اتخاذ القرارات - دراسة البدائل المتاحة (su_c8_s1)
    {"id": "su_r221", "subcategory_id": "su_c8_s1", "name": "تقرير تحليل بدائل تطوير المناهج", "order": 221},
    {"id": "su_r222", "subcategory_id": "su_c8_s1", "name": "تقرير مقارنة استراتيجيات التدريس", "order": 222},
    {"id": "su_r223", "subcategory_id": "su_c8_s1", "name": "تقرير دراسة خيارات تحسين الأداء", "order": 223},
    {"id": "su_r224", "subcategory_id": "su_c8_s1", "name": "تقرير تقييم بدائل البرامج التدريبية", "order": 224},
    {"id": "su_r225", "subcategory_id": "su_c8_s1", "name": "تقرير دراسة جدوى المبادرات", "order": 225},
    {"id": "su_r226", "subcategory_id": "su_c8_s1", "name": "تقرير تحليل تكلفة البدائل", "order": 226},
    {"id": "su_r227", "subcategory_id": "su_c8_s1", "name": "تقرير استشارة الخبراء في القرارات", "order": 227},
    {"id": "su_r228", "subcategory_id": "su_c8_s1", "name": "تقرير مقارنة نماذج الإشراف", "order": 228},
    {"id": "su_r229", "subcategory_id": "su_c8_s1", "name": "تقرير تحليل المخاطر للبدائل", "order": 229},
    {"id": "su_r230", "subcategory_id": "su_c8_s1", "name": "تقرير توصيات بشأن البديل الأمثل", "order": 230},

    # اتخاذ القرارات - اتخاذ قرارات مبنية على بيانات (su_c8_s2)
    {"id": "su_r231", "subcategory_id": "su_c8_s2", "name": "تقرير قرار تحسين بناء على نتائج الطلاب", "order": 231},
    {"id": "su_r232", "subcategory_id": "su_c8_s2", "name": "تقرير استخدام البيانات في توجيه المعلمين", "order": 232},
    {"id": "su_r233", "subcategory_id": "su_c8_s2", "name": "تقرير تعديل الخطط بناء على المؤشرات", "order": 233},
    {"id": "su_r234", "subcategory_id": "su_c8_s2", "name": "تقرير توظيف تحليلات التعلم", "order": 234},
    {"id": "su_r235", "subcategory_id": "su_c8_s2", "name": "تقرير دعم القرار بالأدلة", "order": 235},
    {"id": "su_r236", "subcategory_id": "su_c8_s2", "name": "تقرير قياس أثر القرارات السابقة", "order": 236},
    {"id": "su_r237", "subcategory_id": "su_c8_s2", "name": "تقرير اتخاذ قرار بشأن موارد", "order": 237},
    {"id": "su_r238", "subcategory_id": "su_c8_s2", "name": "تقرير قرارات التقويم بناء على بيانات", "order": 238},
    {"id": "su_r239", "subcategory_id": "su_c8_s2", "name": "تقرير توثيق عملية اتخاذ القرار", "order": 239},
    {"id": "su_r240", "subcategory_id": "su_c8_s2", "name": "تقرير شفافية القرارات", "order": 240},

    # اتخاذ القرارات - تحمل مسؤولية نتائج القرار (su_c8_s3)
    {"id": "su_r241", "subcategory_id": "su_c8_s3", "name": "تقرير متابعة تنفيذ القرارات", "order": 241},
    {"id": "su_r242", "subcategory_id": "su_c8_s3", "name": "تقرير تقييم نتائج القرارات الإشرافية", "order": 242},
    {"id": "su_r243", "subcategory_id": "su_c8_s3", "name": "تقرير تحليل أسباب نجاح أو فشل القرارات", "order": 243},
    {"id": "su_r244", "subcategory_id": "su_c8_s3", "name": "تقرير مراجعة القرارات السابقة", "order": 244},
    {"id": "su_r245", "subcategory_id": "su_c8_s3", "name": "تقرير الاعتراف بالأخطاء وتصحيحها", "order": 245},
    {"id": "su_r246", "subcategory_id": "su_c8_s3", "name": "تقرير تحمل تبعات القرارات", "order": 246},
    {"id": "su_r247", "subcategory_id": "su_c8_s3", "name": "تقرير توثيق الدروس المستفادة", "order": 247},
    {"id": "su_r248", "subcategory_id": "su_c8_s3", "name": "تقرير تأثير القرارات على الطلاب", "order": 248},
    {"id": "su_r249", "subcategory_id": "su_c8_s3", "name": "تقرير مساءلة تنفيذ القرارات", "order": 249},
    {"id": "su_r250", "subcategory_id": "su_c8_s3", "name": "تقرير تحسين القرارات المستقبلية", "order": 250},
]

# ==========================================================
# قوالب البرومبت (محدثة بالهيكل المطلوب)
# ==========================================================

SUPERVISOR_ANALYTICAL_TEMPLATE = """
اكتب التقرير كما لو أنك سترفقه رسميًا ضمن ملف إنجاز مهني أو تقويم أداء معتمد، بصياغة واقعية تعكس ممارسة فعلية موثقة وليست طرحًا إنشائيًا عامًا.

{report_name}
{subcategory_name}
{criterion_name} {criterion_percentage}
{subject_line}
{grade_line}
{target_line}
{place_line}
{count_line}

[الهدف التربوي]
نص لا يتجاوز 25 كلمة.

[نبذة مختصرة]
نص لا يتجاوز 25 كلمة.

[إجراءات التنفيذ]
- نقطة أولى.
- نقطة ثانية.
- نقطة ثالثة.
- نقطة رابعة.

[الاستراتيجيات المستخدمة]
نص لا يتجاوز 25 كلمة.

[نقاط القوة]
نص لا يتجاوز 25 كلمة.

[نقاط التحسين]
نص لا يتجاوز 25 كلمة.

[التوصيات]
نص لا يتجاوز 25 كلمة.

ممنوع ترك أي حقل فارغ.
"""

SUPERVISOR_PROJECT_TEMPLATE = """
اكتب التقرير كما لو أنك سترفقه رسميًا ضمن ملف إنجاز مهني أو تقويم أداء معتمد، بصياغة واقعية تعكس ممارسة فعلية موثقة وليست طرحًا إنشائيًا عامًا.

{report_name}
{subcategory_name}
{criterion_name} {criterion_percentage}
{subject_line}
{grade_line}
{target_line}
{place_line}
{count_line}

[الهدف التربوي]
نص لا يتجاوز 25 كلمة.

[نبذة مختصرة]
نص لا يتجاوز 25 كلمة.

[إجراءات التنفيذ]
- نقطة أولى.
- نقطة ثانية.
- نقطة ثالثة.
- نقطة رابعة.

[الاستراتيجيات المستخدمة]
نص لا يتجاوز 25 كلمة.

[نقاط القوة]
نص لا يتجاوز 25 كلمة.

[نقاط التحسين]
نص لا يتجاوز 25 كلمة.

[التوصيات]
نص لا يتجاوز 25 كلمة.

ممنوع ترك أي حقل فارغ.
"""

SUPERVISOR_SUPPORT_TEMPLATE = """
اكتب التقرير كما لو أنك سترفقه رسميًا ضمن ملف إنجاز مهني أو تقويم أداء معتمد، بصياغة واقعية تعكس ممارسة فعلية موثقة وليست طرحًا إنشائيًا عامًا.

{report_name}
{subcategory_name}
{criterion_name} {criterion_percentage}
{subject_line}
{grade_line}
{target_line}
{place_line}
{count_line}

[الهدف التربوي]
نص لا يتجاوز 25 كلمة.

[نبذة مختصرة]
نص لا يتجاوز 25 كلمة.

[إجراءات التنفيذ]
- نقطة أولى.
- نقطة ثانية.
- نقطة ثالثة.
- نقطة رابعة.

[الاستراتيجيات المستخدمة]
نص لا يتجاوز 25 كلمة.

[نقاط القوة]
نص لا يتجاوز 25 كلمة.

[نقاط التحسين]
نص لا يتجاوز 25 كلمة.

[التوصيات]
نص لا يتجاوز 25 كلمة.

ممنوع ترك أي حقل فارغ.
"""