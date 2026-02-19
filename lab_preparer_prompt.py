# -*- coding: utf-8 -*-

# قائمة المعايير الرئيسية لمحضر المختبر
LAB_CRITERIA = [
    {"id": "lp_c1", "name": "أداء الواجبات الوظيفية", "order": 1},
    {"id": "lp_c2", "name": "التفاعل مع المجتمع المهني", "order": 2},
    {"id": "lp_c3", "name": "التفاعل مع أولياء الأمور", "order": 3},
    {"id": "lp_c4", "name": "التنوع في استراتيجيات التدريس", "order": 4},
    {"id": "lp_c5", "name": "تحسين نتائج المتعلمين", "order": 5},
    {"id": "lp_c6", "name": "إعداد خطة يومية لأنشطة المختبر", "order": 6},
    {"id": "lp_c7", "name": "المعرفة بالأسس والمفاهيم الفنية", "order": 7},
    {"id": "lp_c8", "name": "توفير المستلزمات اللازمة لأداء التجارب العلمية", "order": 8},
    {"id": "lp_c9", "name": "الالتزام بسياسات وإجراءات السلامة المهنية", "order": 9},
    {"id": "lp_c10", "name": "تجهيز وتنظيم المختبر", "order": 10},
    {"id": "lp_c11", "name": "إعداد تقارير فنية دورية", "order": 11},
    {"id": "lp_c12", "name": "إعداد تقارير عن الأجهزة والمستلزمات", "order": 12}
]

