# -*- coding: utf-8 -*-

# =========================
# المعايير الرئيسية (الجدارات القيادية) لمدير المدرسة - نموذج الأداء الوظيفي
# (الإصدار المحدث وفق المعايير الرسمية)
# =========================

PRINCIPAL_CRITERIA = [
    {"id": "pri_new_c1", "name": "أداء الواجبات الوظيفية", "order": 1, "weight": 5},
    {"id": "pri_new_c2", "name": "التفاعل مع المجتمع المهني", "order": 2, "weight": 5},
    {"id": "pri_new_c3", "name": "التفاعل مع أولياء الأمور", "order": 3, "weight": 5},
    {"id": "pri_new_c4", "name": "مرن وقادر على تنفيذ أعماله في ظل ظروف العمل المختلفة", "order": 4, "weight": 5},
    {"id": "pri_new_c5", "name": "يدعم ويشارك في المبادرات النوعية", "order": 5, "weight": 5},
    {"id": "pri_new_c6", "name": "يتخذ إجراءات تربوية تحقق الانضباط المدرسي", "order": 6, "weight": 5},
    {"id": "pri_new_c7", "name": "يدير الموارد في المدرسة بكفاءة", "order": 7, "weight": 5},
    {"id": "pri_new_c8", "name": "يعد خطة للتطوير المهني", "order": 8, "weight": 5},
    {"id": "pri_new_c9", "name": "يقدم التغذية الراجعة ويتابع تحقق مؤشرات الأداء الوظيفي", "order": 9, "weight": 5},
    {"id": "pri_new_c10", "name": "يدعم تنفيذ برامج التطوير المهني", "order": 10, "weight": 5},
    {"id": "pri_new_c11", "name": "يقيم أداء منسوبي المدرسة", "order": 11, "weight": 5},
    {"id": "pri_new_c12", "name": "ينفذ إجراءات علمية لتحسين نتائج التعلم", "order": 12, "weight": 15},
    {"id": "pri_new_c13", "name": "يسهم في تحسين مستوى أداء المدرسة", "order": 13, "weight": 10},
    {"id": "pri_new_c14", "name": "يعد الخطط المدرسية اللازمة", "order": 14, "weight": 5},
    {"id": "pri_new_c15", "name": "يتابع تنفيذ الخطط المدرسية بمختلف أنواعها", "order": 15, "weight": 5},
    {"id": "pri_new_c16", "name": "يهيئ الفرص والإمكانات الداعمة لمشاركة الطلاب", "order": 16, "weight": 5},
    {"id": "pri_new_c17", "name": "يوظف المنصات الرقمية وتطبيقاتها المعتمدة", "order": 17, "weight": 5},
    {"id": "pri_new_c18", "name": "يتابع تعزيز السلوك الإيجابي للطلاب", "order": 18, "weight": 5},
    {"id": "pri_new_c19", "name": "يهيئ بيئة مدرسية آمنة ومحفزة على التعلم", "order": 19, "weight": 5},
]

# =========================
# التصنيفات الفرعية (المؤشرات السلوكية تحت كل معيار)
# =========================

PRINCIPAL_SUBCATEGORIES = [
    # pri_new_c1 - أداء الواجبات الوظيفية
    {"id": "pri_new_c1_s1", "criterion_id": "pri_new_c1", "name": "الالتزام بالدوام وقواعد السلوك الوظيفي", "order": 1},
    {"id": "pri_new_c1_s2", "criterion_id": "pri_new_c1", "name": "الامتثال للأنظمة واللوائح والتعاميم", "order": 2},
    {"id": "pri_new_c1_s3", "criterion_id": "pri_new_c1", "name": "تنفيذ المهام وفق الصلاحيات المخولة", "order": 3},
    {"id": "pri_new_c1_s4", "criterion_id": "pri_new_c1", "name": "حماية بيانات المدرسة والمعلومات", "order": 4},

    # pri_new_c2 - التفاعل مع المجتمع المهني
    {"id": "pri_new_c2_s1", "criterion_id": "pri_new_c2", "name": "المشاركة الفاعلة في اللقاءات المهنية", "order": 1},
    {"id": "pri_new_c2_s2", "criterion_id": "pri_new_c2", "name": "دعم تبادل الخبرات بين المعلمين", "order": 2},
    {"id": "pri_new_c2_s3", "criterion_id": "pri_new_c2", "name": "نشر التجارب التربوية والممارسات المتميزة", "order": 3},
    {"id": "pri_new_c2_s4", "criterion_id": "pri_new_c2", "name": "تمثيل المدرسة في المحافل المهنية", "order": 4},

    # pri_new_c3 - التفاعل مع أولياء الأمور
    {"id": "pri_new_c3_s1", "criterion_id": "pri_new_c3", "name": "تفعيل قنوات الاتصال مع أولياء الأمور", "order": 1},
    {"id": "pri_new_c3_s2", "criterion_id": "pri_new_c3", "name": "عقد اجتماعات دورية مع مجلس الآباء", "order": 2},
    {"id": "pri_new_c3_s3", "criterion_id": "pri_new_c3", "name": "مناقشة نتائج الطلاب وتقارير الأداء", "order": 3},
    {"id": "pri_new_c3_s4", "criterion_id": "pri_new_c3", "name": "تعزيز الشراكة المجتمعية مع الأسر", "order": 4},

    # pri_new_c4 - مرونة وتكيف
    {"id": "pri_new_c4_s1", "criterion_id": "pri_new_c4", "name": "إدارة التحديات الطارئة ومواجهة الأزمات", "order": 1},
    {"id": "pri_new_c4_s2", "criterion_id": "pri_new_c4", "name": "التكيف مع المتغيرات التنظيمية والتعليمية", "order": 2},
    {"id": "pri_new_c4_s3", "criterion_id": "pri_new_c4", "name": "معالجة المشكلات الإدارية بحلول عملية", "order": 3},
    {"id": "pri_new_c4_s4", "criterion_id": "pri_new_c4", "name": "اتخاذ قرارات سريعة ومناسبة للمستجدات", "order": 4},

    # pri_new_c5 - دعم المبادرات النوعية
    {"id": "pri_new_c5_s1", "criterion_id": "pri_new_c5", "name": "دعم التجارب والمشروعات التطويرية", "order": 1},
    {"id": "pri_new_c5_s2", "criterion_id": "pri_new_c5", "name": "دراسة التجارب الواردة من المدارس الأخرى", "order": 2},
    {"id": "pri_new_c5_s3", "criterion_id": "pri_new_c5", "name": "إعداد تقارير حول التجارب القابلة للتطبيق", "order": 3},
    {"id": "pri_new_c5_s4", "criterion_id": "pri_new_c5", "name": "نشر التجارب والمشروعات المتميزة", "order": 4},
    {"id": "pri_new_c5_s5", "criterion_id": "pri_new_c5", "name": "توظيف التقنية في متابعة المبادرات ونشرها", "order": 5},
    {"id": "pri_new_c5_s6", "criterion_id": "pri_new_c5", "name": "اقتراح بدائل تطويرية لتحسين المنتج", "order": 6},
    {"id": "pri_new_c5_s7", "criterion_id": "pri_new_c5", "name": "ابتكار حلول ومبادرات إبداعية للتحديات", "order": 7},

    # pri_new_c6 - إجراءات الانضباط المدرسي
    {"id": "pri_new_c6_s1", "criterion_id": "pri_new_c6", "name": "تطبيق قواعد السلوك والمواظبة", "order": 1},
    {"id": "pri_new_c6_s2", "criterion_id": "pri_new_c6", "name": "تنفيذ خطة الانضباط المدرسي", "order": 2},
    {"id": "pri_new_c6_s3", "criterion_id": "pri_new_c6", "name": "توثيق حالات الالتزام والمخالفات", "order": 3},
    {"id": "pri_new_c6_s4", "criterion_id": "pri_new_c6", "name": "تعزيز السلوكيات الإيجابية للطلاب", "order": 4},

    # pri_new_c7 - إدارة الموارد بكفاءة
    {"id": "pri_new_c7_s1", "criterion_id": "pri_new_c7", "name": "توظيف الموارد البشرية والمادية لتحقيق الأهداف", "order": 1},
    {"id": "pri_new_c7_s2", "criterion_id": "pri_new_c7", "name": "إدارة الميزانية التشغيلية بفاعلية", "order": 2},
    {"id": "pri_new_c7_s3", "criterion_id": "pri_new_c7", "name": "توزيع المهام وفق الكفاءة والتخصص", "order": 3},
    {"id": "pri_new_c7_s4", "criterion_id": "pri_new_c7", "name": "متابعة التقارير المالية والتدقيق", "order": 4},

    # pri_new_c8 - إعداد خطة التطوير المهني
    {"id": "pri_new_c8_s1", "criterion_id": "pri_new_c8", "name": "دعم تنفيذ برامج التطوير المهني وتقويمها", "order": 1},
    {"id": "pri_new_c8_s2", "criterion_id": "pri_new_c8", "name": "مساعدة المعلمين في وضع أهداف تطوير واضحة", "order": 2},
    {"id": "pri_new_c8_s3", "criterion_id": "pri_new_c8", "name": "تحليل مخرجات تقييم الأداء وتحديد جوانب القوة والتحسين", "order": 3},
    {"id": "pri_new_c8_s4", "criterion_id": "pri_new_c8", "name": "إعداد خطط تطوير بالشراكة مع المعنيين", "order": 4},
    {"id": "pri_new_c8_s5", "criterion_id": "pri_new_c8", "name": "ترشيح المعلمين للبرامج التدريبية", "order": 5},
    {"id": "pri_new_c8_s6", "criterion_id": "pri_new_c8", "name": "تقديم تغذية راجعة بناءة للمعلمين", "order": 6},
    {"id": "pri_new_c8_s7", "criterion_id": "pri_new_c8", "name": "تقويم البرامج التدريبية وقياس أثرها", "order": 7},
    {"id": "pri_new_c8_s8", "criterion_id": "pri_new_c8", "name": "إعداد ملفات الإنجاز ومتابعتها", "order": 8},

    # pri_new_c9 - التغذية الراجعة ومؤشرات الأداء
    {"id": "pri_new_c9_s1", "criterion_id": "pri_new_c9", "name": "مراجعة أداء الفترة السابقة وتحليله", "order": 1},
    {"id": "pri_new_c9_s2", "criterion_id": "pri_new_c9", "name": "قياس نسبة التقدم المحرز في المؤشرات", "order": 2},
    {"id": "pri_new_c9_s3", "criterion_id": "pri_new_c9", "name": "مناقشة التحديات مع الفريق", "order": 3},
    {"id": "pri_new_c9_s4", "criterion_id": "pri_new_c9", "name": "الاتفاق على إجراءات داعمة لتحقيق المستهدفات", "order": 4},
    {"id": "pri_new_c9_s5", "criterion_id": "pri_new_c9", "name": "إزالة المعوقات التي تعيق الأداء", "order": 5},
    {"id": "pri_new_c9_s6", "criterion_id": "pri_new_c9", "name": "تعزيز السلوكيات الفاعلة لدى العاملين", "order": 6},

    # pri_new_c10 - دعم تنفيذ برامج التطوير المهني
    {"id": "pri_new_c10_s1", "criterion_id": "pri_new_c10", "name": "متابعة تنفيذ البرامج التدريبية", "order": 1},
    {"id": "pri_new_c10_s2", "criterion_id": "pri_new_c10", "name": "قياس أثر التدريب على نواتج التعلم", "order": 2},
    {"id": "pri_new_c10_s3", "criterion_id": "pri_new_c10", "name": "دعم النمو المهني المستمر للمعلمين", "order": 3},
    {"id": "pri_new_c10_s4", "criterion_id": "pri_new_c10", "name": "توظيف نتائج التقييم في تحسين الأداء", "order": 4},

    # pri_new_c11 - تقييم أداء منسوبي المدرسة
    {"id": "pri_new_c11_s1", "criterion_id": "pri_new_c11", "name": "تقييم أداء المرؤوسين بأساليب علمية", "order": 1},
    {"id": "pri_new_c11_s2", "criterion_id": "pri_new_c11", "name": "استخدام أدوات تقويم متنوعة", "order": 2},
    {"id": "pri_new_c11_s3", "criterion_id": "pri_new_c11", "name": "ملاحظة الأداء (تخطيطاً – تنفيذاً – تقويماً)", "order": 3},
    {"id": "pri_new_c11_s4", "criterion_id": "pri_new_c11", "name": "تشجيع التقويم الذاتي للعاملين", "order": 4},
    {"id": "pri_new_c11_s5", "criterion_id": "pri_new_c11", "name": "توظيف نتائج التقويم في تحسين الأداء", "order": 5},
    {"id": "pri_new_c11_s6", "criterion_id": "pri_new_c11", "name": "اتخاذ قرارات مبنية على نتائج التقويم", "order": 6},

    # pri_new_c12 - إجراءات تحسين نتائج التعلم
    {"id": "pri_new_c12_s1", "criterion_id": "pri_new_c12", "name": "تشخيص أداء المعلمين وتصنيفهم", "order": 1},
    {"id": "pri_new_c12_s2", "criterion_id": "pri_new_c12", "name": "تفسير نتائج التعلم لتوجيه القرار", "order": 2},
    {"id": "pri_new_c12_s3", "criterion_id": "pri_new_c12", "name": "تقديم المعالجات التربوية للمتعثرين", "order": 3},
    {"id": "pri_new_c12_s4", "criterion_id": "pri_new_c12", "name": "رصد نمو المتعلمين دراسياً", "order": 4},
    {"id": "pri_new_c12_s5", "criterion_id": "pri_new_c12", "name": "تنمية المعارف والمهارات الأساسية", "order": 5},
    {"id": "pri_new_c12_s6", "criterion_id": "pri_new_c12", "name": "تطوير عمليات التعليم والتعلم", "order": 6},
    {"id": "pri_new_c12_s7", "criterion_id": "pri_new_c12", "name": "التواصل مع أولياء الأمور بشأن النتائج", "order": 7},

    # pri_new_c13 - تحسين مستوى أداء المدرسة
    {"id": "pri_new_c13_s1", "criterion_id": "pri_new_c13", "name": "رفع مستوى الأداء التعليمي", "order": 1},
    {"id": "pri_new_c13_s2", "criterion_id": "pri_new_c13", "name": "تحقيق المستهدفات الاستراتيجية", "order": 2},
    {"id": "pri_new_c13_s3", "criterion_id": "pri_new_c13", "name": "تحسين نتائج التعلم بشكل مستمر", "order": 3},
    {"id": "pri_new_c13_s4", "criterion_id": "pri_new_c13", "name": "متابعة مؤشرات التحسن المدرسي", "order": 4},
    {"id": "pri_new_c13_s5", "criterion_id": "pri_new_c13", "name": "معالجة جوانب القصور في الأداء", "order": 5},

    # pri_new_c14 - إعداد الخطط المدرسية
    {"id": "pri_new_c14_s1", "criterion_id": "pri_new_c14", "name": "إعداد الخطط المدرسية (التشغيلية والتحسينية)", "order": 1},
    {"id": "pri_new_c14_s2", "criterion_id": "pri_new_c14", "name": "توجيه الجهود لتحقيق استراتيجيات الوزارة", "order": 2},
    {"id": "pri_new_c14_s3", "criterion_id": "pri_new_c14", "name": "تهيئة الفرص والإمكانات الداعمة للخطط", "order": 3},
    {"id": "pri_new_c14_s4", "criterion_id": "pri_new_c14", "name": "توظيف المنصات الرقمية المعتمدة في التخطيط", "order": 4},
    {"id": "pri_new_c14_s5", "criterion_id": "pri_new_c14", "name": "دعم فاعلية المدرسة وتحسين الأداء عبر الخطط", "order": 5},

    # pri_new_c15 - متابعة تنفيذ الخطط
    {"id": "pri_new_c15_s1", "criterion_id": "pri_new_c15", "name": "متابعة تنفيذ الخطط التشغيلية", "order": 1},
    {"id": "pri_new_c15_s2", "criterion_id": "pri_new_c15", "name": "متابعة خطط التحسين والانضباط", "order": 2},
    {"id": "pri_new_c15_s3", "criterion_id": "pri_new_c15", "name": "متابعة خطط المعلمين", "order": 3},
    {"id": "pri_new_c15_s4", "criterion_id": "pri_new_c15", "name": "قياس أثر تنفيذ الخطط على الأداء", "order": 4},
    {"id": "pri_new_c15_s5", "criterion_id": "pri_new_c15", "name": "معالجة أوجه القصور في التنفيذ", "order": 5},

    # pri_new_c16 - تهيئة الفرص والإمكانات لمشاركة الطلاب
    {"id": "pri_new_c16_s1", "criterion_id": "pri_new_c16", "name": "دعم المشاركة الصفية واللاصفية", "order": 1},
    {"id": "pri_new_c16_s2", "criterion_id": "pri_new_c16", "name": "دعم المشاركات الداخلية والخارجية", "order": 2},
    {"id": "pri_new_c16_s3", "criterion_id": "pri_new_c16", "name": "تعزيز الأنشطة الطلابية", "order": 3},
    {"id": "pri_new_c16_s4", "criterion_id": "pri_new_c16", "name": "توثيق إنجازات الطلاب", "order": 4},

    # pri_new_c17 - توظيف المنصات الرقمية
    {"id": "pri_new_c17_s1", "criterion_id": "pri_new_c17", "name": "متابعة استخدام المنصات التعليمية", "order": 1},
    {"id": "pri_new_c17_s2", "criterion_id": "pri_new_c17", "name": "ضمان الالتزام بضوابط المنصات", "order": 2},
    {"id": "pri_new_c17_s3", "criterion_id": "pri_new_c17", "name": "دعم التعليم الرقمي في المدرسة", "order": 3},
    {"id": "pri_new_c17_s4", "criterion_id": "pri_new_c17", "name": "توظيف التقنية في عمليات التعليم والتعلم", "order": 4},

    # pri_new_c18 - تعزيز السلوك الإيجابي للطلاب
    {"id": "pri_new_c18_s1", "criterion_id": "pri_new_c18", "name": "متابعة برامج التوجيه الطلابي", "order": 1},
    {"id": "pri_new_c18_s2", "criterion_id": "pri_new_c18", "name": "معالجة الحالات الفردية للطلاب", "order": 2},
    {"id": "pri_new_c18_s3", "criterion_id": "pri_new_c18", "name": "إعداد تقارير التحسن السلوكي", "order": 3},
    {"id": "pri_new_c18_s4", "criterion_id": "pri_new_c18", "name": "تكريم الطلاب المتحسنين سلوكياً", "order": 4},

    # pri_new_c19 - بيئة مدرسية آمنة ومحفزة
    {"id": "pri_new_c19_s1", "criterion_id": "pri_new_c19", "name": "تحقيق معايير الأمن والسلامة", "order": 1},
    {"id": "pri_new_c19_s2", "criterion_id": "pri_new_c19", "name": "تمكين مجتمع المدرسة من تحقيق الأهداف", "order": 2},
    {"id": "pri_new_c19_s3", "criterion_id": "pri_new_c19", "name": "تحقيق التوقعات العالية لنواتج التعلم", "order": 3},
    {"id": "pri_new_c19_s4", "criterion_id": "pri_new_c19", "name": "توفير بيئة تعليمية جاذبة وآمنة نفسياً", "order": 4},
]

# =========================
# التقارير (10 تقارير لكل تصنيف فرعي)
# =========================

