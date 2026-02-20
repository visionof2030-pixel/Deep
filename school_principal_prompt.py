# -*- coding: utf-8 -*-

# =========================
# المعايير الرئيسية (الجدارات القيادية) لمدير المدرسة - نموذج الأداء الوظيفي
# =========================

PRINCIPAL_CRITERIA = [
    {"id": "pri_c1", "name": "المرونة والتكيف مع ظروف العمل المختلفة", "order": 1, "percentage": 5},
    {"id": "pri_c2", "name": "دعم المبادرات النوعية", "order": 2, "percentage": 10},
    {"id": "pri_c3", "name": "اتخاذ إجراءات تربوية لتحقيق الانضباط المدرسي", "order": 3, "percentage": 5},
    {"id": "pri_c4", "name": "إدارة الموارد المدرسية بكفاءة", "order": 4, "percentage": 5},
    {"id": "pri_c5", "name": "المشاركة في إعداد خطط التطوير المهني", "order": 5, "percentage": 5},
    {"id": "pri_c6", "name": "الإسهام في تحسين مستوى أداء المدرسة", "order": 6, "percentage": 5},
    {"id": "pri_c7", "name": "المشاركة في إعداد الخطط المدرسية", "order": 7, "percentage": 5},
    {"id": "pri_c8", "name": "متابعة تنفيذ الخطط المدرسية", "order": 8, "percentage": 5},
    {"id": "pri_c9", "name": "تهيئة الفرص والإمكانات لمشاركة الطلاب في الأنشطة", "order": 9, "percentage": 5},
    {"id": "pri_c10", "name": "تنفيذ إجراءات عملية لتحسين نتائج التعلم", "order": 10, "percentage": 5},
    {"id": "pri_c11", "name": "توظيف المنصات الرقمية في دعم التعليم والتعلم", "order": 11, "percentage": 5},
    {"id": "pri_c12", "name": "متابعة تعزيز السلوك الإيجابي للطلاب", "order": 12, "percentage": 5},
    {"id": "pri_c13", "name": "تهيئة بيئة مدرسية آمنة ومحفزة", "order": 13, "percentage": 5},
    {"id": "pri_c14", "name": "تقديم التغذية الراجعة ومتابعة مؤشرات الأداء الوظيفي", "order": 14, "percentage": 5}
]

# =========================
# التصنيفات الفرعية (المؤشرات السلوكية تحت كل معيار)
# =========================

PRINCIPAL_SUBCATEGORIES = [
    # pri_c1 - المرونة والتكيف مع ظروف العمل المختلفة
    {"id": "pri_c1_s1", "criterion_id": "pri_c1", "name": "إدارة المهام المتعددة بكفاءة وتنظيم", "order": 1},
    {"id": "pri_c1_s2", "criterion_id": "pri_c1", "name": "التكيف السريع مع المتغيرات والطوارئ", "order": 2},
    {"id": "pri_c1_s3", "criterion_id": "pri_c1", "name": "معالجة المشكلات الإدارية بقرارات مناسبة", "order": 3},
    {"id": "pri_c1_s4", "criterion_id": "pri_c1", "name": "التنسيق الفعال مع الجهات ذات العلاقة", "order": 4},
    {"id": "pri_c1_s5", "criterion_id": "pri_c1", "name": "المحافظة على استقرار العمل في الظروف الاستثنائية", "order": 5},

    # pri_c2 - دعم المبادرات النوعية
    {"id": "pri_c2_s1", "criterion_id": "pri_c2", "name": "إطلاق مبادرات تطويرية لرفع التحصيل الدراسي", "order": 1},
    {"id": "pri_c2_s2", "criterion_id": "pri_c2", "name": "توثيق ونشر الممارسات المدرسية المتميزة", "order": 2},
    {"id": "pri_c2_s3", "criterion_id": "pri_c2", "name": "توظيف التقنية في متابعة المبادرات وقياس أثرها", "order": 3},
    {"id": "pri_c2_s4", "criterion_id": "pri_c2", "name": "بناء شراكات مجتمعية داعمة للمبادرات", "order": 4},
    {"id": "pri_c2_s5", "criterion_id": "pri_c2", "name": "قياس وتحليل أثر المبادرات على الأداء العام للمدرسة", "order": 5},

    # pri_c3 - اتخاذ إجراءات تربوية لتحقيق الانضباط المدرسي
    {"id": "pri_c3_s1", "criterion_id": "pri_c3", "name": "إعداد خطة انضباط مدرسي واضحة ومعلنة", "order": 1},
    {"id": "pri_c3_s2", "criterion_id": "pri_c3", "name": "تطبيق قواعد السلوك والمواظبة بعدالة", "order": 2},
    {"id": "pri_c3_s3", "criterion_id": "pri_c3", "name": "متابعة تنفيذ برامج تعزيز السلوك الإيجابي", "order": 3},
    {"id": "pri_c3_s4", "criterion_id": "pri_c3", "name": "معالجة المخالفات بأساليب تربوية تصحيحية", "order": 4},
    {"id": "pri_c3_s5", "criterion_id": "pri_c3", "name": "تضمين برامج الانضباط ضمن الخطة التشغيلية", "order": 5},

    # pri_c4 - إدارة الموارد المدرسية بكفاءة
    {"id": "pri_c4_s1", "criterion_id": "pri_c4", "name": "توزيع المهام وفق الكفاءة والخبرة", "order": 1},
    {"id": "pri_c4_s2", "criterion_id": "pri_c4", "name": "تحقيق العدالة والشفافية في إسناد الأعمال", "order": 2},
    {"id": "pri_c4_s3", "criterion_id": "pri_c4", "name": "متابعة كفاءة استخدام الموارد البشرية والمادية", "order": 3},
    {"id": "pri_c4_s4", "criterion_id": "pri_c4", "name": "الإشراف على الصرف المالي وفق الأنظمة", "order": 4},
    {"id": "pri_c4_s5", "criterion_id": "pri_c4", "name": "تعظيم الاستفادة من الإمكانات المتاحة", "order": 5},

    # pri_c5 - المشاركة في إعداد خطط التطوير المهني
    {"id": "pri_c5_s1", "criterion_id": "pri_c5", "name": "إعداد خطة تطوير مهني مبنية على احتياجات المدرسة", "order": 1},
    {"id": "pri_c5_s2", "criterion_id": "pri_c5", "name": "حصر الاحتياجات التدريبية لمنسوبي المدرسة", "order": 2},
    {"id": "pri_c5_s3", "criterion_id": "pri_c5", "name": "متابعة تنفيذ البرامج التدريبية", "order": 3},
    {"id": "pri_c5_s4", "criterion_id": "pri_c5", "name": "تشجيع الحصول على الرخص المهنية", "order": 4},
    {"id": "pri_c5_s5", "criterion_id": "pri_c5", "name": "دعم نقل الخبرات بين المعلمين", "order": 5},

    # pri_c6 - الإسهام في تحسين مستوى أداء المدرسة
    {"id": "pri_c6_s1", "criterion_id": "pri_c6", "name": "إعداد وتنفيذ خطط تحسين مدرسية", "order": 1},
    {"id": "pri_c6_s2", "criterion_id": "pri_c6", "name": "بناء خطط علاجية لمعالجة جوانب الضعف", "order": 2},
    {"id": "pri_c6_s3", "criterion_id": "pri_c6", "name": "متابعة مؤشرات الأداء المدرسي بانتظام", "order": 3},
    {"id": "pri_c6_s4", "criterion_id": "pri_c6", "name": "دعم تطوير أداء المعلمين", "order": 4},
    {"id": "pri_c6_s5", "criterion_id": "pri_c6", "name": "تعزيز الشراكة مع المجتمع المدرسي", "order": 5},

    # pri_c7 - المشاركة في إعداد الخطط المدرسية
    {"id": "pri_c7_s1", "criterion_id": "pri_c7", "name": "إعداد الخطة التشغيلية وفق تحليل واقع المدرسة", "order": 1},
    {"id": "pri_c7_s2", "criterion_id": "pri_c7", "name": "وضع خطط بديلة للطوارئ", "order": 2},
    {"id": "pri_c7_s3", "criterion_id": "pri_c7", "name": "إعداد خطط الزيارات والإشراف", "order": 3},
    {"id": "pri_c7_s4", "criterion_id": "pri_c7", "name": "إعداد خطط الأمن والسلامة وإدارة المخاطر", "order": 4},
    {"id": "pri_c7_s5", "criterion_id": "pri_c7", "name": "إعداد خطة النموذج الإشرافي", "order": 5},

    # pri_c8 - متابعة تنفيذ الخطط المدرسية
    {"id": "pri_c8_s1", "criterion_id": "pri_c8", "name": "متابعة تنفيذ الخطة التشغيلية والتحسينية", "order": 1},
    {"id": "pri_c8_s2", "criterion_id": "pri_c8", "name": "متابعة خطط الانضباط والتطوير المهني", "order": 2},
    {"id": "pri_c8_s3", "criterion_id": "pri_c8", "name": "متابعة خطط النشاط الطلابي والبرامج العلاجية", "order": 3},
    {"id": "pri_c8_s4", "criterion_id": "pri_c8", "name": "متابعة خطط المعلمين وتقارير التنفيذ", "order": 4},
    {"id": "pri_c8_s5", "criterion_id": "pri_c8", "name": "تقييم أثر الخطط والمشروعات المنفذة", "order": 5},

    # pri_c9 - تهيئة الفرص والإمكانات لمشاركة الطلاب في الأنشطة
    {"id": "pri_c9_s1", "criterion_id": "pri_c9", "name": "توفير بيئة داعمة للأنشطة الصفية واللاصفية", "order": 1},
    {"id": "pri_c9_s2", "criterion_id": "pri_c9", "name": "تمكين الطلاب من المشاركة في الأنشطة الداخلية والخارجية", "order": 2},
    {"id": "pri_c9_s3", "criterion_id": "pri_c9", "name": "دعم المسابقات والمنافسات الطلابية", "order": 3},
    {"id": "pri_c9_s4", "criterion_id": "pri_c9", "name": "تطوير المشاركات الطلابية ورفع مستوى التمثيل الخارجي", "order": 4},
    {"id": "pri_c9_s5", "criterion_id": "pri_c9", "name": "رصد الإنجازات والمراكز المحققة", "order": 5},

    # pri_c10 - تنفيذ إجراءات عملية لتحسين نتائج التعلم
    {"id": "pri_c10_s1", "criterion_id": "pri_c10", "name": "تحليل نتائج المتعلمين وتصنيف مستوياتهم", "order": 1},
    {"id": "pri_c10_s2", "criterion_id": "pri_c10", "name": "تفسير النتائج لاتخاذ قرارات علاجية وإثرائية", "order": 2},
    {"id": "pri_c10_s3", "criterion_id": "pri_c10", "name": "متابعة نمو التحصيل الدراسي بشكل دوري", "order": 3},
    {"id": "pri_c10_s4", "criterion_id": "pri_c10", "name": "تطوير استراتيجيات تعليمية داعمة", "order": 4},
    {"id": "pri_c10_s5", "criterion_id": "pri_c10", "name": "التواصل مع أولياء الأمور بشأن النتائج", "order": 5},

    # pri_c11 - توظيف المنصات الرقمية في دعم التعليم والتعلم
    {"id": "pri_c11_s1", "criterion_id": "pri_c11", "name": "متابعة التزام المعلمين والطلاب باستخدام المنصات الرقمية", "order": 1},
    {"id": "pri_c11_s2", "criterion_id": "pri_c11", "name": "تحليل تقارير الأداء الرقمي", "order": 2},
    {"id": "pri_c11_s3", "criterion_id": "pri_c11", "name": "اتخاذ إجراءات تصحيحية عند وجود قصور", "order": 3},
    {"id": "pri_c11_s4", "criterion_id": "pri_c11", "name": "دعم التحول الرقمي في المدرسة", "order": 4},
    # لاحظ: المعيار الأصلي يحتوي على 4 نقاط فقط، ولكن أضفنا نقطة خامسة افتراضية لاستكمال العدد (يمكن دمجها مع الرابعة)
    # سأضيف نقطة خامسة مكملة:
    {"id": "pri_c11_s5", "criterion_id": "pri_c11", "name": "تطوير كفاءة استخدام التقنية في العمليات التعليمية", "order": 5},

    # pri_c12 - متابعة تعزيز السلوك الإيجابي للطلاب
    {"id": "pri_c12_s1", "criterion_id": "pri_c12", "name": "الإشراف على برامج تعزيز السلوك الإيجابي", "order": 1},
    {"id": "pri_c12_s2", "criterion_id": "pri_c12", "name": "متابعة الحالات الفردية بالتنسيق مع التوجيه الطلابي", "order": 2},
    {"id": "pri_c12_s3", "criterion_id": "pri_c12", "name": "تحليل تقارير التحسن السلوكي", "order": 3},
    {"id": "pri_c12_s4", "criterion_id": "pri_c12", "name": "تكريم الطلاب المتحسنين والمتميزين", "order": 4},
    {"id": "pri_c12_s5", "criterion_id": "pri_c12", "name": "تبني أساليب مبتكرة لتعزيز السلوك الإيجابي", "order": 5},

    # pri_c13 - تهيئة بيئة مدرسية آمنة ومحفزة
    {"id": "pri_c13_s1", "criterion_id": "pri_c13", "name": "متابعة تطبيق اشتراطات الأمن والسلامة", "order": 1},
    {"id": "pri_c13_s2", "criterion_id": "pri_c13", "name": "معالجة الأعطال والمخاطر فوراً", "order": 2},
    {"id": "pri_c13_s3", "criterion_id": "pri_c13", "name": "توفير بيئة مدرسية جاذبة ومحفزة", "order": 3},
    {"id": "pri_c13_s4", "criterion_id": "pri_c13", "name": "تعزيز الأمان النفسي للطلاب والعاملين", "order": 4},
    {"id": "pri_c13_s5", "criterion_id": "pri_c13", "name": "متابعة البلاغات والتقارير الدورية", "order": 5},

    # pri_c14 - تقديم التغذية الراجعة ومتابعة مؤشرات الأداء الوظيفي
    {"id": "pri_c14_s1", "criterion_id": "pri_c14", "name": "تنفيذ زيارات صفية دورية", "order": 1},
    {"id": "pri_c14_s2", "criterion_id": "pri_c14", "name": "تقديم تغذية راجعة تطويرية للمعلمين", "order": 2},
    {"id": "pri_c14_s3", "criterion_id": "pri_c14", "name": "متابعة مؤشرات الانضباط والنشاط", "order": 3},
    {"id": "pri_c14_s4", "criterion_id": "pri_c14", "name": "تعزيز نقاط القوة ومعالجة جوانب التحسين", "order": 4},
    {"id": "pri_c14_s5", "criterion_id": "pri_c14", "name": "توثيق الأداء ومتابعة التطور المهني", "order": 5}
]

# =========================
# التقارير (10 تقارير لكل تصنيف فرعي)
# =========================