# التصنيفات الفرعية لمحضر المختبر
LAB_SUBCATEGORIES = [
    # lp_c1
    {"id": "lp_c1_s1", "criterion_id": "lp_c1", "name": "الالتزام بالأنظمة والتعليمات", "order": 1},
    {"id": "lp_c1_s2", "criterion_id": "lp_c1", "name": "تطبيق إجراءات العمل المعتمدة", "order": 2},
    {"id": "lp_c1_s3", "criterion_id": "lp_c1", "name": "المحافظة على العهد والأدوات", "order": 3},
    {"id": "lp_c1_s4", "criterion_id": "lp_c1", "name": "تنفيذ المهام المكلف بها بدقة", "order": 4},
    # lp_c2
    {"id": "lp_c2_s1", "criterion_id": "lp_c2", "name": "التعاون مع المعلمين في تنفيذ التجارب", "order": 1},
    {"id": "lp_c2_s2", "criterion_id": "lp_c2", "name": "المشاركة في الاجتماعات المهنية", "order": 2},
    {"id": "lp_c2_s3", "criterion_id": "lp_c2", "name": "تبادل الخبرات الفنية", "order": 3},
    {"id": "lp_c2_s4", "criterion_id": "lp_c2", "name": "دعم الأنشطة العلمية المدرسية", "order": 4},
    # lp_c3
    {"id": "lp_c3_s1", "criterion_id": "lp_c3", "name": "المشاركة في المعارض والفعاليات العلمية", "order": 1},
    {"id": "lp_c3_s2", "criterion_id": "lp_c3", "name": "دعم المبادرات التوعوية ذات العلاقة", "order": 2},
    {"id": "lp_c3_s3", "criterion_id": "lp_c3", "name": "المساهمة في تعزيز ثقافة السلامة", "order": 3},
    # lp_c4
    {"id": "lp_c4_s1", "criterion_id": "lp_c4", "name": "دعم تنفيذ التجارب العملية", "order": 1},
    {"id": "lp_c4_s2", "criterion_id": "lp_c4", "name": "تجهيز أنشطة تطبيقية متنوعة", "order": 2},
    {"id": "lp_c4_s3", "criterion_id": "lp_c4", "name": "مساعدة المعلمين في تفعيل الجانب العملي", "order": 3},
    # lp_c5
    {"id": "lp_c5_s1", "criterion_id": "lp_c5", "name": "تهيئة بيئة عملية داعمة للتعلم", "order": 1},
    {"id": "lp_c5_s2", "criterion_id": "lp_c5", "name": "توفير أدوات تساعد على الفهم التطبيقي", "order": 2},
    {"id": "lp_c5_s3", "criterion_id": "lp_c5", "name": "دعم التعلم بالممارسة", "order": 3},
    # lp_c6
    {"id": "lp_c6_s1", "criterion_id": "lp_c6", "name": "إعداد جدول منظم للتجارب", "order": 1},
    {"id": "lp_c6_s2", "criterion_id": "lp_c6", "name": "التنسيق المسبق مع المعلمين", "order": 2},
    {"id": "lp_c6_s3", "criterion_id": "lp_c6", "name": "تحديد الأدوات والمواد المطلوبة", "order": 3},
    # lp_c7
    {"id": "lp_c7_s1", "criterion_id": "lp_c7", "name": "الإلمام بالمفاهيم العلمية المرتبطة بالمقررات", "order": 1},
    {"id": "lp_c7_s2", "criterion_id": "lp_c7", "name": "تشغيل الأجهزة بكفاءة", "order": 2},
    {"id": "lp_c7_s3", "criterion_id": "lp_c7", "name": "تقديم الدعم الفني أثناء الحصص", "order": 3},
    # lp_c8
    {"id": "lp_c8_s1", "criterion_id": "lp_c8", "name": "تجهيز الأدوات والمواد مسبقًا", "order": 1},
    {"id": "lp_c8_s2", "criterion_id": "lp_c8", "name": "التأكد من صلاحية الأجهزة", "order": 2},
    {"id": "lp_c8_s3", "criterion_id": "lp_c8", "name": "توفير بدائل مناسبة عند الحاجة", "order": 3},
    # lp_c9
    {"id": "lp_c9_s1", "criterion_id": "lp_c9", "name": "تطبيق معايير الأمن والسلامة", "order": 1},
    {"id": "lp_c9_s2", "criterion_id": "lp_c9", "name": "توعية الطلاب بإجراءات السلامة", "order": 2},
    {"id": "lp_c9_s3", "criterion_id": "lp_c9", "name": "متابعة جاهزية أدوات الطوارئ", "order": 3},
    # lp_c10
    {"id": "lp_c10_s1", "criterion_id": "lp_c10", "name": "ترتيب الأجهزة وفق معايير السلامة", "order": 1},
    {"id": "lp_c10_s2", "criterion_id": "lp_c10", "name": "تنظيم بيئة العمل المختبرية", "order": 2},
    {"id": "lp_c10_s3", "criterion_id": "lp_c10", "name": "حفظ المواد بطريقة آمنة", "order": 3},
    # lp_c11
    {"id": "lp_c11_s1", "criterion_id": "lp_c11", "name": "توثيق الأنشطة المنفذة", "order": 1},
    {"id": "lp_c11_s2", "criterion_id": "lp_c11", "name": "إعداد تقارير عن حالة الأجهزة", "order": 2},
    {"id": "lp_c11_s3", "criterion_id": "lp_c11", "name": "رفع احتياجات الصيانة للإدارة", "order": 3},
    # lp_c12
    {"id": "lp_c12_s1", "criterion_id": "lp_c12", "name": "متابعة حالة الأجهزة", "order": 1},
    {"id": "lp_c12_s2", "criterion_id": "lp_c12", "name": "تحديد احتياجات الإحلال أو الصيانة", "order": 2},
    {"id": "lp_c12_s3", "criterion_id": "lp_c12", "name": "توثيق حركة العهد والمستهلكات", "order": 3}
]