PRINCIPAL_REPORTS = [
    # pri_new_c1_s1 - الالتزام بالدوام وقواعد السلوك الوظيفي
    {"id": "pri_new_c1_s1_r01", "subcategory_id": "pri_new_c1_s1", "name": "تقرير الالتزام بمواعيد الحضور والانصراف", "order": 1},
    {"id": "pri_new_c1_s1_r02", "subcategory_id": "pri_new_c1_s1", "name": "تقرير متابعة تطبيق قواعد السلوك الوظيفي", "order": 2},
    {"id": "pri_new_c1_s1_r03", "subcategory_id": "pri_new_c1_s1", "name": "تقرير ضبط الدوام الرسمي للعاملين", "order": 3},
    {"id": "pri_new_c1_s1_r04", "subcategory_id": "pri_new_c1_s1", "name": "تقرير تقييم الالتزام بلباس العمل الرسمي", "order": 4},
    {"id": "pri_new_c1_s1_r05", "subcategory_id": "pri_new_c1_s1", "name": "تقرير متابعة الإجازات والغيابات", "order": 5},
    {"id": "pri_new_c1_s1_r06", "subcategory_id": "pri_new_c1_s1", "name": "تقرير سجل الحضور والانصراف الإلكتروني", "order": 6},
    {"id": "pri_new_c1_s1_r07", "subcategory_id": "pri_new_c1_s1", "name": "تقرير معالجة حالات التأخير والانصراف المبكر", "order": 7},
    {"id": "pri_new_c1_s1_r08", "subcategory_id": "pri_new_c1_s1", "name": "تقرير الالتزام بقواعد السلوك في الاجتماعات", "order": 8},
    {"id": "pri_new_c1_s1_r09", "subcategory_id": "pri_new_c1_s1", "name": "تقرير تقييم الانضباط الوظيفي للفريق", "order": 9},
    {"id": "pri_new_c1_s1_r10", "subcategory_id": "pri_new_c1_s1", "name": "تقرير تحليل مؤشرات الالتزام الشهري", "order": 10},

    # pri_new_c1_s2 - الامتثال للأنظمة واللوائح والتعاميم
    {"id": "pri_new_c1_s2_r01", "subcategory_id": "pri_new_c1_s2", "name": "تقرير متابعة تنفيذ التعاميم الوزارية", "order": 1},
    {"id": "pri_new_c1_s2_r02", "subcategory_id": "pri_new_c1_s2", "name": "تقرير الامتثال للوائح المالية والإدارية", "order": 2},
    {"id": "pri_new_c1_s2_r03", "subcategory_id": "pri_new_c1_s2", "name": "تقرير تدقيق الإجراءات وفق النظام", "order": 3},
    {"id": "pri_new_c1_s2_r04", "subcategory_id": "pri_new_c1_s2", "name": "تقرير الالتزام بسياسات الحماية من التمييز", "order": 4},
    {"id": "pri_new_c1_s2_r05", "subcategory_id": "pri_new_c1_s2", "name": "تقرير تطبيق لائحة تقويم الطلاب", "order": 5},
    {"id": "pri_new_c1_s2_r06", "subcategory_id": "pri_new_c1_s2", "name": "تقرير مراجعة القرارات الإدارية مع المستشار القانوني", "order": 6},
    {"id": "pri_new_c1_s2_r07", "subcategory_id": "pri_new_c1_s2", "name": "تقرير الالتزام بضوابط السلامة المهنية", "order": 7},
    {"id": "pri_new_c1_s2_r08", "subcategory_id": "pri_new_c1_s2", "name": "تقرير الامتثال لسياسة الخصوصية", "order": 8},
    {"id": "pri_new_c1_s2_r09", "subcategory_id": "pri_new_c1_s2", "name": "تقرير تحديث دليل الإجراءات باللوائح الجديدة", "order": 9},
    {"id": "pri_new_c1_s2_r10", "subcategory_id": "pri_new_c1_s2", "name": "تقرير تحليل مخاطر عدم الامتثال", "order": 10},

    # pri_new_c1_s3 - تنفيذ المهام وفق الصلاحيات المخولة
    {"id": "pri_new_c1_s3_r01", "subcategory_id": "pri_new_c1_s3", "name": "تقرير تفويض الصلاحيات للوكلاء", "order": 1},
    {"id": "pri_new_c1_s3_r02", "subcategory_id": "pri_new_c1_s3", "name": "تقرير تنفيذ المهام ضمن حدود الصلاحية", "order": 2},
    {"id": "pri_new_c1_s3_r03", "subcategory_id": "pri_new_c1_s3", "name": "تقرير الرقابة على تنفيذ الصلاحيات المالية", "order": 3},
    {"id": "pri_new_c1_s3_r04", "subcategory_id": "pri_new_c1_s3", "name": "تقرير التوثيق الرسمي للقرارات الإدارية", "order": 4},
    {"id": "pri_new_c1_s3_r05", "subcategory_id": "pri_new_c1_s3", "name": "تقرير الالتزام بإجراءات التعاقد والمشتريات", "order": 5},
    {"id": "pri_new_c1_s3_r06", "subcategory_id": "pri_new_c1_s3", "name": "تقرير مراجعة صلاحيات فريق العمل", "order": 6},
    {"id": "pri_new_c1_s3_r07", "subcategory_id": "pri_new_c1_s3", "name": "تقرير تدريب العاملين على حدود الصلاحيات", "order": 7},
    {"id": "pri_new_c1_s3_r08", "subcategory_id": "pri_new_c1_s3", "name": "تقرير حالات تجاوز الصلاحية (إن وجدت)", "order": 8},
    {"id": "pri_new_c1_s3_r09", "subcategory_id": "pri_new_c1_s3", "name": "تقرير تحديث وثيقة الصلاحيات", "order": 9},
    {"id": "pri_new_c1_s3_r10", "subcategory_id": "pri_new_c1_s3", "name": "تقرير تقييم فاعلية توزيع الصلاحيات", "order": 10},

    # pri_new_c1_s4 - حماية بيانات المدرسة والمعلومات
    {"id": "pri_new_c1_s4_r01", "subcategory_id": "pri_new_c1_s4", "name": "تقرير أمن البيانات الإلكترونية", "order": 1},
    {"id": "pri_new_c1_s4_r02", "subcategory_id": "pri_new_c1_s4", "name": "تقرير صلاحية الوصول للملفات الحساسة", "order": 2},
    {"id": "pri_new_c1_s4_r03", "subcategory_id": "pri_new_c1_s4", "name": "تقرير النسخ الاحتياطي لقواعد البيانات", "order": 3},
    {"id": "pri_new_c1_s4_r04", "subcategory_id": "pri_new_c1_s4", "name": "تقرير سياسة الخصوصية وحماية بيانات الطلاب", "order": 4},
    {"id": "pri_new_c1_s4_r05", "subcategory_id": "pri_new_c1_s4", "name": "تقرير تدريب العاملين على أمن المعلومات", "order": 5},
    {"id": "pri_new_c1_s4_r06", "subcategory_id": "pri_new_c1_s4", "name": "تقرير الالتزام بقوانين حماية البيانات", "order": 6},
    {"id": "pri_new_c1_s4_r07", "subcategory_id": "pri_new_c1_s4", "name": "تقرير حوادث اختراق البيانات (إن وجدت)", "order": 7},
    {"id": "pri_new_c1_s4_r08", "subcategory_id": "pri_new_c1_s4", "name": "تقرير تحديث كلمات المرور والدخول الآمن", "order": 8},
    {"id": "pri_new_c1_s4_r09", "subcategory_id": "pri_new_c1_s4", "name": "تقرير تصنيف المعلومات حسب الحساسية", "order": 9},
    {"id": "pri_new_c1_s4_r10", "subcategory_id": "pri_new_c1_s4", "name": "تقرير مراجعة سياسات أمن المعلومات", "order": 10},

    # pri_new_c2_s1 - المشاركة الفاعلة في اللقاءات المهنية
    {"id": "pri_new_c2_s1_r01", "subcategory_id": "pri_new_c2_s1", "name": "تقرير حضور اجتماعات مديري المدارس", "order": 1},
    {"id": "pri_new_c2_s1_r02", "subcategory_id": "pri_new_c2_s1", "name": "تقرير المشاركة في ورش عمل التطوير المهني", "order": 2},
    {"id": "pri_new_c2_s1_r03", "subcategory_id": "pri_new_c2_s1", "name": "تقرير تمثيل المدرسة في المؤتمرات التربوية", "order": 3},
    {"id": "pri_new_c2_s1_r04", "subcategory_id": "pri_new_c2_s1", "name": "تقرير المساهمة في اللجان المهنية", "order": 4},
    {"id": "pri_new_c2_s1_r05", "subcategory_id": "pri_new_c2_s1", "name": "تقرير تنظيم لقاءات مهنية داخل المدرسة", "order": 5},
    {"id": "pri_new_c2_s1_r06", "subcategory_id": "pri_new_c2_s1", "name": "تقرير التفاعل مع مشرفي مكتب التعليم", "order": 6},
    {"id": "pri_new_c2_s1_r07", "subcategory_id": "pri_new_c2_s1", "name": "تقرير المشاركة في مجتمعات التعلم المهنية", "order": 7},
    {"id": "pri_new_c2_s1_r08", "subcategory_id": "pri_new_c2_s1", "name": "تقرير حضور اللقاءات التعريفية بالمناهج الجديدة", "order": 8},
    {"id": "pri_new_c2_s1_r09", "subcategory_id": "pri_new_c2_s1", "name": "تقرير الإسهام في اللقاءات الإشرافية", "order": 9},
    {"id": "pri_new_c2_s1_r10", "subcategory_id": "pri_new_c2_s1", "name": "تقرير أثر المشاركة في اللقاءات على الأداء", "order": 10},

    # pri_new_c2_s2 - دعم تبادل الخبرات بين المعلمين
    {"id": "pri_new_c2_s2_r01", "subcategory_id": "pri_new_c2_s2", "name": "تقرير تنظيم زيارات تبادلية بين المعلمين", "order": 1},
    {"id": "pri_new_c2_s2_r02", "subcategory_id": "pri_new_c2_s2", "name": "تقرير حلقات النقاش المهنية", "order": 2},
    {"id": "pri_new_c2_s2_r03", "subcategory_id": "pri_new_c2_s2", "name": "تقرير تبادل خطط الدروس الناجحة", "order": 3},
    {"id": "pri_new_c2_s2_r04", "subcategory_id": "pri_new_c2_s2", "name": "تقرير منصة تبادل الخبرات الإلكترونية", "order": 4},
    {"id": "pri_new_c2_s2_r05", "subcategory_id": "pri_new_c2_s2", "name": "تقرير الإرشاد والتوجيه للمعلمين الجدد", "order": 5},
    {"id": "pri_new_c2_s2_r06", "subcategory_id": "pri_new_c2_s2", "name": "تقرير مجتمعات التعلم داخل المدرسة", "order": 6},
    {"id": "pri_new_c2_s2_r07", "subcategory_id": "pri_new_c2_s2", "name": "تقرير عقد ورش عمل بقيادة المعلمين", "order": 7},
    {"id": "pri_new_c2_s2_r08", "subcategory_id": "pri_new_c2_s2", "name": "تقرير توثيق الممارسات المتميزة للمعلمين", "order": 8},
    {"id": "pri_new_c2_s2_r09", "subcategory_id": "pri_new_c2_s2", "name": "تقرير تحفيز المعلمين لنقل الخبرات", "order": 9},
    {"id": "pri_new_c2_s2_r10", "subcategory_id": "pri_new_c2_s2", "name": "تقرير قياس أثر تبادل الخبرات على الأداء", "order": 10},

    # pri_new_c2_s3 - نشر التجارب التربوية والممارسات المتميزة
    {"id": "pri_new_c2_s3_r01", "subcategory_id": "pri_new_c2_s3", "name": "تقرير نشر قصص نجاح المدرسة عبر الموقع", "order": 1},
    {"id": "pri_new_c2_s3_r02", "subcategory_id": "pri_new_c2_s3", "name": "تقرير إصدار نشرات إلكترونية للممارسات", "order": 2},
    {"id": "pri_new_c2_s3_r03", "subcategory_id": "pri_new_c2_s3", "name": "تقرير المشاركة في المعارض التربوية", "order": 3},
    {"id": "pri_new_c2_s3_r04", "subcategory_id": "pri_new_c2_s3", "name": "تقرير توثيق التجارب في منصة الخبرات", "order": 4},
    {"id": "pri_new_c2_s3_r05", "subcategory_id": "pri_new_c2_s3", "name": "تقرير نشر أوراق عمل عن المبادرات", "order": 5},
    {"id": "pri_new_c2_s3_r06", "subcategory_id": "pri_new_c2_s3", "name": "تقرير استخدام وسائل التواصل لنشر التجارب", "order": 6},
    {"id": "pri_new_c2_s3_r07", "subcategory_id": "pri_new_c2_s3", "name": "تقرير تنظيم يوم المهنة المفتوح", "order": 7},
    {"id": "pri_new_c2_s3_r08", "subcategory_id": "pri_new_c2_s3", "name": "تقرير إعداد كتيبات عن التجارب الناجحة", "order": 8},
    {"id": "pri_new_c2_s3_r09", "subcategory_id": "pri_new_c2_s3", "name": "تقرير استضافة مدارس أخرى للاطلاع", "order": 9},
    {"id": "pri_new_c2_s3_r10", "subcategory_id": "pri_new_c2_s3", "name": "تقرير تحليل انتشار التجارب وأثرها", "order": 10},

    # pri_new_c2_s4 - تمثيل المدرسة في المحافل المهنية
    {"id": "pri_new_c2_s4_r01", "subcategory_id": "pri_new_c2_s4", "name": "تقرير المشاركة في ملتقى القيادات المدرسية", "order": 1},
    {"id": "pri_new_c2_s4_r02", "subcategory_id": "pri_new_c2_s4", "name": "تقرير حضور اللقاءات التنسيقية مع مكتب التعليم", "order": 2},
    {"id": "pri_new_c2_s4_r03", "subcategory_id": "pri_new_c2_s4", "name": "تقرير تمثيل المنطقة في المؤتمرات", "order": 3},
    {"id": "pri_new_c2_s4_r04", "subcategory_id": "pri_new_c2_s4", "name": "تقرير المشاركة في مجالس التدريب المهني", "order": 4},
    {"id": "pri_new_c2_s4_r05", "subcategory_id": "pri_new_c2_s4", "name": "تقرير التحدث في ندوات تربوية", "order": 5},
    {"id": "pri_new_c2_s4_r06", "subcategory_id": "pri_new_c2_s4", "name": "تقرير تمثيل المدرسة في اللجان الاستشارية", "order": 6},
    {"id": "pri_new_c2_s4_r07", "subcategory_id": "pri_new_c2_s4", "name": "تقرير المشاركة في تقييم المدارس الأخرى", "order": 7},
    {"id": "pri_new_c2_s4_r08", "subcategory_id": "pri_new_c2_s4", "name": "تقرير حضور اجتماعات الشراكة المجتمعية", "order": 8},
    {"id": "pri_new_c2_s4_r09", "subcategory_id": "pri_new_c2_s4", "name": "تقرير التنسيق مع الجهات الخارجية", "order": 9},
    {"id": "pri_new_c2_s4_r10", "subcategory_id": "pri_new_c2_s4", "name": "تقرير أثر التمثيل على سمعة المدرسة", "order": 10},

    # pri_new_c3_s1 - تفعيل قنوات الاتصال مع أولياء الأمور
    {"id": "pri_new_c3_s1_r01", "subcategory_id": "pri_new_c3_s1", "name": "تقرير استخدام تطبيق نور للتواصل", "order": 1},
    {"id": "pri_new_c3_s1_r02", "subcategory_id": "pri_new_c3_s1", "name": "تقرير قنوات الواتساب والتليجرام", "order": 2},
    {"id": "pri_new_c3_s1_r03", "subcategory_id": "pri_new_c3_s1", "name": "تقرير الموقع الإلكتروني للمدرسة", "order": 3},
    {"id": "pri_new_c3_s1_r04", "subcategory_id": "pri_new_c3_s1", "name": "تقرير البريد الإلكتروني للاستفسارات", "order": 4},
    {"id": "pri_new_c3_s1_r05", "subcategory_id": "pri_new_c3_s1", "name": "تقرير تفعيل خدمة الرسائل النصية", "order": 5},
    {"id": "pri_new_c3_s1_r06", "subcategory_id": "pri_new_c3_s1", "name": "تقرير استبيان رضا أولياء الأمور عن التواصل", "order": 6},
    {"id": "pri_new_c3_s1_r07", "subcategory_id": "pri_new_c3_s1", "name": "تقرير سرعة الاستجابة لاستفسارات الأسر", "order": 7},
    {"id": "pri_new_c3_s1_r08", "subcategory_id": "pri_new_c3_s1", "name": "تقرير تعدد اللغات في التواصل", "order": 8},
    {"id": "pri_new_c3_s1_r09", "subcategory_id": "pri_new_c3_s1", "name": "تقرير تطوير قنوات التواصل", "order": 9},
    {"id": "pri_new_c3_s1_r10", "subcategory_id": "pri_new_c3_s1", "name": "تقرير تحليل فاعلية قنوات التواصل", "order": 10},

    # pri_new_c3_s2 - عقد اجتماعات دورية مع مجلس الآباء
    {"id": "pri_new_c3_s2_r01", "subcategory_id": "pri_new_c3_s2", "name": "تقرير اجتماع مجلس الآباء الفصلي", "order": 1},
    {"id": "pri_new_c3_s2_r02", "subcategory_id": "pri_new_c3_s2", "name": "تقرير مناقشة خطة المدرسة مع المجلس", "order": 2},
    {"id": "pri_new_c3_s2_r03", "subcategory_id": "pri_new_c3_s2", "name": "تقرير مشاركة المجلس في الأنشطة", "order": 3},
    {"id": "pri_new_c3_s2_r04", "subcategory_id": "pri_new_c3_s2", "name": "تقرير انتخابات مجلس الآباء الجديد", "order": 4},
    {"id": "pri_new_c3_s2_r05", "subcategory_id": "pri_new_c3_s2", "name": "تقرير توصيات المجلس وتنفيذها", "order": 5},
    {"id": "pri_new_c3_s2_r06", "subcategory_id": "pri_new_c3_s2", "name": "تقرير محاضر اجتماعات المجلس", "order": 6},
    {"id": "pri_new_c3_s2_r07", "subcategory_id": "pri_new_c3_s2", "name": "تقرير تفعيل دور المجلس في المدرسة", "order": 7},
    {"id": "pri_new_c3_s2_r08", "subcategory_id": "pri_new_c3_s2", "name": "تقرير شراكات المجلس مع المجتمع", "order": 8},
    {"id": "pri_new_c3_s2_r09", "subcategory_id": "pri_new_c3_s2", "name": "تقرير تقييم أداء المجلس", "order": 9},
    {"id": "pri_new_c3_s2_r10", "subcategory_id": "pri_new_c3_s2", "name": "تقرير أثر اجتماعات المجلس على التحسين", "order": 10},

    # pri_new_c3_s3 - مناقشة نتائج الطلاب وتقارير الأداء
    {"id": "pri_new_c3_s3_r01", "subcategory_id": "pri_new_c3_s3", "name": "تقرير لقاءات أولياء الأمور بعد الاختبارات", "order": 1},
    {"id": "pri_new_c3_s3_r02", "subcategory_id": "pri_new_c3_s3", "name": "تقرير تسليم تقارير التقدم لأولياء الأمور", "order": 2},
    {"id": "pri_new_c3_s3_r03", "subcategory_id": "pri_new_c3_s3", "name": "تقرير شرح نتائج الطلاب للأسر", "order": 3},
    {"id": "pri_new_c3_s3_r04", "subcategory_id": "pri_new_c3_s3", "name": "تقرير مناقشة خطط التحسين مع الأسر", "order": 4},
    {"id": "pri_new_c3_s3_r05", "subcategory_id": "pri_new_c3_s3", "name": "تقرير توزيع كشوف الدرجات", "order": 5},
    {"id": "pri_new_c3_s3_r06", "subcategory_id": "pri_new_c3_s3", "name": "تقرير اجتماعات فردية لأولياء أمور المتعثرين", "order": 6},
    {"id": "pri_new_c3_s3_r07", "subcategory_id": "pri_new_c3_s3", "name": "تقرير استلام مقترحات الأسر بشأن النتائج", "order": 7},
    {"id": "pri_new_c3_s3_r08", "subcategory_id": "pri_new_c3_s3", "name": "تقرير توعية الأسر بدورهم في التحصيل", "order": 8},
    {"id": "pri_new_c3_s3_r09", "subcategory_id": "pri_new_c3_s3", "name": "تقرير تحليل ملاحظات الأسر حول النتائج", "order": 9},
    {"id": "pri_new_c3_s3_r10", "subcategory_id": "pri_new_c3_s3", "name": "تقرير قياس رضا الأسر عن التواصل", "order": 10},

    # pri_new_c3_s4 - تعزيز الشراكة المجتمعية مع الأسر
    {"id": "pri_new_c3_s4_r01", "subcategory_id": "pri_new_c3_s4", "name": "تقرير مشاركة الأسر في الفعاليات المدرسية", "order": 1},
    {"id": "pri_new_c3_s4_r02", "subcategory_id": "pri_new_c3_s4", "name": "تقرير برامج توعوية للأسر", "order": 2},
    {"id": "pri_new_c3_s4_r03", "subcategory_id": "pri_new_c3_s4", "name": "تقرير مساهمة الأسر في دعم الأنشطة", "order": 3},
    {"id": "pri_new_c3_s4_r04", "subcategory_id": "pri_new_c3_s4", "name": "تقرير يوم الأسرة المفتوح", "order": 4},
    {"id": "pri_new_c3_s4_r05", "subcategory_id": "pri_new_c3_s4", "name": "تقرير ورش عمل للأسر عن مهارات تربوية", "order": 5},
    {"id": "pri_new_c3_s4_r06", "subcategory_id": "pri_new_c3_s4", "name": "تقرير استضافة الأسر في لجان المدرسة", "order": 6},
    {"id": "pri_new_c3_s4_r07", "subcategory_id": "pri_new_c3_s4", "name": "تقرير مبادرات تطوعية للأسر", "order": 7},
    {"id": "pri_new_c3_s4_r08", "subcategory_id": "pri_new_c3_s4", "name": "تقرير شراكات مع مؤسسات المجتمع", "order": 8},
    {"id": "pri_new_c3_s4_r09", "subcategory_id": "pri_new_c3_s4", "name": "تقرير قياس أثر المشاركة المجتمعية", "order": 9},
    {"id": "pri_new_c3_s4_r10", "subcategory_id": "pri_new_c3_s4", "name": "تقرير تطوير خطة الشراكة مع الأسر", "order": 10},

    # pri_new_c4_s1 - إدارة التحديات الطارئة ومواجهة الأزمات
    {"id": "pri_new_c4_s1_r01", "subcategory_id": "pri_new_c4_s1", "name": "تقرير التعامل مع حالات الطقس السيئ", "order": 1},
    {"id": "pri_new_c4_s1_r02", "subcategory_id": "pri_new_c4_s1", "name": "تقرير إجراءات مواجهة نقص المعلمين المفاجئ", "order": 2},
    {"id": "pri_new_c4_s1_r03", "subcategory_id": "pri_new_c4_s1", "name": "تقرير خطة إخلاء المدرسة في الحالات الطارئة", "order": 3},
    {"id": "pri_new_c4_s1_r04", "subcategory_id": "pri_new_c4_s1", "name": "تقرير إدارة أزمة انتشار الأمراض", "order": 4},
    {"id": "pri_new_c4_s1_r05", "subcategory_id": "pri_new_c4_s1", "name": "تقرير التعامل مع انقطاع الخدمات", "order": 5},
    {"id": "pri_new_c4_s1_r06", "subcategory_id": "pri_new_c4_s1", "name": "تقرير إدارة الأزمات النفسية للطلاب", "order": 6},
    {"id": "pri_new_c4_s1_r07", "subcategory_id": "pri_new_c4_s1", "name": "تقرير التنسيق مع الجهات الخارجية في الأزمات", "order": 7},
    {"id": "pri_new_c4_s1_r08", "subcategory_id": "pri_new_c4_s1", "name": "تقرير تدريب الفريق على إدارة الأزمات", "order": 8},
    {"id": "pri_new_c4_s1_r09", "subcategory_id": "pri_new_c4_s1", "name": "تقرير تقييم الجاهزية للطوارئ", "order": 9},
    {"id": "pri_new_c4_s1_r10", "subcategory_id": "pri_new_c4_s1", "name": "تقرير توثيق الدروس المستفادة من الأزمات", "order": 10},

    # pri_new_c4_s2 - التكيف مع المتغيرات التنظيمية والتعليمية
    {"id": "pri_new_c4_s2_r01", "subcategory_id": "pri_new_c4_s2", "name": "تقرير تكيف المدرسة مع نظام التعليم عن بعد", "order": 1},
    {"id": "pri_new_c4_s2_r02", "subcategory_id": "pri_new_c4_s2", "name": "تقرير تطبيق التحديثات المنهجية الجديدة", "order": 2},
    {"id": "pri_new_c4_s2_r03", "subcategory_id": "pri_new_c4_s2", "name": "تقرير التكيف مع لوائح التقويم المحدثة", "order": 3},
    {"id": "pri_new_c4_s2_r04", "subcategory_id": "pri_new_c4_s2", "name": "تقرير مرونة الجدول المدرسي للتغيرات", "order": 4},
    {"id": "pri_new_c4_s2_r05", "subcategory_id": "pri_new_c4_s2", "name": "تقرير التعامل مع تغييرات الهيكل الإداري", "order": 5},
    {"id": "pri_new_c4_s2_r06", "subcategory_id": "pri_new_c4_s2", "name": "تقرير تكيف المعلمين مع استراتيجيات جديدة", "order": 6},
    {"id": "pri_new_c4_s2_r07", "subcategory_id": "pri_new_c4_s2", "name": "تقرير مواكبة متطلبات الاختبارات الدولية", "order": 7},
    {"id": "pri_new_c4_s2_r08", "subcategory_id": "pri_new_c4_s2", "name": "تقرير تكيف الإدارة مع سياسات الوزارة", "order": 8},
    {"id": "pri_new_c4_s2_r09", "subcategory_id": "pri_new_c4_s2", "name": "تقرير سرعة الاستجابة للتعاميم الجديدة", "order": 9},
    {"id": "pri_new_c4_s2_r10", "subcategory_id": "pri_new_c4_s2", "name": "تقرير تحسين المرونة التنظيمية", "order": 10},

    # pri_new_c4_s3 - معالجة المشكلات الإدارية بحلول عملية
    {"id": "pri_new_c4_s3_r01", "subcategory_id": "pri_new_c4_s3", "name": "تقرير حل مشكلة ازدحام الساحة الصباحية", "order": 1},
    {"id": "pri_new_c4_s3_r02", "subcategory_id": "pri_new_c4_s3", "name": "تقرير معالجة تأخر الحافلات المدرسية", "order": 2},
    {"id": "pri_new_c4_s3_r03", "subcategory_id": "pri_new_c4_s3", "name": "تقرير حل النزاعات بين المعلمين", "order": 3},
    {"id": "pri_new_c4_s3_r04", "subcategory_id": "pri_new_c4_s3", "name": "تقرير إجراءات تحسين النظافة بعد الشكاوى", "order": 4},
    {"id": "pri_new_c4_s3_r05", "subcategory_id": "pri_new_c4_s3", "name": "تقرير معالجة نقص الموارد في المختبر", "order": 5},
    {"id": "pri_new_c4_s3_r06", "subcategory_id": "pri_new_c4_s3", "name": "تقرير حل مشكلة تسرب الطلاب", "order": 6},
    {"id": "pri_new_c4_s3_r07", "subcategory_id": "pri_new_c4_s3", "name": "تقرير التعامل مع شكاوى أولياء الأمور", "order": 7},
    {"id": "pri_new_c4_s3_r08", "subcategory_id": "pri_new_c4_s3", "name": "تقرير إجراءات تحسين بيئة العمل للمعلمين", "order": 8},
    {"id": "pri_new_c4_s3_r09", "subcategory_id": "pri_new_c4_s3", "name": "تقرير معالجة تحديات الجدول المدرسي", "order": 9},
    {"id": "pri_new_c4_s3_r10", "subcategory_id": "pri_new_c4_s3", "name": "تقرير تحليل فعالية الحلول الإدارية", "order": 10},

    # pri_new_c4_s4 - اتخاذ قرارات سريعة ومناسبة للمستجدات
    {"id": "pri_new_c4_s4_r01", "subcategory_id": "pri_new_c4_s4", "name": "تقرير قرارات تحويل التعليم عن بعد أثناء العواصف", "order": 1},
    {"id": "pri_new_c4_s4_r02", "subcategory_id": "pri_new_c4_s4", "name": "تقرير قرار تغيير موعد الاختبارات لظروف طارئة", "order": 2},
    {"id": "pri_new_c4_s4_r03", "subcategory_id": "pri_new_c4_s4", "name": "تقرير قرارات سريعة لتعويض غياب المعلمين", "order": 3},
    {"id": "pri_new_c4_s4_r04", "subcategory_id": "pri_new_c4_s4", "name": "تقرير إجراءات فورية عند حدوث مشكلة أمنية", "order": 4},
    {"id": "pri_new_c4_s4_r05", "subcategory_id": "pri_new_c4_s4", "name": "تقرير قرارات توفير الدعم النفسي بعد حوادث", "order": 5},
    {"id": "pri_new_c4_s4_r06", "subcategory_id": "pri_new_c4_s4", "name": "تقرير قرارات تنظيم الدوام في رمضان", "order": 6},
    {"id": "pri_new_c4_s4_r07", "subcategory_id": "pri_new_c4_s4", "name": "تقرير قرارات استباقية للتعامل مع المتغيرات", "order": 7},
    {"id": "pri_new_c4_s4_r08", "subcategory_id": "pri_new_c4_s4", "name": "تقرير مراجعة القرارات المتخذة وتقييمها", "order": 8},
    {"id": "pri_new_c4_s4_r09", "subcategory_id": "pri_new_c4_s4", "name": "تقرير مشاركة الفريق في القرارات العاجلة", "order": 9},
    {"id": "pri_new_c4_s4_r10", "subcategory_id": "pri_new_c4_s4", "name": "تقرير أثر سرعة القرارات على استقرار المدرسة", "order": 10},

    # pri_new_c5_s1 - دعم التجارب والمشروعات التطويرية
    {"id": "pri_new_c5_s1_r01", "subcategory_id": "pri_new_c5_s1", "name": "تقرير دعم مشروع تحسين القراءة", "order": 1},
    {"id": "pri_new_c5_s1_r02", "subcategory_id": "pri_new_c5_s1", "name": "تقرير توفير موارد لمبادرة الرياضيات الذهنية", "order": 2},
    {"id": "pri_new_c5_s1_r03", "subcategory_id": "pri_new_c5_s1", "name": "تقرير احتضان تجربة التعلم القائم على المشاريع", "order": 3},
    {"id": "pri_new_c5_s1_r04", "subcategory_id": "pri_new_c5_s1", "name": "تقرير دمج التقنية في مشروع الإبداع العلمي", "order": 4},
    {"id": "pri_new_c5_s1_r05", "subcategory_id": "pri_new_c5_s1", "name": "تقرير دعم تجربة الفصول المقلوبة", "order": 5},
    {"id": "pri_new_c5_s1_r06", "subcategory_id": "pri_new_c5_s1", "name": "تقرير تخصيص حصص للمشروعات التطويرية", "order": 6},
    {"id": "pri_new_c5_s1_r07", "subcategory_id": "pri_new_c5_s1", "name": "تقرير تحفيز المعلمين على تقديم مشروعات", "order": 7},
    {"id": "pri_new_c5_s1_r08", "subcategory_id": "pri_new_c5_s1", "name": "تقرير متابعة تنفيذ المشروعات", "order": 8},
    {"id": "pri_new_c5_s1_r09", "subcategory_id": "pri_new_c5_s1", "name": "تقرير شراكات لدعم المشروعات", "order": 9},
    {"id": "pri_new_c5_s1_r10", "subcategory_id": "pri_new_c5_s1", "name": "تقرير قياس أثر المشروعات على الطلاب", "order": 10},

    # pri_new_c5_s2 - دراسة التجارب الواردة من المدارس الأخرى
    {"id": "pri_new_c5_s2_r01", "subcategory_id": "pri_new_c5_s2", "name": "تقرير زيارة مدرسة متميزة للاطلاع على تجاربها", "order": 1},
    {"id": "pri_new_c5_s2_r02", "subcategory_id": "pri_new_c5_s2", "name": "تقرير دراسة تجربة التدخلات العلاجية", "order": 2},
    {"id": "pri_new_c5_s2_r03", "subcategory_id": "pri_new_c5_s2", "name": "تقرير تحليل تجربة تحسين السلوك من مدرسة أخرى", "order": 3},
    {"id": "pri_new_c5_s2_r04", "subcategory_id": "pri_new_c5_s2", "name": "تقرير استضافة مدير مدرسة لعرض تجربته", "order": 4},
    {"id": "pri_new_c5_s2_r05", "subcategory_id": "pri_new_c5_s2", "name": "تقرير مراجعة تقارير التجارب الناجحة", "order": 5},
    {"id": "pri_new_c5_s2_r06", "subcategory_id": "pri_new_c5_s2", "name": "تقرير تقييم قابلية تطبيق التجارب", "order": 6},
    {"id": "pri_new_c5_s2_r07", "subcategory_id": "pri_new_c5_s2", "name": "تقرير مقارنة ممارسات مدارس أخرى", "order": 7},
    {"id": "pri_new_c5_s2_r08", "subcategory_id": "pri_new_c5_s2", "name": "تقرير استفادة المدرسة من تجارب خارجية", "order": 8},
    {"id": "pri_new_c5_s2_r09", "subcategory_id": "pri_new_c5_s2", "name": "تقرير تحديث قاعدة بيانات التجارب", "order": 9},
    {"id": "pri_new_c5_s2_r10", "subcategory_id": "pri_new_c5_s2", "name": "تقرير توصيات لتبني تجارب جديدة", "order": 10},

    # pri_new_c5_s3 - إعداد تقارير حول التجارب القابلة للتطبيق
    {"id": "pri_new_c5_s3_r01", "subcategory_id": "pri_new_c5_s3", "name": "تقرير توثيق تجربة الشراكة المجتمعية", "order": 1},
    {"id": "pri_new_c5_s3_r02", "subcategory_id": "pri_new_c5_s3", "name": "تقرير إعداد ملف التجارب المتميزة", "order": 2},
    {"id": "pri_new_c5_s3_r03", "subcategory_id": "pri_new_c5_s3", "name": "تقرير تحليل جدوى تطبيق تجربة معينة", "order": 3},
    {"id": "pri_new_c5_s3_r04", "subcategory_id": "pri_new_c5_s3", "name": "تقرير عرض تجارب المدارس على فريق القيادة", "order": 4},
    {"id": "pri_new_c5_s3_r05", "subcategory_id": "pri_new_c5_s3", "name": "تقرير توصيات بشأن التجارب الموصى بها", "order": 5},
    {"id": "pri_new_c5_s3_r06", "subcategory_id": "pri_new_c5_s3", "name": "تقرير تحديث تقارير التجارب سنوياً", "order": 6},
    {"id": "pri_new_c5_s3_r07", "subcategory_id": "pri_new_c5_s3", "name": "تقرير نشر التقارير على منصة المدرسة", "order": 7},
    {"id": "pri_new_c5_s3_r08", "subcategory_id": "pri_new_c5_s3", "name": "تقرير دراسة التكاليف والموارد للتجارب", "order": 8},
    {"id": "pri_new_c5_s3_r09", "subcategory_id": "pri_new_c5_s3", "name": "تقرير مقارنة التجارب المتشابهة", "order": 9},
    {"id": "pri_new_c5_s3_r10", "subcategory_id": "pri_new_c5_s3", "name": "تقرير أثر التقارير على اتخاذ القرار", "order": 10},

    # pri_new_c5_s4 - نشر التجارب والمشروعات المتميزة
    {"id": "pri_new_c5_s4_r01", "subcategory_id": "pri_new_c5_s4", "name": "تقرير نشر تجارب المدرسة في الملتقيات", "order": 1},
    {"id": "pri_new_c5_s4_r02", "subcategory_id": "pri_new_c5_s4", "name": "تقرير إصدار نشرة ربع سنوية للتجارب", "order": 2},
    {"id": "pri_new_c5_s4_r03", "subcategory_id": "pri_new_c5_s4", "name": "تقرير تغطية إعلامية للمشروعات المتميزة", "order": 3},
    {"id": "pri_new_c5_s4_r04", "subcategory_id": "pri_new_c5_s4", "name": "تقرير توثيق فيديوهات للمشروعات", "order": 4},
    {"id": "pri_new_c5_s4_r05", "subcategory_id": "pri_new_c5_s4", "name": "تقرير إنشاء صفحة للمشروعات على الموقع", "order": 5},
    {"id": "pri_new_c5_s4_r06", "subcategory_id": "pri_new_c5_s4", "name": "تقرير مشاركة التجارب في اليوم المهني", "order": 6},
    {"id": "pri_new_c5_s4_r07", "subcategory_id": "pri_new_c5_s4", "name": "تقرير إعداد ملصقات تعرض التجارب", "order": 7},
    {"id": "pri_new_c5_s4_r08", "subcategory_id": "pri_new_c5_s4", "name": "تقرير استضافة مدارس لنشر التجارب", "order": 8},
    {"id": "pri_new_c5_s4_r09", "subcategory_id": "pri_new_c5_s4", "name": "تقرير قياس مدى انتشار التجارب", "order": 9},
    {"id": "pri_new_c5_s4_r10", "subcategory_id": "pri_new_c5_s4", "name": "تقرير تطوير استراتيجيات النشر", "order": 10},

    # pri_new_c5_s5 - توظيف التقنية في متابعة المبادرات ونشرها
    {"id": "pri_new_c5_s5_r01", "subcategory_id": "pri_new_c5_s5", "name": "تقرير استخدام لوحة متابعة إلكترونية للمبادرات", "order": 1},
    {"id": "pri_new_c5_s5_r02", "subcategory_id": "pri_new_c5_s5", "name": "تقرير قناة يوتيوب لنشر المبادرات", "order": 2},
    {"id": "pri_new_c5_s5_r03", "subcategory_id": "pri_new_c5_s5", "name": "تقرير منصة إلكترونية لعرض التجارب", "order": 3},
    {"id": "pri_new_c5_s5_r04", "subcategory_id": "pri_new_c5_s5", "name": "تقرير استخدام وسائل التواصل في المتابعة", "order": 4},
    {"id": "pri_new_c5_s5_r05", "subcategory_id": "pri_new_c5_s5", "name": "تقرير تطبيق جوال لمتابعة المبادرات", "order": 5},
    {"id": "pri_new_c5_s5_r06", "subcategory_id": "pri_new_c5_s5", "name": "تقرير تحليل بيانات المبادرات إلكترونياً", "order": 6},
    {"id": "pri_new_c5_s5_r07", "subcategory_id": "pri_new_c5_s5", "name": "تقرير استطلاعات إلكترونية لقياس الأثر", "order": 7},
    {"id": "pri_new_c5_s5_r08", "subcategory_id": "pri_new_c5_s5", "name": "تقرير تحديث المحتوى الرقمي للمبادرات", "order": 8},
    {"id": "pri_new_c5_s5_r09", "subcategory_id": "pri_new_c5_s5", "name": "تقرير تدريب الفريق على استخدام التقنية", "order": 9},
    {"id": "pri_new_c5_s5_r10", "subcategory_id": "pri_new_c5_s5", "name": "تقرير أثر التقنية على نشر المبادرات", "order": 10},

    # pri_new_c5_s6 - اقتراح بدائل تطويرية لتحسين المنتج
    {"id": "pri_new_c5_s6_r01", "subcategory_id": "pri_new_c5_s6", "name": "تقرير اقتراح تحسينات على مشروع القراءة", "order": 1},
    {"id": "pri_new_c5_s6_r02", "subcategory_id": "pri_new_c5_s6", "name": "تقرير بدائل لتنفيذ البرامج العلاجية", "order": 2},
    {"id": "pri_new_c5_s6_r03", "subcategory_id": "pri_new_c5_s6", "name": "تقرير تطوير خطة الانضباط ببدائل جديدة", "order": 3},
    {"id": "pri_new_c5_s6_r04", "subcategory_id": "pri_new_c5_s6", "name": "تقرير مقترحات لتحسين بيئة التعلم", "order": 4},
    {"id": "pri_new_c5_s6_r05", "subcategory_id": "pri_new_c5_s6", "name": "تقرير بدائل لتفعيل الأنشطة الطلابية", "order": 5},
    {"id": "pri_new_c5_s6_r06", "subcategory_id": "pri_new_c5_s6", "name": "تقرير اقتراح أدوات تقويم بديلة", "order": 6},
    {"id": "pri_new_c5_s6_r07", "subcategory_id": "pri_new_c5_s6", "name": "تقرير بدائل لتنمية مهارات المعلمين", "order": 7},
    {"id": "pri_new_c5_s6_r08", "subcategory_id": "pri_new_c5_s6", "name": "تقرير تحسين عمليات الشراكة المجتمعية", "order": 8},
    {"id": "pri_new_c5_s6_r09", "subcategory_id": "pri_new_c5_s6", "name": "تقرير ورش عمل لمناقشة البدائل", "order": 9},
    {"id": "pri_new_c5_s6_r10", "subcategory_id": "pri_new_c5_s6", "name": "تقرير قياس فاعلية البدائل المقترحة", "order": 10},

    # pri_new_c5_s7 - ابتكار حلول ومبادرات إبداعية للتحديات
    {"id": "pri_new_c5_s7_r01", "subcategory_id": "pri_new_c5_s7", "name": "تقرير مبادرة النادي العلمي الافتراضي", "order": 1},
    {"id": "pri_new_c5_s7_r02", "subcategory_id": "pri_new_c5_s7", "name": "تقرير ابتكار برنامج تحفيزي للطلاب", "order": 2},
    {"id": "pri_new_c5_s7_r03", "subcategory_id": "pri_new_c5_s7", "name": "تقرير تطبيق نظام النقاط لمكافأة المعلمين", "order": 3},
    {"id": "pri_new_c5_s7_r04", "subcategory_id": "pri_new_c5_s7", "name": "تقرير مشروع التعلم عبر المشاريع", "order": 4},
    {"id": "pri_new_c5_s7_r05", "subcategory_id": "pri_new_c5_s7", "name": "تقرير ابتكار مسابقات داخلية لتعزيز القيم", "order": 5},
    {"id": "pri_new_c5_s7_r06", "subcategory_id": "pri_new_c5_s7", "name": "تقرير استخدام الذكاء الاصطناعي في متابعة الطلاب", "order": 6},
    {"id": "pri_new_c5_s7_r07", "subcategory_id": "pri_new_c5_s7", "name": "تقرير مبادرة أندية الأمهات", "order": 7},
    {"id": "pri_new_c5_s7_r08", "subcategory_id": "pri_new_c5_s7", "name": "تقرير ابتكار خطة إخلاء ذكية", "order": 8},
    {"id": "pri_new_c5_s7_r09", "subcategory_id": "pri_new_c5_s7", "name": "تقرير تحفيز الطلاب على الابتكار", "order": 9},
    {"id": "pri_new_c5_s7_r10", "subcategory_id": "pri_new_c5_s7", "name": "تقرير قياس أثر الابتكارات على الأداء", "order": 10},

    # pri_new_c6_s1 - تطبيق قواعد السلوك والمواظبة
    {"id": "pri_new_c6_s1_r01", "subcategory_id": "pri_new_c6_s1", "name": "تقرير تطبيق لائحة السلوك على الطلاب", "order": 1},
    {"id": "pri_new_c6_s1_r02", "subcategory_id": "pri_new_c6_s1", "name": "تقرير متابعة المواظبة اليومية", "order": 2},
    {"id": "pri_new_c6_s1_r03", "subcategory_id": "pri_new_c6_s1", "name": "تقرير حالات الغياب وتطبيق الإجراءات", "order": 3},
    {"id": "pri_new_c6_s1_r04", "subcategory_id": "pri_new_c6_s1", "name": "تقرير توثيق المخالفات في نظام نور", "order": 4},
    {"id": "pri_new_c6_s1_r05", "subcategory_id": "pri_new_c6_s1", "name": "تقرير توعية الطلاب بقواعد السلوك", "order": 5},
    {"id": "pri_new_c6_s1_r06", "subcategory_id": "pri_new_c6_s1", "name": "تقرير متابعة انضباط الفصول", "order": 6},
    {"id": "pri_new_c6_s1_r07", "subcategory_id": "pri_new_c6_s1", "name": "تقرير تطبيق الإجراءات على المخالفين", "order": 7},
    {"id": "pri_new_c6_s1_r08", "subcategory_id": "pri_new_c6_s1", "name": "تقرير تقييم فعالية تطبيق القواعد", "order": 8},
    {"id": "pri_new_c6_s1_r09", "subcategory_id": "pri_new_c6_s1", "name": "تقرير مراجعة لائحة السلوك مع المرشد", "order": 9},
    {"id": "pri_new_c6_s1_r10", "subcategory_id": "pri_new_c6_s1", "name": "تقرير تحليل بيانات الانضباط", "order": 10},

    # pri_new_c6_s2 - تنفيذ خطة الانضباط المدرسي
    {"id": "pri_new_c6_s2_r01", "subcategory_id": "pri_new_c6_s2", "name": "تقرير إعداد خطة الانضباط السنوية", "order": 1},
    {"id": "pri_new_c6_s2_r02", "subcategory_id": "pri_new_c6_s2", "name": "تقرير توزيع مهام الانضباط على الوكلاء", "order": 2},
    {"id": "pri_new_c6_s2_r03", "subcategory_id": "pri_new_c6_s2", "name": "تقرير جدول حصص الانتظار والانضباط", "order": 3},
    {"id": "pri_new_c6_s2_r04", "subcategory_id": "pri_new_c6_s2", "name": "تقرير متابعة تنفيذ خطة الانضباط", "order": 4},
    {"id": "pri_new_c6_s2_r05", "subcategory_id": "pri_new_c6_s2", "name": "تقرير تحديث خطة الانضباط", "order": 5},
    {"id": "pri_new_c6_s2_r06", "subcategory_id": "pri_new_c6_s2", "name": "تقرير إعلان خطة الانضباط للمجتمع", "order": 6},
    {"id": "pri_new_c6_s2_r07", "subcategory_id": "pri_new_c6_s2", "name": "تقرير تدريب المعلمين على تنفيذ الخطة", "order": 7},
    {"id": "pri_new_c6_s2_r08", "subcategory_id": "pri_new_c6_s2", "name": "تقرير تقييم تنفيذ الخطة", "order": 8},
    {"id": "pri_new_c6_s2_r09", "subcategory_id": "pri_new_c6_s2", "name": "تقرير تحديات تنفيذ خطة الانضباط", "order": 9},
    {"id": "pri_new_c6_s2_r10", "subcategory_id": "pri_new_c6_s2", "name": "تقرير أثر الخطة على تحسين السلوك", "order": 10},

    # pri_new_c6_s3 - توثيق حالات الالتزام والمخالفات
    {"id": "pri_new_c6_s3_r01", "subcategory_id": "pri_new_c6_s3", "name": "تقرير سجل يومي للمخالفات", "order": 1},
    {"id": "pri_new_c6_s3_r02", "subcategory_id": "pri_new_c6_s3", "name": "تقرير توثيق حالات التأخر الصباحي", "order": 2},
    {"id": "pri_new_c6_s3_r03", "subcategory_id": "pri_new_c6_s3", "name": "تقرير سجل الغياب الإلكتروني", "order": 3},
    {"id": "pri_new_c6_s3_r04", "subcategory_id": "pri_new_c6_s3", "name": "تقرير توثيق حالات السلوك الإيجابي", "order": 4},
    {"id": "pri_new_c6_s3_r05", "subcategory_id": "pri_new_c6_s3", "name": "تقرير إشعار أولياء الأمور بالمخالفات", "order": 5},
    {"id": "pri_new_c6_s3_r06", "subcategory_id": "pri_new_c6_s3", "name": "تقرير توثيق الإجراءات المتخذة", "order": 6},
    {"id": "pri_new_c6_s3_r07", "subcategory_id": "pri_new_c6_s3", "name": "تقرير تحديث قاعدة بيانات السلوك", "order": 7},
    {"id": "pri_new_c6_s3_r08", "subcategory_id": "pri_new_c6_s3", "name": "تقرير تحليل إحصائي للمخالفات", "order": 8},
    {"id": "pri_new_c6_s3_r09", "subcategory_id": "pri_new_c6_s3", "name": "تقرير سرية التوثيق", "order": 9},
    {"id": "pri_new_c6_s3_r10", "subcategory_id": "pri_new_c6_s3", "name": "تقرير استخدام التوثيق في التقويم", "order": 10},

    # pri_new_c6_s4 - تعزيز السلوكيات الإيجابية للطلاب
    {"id": "pri_new_c6_s4_r01", "subcategory_id": "pri_new_c6_s4", "name": "تقرير برنامج الطالب المثالي", "order": 1},
    {"id": "pri_new_c6_s4_r02", "subcategory_id": "pri_new_c6_s4", "name": "تقرير تكريم الفصل المثالي", "order": 2},
    {"id": "pri_new_c6_s4_r03", "subcategory_id": "pri_new_c6_s4", "name": "تقرير لوحة الشرف الإلكترونية", "order": 3},
    {"id": "pri_new_c6_s4_r04", "subcategory_id": "pri_new_c6_s4", "name": "تقرير جوائز السلوك الإيجابي", "order": 4},
    {"id": "pri_new_c6_s4_r05", "subcategory_id": "pri_new_c6_s4", "name": "تقرير ورش عمل عن القيم", "order": 5},
    {"id": "pri_new_c6_s4_r06", "subcategory_id": "pri_new_c6_s4", "name": "تقرير مسابقات أفضل سلوك", "order": 6},
    {"id": "pri_new_c6_s4_r07", "subcategory_id": "pri_new_c6_s4", "name": "تقرير تكريم أولياء الأمور المتميزين", "order": 7},
    {"id": "pri_new_c6_s4_r08", "subcategory_id": "pri_new_c6_s4", "name": "تقرير إشراك الطلاب في تعزيز السلوك", "order": 8},
    {"id": "pri_new_c6_s4_r09", "subcategory_id": "pri_new_c6_s4", "name": "تقرير قياس أثر التعزيز على السلوك", "order": 9},
    {"id": "pri_new_c6_s4_r10", "subcategory_id": "pri_new_c6_s4", "name": "تقرير تطوير برامج التعزيز", "order": 10},

    # pri_new_c7_s1 - توظيف الموارد البشرية والمادية لتحقيق الأهداف
    {"id": "pri_new_c7_s1_r01", "subcategory_id": "pri_new_c7_s1", "name": "تقرير توزيع المعلمين على الفصول", "order": 1},
    {"id": "pri_new_c7_s1_r02", "subcategory_id": "pri_new_c7_s1", "name": "تقرير استغلال المختبرات المدرسية", "order": 2},
    {"id": "pri_new_c7_s1_r03", "subcategory_id": "pri_new_c7_s1", "name": "تقرير استخدام التقنية في توفير الموارد", "order": 3},
    {"id": "pri_new_c7_s1_r04", "subcategory_id": "pri_new_c7_s1", "name": "تقرير تحسين استثمار المساحات", "order": 4},
    {"id": "pri_new_c7_s1_r05", "subcategory_id": "pri_new_c7_s1", "name": "تقرير توظيف الإداريين وفق الاختصاص", "order": 5},
    {"id": "pri_new_c7_s1_r06", "subcategory_id": "pri_new_c7_s1", "name": "تقرير متابعة كفاءة استخدام الموارد", "order": 6},
    {"id": "pri_new_c7_s1_r07", "subcategory_id": "pri_new_c7_s1", "name": "تقرير ترشيد استهلاك الكهرباء والماء", "order": 7},
    {"id": "pri_new_c7_s1_r08", "subcategory_id": "pri_new_c7_s1", "name": "تقرير الصيانة الدورية للمرافق", "order": 8},
    {"id": "pri_new_c7_s1_r09", "subcategory_id": "pri_new_c7_s1", "name": "تقرير خطط الطوارئ للحفاظ على الموارد", "order": 9},
    {"id": "pri_new_c7_s1_r10", "subcategory_id": "pri_new_c7_s1", "name": "تقرير قياس العائد من الموارد", "order": 10},

    # pri_new_c7_s2 - إدارة الميزانية التشغيلية بفاعلية
    {"id": "pri_new_c7_s2_r01", "subcategory_id": "pri_new_c7_s2", "name": "تقرير إعداد الميزانية السنوية", "order": 1},
    {"id": "pri_new_c7_s2_r02", "subcategory_id": "pri_new_c7_s2", "name": "تقرير الصرف على البرامج والأنشطة", "order": 2},
    {"id": "pri_new_c7_s2_r03", "subcategory_id": "pri_new_c7_s2", "name": "تقرير متابعة تنفيذ الميزانية", "order": 3},
    {"id": "pri_new_c7_s2_r04", "subcategory_id": "pri_new_c7_s2", "name": "تقرير تدقيق الحسابات الشهري", "order": 4},
    {"id": "pri_new_c7_s2_r05", "subcategory_id": "pri_new_c7_s2", "name": "تقرير ترشيد النفقات", "order": 5},
    {"id": "pri_new_c7_s2_r06", "subcategory_id": "pri_new_c7_s2", "name": "تقرير الإبلاغ عن الصرف للجهات المختصة", "order": 6},
    {"id": "pri_new_c7_s2_r07", "subcategory_id": "pri_new_c7_s2", "name": "تقرير تحليل الانحرافات المالية", "order": 7},
    {"id": "pri_new_c7_s2_r08", "subcategory_id": "pri_new_c7_s2", "name": "تقرير خطط توفير الموارد المالية", "order": 8},
    {"id": "pri_new_c7_s2_r09", "subcategory_id": "pri_new_c7_s2", "name": "تقرير الشفافية في الصرف", "order": 9},
    {"id": "pri_new_c7_s2_r10", "subcategory_id": "pri_new_c7_s2", "name": "تقرير تقييم كفاءة إدارة الميزانية", "order": 10},

    # pri_new_c7_s3 - توزيع المهام وفق الكفاءة والتخصص
    {"id": "pri_new_c7_s3_r01", "subcategory_id": "pri_new_c7_s3", "name": "تقرير توزيع الحصص على التخصصات", "order": 1},
    {"id": "pri_new_c7_s3_r02", "subcategory_id": "pri_new_c7_s3", "name": "تقرير تشكيل اللجان المدرسية", "order": 2},
    {"id": "pri_new_c7_s3_r03", "subcategory_id": "pri_new_c7_s3", "name": "تقرير تكليف قادة الأقسام", "order": 3},
    {"id": "pri_new_c7_s3_r04", "subcategory_id": "pri_new_c7_s3", "name": "تقرير توزيع أعمال الامتحانات", "order": 4},
    {"id": "pri_new_c7_s3_r05", "subcategory_id": "pri_new_c7_s3", "name": "تقرير مراجعة التوزيع مع نهاية العام", "order": 5},
    {"id": "pri_new_c7_s3_r06", "subcategory_id": "pri_new_c7_s3", "name": "تقرير تحسين التوزيع بناءً على الأداء", "order": 6},
    {"id": "pri_new_c7_s3_r07", "subcategory_id": "pri_new_c7_s3", "name": "تقرير مشاركة المعلمين في اختيار المهام", "order": 7},
    {"id": "pri_new_c7_s3_r08", "subcategory_id": "pri_new_c7_s3", "name": "تقرير تكافؤ الفرص في التوزيع", "order": 8},
    {"id": "pri_new_c7_s3_r09", "subcategory_id": "pri_new_c7_s3", "name": "تقرير قياس رضا العاملين عن التوزيع", "order": 9},
    {"id": "pri_new_c7_s3_r10", "subcategory_id": "pri_new_c7_s3", "name": "تقرير أثر التوزيع على الإنتاجية", "order": 10},

    # pri_new_c7_s4 - متابعة التقارير المالية والتدقيق
    {"id": "pri_new_c7_s4_r01", "subcategory_id": "pri_new_c7_s4", "name": "تقرير مراجعة الإيرادات والمصروفات", "order": 1},
    {"id": "pri_new_c7_s4_r02", "subcategory_id": "pri_new_c7_s4", "name": "تقرير تدقيق الفواتير والمشتريات", "order": 2},
    {"id": "pri_new_c7_s4_r03", "subcategory_id": "pri_new_c7_s4", "name": "تقرير متابعة الصندوق المدرسي", "order": 3},
    {"id": "pri_new_c7_s4_r04", "subcategory_id": "pri_new_c7_s4", "name": "تقرير تقارير نهاية العام المالي", "order": 4},
    {"id": "pri_new_c7_s4_r05", "subcategory_id": "pri_new_c7_s4", "name": "تقرير التزام الصرف باللوائح", "order": 5},
    {"id": "pri_new_c7_s4_r06", "subcategory_id": "pri_new_c7_s4", "name": "تقرير تدقيق داخلي دوري", "order": 6},
    {"id": "pri_new_c7_s4_r07", "subcategory_id": "pri_new_c7_s4", "name": "تقرير متابعة تحصيل الرسوم", "order": 7},
    {"id": "pri_new_c7_s4_r08", "subcategory_id": "pri_new_c7_s4", "name": "تقرير إعداد التقارير للجهات الرقابية", "order": 8},
    {"id": "pri_new_c7_s4_r09", "subcategory_id": "pri_new_c7_s4", "name": "تقرير تحليل التقارير المالية", "order": 9},
    {"id": "pri_new_c7_s4_r10", "subcategory_id": "pri_new_c7_s4", "name": "تقرير تحسين دقة التقارير المالية", "order": 10},

    # pri_new_c8_s1 - دعم تنفيذ برامج التطوير المهني وتقويمها
    {"id": "pri_new_c8_s1_r01", "subcategory_id": "pri_new_c8_s1", "name": "تقرير متابعة تنفيذ البرامج التدريبية", "order": 1},
    {"id": "pri_new_c8_s1_r02", "subcategory_id": "pri_new_c8_s1", "name": "تقرير تقويم البرامج من قبل المتدربين", "order": 2},
    {"id": "pri_new_c8_s1_r03", "subcategory_id": "pri_new_c8_s1", "name": "تقرير تحليل نتائج التقييم", "order": 3},
    {"id": "pri_new_c8_s1_r04", "subcategory_id": "pri_new_c8_s1", "name": "تقرير تحسين البرامج بناءً على التغذية", "order": 4},
    {"id": "pri_new_c8_s1_r05", "subcategory_id": "pri_new_c8_s1", "name": "تقرير توثيق أثر البرامج على الأداء", "order": 5},
    {"id": "pri_new_c8_s1_r06", "subcategory_id": "pri_new_c8_s1", "name": "تقرير استمرارية البرامج الناجحة", "order": 6},
    {"id": "pri_new_c8_s1_r07", "subcategory_id": "pri_new_c8_s1", "name": "تقرير تكريم المعلمين المشاركين", "order": 7},
    {"id": "pri_new_c8_s1_r08", "subcategory_id": "pri_new_c8_s1", "name": "تقرير متابعة تنفيذ البرامج عن بعد", "order": 8},
    {"id": "pri_new_c8_s1_r09", "subcategory_id": "pri_new_c8_s1", "name": "تقرير تحديث قاعدة بيانات التدريب", "order": 9},
    {"id": "pri_new_c8_s1_r10", "subcategory_id": "pri_new_c8_s1", "name": "تقرير تقييم العائد على التدريب", "order": 10},

    # pri_new_c8_s2 - مساعدة المعلمين في وضع أهداف تطوير واضحة
    {"id": "pri_new_c8_s2_r01", "subcategory_id": "pri_new_c8_s2", "name": "تقرير لقاءات توجيهية لوضع الأهداف", "order": 1},
    {"id": "pri_new_c8_s2_r02", "subcategory_id": "pri_new_c8_s2", "name": "تقرير نموذج خطة التطوير الذاتي", "order": 2},
    {"id": "pri_new_c8_s2_r03", "subcategory_id": "pri_new_c8_s2", "name": "تقرير مراجعة أهداف المعلمين", "order": 3},
    {"id": "pri_new_c8_s2_r04", "subcategory_id": "pri_new_c8_s2", "name": "تقرير ورش عمل عن كتابة الأهداف الذكية", "order": 4},
    {"id": "pri_new_c8_s2_r05", "subcategory_id": "pri_new_c8_s2", "name": "تقرير متابعة تحقيق الأهداف", "order": 5},
    {"id": "pri_new_c8_s2_r06", "subcategory_id": "pri_new_c8_s2", "name": "تقرير تعديل الأهداف حسب الاحتياجات", "order": 6},
    {"id": "pri_new_c8_s2_r07", "subcategory_id": "pri_new_c8_s2", "name": "تقرير تغذية راجعة حول الأهداف", "order": 7},
    {"id": "pri_new_c8_s2_r08", "subcategory_id": "pri_new_c8_s2", "name": "تقرير توثيق الأهداف في ملف الإنجاز", "order": 8},
    {"id": "pri_new_c8_s2_r09", "subcategory_id": "pri_new_c8_s2", "name": "تقرير قياس مدى وضوح الأهداف", "order": 9},
    {"id": "pri_new_c8_s2_r10", "subcategory_id": "pri_new_c8_s2", "name": "تقرير أثر الأهداف على التطوير", "order": 10},

    # pri_new_c8_s3 - تحليل مخرجات تقييم الأداء وتحديد جوانب القوة والتحسين
    {"id": "pri_new_c8_s3_r01", "subcategory_id": "pri_new_c8_s3", "name": "تقرير تحليل نتائج تقييم المعلمين", "order": 1},
    {"id": "pri_new_c8_s3_r02", "subcategory_id": "pri_new_c8_s3", "name": "تقرير تحديد نقاط القوة لدى المعلمين", "order": 2},
    {"id": "pri_new_c8_s3_r03", "subcategory_id": "pri_new_c8_s3", "name": "تقرير تحديد جوانب التحسين", "order": 3},
    {"id": "pri_new_c8_s3_r04", "subcategory_id": "pri_new_c8_s3", "name": "تقرير مقارنة الأداء بالسنوات السابقة", "order": 4},
    {"id": "pri_new_c8_s3_r05", "subcategory_id": "pri_new_c8_s3", "name": "تقرير تحليل الفجوات في المهارات", "order": 5},
    {"id": "pri_new_c8_s3_r06", "subcategory_id": "pri_new_c8_s3", "name": "تقرير عرض النتائج على المعلمين", "order": 6},
    {"id": "pri_new_c8_s3_r07", "subcategory_id": "pri_new_c8_s3", "name": "تقرير توصيات لتحسين الأداء", "order": 7},
    {"id": "pri_new_c8_s3_r08", "subcategory_id": "pri_new_c8_s3", "name": "تقرير توثيق نتائج التحليل", "order": 8},
    {"id": "pri_new_c8_s3_r09", "subcategory_id": "pri_new_c8_s3", "name": "تقرير استخدام التحليل في التخطيط", "order": 9},
    {"id": "pri_new_c8_s3_r10", "subcategory_id": "pri_new_c8_s3", "name": "تقرير قياس تطور الأداء بناءً على التحليل", "order": 10},

    # pri_new_c8_s4 - إعداد خطط تطوير بالشراكة مع المعنيين
    {"id": "pri_new_c8_s4_r01", "subcategory_id": "pri_new_c8_s4", "name": "تقرير ورش عمل تشاركية لإعداد الخطة", "order": 1},
    {"id": "pri_new_c8_s4_r02", "subcategory_id": "pri_new_c8_s4", "name": "تقرير إشراك قادة الأقسام في التخطيط", "order": 2},
    {"id": "pri_new_c8_s4_r03", "subcategory_id": "pri_new_c8_s4", "name": "تقرير تحديد أولويات التطوير مع الفريق", "order": 3},
    {"id": "pri_new_c8_s4_r04", "subcategory_id": "pri_new_c8_s4", "name": "تقرير اعتماد الخطة من المعلمين", "order": 4},
    {"id": "pri_new_c8_s4_r05", "subcategory_id": "pri_new_c8_s4", "name": "تقرير توثيق مقترحات المعلمين", "order": 5},
    {"id": "pri_new_c8_s4_r06", "subcategory_id": "pri_new_c8_s4", "name": "تقرير مراجعة الخطة مع المشرفين", "order": 6},
    {"id": "pri_new_c8_s4_r07", "subcategory_id": "pri_new_c8_s4", "name": "تقرير تحديث الخطة بناءً على التغذية", "order": 7},
    {"id": "pri_new_c8_s4_r08", "subcategory_id": "pri_new_c8_s4", "name": "تقرير إعلان الخطة للمجتمع المدرسي", "order": 8},
    {"id": "pri_new_c8_s4_r09", "subcategory_id": "pri_new_c8_s4", "name": "تقرير قياس رضا المعنيين عن الخطة", "order": 9},
    {"id": "pri_new_c8_s4_r10", "subcategory_id": "pri_new_c8_s4", "name": "تقرير أثر الشراكة على جودة الخطة", "order": 10},

    # pri_new_c8_s5 - ترشيح المعلمين للبرامج التدريبية
    {"id": "pri_new_c8_s5_r01", "subcategory_id": "pri_new_c8_s5", "name": "تقرير حصر الاحتياجات التدريبية", "order": 1},
    {"id": "pri_new_c8_s5_r02", "subcategory_id": "pri_new_c8_s5", "name": "تقرير ترشيح المعلمين لبرامج متخصصة", "order": 2},
    {"id": "pri_new_c8_s5_r03", "subcategory_id": "pri_new_c8_s5", "name": "تقرير متابعة تسجيل المعلمين في البرامج", "order": 3},
    {"id": "pri_new_c8_s5_r04", "subcategory_id": "pri_new_c8_s5", "name": "تقرير مفاضلة البرامج حسب الأولوية", "order": 4},
    {"id": "pri_new_c8_s5_r05", "subcategory_id": "pri_new_c8_s5", "name": "تقرير ترشيح المعلمين المتميزين لبرامج القيادة", "order": 5},
    {"id": "pri_new_c8_s5_r06", "subcategory_id": "pri_new_c8_s5", "name": "تقرير تخصيص ميزانية للترشيحات", "order": 6},
    {"id": "pri_new_c8_s5_r07", "subcategory_id": "pri_new_c8_s5", "name": "تقرير إفادة المعلمين بالبرامج المتاحة", "order": 7},
    {"id": "pri_new_c8_s5_r08", "subcategory_id": "pri_new_c8_s5", "name": "تقرير متابعة حضور البرامج", "order": 8},
    {"id": "pri_new_c8_s5_r09", "subcategory_id": "pri_new_c8_s5", "name": "تقرير تقييم فاعلية الترشيحات", "order": 9},
    {"id": "pri_new_c8_s5_r10", "subcategory_id": "pri_new_c8_s5", "name": "تقرير تحديث قاعدة بيانات التدريب", "order": 10},

    # pri_new_c8_s6 - تقديم تغذية راجعة بناءة للمعلمين
    {"id": "pri_new_c8_s6_r01", "subcategory_id": "pri_new_c8_s6", "name": "تقرير التغذية الراجعة بعد الزيارات الصفية", "order": 1},
    {"id": "pri_new_c8_s6_r02", "subcategory_id": "pri_new_c8_s6", "name": "تقرير جلسات التغذية الفردية", "order": 2},
    {"id": "pri_new_c8_s6_r03", "subcategory_id": "pri_new_c8_s6", "name": "تقرير ملاحظات مكتوبة للمعلمين", "order": 3},
    {"id": "pri_new_c8_s6_r04", "subcategory_id": "pri_new_c8_s6", "name": "تقرير تدريب القادة على التغذية الفاعلة", "order": 4},
    {"id": "pri_new_c8_s6_r05", "subcategory_id": "pri_new_c8_s6", "name": "تقرير متابعة تنفيذ توصيات التغذية", "order": 5},
    {"id": "pri_new_c8_s6_r06", "subcategory_id": "pri_new_c8_s6", "name": "تقرير استجابة المعلمين للتغذية", "order": 6},
    {"id": "pri_new_c8_s6_r07", "subcategory_id": "pri_new_c8_s6", "name": "تقرير توثيق التغذية الراجعة", "order": 7},
    {"id": "pri_new_c8_s6_r08", "subcategory_id": "pri_new_c8_s6", "name": "تقرير قياس رضا المعلمين عن التغذية", "order": 8},
    {"id": "pri_new_c8_s6_r09", "subcategory_id": "pri_new_c8_s6", "name": "تقرير أثر التغذية على تحسين الأداء", "order": 9},
    {"id": "pri_new_c8_s6_r10", "subcategory_id": "pri_new_c8_s6", "name": "تقرير تطوير أدوات التغذية", "order": 10},

    # pri_new_c8_s7 - تقويم البرامج التدريبية وقياس أثرها
    {"id": "pri_new_c8_s7_r01", "subcategory_id": "pri_new_c8_s7", "name": "تقرير استبيانات تقييم البرامج", "order": 1},
    {"id": "pri_new_c8_s7_r02", "subcategory_id": "pri_new_c8_s7", "name": "تقرير قياس تطبيق المهارات بعد التدريب", "order": 2},
    {"id": "pri_new_c8_s7_r03", "subcategory_id": "pri_new_c8_s7", "name": "تقرير تحليل العائد على التدريب", "order": 3},
    {"id": "pri_new_c8_s7_r04", "subcategory_id": "pri_new_c8_s7", "name": "تقرير متابعة تحسن الأداء الوظيفي", "order": 4},
    {"id": "pri_new_c8_s7_r05", "subcategory_id": "pri_new_c8_s7", "name": "تقرير مقارنة قبل وبعد التدريب", "order": 5},
    {"id": "pri_new_c8_s7_r06", "subcategory_id": "pri_new_c8_s7", "name": "تقرير تحديات تطبيق التدريب", "order": 6},
    {"id": "pri_new_c8_s7_r07", "subcategory_id": "pri_new_c8_s7", "name": "تقرير توصيات لتطوير البرامج", "order": 7},
    {"id": "pri_new_c8_s7_r08", "subcategory_id": "pri_new_c8_s7", "name": "تقرير توثيق أثر التدريب", "order": 8},
    {"id": "pri_new_c8_s7_r09", "subcategory_id": "pri_new_c8_s7", "name": "تقرير قياس استدامة أثر التدريب", "order": 9},
    {"id": "pri_new_c8_s7_r10", "subcategory_id": "pri_new_c8_s7", "name": "تقرير عرض نتائج التقويم على الجهات المعنية", "order": 10},

    # pri_new_c8_s8 - إعداد ملفات الإنجاز ومتابعتها
    {"id": "pri_new_c8_s8_r01", "subcategory_id": "pri_new_c8_s8", "name": "تقرير توثيق إنجازات المعلمين", "order": 1},
    {"id": "pri_new_c8_s8_r02", "subcategory_id": "pri_new_c8_s8", "name": "تقرير مراجعة ملفات الإنجاز", "order": 2},
    {"id": "pri_new_c8_s8_r03", "subcategory_id": "pri_new_c8_s8", "name": "تقرير إرشاد المعلمين لإعداد الملفات", "order": 3},
    {"id": "pri_new_c8_s8_r04", "subcategory_id": "pri_new_c8_s8", "name": "تقرير تقييم الملفات وفق معايير", "order": 4},
    {"id": "pri_new_c8_s8_r05", "subcategory_id": "pri_new_c8_s8", "name": "تقرير استخدام الملفات في التقويم", "order": 5},
    {"id": "pri_new_c8_s8_r06", "subcategory_id": "pri_new_c8_s8", "name": "تقرير توثيق الشهادات والدورات", "order": 6},
    {"id": "pri_new_c8_s8_r07", "subcategory_id": "pri_new_c8_s8", "name": "تقرير تحديث الملفات بشكل دوري", "order": 7},
    {"id": "pri_new_c8_s8_r08", "subcategory_id": "pri_new_c8_s8", "name": "تقرير حوسبة ملفات الإنجاز", "order": 8},
    {"id": "pri_new_c8_s8_r09", "subcategory_id": "pri_new_c8_s8", "name": "تقرير قياس جودة الملفات", "order": 9},
    {"id": "pri_new_c8_s8_r10", "subcategory_id": "pri_new_c8_s8", "name": "تقرير أثر الملفات على التطوير", "order": 10},

    # pri_new_c9_s1 - مراجعة أداء الفترة السابقة وتحليله
    {"id": "pri_new_c9_s1_r01", "subcategory_id": "pri_new_c9_s1", "name": "تقرير تحليل أداء الفصل الدراسي الأول", "order": 1},
    {"id": "pri_new_c9_s1_r02", "subcategory_id": "pri_new_c9_s1", "name": "تقرير مؤشرات الأداء الرئيسية", "order": 2},
    {"id": "pri_new_c9_s1_r03", "subcategory_id": "pri_new_c9_s1", "name": "تقرير مقارنة الأداء بالخطط", "order": 3},
    {"id": "pri_new_c9_s1_r04", "subcategory_id": "pri_new_c9_s1", "name": "تقرير تحديد الإنجازات والتحديات", "order": 4},
    {"id": "pri_new_c9_s1_r05", "subcategory_id": "pri_new_c9_s1", "name": "تقرير تحليل نتائج نهاية العام", "order": 5},
    {"id": "pri_new_c9_s1_r06", "subcategory_id": "pri_new_c9_s1", "name": "تقرير مراجعة أداء المعلمين", "order": 6},
    {"id": "pri_new_c9_s1_r07", "subcategory_id": "pri_new_c9_s1", "name": "تقرير تحليل تقارير الزيارات", "order": 7},
    {"id": "pri_new_c9_s1_r08", "subcategory_id": "pri_new_c9_s1", "name": "تقرير ورشة تحليل الأداء مع الفريق", "order": 8},
    {"id": "pri_new_c9_s1_r09", "subcategory_id": "pri_new_c9_s1", "name": "تقرير توثيق نتائج التحليل", "order": 9},
    {"id": "pri_new_c9_s1_r10", "subcategory_id": "pri_new_c9_s1", "name": "تقرير استخدام التحليل في التخطيط", "order": 10},

    # pri_new_c9_s2 - قياس نسبة التقدم المحرز في المؤشرات
    {"id": "pri_new_c9_s2_r01", "subcategory_id": "pri_new_c9_s2", "name": "تقرير نسبة إنجاز الخطة التشغيلية", "order": 1},
    {"id": "pri_new_c9_s2_r02", "subcategory_id": "pri_new_c9_s2", "name": "تقرير مؤشرات تحسن نواتج التعلم", "order": 2},
    {"id": "pri_new_c9_s2_r03", "subcategory_id": "pri_new_c9_s2", "name": "تقرير تقدم برامج التطوير المهني", "order": 3},
    {"id": "pri_new_c9_s2_r04", "subcategory_id": "pri_new_c9_s2", "name": "تقرير قياس رضا المستفيدين", "order": 4},
    {"id": "pri_new_c9_s2_r05", "subcategory_id": "pri_new_c9_s2", "name": "تقرير مؤشرات الانضباط", "order": 5},
    {"id": "pri_new_c9_s2_r06", "subcategory_id": "pri_new_c9_s2", "name": "تقرير قياس التقدم شهرياً", "order": 6},
    {"id": "pri_new_c9_s2_r07", "subcategory_id": "pri_new_c9_s2", "name": "تقرير تحليل الانحرافات", "order": 7},
    {"id": "pri_new_c9_s2_r08", "subcategory_id": "pri_new_c9_s2", "name": "تقرير عرض المؤشرات على القيادة", "order": 8},
    {"id": "pri_new_c9_s2_r09", "subcategory_id": "pri_new_c9_s2", "name": "تقرير تحديث المؤشرات دورياً", "order": 9},
    {"id": "pri_new_c9_s2_r10", "subcategory_id": "pri_new_c9_s2", "name": "تقرير استخدام المؤشرات لتحفيز الفريق", "order": 10},

    # pri_new_c9_s3 - مناقشة التحديات مع الفريق
    {"id": "pri_new_c9_s3_r01", "subcategory_id": "pri_new_c9_s3", "name": "تقرير اجتماع قيادة المدرسة لمناقشة التحديات", "order": 1},
    {"id": "pri_new_c9_s3_r02", "subcategory_id": "pri_new_c9_s3", "name": "تقرير ورشة حل المشكلات", "order": 2},
    {"id": "pri_new_c9_s3_r03", "subcategory_id": "pri_new_c9_s3", "name": "تقرير حصر التحديات التي تواجه الأقسام", "order": 3},
    {"id": "pri_new_c9_s3_r04", "subcategory_id": "pri_new_c9_s3", "name": "تقرير تحليل الأسباب الجذرية", "order": 4},
    {"id": "pri_new_c9_s3_r05", "subcategory_id": "pri_new_c9_s3", "name": "تقرير تحديد أولويات التحديات", "order": 5},
    {"id": "pri_new_c9_s3_r06", "subcategory_id": "pri_new_c9_s3", "name": "تقرير اقتراح حلول من الفريق", "order": 6},
    {"id": "pri_new_c9_s3_r07", "subcategory_id": "pri_new_c9_s3", "name": "تقرير توثيق مخرجات المناقشات", "order": 7},
    {"id": "pri_new_c9_s3_r08", "subcategory_id": "pri_new_c9_s3", "name": "تقرير متابعة تنفيذ الحلول", "order": 8},
    {"id": "pri_new_c9_s3_r09", "subcategory_id": "pri_new_c9_s3", "name": "تقرير قياس فعالية المناقشات", "order": 9},
    {"id": "pri_new_c9_s3_r10", "subcategory_id": "pri_new_c9_s3", "name": "تقرير تحسين آليات المناقشة", "order": 10},

    # pri_new_c9_s4 - الاتفاق على إجراءات داعمة لتحقيق المستهدفات
    {"id": "pri_new_c9_s4_r01", "subcategory_id": "pri_new_c9_s4", "name": "تقرير وضع خطة إجراءات داعمة", "order": 1},
    {"id": "pri_new_c9_s4_r02", "subcategory_id": "pri_new_c9_s4", "name": "تقرير تحديد مسؤوليات التنفيذ", "order": 2},
    {"id": "pri_new_c9_s4_r03", "subcategory_id": "pri_new_c9_s4", "name": "تقرير توفير موارد للإجراءات", "order": 3},
    {"id": "pri_new_c9_s4_r04", "subcategory_id": "pri_new_c9_s4", "name": "تقرير جدول زمني للإجراءات", "order": 4},
    {"id": "pri_new_c9_s4_r05", "subcategory_id": "pri_new_c9_s4", "name": "تقرير متابعة تنفيذ الإجراءات", "order": 5},
    {"id": "pri_new_c9_s4_r06", "subcategory_id": "pri_new_c9_s4", "name": "تقرير تقييم فاعلية الإجراءات", "order": 6},
    {"id": "pri_new_c9_s4_r07", "subcategory_id": "pri_new_c9_s4", "name": "تقرير تعديل الإجراءات حسب المستجدات", "order": 7},
    {"id": "pri_new_c9_s4_r08", "subcategory_id": "pri_new_c9_s4", "name": "تقرير توثيق الاتفاقيات", "order": 8},
    {"id": "pri_new_c9_s4_r09", "subcategory_id": "pri_new_c9_s4", "name": "تقرير إشراك الفريق في الاتفاق", "order": 9},
    {"id": "pri_new_c9_s4_r10", "subcategory_id": "pri_new_c9_s4", "name": "تقرير قياس أثر الإجراءات على المستهدفات", "order": 10},

    # pri_new_c9_s5 - إزالة المعوقات التي تعيق الأداء
    {"id": "pri_new_c9_s5_r01", "subcategory_id": "pri_new_c9_s5", "name": "تقرير حصر المعوقات الإدارية", "order": 1},
    {"id": "pri_new_c9_s5_r02", "subcategory_id": "pri_new_c9_s5", "name": "تقرير إجراءات إزالة المعوقات الفنية", "order": 2},
    {"id": "pri_new_c9_s5_r03", "subcategory_id": "pri_new_c9_s5", "name": "تقرير تذليل عقبات الموارد", "order": 3},
    {"id": "pri_new_c9_s5_r04", "subcategory_id": "pri_new_c9_s5", "name": "تقرير معالجة مشكلات التواصل", "order": 4},
    {"id": "pri_new_c9_s5_r05", "subcategory_id": "pri_new_c9_s5", "name": "تقرير تحسين بيئة العمل لإزالة المعوقات", "order": 5},
    {"id": "pri_new_c9_s5_r06", "subcategory_id": "pri_new_c9_s5", "name": "تقرير متابعة زمن إزالة المعوقات", "order": 6},
    {"id": "pri_new_c9_s5_r07", "subcategory_id": "pri_new_c9_s5", "name": "تقرير تقييم فعالية الإزالة", "order": 7},
    {"id": "pri_new_c9_s5_r08", "subcategory_id": "pri_new_c9_s5", "name": "تقرير توثيق المعوقات والحلول", "order": 8},
    {"id": "pri_new_c9_s5_r09", "subcategory_id": "pri_new_c9_s5", "name": "تقرير منع تكرار المعوقات", "order": 9},
    {"id": "pri_new_c9_s5_r10", "subcategory_id": "pri_new_c9_s5", "name": "تقرير أثر إزالة المعوقات على الأداء", "order": 10},

    # pri_new_c9_s6 - تعزيز السلوكيات الفاعلة لدى العاملين
    {"id": "pri_new_c9_s6_r01", "subcategory_id": "pri_new_c9_s6", "name": "تقرير تكريم الموظفين المتميزين", "order": 1},
    {"id": "pri_new_c9_s6_r02", "subcategory_id": "pri_new_c9_s6", "name": "تقرير برنامج الموظف المثالي", "order": 2},
    {"id": "pri_new_c9_s6_r03", "subcategory_id": "pri_new_c9_s6", "name": "تقرير نشر قصص النجاح للموظفين", "order": 3},
    {"id": "pri_new_c9_s6_r04", "subcategory_id": "pri_new_c9_s6", "name": "تقرير حوافز الأداء المتميز", "order": 4},
    {"id": "pri_new_c9_s6_r05", "subcategory_id": "pri_new_c9_s6", "name": "تقرير شهادات شكر وتقدير", "order": 5},
    {"id": "pri_new_c9_s6_r06", "subcategory_id": "pri_new_c9_s6", "name": "تقرير ورش عمل لتعزيز الروح المعنوية", "order": 6},
    {"id": "pri_new_c9_s6_r07", "subcategory_id": "pri_new_c9_s6", "name": "تقرير إشراك الموظفين في القرارات", "order": 7},
    {"id": "pri_new_c9_s6_r08", "subcategory_id": "pri_new_c9_s6", "name": "تقرير قياس الرضا الوظيفي", "order": 8},
    {"id": "pri_new_c9_s6_r09", "subcategory_id": "pri_new_c9_s6", "name": "تقرير تطوير سياسة الحوافز", "order": 9},
    {"id": "pri_new_c9_s6_r10", "subcategory_id": "pri_new_c9_s6", "name": "تقرير أثر التعزيز على الإنتاجية", "order": 10},

    # pri_new_c10_s1 - متابعة تنفيذ البرامج التدريبية
    {"id": "pri_new_c10_s1_r01", "subcategory_id": "pri_new_c10_s1", "name": "تقرير سجل حضور البرامج", "order": 1},
    {"id": "pri_new_c10_s1_r02", "subcategory_id": "pri_new_c10_s1", "name": "تقرير تنفيذ البرامج حسب الخطة", "order": 2},
    {"id": "pri_new_c10_s1_r03", "subcategory_id": "pri_new_c10_s1", "name": "تقرير متابعة تنفيذ البرامج عن بعد", "order": 3},
    {"id": "pri_new_c10_s1_r04", "subcategory_id": "pri_new_c10_s1", "name": "تقرير تقارير المدربين عن التنفيذ", "order": 4},
    {"id": "pri_new_c10_s1_r05", "subcategory_id": "pri_new_c10_s1", "name": "تقرير تحديات تنفيذ البرامج", "order": 5},
    {"id": "pri_new_c10_s1_r06", "subcategory_id": "pri_new_c10_s1", "name": "تقرير تعديل مواعيد البرامج", "order": 6},
    {"id": "pri_new_c10_s1_r07", "subcategory_id": "pri_new_c10_s1", "name": "تقرير إنجاز الخطة التدريبية", "order": 7},
    {"id": "pri_new_c10_s1_r08", "subcategory_id": "pri_new_c10_s1", "name": "تقرير توثيق تنفيذ البرامج", "order": 8},
    {"id": "pri_new_c10_s1_r09", "subcategory_id": "pri_new_c10_s1", "name": "تقرير متابعة تنفيذ البرامج التخصصية", "order": 9},
    {"id": "pri_new_c10_s1_r10", "subcategory_id": "pri_new_c10_s1", "name": "تقرير قياس جودة التنفيذ", "order": 10},

    # pri_new_c10_s2 - قياس أثر التدريب على نواتج التعلم
    {"id": "pri_new_c10_s2_r01", "subcategory_id": "pri_new_c10_s2", "name": "تقرير تحسن نتائج الطلاب بعد تدريب المعلمين", "order": 1},
    {"id": "pri_new_c10_s2_r02", "subcategory_id": "pri_new_c10_s2", "name": "تقرير تطبيق المعلمين لاستراتيجيات جديدة", "order": 2},
    {"id": "pri_new_c10_s2_r03", "subcategory_id": "pri_new_c10_s2", "name": "تقرير قياس أثر التدريب على مهارات الطلاب", "order": 3},
    {"id": "pri_new_c10_s2_r04", "subcategory_id": "pri_new_c10_s2", "name": "تقرير مقارنة نتائج قبل وبعد التدريب", "order": 4},
    {"id": "pri_new_c10_s2_r05", "subcategory_id": "pri_new_c10_s2", "name": "تقرير استمرارية أثر التدريب", "order": 5},
    {"id": "pri_new_c10_s2_r06", "subcategory_id": "pri_new_c10_s2", "name": "تقرير تحليل أثر التدريب على الأداء الصفي", "order": 6},
    {"id": "pri_new_c10_s2_r07", "subcategory_id": "pri_new_c10_s2", "name": "تقرير توصيات لتعزيز أثر التدريب", "order": 7},
    {"id": "pri_new_c10_s2_r08", "subcategory_id": "pri_new_c10_s2", "name": "تقرير توثيق قصص نجاح التدريب", "order": 8},
    {"id": "pri_new_c10_s2_r09", "subcategory_id": "pri_new_c10_s2", "name": "تقرير قياس العائد على التدريب", "order": 9},
    {"id": "pri_new_c10_s2_r10", "subcategory_id": "pri_new_c10_s2", "name": "تقرير تطوير أدوات قياس الأثر", "order": 10},

    # pri_new_c10_s3 - دعم النمو المهني المستمر للمعلمين
    {"id": "pri_new_c10_s3_r01", "subcategory_id": "pri_new_c10_s3", "name": "تقرير توفير مصادر تعلم للمعلمين", "order": 1},
    {"id": "pri_new_c10_s3_r02", "subcategory_id": "pri_new_c10_s3", "name": "تقرير تشجيع المعلمين على البحث الإجرائي", "order": 2},
    {"id": "pri_new_c10_s3_r03", "subcategory_id": "pri_new_c10_s3", "name": "تقرير دمج المعلمين في مجتمعات تعلم", "order": 3},
    {"id": "pri_new_c10_s3_r04", "subcategory_id": "pri_new_c10_s3", "name": "تقرير توفير منح تدريبية للمعلمين", "order": 4},
    {"id": "pri_new_c10_s3_r05", "subcategory_id": "pri_new_c10_s3", "name": "تقرير متابعة خطط التطوير الذاتي", "order": 5},
    {"id": "pri_new_c10_s3_r06", "subcategory_id": "pri_new_c10_s3", "name": "تقرير حوافز للمعلمين المتطوعين للتدريب", "order": 6},
    {"id": "pri_new_c10_s3_r07", "subcategory_id": "pri_new_c10_s3", "name": "تقرير تنظيم أيام مهنية داخل المدرسة", "order": 7},
    {"id": "pri_new_c10_s3_r08", "subcategory_id": "pri_new_c10_s3", "name": "تقرير استضافة خبراء للمعلمين", "order": 8},
    {"id": "pri_new_c10_s3_r09", "subcategory_id": "pri_new_c10_s3", "name": "تقرير قياس رضا المعلمين عن الدعم", "order": 9},
    {"id": "pri_new_c10_s3_r10", "subcategory_id": "pri_new_c10_s3", "name": "تقرير أثر الدعم على التطور المهني", "order": 10},

    # pri_new_c10_s4 - توظيف نتائج التقييم في تحسين الأداء
    {"id": "pri_new_c10_s4_r01", "subcategory_id": "pri_new_c10_s4", "name": "تقرير استخدام تقارير الأداء لتحسين التدريس", "order": 1},
    {"id": "pri_new_c10_s4_r02", "subcategory_id": "pri_new_c10_s4", "name": "تقرير تعديل الخطط بناءً على نتائج التقويم", "order": 2},
    {"id": "pri_new_c10_s4_r03", "subcategory_id": "pri_new_c10_s4", "name": "تقرير توجيه البرامج التدريبية وفق الاحتياجات", "order": 3},
    {"id": "pri_new_c10_s4_r04", "subcategory_id": "pri_new_c10_s4", "name": "تقرير تحسين أدوات التقويم", "order": 4},
    {"id": "pri_new_c10_s4_r05", "subcategory_id": "pri_new_c10_s4", "name": "تقرير متابعة تحسن الأداء بعد التعديلات", "order": 5},
    {"id": "pri_new_c10_s4_r06", "subcategory_id": "pri_new_c10_s4", "name": "تقرير توثيق نتائج التقييم", "order": 6},
    {"id": "pri_new_c10_s4_r07", "subcategory_id": "pri_new_c10_s4", "name": "تقرير ورش عمل لتحليل نتائج التقييم", "order": 7},
    {"id": "pri_new_c10_s4_r08", "subcategory_id": "pri_new_c10_s4", "name": "تقرير ربط التقييم بالحوافز", "order": 8},
    {"id": "pri_new_c10_s4_r09", "subcategory_id": "pri_new_c10_s4", "name": "تقرير قياس فعالية توظيف النتائج", "order": 9},
    {"id": "pri_new_c10_s4_r10", "subcategory_id": "pri_new_c10_s4", "name": "تقرير تطوير ثقافة التقويم", "order": 10},

    # pri_new_c11_s1 - تقييم أداء المرؤوسين بأساليب علمية
    {"id": "pri_new_c11_s1_r01", "subcategory_id": "pri_new_c11_s1", "name": "تقرير استخدام بطاقة الأداء المتوازن", "order": 1},
    {"id": "pri_new_c11_s1_r02", "subcategory_id": "pri_new_c11_s1", "name": "تقرير تقييم 360 درجة", "order": 2},
    {"id": "pri_new_c11_s1_r03", "subcategory_id": "pri_new_c11_s1", "name": "تقرير تطبيق معايير الأداء الوظيفي", "order": 3},
    {"id": "pri_new_c11_s1_r04", "subcategory_id": "pri_new_c11_s1", "name": "تقرير تدريب القادة على أساليب التقييم", "order": 4},
    {"id": "pri_new_c11_s1_r05", "subcategory_id": "pri_new_c11_s1", "name": "تقرير مراجعة أداء الإداريين", "order": 5},
    {"id": "pri_new_c11_s1_r06", "subcategory_id": "pri_new_c11_s1", "name": "تقرير تحليل نتائج التقييم", "order": 6},
    {"id": "pri_new_c11_s1_r07", "subcategory_id": "pri_new_c11_s1", "name": "تقرير توثيق التقييم في ملفات الموظفين", "order": 7},
    {"id": "pri_new_c11_s1_r08", "subcategory_id": "pri_new_c11_s1", "name": "تقرير قياس دقة التقييم", "order": 8},
    {"id": "pri_new_c11_s1_r09", "subcategory_id": "pri_new_c11_s1", "name": "تقرير تطوير أدوات التقييم", "order": 9},
    {"id": "pri_new_c11_s1_r10", "subcategory_id": "pri_new_c11_s1", "name": "تقرير أثر التقييم على الأداء", "order": 10},

    # pri_new_c11_s2 - استخدام أدوات تقويم متنوعة
    {"id": "pri_new_c11_s2_r01", "subcategory_id": "pri_new_c11_s2", "name": "تقرير استخدام المقابلات في التقييم", "order": 1},
    {"id": "pri_new_c11_s2_r02", "subcategory_id": "pri_new_c11_s2", "name": "تقرير تطبيق الاستبانات", "order": 2},
    {"id": "pri_new_c11_s2_r03", "subcategory_id": "pri_new_c11_s2", "name": "تقرير الملاحظة المباشرة", "order": 3},
    {"id": "pri_new_c11_s2_r04", "subcategory_id": "pri_new_c11_s2", "name": "تقرير تحليل ملفات الإنجاز", "order": 4},
    {"id": "pri_new_c11_s2_r05", "subcategory_id": "pri_new_c11_s2", "name": "تقرير استخدام الاختبارات المهنية", "order": 5},
    {"id": "pri_new_c11_s2_r06", "subcategory_id": "pri_new_c11_s2", "name": "تقرير تقييم الأقران", "order": 6},
    {"id": "pri_new_c11_s2_r07", "subcategory_id": "pri_new_c11_s2", "name": "تقرير تقييم الذات", "order": 7},
    {"id": "pri_new_c11_s2_r08", "subcategory_id": "pri_new_c11_s2", "name": "تقرير تنويع الأدوات حسب الفئة", "order": 8},
    {"id": "pri_new_c11_s2_r09", "subcategory_id": "pri_new_c11_s2", "name": "تقرير قياس فاعلية الأدوات", "order": 9},
    {"id": "pri_new_c11_s2_r10", "subcategory_id": "pri_new_c11_s2", "name": "تقرير تحديث الأدوات", "order": 10},

    # pri_new_c11_s3 - ملاحظة الأداء (تخطيطاً – تنفيذاً – تقويماً)
    {"id": "pri_new_c11_s3_r01", "subcategory_id": "pri_new_c11_s3", "name": "تقرير متابعة خطط المعلمين", "order": 1},
    {"id": "pri_new_c11_s3_r02", "subcategory_id": "pri_new_c11_s3", "name": "تقرير ملاحظة تنفيذ الدروس", "order": 2},
    {"id": "pri_new_c11_s3_r03", "subcategory_id": "pri_new_c11_s3", "name": "تقرير مراجعة أدوات التقويم", "order": 3},
    {"id": "pri_new_c11_s3_r04", "subcategory_id": "pri_new_c11_s3", "name": "تقرير زيارة صفية لملاحظة التنفيذ", "order": 4},
    {"id": "pri_new_c11_s3_r05", "subcategory_id": "pri_new_c11_s3", "name": "تقرير متابعة تنفيذ الأنشطة", "order": 5},
    {"id": "pri_new_c11_s3_r06", "subcategory_id": "pri_new_c11_s3", "name": "تقرير ملاحظة إدارة الفصل", "order": 6},
    {"id": "pri_new_c11_s3_r07", "subcategory_id": "pri_new_c11_s3", "name": "تقرير توثيق الملاحظات", "order": 7},
    {"id": "pri_new_c11_s3_r08", "subcategory_id": "pri_new_c11_s3", "name": "تقرير تحليل نتائج الملاحظة", "order": 8},
    {"id": "pri_new_c11_s3_r09", "subcategory_id": "pri_new_c11_s3", "name": "تقرير تغذية راجعة بناءً على الملاحظة", "order": 9},
    {"id": "pri_new_c11_s3_r10", "subcategory_id": "pri_new_c11_s3", "name": "تقرير أثر الملاحظة على تحسين الأداء", "order": 10},

    # pri_new_c11_s4 - تشجيع التقويم الذاتي للعاملين
    {"id": "pri_new_c11_s4_r01", "subcategory_id": "pri_new_c11_s4", "name": "تقرير توعية بأهمية التقويم الذاتي", "order": 1},
    {"id": "pri_new_c11_s4_r02", "subcategory_id": "pri_new_c11_s4", "name": "تقرير توفير استمارات تقويم ذاتي", "order": 2},
    {"id": "pri_new_c11_s4_r03", "subcategory_id": "pri_new_c11_s4", "name": "تقرير ورش عمل عن التقويم الذاتي", "order": 3},
    {"id": "pri_new_c11_s4_r04", "subcategory_id": "pri_new_c11_s4", "name": "تقرير تحليل نتائج التقويم الذاتي", "order": 4},
    {"id": "pri_new_c11_s4_r05", "subcategory_id": "pri_new_c11_s4", "name": "تقرير ربط التقويم الذاتي بخطط التطوير", "order": 5},
    {"id": "pri_new_c11_s4_r06", "subcategory_id": "pri_new_c11_s4", "name": "تقرير نماذج تقويم ذاتي إلكترونية", "order": 6},
    {"id": "pri_new_c11_s4_r07", "subcategory_id": "pri_new_c11_s4", "name": "تقرير مناقشة التقويم الذاتي مع الموظفين", "order": 7},
    {"id": "pri_new_c11_s4_r08", "subcategory_id": "pri_new_c11_s4", "name": "تقرير قياس مدى ممارسة التقويم الذاتي", "order": 8},
    {"id": "pri_new_c11_s4_r09", "subcategory_id": "pri_new_c11_s4", "name": "تقرير تحديث أدوات التقويم الذاتي", "order": 9},
    {"id": "pri_new_c11_s4_r10", "subcategory_id": "pri_new_c11_s4", "name": "تقرير أثر التقويم الذاتي على الأداء", "order": 10},

    # pri_new_c11_s5 - توظيف نتائج التقويم في تحسين الأداء
    {"id": "pri_new_c11_s5_r01", "subcategory_id": "pri_new_c11_s5", "name": "تقرير استخدام نتائج التقويم في التدريب", "order": 1},
    {"id": "pri_new_c11_s5_r02", "subcategory_id": "pri_new_c11_s5", "name": "تقرير تعديل المهام بناءً على التقويم", "order": 2},
    {"id": "pri_new_c11_s5_r03", "subcategory_id": "pri_new_c11_s5", "name": "تقرير تحفيز المتميزين بناءً على التقويم", "order": 3},
    {"id": "pri_new_c11_s5_r04", "subcategory_id": "pri_new_c11_s5", "name": "تقرير خطط تحسين للمحتاجين", "order": 4},
    {"id": "pri_new_c11_s5_r05", "subcategory_id": "pri_new_c11_s5", "name": "تقرير متابعة تحسن الأداء بعد التوظيف", "order": 5},
    {"id": "pri_new_c11_s5_r06", "subcategory_id": "pri_new_c11_s5", "name": "تقرير توثيق أثر التقويم", "order": 6},
    {"id": "pri_new_c11_s5_r07", "subcategory_id": "pri_new_c11_s5", "name": "تقرير مراجعة فاعلية توظيف النتائج", "order": 7},
    {"id": "pri_new_c11_s5_r08", "subcategory_id": "pri_new_c11_s5", "name": "تقرير تطوير آليات التوظيف", "order": 8},
    {"id": "pri_new_c11_s5_r09", "subcategory_id": "pri_new_c11_s5", "name": "تقرير قياس رضا الموظفين عن العدالة", "order": 9},
    {"id": "pri_new_c11_s5_r10", "subcategory_id": "pri_new_c11_s5", "name": "تقرير استدامة التحسين", "order": 10},

    # pri_new_c11_s6 - اتخاذ قرارات مبنية على نتائج التقويم
    {"id": "pri_new_c11_s6_r01", "subcategory_id": "pri_new_c11_s6", "name": "تقرير قرارات الترقية بناءً على التقويم", "order": 1},
    {"id": "pri_new_c11_s6_r02", "subcategory_id": "pri_new_c11_s6", "name": "تقرير قرارات نقل الصلاحيات", "order": 2},
    {"id": "pri_new_c11_s6_r03", "subcategory_id": "pri_new_c11_s6", "name": "تقرير قرارات تكليف بمهام جديدة", "order": 3},
    {"id": "pri_new_c11_s6_r04", "subcategory_id": "pri_new_c11_s6", "name": "تقرير قرارات تحسين بيئة العمل", "order": 4},
    {"id": "pri_new_c11_s6_r05", "subcategory_id": "pri_new_c11_s6", "name": "تقرير قرارات فصل أو إنذار (إن لزم)", "order": 5},
    {"id": "pri_new_c11_s6_r06", "subcategory_id": "pri_new_c11_s6", "name": "تقرير توثيق القرارات وربطها بالنتائج", "order": 6},
    {"id": "pri_new_c11_s6_r07", "subcategory_id": "pri_new_c11_s6", "name": "تقرير مراجعة القرارات المتخذة", "order": 7},
    {"id": "pri_new_c11_s6_r08", "subcategory_id": "pri_new_c11_s6", "name": "تقرير إشراف على تنفيذ القرارات", "order": 8},
    {"id": "pri_new_c11_s6_r09", "subcategory_id": "pri_new_c11_s6", "name": "تقرير قياس فاعلية القرارات", "order": 9},
    {"id": "pri_new_c11_s6_r10", "subcategory_id": "pri_new_c11_s6", "name": "تقرير تحسين آليات اتخاذ القرار", "order": 10},

    # pri_new_c12_s1 - تشخيص أداء المعلمين وتصنيفهم
    {"id": "pri_new_c12_s1_r01", "subcategory_id": "pri_new_c12_s1", "name": "تقرير تحليل نتائج الزيارات الصفية", "order": 1},
    {"id": "pri_new_c12_s1_r02", "subcategory_id": "pri_new_c12_s1", "name": "تقرير تصنيف المعلمين حسب الأداء", "order": 2},
    {"id": "pri_new_c12_s1_r03", "subcategory_id": "pri_new_c12_s1", "name": "تقرير تحديد المعلمين المتميزين", "order": 3},
    {"id": "pri_new_c12_s1_r04", "subcategory_id": "pri_new_c12_s1", "name": "تقرير تحديد المعلمين المحتاجين للدعم", "order": 4},
    {"id": "pri_new_c12_s1_r05", "subcategory_id": "pri_new_c12_s1", "name": "تقرير تحليل نتائج الطلاب لكل معلم", "order": 5},
    {"id": "pri_new_c12_s1_r06", "subcategory_id": "pri_new_c12_s1", "name": "تقرير مقارنة أداء المعلمين", "order": 6},
    {"id": "pri_new_c12_s1_r07", "subcategory_id": "pri_new_c12_s1", "name": "تقرير تحديث قاعدة بيانات أداء المعلمين", "order": 7},
    {"id": "pri_new_c12_s1_r08", "subcategory_id": "pri_new_c12_s1", "name": "تقرير استخدام أدوات تشخيص متنوعة", "order": 8},
    {"id": "pri_new_c12_s1_r09", "subcategory_id": "pri_new_c12_s1", "name": "تقرير توثيق نتائج التشخيص", "order": 9},
    {"id": "pri_new_c12_s1_r10", "subcategory_id": "pri_new_c12_s1", "name": "تقرير أثر التشخيص على خطط الدعم", "order": 10},

    # pri_new_c12_s2 - تفسير نتائج التعلم لتوجيه القرار
    {"id": "pri_new_c12_s2_r01", "subcategory_id": "pri_new_c12_s2", "name": "تقرير تحليل نتائج الاختبارات", "order": 1},
    {"id": "pri_new_c12_s2_r02", "subcategory_id": "pri_new_c12_s2", "name": "تقرير تحديد أسباب تدني النتائج", "order": 2},
    {"id": "pri_new_c12_s2_r03", "subcategory_id": "pri_new_c12_s2", "name": "تقرير مقارنة نتائج الفصول", "order": 3},
    {"id": "pri_new_c12_s2_r04", "subcategory_id": "pri_new_c12_s2", "name": "تقرير تفسير الفروق في النتائج", "order": 4},
    {"id": "pri_new_c12_s2_r05", "subcategory_id": "pri_new_c12_s2", "name": "تقرير توصيات بناءً على التفسير", "order": 5},
    {"id": "pri_new_c12_s2_r06", "subcategory_id": "pri_new_c12_s2", "name": "تقرير استخدام التفسير في تعديل التدريس", "order": 6},
    {"id": "pri_new_c12_s2_r07", "subcategory_id": "pri_new_c12_s2", "name": "تقرير ورش عمل مع المعلمين لتفسير النتائج", "order": 7},
    {"id": "pri_new_c12_s2_r08", "subcategory_id": "pri_new_c12_s2", "name": "تقرير توثيق التفسيرات", "order": 8},
    {"id": "pri_new_c12_s2_r09", "subcategory_id": "pri_new_c12_s2", "name": "تقرير قياس فاعلية التفسير في القرارات", "order": 9},
    {"id": "pri_new_c12_s2_r10", "subcategory_id": "pri_new_c12_s2", "name": "تقرير تطوير مهارات التفسير", "order": 10},

    # pri_new_c12_s3 - تقديم المعالجات التربوية للمتعثرين
    {"id": "pri_new_c12_s3_r01", "subcategory_id": "pri_new_c12_s3", "name": "تقرير برامج التقوية للطلاب المتعثرين", "order": 1},
    {"id": "pri_new_c12_s3_r02", "subcategory_id": "pri_new_c12_s3", "name": "تقرير حصص علاجية بعد الدوام", "order": 2},
    {"id": "pri_new_c12_s3_r03", "subcategory_id": "pri_new_c12_s3", "name": "تقرير استخدام استراتيجيات تدريس متنوعة", "order": 3},
    {"id": "pri_new_c12_s3_r04", "subcategory_id": "pri_new_c12_s3", "name": "تقرير متابعة تقدم المتعثرين", "order": 4},
    {"id": "pri_new_c12_s3_r05", "subcategory_id": "pri_new_c12_s3", "name": "تقرير إشراك أولياء الأمور في العلاج", "order": 5},
    {"id": "pri_new_c12_s3_r06", "subcategory_id": "pri_new_c12_s3", "name": "تقرير تقييم فعالية المعالجات", "order": 6},
    {"id": "pri_new_c12_s3_r07", "subcategory_id": "pri_new_c12_s3", "name": "تقرير تعديل المعالجات حسب الاحتياج", "order": 7},
    {"id": "pri_new_c12_s3_r08", "subcategory_id": "pri_new_c12_s3", "name": "تقرير توثيق خطط العلاج", "order": 8},
    {"id": "pri_new_c12_s3_r09", "subcategory_id": "pri_new_c12_s3", "name": "تقرير قصص نجاح في العلاج", "order": 9},
    {"id": "pri_new_c12_s3_r10", "subcategory_id": "pri_new_c12_s3", "name": "تقرير استمرارية الدعم", "order": 10},

    # pri_new_c12_s4 - رصد نمو المتعلمين دراسياً
    {"id": "pri_new_c12_s4_r01", "subcategory_id": "pri_new_c12_s4", "name": "تقرير متابعة درجات الطلاب شهرياً", "order": 1},
    {"id": "pri_new_c12_s4_r02", "subcategory_id": "pri_new_c12_s4", "name": "تقرير تحليل تطور الأداء لكل طالب", "order": 2},
    {"id": "pri_new_c12_s4_r03", "subcategory_id": "pri_new_c12_s4", "name": "تقرير منحنيات النمو الدراسي", "order": 3},
    {"id": "pri_new_c12_s4_r04", "subcategory_id": "pri_new_c12_s4", "name": "تقرير مقارنة أداء الطلاب عبر السنوات", "order": 4},
    {"id": "pri_new_c12_s4_r05", "subcategory_id": "pri_new_c12_s4", "name": "تقرير تحديد الطلاب ذوي النمو المرتفع", "order": 5},
    {"id": "pri_new_c12_s4_r06", "subcategory_id": "pri_new_c12_s4", "name": "تقرير تحديد الطلاب ذوي النمو البطيء", "order": 6},
    {"id": "pri_new_c12_s4_r07", "subcategory_id": "pri_new_c12_s4", "name": "تقرير استخدام الرصد في التوجيه", "order": 7},
    {"id": "pri_new_c12_s4_r08", "subcategory_id": "pri_new_c12_s4", "name": "تقرير توثيق بيانات النمو", "order": 8},
    {"id": "pri_new_c12_s4_r09", "subcategory_id": "pri_new_c12_s4", "name": "تقرير تطوير أدوات الرصد", "order": 9},
    {"id": "pri_new_c12_s4_r10", "subcategory_id": "pri_new_c12_s4", "name": "تقرير أثر الرصد على تحسين النتائج", "order": 10},

    # pri_new_c12_s5 - تنمية المعارف والمهارات الأساسية
    {"id": "pri_new_c12_s5_r01", "subcategory_id": "pri_new_c12_s5", "name": "تقرير برنامج تنمية مهارات القراءة", "order": 1},
    {"id": "pri_new_c12_s5_r02", "subcategory_id": "pri_new_c12_s5", "name": "تقرير مشروع إتقان العمليات الحسابية", "order": 2},
    {"id": "pri_new_c12_s5_r03", "subcategory_id": "pri_new_c12_s5", "name": "تقرير أنشطة تنمية التفكير الناقد", "order": 3},
    {"id": "pri_new_c12_s5_r04", "subcategory_id": "pri_new_c12_s5", "name": "تقرير برامج الإثراء للمتفوقين", "order": 4},
    {"id": "pri_new_c12_s5_r05", "subcategory_id": "pri_new_c12_s5", "name": "تقرير متابعة تطبيق المهارات الأساسية", "order": 5},
    {"id": "pri_new_c12_s5_r06", "subcategory_id": "pri_new_c12_s5", "name": "تقرير تقييم مستوى الطلاب في المهارات", "order": 6},
    {"id": "pri_new_c12_s5_r07", "subcategory_id": "pri_new_c12_s5", "name": "تقرير تحسين المناهج لتنمية المهارات", "order": 7},
    {"id": "pri_new_c12_s5_r08", "subcategory_id": "pri_new_c12_s5", "name": "تقرير تدريب المعلمين على تنمية المهارات", "order": 8},
    {"id": "pri_new_c12_s5_r09", "subcategory_id": "pri_new_c12_s5", "name": "تقرير توثيق نتائج البرامج", "order": 9},
    {"id": "pri_new_c12_s5_r10", "subcategory_id": "pri_new_c12_s5", "name": "تقرير استدامة تنمية المهارات", "order": 10},

    # pri_new_c12_s6 - تطوير عمليات التعليم والتعلم
    {"id": "pri_new_c12_s6_r01", "subcategory_id": "pri_new_c12_s6", "name": "تقرير تطبيق استراتيجيات التعلم النشط", "order": 1},
    {"id": "pri_new_c12_s6_r02", "subcategory_id": "pri_new_c12_s6", "name": "تقرير استخدام التقنية في التعليم", "order": 2},
    {"id": "pri_new_c12_s6_r03", "subcategory_id": "pri_new_c12_s6", "name": "تقرير تطوير وحدات دراسية", "order": 3},
    {"id": "pri_new_c12_s6_r04", "subcategory_id": "pri_new_c12_s6", "name": "تقرير مشروع التعلم القائم على المشاريع", "order": 4},
    {"id": "pri_new_c12_s6_r05", "subcategory_id": "pri_new_c12_s6", "name": "تقرير متابعة تطبيق التطويرات", "order": 5},
    {"id": "pri_new_c12_s6_r06", "subcategory_id": "pri_new_c12_s6", "name": "تقرير قياس أثر التطوير على النتائج", "order": 6},
    {"id": "pri_new_c12_s6_r07", "subcategory_id": "pri_new_c12_s6", "name": "تقرير ورش عمل لتطوير استراتيجيات التدريس", "order": 7},
    {"id": "pri_new_c12_s6_r08", "subcategory_id": "pri_new_c12_s6", "name": "تقرير توثيق عمليات التطوير", "order": 8},
    {"id": "pri_new_c12_s6_r09", "subcategory_id": "pri_new_c12_s6", "name": "تقرير تحسين جودة التعليم", "order": 9},
    {"id": "pri_new_c12_s6_r10", "subcategory_id": "pri_new_c12_s6", "name": "تقرير استدامة التطوير", "order": 10},

    # pri_new_c12_s7 - التواصل مع أولياء الأمور بشأن النتائج
    {"id": "pri_new_c12_s7_r01", "subcategory_id": "pri_new_c12_s7", "name": "تقرير إشعار أولياء الأمور بنتائج الاختبارات", "order": 1},
    {"id": "pri_new_c12_s7_r02", "subcategory_id": "pri_new_c12_s7", "name": "تقرير اجتماعات مع أولياء الأمور", "order": 2},
    {"id": "pri_new_c12_s7_r03", "subcategory_id": "pri_new_c12_s7", "name": "تقرير استشارات لأولياء الأمور حول التحصيل", "order": 3},
    {"id": "pri_new_c12_s7_r04", "subcategory_id": "pri_new_c12_s7", "name": "تقرير تقارير دورية عن تقدم الطلاب", "order": 4},
    {"id": "pri_new_c12_s7_r05", "subcategory_id": "pri_new_c12_s7", "name": "تقرير إشراك الأسر في خطط التحسين", "order": 5},
    {"id": "pri_new_c12_s7_r06", "subcategory_id": "pri_new_c12_s7", "name": "تقرير قنوات تواصل فعالة مع الأسر", "order": 6},
    {"id": "pri_new_c12_s7_r07", "subcategory_id": "pri_new_c12_s7", "name": "تقرير استطلاع رضا الأسر عن التواصل", "order": 7},
    {"id": "pri_new_c12_s7_r08", "subcategory_id": "pri_new_c12_s7", "name": "تقرير تحسين التواصل بناءً على التغذية", "order": 8},
    {"id": "pri_new_c12_s7_r09", "subcategory_id": "pri_new_c12_s7", "name": "تقرير توثيق التواصل مع الأسر", "order": 9},
    {"id": "pri_new_c12_s7_r10", "subcategory_id": "pri_new_c12_s7", "name": "تقرير أثر التواصل على تحسن النتائج", "order": 10},

    # pri_new_c13_s1 - رفع مستوى الأداء التعليمي
    {"id": "pri_new_c13_s1_r01", "subcategory_id": "pri_new_c13_s1", "name": "تقرير تحسن نتائج الطلاب في المواد الأساسية", "order": 1},
    {"id": "pri_new_c13_s1_r02", "subcategory_id": "pri_new_c13_s1", "name": "تقرير زيادة نسبة النجاح", "order": 2},
    {"id": "pri_new_c13_s1_r03", "subcategory_id": "pri_new_c13_s1", "name": "تقرير تطوير أداء المعلمين", "order": 3},
    {"id": "pri_new_c13_s1_r04", "subcategory_id": "pri_new_c13_s1", "name": "تقرير تحسين الممارسات الصفية", "order": 4},
    {"id": "pri_new_c13_s1_r05", "subcategory_id": "pri_new_c13_s1", "name": "تقرير برامج تحسين التعليم", "order": 5},
    {"id": "pri_new_c13_s1_r06", "subcategory_id": "pri_new_c13_s1", "name": "تقرير متابعة مؤشرات الأداء التعليمي", "order": 6},
    {"id": "pri_new_c13_s1_r07", "subcategory_id": "pri_new_c13_s1", "name": "تقرير مقارنة الأداء بالمعايير", "order": 7},
    {"id": "pri_new_c13_s1_r08", "subcategory_id": "pri_new_c13_s1", "name": "تقرير توثيق تحسن الأداء", "order": 8},
    {"id": "pri_new_c13_s1_r09", "subcategory_id": "pri_new_c13_s1", "name": "تقرير تحليل عوامل تحسين الأداء", "order": 9},
    {"id": "pri_new_c13_s1_r10", "subcategory_id": "pri_new_c13_s1", "name": "تقرير استدامة الرفع", "order": 10},

    # pri_new_c13_s2 - تحقيق المستهدفات الاستراتيجية
    {"id": "pri_new_c13_s2_r01", "subcategory_id": "pri_new_c13_s2", "name": "تقرير إنجاز أهداف الخطة الاستراتيجية", "order": 1},
    {"id": "pri_new_c13_s2_r02", "subcategory_id": "pri_new_c13_s2", "name": "تقرير نسبة تحقيق مؤشرات الأداء", "order": 2},
    {"id": "pri_new_c13_s2_r03", "subcategory_id": "pri_new_c13_s2", "name": "تقرير مواءمة المخرجات مع المستهدفات", "order": 3},
    {"id": "pri_new_c13_s2_r04", "subcategory_id": "pri_new_c13_s2", "name": "تقرير مراجعة المستهدفات مع القيادة", "order": 4},
    {"id": "pri_new_c13_s2_r05", "subcategory_id": "pri_new_c13_s2", "name": "تقرير تحديث المستهدفات", "order": 5},
    {"id": "pri_new_c13_s2_r06", "subcategory_id": "pri_new_c13_s2", "name": "تقرير تحليل الفجوات في التحقيق", "order": 6},
    {"id": "pri_new_c13_s2_r07", "subcategory_id": "pri_new_c13_s2", "name": "تقرير خطط لتحقيق المستهدفات غير المحققة", "order": 7},
    {"id": "pri_new_c13_s2_r08", "subcategory_id": "pri_new_c13_s2", "name": "تقرير توثيق إنجازات الاستراتيجية", "order": 8},
    {"id": "pri_new_c13_s2_r09", "subcategory_id": "pri_new_c13_s2", "name": "تقرير قياس رضا المستفيدين عن الاستراتيجية", "order": 9},
    {"id": "pri_new_c13_s2_r10", "subcategory_id": "pri_new_c13_s2", "name": "تقرير أثر تحقيق المستهدفات على السمعة", "order": 10},

    # pri_new_c13_s3 - تحسين نتائج التعلم بشكل مستمر
    {"id": "pri_new_c13_s3_r01", "subcategory_id": "pri_new_c13_s3", "name": "تقرير تطور نتائج التعلم على ثلاث سنوات", "order": 1},
    {"id": "pri_new_c13_s3_r02", "subcategory_id": "pri_new_c13_s3", "name": "تقرير خطط التحسين السنوية للنتائج", "order": 2},
    {"id": "pri_new_c13_s3_r03", "subcategory_id": "pri_new_c13_s3", "name": "تقرير برامج تحسين نواتج التعلم", "order": 3},
    {"id": "pri_new_c13_s3_r04", "subcategory_id": "pri_new_c13_s3", "name": "تقرير متابعة تحسن النتائج دورياً", "order": 4},
    {"id": "pri_new_c13_s3_r05", "subcategory_id": "pri_new_c13_s3", "name": "تقرير تحليل العوامل المؤثرة في التحسن", "order": 5},
    {"id": "pri_new_c13_s3_r06", "subcategory_id": "pri_new_c13_s3", "name": "تقرير توثيق قصص نجاح في تحسين النتائج", "order": 6},
    {"id": "pri_new_c13_s3_r07", "subcategory_id": "pri_new_c13_s3", "name": "تقرير تحديث استراتيجيات التحسين", "order": 7},
    {"id": "pri_new_c13_s3_r08", "subcategory_id": "pri_new_c13_s3", "name": "تقرير إشراف القيادة على التحسين", "order": 8},
    {"id": "pri_new_c13_s3_r09", "subcategory_id": "pri_new_c13_s3", "name": "تقرير قياس رضا الطلاب عن التحسن", "order": 9},
    {"id": "pri_new_c13_s3_r10", "subcategory_id": "pri_new_c13_s3", "name": "تقرير استدامة تحسن النتائج", "order": 10},

    # pri_new_c13_s4 - متابعة مؤشرات التحسن المدرسي
    {"id": "pri_new_c13_s4_r01", "subcategory_id": "pri_new_c13_s4", "name": "تقرير مؤشرات تحسن الانضباط", "order": 1},
    {"id": "pri_new_c13_s4_r02", "subcategory_id": "pri_new_c13_s4", "name": "تقرير مؤشرات تحسن نتائج الطلاب", "order": 2},
    {"id": "pri_new_c13_s4_r03", "subcategory_id": "pri_new_c13_s4", "name": "تقرير مؤشرات رضا المستفيدين", "order": 3},
    {"id": "pri_new_c13_s4_r04", "subcategory_id": "pri_new_c13_s4", "name": "تقرير مؤشرات أداء المعلمين", "order": 4},
    {"id": "pri_new_c13_s4_r05", "subcategory_id": "pri_new_c13_s4", "name": "تقرير لوحة مؤشرات التحسن", "order": 5},
    {"id": "pri_new_c13_s4_r06", "subcategory_id": "pri_new_c13_s4", "name": "تقرير تحليل تطور المؤشرات", "order": 6},
    {"id": "pri_new_c13_s4_r07", "subcategory_id": "pri_new_c13_s4", "name": "تقرير تحديث المؤشرات", "order": 7},
    {"id": "pri_new_c13_s4_r08", "subcategory_id": "pri_new_c13_s4", "name": "تقرير عرض المؤشرات على الفريق", "order": 8},
    {"id": "pri_new_c13_s4_r09", "subcategory_id": "pri_new_c13_s4", "name": "تقرير استخدام المؤشرات في التحفيز", "order": 9},
    {"id": "pri_new_c13_s4_r10", "subcategory_id": "pri_new_c13_s4", "name": "تقرير قياس دقة المؤشرات", "order": 10},

    # pri_new_c13_s5 - معالجة جوانب القصور في الأداء
    {"id": "pri_new_c13_s5_r01", "subcategory_id": "pri_new_c13_s5", "name": "تقرير تشخيص جوانب القصور", "order": 1},
    {"id": "pri_new_c13_s5_r02", "subcategory_id": "pri_new_c13_s5", "name": "تقرير خطط علاجية للقصور", "order": 2},
    {"id": "pri_new_c13_s5_r03", "subcategory_id": "pri_new_c13_s5", "name": "تقرير متابعة معالجة القصور", "order": 3},
    {"id": "pri_new_c13_s5_r04", "subcategory_id": "pri_new_c13_s5", "name": "تقرير تحليل أسباب القصور", "order": 4},
    {"id": "pri_new_c13_s5_r05", "subcategory_id": "pri_new_c13_s5", "name": "تقرير تقييم فعالية المعالجة", "order": 5},
    {"id": "pri_new_c13_s5_r06", "subcategory_id": "pri_new_c13_s5", "name": "تقرير توثيق إجراءات المعالجة", "order": 6},
    {"id": "pri_new_c13_s5_r07", "subcategory_id": "pri_new_c13_s5", "name": "تقرير منع تكرار القصور", "order": 7},
    {"id": "pri_new_c13_s5_r08", "subcategory_id": "pri_new_c13_s5", "name": "تقرير تحسين آليات المعالجة", "order": 8},
    {"id": "pri_new_c13_s5_r09", "subcategory_id": "pri_new_c13_s5", "name": "تقرير قياس رضا العاملين عن المعالجة", "order": 9},
    {"id": "pri_new_c13_s5_r10", "subcategory_id": "pri_new_c13_s5", "name": "تقرير أثر المعالجة على الأداء", "order": 10},

    # pri_new_c14_s1 - إعداد الخطط المدرسية (التشغيلية والتحسينية)
    {"id": "pri_new_c14_s1_r01", "subcategory_id": "pri_new_c14_s1", "name": "تقرير إعداد الخطة التشغيلية السنوية", "order": 1},
    {"id": "pri_new_c14_s1_r02", "subcategory_id": "pri_new_c14_s1", "name": "تقرير خطة التحسين المدرسي", "order": 2},
    {"id": "pri_new_c14_s1_r03", "subcategory_id": "pri_new_c14_s1", "name": "تقرير تحليل الواقع قبل التخطيط", "order": 3},
    {"id": "pri_new_c14_s1_r04", "subcategory_id": "pri_new_c14_s1", "name": "تقرير مشاركة الأقسام في إعداد الخطة", "order": 4},
    {"id": "pri_new_c14_s1_r05", "subcategory_id": "pri_new_c14_s1", "name": "تقرير تحديد الأهداف والمؤشرات", "order": 5},
    {"id": "pri_new_c14_s1_r06", "subcategory_id": "pri_new_c14_s1", "name": "تقرير توزيع مسؤوليات الخطة", "order": 6},
    {"id": "pri_new_c14_s1_r07", "subcategory_id": "pri_new_c14_s1", "name": "تقرير مراجعة الخطة مع المشرفين", "order": 7},
    {"id": "pri_new_c14_s1_r08", "subcategory_id": "pri_new_c14_s1", "name": "تقرير اعتماد الخطة", "order": 8},
    {"id": "pri_new_c14_s1_r09", "subcategory_id": "pri_new_c14_s1", "name": "تقرير تحديث الخطة", "order": 9},
    {"id": "pri_new_c14_s1_r10", "subcategory_id": "pri_new_c14_s1", "name": "تقرير تقييم جودة الخطة", "order": 10},

    # pri_new_c14_s2 - توجيه الجهود لتحقيق استراتيجيات الوزارة
    {"id": "pri_new_c14_s2_r01", "subcategory_id": "pri_new_c14_s2", "name": "تقرير مواءمة خطط المدرسة مع رؤية الوزارة", "order": 1},
    {"id": "pri_new_c14_s2_r02", "subcategory_id": "pri_new_c14_s2", "name": "تقرير تنفيذ مبادرات الوزارة", "order": 2},
    {"id": "pri_new_c14_s2_r03", "subcategory_id": "pri_new_c14_s2", "name": "تقرير توجيه المعلمين لتحقيق الاستراتيجيات", "order": 3},
    {"id": "pri_new_c14_s2_r04", "subcategory_id": "pri_new_c14_s2", "name": "تقرير متابعة مؤشرات الاستراتيجية", "order": 4},
    {"id": "pri_new_c14_s2_r05", "subcategory_id": "pri_new_c14_s2", "name": "تقرير تحديث الخطط وفق استراتيجيات الوزارة", "order": 5},
    {"id": "pri_new_c14_s2_r06", "subcategory_id": "pri_new_c14_s2", "name": "تقرير ورش عمل للتعريف بالاستراتيجيات", "order": 6},
    {"id": "pri_new_c14_s2_r07", "subcategory_id": "pri_new_c14_s2", "name": "تقرير قياس مدى تحقيق الاستراتيجيات", "order": 7},
    {"id": "pri_new_c14_s2_r08", "subcategory_id": "pri_new_c14_s2", "name": "تقرير توثيق مساهمات المدرسة", "order": 8},
    {"id": "pri_new_c14_s2_r09", "subcategory_id": "pri_new_c14_s2", "name": "تقرير تحسين التوجيه الاستراتيجي", "order": 9},
    {"id": "pri_new_c14_s2_r10", "subcategory_id": "pri_new_c14_s2", "name": "تقرير أثر التوجيه على الأداء", "order": 10},

    # pri_new_c14_s3 - تهيئة الفرص والإمكانات الداعمة للخطط
    {"id": "pri_new_c14_s3_r01", "subcategory_id": "pri_new_c14_s3", "name": "تقرير توفير الموارد اللازمة للخطط", "order": 1},
    {"id": "pri_new_c14_s3_r02", "subcategory_id": "pri_new_c14_s3", "name": "تقرير تخصيص ميزانية للخطط", "order": 2},
    {"id": "pri_new_c14_s3_r03", "subcategory_id": "pri_new_c14_s3", "name": "تقرير تجهيز البنية التحتية", "order": 3},
    {"id": "pri_new_c14_s3_r04", "subcategory_id": "pri_new_c14_s3", "name": "تقرير تدريب العاملين لتنفيذ الخطط", "order": 4},
    {"id": "pri_new_c14_s3_r05", "subcategory_id": "pri_new_c14_s3", "name": "تقرير توفير الوقت في الجدول للخطط", "order": 5},
    {"id": "pri_new_c14_s3_r06", "subcategory_id": "pri_new_c14_s3", "name": "تقرير متابعة توفر الإمكانات", "order": 6},
    {"id": "pri_new_c14_s3_r07", "subcategory_id": "pri_new_c14_s3", "name": "تقرير تحديث الإمكانات حسب الاحتياج", "order": 7},
    {"id": "pri_new_c14_s3_r08", "subcategory_id": "pri_new_c14_s3", "name": "تقرير شراكات لدعم الإمكانات", "order": 8},
    {"id": "pri_new_c14_s3_r09", "subcategory_id": "pri_new_c14_s3", "name": "تقرير قياس كفاية الإمكانات", "order": 9},
    {"id": "pri_new_c14_s3_r10", "subcategory_id": "pri_new_c14_s3", "name": "تقرير أثر الإمكانات على تنفيذ الخطط", "order": 10},

    # pri_new_c14_s4 - توظيف المنصات الرقمية المعتمدة في التخطيط
    {"id": "pri_new_c14_s4_r01", "subcategory_id": "pri_new_c14_s4", "name": "تقرير استخدام منصة مستقبلي في التخطيط", "order": 1},
    {"id": "pri_new_c14_s4_r02", "subcategory_id": "pri_new_c14_s4", "name": "تقرير توظيف نظام نور في متابعة الخطط", "order": 2},
    {"id": "pri_new_c14_s4_r03", "subcategory_id": "pri_new_c14_s4", "name": "تقرير استخدام منصة مدرستي في التخطيط للدروس", "order": 3},
    {"id": "pri_new_c14_s4_r04", "subcategory_id": "pri_new_c14_s4", "name": "تقرير تدريب المعلمين على المنصات", "order": 4},
    {"id": "pri_new_c14_s4_r05", "subcategory_id": "pri_new_c14_s4", "name": "تقرير متابعة استخدام المنصات في التخطيط", "order": 5},
    {"id": "pri_new_c14_s4_r06", "subcategory_id": "pri_new_c14_s4", "name": "تقرير تحديث الخطط عبر المنصات", "order": 6},
    {"id": "pri_new_c14_s4_r07", "subcategory_id": "pri_new_c14_s4", "name": "تقرير تحليل بيانات المنصات لدعم التخطيط", "order": 7},
    {"id": "pri_new_c14_s4_r08", "subcategory_id": "pri_new_c14_s4", "name": "تقرير قياس فاعلية المنصات في التخطيط", "order": 8},
    {"id": "pri_new_c14_s4_r09", "subcategory_id": "pri_new_c14_s4", "name": "تقرير توثيق استخدام المنصات", "order": 9},
    {"id": "pri_new_c14_s4_r10", "subcategory_id": "pri_new_c14_s4", "name": "تقرير تطوير توظيف المنصات", "order": 10},

    # pri_new_c14_s5 - دعم فاعلية المدرسة وتحسين الأداء عبر الخطط
    {"id": "pri_new_c14_s5_r01", "subcategory_id": "pri_new_c14_s5", "name": "تقرير أثر الخطط على تحسن الأداء", "order": 1},
    {"id": "pri_new_c14_s5_r02", "subcategory_id": "pri_new_c14_s5", "name": "تقرير ربط الخطط بمؤشرات الأداء", "order": 2},
    {"id": "pri_new_c14_s5_r03", "subcategory_id": "pri_new_c14_s5", "name": "تقرير مراجعة فاعلية الخطط", "order": 3},
    {"id": "pri_new_c14_s5_r04", "subcategory_id": "pri_new_c14_s5", "name": "تقرير تحسين الخطط بناءً على النتائج", "order": 4},
    {"id": "pri_new_c14_s5_r05", "subcategory_id": "pri_new_c14_s5", "name": "تقرير توثيق إسهامات الخطط في التطوير", "order": 5},
    {"id": "pri_new_c14_s5_r06", "subcategory_id": "pri_new_c14_s5", "name": "تقرير قياس رضا المستفيدين عن الخطط", "order": 6},
    {"id": "pri_new_c14_s5_r07", "subcategory_id": "pri_new_c14_s5", "name": "تقرير استدامة فاعلية الخطط", "order": 7},
    {"id": "pri_new_c14_s5_r08", "subcategory_id": "pri_new_c14_s5", "name": "تقرير تحديث مؤشرات فاعلية الخطط", "order": 8},
    {"id": "pri_new_c14_s5_r09", "subcategory_id": "pri_new_c14_s5", "name": "تقرير نشر فاعلية الخطط", "order": 9},
    {"id": "pri_new_c14_s5_r10", "subcategory_id": "pri_new_c14_s5", "name": "تقرير تحسين آليات الدعم", "order": 10},

    # pri_new_c15_s1 - متابعة تنفيذ الخطط التشغيلية
    {"id": "pri_new_c15_s1_r01", "subcategory_id": "pri_new_c15_s1", "name": "تقرير متابعة تنفيذ الخطة التشغيلية شهرياً", "order": 1},
    {"id": "pri_new_c15_s1_r02", "subcategory_id": "pri_new_c15_s1", "name": "تقرير اجتماعات متابعة الخطة", "order": 2},
    {"id": "pri_new_c15_s1_r03", "subcategory_id": "pri_new_c15_s1", "name": "تقرير تقارير فرق العمل عن التنفيذ", "order": 3},
    {"id": "pri_new_c15_s1_r04", "subcategory_id": "pri_new_c15_s1", "name": "تقرير تحديات تنفيذ الخطة", "order": 4},
    {"id": "pri_new_c15_s1_r05", "subcategory_id": "pri_new_c15_s1", "name": "تقرير إنجاز الخطة", "order": 5},
    {"id": "pri_new_c15_s1_r06", "subcategory_id": "pri_new_c15_s1", "name": "تقرير تعديل الخطة أثناء التنفيذ", "order": 6},
    {"id": "pri_new_c15_s1_r07", "subcategory_id": "pri_new_c15_s1", "name": "تقرير توثيق نتائج المتابعة", "order": 7},
    {"id": "pri_new_c15_s1_r08", "subcategory_id": "pri_new_c15_s1", "name": "تقرير قياس نسبة الإنجاز", "order": 8},
    {"id": "pri_new_c15_s1_r09", "subcategory_id": "pri_new_c15_s1", "name": "تقرير تحسين عملية المتابعة", "order": 9},
    {"id": "pri_new_c15_s1_r10", "subcategory_id": "pri_new_c15_s1", "name": "تقرير أثر المتابعة على التنفيذ", "order": 10},

    # pri_new_c15_s2 - متابعة خطط التحسين والانضباط
    {"id": "pri_new_c15_s2_r01", "subcategory_id": "pri_new_c15_s2", "name": "تقرير متابعة خطة التحسين", "order": 1},
    {"id": "pri_new_c15_s2_r02", "subcategory_id": "pri_new_c15_s2", "name": "تقرير متابعة خطة الانضباط", "order": 2},
    {"id": "pri_new_c15_s2_r03", "subcategory_id": "pri_new_c15_s2", "name": "تقرير اجتماعات متابعة خطط التحسين", "order": 3},
    {"id": "pri_new_c15_s2_r04", "subcategory_id": "pri_new_c15_s2", "name": "تقرير تحديث خطط التحسين", "order": 4},
    {"id": "pri_new_c15_s2_r05", "subcategory_id": "pri_new_c15_s2", "name": "تقرير مؤشرات تنفيذ خطط الانضباط", "order": 5},
    {"id": "pri_new_c15_s2_r06", "subcategory_id": "pri_new_c15_s2", "name": "تقرير تقييم أثر خطط التحسين", "order": 6},
    {"id": "pri_new_c15_s2_r07", "subcategory_id": "pri_new_c15_s2", "name": "تقرير توثيق متابعة الخطط", "order": 7},
    {"id": "pri_new_c15_s2_r08", "subcategory_id": "pri_new_c15_s2", "name": "تقرير تحسين آليات المتابعة", "order": 8},
    {"id": "pri_new_c15_s2_r09", "subcategory_id": "pri_new_c15_s2", "name": "تقرير قياس رضا الفريق عن المتابعة", "order": 9},
    {"id": "pri_new_c15_s2_r10", "subcategory_id": "pri_new_c15_s2", "name": "تقرير استدامة متابعة الخطط", "order": 10},

    # pri_new_c15_s3 - متابعة خطط المعلمين
    {"id": "pri_new_c15_s3_r01", "subcategory_id": "pri_new_c15_s3", "name": "تقرير متابعة خطط المعلمين الفصلية", "order": 1},
    {"id": "pri_new_c15_s3_r02", "subcategory_id": "pri_new_c15_s3", "name": "تقرير مراجعة خطط الدروس", "order": 2},
    {"id": "pri_new_c15_s3_r03", "subcategory_id": "pri_new_c15_s3", "name": "تقرير متابعة خطط الأنشطة الصفية", "order": 3},
    {"id": "pri_new_c15_s3_r04", "subcategory_id": "pri_new_c15_s3", "name": "تقرير تحليل تقارير المعلمين", "order": 4},
    {"id": "pri_new_c15_s3_r05", "subcategory_id": "pri_new_c15_s3", "name": "تقرير التغذية الراجعة على خطط المعلمين", "order": 5},
    {"id": "pri_new_c15_s3_r06", "subcategory_id": "pri_new_c15_s3", "name": "تقرير تحديث خطط المعلمين", "order": 6},
    {"id": "pri_new_c15_s3_r07", "subcategory_id": "pri_new_c15_s3", "name": "تقرير توثيق خطط المعلمين", "order": 7},
    {"id": "pri_new_c15_s3_r08", "subcategory_id": "pri_new_c15_s3", "name": "تقرير قياس جودة خطط المعلمين", "order": 8},
    {"id": "pri_new_c15_s3_r09", "subcategory_id": "pri_new_c15_s3", "name": "تقرير أثر خطط المعلمين على الطلاب", "order": 9},
    {"id": "pri_new_c15_s3_r10", "subcategory_id": "pri_new_c15_s3", "name": "تقرير تحسين متابعة خطط المعلمين", "order": 10},

    # pri_new_c15_s4 - قياس أثر تنفيذ الخطط على الأداء
    {"id": "pri_new_c15_s4_r01", "subcategory_id": "pri_new_c15_s4", "name": "تقرير قياس أثر الخطة التشغيلية على الأداء", "order": 1},
    {"id": "pri_new_c15_s4_r02", "subcategory_id": "pri_new_c15_s4", "name": "تقرير تحسين نتائج الطلاب بعد الخطط", "order": 2},
    {"id": "pri_new_c15_s4_r03", "subcategory_id": "pri_new_c15_s4", "name": "تقرير تحليل العائد من الخطط", "order": 3},
    {"id": "pri_new_c15_s4_r04", "subcategory_id": "pri_new_c15_s4", "name": "تقرير استبيانات قياس الأثر", "order": 4},
    {"id": "pri_new_c15_s4_r05", "subcategory_id": "pri_new_c15_s4", "name": "تقرير مقارنة قبل وبعد تنفيذ الخطط", "order": 5},
    {"id": "pri_new_c15_s4_r06", "subcategory_id": "pri_new_c15_s4", "name": "تقرير استدامة أثر الخطط", "order": 6},
    {"id": "pri_new_c15_s4_r07", "subcategory_id": "pri_new_c15_s4", "name": "تقرير تحديات قياس الأثر", "order": 7},
    {"id": "pri_new_c15_s4_r08", "subcategory_id": "pri_new_c15_s4", "name": "تقرير توصيات لتحسين الأثر", "order": 8},
    {"id": "pri_new_c15_s4_r09", "subcategory_id": "pri_new_c15_s4", "name": "تقرير توثيق قصص نجاح الأثر", "order": 9},
    {"id": "pri_new_c15_s4_r10", "subcategory_id": "pri_new_c15_s4", "name": "تقرير عرض نتائج التقييم على القيادة", "order": 10},

    # pri_new_c15_s5 - معالجة أوجه القصور في التنفيذ
    {"id": "pri_new_c15_s5_r01", "subcategory_id": "pri_new_c15_s5", "name": "تقرير تحديد أوجه القصور في تنفيذ الخطط", "order": 1},
    {"id": "pri_new_c15_s5_r02", "subcategory_id": "pri_new_c15_s5", "name": "تقرير إجراءات تصحيحية للقصور", "order": 2},
    {"id": "pri_new_c15_s5_r03", "subcategory_id": "pri_new_c15_s5", "name": "تقرير متابعة تنفيذ الإجراءات التصحيحية", "order": 3},
    {"id": "pri_new_c15_s5_r04", "subcategory_id": "pri_new_c15_s5", "name": "تقرير تحليل أسباب القصور", "order": 4},
    {"id": "pri_new_c15_s5_r05", "subcategory_id": "pri_new_c15_s5", "name": "تقرير تقييم فعالية المعالجة", "order": 5},
    {"id": "pri_new_c15_s5_r06", "subcategory_id": "pri_new_c15_s5", "name": "تقرير توثيق إجراءات المعالجة", "order": 6},
    {"id": "pri_new_c15_s5_r07", "subcategory_id": "pri_new_c15_s5", "name": "تقرير منع تكرار القصور", "order": 7},
    {"id": "pri_new_c15_s5_r08", "subcategory_id": "pri_new_c15_s5", "name": "تقرير تحسين آليات المعالجة", "order": 8},
    {"id": "pri_new_c15_s5_r09", "subcategory_id": "pri_new_c15_s5", "name": "تقرير قياس رضا الفريق عن المعالجة", "order": 9},
    {"id": "pri_new_c15_s5_r10", "subcategory_id": "pri_new_c15_s5", "name": "تقرير أثر المعالجة على تحسين التنفيذ", "order": 10},

    # pri_new_c16_s1 - دعم المشاركة الصفية واللاصفية
    {"id": "pri_new_c16_s1_r01", "subcategory_id": "pri_new_c16_s1", "name": "تقرير تفعيل الأنشطة الصفية", "order": 1},
    {"id": "pri_new_c16_s1_r02", "subcategory_id": "pri_new_c16_s1", "name": "تقرير حصص النشاط الطلابي", "order": 2},
    {"id": "pri_new_c16_s1_r03", "subcategory_id": "pri_new_c16_s1", "name": "تقرير مشاركة الطلاب في الإذاعة المدرسية", "order": 3},
    {"id": "pri_new_c16_s1_r04", "subcategory_id": "pri_new_c16_s1", "name": "تقرير دعم الأندية الطلابية", "order": 4},
    {"id": "pri_new_c16_s1_r05", "subcategory_id": "pri_new_c16_s1", "name": "تقرير تشجيع الطلاب على المبادرات", "order": 5},
    {"id": "pri_new_c16_s1_r06", "subcategory_id": "pri_new_c16_s1", "name": "تقرير توفير أدوات للأنشطة", "order": 6},
    {"id": "pri_new_c16_s1_r07", "subcategory_id": "pri_new_c16_s1", "name": "تقرير متابعة مشاركة الطلاب", "order": 7},
    {"id": "pri_new_c16_s1_r08", "subcategory_id": "pri_new_c16_s1", "name": "تقرير تكريم المشاركين", "order": 8},
    {"id": "pri_new_c16_s1_r09", "subcategory_id": "pri_new_c16_s1", "name": "تقرير قياس رضا الطلاب عن الأنشطة", "order": 9},
    {"id": "pri_new_c16_s1_r10", "subcategory_id": "pri_new_c16_s1", "name": "تقرير تطوير المشاركة الصفية", "order": 10},

    # pri_new_c16_s2 - دعم المشاركات الداخلية والخارجية
    {"id": "pri_new_c16_s2_r01", "subcategory_id": "pri_new_c16_s2", "name": "تقرير مشاركة الطلاب في المسابقات الداخلية", "order": 1},
    {"id": "pri_new_c16_s2_r02", "subcategory_id": "pri_new_c16_s2", "name": "تقرير المشاركة في مسابقات خارجية", "order": 2},
    {"id": "pri_new_c16_s2_r03", "subcategory_id": "pri_new_c16_s2", "name": "تقرير رحلات مدرسية تعليمية", "order": 3},
    {"id": "pri_new_c16_s2_r04", "subcategory_id": "pri_new_c16_s2", "name": "تقرير زيارات ميدانية", "order": 4},
    {"id": "pri_new_c16_s2_r05", "subcategory_id": "pri_new_c16_s2", "name": "تقرير توفير الإشراف للمشاركات الخارجية", "order": 5},
    {"id": "pri_new_c16_s2_r06", "subcategory_id": "pri_new_c16_s2", "name": "تقرير تمكين الطلاب من التمثيل الخارجي", "order": 6},
    {"id": "pri_new_c16_s2_r07", "subcategory_id": "pri_new_c16_s2", "name": "تقرير متابعة نتائج المشاركات", "order": 7},
    {"id": "pri_new_c16_s2_r08", "subcategory_id": "pri_new_c16_s2", "name": "تقرير تكريم الفرق المشاركة", "order": 8},
    {"id": "pri_new_c16_s2_r09", "subcategory_id": "pri_new_c16_s2", "name": "تقرير قياس أثر المشاركات على الطلاب", "order": 9},
    {"id": "pri_new_c16_s2_r10", "subcategory_id": "pri_new_c16_s2", "name": "تقرير تطوير المشاركات الخارجية", "order": 10},

    # pri_new_c16_s3 - تعزيز الأنشطة الطلابية
    {"id": "pri_new_c16_s3_r01", "subcategory_id": "pri_new_c16_s3", "name": "تقرير خطة النشاط الطلابي السنوية", "order": 1},
    {"id": "pri_new_c16_s3_r02", "subcategory_id": "pri_new_c16_s3", "name": "تقرير تنفيذ برامج النشاط", "order": 2},
    {"id": "pri_new_c16_s3_r03", "subcategory_id": "pri_new_c16_s3", "name": "تقرير توفير موارد للأنشطة", "order": 3},
    {"id": "pri_new_c16_s3_r04", "subcategory_id": "pri_new_c16_s3", "name": "تقرير تفعيل يوم النشاط", "order": 4},
    {"id": "pri_new_c16_s3_r05", "subcategory_id": "pri_new_c16_s3", "name": "تقرير مشاركة المعلمين في الأنشطة", "order": 5},
    {"id": "pri_new_c16_s3_r06", "subcategory_id": "pri_new_c16_s3", "name": "تقرير متابعة تنفيذ الأنشطة", "order": 6},
    {"id": "pri_new_c16_s3_r07", "subcategory_id": "pri_new_c16_s3", "name": "تقرير تحديث خطة الأنشطة", "order": 7},
    {"id": "pri_new_c16_s3_r08", "subcategory_id": "pri_new_c16_s3", "name": "تقرير تقييم الأنشطة", "order": 8},
    {"id": "pri_new_c16_s3_r09", "subcategory_id": "pri_new_c16_s3", "name": "تقرير قياس رضا الطلاب عن الأنشطة", "order": 9},
    {"id": "pri_new_c16_s3_r10", "subcategory_id": "pri_new_c16_s3", "name": "تقرير استدامة الأنشطة", "order": 10},

    # pri_new_c16_s4 - توثيق إنجازات الطلاب
    {"id": "pri_new_c16_s4_r01", "subcategory_id": "pri_new_c16_s4", "name": "تقرير سجل إنجازات الطلاب", "order": 1},
    {"id": "pri_new_c16_s4_r02", "subcategory_id": "pri_new_c16_s4", "name": "تقرير توثيق جوائز الطلاب", "order": 2},
    {"id": "pri_new_c16_s4_r03", "subcategory_id": "pri_new_c16_s4", "name": "تقرير نشر إنجازات الطلاب في الموقع", "order": 3},
    {"id": "pri_new_c16_s4_r04", "subcategory_id": "pri_new_c16_s4", "name": "تقرير الاحتفاء بالإنجازات", "order": 4},
    {"id": "pri_new_c16_s4_r05", "subcategory_id": "pri_new_c16_s4", "name": "تقرير تحليل الإنجازات", "order": 5},
    {"id": "pri_new_c16_s4_r06", "subcategory_id": "pri_new_c16_s4", "name": "تقرير إبلاغ المجتمع بالإنجازات", "order": 6},
    {"id": "pri_new_c16_s4_r07", "subcategory_id": "pri_new_c16_s4", "name": "تقرير مقارنة الإنجازات بالسنوات السابقة", "order": 7},
    {"id": "pri_new_c16_s4_r08", "subcategory_id": "pri_new_c16_s4", "name": "تقرير تكريم الطلاب المتميزين", "order": 8},
    {"id": "pri_new_c16_s4_r09", "subcategory_id": "pri_new_c16_s4", "name": "تقرير استدامة الإنجازات", "order": 9},
    {"id": "pri_new_c16_s4_r10", "subcategory_id": "pri_new_c16_s4", "name": "تقرير أثر الإنجازات على تحفيز الآخرين", "order": 10},

    # pri_new_c17_s1 - متابعة استخدام المنصات التعليمية
    {"id": "pri_new_c17_s1_r01", "subcategory_id": "pri_new_c17_s1", "name": "تقرير متابعة استخدام منصة مدرستي", "order": 1},
    {"id": "pri_new_c17_s1_r02", "subcategory_id": "pri_new_c17_s1", "name": "تقرير تقارير حضور الطلاب على المنصة", "order": 2},
    {"id": "pri_new_c17_s1_r03", "subcategory_id": "pri_new_c17_s1", "name": "تقرير تفعيل الواجبات الإلكترونية", "order": 3},
    {"id": "pri_new_c17_s1_r04", "subcategory_id": "pri_new_c17_s1", "name": "تقرير متابعة استخدام المعلمين للمنصة", "order": 4},
    {"id": "pri_new_c17_s1_r05", "subcategory_id": "pri_new_c17_s1", "name": "تقرير تحديث المحتوى على المنصة", "order": 5},
    {"id": "pri_new_c17_s1_r06", "subcategory_id": "pri_new_c17_s1", "name": "تقرير تحليل استخدام المنصة", "order": 6},
    {"id": "pri_new_c17_s1_r07", "subcategory_id": "pri_new_c17_s1", "name": "تقرير تدريب المستخدمين على المنصة", "order": 7},
    {"id": "pri_new_c17_s1_r08", "subcategory_id": "pri_new_c17_s1", "name": "تقرير حل مشكلات المنصة", "order": 8},
    {"id": "pri_new_c17_s1_r09", "subcategory_id": "pri_new_c17_s1", "name": "تقرير قياس رضا المستخدمين عن المنصة", "order": 9},
    {"id": "pri_new_c17_s1_r10", "subcategory_id": "pri_new_c17_s1", "name": "تقرير تطوير استخدام المنصة", "order": 10},

    # pri_new_c17_s2 - ضمان الالتزام بضوابط المنصات
    {"id": "pri_new_c17_s2_r01", "subcategory_id": "pri_new_c17_s2", "name": "تقرير الالتزام بضوابط السلوك الرقمي", "order": 1},
    {"id": "pri_new_c17_s2_r02", "subcategory_id": "pri_new_c17_s2", "name": "تقرير متابعة خصوصية البيانات", "order": 2},
    {"id": "pri_new_c17_s2_r03", "subcategory_id": "pri_new_c17_s2", "name": "تقرير ضوابط استخدام المنصة للطلاب", "order": 3},
    {"id": "pri_new_c17_s2_r04", "subcategory_id": "pri_new_c17_s2", "name": "تقرير توعية المستخدمين بالضوابط", "order": 4},
    {"id": "pri_new_c17_s2_r05", "subcategory_id": "pri_new_c17_s2", "name": "تقرير مراجعة الامتثال للضوابط", "order": 5},
    {"id": "pri_new_c17_s2_r06", "subcategory_id": "pri_new_c17_s2", "name": "تقرير معالجة مخالفات الضوابط", "order": 6},
    {"id": "pri_new_c17_s2_r07", "subcategory_id": "pri_new_c17_s2", "name": "تقرير تحديث الضوابط", "order": 7},
    {"id": "pri_new_c17_s2_r08", "subcategory_id": "pri_new_c17_s2", "name": "تقرير توثيق الالتزام", "order": 8},
    {"id": "pri_new_c17_s2_r09", "subcategory_id": "pri_new_c17_s2", "name": "تقرير قياس مدى الالتزام", "order": 9},
    {"id": "pri_new_c17_s2_r10", "subcategory_id": "pri_new_c17_s2", "name": "تقرير تحسين آليات الضبط", "order": 10},

    # pri_new_c17_s3 - دعم التعليم الرقمي في المدرسة
    {"id": "pri_new_c17_s3_r01", "subcategory_id": "pri_new_c17_s3", "name": "تقرير توفير البنية التحتية للتعليم الرقمي", "order": 1},
    {"id": "pri_new_c17_s3_r02", "subcategory_id": "pri_new_c17_s3", "name": "تقرير تدريب المعلمين على التعليم الرقمي", "order": 2},
    {"id": "pri_new_c17_s3_r03", "subcategory_id": "pri_new_c17_s3", "name": "تقرير تفعيل الفصول الافتراضية", "order": 3},
    {"id": "pri_new_c17_s3_r04", "subcategory_id": "pri_new_c17_s3", "name": "تقرير استخدام المصادر الرقمية", "order": 4},
    {"id": "pri_new_c17_s3_r05", "subcategory_id": "pri_new_c17_s3", "name": "تقرير متابعة جودة التعليم الرقمي", "order": 5},
    {"id": "pri_new_c17_s3_r06", "subcategory_id": "pri_new_c17_s3", "name": "تقرير تحسين المنصات التعليمية", "order": 6},
    {"id": "pri_new_c17_s3_r07", "subcategory_id": "pri_new_c17_s3", "name": "تقرير شراكات لدعم الرقمنة", "order": 7},
    {"id": "pri_new_c17_s3_r08", "subcategory_id": "pri_new_c17_s3", "name": "تقرير قياس رضا المستفيدين عن الرقمنة", "order": 8},
    {"id": "pri_new_c17_s3_r09", "subcategory_id": "pri_new_c17_s3", "name": "تقرير تحديث استراتيجيات التعليم الرقمي", "order": 9},
    {"id": "pri_new_c17_s3_r10", "subcategory_id": "pri_new_c17_s3", "name": "تقرير استدامة التعليم الرقمي", "order": 10},

    # pri_new_c17_s4 - توظيف التقنية في عمليات التعليم والتعلم
    {"id": "pri_new_c17_s4_r01", "subcategory_id": "pri_new_c17_s4", "name": "تقرير استخدام السبورات التفاعلية", "order": 1},
    {"id": "pri_new_c17_s4_r02", "subcategory_id": "pri_new_c17_s4", "name": "تقرير توظيف المحاكاة في العلوم", "order": 2},
    {"id": "pri_new_c17_s4_r03", "subcategory_id": "pri_new_c17_s4", "name": "تقرير استخدام التطبيقات التعليمية", "order": 3},
    {"id": "pri_new_c17_s4_r04", "subcategory_id": "pri_new_c17_s4", "name": "تقرير توظيف الذكاء الاصطناعي في التقييم", "order": 4},
    {"id": "pri_new_c17_s4_r05", "subcategory_id": "pri_new_c17_s4", "name": "تقرير متابعة توظيف التقنية", "order": 5},
    {"id": "pri_new_c17_s4_r06", "subcategory_id": "pri_new_c17_s4", "name": "تقرير تدريب المعلمين على توظيف التقنية", "order": 6},
    {"id": "pri_new_c17_s4_r07", "subcategory_id": "pri_new_c17_s4", "name": "تقرير تحديث الأجهزة والتقنيات", "order": 7},
    {"id": "pri_new_c17_s4_r08", "subcategory_id": "pri_new_c17_s4", "name": "تقرير قياس أثر التقنية على التعلم", "order": 8},
    {"id": "pri_new_c17_s4_r09", "subcategory_id": "pri_new_c17_s4", "name": "تقرير توثيق استخدام التقنية", "order": 9},
    {"id": "pri_new_c17_s4_r10", "subcategory_id": "pri_new_c17_s4", "name": "تقرير تطوير توظيف التقنية", "order": 10},

    # pri_new_c18_s1 - متابعة برامج التوجيه الطلابي
    {"id": "pri_new_c18_s1_r01", "subcategory_id": "pri_new_c18_s1", "name": "تقرير خطة التوجيه الطلابي", "order": 1},
    {"id": "pri_new_c18_s1_r02", "subcategory_id": "pri_new_c18_s1", "name": "تقرير تنفيذ برامج الإرشاد", "order": 2},
    {"id": "pri_new_c18_s1_r03", "subcategory_id": "pri_new_c18_s1", "name": "تقرير متابعة جلسات الإرشاد الفردي", "order": 3},
    {"id": "pri_new_c18_s1_r04", "subcategory_id": "pri_new_c18_s1", "name": "تقرير ورش عمل التوعية", "order": 4},
    {"id": "pri_new_c18_s1_r05", "subcategory_id": "pri_new_c18_s1", "name": "تقرير متابعة حالات الإحالة", "order": 5},
    {"id": "pri_new_c18_s1_r06", "subcategory_id": "pri_new_c18_s1", "name": "تقرير تقارير التوجيه الشهرية", "order": 6},
    {"id": "pri_new_c18_s1_r07", "subcategory_id": "pri_new_c18_s1", "name": "تقرير تحديث برامج التوجيه", "order": 7},
    {"id": "pri_new_c18_s1_r08", "subcategory_id": "pri_new_c18_s1", "name": "تقرير تقييم أثر برامج التوجيه", "order": 8},
    {"id": "pri_new_c18_s1_r09", "subcategory_id": "pri_new_c18_s1", "name": "تقرير توثيق حالات التوجيه", "order": 9},
    {"id": "pri_new_c18_s1_r10", "subcategory_id": "pri_new_c18_s1", "name": "تقرير تطوير برامج التوجيه", "order": 10},

    # pri_new_c18_s2 - معالجة الحالات الفردية للطلاب
    {"id": "pri_new_c18_s2_r01", "subcategory_id": "pri_new_c18_s2", "name": "تقرير حالات السلوك الفردية", "order": 1},
    {"id": "pri_new_c18_s2_r02", "subcategory_id": "pri_new_c18_s2", "name": "تقرير خطة تعديل السلوك الفردية", "order": 2},
    {"id": "pri_new_c18_s2_r03", "subcategory_id": "pri_new_c18_s2", "name": "تقرير متابعة الحالة مع المرشد", "order": 3},
    {"id": "pri_new_c18_s2_r04", "subcategory_id": "pri_new_c18_s2", "name": "تقرير اجتماعات مع أولياء الأمور", "order": 4},
    {"id": "pri_new_c18_s2_r05", "subcategory_id": "pri_new_c18_s2", "name": "تقرير تحويل الحالات للجهات المختصة", "order": 5},
    {"id": "pri_new_c18_s2_r06", "subcategory_id": "pri_new_c18_s2", "name": "تقرير متابعة تقدم الحالة", "order": 6},
    {"id": "pri_new_c18_s2_r07", "subcategory_id": "pri_new_c18_s2", "name": "تقرير تقييم فعالية التدخلات", "order": 7},
    {"id": "pri_new_c18_s2_r08", "subcategory_id": "pri_new_c18_s2", "name": "تقرير توثيق حالات التحسن", "order": 8},
    {"id": "pri_new_c18_s2_r09", "subcategory_id": "pri_new_c18_s2", "name": "تقرير تحديث سجل الحالات", "order": 9},
    {"id": "pri_new_c18_s2_r10", "subcategory_id": "pri_new_c18_s2", "name": "تقرير تحسين آليات المعالجة", "order": 10},

    # pri_new_c18_s3 - إعداد تقارير التحسن السلوكي
    {"id": "pri_new_c18_s3_r01", "subcategory_id": "pri_new_c18_s3", "name": "تقرير تحليل مخالفات السلوك الشهرية", "order": 1},
    {"id": "pri_new_c18_s3_r02", "subcategory_id": "pri_new_c18_s3", "name": "تقرير مؤشرات انخفاض المخالفات", "order": 2},
    {"id": "pri_new_c18_s3_r03", "subcategory_id": "pri_new_c18_s3", "name": "تقرير مقارنة سلوك الفصول", "order": 3},
    {"id": "pri_new_c18_s3_r04", "subcategory_id": "pri_new_c18_s3", "name": "تقرير تحليل أسباب المخالفات", "order": 4},
    {"id": "pri_new_c18_s3_r05", "subcategory_id": "pri_new_c18_s3", "name": "تقرير تطور السلوك عبر الفصول", "order": 5},
    {"id": "pri_new_c18_s3_r06", "subcategory_id": "pri_new_c18_s3", "name": "تقرير تحديد الأنماط السلوكية", "order": 6},
    {"id": "pri_new_c18_s3_r07", "subcategory_id": "pri_new_c18_s3", "name": "تقرير أثر برامج التعزيز على التحسن", "order": 7},
    {"id": "pri_new_c18_s3_r08", "subcategory_id": "pri_new_c18_s3", "name": "تقرير تحليل تقارير التوجيه", "order": 8},
    {"id": "pri_new_c18_s3_r09", "subcategory_id": "pri_new_c18_s3", "name": "تقرير توصيات للتحسين", "order": 9},
    {"id": "pri_new_c18_s3_r10", "subcategory_id": "pri_new_c18_s3", "name": "تقرير عرض التحليل على القيادة", "order": 10},

    # pri_new_c18_s4 - تكريم الطلاب المتحسنين سلوكياً
    {"id": "pri_new_c18_s4_r01", "subcategory_id": "pri_new_c18_s4", "name": "تقرير حفل تكريم المتميزين سلوكياً", "order": 1},
    {"id": "pri_new_c18_s4_r02", "subcategory_id": "pri_new_c18_s4", "name": "تقرير تكريم الطلاب المتحسنين", "order": 2},
    {"id": "pri_new_c18_s4_r03", "subcategory_id": "pri_new_c18_s4", "name": "تقرير شهادات شكر للطلاب", "order": 3},
    {"id": "pri_new_c18_s4_r04", "subcategory_id": "pri_new_c18_s4", "name": "تقرير نشر أسماء المكرمين في الإذاعة", "order": 4},
    {"id": "pri_new_c18_s4_r05", "subcategory_id": "pri_new_c18_s4", "name": "تقرير جوائز عينية للطلاب", "order": 5},
    {"id": "pri_new_c18_s4_r06", "subcategory_id": "pri_new_c18_s4", "name": "تقرير تكريم أولياء الأمور", "order": 6},
    {"id": "pri_new_c18_s4_r07", "subcategory_id": "pri_new_c18_s4", "name": "تقرير متابعة أثر التكريم", "order": 7},
    {"id": "pri_new_c18_s4_r08", "subcategory_id": "pri_new_c18_s4", "name": "تقرير تنوع طرق التكريم", "order": 8},
    {"id": "pri_new_c18_s4_r09", "subcategory_id": "pri_new_c18_s4", "name": "تقرير إشراك الطلاب في التكريم", "order": 9},
    {"id": "pri_new_c18_s4_r10", "subcategory_id": "pri_new_c18_s4", "name": "تقرير توثيق لحظات التكريم", "order": 10},

    # pri_new_c19_s1 - تحقيق معايير الأمن والسلامة
    {"id": "pri_new_c19_s1_r01", "subcategory_id": "pri_new_c19_s1", "name": "تقرير جاهزية طفايات الحريق", "order": 1},
    {"id": "pri_new_c19_s1_r02", "subcategory_id": "pri_new_c19_s1", "name": "تقرير صيانة مخارج الطوارئ", "order": 2},
    {"id": "pri_new_c19_s1_r03", "subcategory_id": "pri_new_c19_s1", "name": "تقرير تدريب العاملين على السلامة", "order": 3},
    {"id": "pri_new_c19_s1_r04", "subcategory_id": "pri_new_c19_s1", "name": "تقرير توفر الإسعافات الأولية", "order": 4},
    {"id": "pri_new_c19_s1_r05", "subcategory_id": "pri_new_c19_s1", "name": "تقرير متابعة اشتراطات الأمن دورياً", "order": 5},
    {"id": "pri_new_c19_s1_r06", "subcategory_id": "pri_new_c19_s1", "name": "تقرير سلامة الألعاب والساحات", "order": 6},
    {"id": "pri_new_c19_s1_r07", "subcategory_id": "pri_new_c19_s1", "name": "تقرير التزام المقصف بالاشتراطات", "order": 7},
    {"id": "pri_new_c19_s1_r08", "subcategory_id": "pri_new_c19_s1", "name": "تقرير فحص التمديدات الكهربائية", "order": 8},
    {"id": "pri_new_c19_s1_r09", "subcategory_id": "pri_new_c19_s1", "name": "تقرير خطط الإخلاء", "order": 9},
    {"id": "pri_new_c19_s1_r10", "subcategory_id": "pri_new_c19_s1", "name": "تقرير تقييم تطبيق اشتراطات السلامة", "order": 10},

    # pri_new_c19_s2 - تمكين مجتمع المدرسة من تحقيق الأهداف
    {"id": "pri_new_c19_s2_r01", "subcategory_id": "pri_new_c19_s2", "name": "تقرير مشاركة المعلمين في اتخاذ القرارات", "order": 1},
    {"id": "pri_new_c19_s2_r02", "subcategory_id": "pri_new_c19_s2", "name": "تقرير تفويض الصلاحيات للوكلاء", "order": 2},
    {"id": "pri_new_c19_s2_r03", "subcategory_id": "pri_new_c19_s2", "name": "تقرير تمكين الطلاب من المبادرات", "order": 3},
    {"id": "pri_new_c19_s2_r04", "subcategory_id": "pri_new_c19_s2", "name": "تقرير إشراك أولياء الأمور في التخطيط", "order": 4},
    {"id": "pri_new_c19_s2_r05", "subcategory_id": "pri_new_c19_s2", "name": "تقرير تحفيز المجتمع المدرسي", "order": 5},
    {"id": "pri_new_c19_s2_r06", "subcategory_id": "pri_new_c19_s2", "name": "تقرير قياس مدى التمكين", "order": 6},
    {"id": "pri_new_c19_s2_r07", "subcategory_id": "pri_new_c19_s2", "name": "تقرير تحديث آليات التمكين", "order": 7},
    {"id": "pri_new_c19_s2_r08", "subcategory_id": "pri_new_c19_s2", "name": "تقرير توثيق مبادرات التمكين", "order": 8},
    {"id": "pri_new_c19_s2_r09", "subcategory_id": "pri_new_c19_s2", "name": "تقرير أثر التمكين على الأداء", "order": 9},
    {"id": "pri_new_c19_s2_r10", "subcategory_id": "pri_new_c19_s2", "name": "تقرير استدامة التمكين", "order": 10},

    # pri_new_c19_s3 - تحقيق التوقعات العالية لنواتج التعلم
    {"id": "pri_new_c19_s3_r01", "subcategory_id": "pri_new_c19_s3", "name": "تقرير وضع معايير عالية للتوقع", "order": 1},
    {"id": "pri_new_c19_s3_r02", "subcategory_id": "pri_new_c19_s3", "name": "تقرير توجيه المعلمين لرفع التوقعات", "order": 2},
    {"id": "pri_new_c19_s3_r03", "subcategory_id": "pri_new_c19_s3", "name": "تقرير متابعة تحقيق التوقعات", "order": 3},
    {"id": "pri_new_c19_s3_r04", "subcategory_id": "pri_new_c19_s3", "name": "تقرير تحليل الفجوة بين التوقعات والنتائج", "order": 4},
    {"id": "pri_new_c19_s3_r05", "subcategory_id": "pri_new_c19_s3", "name": "تقرير تحفيز الطلاب لتحقيق التوقعات", "order": 5},
    {"id": "pri_new_c19_s3_r06", "subcategory_id": "pri_new_c19_s3", "name": "تقرير تحديث التوقعات", "order": 6},
    {"id": "pri_new_c19_s3_r07", "subcategory_id": "pri_new_c19_s3", "name": "تقرير توثيق تحقيق التوقعات", "order": 7},
    {"id": "pri_new_c19_s3_r08", "subcategory_id": "pri_new_c19_s3", "name": "تقرير قياس رضا المجتمع عن التوقعات", "order": 8},
    {"id": "pri_new_c19_s3_r09", "subcategory_id": "pri_new_c19_s3", "name": "تقرير أثر التوقعات على التحصيل", "order": 9},
    {"id": "pri_new_c19_s3_r10", "subcategory_id": "pri_new_c19_s3", "name": "تقرير استدامة التوقعات العالية", "order": 10},

    # pri_new_c19_s4 - توفير بيئة تعليمية جاذبة وآمنة نفسياً
    {"id": "pri_new_c19_s4_r01", "subcategory_id": "pri_new_c19_s4", "name": "تقرير تحسين المظهر العام للمدرسة", "order": 1},
    {"id": "pri_new_c19_s4_r02", "subcategory_id": "pri_new_c19_s4", "name": "تقرير توفير مساحات خضراء", "order": 2},
    {"id": "pri_new_c19_s4_r03", "subcategory_id": "pri_new_c19_s4", "name": "تقرير برامج الدعم النفسي", "order": 3},
    {"id": "pri_new_c19_s4_r04", "subcategory_id": "pri_new_c19_s4", "name": "تقرير مكافحة التنمر", "order": 4},
    {"id": "pri_new_c19_s4_r05", "subcategory_id": "pri_new_c19_s4", "name": "تقرير تهوية وإضاءة الفصول", "order": 5},
    {"id": "pri_new_c19_s4_r06", "subcategory_id": "pri_new_c19_s4", "name": "تقرير توفير مرشد نفسي", "order": 6},
    {"id": "pri_new_c19_s4_r07", "subcategory_id": "pri_new_c19_s4", "name": "تقرير استطلاع المناخ النفسي", "order": 7},
    {"id": "pri_new_c19_s4_r08", "subcategory_id": "pri_new_c19_s4", "name": "تقرير تحسين البيئة بناءً على الاقتراحات", "order": 8},
    {"id": "pri_new_c19_s4_r09", "subcategory_id": "pri_new_c19_s4", "name": "تقرير قياس رضا الطلاب عن البيئة", "order": 9},
    {"id": "pri_new_c19_s4_r10", "subcategory_id": "pri_new_c19_s4", "name": "تقرير استدامة البيئة الآمنة", "order": 10},
]