PRINCIPAL_REPORTS = [
    # pri_c1_s1 - إدارة المهام المتعددة بكفاءة وتنظيم
    {"id": "pri_c1_s1_r01", "subcategory_id": "pri_c1_s1", "name": "تقرير تنظيم المهام اليومية لقادة الأقسام", "order": 1},
    {"id": "pri_c1_s1_r02", "subcategory_id": "pri_c1_s1", "name": "تقرير أولويات العمل في الفترات المزدحمة (الاختبارات)", "order": 2},
    {"id": "pri_c1_s1_r03", "subcategory_id": "pri_c1_s1", "name": "تقرير كفاءة إدارة الوقت لدى الفريق الإداري", "order": 3},
    {"id": "pri_c1_s1_r04", "subcategory_id": "pri_c1_s1", "name": "تقرير توزيع المهام الإشرافية بين الوكلاء", "order": 4},
    {"id": "pri_c1_s1_r05", "subcategory_id": "pri_c1_s1", "name": "تقرير استخدام أدوات تنظيم المهام الرقمية", "order": 5},
    {"id": "pri_c1_s1_r06", "subcategory_id": "pri_c1_s1", "name": "تقرير التوازن بين المهام الروتينية والطارئة", "order": 6},
    {"id": "pri_c1_s1_r07", "subcategory_id": "pri_c1_s1", "name": "تقرير متابعة إنجاز المهام الإدارية في وقتها", "order": 7},
    {"id": "pri_c1_s1_r08", "subcategory_id": "pri_c1_s1", "name": "تقرير تفويض المهام وتوزيع المسؤوليات", "order": 8},
    {"id": "pri_c1_s1_r09", "subcategory_id": "pri_c1_s1", "name": "تقرير مرونة إعادة توزيع المهام عند الحاجة", "order": 9},
    {"id": "pri_c1_s1_r10", "subcategory_id": "pri_c1_s1", "name": "تقرير أثر تنظيم المهام على رضا العاملين", "order": 10},

    # pri_c1_s2 - التكيف السريع مع المتغيرات والطوارئ
    {"id": "pri_c1_s2_r01", "subcategory_id": "pri_c1_s2", "name": "تقرير التعامل مع حالات الطوارئ (أمطار، حريق)", "order": 1},
    {"id": "pri_c1_s2_r02", "subcategory_id": "pri_c1_s2", "name": "تقرير التكيف مع التعاميم الوزارية المفاجئة", "order": 2},
    {"id": "pri_c1_s2_r03", "subcategory_id": "pri_c1_s2", "name": "تقرير مرونة تعديل الجدول لظروف قاهرة", "order": 3},
    {"id": "pri_c1_s2_r04", "subcategory_id": "pri_c1_s2", "name": "تقرير الاستجابة السريعة لنقص المعلمين", "order": 4},
    {"id": "pri_c1_s2_r05", "subcategory_id": "pri_c1_s2", "name": "تقرير إعادة تنظيم العمل أثناء انقطاع الخدمات", "order": 5},
    {"id": "pri_c1_s2_r06", "subcategory_id": "pri_c1_s2", "name": "تقرير سرعة تجهيز البدائل للأنشطة الملغاة", "order": 6},
    {"id": "pri_c1_s2_r07", "subcategory_id": "pri_c1_s2", "name": "تقرير التعامل مع زيادة أعداد الطلاب فجأة", "order": 7},
    {"id": "pri_c1_s2_r08", "subcategory_id": "pri_c1_s2", "name": "تقرير التكيف مع تغيرات المناهج الدراسية", "order": 8},
    {"id": "pri_c1_s2_r09", "subcategory_id": "pri_c1_s2", "name": "تقرير مرونة خطط الإخلاء في الظروف المختلفة", "order": 9},
    {"id": "pri_c1_s2_r10", "subcategory_id": "pri_c1_s2", "name": "تقرير تقييم سرعة الاستجابة للأحداث غير المتوقعة", "order": 10},

    # pri_c1_s3 - معالجة المشكلات الإدارية بقرارات مناسبة
    {"id": "pri_c1_s3_r01", "subcategory_id": "pri_c1_s3", "name": "تقرير معالجة مشكلة نقص المعلمين في تخصص ما", "order": 1},
    {"id": "pri_c1_s3_r02", "subcategory_id": "pri_c1_s3", "name": "تقرير حل النزاعات بين أعضاء هيئة التدريس", "order": 2},
    {"id": "pri_c1_s3_r03", "subcategory_id": "pri_c1_s3", "name": "تقرير معالجة شكاوى أولياء الأمور المتكررة", "order": 3},
    {"id": "pri_c1_s3_r04", "subcategory_id": "pri_c1_s3", "name": "تقرير قرارات تحسين البيئة المدرسية بعد شكاوى", "order": 4},
    {"id": "pri_c1_s3_r05", "subcategory_id": "pri_c1_s3", "name": "تقرير إجراءات حل مشكلات الصيانة العاجلة", "order": 5},
    {"id": "pri_c1_s3_r06", "subcategory_id": "pri_c1_s3", "name": "تقرير معالجة تدني نتائج الطلاب في مادة", "order": 6},
    {"id": "pri_c1_s3_r07", "subcategory_id": "pri_c1_s3", "name": "تقرير قرارات إدارية في حالات غياب القيادات", "order": 7},
    {"id": "pri_c1_s3_r08", "subcategory_id": "pri_c1_s3", "name": "تقرير حل مشكلات الموازنة المالية", "order": 8},
    {"id": "pri_c1_s3_r09", "subcategory_id": "pri_c1_s3", "name": "تقرير التعامل مع مشكلات الانضباط الطلابي", "order": 9},
    {"id": "pri_c1_s3_r10", "subcategory_id": "pri_c1_s3", "name": "تقرير فعالية القرارات في حل المشكلات الإدارية", "order": 10},

    # pri_c1_s4 - التنسيق الفعال مع الجهات ذات العلاقة
    {"id": "pri_c1_s4_r01", "subcategory_id": "pri_c1_s4", "name": "تقرير التنسيق مع مكتب التعليم للدعم والزيارات", "order": 1},
    {"id": "pri_c1_s4_r02", "subcategory_id": "pri_c1_s4", "name": "تقرير التعاون مع الدفاع المدني في خطط السلامة", "order": 2},
    {"id": "pri_c1_s4_r03", "subcategory_id": "pri_c1_s4", "name": "تقرير التنسيق مع هيئة الصحة العامة في البرامج الوقائية", "order": 3},
    {"id": "pri_c1_s4_r04", "subcategory_id": "pri_c1_s4", "name": "تقرير الشراكة مع المراكز الصحية للكشف المبكر", "order": 4},
    {"id": "pri_c1_s4_r05", "subcategory_id": "pri_c1_s4", "name": "تقرير التنسيق مع قسم الإشراف التربوي", "order": 5},
    {"id": "pri_c1_s4_r06", "subcategory_id": "pri_c1_s4", "name": "تقرير التواصل مع أولياء الأمور عبر مجالس الآباء", "order": 6},
    {"id": "pri_c1_s4_r07", "subcategory_id": "pri_c1_s4", "name": "تقرير التنسيق مع المؤسسات المجتمعية لدعم الأنشطة", "order": 7},
    {"id": "pri_c1_s4_r08", "subcategory_id": "pri_c1_s4", "name": "تقرير التعاون مع الشرطة في برامج التوعية", "order": 8},
    {"id": "pri_c1_s4_r09", "subcategory_id": "pri_c1_s4", "name": "تقرير التنسيق مع الجهات المانحة للموارد", "order": 9},
    {"id": "pri_c1_s4_r10", "subcategory_id": "pri_c1_s4", "name": "تقرير فعالية التنسيق مع الجهات الخارجية", "order": 10},

    # pri_c1_s5 - المحافظة على استقرار العمل في الظروف الاستثنائية
    {"id": "pri_c1_s5_r01", "subcategory_id": "pri_c1_s5", "name": "تقرير استمرارية التعلم أثناء تعليق الدراسة (كوفيد-19)", "order": 1},
    {"id": "pri_c1_s5_r02", "subcategory_id": "pri_c1_s5", "name": "تقرير الحفاظ على سير العمل أثناء غياب مدير المدرسة", "order": 2},
    {"id": "pri_c1_s5_r03", "subcategory_id": "pri_c1_s5", "name": "تقرير استقرار العمل في ظل تغيير الكادر الإداري", "order": 3},
    {"id": "pri_c1_s5_r04", "subcategory_id": "pri_c1_s5", "name": "تقرير ضبط الانضباط في فترات الاختبارات", "order": 4},
    {"id": "pri_c1_s5_r05", "subcategory_id": "pri_c1_s5", "name": "تقرير استمرارية الخدمات أثناء الصيانة الطارئة", "order": 5},
    {"id": "pri_c1_s5_r06", "subcategory_id": "pri_c1_s5", "name": "تقرير الحفاظ على الهدوء في الأزمات", "order": 6},
    {"id": "pri_c1_s5_r07", "subcategory_id": "pri_c1_s5", "name": "تقرير استقرار العمل بعد حوادث مؤسفة", "order": 7},
    {"id": "pri_c1_s5_r08", "subcategory_id": "pri_c1_s5", "name": "تقرير استمرارية البرامج العلاجية أثناء الظروف", "order": 8},
    {"id": "pri_c1_s5_r09", "subcategory_id": "pri_c1_s5", "name": "تقرير دور القيادة في طمأنة العاملين أثناء الطوارئ", "order": 9},
    {"id": "pri_c1_s5_r10", "subcategory_id": "pri_c1_s5", "name": "تقرير تقييم استقرار العمل في الظروف الاستثنائية", "order": 10},

    # pri_c2_s1 - إطلاق مبادرات تطويرية لرفع التحصيل الدراسي
    {"id": "pri_c2_s1_r01", "subcategory_id": "pri_c2_s1", "name": "تقرير مبادرة تحسين مهارات القراءة في المرحلة الابتدائية", "order": 1},
    {"id": "pri_c2_s1_r02", "subcategory_id": "pri_c2_s1", "name": "تقرير مشروع رفع التحصيل في الرياضيات باستخدام الذكاء الاصطناعي", "order": 2},
    {"id": "pri_c2_s1_r03", "subcategory_id": "pri_c2_s1", "name": "تقرير مبادرة مجموعات التقوية الصباحية", "order": 3},
    {"id": "pri_c2_s1_r04", "subcategory_id": "pri_c2_s1", "name": "تقرير برنامج إثرائي للمتفوقين في العلوم", "order": 4},
    {"id": "pri_c2_s1_r05", "subcategory_id": "pri_c2_s1", "name": "تقرير مبادرة التعلم القائم على المشاريع", "order": 5},
    {"id": "pri_c2_s1_r06", "subcategory_id": "pri_c2_s1", "name": "تقرير مسابقة التحدي القرائي بين الفصول", "order": 6},
    {"id": "pri_c2_s1_r07", "subcategory_id": "pri_c2_s1", "name": "تقرير مبادرة الأندية العلمية بعد الدوام", "order": 7},
    {"id": "pri_c2_s1_r08", "subcategory_id": "pri_c2_s1", "name": "تقرير برنامج تحسين نتائج المواد الأساسية", "order": 8},
    {"id": "pri_c2_s1_r09", "subcategory_id": "pri_c2_s1", "name": "تقرير مبادرة الدروس التفاعلية عبر المنصات", "order": 9},
    {"id": "pri_c2_s1_r10", "subcategory_id": "pri_c2_s1", "name": "تقرير أثر المبادرات على نتائج الاختبارات الدولية", "order": 10},

    # pri_c2_s2 - توثيق ونشر الممارسات المدرسية المتميزة
    {"id": "pri_c2_s2_r01", "subcategory_id": "pri_c2_s2", "name": "تقرير توثيق تجربة التعلم عن بعد الناجحة", "order": 1},
    {"id": "pri_c2_s2_r02", "subcategory_id": "pri_c2_s2", "name": "تقرير نشر ممارسات المعلمين المتميزين عبر الموقع", "order": 2},
    {"id": "pri_c2_s2_r03", "subcategory_id": "pri_c2_s2", "name": "تقرير إصدار نشرات دورية لإنجازات المدرسة", "order": 3},
    {"id": "pri_c2_s2_r04", "subcategory_id": "pri_c2_s2", "name": "تقرير توثيق مبادرات الانضباط الإيجابي", "order": 4},
    {"id": "pri_c2_s2_r05", "subcategory_id": "pri_c2_s2", "name": "تقرير مشاركة قصص النجاح في ملتقيات التعليم", "order": 5},
    {"id": "pri_c2_s2_r06", "subcategory_id": "pri_c2_s2", "name": "تقرير قاعدة بيانات للممارسات المتميزة قابلة للتصفح", "order": 6},
    {"id": "pri_c2_s2_r07", "subcategory_id": "pri_c2_s2", "name": "تقرير فيديوهات تعليمية توثق استراتيجيات ناجحة", "order": 7},
    {"id": "pri_c2_s2_r08", "subcategory_id": "pri_c2_s2", "name": "تقرير نشر ثقافة التميز عبر الإذاعة المدرسية", "order": 8},
    {"id": "pri_c2_s2_r09", "subcategory_id": "pri_c2_s2", "name": "تقرير توثيق تجارب الشراكة المجتمعية", "order": 9},
    {"id": "pri_c2_s2_r10", "subcategory_id": "pri_c2_s2", "name": "تقرير أثر النشر على تبني ممارسات جديدة", "order": 10},

    # pri_c2_s3 - توظيف التقنية في متابعة المبادرات وقياس أثرها
    {"id": "pri_c2_s3_r01", "subcategory_id": "pri_c2_s3", "name": "تقرير استخدام لوحات المؤشرات لمتابعة المبادرات", "order": 1},
    {"id": "pri_c2_s3_r02", "subcategory_id": "pri_c2_s3", "name": "تقرير تحليل بيانات المبادرات عبر نظام نور", "order": 2},
    {"id": "pri_c2_s3_r03", "subcategory_id": "pri_c2_s3", "name": "تقرير استطلاعات إلكترونية لقياس رضا المستفيدين", "order": 3},
    {"id": "pri_c2_s3_r04", "subcategory_id": "pri_c2_s3", "name": "تقرير منصة إلكترونية لمتابعة تقدم المبادرات", "order": 4},
    {"id": "pri_c2_s3_r05", "subcategory_id": "pri_c2_s3", "name": "تقرير توظيف الذكاء الاصطناعي في تحليل الأثر", "order": 5},
    {"id": "pri_c2_s3_r06", "subcategory_id": "pri_c2_s3", "name": "تقرير قياس العائد على الاستثمار في المبادرات", "order": 6},
    {"id": "pri_c2_s3_r07", "subcategory_id": "pri_c2_s3", "name": "تقرير تحليل مؤشرات الأداء الرئيسية للمبادرات", "order": 7},
    {"id": "pri_c2_s3_r08", "subcategory_id": "pri_c2_s3", "name": "تقرير استخدام الجداول التفاعلية في العروض", "order": 8},
    {"id": "pri_c2_s3_r09", "subcategory_id": "pri_c2_s3", "name": "تقرير توثيق الأثر باستخدام الوسائط المتعددة", "order": 9},
    {"id": "pri_c2_s3_r10", "subcategory_id": "pri_c2_s3", "name": "تقرير تحديث البيانات دورياً لمتابعة المبادرات", "order": 10},

    # pri_c2_s4 - بناء شراكات مجتمعية داعمة للمبادرات
    {"id": "pri_c2_s4_r01", "subcategory_id": "pri_c2_s4", "name": "تقرير الشراكة مع شركة محلية لدعم المختبرات", "order": 1},
    {"id": "pri_c2_s4_r02", "subcategory_id": "pri_c2_s4", "name": "تقرير التعاون مع الجمعيات الخيرية في برامج العطاء", "order": 2},
    {"id": "pri_c2_s4_r03", "subcategory_id": "pri_c2_s4", "name": "تقرير شراكة مع جامعة لتقديم إرشاد مهني", "order": 3},
    {"id": "pri_c2_s4_r04", "subcategory_id": "pri_c2_s4", "name": "تقرير مذكرات تفاهم مع أندية رياضية للأنشطة", "order": 4},
    {"id": "pri_c2_s4_r05", "subcategory_id": "pri_c2_s4", "name": "تقرير دعم أولياء الأمور لمبادرات المدرسة", "order": 5},
    {"id": "pri_c2_s4_r06", "subcategory_id": "pri_c2_s4", "name": "تقرير شراكة مع مركز تدريب لتقديم دورات", "order": 6},
    {"id": "pri_c2_s4_r07", "subcategory_id": "pri_c2_s4", "name": "تقرير مساهمات رجال الأعمال في تجهيز المرافق", "order": 7},
    {"id": "pri_c2_s4_r08", "subcategory_id": "pri_c2_s4", "name": "تقرير شراكة مع المكتبة العامة لتعزيز القراءة", "order": 8},
    {"id": "pri_c2_s4_r09", "subcategory_id": "pri_c2_s4", "name": "تقرير التعاون مع مؤسسات ذوي الإعاقة", "order": 9},
    {"id": "pri_c2_s4_r10", "subcategory_id": "pri_c2_s4", "name": "تقرير قياس أثر الشراكات على المبادرات", "order": 10},

    # pri_c2_s5 - قياس وتحليل أثر المبادرات على الأداء العام للمدرسة
    {"id": "pri_c2_s5_r01", "subcategory_id": "pri_c2_s5", "name": "تقرير أثر مبادرة تحسين القراءة على نتائج اللغة العربية", "order": 1},
    {"id": "pri_c2_s5_r02", "subcategory_id": "pri_c2_s5", "name": "تقرير تحليل أثر برامج التقوية على نسبة النجاح", "order": 2},
    {"id": "pri_c2_s5_r03", "subcategory_id": "pri_c2_s5", "name": "تقرير قياس أثر مبادرات الانضباط على الغياب", "order": 3},
    {"id": "pri_c2_s5_r04", "subcategory_id": "pri_c2_s5", "name": "تقرير تحليل أثر الأنشطة على رضا الطلاب", "order": 4},
    {"id": "pri_c2_s5_r05", "subcategory_id": "pri_c2_s5", "name": "تقرير قياس العائد على المبادرات التدريبية للمعلمين", "order": 5},
    {"id": "pri_c2_s5_r06", "subcategory_id": "pri_c2_s5", "name": "تقرير أثر مبادرات الشراكة على تحسين الموارد", "order": 6},
    {"id": "pri_c2_s5_r07", "subcategory_id": "pri_c2_s5", "name": "تقرير تحليل البيانات المقارنة قبل وبعد المبادرات", "order": 7},
    {"id": "pri_c2_s5_r08", "subcategory_id": "pri_c2_s5", "name": "تقرير مؤشرات الأداء المرتبطة بالمبادرات", "order": 8},
    {"id": "pri_c2_s5_r09", "subcategory_id": "pri_c2_s5", "name": "تقرير استمرارية أثر المبادرات على المدى البعيد", "order": 9},
    {"id": "pri_c2_s5_r10", "subcategory_id": "pri_c2_s5", "name": "تقرير توصيات تحسين المبادرات بناءً على التحليل", "order": 10},

    # pri_c3_s1 - إعداد خطة انضباط مدرسي واضحة ومعلنة
    {"id": "pri_c3_s1_r01", "subcategory_id": "pri_c3_s1", "name": "تقرير خطة الانضباط المدرسي للعام الدراسي", "order": 1},
    {"id": "pri_c3_s1_r02", "subcategory_id": "pri_c3_s1", "name": "تقرير إعلان خطة الانضباط للمجتمع المدرسي", "order": 2},
    {"id": "pri_c3_s1_r03", "subcategory_id": "pri_c3_s1", "name": "تقرير ورش عمل تعريفية بقواعد السلوك", "order": 3},
    {"id": "pri_c3_s1_r04", "subcategory_id": "pri_c3_s1", "name": "تقرير تضمين خطة الانضباط في دليل الطالب", "order": 4},
    {"id": "pri_c3_s1_r05", "subcategory_id": "pri_c3_s1", "name": "تقرير اجتماعات أولياء الأمور لمناقشة الانضباط", "order": 5},
    {"id": "pri_c3_s1_r06", "subcategory_id": "pri_c3_s1", "name": "تقرير نشر الخطة عبر المنصات الإلكترونية", "order": 6},
    {"id": "pri_c3_s1_r07", "subcategory_id": "pri_c3_s1", "name": "تقرير توحيد مفاهيم الانضباط بين المعلمين", "order": 7},
    {"id": "pri_c3_s1_r08", "subcategory_id": "pri_c3_s1", "name": "تقرير مراجعة الخطة مع التوجيه الطلابي", "order": 8},
    {"id": "pri_c3_s1_r09", "subcategory_id": "pri_c3_s1", "name": "تقرير تحديث الخطة بناءً على تقارير سابقة", "order": 9},
    {"id": "pri_c3_s1_r10", "subcategory_id": "pri_c3_s1", "name": "تقرير قياس وعي الطلاب بالخطة", "order": 10},

    # pri_c3_s2 - تطبيق قواعد السلوك والمواظبة بعدالة
    {"id": "pri_c3_s2_r01", "subcategory_id": "pri_c3_s2", "name": "تقرير حالات تطبيق قواعد السلوك بشكل موحد", "order": 1},
    {"id": "pri_c3_s2_r02", "subcategory_id": "pri_c3_s2", "name": "تقرير متابعة انضباط الطلاب يومياً", "order": 2},
    {"id": "pri_c3_s2_r03", "subcategory_id": "pri_c3_s2", "name": "تقرير لجنة الانضباط وقراراتها", "order": 3},
    {"id": "pri_c3_s2_r04", "subcategory_id": "pri_c3_s2", "name": "تقرير عدالة التعامل مع المخالفات المتشابهة", "order": 4},
    {"id": "pri_c3_s2_r05", "subcategory_id": "pri_c3_s2", "name": "تقرير توثيق المخالفات والإجراءات", "order": 5},
    {"id": "pri_c3_s2_r06", "subcategory_id": "pri_c3_s2", "name": "تقرير استئناف الطلاب وأولياء الأمور على القرارات", "order": 6},
    {"id": "pri_c3_s2_r07", "subcategory_id": "pri_c3_s2", "name": "تقرير مراجعة تطبيق القواعد مع وكلاء المدرسة", "order": 7},
    {"id": "pri_c3_s2_r08", "subcategory_id": "pri_c3_s2", "name": "تقرير الشفافية في الإجراءات التأديبية", "order": 8},
    {"id": "pri_c3_s2_r09", "subcategory_id": "pri_c3_s2", "name": "تقرير تدريب المعلمين على تطبيق القواعد", "order": 9},
    {"id": "pri_c3_s2_r10", "subcategory_id": "pri_c3_s2", "name": "تقرير مؤشرات العدالة في تطبيق الانضباط", "order": 10},

    # pri_c3_s3 - متابعة تنفيذ برامج تعزيز السلوك الإيجابي
    {"id": "pri_c3_s3_r01", "subcategory_id": "pri_c3_s3", "name": "تقرير برنامج الطالب المثالي شهرياً", "order": 1},
    {"id": "pri_c3_s3_r02", "subcategory_id": "pri_c3_s3", "name": "تقرير مبادرات تعزيز السلوك في الفصول", "order": 2},
    {"id": "pri_c3_s3_r03", "subcategory_id": "pri_c3_s3", "name": "تقرير ورش عمل عن القيم والأخلاق", "order": 3},
    {"id": "pri_c3_s3_r04", "subcategory_id": "pri_c3_s3", "name": "تقرير تكريم الطلاب المتميزين سلوكياً", "order": 4},
    {"id": "pri_c3_s3_r05", "subcategory_id": "pri_c3_s3", "name": "تقرير برامج الإرشاد الجماعي لتعزيز السلوك", "order": 5},
    {"id": "pri_c3_s3_r06", "subcategory_id": "pri_c3_s3", "name": "تقرير أنشطة توعوية عن المواظبة", "order": 6},
    {"id": "pri_c3_s3_r07", "subcategory_id": "pri_c3_s3", "name": "تقرير مسابقات أفضل فصل منضبط", "order": 7},
    {"id": "pri_c3_s3_r08", "subcategory_id": "pri_c3_s3", "name": "تقرير متابعة تنفيذ برامج التحسين السلوكي", "order": 8},
    {"id": "pri_c3_s3_r09", "subcategory_id": "pri_c3_s3", "name": "تقرير شراكات مع أسر لتعديل السلوك", "order": 9},
    {"id": "pri_c3_s3_r10", "subcategory_id": "pri_c3_s3", "name": "تقرير قياس أثر البرامج على تحسن السلوك", "order": 10},

    # pri_c3_s4 - معالجة المخالفات بأساليب تربوية تصحيحية
    {"id": "pri_c3_s4_r01", "subcategory_id": "pri_c3_s4", "name": "تقرير خطط تعديل السلوك للطلاب المخالفين", "order": 1},
    {"id": "pri_c3_s4_r02", "subcategory_id": "pri_c3_s4", "name": "تقرير جلسات الإرشاد الفردي للطلاب", "order": 2},
    {"id": "pri_c3_s4_r03", "subcategory_id": "pri_c3_s4", "name": "تقرير برامج الخدمة المجتمعية كبديل للعقاب", "order": 3},
    {"id": "pri_c3_s4_r04", "subcategory_id": "pri_c3_s4", "name": "تقرير متابعة الحالات السلوكية مع المرشد", "order": 4},
    {"id": "pri_c3_s4_r05", "subcategory_id": "pri_c3_s4", "name": "تقرير التواصل مع أولياء الأمور في المخالفات", "order": 5},
    {"id": "pri_c3_s4_r06", "subcategory_id": "pri_c3_s4", "name": "تقرير تحويل المخالفات المتكررة إلى جهات متخصصة", "order": 6},
    {"id": "pri_c3_s4_r07", "subcategory_id": "pri_c3_s4", "name": "تقرير برامج التوعية الوقائية قبل المخالفات", "order": 7},
    {"id": "pri_c3_s4_r08", "subcategory_id": "pri_c3_s4", "name": "تقرير تحليل أسباب المخالفات وعلاجها", "order": 8},
    {"id": "pri_c3_s4_r09", "subcategory_id": "pri_c3_s4", "name": "تقرير قصص نجاح في تعديل السلوك", "order": 9},
    {"id": "pri_c3_s4_r10", "subcategory_id": "pri_c3_s4", "name": "تقرير تقييم فاعلية الأساليب التصحيحية", "order": 10},

    # pri_c3_s5 - تضمين برامج الانضباط ضمن الخطة التشغيلية
    {"id": "pri_c3_s5_r01", "subcategory_id": "pri_c3_s5", "name": "تقرير دمج أنشطة الانضباط في الخطة السنوية", "order": 1},
    {"id": "pri_c3_s5_r02", "subcategory_id": "pri_c3_s5", "name": "تقرير تخصيص موارد للانضباط في الميزانية", "order": 2},
    {"id": "pri_c3_s5_r03", "subcategory_id": "pri_c3_s5", "name": "تقرير جدولة برامج تعزيز السلوك على مدار العام", "order": 3},
    {"id": "pri_c3_s5_r04", "subcategory_id": "pri_c3_s5", "name": "تقرير مؤشرات الانضباط في تقارير الخطة", "order": 4},
    {"id": "pri_c3_s5_r05", "subcategory_id": "pri_c3_s5", "name": "تقرير مسؤوليات الفرق في تنفيذ خطة الانضباط", "order": 5},
    {"id": "pri_c3_s5_r06", "subcategory_id": "pri_c3_s5", "name": "تقرير تكامل خطة الانضباط مع خطط أخرى", "order": 6},
    {"id": "pri_c3_s5_r07", "subcategory_id": "pri_c3_s5", "name": "تقرير مراجعة الخطة التشغيلية للانضباط", "order": 7},
    {"id": "pri_c3_s5_r08", "subcategory_id": "pri_c3_s5", "name": "تقرير إبلاغ جميع العاملين بخطة الانضباط", "order": 8},
    {"id": "pri_c3_s5_r09", "subcategory_id": "pri_c3_s5", "name": "تقرير ربط خطط الانضباط بالحوافز", "order": 9},
    {"id": "pri_c3_s5_r10", "subcategory_id": "pri_c3_s5", "name": "تقرير تحديث خطة الانضباط في الخطة التشغيلية", "order": 10},

    # pri_c4_s1 - توزيع المهام وفق الكفاءة والخبرة
    {"id": "pri_c4_s1_r01", "subcategory_id": "pri_c4_s1", "name": "تقرير توزيع الحصص على المعلمين حسب التخصص", "order": 1},
    {"id": "pri_c4_s1_r02", "subcategory_id": "pri_c4_s1", "name": "تقرير إسناد المهام الإشرافية للأكفاء", "order": 2},
    {"id": "pri_c4_s1_r03", "subcategory_id": "pri_c4_s1", "name": "تقرير تشكيل لجان بناءً على الخبرات", "order": 3},
    {"id": "pri_c4_s1_r04", "subcategory_id": "pri_c4_s1", "name": "تقرير توزيع أعمال الامتحانات على المراقبين", "order": 4},
    {"id": "pri_c4_s1_r05", "subcategory_id": "pri_c4_s1", "name": "تقرير تكليف قائد فريق النشاط المناسب", "order": 5},
    {"id": "pri_c4_s1_r06", "subcategory_id": "pri_c4_s1", "name": "تقرير مراجعة التوزيع مع نهاية العام", "order": 6},
    {"id": "pri_c4_s1_r07", "subcategory_id": "pri_c4_s1", "name": "تقرير تحسين التوزيع بناءً على الأداء", "order": 7},
    {"id": "pri_c4_s1_r08", "subcategory_id": "pri_c4_s1", "name": "تقرير مشاركة المعلمين في اختيار المهام", "order": 8},
    {"id": "pri_c4_s1_r09", "subcategory_id": "pri_c4_s1", "name": "تقرير تكافؤ الفرص في توزيع المهام", "order": 9},
    {"id": "pri_c4_s1_r10", "subcategory_id": "pri_c4_s1", "name": "تقرير أثر التوزيع على الإنتاجية", "order": 10},

    # pri_c4_s2 - تحقيق العدالة والشفافية في إسناد الأعمال
    {"id": "pri_c4_s2_r01", "subcategory_id": "pri_c4_s2", "name": "تقرير معايير إسناد الأعمال للمعلمين", "order": 1},
    {"id": "pri_c4_s2_r02", "subcategory_id": "pri_c4_s2", "name": "تقرير الإعلان عن آلية اختيار قادة الأقسام", "order": 2},
    {"id": "pri_c4_s2_r03", "subcategory_id": "pri_c4_s2", "name": "تقرير الشكاوى المتعلقة بعدم العدالة", "order": 3},
    {"id": "pri_c4_s2_r04", "subcategory_id": "pri_c4_s2", "name": "تقرير تدوير المهام الإضافية بشكل عادل", "order": 4},
    {"id": "pri_c4_s2_r05", "subcategory_id": "pri_c4_s2", "name": "تقرير شفافية الإجراءات في تشكيل اللجان", "order": 5},
    {"id": "pri_c4_s2_r06", "subcategory_id": "pri_c4_s2", "name": "تقرير استبيان حول العدالة بين الموظفين", "order": 6},
    {"id": "pri_c4_s2_r07", "subcategory_id": "pri_c4_s2", "name": "تقرير توثيق القرارات وإتاحتها للجميع", "order": 7},
    {"id": "pri_c4_s2_r08", "subcategory_id": "pri_c4_s2", "name": "تقرير مراجعة إسناد المهام مع ممثلي المعلمين", "order": 8},
    {"id": "pri_c4_s2_r09", "subcategory_id": "pri_c4_s2", "name": "تقرير تطوير سياسة إسناد الأعمال", "order": 9},
    {"id": "pri_c4_s2_r10", "subcategory_id": "pri_c4_s2", "name": "تقرير مؤشرات العدالة في التوزيع", "order": 10},

    # pri_c4_s3 - متابعة كفاءة استخدام الموارد البشرية والمادية
    {"id": "pri_c4_s3_r01", "subcategory_id": "pri_c4_s3", "name": "تقرير استغلال أوقات المعلمين في الأنشطة", "order": 1},
    {"id": "pri_c4_s3_r02", "subcategory_id": "pri_c4_s3", "name": "تقرير صيانة الأجهزة والمختبرات", "order": 2},
    {"id": "pri_c4_s3_r03", "subcategory_id": "pri_c4_s3", "name": "تقرير استخدام الفصول والمعامل", "order": 3},
    {"id": "pri_c4_s3_r04", "subcategory_id": "pri_c4_s3", "name": "تقرير متابعة استهلاك الكهرباء والماء", "order": 4},
    {"id": "pri_c4_s3_r05", "subcategory_id": "pri_c4_s3", "name": "تقرير كفاءة استخدام المستودعات والمخزون", "order": 5},
    {"id": "pri_c4_s3_r06", "subcategory_id": "pri_c4_s3", "name": "تقرير توزيع الموارد البشرية حسب الاحتياج", "order": 6},
    {"id": "pri_c4_s3_r07", "subcategory_id": "pri_c4_s3", "name": "تقرير إعادة توزيع المعلمين بعد النقل", "order": 7},
    {"id": "pri_c4_s3_r08", "subcategory_id": "pri_c4_s3", "name": "تقرير استغلال التقنية في ترشيد الموارد", "order": 8},
    {"id": "pri_c4_s3_r09", "subcategory_id": "pri_c4_s3", "name": "تقرير مراجعة كفاءة استخدام الموارد", "order": 9},
    {"id": "pri_c4_s3_r10", "subcategory_id": "pri_c4_s3", "name": "تقرير مقترحات تحسين كفاءة الموارد", "order": 10},

    # pri_c4_s4 - الإشراف على الصرف المالي وفق الأنظمة
    {"id": "pri_c4_s4_r01", "subcategory_id": "pri_c4_s4", "name": "تقرير تنفيذ الميزانية التشغيلية", "order": 1},
    {"id": "pri_c4_s4_r02", "subcategory_id": "pri_c4_s4", "name": "تقرير صرف المكافآت والحوافز", "order": 2},
    {"id": "pri_c4_s4_r03", "subcategory_id": "pri_c4_s4", "name": "تقرير مشتريات المدرسة من الأجهزة", "order": 3},
    {"id": "pri_c4_s4_r04", "subcategory_id": "pri_c4_s4", "name": "تقرير الصرف على الصيانة والنظافة", "order": 4},
    {"id": "pri_c4_s4_r05", "subcategory_id": "pri_c4_s4", "name": "تقرير مراجعة الفواتير والعقود", "order": 5},
    {"id": "pri_c4_s4_r06", "subcategory_id": "pri_c4_s4", "name": "تقرير التزام الصرف باللوائح المالية", "order": 6},
    {"id": "pri_c4_s4_r07", "subcategory_id": "pri_c4_s4", "name": "تقرير الصرف على الأنشطة والبرامج", "order": 7},
    {"id": "pri_c4_s4_r08", "subcategory_id": "pri_c4_s4", "name": "تقرير تدقيق الحسابات الداخلي", "order": 8},
    {"id": "pri_c4_s4_r09", "subcategory_id": "pri_c4_s4", "name": "تقرير الشفافية في الصرف", "order": 9},
    {"id": "pri_c4_s4_r10", "subcategory_id": "pri_c4_s4", "name": "تقرير متابعة الصرف مع نهاية العام", "order": 10},

    # pri_c4_s5 - تعظيم الاستفادة من الإمكانات المتاحة
    {"id": "pri_c4_s5_r01", "subcategory_id": "pri_c4_s5", "name": "تقرير استخدام المرافق بعد الدوام للمجتمع", "order": 1},
    {"id": "pri_c4_s5_r02", "subcategory_id": "pri_c4_s5", "name": "تقرير استثمار خبرات المعلمين في التدريب", "order": 2},
    {"id": "pri_c4_s5_r03", "subcategory_id": "pri_c4_s5", "name": "تقرير مشاركة الموارد بين المدارس", "order": 3},
    {"id": "pri_c4_s5_r04", "subcategory_id": "pri_c4_s5", "name": "تقرير إعادة تدوير المواد المستهلكة", "order": 4},
    {"id": "pri_c4_s5_r05", "subcategory_id": "pri_c4_s5", "name": "تقرير استغلال المساحات الفارغة", "order": 5},
    {"id": "pri_c4_s5_r06", "subcategory_id": "pri_c4_s5", "name": "تقرير تحويل المخلفات إلى موارد", "order": 6},
    {"id": "pri_c4_s5_r07", "subcategory_id": "pri_c4_s5", "name": "تقرير استخدام التقنية لتعظيم الموارد", "order": 7},
    {"id": "pri_c4_s5_r08", "subcategory_id": "pri_c4_s5", "name": "تقرير شراكات لتوفير موارد إضافية", "order": 8},
    {"id": "pri_c4_s5_r09", "subcategory_id": "pri_c4_s5", "name": "تقرير أفكار إبداعية لتعظيم الإمكانات", "order": 9},
    {"id": "pri_c4_s5_r10", "subcategory_id": "pri_c4_s5", "name": "تقرير قياس العائد من الاستفادة القصوى", "order": 10},

    # pri_c5_s1 - إعداد خطة تطوير مهني مبنية على احتياجات المدرسة
    {"id": "pri_c5_s1_r01", "subcategory_id": "pri_c5_s1", "name": "تقرير تحليل الاحتياجات التدريبية للمعلمين", "order": 1},
    {"id": "pri_c5_s1_r02", "subcategory_id": "pri_c5_s1", "name": "تقرير خطة التطوير المهني السنوية", "order": 2},
    {"id": "pri_c5_s1_r03", "subcategory_id": "pri_c5_s1", "name": "تقرير تحديد الأولويات التدريبية حسب التخصصات", "order": 3},
    {"id": "pri_c5_s1_r04", "subcategory_id": "pri_c5_s1", "name": "تقرير ربط الخطة برؤية المدرسة", "order": 4},
    {"id": "pri_c5_s1_r05", "subcategory_id": "pri_c5_s1", "name": "تقرير مشاركة المعلمين في اقتراح البرامج", "order": 5},
    {"id": "pri_c5_s1_r06", "subcategory_id": "pri_c5_s1", "name": "تقرير مراجعة الخطة مع المشرفين", "order": 6},
    {"id": "pri_c5_s1_r07", "subcategory_id": "pri_c5_s1", "name": "تقرير تضمين الخطة للبرامج الإلزامية", "order": 7},
    {"id": "pri_c5_s1_r08", "subcategory_id": "pri_c5_s1", "name": "تقرير مواءمة الخطة مع المستجدات", "order": 8},
    {"id": "pri_c5_s1_r09", "subcategory_id": "pri_c5_s1", "name": "تقرير تخصيص ميزانية للخطة", "order": 9},
    {"id": "pri_c5_s1_r10", "subcategory_id": "pri_c5_s1", "name": "تقرير إعلان الخطة للمعلمين", "order": 10},

    # pri_c5_s2 - حصر الاحتياجات التدريبية لمنسوبي المدرسة
    {"id": "pri_c5_s2_r01", "subcategory_id": "pri_c5_s2", "name": "تقرير استبانة الاحتياجات التدريبية", "order": 1},
    {"id": "pri_c5_s2_r02", "subcategory_id": "pri_c5_s2", "name": "تقرير تحليل نتائج تقييم الأداء لتحديد الاحتياجات", "order": 2},
    {"id": "pri_c5_s2_r03", "subcategory_id": "pri_c5_s2", "name": "تقرير مقابلات شخصية لتحديد الاحتياجات", "order": 3},
    {"id": "pri_c5_s2_r04", "subcategory_id": "pri_c5_s2", "name": "تقرير الاحتياجات التدريبية للإداريين", "order": 4},
    {"id": "pri_c5_s2_r05", "subcategory_id": "pri_c5_s2", "name": "تقرير أولويات التدريب للمعلمين الجدد", "order": 5},
    {"id": "pri_c5_s2_r06", "subcategory_id": "pri_c5_s2", "name": "تقرير الاحتياجات في ضوء التوجهات الحديثة", "order": 6},
    {"id": "pri_c5_s2_r07", "subcategory_id": "pri_c5_s2", "name": "تقرير تحديث قاعدة بيانات الاحتياجات", "order": 7},
    {"id": "pri_c5_s2_r08", "subcategory_id": "pri_c5_s2", "name": "تقرير الاحتياجات الخاصة بكل مرحلة", "order": 8},
    {"id": "pri_c5_s2_r09", "subcategory_id": "pri_c5_s2", "name": "تقرير تحليل الفجوات المهنية", "order": 9},
    {"id": "pri_c5_s2_r10", "subcategory_id": "pri_c5_s2", "name": "تقرير مصفوفة الاحتياجات التدريبية", "order": 10},

    # pri_c5_s3 - متابعة تنفيذ البرامج التدريبية
    {"id": "pri_c5_s3_r01", "subcategory_id": "pri_c5_s3", "name": "تقرير سجل حضور البرامج التدريبية", "order": 1},
    {"id": "pri_c5_s3_r02", "subcategory_id": "pri_c5_s3", "name": "تقرير تقييم المدربين والبرامج", "order": 2},
    {"id": "pri_c5_s3_r03", "subcategory_id": "pri_c5_s3", "name": "تقرير متابعة تطبيق ما تم التدريب عليه", "order": 3},
    {"id": "pri_c5_s3_r04", "subcategory_id": "pri_c5_s3", "name": "تقرير إنجاز الخطة التدريبية", "order": 4},
    {"id": "pri_c5_s3_r05", "subcategory_id": "pri_c5_s3", "name": "تقرير أثر التدريب على الممارسات الصفية", "order": 5},
    {"id": "pri_c5_s3_r06", "subcategory_id": "pri_c5_s3", "name": "تقرير تحديات تنفيذ البرامج", "order": 6},
    {"id": "pri_c5_s3_r07", "subcategory_id": "pri_c5_s3", "name": "تقرير استكمال البرامج للمعلمين", "order": 7},
    {"id": "pri_c5_s3_r08", "subcategory_id": "pri_c5_s3", "name": "تقرير إعادة جدولة البرامج المتعثرة", "order": 8},
    {"id": "pri_c5_s3_r09", "subcategory_id": "pri_c5_s3", "name": "تقرير التنسيق مع مقدمي التدريب", "order": 9},
    {"id": "pri_c5_s3_r10", "subcategory_id": "pri_c5_s3", "name": "تقرير مؤشرات نجاح التدريب", "order": 10},

    # pri_c5_s4 - تشجيع الحصول على الرخص المهنية
    {"id": "pri_c5_s4_r01", "subcategory_id": "pri_c5_s4", "name": "تقرير حملة توعية بأهمية الرخص المهنية", "order": 1},
    {"id": "pri_c5_s4_r02", "subcategory_id": "pri_c5_s4", "name": "تقرير عدد المعلمين الحاصلين على الرخص", "order": 2},
    {"id": "pri_c5_s4_r03", "subcategory_id": "pri_c5_s4", "name": "تقرير دعم المدرسة لاجتياز الاختبارات", "order": 3},
    {"id": "pri_c5_s4_r04", "subcategory_id": "pri_c5_s4", "name": "تقرير ورش تحضيرية للرخص المهنية", "order": 4},
    {"id": "pri_c5_s4_r05", "subcategory_id": "pri_c5_s4", "name": "تقرير حوافز للحصول على الرخص", "order": 5},
    {"id": "pri_c5_s4_r06", "subcategory_id": "pri_c5_s4", "name": "تقرير إتاحة مصادر التحضير للرخص", "order": 6},
    {"id": "pri_c5_s4_r07", "subcategory_id": "pri_c5_s4", "name": "تقرير متابعة تجديد الرخص", "order": 7},
    {"id": "pri_c5_s4_r08", "subcategory_id": "pri_c5_s4", "name": "تقرير ربط الرخص بالترقيات", "order": 8},
    {"id": "pri_c5_s4_r09", "subcategory_id": "pri_c5_s4", "name": "تقرير قصص نجاح في الحصول على الرخص", "order": 9},
    {"id": "pri_c5_s4_r10", "subcategory_id": "pri_c5_s4", "name": "تقرير تأثير الرخص على الأداء", "order": 10},

    # pri_c5_s5 - دعم نقل الخبرات بين المعلمين
    {"id": "pri_c5_s5_r01", "subcategory_id": "pri_c5_s5", "name": "تقرير برنامج التوجيه والإرشاد للمعلمين الجدد", "order": 1},
    {"id": "pri_c5_s5_r02", "subcategory_id": "pri_c5_s5", "name": "تقرير لقاءات تبادل الخبرات بين الأقسام", "order": 2},
    {"id": "pri_c5_s5_r03", "subcategory_id": "pri_c5_s5", "name": "تقرير دروس تطبيقية يقدمها معلمون متميزون", "order": 3},
    {"id": "pri_c5_s5_r04", "subcategory_id": "pri_c5_s5", "name": "تقرير منصة إلكترونية لمشاركة التجارب", "order": 4},
    {"id": "pri_c5_s5_r05", "subcategory_id": "pri_c5_s5", "name": "تقرير مجتمعات التعلم المهنية", "order": 5},
    {"id": "pri_c5_s5_r06", "subcategory_id": "pri_c5_s5", "name": "تقرير زيارات تبادلية بين المعلمين", "order": 6},
    {"id": "pri_c5_s5_r07", "subcategory_id": "pri_c5_s5", "name": "تقرير ورش عمل يقدمها المعلمون", "order": 7},
    {"id": "pri_c5_s5_r08", "subcategory_id": "pri_c5_s5", "name": "تقرير توثيق ونشر تجارب ناجحة", "order": 8},
    {"id": "pri_c5_s5_r09", "subcategory_id": "pri_c5_s5", "name": "تقرير حلقات النقاش بعد الزيارات الصفية", "order": 9},
    {"id": "pri_c5_s5_r10", "subcategory_id": "pri_c5_s5", "name": "تقرير قياس أثر نقل الخبرات", "order": 10},

    # pri_c6_s1 - إعداد وتنفيذ خطط تحسين مدرسية
    {"id": "pri_c6_s1_r01", "subcategory_id": "pri_c6_s1", "name": "تقرير خطة تحسين الأداء المدرسي السنوية", "order": 1},
    {"id": "pri_c6_s1_r02", "subcategory_id": "pri_c6_s1", "name": "تقرير تشخيص الواقع الراهن للمدرسة", "order": 2},
    {"id": "pri_c6_s1_r03", "subcategory_id": "pri_c6_s1", "name": "تقرير تحديد مجالات التحسين ذات الأولوية", "order": 3},
    {"id": "pri_c6_s1_r04", "subcategory_id": "pri_c6_s1", "name": "تقرير إشراك المعلمين في بناء الخطة", "order": 4},
    {"id": "pri_c6_s1_r05", "subcategory_id": "pri_c6_s1", "name": "تقرير تنفيذ أنشطة الخطة التحسينية", "order": 5},
    {"id": "pri_c6_s1_r06", "subcategory_id": "pri_c6_s1", "name": "تقرير متابعة تقدم الخطة", "order": 6},
    {"id": "pri_c6_s1_r07", "subcategory_id": "pri_c6_s1", "name": "تقرير تحديث الخطة حسب المستجدات", "order": 7},
    {"id": "pri_c6_s1_r08", "subcategory_id": "pri_c6_s1", "name": "تقرير تقييم نتائج الخطة", "order": 8},
    {"id": "pri_c6_s1_r09", "subcategory_id": "pri_c6_s1", "name": "تقرير استدامة التحسين", "order": 9},
    {"id": "pri_c6_s1_r10", "subcategory_id": "pri_c6_s1", "name": "تقرير توثيق إنجازات الخطة التحسينية", "order": 10},

    # pri_c6_s2 - بناء خطط علاجية لمعالجة جوانب الضعف
    {"id": "pri_c6_s2_r01", "subcategory_id": "pri_c6_s2", "name": "تقرير خطة علاجية لضعف القراءة والكتابة", "order": 1},
    {"id": "pri_c6_s2_r02", "subcategory_id": "pri_c6_s2", "name": "تقرير خطة علاجية للطلاب المتعثرين في الرياضيات", "order": 2},
    {"id": "pri_c6_s2_r03", "subcategory_id": "pri_c6_s2", "name": "تقرير برامج التقوية بعد الدوام", "order": 3},
    {"id": "pri_c6_s2_r04", "subcategory_id": "pri_c6_s2", "name": "تقرير تحديد الطلاب المستهدفين للخطة", "order": 4},
    {"id": "pri_c6_s2_r05", "subcategory_id": "pri_c6_s2", "name": "تقرير متابعة تقدم الطلاب في الخطة العلاجية", "order": 5},
    {"id": "pri_c6_s2_r06", "subcategory_id": "pri_c6_s2", "name": "تقرير تقييم فعالية الخطة العلاجية", "order": 6},
    {"id": "pri_c6_s2_r07", "subcategory_id": "pri_c6_s2", "name": "تقرير دمج أولياء الأمور في الخطة", "order": 7},
    {"id": "pri_c6_s2_r08", "subcategory_id": "pri_c6_s2", "name": "تقرير تحسين الخطة بناءً على النتائج", "order": 8},
    {"id": "pri_c6_s2_r09", "subcategory_id": "pri_c6_s2", "name": "تقرير قصص نجاح في العلاج", "order": 9},
    {"id": "pri_c6_s2_r10", "subcategory_id": "pri_c6_s2", "name": "تقرير استمرارية الدعم بعد العلاج", "order": 10},

    # pri_c6_s3 - متابعة مؤشرات الأداء المدرسي بانتظام
    {"id": "pri_c6_s3_r01", "subcategory_id": "pri_c6_s3", "name": "تقرير مؤشرات نسبة النجاح في المواد", "order": 1},
    {"id": "pri_c6_s3_r02", "subcategory_id": "pri_c6_s3", "name": "تقرير مؤشرات الغياب اليومي", "order": 2},
    {"id": "pri_c6_s3_r03", "subcategory_id": "pri_c6_s3", "name": "تقرير مؤشرات السلوك (المخالفات)", "order": 3},
    {"id": "pri_c6_s3_r04", "subcategory_id": "pri_c6_s3", "name": "تقرير مؤشرات أداء المعلمين", "order": 4},
    {"id": "pri_c6_s3_r05", "subcategory_id": "pri_c6_s3", "name": "تقرير مؤشرات رضا المستفيدين", "order": 5},
    {"id": "pri_c6_s3_r06", "subcategory_id": "pri_c6_s3", "name": "تقرير تحليل المؤشرات شهرياً", "order": 6},
    {"id": "pri_c6_s3_r07", "subcategory_id": "pri_c6_s3", "name": "تقرير مقارنة المؤشرات بالسنوات السابقة", "order": 7},
    {"id": "pri_c6_s3_r08", "subcategory_id": "pri_c6_s3", "name": "تقرير عرض المؤشرات على فريق القيادة", "order": 8},
    {"id": "pri_c6_s3_r09", "subcategory_id": "pri_c6_s3", "name": "تقرير استخدام المؤشرات لاتخاذ القرارات", "order": 9},
    {"id": "pri_c6_s3_r10", "subcategory_id": "pri_c6_s3", "name": "تقرير تطوير المؤشرات لتشمل جوانب جديدة", "order": 10},

    # pri_c6_s4 - دعم تطوير أداء المعلمين
    {"id": "pri_c6_s4_r01", "subcategory_id": "pri_c6_s4", "name": "تقرير برامج التنمية المهنية المستمرة", "order": 1},
    {"id": "pri_c6_s4_r02", "subcategory_id": "pri_c6_s4", "name": "تقرير الزيارات الصفية والتغذية الراجعة", "order": 2},
    {"id": "pri_c6_s4_r03", "subcategory_id": "pri_c6_s4", "name": "تقرير توفير مصادر تعلم للمعلمين", "order": 3},
    {"id": "pri_c6_s4_r04", "subcategory_id": "pri_c6_s4", "name": "تقرير تحفيز المعلمين للتميز", "order": 4},
    {"id": "pri_c6_s4_r05", "subcategory_id": "pri_c6_s4", "name": "تقرير إشراك المعلمين في مجتمعات تعلم", "order": 5},
    {"id": "pri_c6_s4_r06", "subcategory_id": "pri_c6_s4", "name": "تقرير متابعة خطط التطوير الذاتي للمعلمين", "order": 6},
    {"id": "pri_c6_s4_r07", "subcategory_id": "pri_c6_s4", "name": "تقرير تكريم المعلمين المتميزين", "order": 7},
    {"id": "pri_c6_s4_r08", "subcategory_id": "pri_c6_s4", "name": "تقرير دعم المعلمين في البحث الإجرائي", "order": 8},
    {"id": "pri_c6_s4_r09", "subcategory_id": "pri_c6_s4", "name": "تقرير برامج الإرشاد المهني للمعلمين", "order": 9},
    {"id": "pri_c6_s4_r10", "subcategory_id": "pri_c6_s4", "name": "تقرير قياس أثر الدعم على أداء المعلمين", "order": 10},

    # pri_c6_s5 - تعزيز الشراكة مع المجتمع المدرسي
    {"id": "pri_c6_s5_r01", "subcategory_id": "pri_c6_s5", "name": "تقرير اجتماعات مجلس أولياء الأمور", "order": 1},
    {"id": "pri_c6_s5_r02", "subcategory_id": "pri_c6_s5", "name": "تقرير مشاركة أولياء الأمور في الأنشطة", "order": 2},
    {"id": "pri_c6_s5_r03", "subcategory_id": "pri_c6_s5", "name": "تقرير برامج توعوية للأسر", "order": 3},
    {"id": "pri_c6_s5_r04", "subcategory_id": "pri_c6_s5", "name": "تقرير استطلاعات رأي أولياء الأمور", "order": 4},
    {"id": "pri_c6_s5_r05", "subcategory_id": "pri_c6_s5", "name": "تقرير تفعيل التواصل عبر المنصات", "order": 5},
    {"id": "pri_c6_s5_r06", "subcategory_id": "pri_c6_s5", "name": "تقرير مشاركة المجتمع المحلي في الدعم", "order": 6},
    {"id": "pri_c6_s5_r07", "subcategory_id": "pri_c6_s5", "name": "تقرير شراكات مع مؤسسات مجتمعية", "order": 7},
    {"id": "pri_c6_s5_r08", "subcategory_id": "pri_c6_s5", "name": "تقرير فعاليات مفتوحة للمجتمع", "order": 8},
    {"id": "pri_c6_s5_r09", "subcategory_id": "pri_c6_s5", "name": "تقرير تطوير آليات الشراكة", "order": 9},
    {"id": "pri_c6_s5_r10", "subcategory_id": "pri_c6_s5", "name": "تقرير أثر الشراكة على تحسين المدرسة", "order": 10},

    # pri_c7_s1 - إعداد الخطة التشغيلية وفق تحليل واقع المدرسة
    {"id": "pri_c7_s1_r01", "subcategory_id": "pri_c7_s1", "name": "تقرير تحليل SWOT للمدرسة", "order": 1},
    {"id": "pri_c7_s1_r02", "subcategory_id": "pri_c7_s1", "name": "تقرير تحديد الأهداف التشغيلية السنوية", "order": 2},
    {"id": "pri_c7_s1_r03", "subcategory_id": "pri_c7_s1", "name": "تقرير مواءمة الخطة مع الاستراتيجية العامة", "order": 3},
    {"id": "pri_c7_s1_r04", "subcategory_id": "pri_c7_s1", "name": "تقرير مشاركة الأقسام في بناء الخطة", "order": 4},
    {"id": "pri_c7_s1_r05", "subcategory_id": "pri_c7_s1", "name": "تقرير اعتماد الخطة من مكتب التعليم", "order": 5},
    {"id": "pri_c7_s1_r06", "subcategory_id": "pri_c7_s1", "name": "تقرير توزيع مسؤوليات تنفيذ الخطة", "order": 6},
    {"id": "pri_c7_s1_r07", "subcategory_id": "pri_c7_s1", "name": "تقرير مؤشرات قياس الخطة", "order": 7},
    {"id": "pri_c7_s1_r08", "subcategory_id": "pri_c7_s1", "name": "تقرير مراجعة الخطة مع بداية العام", "order": 8},
    {"id": "pri_c7_s1_r09", "subcategory_id": "pri_c7_s1", "name": "تقرير تحديث الخطة بناءً على تحليل واقع", "order": 9},
    {"id": "pri_c7_s1_r10", "subcategory_id": "pri_c7_s1", "name": "تقرير تقييم جودة الخطة التشغيلية", "order": 10},

    # pri_c7_s2 - وضع خطط بديلة للطوارئ
    {"id": "pri_c7_s2_r01", "subcategory_id": "pri_c7_s2", "name": "تقرير خطة الطوارئ للكوارث الطبيعية", "order": 1},
    {"id": "pri_c7_s2_r02", "subcategory_id": "pri_c7_s2", "name": "تقرير خطة استمرارية التعليم عند تعليق الدراسة", "order": 2},
    {"id": "pri_c7_s2_r03", "subcategory_id": "pri_c7_s2", "name": "تقرير خطة بديلة لنقص المعلمين", "order": 3},
    {"id": "pri_c7_s2_r04", "subcategory_id": "pri_c7_s2", "name": "تقرير خطة إخلاء المدرسة", "order": 4},
    {"id": "pri_c7_s2_r05", "subcategory_id": "pri_c7_s2", "name": "تقرير خطة التعامل مع انقطاع الخدمات", "order": 5},
    {"id": "pri_c7_s2_r06", "subcategory_id": "pri_c7_s2", "name": "تقرير تدريب العاملين على الخطط البديلة", "order": 6},
    {"id": "pri_c7_s2_r07", "subcategory_id": "pri_c7_s2", "name": "تقرير مراجعة خطط الطوارئ دورياً", "order": 7},
    {"id": "pri_c7_s2_r08", "subcategory_id": "pri_c7_s2", "name": "تقرير محاكاة لخطط الطوارئ", "order": 8},
    {"id": "pri_c7_s2_r09", "subcategory_id": "pri_c7_s2", "name": "تقرير تقييم جاهزية الخطط البديلة", "order": 9},
    {"id": "pri_c7_s2_r10", "subcategory_id": "pri_c7_s2", "name": "تقرير تحديث الخطط بناءً على المخاطر المستجدة", "order": 10},

    # pri_c7_s3 - إعداد خطط الزيارات والإشراف
    {"id": "pri_c7_s3_r01", "subcategory_id": "pri_c7_s3", "name": "تقرير خطة الزيارات الصفية لقادة الأقسام", "order": 1},
    {"id": "pri_c7_s3_r02", "subcategory_id": "pri_c7_s3", "name": "تقرير جدولة زيارات المشرفين الخارجيين", "order": 2},
    {"id": "pri_c7_s3_r03", "subcategory_id": "pri_c7_s3", "name": "تقرير خطة الإشراف اليومي على الدوام", "order": 3},
    {"id": "pri_c7_s3_r04", "subcategory_id": "pri_c7_s3", "name": "تقرير توزيع الزيارات بين الوكلاء", "order": 4},
    {"id": "pri_c7_s3_r05", "subcategory_id": "pri_c7_s3", "name": "تقرير تغطية الزيارات لجميع المعلمين", "order": 5},
    {"id": "pri_c7_s3_r06", "subcategory_id": "pri_c7_s3", "name": "تقرير متابعة تنفيذ خطة الزيارات", "order": 6},
    {"id": "pri_c7_s3_r07", "subcategory_id": "pri_c7_s3", "name": "تقرير توثيق نتائج الزيارات", "order": 7},
    {"id": "pri_c7_s3_r08", "subcategory_id": "pri_c7_s3", "name": "تقرير تحليل نتائج الزيارات لتحسين الأداء", "order": 8},
    {"id": "pri_c7_s3_r09", "subcategory_id": "pri_c7_s3", "name": "تقرير مراجعة خطة الزيارات مع الخبرات", "order": 9},
    {"id": "pri_c7_s3_r10", "subcategory_id": "pri_c7_s3", "name": "تقرير تقييم فاعلية خطة الزيارات", "order": 10},

    # pri_c7_s4 - إعداد خطط الأمن والسلامة وإدارة المخاطر
    {"id": "pri_c7_s4_r01", "subcategory_id": "pri_c7_s4", "name": "تقرير خطة الأمن والسلامة المدرسية", "order": 1},
    {"id": "pri_c7_s4_r02", "subcategory_id": "pri_c7_s4", "name": "تقرير خطة إدارة المخاطر", "order": 2},
    {"id": "pri_c7_s4_r03", "subcategory_id": "pri_c7_s4", "name": "تقرير تحديد مخاطر المدرسة", "order": 3},
    {"id": "pri_c7_s4_r04", "subcategory_id": "pri_c7_s4", "name": "تقرير تجهيزات السلامة (طفايات، إنذار)", "order": 4},
    {"id": "pri_c7_s4_r05", "subcategory_id": "pri_c7_s4", "name": "تقرير تدريبات الإخلاء", "order": 5},
    {"id": "pri_c7_s4_r06", "subcategory_id": "pri_c7_s4", "name": "تقرير توعية الطلاب بالسلامة", "order": 6},
    {"id": "pri_c7_s4_r07", "subcategory_id": "pri_c7_s4", "name": "تقرير الصيانة الوقائية للمباني", "order": 7},
    {"id": "pri_c7_s4_r08", "subcategory_id": "pri_c7_s4", "name": "تقرير متابعة تنفيذ خطة الأمن", "order": 8},
    {"id": "pri_c7_s4_r09", "subcategory_id": "pri_c7_s4", "name": "تقرير تقييم خطة السلامة", "order": 9},
    {"id": "pri_c7_s4_r10", "subcategory_id": "pri_c7_s4", "name": "تقرير تحديث خطة إدارة المخاطر", "order": 10},

    # pri_c7_s5 - إعداد خطة النموذج الإشرافي
    {"id": "pri_c7_s5_r01", "subcategory_id": "pri_c7_s5", "name": "تقرير خطة تطبيق النموذج الإشرافي", "order": 1},
    {"id": "pri_c7_s5_r02", "subcategory_id": "pri_c7_s5", "name": "تقرير توزيع الأدوار الإشرافية", "order": 2},
    {"id": "pri_c7_s5_r03", "subcategory_id": "pri_c7_s5", "name": "تقرير برامج التطوير المهني للإشراف", "order": 3},
    {"id": "pri_c7_s5_r04", "subcategory_id": "pri_c7_s5", "name": "تقرير متابعة تنفيذ النموذج الإشرافي", "order": 4},
    {"id": "pri_c7_s5_r05", "subcategory_id": "pri_c7_s5", "name": "تقرير أدوات الإشراف المستخدمة", "order": 5},
    {"id": "pri_c7_s5_r06", "subcategory_id": "pri_c7_s5", "name": "تقرير تدريب المشرفين على النموذج", "order": 6},
    {"id": "pri_c7_s5_r07", "subcategory_id": "pri_c7_s5", "name": "تقرير تقييم فعالية النموذج الإشرافي", "order": 7},
    {"id": "pri_c7_s5_r08", "subcategory_id": "pri_c7_s5", "name": "تقرير تحسين النموذج بناءً على التغذية", "order": 8},
    {"id": "pri_c7_s5_r09", "subcategory_id": "pri_c7_s5", "name": "تقرير توثيق ممارسات النموذج", "order": 9},
    {"id": "pri_c7_s5_r10", "subcategory_id": "pri_c7_s5", "name": "تقرير قياس أثر النموذج على أداء المعلمين", "order": 10},

    # pri_c8_s1 - متابعة تنفيذ الخطة التشغيلية والتحسينية
    {"id": "pri_c8_s1_r01", "subcategory_id": "pri_c8_s1", "name": "تقرير متابعة تنفيذ الخطة التشغيلية شهرياً", "order": 1},
    {"id": "pri_c8_s1_r02", "subcategory_id": "pri_c8_s1", "name": "تقرير إنجاز مؤشرات الخطة التحسينية", "order": 2},
    {"id": "pri_c8_s1_r03", "subcategory_id": "pri_c8_s1", "name": "تقرير تحديات تنفيذ الخطة", "order": 3},
    {"id": "pri_c8_s1_r04", "subcategory_id": "pri_c8_s1", "name": "تقرير اجتماعات متابعة الخطة", "order": 4},
    {"id": "pri_c8_s1_r05", "subcategory_id": "pri_c8_s1", "name": "تقرير تقارير فرق العمل عن التنفيذ", "order": 5},
    {"id": "pri_c8_s1_r06", "subcategory_id": "pri_c8_s1", "name": "تقرير تعديل الخطة بناءً على المتابعة", "order": 6},
    {"id": "pri_c8_s1_r07", "subcategory_id": "pri_c8_s1", "name": "تقرير إنجاز الخطة في نهاية الفصل", "order": 7},
    {"id": "pri_c8_s1_r08", "subcategory_id": "pri_c8_s1", "name": "تقرير أثر الخطة على الأداء", "order": 8},
    {"id": "pri_c8_s1_r09", "subcategory_id": "pri_c8_s1", "name": "تقرير استدامة نتائج الخطة", "order": 9},
    {"id": "pri_c8_s1_r10", "subcategory_id": "pri_c8_s1", "name": "تقرير توثيق إنجازات الخطة", "order": 10},

    # pri_c8_s2 - متابعة خطط الانضباط والتطوير المهني
    {"id": "pri_c8_s2_r01", "subcategory_id": "pri_c8_s2", "name": "تقرير متابعة تنفيذ خطة الانضباط", "order": 1},
    {"id": "pri_c8_s2_r02", "subcategory_id": "pri_c8_s2", "name": "تقرير مؤشرات الانضباط أثناء التنفيذ", "order": 2},
    {"id": "pri_c8_s2_r03", "subcategory_id": "pri_c8_s2", "name": "تقرير متابعة خطة التطوير المهني", "order": 3},
    {"id": "pri_c8_s2_r04", "subcategory_id": "pri_c8_s2", "name": "تقرير حضور البرامج التدريبية", "order": 4},
    {"id": "pri_c8_s2_r05", "subcategory_id": "pri_c8_s2", "name": "تقرير تطبيق المعلمين لما تعلموه", "order": 5},
    {"id": "pri_c8_s2_r06", "subcategory_id": "pri_c8_s2", "name": "تقرير تعديل الخطط حسب الاحتياج", "order": 6},
    {"id": "pri_c8_s2_r07", "subcategory_id": "pri_c8_s2", "name": "تقرير تقييم أثر خطط الانضباط", "order": 7},
    {"id": "pri_c8_s2_r08", "subcategory_id": "pri_c8_s2", "name": "تقرير تقييم أثر التطوير المهني", "order": 8},
    {"id": "pri_c8_s2_r09", "subcategory_id": "pri_c8_s2", "name": "تقرير استمرارية الخطط", "order": 9},
    {"id": "pri_c8_s2_r10", "subcategory_id": "pri_c8_s2", "name": "تقرير تحديث الخطط بناءً على المتابعة", "order": 10},

    # pri_c8_s3 - متابعة خطط النشاط الطلابي والبرامج العلاجية
    {"id": "pri_c8_s3_r01", "subcategory_id": "pri_c8_s3", "name": "تقرير تنفيذ خطة النشاط الطلابي", "order": 1},
    {"id": "pri_c8_s3_r02", "subcategory_id": "pri_c8_s3", "name": "تقرير مشاركة الطلاب في الأنشطة", "order": 2},
    {"id": "pri_c8_s3_r03", "subcategory_id": "pri_c8_s3", "name": "تقرير متابعة البرامج العلاجية", "order": 3},
    {"id": "pri_c8_s3_r04", "subcategory_id": "pri_c8_s3", "name": "تقرير تقدم الطلاب في البرامج العلاجية", "order": 4},
    {"id": "pri_c8_s3_r05", "subcategory_id": "pri_c8_s3", "name": "تقرير تحديات تنفيذ الأنشطة", "order": 5},
    {"id": "pri_c8_s3_r06", "subcategory_id": "pri_c8_s3", "name": "تقرير تعديل خطط الأنشطة", "order": 6},
    {"id": "pri_c8_s3_r07", "subcategory_id": "pri_c8_s3", "name": "تقرير تقييم فعالية البرامج العلاجية", "order": 7},
    {"id": "pri_c8_s3_r08", "subcategory_id": "pri_c8_s3", "name": "تقرير أثر الأنشطة على التحصيل", "order": 8},
    {"id": "pri_c8_s3_r09", "subcategory_id": "pri_c8_s3", "name": "تقرير استمرارية الأنشطة", "order": 9},
    {"id": "pri_c8_s3_r10", "subcategory_id": "pri_c8_s3", "name": "تقرير توثيق إنجازات الأنشطة", "order": 10},

    # pri_c8_s4 - متابعة خطط المعلمين وتقارير التنفيذ
    {"id": "pri_c8_s4_r01", "subcategory_id": "pri_c8_s4", "name": "تقرير متابعة خطط المعلمين الفصلية", "order": 1},
    {"id": "pri_c8_s4_r02", "subcategory_id": "pri_c8_s4", "name": "تقرير تقارير تنفيذ المنهج", "order": 2},
    {"id": "pri_c8_s4_r03", "subcategory_id": "pri_c8_s4", "name": "تقرير متابعة خطط الأنشطة الصفية", "order": 3},
    {"id": "pri_c8_s4_r04", "subcategory_id": "pri_c8_s4", "name": "تقرير تحليل تقارير المعلمين", "order": 4},
    {"id": "pri_c8_s4_r05", "subcategory_id": "pri_c8_s4", "name": "تقرير متابعة تنفيذ خطط التقويم", "order": 5},
    {"id": "pri_c8_s4_r06", "subcategory_id": "pri_c8_s4", "name": "تقرير التغذية الراجعة للمعلمين", "order": 6},
    {"id": "pri_c8_s4_r07", "subcategory_id": "pri_c8_s4", "name": "تقرير تحديث الخطط بناءً على التقارير", "order": 7},
    {"id": "pri_c8_s4_r08", "subcategory_id": "pri_c8_s4", "name": "تقرير تقييم جودة خطط المعلمين", "order": 8},
    {"id": "pri_c8_s4_r09", "subcategory_id": "pri_c8_s4", "name": "تقرير أثر خطط المعلمين على الطلاب", "order": 9},
    {"id": "pri_c8_s4_r10", "subcategory_id": "pri_c8_s4", "name": "تقرير توثيق أفضل خطط المعلمين", "order": 10},

    # pri_c8_s5 - تقييم أثر الخطط والمشروعات المنفذة
    {"id": "pri_c8_s5_r01", "subcategory_id": "pri_c8_s5", "name": "تقرير تقييم أثر الخطة التشغيلية", "order": 1},
    {"id": "pri_c8_s5_r02", "subcategory_id": "pri_c8_s5", "name": "تقرير قياس نتائج المشروعات التطويرية", "order": 2},
    {"id": "pri_c8_s5_r03", "subcategory_id": "pri_c8_s5", "name": "تقرير تحليل العائد من الخطط", "order": 3},
    {"id": "pri_c8_s5_r04", "subcategory_id": "pri_c8_s5", "name": "تقرير استبيانات قياس الأثر", "order": 4},
    {"id": "pri_c8_s5_r05", "subcategory_id": "pri_c8_s5", "name": "تقرير مقارنة قبل وبعد تنفيذ الخطط", "order": 5},
    {"id": "pri_c8_s5_r06", "subcategory_id": "pri_c8_s5", "name": "تقرير استدامة أثر الخطط", "order": 6},
    {"id": "pri_c8_s5_r07", "subcategory_id": "pri_c8_s5", "name": "تقرير تحديات قياس الأثر", "order": 7},
    {"id": "pri_c8_s5_r08", "subcategory_id": "pri_c8_s5", "name": "تقرير توصيات لتحسين الأثر", "order": 8},
    {"id": "pri_c8_s5_r09", "subcategory_id": "pri_c8_s5", "name": "تقرير توثيق قصص نجاح الأثر", "order": 9},
    {"id": "pri_c8_s5_r10", "subcategory_id": "pri_c8_s5", "name": "تقرير عرض نتائج التقييم على القيادة", "order": 10},

    # pri_c9_s1 - توفير بيئة داعمة للأنشطة الصفية واللاصفية
    {"id": "pri_c9_s1_r01", "subcategory_id": "pri_c9_s1", "name": "تقرير تجهيز الفصول للأنشطة الصفية", "order": 1},
    {"id": "pri_c9_s1_r02", "subcategory_id": "pri_c9_s1", "name": "تقرير تخصيص أماكن للأنشطة اللاصفية", "order": 2},
    {"id": "pri_c9_s1_r03", "subcategory_id": "pri_c9_s1", "name": "تقرير توفير المواد والوسائل للأنشطة", "order": 3},
    {"id": "pri_c9_s1_r04", "subcategory_id": "pri_c9_s1", "name": "تقرير مرونة الجدول لإتاحة الأنشطة", "order": 4},
    {"id": "pri_c9_s1_r05", "subcategory_id": "pri_c9_s1", "name": "تقرير تشجيع المعلمين على الأنشطة", "order": 5},
    {"id": "pri_c9_s1_r06", "subcategory_id": "pri_c9_s1", "name": "تقرير توفير فرق داعمة للأنشطة", "order": 6},
    {"id": "pri_c9_s1_r07", "subcategory_id": "pri_c9_s1", "name": "تقرير تحسين ساحة الأنشطة", "order": 7},
    {"id": "pri_c9_s1_r08", "subcategory_id": "pri_c9_s1", "name": "تقرير توفير أدوات السلامة في الأنشطة", "order": 8},
    {"id": "pri_c9_s1_r09", "subcategory_id": "pri_c9_s1", "name": "تقرير استطلاع احتياجات الأنشطة", "order": 9},
    {"id": "pri_c9_s1_r10", "subcategory_id": "pri_c9_s1", "name": "تقرير قياس رضا الطلاب عن بيئة الأنشطة", "order": 10},

    # pri_c9_s2 - تمكين الطلاب من المشاركة في الأنشطة الداخلية والخارجية
    {"id": "pri_c9_s2_r01", "subcategory_id": "pri_c9_s2", "name": "تقرير مشاركة الطلاب في الأندية المدرسية", "order": 1},
    {"id": "pri_c9_s2_r02", "subcategory_id": "pri_c9_s2", "name": "تقرير مشاركة الفرق في المسابقات الخارجية", "order": 2},
    {"id": "pri_c9_s2_r03", "subcategory_id": "pri_c9_s2", "name": "تقرير تمكين جميع الطلاب من المشاركة", "order": 3},
    {"id": "pri_c9_s2_r04", "subcategory_id": "pri_c9_s2", "name": "تقرير رحلات مدرسية تعليمية", "order": 4},
    {"id": "pri_c9_s2_r05", "subcategory_id": "pri_c9_s2", "name": "تقرير مشاركة الطلاب في اليوم المفتوح", "order": 5},
    {"id": "pri_c9_s2_r06", "subcategory_id": "pri_c9_s2", "name": "تقرير تمكين الطلاب من قيادة الأنشطة", "order": 6},
    {"id": "pri_c9_s2_r07", "subcategory_id": "pri_c9_s2", "name": "تقرير تذليل العقبات لمشاركة ذوي الإعاقة", "order": 7},
    {"id": "pri_c9_s2_r08", "subcategory_id": "pri_c9_s2", "name": "تقرير تشجيع الطلاب الموهوبين", "order": 8},
    {"id": "pri_c9_s2_r09", "subcategory_id": "pri_c9_s2", "name": "تقرير توفير الإشراف الكافي للرحلات", "order": 9},
    {"id": "pri_c9_s2_r10", "subcategory_id": "pri_c9_s2", "name": "تقرير تقييم تجارب المشاركة الخارجية", "order": 10},

    # pri_c9_s3 - دعم المسابقات والمنافسات الطلابية
    {"id": "pri_c9_s3_r01", "subcategory_id": "pri_c9_s3", "name": "تقرير خطة المسابقات الداخلية", "order": 1},
    {"id": "pri_c9_s3_r02", "subcategory_id": "pri_c9_s3", "name": "تقرير مشاركة المدرسة في مسابقات وزارية", "order": 2},
    {"id": "pri_c9_s3_r03", "subcategory_id": "pri_c9_s3", "name": "تقرير تدريب الفرق للمسابقات", "order": 3},
    {"id": "pri_c9_s3_r04", "subcategory_id": "pri_c9_s3", "name": "تقرير توفير جوائز للفائزين", "order": 4},
    {"id": "pri_c9_s3_r05", "subcategory_id": "pri_c9_s3", "name": "تقرير تكريم الطلاب المتميزين", "order": 5},
    {"id": "pri_c9_s3_r06", "subcategory_id": "pri_c9_s3", "name": "تقرير إقامة معارض للمشروعات الفائزة", "order": 6},
    {"id": "pri_c9_s3_r07", "subcategory_id": "pri_c9_s3", "name": "تقرير تحفيز المشاركة في المسابقات", "order": 7},
    {"id": "pri_c9_s3_r08", "subcategory_id": "pri_c9_s3", "name": "تقرير متابعة نتائج المسابقات", "order": 8},
    {"id": "pri_c9_s3_r09", "subcategory_id": "pri_c9_s3", "name": "تقرير تطوير أداء الفرق", "order": 9},
    {"id": "pri_c9_s3_r10", "subcategory_id": "pri_c9_s3", "name": "تقرير أثر المسابقات على التحصيل", "order": 10},

    # pri_c9_s4 - تطوير المشاركات الطلابية ورفع مستوى التمثيل الخارجي
    {"id": "pri_c9_s4_r01", "subcategory_id": "pri_c9_s4", "name": "تقرير تطوير مهارات الطلاب للمشاركات", "order": 1},
    {"id": "pri_c9_s4_r02", "subcategory_id": "pri_c9_s4", "name": "تقرير برامج إعداد الطلاب للمسابقات الدولية", "order": 2},
    {"id": "pri_c9_s4_r03", "subcategory_id": "pri_c9_s4", "name": "تقرير تحسين مستوى التمثيل الخارجي", "order": 3},
    {"id": "pri_c9_s4_r04", "subcategory_id": "pri_c9_s4", "name": "تقرير تدريب الطلاب على مهارات القيادة", "order": 4},
    {"id": "pri_c9_s4_r05", "subcategory_id": "pri_c9_s4", "name": "تقرير مشاركات الطلاب في المحافل المحلية", "order": 5},
    {"id": "pri_c9_s4_r06", "subcategory_id": "pri_c9_s4", "name": "تقرير تحسين الصورة الذهنية للمدرسة", "order": 6},
    {"id": "pri_c9_s4_r07", "subcategory_id": "pri_c9_s4", "name": "تقرير مراجعة أداء الطلاب في التمثيل", "order": 7},
    {"id": "pri_c9_s4_r08", "subcategory_id": "pri_c9_s4", "name": "تقرير تبادل الخبرات مع مدارس أخرى", "order": 8},
    {"id": "pri_c9_s4_r09", "subcategory_id": "pri_c9_s4", "name": "تقرير توثيق المشاركات الخارجية", "order": 9},
    {"id": "pri_c9_s4_r10", "subcategory_id": "pri_c9_s4", "name": "تقرير قياس تطور مستوى المشاركات", "order": 10},

    # pri_c9_s5 - رصد الإنجازات والمراكز المحققة
    {"id": "pri_c9_s5_r01", "subcategory_id": "pri_c9_s5", "name": "تقرير سجل إنجازات الطلاب", "order": 1},
    {"id": "pri_c9_s5_r02", "subcategory_id": "pri_c9_s5", "name": "تقرير المراكز المحققة في المسابقات", "order": 2},
    {"id": "pri_c9_s5_r03", "subcategory_id": "pri_c9_s5", "name": "تقرير توثيق الإنجازات في موقع المدرسة", "order": 3},
    {"id": "pri_c9_s5_r04", "subcategory_id": "pri_c9_s5", "name": "تقرير الاحتفاء بالإنجازات", "order": 4},
    {"id": "pri_c9_s5_r05", "subcategory_id": "pri_c9_s5", "name": "تقرير تحليل الإنجازات لتحديد نقاط القوة", "order": 5},
    {"id": "pri_c9_s5_r06", "subcategory_id": "pri_c9_s5", "name": "تقرير إبلاغ المجتمع المدرسي بالإنجازات", "order": 6},
    {"id": "pri_c9_s5_r07", "subcategory_id": "pri_c9_s5", "name": "تقرير مقارنة الإنجازات بالأعوام السابقة", "order": 7},
    {"id": "pri_c9_s5_r08", "subcategory_id": "pri_c9_s5", "name": "تقرير تكريم الطلاب المتميزين", "order": 8},
    {"id": "pri_c9_s5_r09", "subcategory_id": "pri_c9_s5", "name": "تقرير استدامة الإنجازات", "order": 9},
    {"id": "pri_c9_s5_r10", "subcategory_id": "pri_c9_s5", "name": "تقرير أثر الإنجازات على تحفيز الآخرين", "order": 10},

    # pri_c10_s1 - تحليل نتائج المتعلمين وتصنيف مستوياتهم
    {"id": "pri_c10_s1_r01", "subcategory_id": "pri_c10_s1", "name": "تقرير تحليل نتائج نهاية الفصل", "order": 1},
    {"id": "pri_c10_s1_r02", "subcategory_id": "pri_c10_s1", "name": "تقرير تصنيف الطلاب حسب المستوى", "order": 2},
    {"id": "pri_c10_s1_r03", "subcategory_id": "pri_c10_s1", "name": "تقرير تحديد الطلاب المتفوقين والمتعثرين", "order": 3},
    {"id": "pri_c10_s1_r04", "subcategory_id": "pri_c10_s1", "name": "تقرير تحليل نتائج المواد المختلفة", "order": 4},
    {"id": "pri_c10_s1_r05", "subcategory_id": "pri_c10_s1", "name": "تقرير مقارنة نتائج الفصول", "order": 5},
    {"id": "pri_c10_s1_r06", "subcategory_id": "pri_c10_s1", "name": "تقرير تحليل نتائج الاختبارات الدولية", "order": 6},
    {"id": "pri_c10_s1_r07", "subcategory_id": "pri_c10_s1", "name": "تقرير استخدام أدوات تحليل البيانات", "order": 7},
    {"id": "pri_c10_s1_r08", "subcategory_id": "pri_c10_s1", "name": "تقرير تصنيف الطلاب حسب الاحتياجات", "order": 8},
    {"id": "pri_c10_s1_r09", "subcategory_id": "pri_c10_s1", "name": "تقرير تحليل تطور الطلاب عبر السنوات", "order": 9},
    {"id": "pri_c10_s1_r10", "subcategory_id": "pri_c10_s1", "name": "تقرير عرض نتائج التحليل على المعلمين", "order": 10},

    # pri_c10_s2 - تفسير النتائج لاتخاذ قرارات علاجية وإثرائية
    {"id": "pri_c10_s2_r01", "subcategory_id": "pri_c10_s2", "name": "تقرير تفسير أسباب ضعف النتائج", "order": 1},
    {"id": "pri_c10_s2_r02", "subcategory_id": "pri_c10_s2", "name": "تقرير خطط علاجية بناءً على التحليل", "order": 2},
    {"id": "pri_c10_s2_r03", "subcategory_id": "pri_c10_s2", "name": "تقرير برامج إثرائية للمتفوقين", "order": 3},
    {"id": "pri_c10_s2_r04", "subcategory_id": "pri_c10_s2", "name": "تقرير توجيه المعلمين لتعديل التدريس", "order": 4},
    {"id": "pri_c10_s2_r05", "subcategory_id": "pri_c10_s2", "name": "تقرير قرارات بشأن توزيع الطلاب", "order": 5},
    {"id": "pri_c10_s2_r06", "subcategory_id": "pri_c10_s2", "name": "تقرير توصيات لتطوير المناهج", "order": 6},
    {"id": "pri_c10_s2_r07", "subcategory_id": "pri_c10_s2", "name": "تقرير اجتماعات لمناقشة النتائج", "order": 7},
    {"id": "pri_c10_s2_r08", "subcategory_id": "pri_c10_s2", "name": "تقرير متابعة تنفيذ القرارات", "order": 8},
    {"id": "pri_c10_s2_r09", "subcategory_id": "pri_c10_s2", "name": "تقرير تقييم فاعلية القرارات", "order": 9},
    {"id": "pri_c10_s2_r10", "subcategory_id": "pri_c10_s2", "name": "تقرير توثيق القرارات المبنية على النتائج", "order": 10},

    # pri_c10_s3 - متابعة نمو التحصيل الدراسي بشكل دوري
    {"id": "pri_c10_s3_r01", "subcategory_id": "pri_c10_s3", "name": "تقرير متابعة نتائج الطلاب شهرياً", "order": 1},
    {"id": "pri_c10_s3_r02", "subcategory_id": "pri_c10_s3", "name": "تقرير تحليل تطور درجات الطلاب", "order": 2},
    {"id": "pri_c10_s3_r03", "subcategory_id": "pri_c10_s3", "name": "تقرير منحنيات التحصيل", "order": 3},
    {"id": "pri_c10_s3_r04", "subcategory_id": "pri_c10_s3", "name": "تقرير متابعة أثر البرامج على التحصيل", "order": 4},
    {"id": "pri_c10_s3_r05", "subcategory_id": "pri_c10_s3", "name": "تقرير مقارنة تحصيل الفصول", "order": 5},
    {"id": "pri_c10_s3_r06", "subcategory_id": "pri_c10_s3", "name": "تقرير تحديث مؤشرات التحصيل", "order": 6},
    {"id": "pri_c10_s3_r07", "subcategory_id": "pri_c10_s3", "name": "تقرير تقارير دورية للمعلمين", "order": 7},
    {"id": "pri_c10_s3_r08", "subcategory_id": "pri_c10_s3", "name": "تقرير اجتماعات متابعة التحصيل", "order": 8},
    {"id": "pri_c10_s3_r09", "subcategory_id": "pri_c10_s3", "name": "تقرير اكتشاف الانحرافات مبكراً", "order": 9},
    {"id": "pri_c10_s3_r10", "subcategory_id": "pri_c10_s3", "name": "تقرير قياس نمو التحصيل السنوي", "order": 10},

    # pri_c10_s4 - تطوير استراتيجيات تعليمية داعمة
    {"id": "pri_c10_s4_r01", "subcategory_id": "pri_c10_s4", "name": "تقرير تدريب المعلمين على استراتيجيات حديثة", "order": 1},
    {"id": "pri_c10_s4_r02", "subcategory_id": "pri_c10_s4", "name": "تقرير تطبيق التعلم النشط", "order": 2},
    {"id": "pri_c10_s4_r03", "subcategory_id": "pri_c10_s4", "name": "تقرير استخدام التلعيب في التعليم", "order": 3},
    {"id": "pri_c10_s4_r04", "subcategory_id": "pri_c10_s4", "name": "تقرير توظيف المشاريع في التدريس", "order": 4},
    {"id": "pri_c10_s4_r05", "subcategory_id": "pri_c10_s4", "name": "تقرير استراتيجيات التفكير الناقد", "order": 5},
    {"id": "pri_c10_s4_r06", "subcategory_id": "pri_c10_s4", "name": "تقرير متابعة تطبيق الاستراتيجيات", "order": 6},
    {"id": "pri_c10_s4_r07", "subcategory_id": "pri_c10_s4", "name": "تقرير قياس أثر الاستراتيجيات على التحصيل", "order": 7},
    {"id": "pri_c10_s4_r08", "subcategory_id": "pri_c10_s4", "name": "تقرير تبادل الخبرات في الاستراتيجيات", "order": 8},
    {"id": "pri_c10_s4_r09", "subcategory_id": "pri_c10_s4", "name": "تقرير تطوير دليل الاستراتيجيات", "order": 9},
    {"id": "pri_c10_s4_r10", "subcategory_id": "pri_c10_s4", "name": "تقرير استدامة تطبيق الاستراتيجيات", "order": 10},

    # pri_c10_s5 - التواصل مع أولياء الأمور بشأن النتائج
    {"id": "pri_c10_s5_r01", "subcategory_id": "pri_c10_s5", "name": "تقرير إشعار أولياء الأمور بالنتائج", "order": 1},
    {"id": "pri_c10_s5_r02", "subcategory_id": "pri_c10_s5", "name": "تقرير اجتماعات مع أولياء أمور المتعثرين", "order": 2},
    {"id": "pri_c10_s5_r03", "subcategory_id": "pri_c10_s5", "name": "تقرير برامج توعوية للأسر لدعم التحصيل", "order": 3},
    {"id": "pri_c10_s5_r04", "subcategory_id": "pri_c10_s5", "name": "تقرير استشارات لأولياء الأمور", "order": 4},
    {"id": "pri_c10_s5_r05", "subcategory_id": "pri_c10_s5", "name": "تقرير تقارير دورية عن تقدم الطلاب", "order": 5},
    {"id": "pri_c10_s5_r06", "subcategory_id": "pri_c10_s5", "name": "تقرير إشراك الأسر في خطط التحسين", "order": 6},
    {"id": "pri_c10_s5_r07", "subcategory_id": "pri_c10_s5", "name": "تقرير قنوات تواصل فعالة", "order": 7},
    {"id": "pri_c10_s5_r08", "subcategory_id": "pri_c10_s5", "name": "تقرير استطلاع رضا أولياء الأمور", "order": 8},
    {"id": "pri_c10_s5_r09", "subcategory_id": "pri_c10_s5", "name": "تقرير تحسين التواصل بناءً على التغذية", "order": 9},
    {"id": "pri_c10_s5_r10", "subcategory_id": "pri_c10_s5", "name": "تقرير أثر التواصل على تحسن النتائج", "order": 10},

    # pri_c11_s1 - متابعة التزام المعلمين والطلاب باستخدام المنصات الرقمية
    {"id": "pri_c11_s1_r01", "subcategory_id": "pri_c11_s1", "name": "تقرير تقارير منصة مدرستي لتفعيل المعلمين", "order": 1},
    {"id": "pri_c11_s1_r02", "subcategory_id": "pri_c11_s1", "name": "تقرير حضور الطلاب على المنصات", "order": 2},
    {"id": "pri_c11_s1_r03", "subcategory_id": "pri_c11_s1", "name": "تقرير تفعيل الواجبات الإلكترونية", "order": 3},
    {"id": "pri_c11_s1_r04", "subcategory_id": "pri_c11_s1", "name": "تقرير متابعة استخدام المنصات أسبوعياً", "order": 4},
    {"id": "pri_c11_s1_r05", "subcategory_id": "pri_c11_s1", "name": "تقرير التزام المعلمين برفع المحتوى", "order": 5},
    {"id": "pri_c11_s1_r06", "subcategory_id": "pri_c11_s1", "name": "تقرير تفعيل الاختبارات الإلكترونية", "order": 6},
    {"id": "pri_c11_s1_r07", "subcategory_id": "pri_c11_s1", "name": "تقرير متابعة تسجيل الدخول اليومي", "order": 7},
    {"id": "pri_c11_s1_r08", "subcategory_id": "pri_c11_s1", "name": "تقرير تدريب المتأخرين على استخدام المنصات", "order": 8},
    {"id": "pri_c11_s1_r09", "subcategory_id": "pri_c11_s1", "name": "تقرير مقارنة استخدام المنصات بين الفصول", "order": 9},
    {"id": "pri_c11_s1_r10", "subcategory_id": "pri_c11_s1", "name": "تقرير تحليل مؤشرات الالتزام الشهري", "order": 10},

    # pri_c11_s2 - تحليل تقارير الأداء الرقمي
    {"id": "pri_c11_s2_r01", "subcategory_id": "pri_c11_s2", "name": "تقرير تحليل أداء الطلاب على المنصة", "order": 1},
    {"id": "pri_c11_s2_r02", "subcategory_id": "pri_c11_s2", "name": "تقرير تحليل تفاعل المعلمين مع المنصة", "order": 2},
    {"id": "pri_c11_s2_r03", "subcategory_id": "pri_c11_s2", "name": "تقرير مؤشرات إنجاز الواجبات", "order": 3},
    {"id": "pri_c11_s2_r04", "subcategory_id": "pri_c11_s2", "name": "تقرير نتائج الاختبارات الإلكترونية", "order": 4},
    {"id": "pri_c11_s2_r05", "subcategory_id": "pri_c11_s2", "name": "تقرير تحليل بيانات الحضور الرقمي", "order": 5},
    {"id": "pri_c11_s2_r06", "subcategory_id": "pri_c11_s2", "name": "تقرير مقارنة الأداء الرقمي بين الفصول", "order": 6},
    {"id": "pri_c11_s2_r07", "subcategory_id": "pri_c11_s2", "name": "تقرير استخراج تقارير دورية من المنصة", "order": 7},
    {"id": "pri_c11_s2_r08", "subcategory_id": "pri_c11_s2", "name": "تقرير تحليل تطور الأداء الرقمي", "order": 8},
    {"id": "pri_c11_s2_r09", "subcategory_id": "pri_c11_s2", "name": "تقرير تحديد المعلمين المتميزين في الاستخدام", "order": 9},
    {"id": "pri_c11_s2_r10", "subcategory_id": "pri_c11_s2", "name": "تقرير توصيات لتحسين الأداء الرقمي", "order": 10},

    # pri_c11_s3 - اتخاذ إجراءات تصحيحية عند وجود قصور
    {"id": "pri_c11_s3_r01", "subcategory_id": "pri_c11_s3", "name": "تقرير خطة تحسين للمعلمين قليلي الاستخدام", "order": 1},
    {"id": "pri_c11_s3_r02", "subcategory_id": "pri_c11_s3", "name": "تقرير برامج تدريبية للمعلمين على المنصات", "order": 2},
    {"id": "pri_c11_s3_r03", "subcategory_id": "pri_c11_s3", "name": "تقرير توعية الطلاب بأهمية المنصات", "order": 3},
    {"id": "pri_c11_s3_r04", "subcategory_id": "pri_c11_s3", "name": "تقرير متابعة تحسن الأداء بعد الإجراءات", "order": 4},
    {"id": "pri_c11_s3_r05", "subcategory_id": "pri_c11_s3", "name": "تقرير اجتماعات مع المقصرين", "order": 5},
    {"id": "pri_c11_s3_r06", "subcategory_id": "pri_c11_s3", "name": "تقرير تحديث البنية التحتية لدعم الاستخدام", "order": 6},
    {"id": "pri_c11_s3_r07", "subcategory_id": "pri_c11_s3", "name": "تقرير تحفيز الاستخدام عبر المسابقات", "order": 7},
    {"id": "pri_c11_s3_r08", "subcategory_id": "pri_c11_s3", "name": "تقرير إجراءات إدارية للمعلمين غير الملتزمين", "order": 8},
    {"id": "pri_c11_s3_r09", "subcategory_id": "pri_c11_s3", "name": "تقرير متابعة قصور الطلاب", "order": 9},
    {"id": "pri_c11_s3_r10", "subcategory_id": "pri_c11_s3", "name": "تقرير تقييم فاعلية الإجراءات التصحيحية", "order": 10},

    # pri_c11_s4 - دعم التحول الرقمي في المدرسة
    {"id": "pri_c11_s4_r01", "subcategory_id": "pri_c11_s4", "name": "تقرير خطة التحول الرقمي للمدرسة", "order": 1},
    {"id": "pri_c11_s4_r02", "subcategory_id": "pri_c11_s4", "name": "تقرير توفير الأجهزة والبنية التحتية", "order": 2},
    {"id": "pri_c11_s4_r03", "subcategory_id": "pri_c11_s4", "name": "تقرير تدريب الكادر على المهارات الرقمية", "order": 3},
    {"id": "pri_c11_s4_r04", "subcategory_id": "pri_c11_s4", "name": "تقرير استخدام الأنظمة الإلكترونية في الإدارة", "order": 4},
    {"id": "pri_c11_s4_r05", "subcategory_id": "pri_c11_s4", "name": "تقرير تطوير موقع المدرسة", "order": 5},
    {"id": "pri_c11_s4_r06", "subcategory_id": "pri_c11_s4", "name": "تقرير تفعيل التواصل الرقمي مع أولياء الأمور", "order": 6},
    {"id": "pri_c11_s4_r07", "subcategory_id": "pri_c11_s4", "name": "تقرير متابعة تنفيذ التحول الرقمي", "order": 7},
    {"id": "pri_c11_s4_r08", "subcategory_id": "pri_c11_s4", "name": "تقرير قياس رضا المستخدمين عن الرقمنة", "order": 8},
    {"id": "pri_c11_s4_r09", "subcategory_id": "pri_c11_s4", "name": "تقرير تحديث الخطط الرقمية", "order": 9},
    {"id": "pri_c11_s4_r10", "subcategory_id": "pri_c11_s4", "name": "تقرير استدامة التحول الرقمي", "order": 10},

    # pri_c11_s5 - تطوير كفاءة استخدام التقنية في العمليات التعليمية
    {"id": "pri_c11_s5_r01", "subcategory_id": "pri_c11_s5", "name": "تقرير استخدام التقنية في شرح الدروس", "order": 1},
    {"id": "pri_c11_s5_r02", "subcategory_id": "pri_c11_s5", "name": "تقرير توظيف الوسائط المتعددة", "order": 2},
    {"id": "pri_c11_s5_r03", "subcategory_id": "pri_c11_s5", "name": "تقرير استخدام المحاكاة في العلوم", "order": 3},
    {"id": "pri_c11_s5_r04", "subcategory_id": "pri_c11_s5", "name": "تقرير تطبيق التعلم الإلكتروني المدمج", "order": 4},
    {"id": "pri_c11_s5_r05", "subcategory_id": "pri_c11_s5", "name": "تقرير تقييم كفاءة استخدام التقنية", "order": 5},
    {"id": "pri_c11_s5_r06", "subcategory_id": "pri_c11_s5", "name": "تقرير تطوير مهارات المعلمين في التقنية", "order": 6},
    {"id": "pri_c11_s5_r07", "subcategory_id": "pri_c11_s5", "name": "تقرير استحداث معامل افتراضية", "order": 7},
    {"id": "pri_c11_s5_r08", "subcategory_id": "pri_c11_s5", "name": "تقرير توظيف الذكاء الاصطناعي في التعليم", "order": 8},
    {"id": "pri_c11_s5_r09", "subcategory_id": "pri_c11_s5", "name": "تقرير متابعة تطور استخدام التقنية", "order": 9},
    {"id": "pri_c11_s5_r10", "subcategory_id": "pri_c11_s5", "name": "تقرير أثر التقنية على نواتج التعلم", "order": 10},

    # pri_c12_s1 - الإشراف على برامج تعزيز السلوك الإيجابي
    {"id": "pri_c12_s1_r01", "subcategory_id": "pri_c12_s1", "name": "تقرير خطة برامج تعزيز السلوك", "order": 1},
    {"id": "pri_c12_s1_r02", "subcategory_id": "pri_c12_s1", "name": "تقرير تنفيذ برنامج الطالب المثالي", "order": 2},
    {"id": "pri_c12_s1_r03", "subcategory_id": "pri_c12_s1", "name": "تقرير مسابقات أفضل فصل", "order": 3},
    {"id": "pri_c12_s1_r04", "subcategory_id": "pri_c12_s1", "name": "تقرير تكريم الطلاب ذوي السلوك المتميز", "order": 4},
    {"id": "pri_c12_s1_r05", "subcategory_id": "pri_c12_s1", "name": "تقرير ورش عمل عن القيم", "order": 5},
    {"id": "pri_c12_s1_r06", "subcategory_id": "pri_c12_s1", "name": "تقرير إشراك أولياء الأمور في التعزيز", "order": 6},
    {"id": "pri_c12_s1_r07", "subcategory_id": "pri_c12_s1", "name": "تقرير متابعة تنفيذ البرامج", "order": 7},
    {"id": "pri_c12_s1_r08", "subcategory_id": "pri_c12_s1", "name": "تقرير تقييم أثر برامج التعزيز", "order": 8},
    {"id": "pri_c12_s1_r09", "subcategory_id": "pri_c12_s1", "name": "تقرير تطوير البرامج بناءً على التغذية", "order": 9},
    {"id": "pri_c12_s1_r10", "subcategory_id": "pri_c12_s1", "name": "تقرير توثيق قصص النجاح السلوكية", "order": 10},

    # pri_c12_s2 - متابعة الحالات الفردية بالتنسيق مع التوجيه الطلابي
    {"id": "pri_c12_s2_r01", "subcategory_id": "pri_c12_s2", "name": "تقرير حالات السلوك الفردية", "order": 1},
    {"id": "pri_c12_s2_r02", "subcategory_id": "pri_c12_s2", "name": "تقرير خطة تعديل السلوك الفردية", "order": 2},
    {"id": "pri_c12_s2_r03", "subcategory_id": "pri_c12_s2", "name": "تقرير متابعة الطالب مع المرشد", "order": 3},
    {"id": "pri_c12_s2_r04", "subcategory_id": "pri_c12_s2", "name": "تقرير اجتماعات التوجيه مع أولياء الأمور", "order": 4},
    {"id": "pri_c12_s2_r05", "subcategory_id": "pri_c12_s2", "name": "تقرير تحويل الحالات للجهات المختصة", "order": 5},
    {"id": "pri_c12_s2_r06", "subcategory_id": "pri_c12_s2", "name": "تقرير متابعة تقدم الحالات الفردية", "order": 6},
    {"id": "pri_c12_s2_r07", "subcategory_id": "pri_c12_s2", "name": "تقرير تنسيق الأدوار بين المرشد والمعلمين", "order": 7},
    {"id": "pri_c12_s2_r08", "subcategory_id": "pri_c12_s2", "name": "تقرير تقييم فعالية التدخلات", "order": 8},
    {"id": "pri_c12_s2_r09", "subcategory_id": "pri_c12_s2", "name": "تقرير توثيق حالات التحسن", "order": 9},
    {"id": "pri_c12_s2_r10", "subcategory_id": "pri_c12_s2", "name": "تقرير تحديث سجل الحالات الفردية", "order": 10},

    # pri_c12_s3 - تحليل تقارير التحسن السلوكي
    {"id": "pri_c12_s3_r01", "subcategory_id": "pri_c12_s3", "name": "تقرير تحليل مخالفات السلوك الشهرية", "order": 1},
    {"id": "pri_c12_s3_r02", "subcategory_id": "pri_c12_s3", "name": "تقرير مؤشرات انخفاض المخالفات", "order": 2},
    {"id": "pri_c12_s3_r03", "subcategory_id": "pri_c12_s3", "name": "تقرير مقارنة سلوك الفصول", "order": 3},
    {"id": "pri_c12_s3_r04", "subcategory_id": "pri_c12_s3", "name": "تقرير تحليل أسباب المخالفات", "order": 4},
    {"id": "pri_c12_s3_r05", "subcategory_id": "pri_c12_s3", "name": "تقرير تطور السلوك عبر الفصول الدراسية", "order": 5},
    {"id": "pri_c12_s3_r06", "subcategory_id": "pri_c12_s3", "name": "تقرير تحديد الأنماط السلوكية", "order": 6},
    {"id": "pri_c12_s3_r07", "subcategory_id": "pri_c12_s3", "name": "تقرير أثر برامج التعزيز على التحسن", "order": 7},
    {"id": "pri_c12_s3_r08", "subcategory_id": "pri_c12_s3", "name": "تقرير تحليل تقارير التوجيه الطلابي", "order": 8},
    {"id": "pri_c12_s3_r09", "subcategory_id": "pri_c12_s3", "name": "تقرير توصيات للتحسين", "order": 9},
    {"id": "pri_c12_s3_r10", "subcategory_id": "pri_c12_s3", "name": "تقرير عرض التحليل على القيادة", "order": 10},

    # pri_c12_s4 - تكريم الطلاب المتحسنين والمتميزين
    {"id": "pri_c12_s4_r01", "subcategory_id": "pri_c12_s4", "name": "تقرير حفل تكريم المتميزين", "order": 1},
    {"id": "pri_c12_s4_r02", "subcategory_id": "pri_c12_s4", "name": "تقرير تكريم الطلاب المتحسنين سلوكياً", "order": 2},
    {"id": "pri_c12_s4_r03", "subcategory_id": "pri_c12_s4", "name": "تقرير شهادات شكر للطلاب", "order": 3},
    {"id": "pri_c12_s4_r04", "subcategory_id": "pri_c12_s4", "name": "تقرير نشر أسماء المكرمين في الإذاعة", "order": 4},
    {"id": "pri_c12_s4_r05", "subcategory_id": "pri_c12_s4", "name": "تقرير جوائز عينية للطلاب", "order": 5},
    {"id": "pri_c12_s4_r06", "subcategory_id": "pri_c12_s4", "name": "تقرير تكريم أولياء الأمور", "order": 6},
    {"id": "pri_c12_s4_r07", "subcategory_id": "pri_c12_s4", "name": "تقرير متابعة أثر التكريم", "order": 7},
    {"id": "pri_c12_s4_r08", "subcategory_id": "pri_c12_s4", "name": "تقرير تنوع طرق التكريم", "order": 8},
    {"id": "pri_c12_s4_r09", "subcategory_id": "pri_c12_s4", "name": "تقرير إشراك الطلاب في التكريم", "order": 9},
    {"id": "pri_c12_s4_r10", "subcategory_id": "pri_c12_s4", "name": "تقرير توثيق لحظات التكريم", "order": 10},

    # pri_c12_s5 - تبني أساليب مبتكرة لتعزيز السلوك الإيجابي
    {"id": "pri_c12_s5_r01", "subcategory_id": "pri_c12_s5", "name": "تقرير استخدام النقاط الإلكترونية للسلوك", "order": 1},
    {"id": "pri_c12_s5_r02", "subcategory_id": "pri_c12_s5", "name": "تقرير تطبيق الاقتصاد الرمزي", "order": 2},
    {"id": "pri_c12_s5_r03", "subcategory_id": "pri_c12_s5", "name": "تقرير مسابقات السلوك عبر التطبيقات", "order": 3},
    {"id": "pri_c12_s5_r04", "subcategory_id": "pri_c12_s5", "name": "تقرير مشروع الأصدقاء الداعمين", "order": 4},
    {"id": "pri_c12_s5_r05", "subcategory_id": "pri_c12_s5", "name": "تقرير استخدام الفنون في تعزيز القيم", "order": 5},
    {"id": "pri_c12_s5_r06", "subcategory_id": "pri_c12_s5", "name": "تقرير توظيف المسرح في تعزيز السلوك", "order": 6},
    {"id": "pri_c12_s5_r07", "subcategory_id": "pri_c12_s5", "name": "تقرير مبادرات الطلاب لتعزيز السلوك", "order": 7},
    {"id": "pri_c12_s5_r08", "subcategory_id": "pri_c12_s5", "name": "تقرير شراكات مع جهات خارجية للتعزيز", "order": 8},
    {"id": "pri_c12_s5_r09", "subcategory_id": "pri_c12_s5", "name": "تقرير قياس فاعلية الأساليب المبتكرة", "order": 9},
    {"id": "pri_c12_s5_r10", "subcategory_id": "pri_c12_s5", "name": "تقرير نشر الأساليب الناجحة", "order": 10},

    # pri_c13_s1 - متابعة تطبيق اشتراطات الأمن والسلامة
    {"id": "pri_c13_s1_r01", "subcategory_id": "pri_c13_s1", "name": "تقرير جاهزية طفايات الحريق", "order": 1},
    {"id": "pri_c13_s1_r02", "subcategory_id": "pri_c13_s1", "name": "تقرير صيانة مخارج الطوارئ", "order": 2},
    {"id": "pri_c13_s1_r03", "subcategory_id": "pri_c13_s1", "name": "تقرير تدريب العاملين على السلامة", "order": 3},
    {"id": "pri_c13_s1_r04", "subcategory_id": "pri_c13_s1", "name": "تقرير توفر الإسعافات الأولية", "order": 4},
    {"id": "pri_c13_s1_r05", "subcategory_id": "pri_c13_s1", "name": "تقرير متابعة اشتراطات الأمن دورياً", "order": 5},
    {"id": "pri_c13_s1_r06", "subcategory_id": "pri_c13_s1", "name": "تقرير سلامة الألعاب والساحات", "order": 6},
    {"id": "pri_c13_s1_r07", "subcategory_id": "pri_c13_s1", "name": "تقرير التزام المقصف بالاشتراطات", "order": 7},
    {"id": "pri_c13_s1_r08", "subcategory_id": "pri_c13_s1", "name": "تقرير فحص التمديدات الكهربائية", "order": 8},
    {"id": "pri_c13_s1_r09", "subcategory_id": "pri_c13_s1", "name": "تقرير خطط الإخلاء", "order": 9},
    {"id": "pri_c13_s1_r10", "subcategory_id": "pri_c13_s1", "name": "تقرير تقييم تطبيق اشتراطات السلامة", "order": 10},

    # pri_c13_s2 - معالجة الأعطال والمخاطر فوراً
    {"id": "pri_c13_s2_r01", "subcategory_id": "pri_c13_s2", "name": "تقرير أعطال الكهرباء ومعالجتها", "order": 1},
    {"id": "pri_c13_s2_r02", "subcategory_id": "pri_c13_s2", "name": "تقرير تسرب المياه وإصلاحه", "order": 2},
    {"id": "pri_c13_s2_r03", "subcategory_id": "pri_c13_s2", "name": "تقرير معالجة المخاطر بالألعاب", "order": 3},
    {"id": "pri_c13_s2_r04", "subcategory_id": "pri_c13_s2", "name": "تقرير سرعة الاستجابة للبلاغات", "order": 4},
    {"id": "pri_c13_s2_r05", "subcategory_id": "pri_c13_s2", "name": "تقرير إصلاح أعطال التكييف", "order": 5},
    {"id": "pri_c13_s2_r06", "subcategory_id": "pri_c13_s2", "name": "تقرير معالجة التشققات الجدارية", "order": 6},
    {"id": "pri_c13_s2_r07", "subcategory_id": "pri_c13_s2", "name": "تقرير إزالة المخاطر المؤقتة", "order": 7},
    {"id": "pri_c13_s2_r08", "subcategory_id": "pri_c13_s2", "name": "تقرير متابعة إصلاح الأعطال", "order": 8},
    {"id": "pri_c13_s2_r09", "subcategory_id": "pri_c13_s2", "name": "تقرير تقييم سرعة المعالجة", "order": 9},
    {"id": "pri_c13_s2_r10", "subcategory_id": "pri_c13_s2", "name": "تقرير توثيق الأعطال المتكررة", "order": 10},

    # pri_c13_s3 - توفير بيئة مدرسية جاذبة ومحفزة
    {"id": "pri_c13_s3_r01", "subcategory_id": "pri_c13_s3", "name": "تقرير تحسين المظهر العام للمدرسة", "order": 1},
    {"id": "pri_c13_s3_r02", "subcategory_id": "pri_c13_s3", "name": "تقرير دهان الفصول بألوان محفزة", "order": 2},
    {"id": "pri_c13_s3_r03", "subcategory_id": "pri_c13_s3", "name": "تقرير توفير مساحات خضراء", "order": 3},
    {"id": "pri_c13_s3_r04", "subcategory_id": "pri_c13_s3", "name": "تقرير لوحات جدارية تعليمية", "order": 4},
    {"id": "pri_c13_s3_r05", "subcategory_id": "pri_c13_s3", "name": "تقرير تجهيز ركن للقراءة", "order": 5},
    {"id": "pri_c13_s3_r06", "subcategory_id": "pri_c13_s3", "name": "تقرير نظافة المرافق", "order": 6},
    {"id": "pri_c13_s3_r07", "subcategory_id": "pri_c13_s3", "name": "تقرير تهوية وإضاءة الفصول", "order": 7},
    {"id": "pri_c13_s3_r08", "subcategory_id": "pri_c13_s3", "name": "تقرير توفير مقاعد مريحة", "order": 8},
    {"id": "pri_c13_s3_r09", "subcategory_id": "pri_c13_s3", "name": "تقرير استطلاع رضا الطلاب عن البيئة", "order": 9},
    {"id": "pri_c13_s3_r10", "subcategory_id": "pri_c13_s3", "name": "تقرير تحسين البيئة بناءً على الاقتراحات", "order": 10},

    # pri_c13_s4 - تعزيز الأمان النفسي للطلاب والعاملين
    {"id": "pri_c13_s4_r01", "subcategory_id": "pri_c13_s4", "name": "تقرير برامج الدعم النفسي", "order": 1},
    {"id": "pri_c13_s4_r02", "subcategory_id": "pri_c13_s4", "name": "تقرير مكافحة التنمر", "order": 2},
    {"id": "pri_c13_s4_r03", "subcategory_id": "pri_c13_s4", "name": "تقرير توفير مرشد نفسي", "order": 3},
    {"id": "pri_c13_s4_r04", "subcategory_id": "pri_c13_s4", "name": "تقرير جلسات توعية للصحة النفسية", "order": 4},
    {"id": "pri_c13_s4_r05", "subcategory_id": "pri_c13_s4", "name": "تقرير بيئة آمنة للعاملين", "order": 5},
    {"id": "pri_c13_s4_r06", "subcategory_id": "pri_c13_s4", "name": "تقرير التعامل مع حالات العنف", "order": 6},
    {"id": "pri_c13_s4_r07", "subcategory_id": "pri_c13_s4", "name": "تقرير تعزيز الثقة بين الطلاب", "order": 7},
    {"id": "pri_c13_s4_r08", "subcategory_id": "pri_c13_s4", "name": "تقرير استبيان المناخ النفسي", "order": 8},
    {"id": "pri_c13_s4_r09", "subcategory_id": "pri_c13_s4", "name": "تقرير شراكات مع جهات استشارية", "order": 9},
    {"id": "pri_c13_s4_r10", "subcategory_id": "pri_c13_s4", "name": "تقرير قياس أثر برامج الأمان النفسي", "order": 10},

    # pri_c13_s5 - متابعة البلاغات والتقارير الدورية
    {"id": "pri_c13_s5_r01", "subcategory_id": "pri_c13_s5", "name": "تقرير سجل البلاغات الواردة", "order": 1},
    {"id": "pri_c13_s5_r02", "subcategory_id": "pri_c13_s5", "name": "تقرير زمن الاستجابة للبلاغات", "order": 2},
    {"id": "pri_c13_s5_r03", "subcategory_id": "pri_c13_s5", "name": "تقرير إجراءات معالجة البلاغات", "order": 3},
    {"id": "pri_c13_s5_r04", "subcategory_id": "pri_c13_s5", "name": "تقرير البلاغات المتكررة", "order": 4},
    {"id": "pri_c13_s5_r05", "subcategory_id": "pri_c13_s5", "name": "تقرير تحليل البلاغات الشهرية", "order": 5},
    {"id": "pri_c13_s5_r06", "subcategory_id": "pri_c13_s5", "name": "تقرير إبلاغ الجهات المختصة", "order": 6},
    {"id": "pri_c13_s5_r07", "subcategory_id": "pri_c13_s5", "name": "تقرير متابعة تنفيذ التوصيات", "order": 7},
    {"id": "pri_c13_s5_r08", "subcategory_id": "pri_c13_s5", "name": "تقرير توثيق البلاغات", "order": 8},
    {"id": "pri_c13_s5_r09", "subcategory_id": "pri_c13_s5", "name": "تقرير تقييم فعالية المعالجة", "order": 9},
    {"id": "pri_c13_s5_r10", "subcategory_id": "pri_c13_s5", "name": "تقرير تحسين نظام البلاغات", "order": 10},

    # pri_c14_s1 - تنفيذ زيارات صفية دورية
    {"id": "pri_c14_s1_r01", "subcategory_id": "pri_c14_s1", "name": "تقرير جدول الزيارات الصفية", "order": 1},
    {"id": "pri_c14_s1_r02", "subcategory_id": "pri_c14_s1", "name": "تقرير عدد الزيارات المنفذة", "order": 2},
    {"id": "pri_c14_s1_r03", "subcategory_id": "pri_c14_s1", "name": "تقرير تغطية الزيارات للمعلمين", "order": 3},
    {"id": "pri_c14_s1_r04", "subcategory_id": "pri_c14_s1", "name": "تقرير أهداف الزيارات", "order": 4},
    {"id": "pri_c14_s1_r05", "subcategory_id": "pri_c14_s1", "name": "تقرير نتائج الزيارات", "order": 5},
    {"id": "pri_c14_s1_r06", "subcategory_id": "pri_c14_s1", "name": "تقرير متابعة تحسن الأداء بعد الزيارات", "order": 6},
    {"id": "pri_c14_s1_r07", "subcategory_id": "pri_c14_s1", "name": "تقرير تنوع الزيارات (تخطيط، تنفيذ)", "order": 7},
    {"id": "pri_c14_s1_r08", "subcategory_id": "pri_c14_s1", "name": "تقرير توثيق الزيارات", "order": 8},
    {"id": "pri_c14_s1_r09", "subcategory_id": "pri_c14_s1", "name": "تقرير مراجعة خطة الزيارات", "order": 9},
    {"id": "pri_c14_s1_r10", "subcategory_id": "pri_c14_s1", "name": "تقرير أثر الزيارات على الممارسات", "order": 10},

    # pri_c14_s2 - تقديم تغذية راجعة تطويرية للمعلمين
    {"id": "pri_c14_s2_r01", "subcategory_id": "pri_c14_s2", "name": "تقرير نماذج التغذية الراجعة", "order": 1},
    {"id": "pri_c14_s2_r02", "subcategory_id": "pri_c14_s2", "name": "تقرير جلسات التغذية الفردية", "order": 2},
    {"id": "pri_c14_s2_r03", "subcategory_id": "pri_c14_s2", "name": "تقرير توقيت التغذية الراجعة", "order": 3},
    {"id": "pri_c14_s2_r04", "subcategory_id": "pri_c14_s2", "name": "تقرير جودة التغذية (إيجابية وبناءة)", "order": 4},
    {"id": "pri_c14_s2_r05", "subcategory_id": "pri_c14_s2", "name": "تقرير متابعة تنفيذ التوصيات", "order": 5},
    {"id": "pri_c14_s2_r06", "subcategory_id": "pri_c14_s2", "name": "تقرير استجابة المعلمين للتغذية", "order": 6},
    {"id": "pri_c14_s2_r07", "subcategory_id": "pri_c14_s2", "name": "تقرير تدريب القادة على التغذية", "order": 7},
    {"id": "pri_c14_s2_r08", "subcategory_id": "pri_c14_s2", "name": "تقرير توثيق التغذية الراجعة", "order": 8},
    {"id": "pri_c14_s2_r09", "subcategory_id": "pri_c14_s2", "name": "تقرير قياس رضا المعلمين عن التغذية", "order": 9},
    {"id": "pri_c14_s2_r10", "subcategory_id": "pri_c14_s2", "name": "تقرير أثر التغذية على الأداء", "order": 10},

    # pri_c14_s3 - متابعة مؤشرات الانضباط والنشاط
    {"id": "pri_c14_s3_r01", "subcategory_id": "pri_c14_s3", "name": "تقرير مؤشرات غياب المعلمين", "order": 1},
    {"id": "pri_c14_s3_r02", "subcategory_id": "pri_c14_s3", "name": "تقرير مؤشرات حضور المعلمين للاجتماعات", "order": 2},
    {"id": "pri_c14_s3_r03", "subcategory_id": "pri_c14_s3", "name": "تقرير مؤشرات الانضباط الوظيفي", "order": 3},
    {"id": "pri_c14_s3_r04", "subcategory_id": "pri_c14_s3", "name": "تقرير مشاركة المعلمين في الأنشطة", "order": 4},
    {"id": "pri_c14_s3_r05", "subcategory_id": "pri_c14_s3", "name": "تقرير مؤشرات أداء المعلمين", "order": 5},
    {"id": "pri_c14_s3_r06", "subcategory_id": "pri_c14_s3", "name": "تقرير تحليل مؤشرات الانضباط", "order": 6},
    {"id": "pri_c14_s3_r07", "subcategory_id": "pri_c14_s3", "name": "تقرير متابعة تحسن المؤشرات", "order": 7},
    {"id": "pri_c14_s3_r08", "subcategory_id": "pri_c14_s3", "name": "تقرير مقارنة مؤشرات الفصول", "order": 8},
    {"id": "pri_c14_s3_r09", "subcategory_id": "pri_c14_s3", "name": "تقرير عرض المؤشرات على المعلمين", "order": 9},
    {"id": "pri_c14_s3_r10", "subcategory_id": "pri_c14_s3", "name": "تقرير استخدام المؤشرات للتحفيز", "order": 10},

    # pri_c14_s4 - تعزيز نقاط القوة ومعالجة جوانب التحسين
    {"id": "pri_c14_s4_r01", "subcategory_id": "pri_c14_s4", "name": "تقرير تحديد نقاط القوة لدى المعلمين", "order": 1},
    {"id": "pri_c14_s4_r02", "subcategory_id": "pri_c14_s4", "name": "تقرير خطط تعزيز نقاط القوة", "order": 2},
    {"id": "pri_c14_s4_r03", "subcategory_id": "pri_c14_s4", "name": "تقرير تحديد جوانب التحسين", "order": 3},
    {"id": "pri_c14_s4_r04", "subcategory_id": "pri_c14_s4", "name": "تقرير خطط علاجية للمعلمين", "order": 4},
    {"id": "pri_c14_s4_r05", "subcategory_id": "pri_c14_s4", "name": "تقرير متابعة تحسن الأداء", "order": 5},
    {"id": "pri_c14_s4_r06", "subcategory_id": "pri_c14_s4", "name": "تقرير تبادل الخبرات بين المعلمين", "order": 6},
    {"id": "pri_c14_s4_r07", "subcategory_id": "pri_c14_s4", "name": "تقرير تكريم المعلمين المتميزين", "order": 7},
    {"id": "pri_c14_s4_r08", "subcategory_id": "pri_c14_s4", "name": "تقرير دعم المعلمين المحتاجين", "order": 8},
    {"id": "pri_c14_s4_r09", "subcategory_id": "pri_c14_s4", "name": "تقرير تقييم فعالية المعالجة", "order": 9},
    {"id": "pri_c14_s4_r10", "subcategory_id": "pri_c14_s4", "name": "تقرير استدامة نقاط القوة", "order": 10},

    # pri_c14_s5 - توثيق الأداء ومتابعة التطور المهني
    {"id": "pri_c14_s5_r01", "subcategory_id": "pri_c14_s5", "name": "تقرير ملفات الإنجاز للمعلمين", "order": 1},
    {"id": "pri_c14_s5_r02", "subcategory_id": "pri_c14_s5", "name": "تقرير توثيق الزيارات الصفية", "order": 2},
    {"id": "pri_c14_s5_r03", "subcategory_id": "pri_c14_s5", "name": "تقرير سجل التطور المهني", "order": 3},
    {"id": "pri_c14_s5_r04", "subcategory_id": "pri_c14_s5", "name": "تقرير متابعة خطط التطوير الذاتي", "order": 4},
    {"id": "pri_c14_s5_r05", "subcategory_id": "pri_c14_s5", "name": "تقرير تحديث بيانات الأداء", "order": 5},
    {"id": "pri_c14_s5_r06", "subcategory_id": "pri_c14_s5", "name": "تقرير توثيق الشهادات والدورات", "order": 6},
    {"id": "pri_c14_s5_r07", "subcategory_id": "pri_c14_s5", "name": "تقرير مراجعة التطور المهني", "order": 7},
    {"id": "pri_c14_s5_r08", "subcategory_id": "pri_c14_s5", "name": "تقرير توثيق الإنجازات", "order": 8},
    {"id": "pri_c14_s5_r09", "subcategory_id": "pri_c14_s5", "name": "تقرير استخدام التوثيق في التقويم", "order": 9},
    {"id": "pri_c14_s5_r10", "subcategory_id": "pri_c14_s5", "name": "تقرير تحسين نظام التوثيق", "order": 10}
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