# قائمة التقارير (تقريران لكل تصنيف فرعي)
LAB_REPORTS = [
    # lp_c1_s1
    {"id": "lp_c1_s1_r001", "subcategory_id": "lp_c1_s1", "name": "تقرير الالتزام بالأنظمة والتعليمات", "order": 1},
    {"id": "lp_c1_s1_r002", "subcategory_id": "lp_c1_s1", "name": "تقرير متابعة تطبيق التعليمات المنظمة لعمل المختبر", "order": 2},
    # lp_c1_s2
    {"id": "lp_c1_s2_r001", "subcategory_id": "lp_c1_s2", "name": "تقرير تطبيق إجراءات العمل المعتمدة", "order": 1},
    {"id": "lp_c1_s2_r002", "subcategory_id": "lp_c1_s2", "name": "تقرير مراجعة الإجراءات والتأكد من تنفيذها", "order": 2},
    # lp_c1_s3
    {"id": "lp_c1_s3_r001", "subcategory_id": "lp_c1_s3", "name": "تقرير المحافظة على العهد والأدوات", "order": 1},
    {"id": "lp_c1_s3_r002", "subcategory_id": "lp_c1_s3", "name": "تقرير جرد العهد السنوي", "order": 2},
    # lp_c1_s4
    {"id": "lp_c1_s4_r001", "subcategory_id": "lp_c1_s4", "name": "تقرير تنفيذ المهام المكلف بها بدقة", "order": 1},
    {"id": "lp_c1_s4_r002", "subcategory_id": "lp_c1_s4", "name": "تقرير إنجاز الأعمال الإدارية والفنية", "order": 2},

    # lp_c2_s1
    {"id": "lp_c2_s1_r001", "subcategory_id": "lp_c2_s1", "name": "تقرير التعاون مع المعلمين في تنفيذ التجارب", "order": 1},
    {"id": "lp_c2_s1_r002", "subcategory_id": "lp_c2_s1", "name": "تقرير التنسيق مع المعلمين لجدولة التجارب", "order": 2},
    # lp_c2_s2
    {"id": "lp_c2_s2_r001", "subcategory_id": "lp_c2_s2", "name": "تقرير المشاركة في الاجتماعات المهنية", "order": 1},
    {"id": "lp_c2_s2_r002", "subcategory_id": "lp_c2_s2", "name": "تقرير حضور ورش العمل واللقاءات الفنية", "order": 2},
    # lp_c2_s3
    {"id": "lp_c2_s3_r001", "subcategory_id": "lp_c2_s3", "name": "تقرير تبادل الخبرات الفنية", "order": 1},
    {"id": "lp_c2_s3_r002", "subcategory_id": "lp_c2_s3", "name": "تقرير نقل الخبرات للمعلمين الجدد", "order": 2},
    # lp_c2_s4
    {"id": "lp_c2_s4_r001", "subcategory_id": "lp_c2_s4", "name": "تقرير دعم الأنشطة العلمية المدرسية", "order": 1},
    {"id": "lp_c2_s4_r002", "subcategory_id": "lp_c2_s4", "name": "تقرير المشاركة في تنظيم معرض العلوم", "order": 2},

    # lp_c3_s1
    {"id": "lp_c3_s1_r001", "subcategory_id": "lp_c3_s1", "name": "تقرير المشاركة في المعارض والفعاليات العلمية", "order": 1},
    {"id": "lp_c3_s1_r002", "subcategory_id": "lp_c3_s1", "name": "تقرير إسهام المختبر في الفعاليات المدرسية", "order": 2},
    # lp_c3_s2
    {"id": "lp_c3_s2_r001", "subcategory_id": "lp_c3_s2", "name": "تقرير دعم المبادرات التوعوية ذات العلاقة", "order": 1},
    {"id": "lp_c3_s2_r002", "subcategory_id": "lp_c3_s2", "name": "تقرير المشاركة في برامج التوعية المجتمعية", "order": 2},
    # lp_c3_s3
    {"id": "lp_c3_s3_r001", "subcategory_id": "lp_c3_s3", "name": "تقرير المساهمة في تعزيز ثقافة السلامة", "order": 1},
    {"id": "lp_c3_s3_r002", "subcategory_id": "lp_c3_s3", "name": "تقرير نشر إجراءات السلامة بين الطلاب", "order": 2},

    # lp_c4_s1
    {"id": "lp_c4_s1_r001", "subcategory_id": "lp_c4_s1", "name": "تقرير دعم تنفيذ التجارب العملية", "order": 1},
    {"id": "lp_c4_s1_r002", "subcategory_id": "lp_c4_s1", "name": "تقرير مساعدة المعلم أثناء التجارب", "order": 2},
    # lp_c4_s2
    {"id": "lp_c4_s2_r001", "subcategory_id": "lp_c4_s2", "name": "تقرير تجهيز أنشطة تطبيقية متنوعة", "order": 1},
    {"id": "lp_c4_s2_r002", "subcategory_id": "lp_c4_s2", "name": "تقرير إعداد تجارب إضافية للمتميزين", "order": 2},
    # lp_c4_s3
    {"id": "lp_c4_s3_r001", "subcategory_id": "lp_c4_s3", "name": "تقرير مساعدة المعلمين في تفعيل الجانب العملي", "order": 1},
    {"id": "lp_c4_s3_r002", "subcategory_id": "lp_c4_s3", "name": "تقرير توفير الدعم الفني أثناء الحصص", "order": 2},

    # lp_c5_s1
    {"id": "lp_c5_s1_r001", "subcategory_id": "lp_c5_s1", "name": "تقرير تهيئة بيئة عملية داعمة للتعلم", "order": 1},
    {"id": "lp_c5_s1_r002", "subcategory_id": "lp_c5_s1", "name": "تقرير تنظيم المختبر ليسهل التعلم", "order": 2},
    # lp_c5_s2
    {"id": "lp_c5_s2_r001", "subcategory_id": "lp_c5_s2", "name": "تقرير توفير أدوات تساعد على الفهم التطبيقي", "order": 1},
    {"id": "lp_c5_s2_r002", "subcategory_id": "lp_c5_s2", "name": "تقرير توفير نماذج تعليمية وشرائح", "order": 2},
    # lp_c5_s3
    {"id": "lp_c5_s3_r001", "subcategory_id": "lp_c5_s3", "name": "تقرير دعم التعلم بالممارسة", "order": 1},
    {"id": "lp_c5_s3_r002", "subcategory_id": "lp_c5_s3", "name": "تقرير تشجيع الطلاب على التجريب", "order": 2},

    # lp_c6_s1
    {"id": "lp_c6_s1_r001", "subcategory_id": "lp_c6_s1", "name": "تقرير إعداد جدول منظم للتجارب", "order": 1},
    {"id": "lp_c6_s1_r002", "subcategory_id": "lp_c6_s1", "name": "تقرير التوزيع الأسبوعي للحصص العملية", "order": 2},
    # lp_c6_s2
    {"id": "lp_c6_s2_r001", "subcategory_id": "lp_c6_s2", "name": "تقرير التنسيق المسبق مع المعلمين", "order": 1},
    {"id": "lp_c6_s2_r002", "subcategory_id": "lp_c6_s2", "name": "تقرير اجتماعات التخطيط للتجارب", "order": 2},
    # lp_c6_s3
    {"id": "lp_c6_s3_r001", "subcategory_id": "lp_c6_s3", "name": "تقرير تحديد الأدوات والمواد المطلوبة", "order": 1},
    {"id": "lp_c6_s3_r002", "subcategory_id": "lp_c6_s3", "name": "تقرير قوائم المستلزمات الشهرية", "order": 2},

    # lp_c7_s1
    {"id": "lp_c7_s1_r001", "subcategory_id": "lp_c7_s1", "name": "تقرير الإلمام بالمفاهيم العلمية المرتبطة بالمقررات", "order": 1},
    {"id": "lp_c7_s1_r002", "subcategory_id": "lp_c7_s1", "name": "تقرير اطلاعه على المناهج الحديثة", "order": 2},
    # lp_c7_s2
    {"id": "lp_c7_s2_r001", "subcategory_id": "lp_c7_s2", "name": "تقرير تشغيل الأجهزة بكفاءة", "order": 1},
    {"id": "lp_c7_s2_r002", "subcategory_id": "lp_c7_s2", "name": "تقرير تدريب المعلمين على الأجهزة الجديدة", "order": 2},
    # lp_c7_s3
    {"id": "lp_c7_s3_r001", "subcategory_id": "lp_c7_s3", "name": "تقرير تقديم الدعم الفني أثناء الحصص", "order": 1},
    {"id": "lp_c7_s3_r002", "subcategory_id": "lp_c7_s3", "name": "تقرير حل المشكلات الفنية الطارئة", "order": 2},

    # lp_c8_s1
    {"id": "lp_c8_s1_r001", "subcategory_id": "lp_c8_s1", "name": "تقرير تجهيز الأدوات والمواد مسبقًا", "order": 1},
    {"id": "lp_c8_s1_r002", "subcategory_id": "lp_c8_s1", "name": "تقرير تحضير محاليل وتجارب قبل الحصة", "order": 2},
    # lp_c8_s2
    {"id": "lp_c8_s2_r001", "subcategory_id": "lp_c8_s2", "name": "تقرير التأكد من صلاحية الأجهزة", "order": 1},
    {"id": "lp_c8_s2_r002", "subcategory_id": "lp_c8_s2", "name": "تقرير فحص الأجهزة بشكل دوري", "order": 2},
    # lp_c8_s3
    {"id": "lp_c8_s3_r001", "subcategory_id": "lp_c8_s3", "name": "تقرير توفير بدائل مناسبة عند الحاجة", "order": 1},
    {"id": "lp_c8_s3_r002", "subcategory_id": "lp_c8_s3", "name": "تقرير إعداد تجارب بديلة في حال نقص المواد", "order": 2},

    # lp_c9_s1
    {"id": "lp_c9_s1_r001", "subcategory_id": "lp_c9_s1", "name": "تقرير تطبيق معايير الأمن والسلامة", "order": 1},
    {"id": "lp_c9_s1_r002", "subcategory_id": "lp_c9_s1", "name": "تقرير الالتزام بلوائح السلامة بالمختبر", "order": 2},
    # lp_c9_s2
    {"id": "lp_c9_s2_r001", "subcategory_id": "lp_c9_s2", "name": "تقرير توعية الطلاب بإجراءات السلامة", "order": 1},
    {"id": "lp_c9_s2_r002", "subcategory_id": "lp_c9_s2", "name": "تقرير تدريب الطلاب على ارتداء الواقيات", "order": 2},
    # lp_c9_s3
    {"id": "lp_c9_s3_r001", "subcategory_id": "lp_c9_s3", "name": "تقرير متابعة جاهزية أدوات الطوارئ", "order": 1},
    {"id": "lp_c9_s3_r002", "subcategory_id": "lp_c9_s3", "name": "تقرير صيانة طفايات الحريق والإسعافات", "order": 2},

    # lp_c10_s1
    {"id": "lp_c10_s1_r001", "subcategory_id": "lp_c10_s1", "name": "تقرير ترتيب الأجهزة وفق معايير السلامة", "order": 1},
    {"id": "lp_c10_s1_r002", "subcategory_id": "lp_c10_s1", "name": "تقرير تنظيم أماكن الأجهزة ووضوحها", "order": 2},
    # lp_c10_s2
    {"id": "lp_c10_s2_r001", "subcategory_id": "lp_c10_s2", "name": "تقرير تنظيم بيئة العمل المختبرية", "order": 1},
    {"id": "lp_c10_s2_r002", "subcategory_id": "lp_c10_s2", "name": "تقرير توزيع المساحات بشكل مناسب", "order": 2},
    # lp_c10_s3
    {"id": "lp_c10_s3_r001", "subcategory_id": "lp_c10_s3", "name": "تقرير حفظ المواد بطريقة آمنة", "order": 1},
    {"id": "lp_c10_s3_r002", "subcategory_id": "lp_c10_s3", "name": "تقرير ترتيب المواد الكيميائية وتصنيفها", "order": 2},

    # lp_c11_s1
    {"id": "lp_c11_s1_r001", "subcategory_id": "lp_c11_s1", "name": "تقرير توثيق الأنشطة المنفذة", "order": 1},
    {"id": "lp_c11_s1_r002", "subcategory_id": "lp_c11_s1", "name": "تقرير سجل التجارب المنفذة", "order": 2},
    # lp_c11_s2
    {"id": "lp_c11_s2_r001", "subcategory_id": "lp_c11_s2", "name": "تقرير إعداد تقارير عن حالة الأجهزة", "order": 1},
    {"id": "lp_c11_s2_r002", "subcategory_id": "lp_c11_s2", "name": "تقرير رصد أعطال الأجهزة", "order": 2},
    # lp_c11_s3
    {"id": "lp_c11_s3_r001", "subcategory_id": "lp_c11_s3", "name": "تقرير رفع احتياجات الصيانة للإدارة", "order": 1},
    {"id": "lp_c11_s3_r002", "subcategory_id": "lp_c11_s3", "name": "تقرير متابعة أعمال الصيانة المنجزة", "order": 2},

    # lp_c12_s1
    {"id": "lp_c12_s1_r001", "subcategory_id": "lp_c12_s1", "name": "تقرير متابعة حالة الأجهزة", "order": 1},
    {"id": "lp_c12_s1_r002", "subcategory_id": "lp_c12_s1", "name": "تقرير كفاءة الأجهزة الدورية", "order": 2},
    # lp_c12_s2
    {"id": "lp_c12_s2_r001", "subcategory_id": "lp_c12_s2", "name": "تقرير تحديد احتياجات الإحلال أو الصيانة", "order": 1},
    {"id": "lp_c12_s2_r002", "subcategory_id": "lp_c12_s2", "name": "تقرير خطة استبدال الأجهزة القديمة", "order": 2},
    # lp_c12_s3
    {"id": "lp_c12_s3_r001", "subcategory_id": "lp_c12_s3", "name": "تقرير توثيق حركة العهد والمستهلكات", "order": 1},
    {"id": "lp_c12_s3_r002", "subcategory_id": "lp_c12_s3", "name": "تقرير سجل الصادر والوارد للمختبر", "order": 2}
]