# =========================
# قالب البرومبت (مع النسبة المئوية)
# =========================

PRINCIPAL_PROMPT_TEMPLATE = """
أنت مدير مدرسة خبير وقائد تربوي، مسؤول عن تحقيق الرؤية الاستراتيجية وقيادة عمليات التطوير المؤسسي وتمكين العاملين.
- كن قياديًا تربويًا موضوعيًا ومتزنًا وبنّاءً  
- قدّم الملاحظات بصيغة تطويرية داعمة تعزز التحسين المستمر  
- راعِ واقع المدرسة وإمكاناتها واحتياجات منسوبيها  
- اربط بين القيادة المدرسية والمعلمين والطلاب والمنهج والبيئة التعليمية  
- ركّز على جودة نواتج التعلم وفاعلية الإدارة في دعمها  
- التزم بلغة عربية فصيحة سليمة وخالية من الأخطاء  
- اجعل المحتوى وكأنه تقرير مقدم من مشرف تربوي عن ممارسة فعلية قام بها مدير المدرسة  

⚠️ **ضوابط بنائية إلزامية للتقرير (تنطبق على جميع الحقول):**

1) **الفئة المستهدفة:**  
   يجب أن تنعكس الفئة المذكورة في (المستهدفون) في جميع الحقول دون استثناء.  
   - لا يجوز أن يكون الهدف موجهاً للطلاب بينما المستهدف هو المعلم.  
   - لا يجوز أن تتحدث الإجراءات عن تطوير طلاب بينما المستهدف معلمون.  
   - جميع الحقول يجب أن تتسق مع الفئة المحددة بدقة.

2) **السياق التنفيذي:**  
   إذا وُجدت مبادرة مرتبطة بخطة تشغيلية أو برنامج مدرسي:  
   - يجب أن يرتبط الهدف، والإجراءات، والاستراتيجيات، ونقاط القوة، ونقاط التحسين، والتوصيات بطبيعة المبادرة المذكورة.  
   - يجب أن تعكس المعالجات دور القيادة المدرسية في التخطيط والتنفيذ والمتابعة.  
   - يمنع كتابة محتوى عام غير مرتبط بطبيعة المبادرة.

3) **إذا لم تُذكر مبادرة محددة:**  
   - يمنع ذكر تفاصيل برنامج أو مشروع محدد.  
   - يجب أن يكون التقرير متعلقًا بالممارسة القيادية العامة.

4) **مكان التنفيذ:**  
   - إذا كان التنفيذ داخل المدرسة، يجب أن تنسجم الإجراءات مع البيئة المدرسية.  
   - إذا كان التنفيذ في لقاءات خارجية أو شراكات مجتمعية، يجب أن تعكس الإجراءات ذلك.  
   - لا يجوز وصف نشاط صفي مباشر إذا كان الدور إشرافيًا إداريًا.

5) **الترابط الداخلي:**  
   - يجب أن تكون الإجراءات منطقية ومكملة للهدف.  
   - يجب أن تكون الاستراتيجيات مناسبة لطبيعة القيادة المدرسية.  
   - يجب أن تستند نقاط القوة والتحسين إلى ما ذُكر سابقًا.  
   - يجب أن تكون التوصيات مبنية على نقاط التحسين وليست منفصلة عنها.

أي إخلال بهذه الضوابط يُعد خللاً مهنيًا في بناء التقرير.  
تحقق داخليًا من الاتساق الكامل قبل إخراج الإجابة.  

**شروط المحتوى:**
اكتب محتوى كل حقل بصيغة تقريرية مهنية وكأنه صادر عن مشرف تربوي.  
لا تكتب أبداً عنوان الحقل داخل المحتوى ولا تعِد صياغته بصيغة مباشرة.  
يجب أن يحتوي كل حقل على ما يقارب 25 كلمة.  
ابدأ بالمضمون مباشرة دون تمهيد أو عبارات إنشائية.  
احرص على وجود ترابط منطقي بين الحقول المطلوبة.  
اجعل الهدف النهائي للمحتوى تحسين جودة القيادة المدرسية وتعزيز التطوير المؤسسي المستدام.  
راعِ الوضوح والترابط، واجعل كل جملة تضيف قيمة قيادية تربوية فعلية.  


  

التقرير المطلوب: "{report_name}"
يندرج تحت التصنيف الفرعي: "{subcategory_name}"
ضمن الجدارة القيادية: "{criterion_name}" (نسبة الجدارة: {criterion_percentage}%)

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