# قالب البرومبت الخاص بمحضر المختبر
LAB_PROMPT_TEMPLATE = """ = """أنت محضر مختبر علمي متمرس، مسؤول عن تجهيز المختبر وتوفير الدعم الفني للتجارب العملية وفق معايير السلامة.

المطلوب:
- عرض المعيار الوظيفي الرئيسي.
- عرض التصنيف الفرعي.
- كتابة تقرير مهني يوضح الإجراءات والممارسات المرتبطة بهذا التصنيف.

التقرير المطلوب: "{report_name}"
وهو يندرج تحت التصنيف الفرعي: "{subcategory_name}"
ضمن المعيار الوظيفي: "{criterion_name}"

{subject_line}
{lesson_line}
{grade_line}
{target_line}
{place_line}
{count_line}

ضوابط الكتابة:
- لغة تقنية واضحة ومتخصصة.
- إبراز دورك في تجهيز وإدارة المختبر.
- توضيح إجراءات الصيانة والسلامة المتبعة.
- الإشارة إلى التعاون مع المعلمين والجهات الخارجية.
- بيان كيفية توثيق الأعمال وإعداد التقارير.
- إبراز استخدام التقنيات الحديثة في المختبر.
- توضيح أثر جهودك على سير العملية التعليمية وسلامة الطلاب.
- صياغة عملية دقيقة من 5–7 أسطر.

**الحقول المطلوبة:**
1. الهدف المهني
2. نبذة مختصرة
3. إجراءات التنفيذ
4. الاستراتيجيات والأساليب
5. نقاط القوة
6. نقاط التحسين
7. التوصيات

يرجى تقديم الإجابة باللغة العربية الفصحى، وتنظيمها بحيث يكون كل حقل في سطر منفصل يبدأ برقمه فقط دون ذكر العنوان."""