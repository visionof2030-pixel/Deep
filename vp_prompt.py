# vp_prompt.py

# معايير الأداء الوظيفي مع النسب المئوية (محدثة)
VP_CRITERIA = [
    {"id": "vp_c1", "name": "أداء الواجبات الوظيفية", "weight": 5, "order": 1},
    {"id": "vp_c2", "name": "التفاعل مع المجتمع المهني", "weight": 5, "order": 2},
    {"id": "vp_c3", "name": "التفاعل مع أولياء الأمور", "weight": 5, "order": 3},
    {"id": "vp_c4", "name": "مرن وقادر على تنفيذ أعماله في ظل ظروف العمل المختلفة", "weight": 5, "order": 4},
    {"id": "vp_c5", "name": "يدعم ويشارك في المبادرات النوعية", "weight": 10, "order": 5},
    {"id": "vp_c6", "name": "يتخذ إجراءات تربوية تحقق الانضباط المدرسي", "weight": 5, "order": 6},
    {"id": "vp_c7", "name": "يدير الموارد في المدرسة بكفاءة", "weight": 5, "order": 7},
    {"id": "vp_c8", "name": "يشارك في إعداد خطة للتطوير المهني", "weight": 5, "order": 8},
    {"id": "vp_c9", "name": "يقدم التغذية الراجعة ويتابع تحقق مؤشرات الأداء الوظيفي", "weight": 5, "order": 9},
    {"id": "vp_c10", "name": "يدعم تنفيذ برامج التطوير المهني", "weight": 5, "order": 10},
    {"id": "vp_c11", "name": "يقيم أداء منسوبي المدرسة", "weight": 5, "order": 11},
    {"id": "vp_c12", "name": "ينفذ إجراءات علمية لتحسين نتائج التعلم", "weight": 15, "order": 12},
    {"id": "vp_c13", "name": "يسهم في تحسين مستوى أداء المدرسة", "weight": 5, "order": 13},
    {"id": "vp_c14", "name": "يشارك في إعداد الخطط المدرسية اللازمة", "weight": 5, "order": 14},
    {"id": "vp_c15", "name": "يتابع تنفيذ الخطط المدرسية بمختلف أنواعها", "weight": 5, "order": 15},
    {"id": "vp_c16", "name": "يهيئ الفرص والإمكانات الداعمة لمشاركة الطلاب", "weight": 5, "order": 16},
    {"id": "vp_c17", "name": "يوظف المنصات الرقمية وتطبيقاتها المعتمدة", "weight": 5, "order": 17},
    {"id": "vp_c18", "name": "يتابع تعزيز السلوك الإيجابي للطلاب", "weight": 5, "order": 18},
    {"id": "vp_c19", "name": "يهيئ بيئة مدرسية آمنة ومحفزة على التعلم", "weight": 5, "order": 19},
]

# التصنيفات الفرعية (محدثة)
VP_SUBCATEGORIES = [
    # vp_c1 - أداء الواجبات الوظيفية (4)
    {"id": "vp_c1_s1", "criterion_id": "vp_c1", "name": "الالتزام بالدوام الرسمي وقواعد السلوك الوظيفي", "order": 1},
    {"id": "vp_c1_s2", "criterion_id": "vp_c1", "name": "الامتثال للأنظمة واللوائح", "order": 2},
    {"id": "vp_c1_s3", "criterion_id": "vp_c1", "name": "حماية البيانات والمعلومات", "order": 3},
    {"id": "vp_c1_s4", "criterion_id": "vp_c1", "name": "تنفيذ المهام وفق الصلاحيات والمسؤوليات", "order": 4},

    # vp_c2 - التفاعل مع المجتمع المهني (4)
    {"id": "vp_c2_s1", "criterion_id": "vp_c2", "name": "حضور المؤتمرات والندوات التعليمية", "order": 1},
    {"id": "vp_c2_s2", "criterion_id": "vp_c2", "name": "المشاركة في ورش العمل", "order": 2},
    {"id": "vp_c2_s3", "criterion_id": "vp_c2", "name": "دعم المعلمين الجدد", "order": 3},
    {"id": "vp_c2_s4", "criterion_id": "vp_c2", "name": "تبادل الخبرات المهنية", "order": 4},

    # vp_c3 - التفاعل مع أولياء الأمور (4)
    {"id": "vp_c3_s1", "criterion_id": "vp_c3", "name": "تفعيل قنوات الاتصال مع أولياء الأمور", "order": 1},
    {"id": "vp_c3_s2", "criterion_id": "vp_c3", "name": "عقد الاجتماعات الدورية مع أولياء الأمور", "order": 2},
    {"id": "vp_c3_s3", "criterion_id": "vp_c3", "name": "مناقشة أداء المتعلمين مع أولياء الأمور", "order": 3},
    {"id": "vp_c3_s4", "criterion_id": "vp_c3", "name": "الاستجابة لملاحظات أولياء الأمور", "order": 4},

    # vp_c4 - المرونة وتنفيذ الأعمال (3)
    {"id": "vp_c4_s1", "criterion_id": "vp_c4", "name": "إدارة المهام المتعددة بفعالية", "order": 1},
    {"id": "vp_c4_s2", "criterion_id": "vp_c4", "name": "معالجة المشكلات الإدارية", "order": 2},
    {"id": "vp_c4_s3", "criterion_id": "vp_c4", "name": "التكيف مع المتغيرات", "order": 3},

    # vp_c5 - المبادرات النوعية (6)
    {"id": "vp_c5_s1", "criterion_id": "vp_c5", "name": "دعم التجارب والمشروعات المتميزة", "order": 1},
    {"id": "vp_c5_s2", "criterion_id": "vp_c5", "name": "دراسة المبادرات الواردة من المدارس", "order": 2},
    {"id": "vp_c5_s3", "criterion_id": "vp_c5", "name": "إعداد تقارير للمشروعات القابلة للتطبيق", "order": 3},
    {"id": "vp_c5_s4", "criterion_id": "vp_c5", "name": "نشر التجارب المتميزة", "order": 4},
    {"id": "vp_c5_s5", "criterion_id": "vp_c5", "name": "توظيف التقنية في المتابعة والنشر", "order": 5},
    {"id": "vp_c5_s6", "criterion_id": "vp_c5", "name": "ابتكار حلول ومبادرات إبداعية", "order": 6},

    # vp_c6 - الانضباط المدرسي (4)
    {"id": "vp_c6_s1", "criterion_id": "vp_c6", "name": "تطبيق قواعد السلوك والمواظبة", "order": 1},
    {"id": "vp_c6_s2", "criterion_id": "vp_c6", "name": "تنفيذ خطة الانضباط", "order": 2},
    {"id": "vp_c6_s3", "criterion_id": "vp_c6", "name": "متابعة تقارير الالتزام", "order": 3},
    {"id": "vp_c6_s4", "criterion_id": "vp_c6", "name": "تعزيز السلوك الإيجابي", "order": 4},

    # vp_c7 - إدارة الموارد (3)
    {"id": "vp_c7_s1", "criterion_id": "vp_c7", "name": "توزيع المهام بعدالة", "order": 1},
    {"id": "vp_c7_s2", "criterion_id": "vp_c7", "name": "إدارة الموارد المالية", "order": 2},
    {"id": "vp_c7_s3", "criterion_id": "vp_c7", "name": "متابعة تقارير التدقيق", "order": 3},

    # vp_c8 - المشاركة في خطة التطوير المهني (4)
    {"id": "vp_c8_s1", "criterion_id": "vp_c8", "name": "إعداد خطة تطوير مهني", "order": 1},
    {"id": "vp_c8_s2", "criterion_id": "vp_c8", "name": "حصر الاحتياجات التدريبية", "order": 2},
    {"id": "vp_c8_s3", "criterion_id": "vp_c8", "name": "متابعة الرخص المهنية", "order": 3},
    {"id": "vp_c8_s4", "criterion_id": "vp_c8", "name": "نقل الخبرات بين المعلمين", "order": 4},

    # vp_c9 - التغذية الراجعة ومؤشرات الأداء (4)
    {"id": "vp_c9_s1", "criterion_id": "vp_c9", "name": "مراجعة الأداء السابق", "order": 1},
    {"id": "vp_c9_s2", "criterion_id": "vp_c9", "name": "قياس نسبة التقدم", "order": 2},
    {"id": "vp_c9_s3", "criterion_id": "vp_c9", "name": "إزالة المعوقات", "order": 3},
    {"id": "vp_c9_s4", "criterion_id": "vp_c9", "name": "تعزيز السلوكيات الفعالة", "order": 4},

    # vp_c10 - دعم تنفيذ برامج التطوير المهني (4)
    {"id": "vp_c10_s1", "criterion_id": "vp_c10", "name": "تنفيذ برامج التطوير", "order": 1},
    {"id": "vp_c10_s2", "criterion_id": "vp_c10", "name": "قياس أثر التدريب", "order": 2},
    {"id": "vp_c10_s3", "criterion_id": "vp_c10", "name": "إعداد ملفات الإنجاز", "order": 3},
    {"id": "vp_c10_s4", "criterion_id": "vp_c10", "name": "متابعة تحسين الأداء", "order": 4},

    # vp_c11 - تقييم أداء منسوبي المدرسة (4)
    {"id": "vp_c11_s1", "criterion_id": "vp_c11", "name": "تقويم أداء المرؤوسين بأساليب علمية", "order": 1},
    {"id": "vp_c11_s2", "criterion_id": "vp_c11", "name": "استخدام أدوات تقويم متنوعة", "order": 2},
    {"id": "vp_c11_s3", "criterion_id": "vp_c11", "name": "ملاحظة الأداء (تخطيط – تنفيذ – تقويم)", "order": 3},
    {"id": "vp_c11_s4", "criterion_id": "vp_c11", "name": "توظيف نتائج التقويم في تحسين الأداء", "order": 4},

    # vp_c12 - تحسين نتائج التعلم (6)
    {"id": "vp_c12_s1", "criterion_id": "vp_c12", "name": "تشخيص أداء المتعلمين وتصنيفهم", "order": 1},
    {"id": "vp_c12_s2", "criterion_id": "vp_c12", "name": "تحليل النتائج", "order": 2},
    {"id": "vp_c12_s3", "criterion_id": "vp_c12", "name": "تقديم معالجات تربوية", "order": 3},
    {"id": "vp_c12_s4", "criterion_id": "vp_c12", "name": "رصد نمو المتعلمين", "order": 4},
    {"id": "vp_c12_s5", "criterion_id": "vp_c12", "name": "تطوير عمليات التعليم والتعلم", "order": 5},
    {"id": "vp_c12_s6", "criterion_id": "vp_c12", "name": "التواصل مع أولياء الأمور بشأن نتائج التعلم", "order": 6},

    # vp_c13 - تحسين مستوى أداء المدرسة (3)
    {"id": "vp_c13_s1", "criterion_id": "vp_c13", "name": "بناء خطط تحسينية", "order": 1},
    {"id": "vp_c13_s2", "criterion_id": "vp_c13", "name": "متابعة مؤشرات الأداء", "order": 2},
    {"id": "vp_c13_s3", "criterion_id": "vp_c13", "name": "تعزيز الشراكات المجتمعية", "order": 3},

    # vp_c14 - إعداد الخطط المدرسية (3)
    {"id": "vp_c14_s1", "criterion_id": "vp_c14", "name": "إعداد الخطة التشغيلية", "order": 1},
    {"id": "vp_c14_s2", "criterion_id": "vp_c14", "name": "إعداد خطط بديلة", "order": 2},
    {"id": "vp_c14_s3", "criterion_id": "vp_c14", "name": "إعداد خطط المخاطر والسلامة", "order": 3},

    # vp_c15 - متابعة تنفيذ الخطط (4)
    {"id": "vp_c15_s1", "criterion_id": "vp_c15", "name": "متابعة تنفيذ الخطط", "order": 1},
    {"id": "vp_c15_s2", "criterion_id": "vp_c15", "name": "متابعة خطط المعلمين", "order": 2},
    {"id": "vp_c15_s3", "criterion_id": "vp_c15", "name": "قياس أثر التنفيذ", "order": 3},
    {"id": "vp_c15_s4", "criterion_id": "vp_c15", "name": "معالجة جوانب القصور", "order": 4},

    # vp_c16 - دعم مشاركة الطلاب (3)
    {"id": "vp_c16_s1", "criterion_id": "vp_c16", "name": "دعم الأنشطة الصفية واللاصفية", "order": 1},
    {"id": "vp_c16_s2", "criterion_id": "vp_c16", "name": "دعم المشاركات الداخلية والخارجية", "order": 2},
    {"id": "vp_c16_s3", "criterion_id": "vp_c16", "name": "توثيق الإنجازات الطلابية", "order": 3},

    # vp_c17 - توظيف المنصات الرقمية (3)
    {"id": "vp_c17_s1", "criterion_id": "vp_c17", "name": "متابعة استخدام المنصات", "order": 1},
    {"id": "vp_c17_s2", "criterion_id": "vp_c17", "name": "الالتزام بضوابط منصة مدرستي", "order": 2},
    {"id": "vp_c17_s3", "criterion_id": "vp_c17", "name": "دعم التعليم الرقمي", "order": 3},

    # vp_c18 - تعزيز السلوك الإيجابي (3)
    {"id": "vp_c18_s1", "criterion_id": "vp_c18", "name": "متابعة لجنة التوجيه الطلابي", "order": 1},
    {"id": "vp_c18_s2", "criterion_id": "vp_c18", "name": "معالجة الحالات الفردية", "order": 2},
    {"id": "vp_c18_s3", "criterion_id": "vp_c18", "name": "تكريم الطلاب المتحسنين", "order": 3},

    # vp_c19 - بيئة مدرسية آمنة ومحفزة (3)
    {"id": "vp_c19_s1", "criterion_id": "vp_c19", "name": "تطبيق معايير الأمن والسلامة", "order": 1},
    {"id": "vp_c19_s2", "criterion_id": "vp_c19", "name": "متابعة البلاغات والأعطال", "order": 2},
    {"id": "vp_c19_s3", "criterion_id": "vp_c19", "name": "توفير بيئة جاذبة ومحفزة", "order": 3},
]

# التقارير (10 تقارير لكل تصنيف فرعي) – تم إنشاؤها بما يتوافق مع التصنيفات الجديدة
VP_REPORTS = [
    # vp_c1_s1 - الالتزام بالدوام الرسمي وقواعد السلوك الوظيفي
    {"id": "vp_c1_s1_r001", "subcategory_id": "vp_c1_s1", "name": "سجل متابعة انضباط الموظفين في الدوام الرسمي", "order": 1},
    {"id": "vp_c1_s1_r002", "subcategory_id": "vp_c1_s1", "name": "تقرير تطبيق قواعد السلوك الوظيفي في المدرسة", "order": 2},
    {"id": "vp_c1_s1_r003", "subcategory_id": "vp_c1_s1", "name": "كشف حضور وانصراف الكادر الإداري والتعليمي", "order": 3},
    {"id": "vp_c1_s1_r004", "subcategory_id": "vp_c1_s1", "name": "تقرير عن حالات مخالفات السلوك الوظيفي والإجراءات المتخذة", "order": 4},
    {"id": "vp_c1_s1_r005", "subcategory_id": "vp_c1_s1", "name": "سجل توعية الموظفين بقواعد السلوك الوظيفي", "order": 5},
    {"id": "vp_c1_s1_r006", "subcategory_id": "vp_c1_s1", "name": "تقرير تحليل نسب الغياب والتأخير", "order": 6},
    {"id": "vp_c1_s1_r007", "subcategory_id": "vp_c1_s1", "name": "سجل المقابلات التوجيهية للموظفين المخالفين", "order": 7},
    {"id": "vp_c1_s1_r008", "subcategory_id": "vp_c1_s1", "name": "تقرير أثر الالتزام بالدوام على سير العمل", "order": 8},
    {"id": "vp_c1_s1_r009", "subcategory_id": "vp_c1_s1", "name": "سجل إشعارات الموظفين بتعليمات الحضور والانصراف", "order": 9},
    {"id": "vp_c1_s1_r010", "subcategory_id": "vp_c1_s1", "name": "تقرير تقييم نظام البصمة أو الحضور الإلكتروني", "order": 10},

    # vp_c1_s2 - الامتثال للأنظمة واللوائح
    {"id": "vp_c1_s2_r001", "subcategory_id": "vp_c1_s2", "name": "تقرير مدى امتثال المدرسة للأنظمة والتعليمات", "order": 1},
    {"id": "vp_c1_s2_r002", "subcategory_id": "vp_c1_s2", "name": "سجل متابعة تنفيذ اللوائح المنظمة للعمل", "order": 2},
    {"id": "vp_c1_s2_r003", "subcategory_id": "vp_c1_s2", "name": "تقرير الالتزام بلائحة تقويم الطالب", "order": 3},
    {"id": "vp_c1_s2_r004", "subcategory_id": "vp_c1_s2", "name": "سجل تدريب الموظفين على الأنظمة الجديدة", "order": 4},
    {"id": "vp_c1_s2_r005", "subcategory_id": "vp_c1_s2", "name": "تقرير عن تطبيق لائحة الإجازات", "order": 5},
    {"id": "vp_c1_s2_r006", "subcategory_id": "vp_c1_s2", "name": "سجل متابعة تعاميم الوزارة وإجراءات تنفيذها", "order": 6},
    {"id": "vp_c1_s2_r007", "subcategory_id": "vp_c1_s2", "name": "تقرير عن ضبط المخالفات الإدارية", "order": 7},
    {"id": "vp_c1_s2_r008", "subcategory_id": "vp_c1_s2", "name": "سجل تحديث دليل الإجراءات المدرسية", "order": 8},
    {"id": "vp_c1_s2_r009", "subcategory_id": "vp_c1_s2", "name": "تقرير الامتثال للوائح الصحة والسلامة", "order": 9},
    {"id": "vp_c1_s2_r010", "subcategory_id": "vp_c1_s2", "name": "سجل مراجعة مدى الالتزام بالأنظمة المالية", "order": 10},

    # vp_c1_s3 - حماية البيانات والمعلومات
    {"id": "vp_c1_s3_r001", "subcategory_id": "vp_c1_s3", "name": "تقرير عن سياسات حماية بيانات الطلاب", "order": 1},
    {"id": "vp_c1_s3_r002", "subcategory_id": "vp_c1_s3", "name": "سجل صلاحيات الوصول لنظام نور", "order": 2},
    {"id": "vp_c1_s3_r003", "subcategory_id": "vp_c1_s3", "name": "تقرير الالتزام بخصوصية المعلومات", "order": 3},
    {"id": "vp_c1_s3_r004", "subcategory_id": "vp_c1_s3", "name": "سجل تدريب الموظفين على أمن المعلومات", "order": 4},
    {"id": "vp_c1_s3_r005", "subcategory_id": "vp_c1_s3", "name": "تقرير عن آليات حفظ الملفات الإلكترونية", "order": 5},
    {"id": "vp_c1_s3_r006", "subcategory_id": "vp_c1_s3", "name": "سجل موافقات أولياء الأمور على نشر بيانات الأبناء", "order": 6},
    {"id": "vp_c1_s3_r007", "subcategory_id": "vp_c1_s3", "name": "تقرير عن مدى أمان كلمات المرور", "order": 7},
    {"id": "vp_c1_s3_r008", "subcategory_id": "vp_c1_s3", "name": "سجل الحوادث المتعلقة بتسريب المعلومات", "order": 8},
    {"id": "vp_c1_s3_r009", "subcategory_id": "vp_c1_s3", "name": "تقرير عن تحديث برامج الحماية", "order": 9},
    {"id": "vp_c1_s3_r010", "subcategory_id": "vp_c1_s3", "name": "سجل التوعية بأمن المعلومات للمجتمع المدرسي", "order": 10},

    # vp_c1_s4 - تنفيذ المهام وفق الصلاحيات والمسؤوليات
    {"id": "vp_c1_s4_r001", "subcategory_id": "vp_c1_s4", "name": "تقرير توزيع المهام على الوكلاء وفق الصلاحيات", "order": 1},
    {"id": "vp_c1_s4_r002", "subcategory_id": "vp_c1_s4", "name": "سجل تفويض الصلاحيات أثناء الغياب", "order": 2},
    {"id": "vp_c1_s4_r003", "subcategory_id": "vp_c1_s4", "name": "تقرير مدى التزام شاغلي الوظائف بمسؤولياتهم", "order": 3},
    {"id": "vp_c1_s4_r004", "subcategory_id": "vp_c1_s4", "name": "سجل متابعة تنفيذ المكلفات الرسمية", "order": 4},
    {"id": "vp_c1_s4_r005", "subcategory_id": "vp_c1_s4", "name": "تقرير عن الإنجاز في ضوء الصلاحيات المخولة", "order": 5},
    {"id": "vp_c1_s4_r006", "subcategory_id": "vp_c1_s4", "name": "سجل تحديث بطاقات الوصف الوظيفي", "order": 6},
    {"id": "vp_c1_s4_r007", "subcategory_id": "vp_c1_s4", "name": "تقرير عن التداخل في الصلاحيات ومعالجته", "order": 7},
    {"id": "vp_c1_s4_r008", "subcategory_id": "vp_c1_s4", "name": "سجل رفع التقارير الدورية عن مستوى الأداء", "order": 8},
    {"id": "vp_c1_s4_r009", "subcategory_id": "vp_c1_s4", "name": "تقرير عن مدى تفويض القيادة للمسؤوليات", "order": 9},
    {"id": "vp_c1_s4_r010", "subcategory_id": "vp_c1_s4", "name": "سجل تحسين آليات توزيع المهام", "order": 10},

    # vp_c2_s1 - حضور المؤتمرات والندوات التعليمية
    {"id": "vp_c2_s1_r001", "subcategory_id": "vp_c2_s1", "name": "تقرير مشاركة المعلمين في المؤتمرات التربوية", "order": 1},
    {"id": "vp_c2_s1_r002", "subcategory_id": "vp_c2_s1", "name": "سجل حضور الندوات التعليمية وتلخيصها", "order": 2},
    {"id": "vp_c2_s1_r003", "subcategory_id": "vp_c2_s1", "name": "تقرير أثر المؤتمرات على تطوير الممارسات", "order": 3},
    {"id": "vp_c2_s1_r004", "subcategory_id": "vp_c2_s1", "name": "سجل نقل خبرات المؤتمرات لبقية المعلمين", "order": 4},
    {"id": "vp_c2_s1_r005", "subcategory_id": "vp_c2_s1", "name": "تقرير عن مشاركة المدرسة في المؤتمرات الافتراضية", "order": 5},
    {"id": "vp_c2_s1_r006", "subcategory_id": "vp_c2_s1", "name": "سجل حصر المؤتمرات المتخصصة للمجال التعليمي", "order": 6},
    {"id": "vp_c2_s1_r007", "subcategory_id": "vp_c2_s1", "name": "تقرير عن التوصيات المطبقة من المؤتمرات", "order": 7},
    {"id": "vp_c2_s1_r008", "subcategory_id": "vp_c2_s1", "name": "سجل شهادات حضور المؤتمرات", "order": 8},
    {"id": "vp_c2_s1_r009", "subcategory_id": "vp_c2_s1", "name": "تقرير عن تنظيم لقاءات علمية مستوحاة من المؤتمرات", "order": 9},
    {"id": "vp_c2_s1_r010", "subcategory_id": "vp_c2_s1", "name": "سجل تقييم الاستفادة من المؤتمرات", "order": 10},

    # vp_c2_s2 - المشاركة في ورش العمل
    {"id": "vp_c2_s2_r001", "subcategory_id": "vp_c2_s2", "name": "تقرير مشاركة المعلمين في ورش العمل التدريبية", "order": 1},
    {"id": "vp_c2_s2_r002", "subcategory_id": "vp_c2_s2", "name": "سجل تنفيذ ورش عمل داخلية من قبل المتدربين", "order": 2},
    {"id": "vp_c2_s2_r003", "subcategory_id": "vp_c2_s2", "name": "تقرير أثر ورش العمل على الأداء الصفي", "order": 3},
    {"id": "vp_c2_s2_r004", "subcategory_id": "vp_c2_s2", "name": "سجل حصر الاحتياجات التدريبية لورش العمل", "order": 4},
    {"id": "vp_c2_s2_r005", "subcategory_id": "vp_c2_s2", "name": "تقرير عن جاهزية قاعة التدريب بالمدرسة", "order": 5},
    {"id": "vp_c2_s2_r006", "subcategory_id": "vp_c2_s2", "name": "سجل متابعة تطبيق مخرجات ورش العمل", "order": 6},
    {"id": "vp_c2_s2_r007", "subcategory_id": "vp_c2_s2", "name": "تقرير عن استضافة مدربين خارجيين", "order": 7},
    {"id": "vp_c2_s2_r008", "subcategory_id": "vp_c2_s2", "name": "سجل تقييم المشاركين لورش العمل", "order": 8},
    {"id": "vp_c2_s2_r009", "subcategory_id": "vp_c2_s2", "name": "تقرير عن مساهمة المدرسة في ورش عمل على مستوى المكتب", "order": 9},
    {"id": "vp_c2_s2_r010", "subcategory_id": "vp_c2_s2", "name": "سجل تطوير خطة التدريب بناءً على الورش", "order": 10},

    # vp_c2_s3 - دعم المعلمين الجدد
    {"id": "vp_c2_s3_r001", "subcategory_id": "vp_c2_s3", "name": "تقرير برنامج دعم المعلمين الجدد", "order": 1},
    {"id": "vp_c2_s3_r002", "subcategory_id": "vp_c2_s3", "name": "سجل توجيه المعلمين الجدد من قبل مرشدين", "order": 2},
    {"id": "vp_c2_s3_r003", "subcategory_id": "vp_c2_s3", "name": "تقرير عن أثر الإرشاد على أداء المعلمين الجدد", "order": 3},
    {"id": "vp_c2_s3_r004", "subcategory_id": "vp_c2_s3", "name": "سجل زيارات صفية للمعلمين الجدد وتغذية راجعة", "order": 4},
    {"id": "vp_c2_s3_r005", "subcategory_id": "vp_c2_s3", "name": "تقرير عن احتياجات المعلمين الجدد التدريبية", "order": 5},
    {"id": "vp_c2_s3_r006", "subcategory_id": "vp_c2_s3", "name": "سجل مشاركة المعلمين الجدد في مجتمعات التعلم", "order": 6},
    {"id": "vp_c2_s3_r007", "subcategory_id": "vp_c2_s3", "name": "تقرير عن استقرار المعلمين الجدد واندماجهم", "order": 7},
    {"id": "vp_c2_s3_r008", "subcategory_id": "vp_c2_s3", "name": "سجل ورش عمل تعريفية باللوائح للمعلمين الجدد", "order": 8},
    {"id": "vp_c2_s3_r009", "subcategory_id": "vp_c2_s3", "name": "تقرير عن توفير دليل المعلم الجديد", "order": 9},
    {"id": "vp_c2_s3_r010", "subcategory_id": "vp_c2_s3", "name": "سجل تقييم برنامج دعم المعلمين الجدد", "order": 10},

    # vp_c2_s4 - تبادل الخبرات المهنية
    {"id": "vp_c2_s4_r001", "subcategory_id": "vp_c2_s4", "name": "تقرير عن تنظيم لقاءات تبادل الخبرات", "order": 1},
    {"id": "vp_c2_s4_r002", "subcategory_id": "vp_c2_s4", "name": "سجل نقل التجارب الناجحة بين المعلمين", "order": 2},
    {"id": "vp_c2_s4_r003", "subcategory_id": "vp_c2_s4", "name": "تقرير عن أثر تبادل الخبرات على الممارسات الصفية", "order": 3},
    {"id": "vp_c2_s4_r004", "subcategory_id": "vp_c2_s4", "name": "سجل زيارات تبادلية بين المعلمين", "order": 4},
    {"id": "vp_c2_s4_r005", "subcategory_id": "vp_c2_s4", "name": "تقرير عن إنشاء بنك خبرات مدرسي", "order": 5},
    {"id": "vp_c2_s4_r006", "subcategory_id": "vp_c2_s4", "name": "سجل مشاركة المعلمين في المنتديات المهنية", "order": 6},
    {"id": "vp_c2_s4_r007", "subcategory_id": "vp_c2_s4", "name": "تقرير عن تبادل الخبرات مع مدارس أخرى", "order": 7},
    {"id": "vp_c2_s4_r008", "subcategory_id": "vp_c2_s4", "name": "سجل الإشراف التشاركي بين المعلمين", "order": 8},
    {"id": "vp_c2_s4_r009", "subcategory_id": "vp_c2_s4", "name": "تقرير عن نشر قصص نجاح مهنية", "order": 9},
    {"id": "vp_c2_s4_r010", "subcategory_id": "vp_c2_s4", "name": "سجل تقييم فعالية تبادل الخبرات", "order": 10},

    # vp_c3_s1 - تفعيل قنوات الاتصال مع أولياء الأمور
    {"id": "vp_c3_s1_r001", "subcategory_id": "vp_c3_s1", "name": "تقرير عن قنوات التواصل المتاحة لأولياء الأمور", "order": 1},
    {"id": "vp_c3_s1_r002", "subcategory_id": "vp_c3_s1", "name": "سجل استخدام نظام نور للتواصل", "order": 2},
    {"id": "vp_c3_s1_r003", "subcategory_id": "vp_c3_s1", "name": "تقرير عن تفعيل مجموعات الواتساب الرسمية", "order": 3},
    {"id": "vp_c3_s1_r004", "subcategory_id": "vp_c3_s1", "name": "سجل البريد الإلكتروني للمراسلات مع أولياء الأمور", "order": 4},
    {"id": "vp_c3_s1_r005", "subcategory_id": "vp_c3_s1", "name": "تقرير عن استجابة المدرسة لاستفسارات أولياء الأمور", "order": 5},
    {"id": "vp_c3_s1_r006", "subcategory_id": "vp_c3_s1", "name": "سجل نشر أرقام التواصل مع الإدارة", "order": 6},
    {"id": "vp_c3_s1_r007", "subcategory_id": "vp_c3_s1", "name": "تقرير عن رضا أولياء الأمور عن قنوات الاتصال", "order": 7},
    {"id": "vp_c3_s1_r008", "subcategory_id": "vp_c3_s1", "name": "سجل تطوير قنوات التواصل بناءً على المقترحات", "order": 8},
    {"id": "vp_c3_s1_r009", "subcategory_id": "vp_c3_s1", "name": "تقرير عن استخدام الموقع الإلكتروني للتواصل", "order": 9},
    {"id": "vp_c3_s1_r010", "subcategory_id": "vp_c3_s1", "name": "سجل إشعارات أولياء الأمور بالفعاليات", "order": 10},

    # vp_c3_s2 - عقد الاجتماعات الدورية مع أولياء الأمور
    {"id": "vp_c3_s2_r001", "subcategory_id": "vp_c3_s2", "name": "تقرير عن اجتماعات مجلس الآباء", "order": 1},
    {"id": "vp_c3_s2_r002", "subcategory_id": "vp_c3_s2", "name": "سجل محاضر اجتماعات أولياء الأمور الدورية", "order": 2},
    {"id": "vp_c3_s2_r003", "subcategory_id": "vp_c3_s2", "name": "تقرير عن حضور أولياء الأمور للاجتماعات", "order": 3},
    {"id": "vp_c3_s2_r004", "subcategory_id": "vp_c3_s2", "name": "سجل جدولة الاجتماعات الفصلية", "order": 4},
    {"id": "vp_c3_s2_r005", "subcategory_id": "vp_c3_s2", "name": "تقرير عن موضوعات الاجتماعات وأهم التوصيات", "order": 5},
    {"id": "vp_c3_s2_r006", "subcategory_id": "vp_c3_s2", "name": "سجل تنظيم لقاءات افتراضية لأولياء الأمور", "order": 6},
    {"id": "vp_c3_s2_r007", "subcategory_id": "vp_c3_s2", "name": "تقرير عن متابعة تنفيذ توصيات الاجتماعات", "order": 7},
    {"id": "vp_c3_s2_r008", "subcategory_id": "vp_c3_s2", "name": "سجل مشاركة أولياء الأمور في وضع جدول الأعمال", "order": 8},
    {"id": "vp_c3_s2_r009", "subcategory_id": "vp_c3_s2", "name": "تقرير عن أثر الاجتماعات على تحسين العلاقة", "order": 9},
    {"id": "vp_c3_s2_r010", "subcategory_id": "vp_c3_s2", "name": "سجل تقييم أولياء الأمور للاجتماعات", "order": 10},

    # vp_c3_s3 - مناقشة أداء المتعلمين مع أولياء الأمور
    {"id": "vp_c3_s3_r001", "subcategory_id": "vp_c3_s3", "name": "تقرير عن لقاءات مناقشة نتائج الطلاب", "order": 1},
    {"id": "vp_c3_s3_r002", "subcategory_id": "vp_c3_s3", "name": "سجل تقارير أداء الطلاب المقدمة لأولياء الأمور", "order": 2},
    {"id": "vp_c3_s3_r003", "subcategory_id": "vp_c3_s3", "name": "تقرير عن اجتماعات خاصة للطلاب المتعثرين", "order": 3},
    {"id": "vp_c3_s3_r004", "subcategory_id": "vp_c3_s3", "name": "سجل توثيق ملاحظات أولياء الأمور حول الأداء", "order": 4},
    {"id": "vp_c3_s3_r005", "subcategory_id": "vp_c3_s3", "name": "تقرير عن خطط تحسين الأداء بالتشارك مع الأسرة", "order": 5},
    {"id": "vp_c3_s3_r006", "subcategory_id": "vp_c3_s3", "name": "سجل توزيع كشوف الدرجات ومناقشتها", "order": 6},
    {"id": "vp_c3_s3_r007", "subcategory_id": "vp_c3_s3", "name": "تقرير عن فعالية التواصل في تحسين نتائج الطلاب", "order": 7},
    {"id": "vp_c3_s3_r008", "subcategory_id": "vp_c3_s3", "name": "سجل توصيات أولياء الأمور لتحسين التعلم", "order": 8},
    {"id": "vp_c3_s3_r009", "subcategory_id": "vp_c3_s3", "name": "تقرير عن مستوى رضا أولياء الأمور عن أداء الأبناء", "order": 9},
    {"id": "vp_c3_s3_r010", "subcategory_id": "vp_c3_s3", "name": "سجل تطوير آليات مناقشة الأداء", "order": 10},

    # vp_c3_s4 - الاستجابة لملاحظات أولياء الأمور
    {"id": "vp_c3_s4_r001", "subcategory_id": "vp_c3_s4", "name": "تقرير عن نظام استقبال شكاوى وملاحظات أولياء الأمور", "order": 1},
    {"id": "vp_c3_s4_r002", "subcategory_id": "vp_c3_s4", "name": "سجل متابعة حل الشكاوى والردود", "order": 2},
    {"id": "vp_c3_s4_r003", "subcategory_id": "vp_c3_s4", "name": "تقرير عن متوسط زمن الاستجابة لملاحظات أولياء الأمور", "order": 3},
    {"id": "vp_c3_s4_r004", "subcategory_id": "vp_c3_s4", "name": "سجل استبيانات قياس رضا أولياء الأمور عن المعالجات", "order": 4},
    {"id": "vp_c3_s4_r005", "subcategory_id": "vp_c3_s4", "name": "تقرير عن أثر الاستجابة على تحسين الخدمات", "order": 5},
    {"id": "vp_c3_s4_r006", "subcategory_id": "vp_c3_s4", "name": "سجل تصنيف الملاحظات وفق الأولويات", "order": 6},
    {"id": "vp_c3_s4_r007", "subcategory_id": "vp_c3_s4", "name": "تقرير عن لجنة استماع أولياء الأمور", "order": 7},
    {"id": "vp_c3_s4_r008", "subcategory_id": "vp_c3_s4", "name": "سجل الإجراءات التصحيحية الناتجة عن الملاحظات", "order": 8},
    {"id": "vp_c3_s4_r009", "subcategory_id": "vp_c3_s4", "name": "تقرير عن نشر ثقافة تقبل الملاحظات", "order": 9},
    {"id": "vp_c3_s4_r010", "subcategory_id": "vp_c3_s4", "name": "سجل تطوير آليات الاستجابة", "order": 10},

    # vp_c4_s1 - إدارة المهام المتعددة بفعالية
    {"id": "vp_c4_s1_r001", "subcategory_id": "vp_c4_s1", "name": "تقرير عن تنظيم الأولويات اليومية للوكيل", "order": 1},
    {"id": "vp_c4_s1_r002", "subcategory_id": "vp_c4_s1", "name": "سجل استخدام أدوات إدارة المهام", "order": 2},
    {"id": "vp_c4_s1_r003", "subcategory_id": "vp_c4_s1", "name": "تقرير عن إنجاز المهام المتزامنة", "order": 3},
    {"id": "vp_c4_s1_r004", "subcategory_id": "vp_c4_s1", "name": "سجل تفويض المهام ومتابعة تنفيذها", "order": 4},
    {"id": "vp_c4_s1_r005", "subcategory_id": "vp_c4_s1", "name": "تقرير عن التعامل مع الطوارئ دون إخلال بالمهام", "order": 5},
    {"id": "vp_c4_s1_r006", "subcategory_id": "vp_c4_s1", "name": "سجل توزيع الوقت بين المهام الإدارية والفنية", "order": 6},
    {"id": "vp_c4_s1_r007", "subcategory_id": "vp_c4_s1", "name": "تقرير عن تحقيق التوازن في المسؤوليات", "order": 7},
    {"id": "vp_c4_s1_r008", "subcategory_id": "vp_c4_s1", "name": "سجل نماذج من خطط العمل الأسبوعية", "order": 8},
    {"id": "vp_c4_s1_r009", "subcategory_id": "vp_c4_s1", "name": "تقرير عن مدى إنجاز المهام في الوقت المحدد", "order": 9},
    {"id": "vp_c4_s1_r010", "subcategory_id": "vp_c4_s1", "name": "سجل تقييم كفاءة إدارة المهام", "order": 10},

    # vp_c4_s2 - معالجة المشكلات الإدارية
    {"id": "vp_c4_s2_r001", "subcategory_id": "vp_c4_s2", "name": "تقرير عن آليات اكتشاف المشكلات الإدارية", "order": 1},
    {"id": "vp_c4_s2_r002", "subcategory_id": "vp_c4_s2", "name": "سجل المشكلات الإدارية والإجراءات المتخذة", "order": 2},
    {"id": "vp_c4_s2_r003", "subcategory_id": "vp_c4_s2", "name": "تقرير عن تحليل أسباب المشكلات", "order": 3},
    {"id": "vp_c4_s2_r004", "subcategory_id": "vp_c4_s2", "name": "سجل اجتماعات فريق حل المشكلات", "order": 4},
    {"id": "vp_c4_s2_r005", "subcategory_id": "vp_c4_s2", "name": "تقرير عن تنفيذ الحلول وقياس فعاليتها", "order": 5},
    {"id": "vp_c4_s2_r006", "subcategory_id": "vp_c4_s2", "name": "سجل تدريب الموظفين على حل المشكلات", "order": 6},
    {"id": "vp_c4_s2_r007", "subcategory_id": "vp_c4_s2", "name": "تقرير عن تطوير سياسات للوقاية من المشكلات", "order": 7},
    {"id": "vp_c4_s2_r008", "subcategory_id": "vp_c4_s2", "name": "سجل التنسيق مع الجهات الخارجية لحل مشكلات", "order": 8},
    {"id": "vp_c4_s2_r009", "subcategory_id": "vp_c4_s2", "name": "تقرير عن مدى رضا المستفيدين بعد الحل", "order": 9},
    {"id": "vp_c4_s2_r010", "subcategory_id": "vp_c4_s2", "name": "سجل تحسين آليات معالجة المشكلات", "order": 10},

    # vp_c4_s3 - التكيف مع المتغيرات
    {"id": "vp_c4_s3_r001", "subcategory_id": "vp_c4_s3", "name": "تقرير عن التعامل مع التغييرات المفاجئة", "order": 1},
    {"id": "vp_c4_s3_r002", "subcategory_id": "vp_c4_s3", "name": "سجل مرونة الجداول في الظروف الطارئة", "order": 2},
    {"id": "vp_c4_s3_r003", "subcategory_id": "vp_c4_s3", "name": "تقرير عن تكيف المدرسة مع التعلم عن بعد", "order": 3},
    {"id": "vp_c4_s3_r004", "subcategory_id": "vp_c4_s3", "name": "سجل تحديث الخطط وفق المستجدات", "order": 4},
    {"id": "vp_c4_s3_r005", "subcategory_id": "vp_c4_s3", "name": "تقرير عن مرونة الموظفين في تنفيذ مهام جديدة", "order": 5},
    {"id": "vp_c4_s3_r006", "subcategory_id": "vp_c4_s3", "name": "سجل استجابة المدرسة للتعليمات المستجدة", "order": 6},
    {"id": "vp_c4_s3_r007", "subcategory_id": "vp_c4_s3", "name": "تقرير عن إدارة الأزمات", "order": 7},
    {"id": "vp_c4_s3_r008", "subcategory_id": "vp_c4_s3", "name": "سجل تدريبات التعامل مع المتغيرات", "order": 8},
    {"id": "vp_c4_s3_r009", "subcategory_id": "vp_c4_s3", "name": "تقرير عن أثر المرونة على استقرار العمل", "order": 9},
    {"id": "vp_c4_s3_r010", "subcategory_id": "vp_c4_s3", "name": "سجل تقييم جاهزية المدرسة للتغيرات", "order": 10},

    # vp_c5_s1 - دعم التجارب والمشروعات المتميزة
    {"id": "vp_c5_s1_r001", "subcategory_id": "vp_c5_s1", "name": "تقرير عن حصر التجارب المتميزة بالمدرسة", "order": 1},
    {"id": "vp_c5_s1_r002", "subcategory_id": "vp_c5_s1", "name": "سجل دعم المشروعات الإبداعية للمعلمين", "order": 2},
    {"id": "vp_c5_s1_r003", "subcategory_id": "vp_c5_s1", "name": "تقرير عن توفير موارد للمشروعات المتميزة", "order": 3},
    {"id": "vp_c5_s1_r004", "subcategory_id": "vp_c5_s1", "name": "سجل متابعة تنفيذ المشروعات", "order": 4},
    {"id": "vp_c5_s1_r005", "subcategory_id": "vp_c5_s1", "name": "تقرير عن أثر المشروعات على البيئة التعليمية", "order": 5},
    {"id": "vp_c5_s1_r006", "subcategory_id": "vp_c5_s1", "name": "سجل تحفيز أصحاب التجارب", "order": 6},
    {"id": "vp_c5_s1_r007", "subcategory_id": "vp_c5_s1", "name": "تقرير عن مشاركة التجارب في المعارض", "order": 7},
    {"id": "vp_c5_s1_r008", "subcategory_id": "vp_c5_s1", "name": "سجل توثيق التجارب ونشرها", "order": 8},
    {"id": "vp_c5_s1_r009", "subcategory_id": "vp_c5_s1", "name": "تقرير عن استدامة المشروعات", "order": 9},
    {"id": "vp_c5_s1_r010", "subcategory_id": "vp_c5_s1", "name": "سجل تقييم دعم التجارب", "order": 10},

    # vp_c5_s2 - دراسة المبادرات الواردة من المدارس
    {"id": "vp_c5_s2_r001", "subcategory_id": "vp_c5_s2", "name": "تقرير عن استقبال المبادرات من المدارس الأخرى", "order": 1},
    {"id": "vp_c5_s2_r002", "subcategory_id": "vp_c5_s2", "name": "سجل تحليل المبادرات ومدى ملاءمتها", "order": 2},
    {"id": "vp_c5_s2_r003", "subcategory_id": "vp_c5_s2", "name": "تقرير عن اختيار المبادرات القابلة للتطبيق", "order": 3},
    {"id": "vp_c5_s2_r004", "subcategory_id": "vp_c5_s2", "name": "سجل فرق دراسة المبادرات", "order": 4},
    {"id": "vp_c5_s2_r005", "subcategory_id": "vp_c5_s2", "name": "تقرير عن تجارب مدارس أخرى تمت الاستفادة منها", "order": 5},
    {"id": "vp_c5_s2_r006", "subcategory_id": "vp_c5_s2", "name": "سجل تبادل الزيارات للاطلاع على المبادرات", "order": 6},
    {"id": "vp_c5_s2_r007", "subcategory_id": "vp_c5_s2", "name": "تقرير عن توثيق المبادرات المستفادة", "order": 7},
    {"id": "vp_c5_s2_r008", "subcategory_id": "vp_c5_s2", "name": "سجل تقييم أثر المبادرات المقتبسة", "order": 8},
    {"id": "vp_c5_s2_r009", "subcategory_id": "vp_c5_s2", "name": "تقرير عن نشر ثقافة دراسة المبادرات", "order": 9},
    {"id": "vp_c5_s2_r010", "subcategory_id": "vp_c5_s2", "name": "سجل تطوير آليات دراسة المبادرات", "order": 10},

    # vp_c5_s3 - إعداد تقارير للمشروعات القابلة للتطبيق
    {"id": "vp_c5_s3_r001", "subcategory_id": "vp_c5_s3", "name": "تقرير عن إعداد تقارير المشروعات المقترحة", "order": 1},
    {"id": "vp_c5_s3_r002", "subcategory_id": "vp_c5_s3", "name": "سجل نماذج تقارير المشروعات", "order": 2},
    {"id": "vp_c5_s3_r003", "subcategory_id": "vp_c5_s3", "name": "تقرير عن دراسة الجدوى للمشروعات", "order": 3},
    {"id": "vp_c5_s3_r004", "subcategory_id": "vp_c5_s3", "name": "سجل عرض المشروعات على القيادة", "order": 4},
    {"id": "vp_c5_s3_r005", "subcategory_id": "vp_c5_s3", "name": "تقرير عن أولويات تنفيذ المشروعات", "order": 5},
    {"id": "vp_c5_s3_r006", "subcategory_id": "vp_c5_s3", "name": "سجل متابعة الموافقات على المشروعات", "order": 6},
    {"id": "vp_c5_s3_r007", "subcategory_id": "vp_c5_s3", "name": "تقرير عن تخصيص ميزانية للمشروعات", "order": 7},
    {"id": "vp_c5_s3_r008", "subcategory_id": "vp_c5_s3", "name": "سجل تحسين التقارير بناءً على التغذية الراجعة", "order": 8},
    {"id": "vp_c5_s3_r009", "subcategory_id": "vp_c5_s3", "name": "تقرير عن أثر التقارير في اتخاذ القرار", "order": 9},
    {"id": "vp_c5_s3_r010", "subcategory_id": "vp_c5_s3", "name": "سجل تقييم جودة التقارير", "order": 10},

    # vp_c5_s4 - نشر التجارب المتميزة
    {"id": "vp_c5_s4_r001", "subcategory_id": "vp_c5_s4", "name": "تقرير عن نشر التجارب المتميزة عبر الإذاعة المدرسية", "order": 1},
    {"id": "vp_c5_s4_r002", "subcategory_id": "vp_c5_s4", "name": "سجل توزيع نشرات للتجارب الناجحة", "order": 2},
    {"id": "vp_c5_s4_r003", "subcategory_id": "vp_c5_s4", "name": "تقرير عن عرض التجارب في اجتماعات المعلمين", "order": 3},
    {"id": "vp_c5_s4_r004", "subcategory_id": "vp_c5_s4", "name": "سجل نشر التجارب على موقع المدرسة", "order": 4},
    {"id": "vp_c5_s4_r005", "subcategory_id": "vp_c5_s4", "name": "تقرير عن مشاركة التجارب مع مدارس أخرى", "order": 5},
    {"id": "vp_c5_s4_r006", "subcategory_id": "vp_c5_s4", "name": "سجل تنظيم يوم المهنة لعرض التجارب", "order": 6},
    {"id": "vp_c5_s4_r007", "subcategory_id": "vp_c5_s4", "name": "تقرير عن أثر النشر على تحفيز المعلمين", "order": 7},
    {"id": "vp_c5_s4_r008", "subcategory_id": "vp_c5_s4", "name": "سجل استفادة المعلمين من التجارب المنشورة", "order": 8},
    {"id": "vp_c5_s4_r009", "subcategory_id": "vp_c5_s4", "name": "تقرير عن تطوير آليات النشر", "order": 9},
    {"id": "vp_c5_s4_r010", "subcategory_id": "vp_c5_s4", "name": "سجل تقييم فاعلية نشر التجارب", "order": 10},

    # vp_c5_s5 - توظيف التقنية في المتابعة والنشر
    {"id": "vp_c5_s5_r001", "subcategory_id": "vp_c5_s5", "name": "تقرير عن استخدام المنصات لنشر التجارب", "order": 1},
    {"id": "vp_c5_s5_r002", "subcategory_id": "vp_c5_s5", "name": "سجل متابعة الأعمال عبر التطبيقات", "order": 2},
    {"id": "vp_c5_s5_r003", "subcategory_id": "vp_c5_s5", "name": "تقرير عن توظيف وسائل التواصل لنشر الإنجازات", "order": 3},
    {"id": "vp_c5_s5_r004", "subcategory_id": "vp_c5_s5", "name": "سجل إنشاء قنوات رقمية للمتابعة", "order": 4},
    {"id": "vp_c5_s5_r005", "subcategory_id": "vp_c5_s5", "name": "تقرير عن تدريب المعلمين على النشر الرقمي", "order": 5},
    {"id": "vp_c5_s5_r006", "subcategory_id": "vp_c5_s5", "name": "سجل استخدام البريد الجماعي للتواصل", "order": 6},
    {"id": "vp_c5_s5_r007", "subcategory_id": "vp_c5_s5", "name": "تقرير عن أثر التقنية في سرعة النشر", "order": 7},
    {"id": "vp_c5_s5_r008", "subcategory_id": "vp_c5_s5", "name": "سجل تطوير موقع المدرسة لعرض التجارب", "order": 8},
    {"id": "vp_c5_s5_r009", "subcategory_id": "vp_c5_s5", "name": "تقرير عن وصول المحتوى للمستفيدين", "order": 9},
    {"id": "vp_c5_s5_r010", "subcategory_id": "vp_c5_s5", "name": "سجل تقييم استخدام التقنية", "order": 10},

    # vp_c5_s6 - ابتكار حلول ومبادرات إبداعية
    {"id": "vp_c5_s6_r001", "subcategory_id": "vp_c5_s6", "name": "تقرير عن مسابقة الابتكار المدرسي", "order": 1},
    {"id": "vp_c5_s6_r002", "subcategory_id": "vp_c5_s6", "name": "سجل حصر المبادرات الإبداعية للمعلمين", "order": 2},
    {"id": "vp_c5_s6_r003", "subcategory_id": "vp_c5_s6", "name": "تقرير عن تنفيذ حلول مبتكرة لمشكلات مدرسية", "order": 3},
    {"id": "vp_c5_s6_r004", "subcategory_id": "vp_c5_s6", "name": "سجل ورش عمل التفكير الإبداعي", "order": 4},
    {"id": "vp_c5_s6_r005", "subcategory_id": "vp_c5_s6", "name": "تقرير عن أثر الابتكار على تحسين الأداء", "order": 5},
    {"id": "vp_c5_s6_r006", "subcategory_id": "vp_c5_s6", "name": "سجل تحفيز الإبداع لدى الطلاب", "order": 6},
    {"id": "vp_c5_s6_r007", "subcategory_id": "vp_c5_s6", "name": "تقرير عن شراكات لدعم الابتكار", "order": 7},
    {"id": "vp_c5_s6_r008", "subcategory_id": "vp_c5_s6", "name": "سجل توثيق المبادرات الإبداعية", "order": 8},
    {"id": "vp_c5_s6_r009", "subcategory_id": "vp_c5_s6", "name": "تقرير عن استدامة الابتكار", "order": 9},
    {"id": "vp_c5_s6_r010", "subcategory_id": "vp_c5_s6", "name": "سجل تقييم بيئة الابتكار بالمدرسة", "order": 10},

    # vp_c6_s1 - تطبيق قواعد السلوك والمواظبة
    {"id": "vp_c6_s1_r001", "subcategory_id": "vp_c6_s1", "name": "تقرير عن تطبيق قواعد السلوك والمواظبة", "order": 1},
    {"id": "vp_c6_s1_r002", "subcategory_id": "vp_c6_s1", "name": "سجل متابعة حالات الغياب", "order": 2},
    {"id": "vp_c6_s1_r003", "subcategory_id": "vp_c6_s1", "name": "تقرير عن المخالفات السلوكية والعقوبات", "order": 3},
    {"id": "vp_c6_s1_r004", "subcategory_id": "vp_c6_s1", "name": "سجل لجنة السلوك والمواظبة", "order": 4},
    {"id": "vp_c6_s1_r005", "subcategory_id": "vp_c6_s1", "name": "تقرير عن التوعية بقواعد السلوك", "order": 5},
    {"id": "vp_c6_s1_r006", "subcategory_id": "vp_c6_s1", "name": "سجل إنذارات الطلاب", "order": 6},
    {"id": "vp_c6_s1_r007", "subcategory_id": "vp_c6_s1", "name": "تقرير عن تحسن السلوك بعد التطبيق", "order": 7},
    {"id": "vp_c6_s1_r008", "subcategory_id": "vp_c6_s1", "name": "سجل تواصل مع أولياء الأمور بشأن السلوك", "order": 8},
    {"id": "vp_c6_s1_r009", "subcategory_id": "vp_c6_s1", "name": "تقرير عن تحديث قواعد السلوك", "order": 9},
    {"id": "vp_c6_s1_r010", "subcategory_id": "vp_c6_s1", "name": "سجل تقييم فعالية القواعد", "order": 10},

    # vp_c6_s2 - تنفيذ خطة الانضباط
    {"id": "vp_c6_s2_r001", "subcategory_id": "vp_c6_s2", "name": "تقرير عن خطة الانضباط المدرسي", "order": 1},
    {"id": "vp_c6_s2_r002", "subcategory_id": "vp_c6_s2", "name": "سجل متابعة تنفيذ الخطة", "order": 2},
    {"id": "vp_c6_s2_r003", "subcategory_id": "vp_c6_s2", "name": "تقرير عن نسب الانضباط الشهرية", "order": 3},
    {"id": "vp_c6_s2_r004", "subcategory_id": "vp_c6_s2", "name": "سجل مبادرات تحسين الانضباط", "order": 4},
    {"id": "vp_c6_s2_r005", "subcategory_id": "vp_c6_s2", "name": "تقرير عن دور المناوبين في الانضباط", "order": 5},
    {"id": "vp_c6_s2_r006", "subcategory_id": "vp_c6_s2", "name": "سجل حوافز الانضباط", "order": 6},
    {"id": "vp_c6_s2_r007", "subcategory_id": "vp_c6_s2", "name": "تقرير عن تكامل خطة الانضباط مع الخطط الأخرى", "order": 7},
    {"id": "vp_c6_s2_r008", "subcategory_id": "vp_c6_s2", "name": "سجل تحديث خطة الانضباط", "order": 8},
    {"id": "vp_c6_s2_r009", "subcategory_id": "vp_c6_s2", "name": "تقرير عن أثر الخطة على البيئة المدرسية", "order": 9},
    {"id": "vp_c6_s2_r010", "subcategory_id": "vp_c6_s2", "name": "سجل تقييم خطة الانضباط", "order": 10},

    # vp_c6_s3 - متابعة تقارير الالتزام
    {"id": "vp_c6_s3_r001", "subcategory_id": "vp_c6_s3", "name": "تقرير عن متابعة الالتزام بلوائح المدرسة", "order": 1},
    {"id": "vp_c6_s3_r002", "subcategory_id": "vp_c6_s3", "name": "سجل رصد حالات عدم الالتزام", "order": 2},
    {"id": "vp_c6_s3_r003", "subcategory_id": "vp_c6_s3", "name": "تقرير عن تحليل تقارير الالتزام", "order": 3},
    {"id": "vp_c6_s3_r004", "subcategory_id": "vp_c6_s3", "name": "سجل إشعارات غير الملتزمين", "order": 4},
    {"id": "vp_c6_s3_r005", "subcategory_id": "vp_c6_s3", "name": "تقرير عن التزام الطلاب بالزي المدرسي", "order": 5},
    {"id": "vp_c6_s3_r006", "subcategory_id": "vp_c6_s3", "name": "سجل متابعة الالتزام بالحضور المبكر", "order": 6},
    {"id": "vp_c6_s3_r007", "subcategory_id": "vp_c6_s3", "name": "تقرير عن مدى التزام المعلمين بالخطط", "order": 7},
    {"id": "vp_c6_s3_r008", "subcategory_id": "vp_c6_s3", "name": "سجل تحسين الالتزام", "order": 8},
    {"id": "vp_c6_s3_r009", "subcategory_id": "vp_c6_s3", "name": "تقرير عن أثر المتابعة على الالتزام", "order": 9},
    {"id": "vp_c6_s3_r010", "subcategory_id": "vp_c6_s3", "name": "سجل تطوير آليات المتابعة", "order": 10},

    # vp_c6_s4 - تعزيز السلوك الإيجابي
    {"id": "vp_c6_s4_r001", "subcategory_id": "vp_c6_s4", "name": "تقرير عن برامج تعزيز السلوك الإيجابي", "order": 1},
    {"id": "vp_c6_s4_r002", "subcategory_id": "vp_c6_s4", "name": "سجل تكريم الطلاب المتميزين سلوكياً", "order": 2},
    {"id": "vp_c6_s4_r003", "subcategory_id": "vp_c6_s4", "name": "تقرير عن أثر التعزيز على تحسن السلوك", "order": 3},
    {"id": "vp_c6_s4_r004", "subcategory_id": "vp_c6_s4", "name": "سجل لوحة شرف السلوك", "order": 4},
    {"id": "vp_c6_s4_r005", "subcategory_id": "vp_c6_s4", "name": "تقرير عن مبادرات الطلاب لتعزيز السلوك", "order": 5},
    {"id": "vp_c6_s4_r006", "subcategory_id": "vp_c6_s4", "name": "سجل ورش عمل عن القيم", "order": 6},
    {"id": "vp_c6_s4_r007", "subcategory_id": "vp_c6_s4", "name": "تقرير عن مشاركة أولياء الأمور في التعزيز", "order": 7},
    {"id": "vp_c6_s4_r008", "subcategory_id": "vp_c6_s4", "name": "سجل استدامة البرامج", "order": 8},
    {"id": "vp_c6_s4_r009", "subcategory_id": "vp_c6_s4", "name": "تقرير عن نشر ثقافة الإيجابية", "order": 9},
    {"id": "vp_c6_s4_r010", "subcategory_id": "vp_c6_s4", "name": "سجل تقييم برامج التعزيز", "order": 10},

    # vp_c7_s1 - توزيع المهام بعدالة
    {"id": "vp_c7_s1_r001", "subcategory_id": "vp_c7_s1", "name": "تقرير عن توزيع المهام بين الكادر", "order": 1},
    {"id": "vp_c7_s1_r002", "subcategory_id": "vp_c7_s1", "name": "سجل مراعاة الخبرات في التوزيع", "order": 2},
    {"id": "vp_c7_s1_r003", "subcategory_id": "vp_c7_s1", "name": "تقرير عن عدالة توزيع الجداول", "order": 3},
    {"id": "vp_c7_s1_r004", "subcategory_id": "vp_c7_s1", "name": "سجل استبيانات رضا الموظفين عن التوزيع", "order": 4},
    {"id": "vp_c7_s1_r005", "subcategory_id": "vp_c7_s1", "name": "تقرير عن توزيع حصص الاحتياط", "order": 5},
    {"id": "vp_c7_s1_r006", "subcategory_id": "vp_c7_s1", "name": "سجل تعديل التوزيع حسب الاحتياج", "order": 6},
    {"id": "vp_c7_s1_r007", "subcategory_id": "vp_c7_s1", "name": "تقرير عن كفاءة التوزيع في تحقيق الأهداف", "order": 7},
    {"id": "vp_c7_s1_r008", "subcategory_id": "vp_c7_s1", "name": "سجل متابعة تنفيذ المهام", "order": 8},
    {"id": "vp_c7_s1_r009", "subcategory_id": "vp_c7_s1", "name": "تقرير عن تطوير آليات التوزيع", "order": 9},
    {"id": "vp_c7_s1_r010", "subcategory_id": "vp_c7_s1", "name": "سجل تقييم العدالة التنظيمية", "order": 10},

    # vp_c7_s2 - إدارة الموارد المالية
    {"id": "vp_c7_s2_r001", "subcategory_id": "vp_c7_s2", "name": "تقرير عن إيرادات ومصروفات الصندوق المدرسي", "order": 1},
    {"id": "vp_c7_s2_r002", "subcategory_id": "vp_c7_s2", "name": "سجل متابعة الميزانية التشغيلية", "order": 2},
    {"id": "vp_c7_s2_r003", "subcategory_id": "vp_c7_s2", "name": "تقرير عن الالتزام باللوائح المالية", "order": 3},
    {"id": "vp_c7_s2_r004", "subcategory_id": "vp_c7_s2", "name": "سجل صرف المستحقات المالية", "order": 4},
    {"id": "vp_c7_s2_r005", "subcategory_id": "vp_c7_s2", "name": "تقرير عن ترشيد استهلاك الموارد", "order": 5},
    {"id": "vp_c7_s2_r006", "subcategory_id": "vp_c7_s2", "name": "سجل التدقيق الداخلي للحسابات", "order": 6},
    {"id": "vp_c7_s2_r007", "subcategory_id": "vp_c7_s2", "name": "تقرير عن أوجه الصرف", "order": 7},
    {"id": "vp_c7_s2_r008", "subcategory_id": "vp_c7_s2", "name": "سجل التخطيط المالي السنوي", "order": 8},
    {"id": "vp_c7_s2_r009", "subcategory_id": "vp_c7_s2", "name": "تقرير عن الشفافية في الإدارة المالية", "order": 9},
    {"id": "vp_c7_s2_r010", "subcategory_id": "vp_c7_s2", "name": "سجل تحسين الإجراءات المالية", "order": 10},

    # vp_c7_s3 - متابعة تقارير التدقيق
    {"id": "vp_c7_s3_r001", "subcategory_id": "vp_c7_s3", "name": "تقرير التدقيق الداخلي السنوي", "order": 1},
    {"id": "vp_c7_s3_r002", "subcategory_id": "vp_c7_s3", "name": "سجل متابعة توصيات التدقيق", "order": 2},
    {"id": "vp_c7_s3_r003", "subcategory_id": "vp_c7_s3", "name": "تقرير عن تنفيذ الإجراءات التصحيحية", "order": 3},
    {"id": "vp_c7_s3_r004", "subcategory_id": "vp_c7_s3", "name": "سجل مراجعة الإجراءات المالية", "order": 4},
    {"id": "vp_c7_s3_r005", "subcategory_id": "vp_c7_s3", "name": "تقرير عن مدى الالتزام بمعايير التدقيق", "order": 5},
    {"id": "vp_c7_s3_r006", "subcategory_id": "vp_c7_s3", "name": "سجل استجابة الإدارة لتقارير التدقيق", "order": 6},
    {"id": "vp_c7_s3_r007", "subcategory_id": "vp_c7_s3", "name": "تقرير عن تحسين الأداء المالي", "order": 7},
    {"id": "vp_c7_s3_r008", "subcategory_id": "vp_c7_s3", "name": "سجل تدقيق المخزون", "order": 8},
    {"id": "vp_c7_s3_r009", "subcategory_id": "vp_c7_s3", "name": "تقرير عن شفافية التقارير", "order": 9},
    {"id": "vp_c7_s3_r010", "subcategory_id": "vp_c7_s3", "name": "سجل تطوير نظام التدقيق", "order": 10},

    # vp_c8_s1 - إعداد خطة تطوير مهني
    {"id": "vp_c8_s1_r001", "subcategory_id": "vp_c8_s1", "name": "تقرير عن إعداد خطة التطوير المهني", "order": 1},
    {"id": "vp_c8_s1_r002", "subcategory_id": "vp_c8_s1", "name": "سجل مشاركة المعلمين في الخطة", "order": 2},
    {"id": "vp_c8_s1_r003", "subcategory_id": "vp_c8_s1", "name": "تقرير عن مواءمة الخطة مع الاحتياجات", "order": 3},
    {"id": "vp_c8_s1_r004", "subcategory_id": "vp_c8_s1", "name": "سجل اعتماد الخطة من القيادة", "order": 4},
    {"id": "vp_c8_s1_r005", "subcategory_id": "vp_c8_s1", "name": "تقرير عن ميزانية التطوير المهني", "order": 5},
    {"id": "vp_c8_s1_r006", "subcategory_id": "vp_c8_s1", "name": "سجل نشر الخطة", "order": 6},
    {"id": "vp_c8_s1_r007", "subcategory_id": "vp_c8_s1", "name": "تقرير عن تقييم الخطة", "order": 7},
    {"id": "vp_c8_s1_r008", "subcategory_id": "vp_c8_s1", "name": "سجل تحديث الخطة", "order": 8},
    {"id": "vp_c8_s1_r009", "subcategory_id": "vp_c8_s1", "name": "تقرير عن تحقيق أهداف الخطة", "order": 9},
    {"id": "vp_c8_s1_r010", "subcategory_id": "vp_c8_s1", "name": "سجل تحسين جودة الخطة", "order": 10},

    # vp_c8_s2 - حصر الاحتياجات التدريبية
    {"id": "vp_c8_s2_r001", "subcategory_id": "vp_c8_s2", "name": "تقرير عن حصر الاحتياجات التدريبية", "order": 1},
    {"id": "vp_c8_s2_r002", "subcategory_id": "vp_c8_s2", "name": "سجل استبيانات تحديد الاحتياجات", "order": 2},
    {"id": "vp_c8_s2_r003", "subcategory_id": "vp_c8_s2", "name": "تقرير عن تحليل الاحتياجات", "order": 3},
    {"id": "vp_c8_s2_r004", "subcategory_id": "vp_c8_s2", "name": "سجل أولويات التدريب", "order": 4},
    {"id": "vp_c8_s2_r005", "subcategory_id": "vp_c8_s2", "name": "تقرير عن مشاركة المعلمين في تحديد الاحتياجات", "order": 5},
    {"id": "vp_c8_s2_r006", "subcategory_id": "vp_c8_s2", "name": "سجل تحديث قائمة الاحتياجات", "order": 6},
    {"id": "vp_c8_s2_r007", "subcategory_id": "vp_c8_s2", "name": "تقرير عن ربط الاحتياجات بخطط التطوير", "order": 7},
    {"id": "vp_c8_s2_r008", "subcategory_id": "vp_c8_s2", "name": "سجل قاعدة بيانات الاحتياجات", "order": 8},
    {"id": "vp_c8_s2_r009", "subcategory_id": "vp_c8_s2", "name": "تقرير عن استجابة البرامج للاحتياجات", "order": 9},
    {"id": "vp_c8_s2_r010", "subcategory_id": "vp_c8_s2", "name": "سجل تحسين عملية الحصر", "order": 10},

    # vp_c8_s3 - متابعة الرخص المهنية
    {"id": "vp_c8_s3_r001", "subcategory_id": "vp_c8_s3", "name": "تقرير عن حصر الحاصلين على الرخصة المهنية", "order": 1},
    {"id": "vp_c8_s3_r002", "subcategory_id": "vp_c8_s3", "name": "سجل متابعة اجتياز المعلمين للرخص", "order": 2},
    {"id": "vp_c8_s3_r003", "subcategory_id": "vp_c8_s3", "name": "تقرير عن برامج دعم الحصول على الرخصة", "order": 3},
    {"id": "vp_c8_s3_r004", "subcategory_id": "vp_c8_s3", "name": "سجل تحفيز المعلمين للحصول على الرخصة", "order": 4},
    {"id": "vp_c8_s3_r005", "subcategory_id": "vp_c8_s3", "name": "تقرير عن نسب الحاصلين على الرخصة", "order": 5},
    {"id": "vp_c8_s3_r006", "subcategory_id": "vp_c8_s3", "name": "سجل توفير موارد تدريبية للرخصة", "order": 6},
    {"id": "vp_c8_s3_r007", "subcategory_id": "vp_c8_s3", "name": "تقرير عن أثر الرخصة على الأداء", "order": 7},
    {"id": "vp_c8_s3_r008", "subcategory_id": "vp_c8_s3", "name": "سجل مشاركة المدرسة في مبادرات الرخصة", "order": 8},
    {"id": "vp_c8_s3_r009", "subcategory_id": "vp_c8_s3", "name": "تقرير عن خطة زيادة الحاصلين", "order": 9},
    {"id": "vp_c8_s3_r010", "subcategory_id": "vp_c8_s3", "name": "سجل تقييم برامج الدعم", "order": 10},

    # vp_c8_s4 - نقل الخبرات بين المعلمين
    {"id": "vp_c8_s4_r001", "subcategory_id": "vp_c8_s4", "name": "تقرير عن نقل الخبرات بعد الدورات", "order": 1},
    {"id": "vp_c8_s4_r002", "subcategory_id": "vp_c8_s4", "name": "سجل ورش عمل من قبل معلمين", "order": 2},
    {"id": "vp_c8_s4_r003", "subcategory_id": "vp_c8_s4", "name": "تقرير عن أثر نقل الخبرة على الممارسات", "order": 3},
    {"id": "vp_c8_s4_r004", "subcategory_id": "vp_c8_s4", "name": "سجل لقاءات تبادل الخبرات", "order": 4},
    {"id": "vp_c8_s4_r005", "subcategory_id": "vp_c8_s4", "name": "تقرير عن تحفيز نقل الخبرة", "order": 5},
    {"id": "vp_c8_s4_r006", "subcategory_id": "vp_c8_s4", "name": "سجل متابعة تطبيق الخبرات المنقولة", "order": 6},
    {"id": "vp_c8_s4_r007", "subcategory_id": "vp_c8_s4", "name": "تقرير عن استدامة نقل الخبرة", "order": 7},
    {"id": "vp_c8_s4_r008", "subcategory_id": "vp_c8_s4", "name": "سجل مواد تدريبية منقولة", "order": 8},
    {"id": "vp_c8_s4_r009", "subcategory_id": "vp_c8_s4", "name": "تقرير عن نشر ثقافة نقل الخبرات", "order": 9},
    {"id": "vp_c8_s4_r010", "subcategory_id": "vp_c8_s4", "name": "سجل تقييم عملية نقل الخبرة", "order": 10},

    # vp_c9_s1 - مراجعة الأداء السابق
    {"id": "vp_c9_s1_r001", "subcategory_id": "vp_c9_s1", "name": "تقرير مراجعة أداء الفصل الماضي", "order": 1},
    {"id": "vp_c9_s1_r002", "subcategory_id": "vp_c9_s1", "name": "سجل تحليل مؤشرات الأداء السابقة", "order": 2},
    {"id": "vp_c9_s1_r003", "subcategory_id": "vp_c9_s1", "name": "تقرير عن الدروس المستفادة", "order": 3},
    {"id": "vp_c9_s1_r004", "subcategory_id": "vp_c9_s1", "name": "سجل اجتماعات مراجعة الأداء", "order": 4},
    {"id": "vp_c9_s1_r005", "subcategory_id": "vp_c9_s1", "name": "تقرير عن مقارنة الأداء بالعام السابق", "order": 5},
    {"id": "vp_c9_s1_r006", "subcategory_id": "vp_c9_s1", "name": "سجل توصيات تحسين الأداء", "order": 6},
    {"id": "vp_c9_s1_r007", "subcategory_id": "vp_c9_s1", "name": "تقرير عن تطور الأداء", "order": 7},
    {"id": "vp_c9_s1_r008", "subcategory_id": "vp_c9_s1", "name": "سجل تحديث خطط التحسين", "order": 8},
    {"id": "vp_c9_s1_r009", "subcategory_id": "vp_c9_s1", "name": "تقرير عن إنجاز الأهداف السابقة", "order": 9},
    {"id": "vp_c9_s1_r010", "subcategory_id": "vp_c9_s1", "name": "سجل تطوير آليات المراجعة", "order": 10},

    # vp_c9_s2 - قياس نسبة التقدم
    {"id": "vp_c9_s2_r001", "subcategory_id": "vp_c9_s2", "name": "تقرير قياس التقدم في مؤشرات الأداء", "order": 1},
    {"id": "vp_c9_s2_r002", "subcategory_id": "vp_c9_s2", "name": "سجل نسب إنجاز الخطط", "order": 2},
    {"id": "vp_c9_s2_r003", "subcategory_id": "vp_c9_s2", "name": "تقرير عن تحليل الفجوات", "order": 3},
    {"id": "vp_c9_s2_r004", "subcategory_id": "vp_c9_s2", "name": "سجل متابعة تحقيق المستهدفات", "order": 4},
    {"id": "vp_c9_s2_r005", "subcategory_id": "vp_c9_s2", "name": "تقرير عن مقارنة التقدم بالخطط الزمنية", "order": 5},
    {"id": "vp_c9_s2_r006", "subcategory_id": "vp_c9_s2", "name": "سجل تحديث مؤشرات القياس", "order": 6},
    {"id": "vp_c9_s2_r007", "subcategory_id": "vp_c9_s2", "name": "تقرير عن أدوات قياس التقدم", "order": 7},
    {"id": "vp_c9_s2_r008", "subcategory_id": "vp_c9_s2", "name": "سجل عرض نتائج القياس", "order": 8},
    {"id": "vp_c9_s2_r009", "subcategory_id": "vp_c9_s2", "name": "تقرير عن استجابة الخطط للتقدم", "order": 9},
    {"id": "vp_c9_s2_r010", "subcategory_id": "vp_c9_s2", "name": "سجل تحسين آليات القياس", "order": 10},

    # vp_c9_s3 - إزالة المعوقات
    {"id": "vp_c9_s3_r001", "subcategory_id": "vp_c9_s3", "name": "تقرير عن تحديد معوقات الأداء", "order": 1},
    {"id": "vp_c9_s3_r002", "subcategory_id": "vp_c9_s3", "name": "سجل إجراءات إزالة المعوقات", "order": 2},
    {"id": "vp_c9_s3_r003", "subcategory_id": "vp_c9_s3", "name": "تقرير عن أثر إزالة المعوقات على الأداء", "order": 3},
    {"id": "vp_c9_s3_r004", "subcategory_id": "vp_c9_s3", "name": "سجل اجتماعات حل المشكلات", "order": 4},
    {"id": "vp_c9_s3_r005", "subcategory_id": "vp_c9_s3", "name": "تقرير عن تحسين بيئة العمل", "order": 5},
    {"id": "vp_c9_s3_r006", "subcategory_id": "vp_c9_s3", "name": "سجل متابعة تنفيذ الحلول", "order": 6},
    {"id": "vp_c9_s3_r007", "subcategory_id": "vp_c9_s3", "name": "تقرير عن شراكات لإزالة المعوقات", "order": 7},
    {"id": "vp_c9_s3_r008", "subcategory_id": "vp_c9_s3", "name": "سجل استبيانات حول المعوقات", "order": 8},
    {"id": "vp_c9_s3_r009", "subcategory_id": "vp_c9_s3", "name": "تقرير عن استدامة الحلول", "order": 9},
    {"id": "vp_c9_s3_r010", "subcategory_id": "vp_c9_s3", "name": "سجل تطوير آليات إزالة المعوقات", "order": 10},

    # vp_c9_s4 - تعزيز السلوكيات الفعالة
    {"id": "vp_c9_s4_r001", "subcategory_id": "vp_c9_s4", "name": "تقرير عن تعزيز السلوكيات الإيجابية لدى الموظفين", "order": 1},
    {"id": "vp_c9_s4_r002", "subcategory_id": "vp_c9_s4", "name": "سجل حوافز للمعلمين المتميزين", "order": 2},
    {"id": "vp_c9_s4_r003", "subcategory_id": "vp_c9_s4", "name": "تقرير عن أثر التعزيز على الأداء", "order": 3},
    {"id": "vp_c9_s4_r004", "subcategory_id": "vp_c9_s4", "name": "سجل تكريم الموظفين", "order": 4},
    {"id": "vp_c9_s4_r005", "subcategory_id": "vp_c9_s4", "name": "تقرير عن نشر ثقافة الإبداع", "order": 5},
    {"id": "vp_c9_s4_r006", "subcategory_id": "vp_c9_s4", "name": "سجل قصص نجاح للموظفين", "order": 6},
    {"id": "vp_c9_s4_r007", "subcategory_id": "vp_c9_s4", "name": "تقرير عن استدامة السلوكيات الفعالة", "order": 7},
    {"id": "vp_c9_s4_r008", "subcategory_id": "vp_c9_s4", "name": "سجل تطوير نظام الحوافز", "order": 8},
    {"id": "vp_c9_s4_r009", "subcategory_id": "vp_c9_s4", "name": "تقرير عن مشاركة الموظفين في التحسين", "order": 9},
    {"id": "vp_c9_s4_r010", "subcategory_id": "vp_c9_s4", "name": "سجل تقييم برامج التعزيز", "order": 10},

    # vp_c10_s1 - تنفيذ برامج التطوير
    {"id": "vp_c10_s1_r001", "subcategory_id": "vp_c10_s1", "name": "تقرير عن تنفيذ برامج التطوير المهني", "order": 1},
    {"id": "vp_c10_s1_r002", "subcategory_id": "vp_c10_s1", "name": "سجل حضور المعلمين للبرامج", "order": 2},
    {"id": "vp_c10_s1_r003", "subcategory_id": "vp_c10_s1", "name": "تقرير عن جودة البرامج المنفذة", "order": 3},
    {"id": "vp_c10_s1_r004", "subcategory_id": "vp_c10_s1", "name": "سجل تنفيذ برامج داخلية", "order": 4},
    {"id": "vp_c10_s1_r005", "subcategory_id": "vp_c10_s1", "name": "تقرير عن توفير مدربين", "order": 5},
    {"id": "vp_c10_s1_r006", "subcategory_id": "vp_c10_s1", "name": "سجل متابعة تنفيذ البرامج", "order": 6},
    {"id": "vp_c10_s1_r007", "subcategory_id": "vp_c10_s1", "name": "تقرير عن استفادة المعلمين", "order": 7},
    {"id": "vp_c10_s1_r008", "subcategory_id": "vp_c10_s1", "name": "سجل تحديث البرامج", "order": 8},
    {"id": "vp_c10_s1_r009", "subcategory_id": "vp_c10_s1", "name": "تقرير عن تكامل البرامج مع الاحتياجات", "order": 9},
    {"id": "vp_c10_s1_r010", "subcategory_id": "vp_c10_s1", "name": "سجل تقييم تنفيذ البرامج", "order": 10},

    # vp_c10_s2 - قياس أثر التدريب
    {"id": "vp_c10_s2_r001", "subcategory_id": "vp_c10_s2", "name": "تقرير عن قياس أثر التدريب على الأداء", "order": 1},
    {"id": "vp_c10_s2_r002", "subcategory_id": "vp_c10_s2", "name": "سجل تحسين الأداء بعد التدريب", "order": 2},
    {"id": "vp_c10_s2_r003", "subcategory_id": "vp_c10_s2", "name": "تقرير عن أدوات قياس الأثر", "order": 3},
    {"id": "vp_c10_s2_r004", "subcategory_id": "vp_c10_s2", "name": "سجل متابعة تطبيق مخرجات التدريب", "order": 4},
    {"id": "vp_c10_s2_r005", "subcategory_id": "vp_c10_s2", "name": "تقرير عن عائد الاستثمار في التدريب", "order": 5},
    {"id": "vp_c10_s2_r006", "subcategory_id": "vp_c10_s2", "name": "سجل استبيانات قياس الأثر", "order": 6},
    {"id": "vp_c10_s2_r007", "subcategory_id": "vp_c10_s2", "name": "تقرير عن استدامة الأثر", "order": 7},
    {"id": "vp_c10_s2_r008", "subcategory_id": "vp_c10_s2", "name": "سجل تحسين البرامج بناءً على الأثر", "order": 8},
    {"id": "vp_c10_s2_r009", "subcategory_id": "vp_c10_s2", "name": "تقرير عن نشر نتائج القياس", "order": 9},
    {"id": "vp_c10_s2_r010", "subcategory_id": "vp_c10_s2", "name": "سجل تطوير آليات القياس", "order": 10},

    # vp_c10_s3 - إعداد ملفات الإنجاز
    {"id": "vp_c10_s3_r001", "subcategory_id": "vp_c10_s3", "name": "تقرير عن إعداد ملفات الإنجاز للمعلمين", "order": 1},
    {"id": "vp_c10_s3_r002", "subcategory_id": "vp_c10_s3", "name": "سجل تحديث ملفات الإنجاز", "order": 2},
    {"id": "vp_c10_s3_r003", "subcategory_id": "vp_c10_s3", "name": "تقرير عن توثيق الإنجازات", "order": 3},
    {"id": "vp_c10_s3_r004", "subcategory_id": "vp_c10_s3", "name": "سجل تدريب المعلمين على إعداد الملفات", "order": 4},
    {"id": "vp_c10_s3_r005", "subcategory_id": "vp_c10_s3", "name": "تقرير عن استخدام الملفات في التقويم", "order": 5},
    {"id": "vp_c10_s3_r006", "subcategory_id": "vp_c10_s3", "name": "سجل نماذج متميزة من الملفات", "order": 6},
    {"id": "vp_c10_s3_r007", "subcategory_id": "vp_c10_s3", "name": "تقرير عن جودة ملفات الإنجاز", "order": 7},
    {"id": "vp_c10_s3_r008", "subcategory_id": "vp_c10_s3", "name": "سجل تحسين ملفات الإنجاز", "order": 8},
    {"id": "vp_c10_s3_r009", "subcategory_id": "vp_c10_s3", "name": "تقرير عن تكامل الملفات مع التطوير", "order": 9},
    {"id": "vp_c10_s3_r010", "subcategory_id": "vp_c10_s3", "name": "سجل تقييم ملفات الإنجاز", "order": 10},

    # vp_c10_s4 - متابعة تحسين الأداء
    {"id": "vp_c10_s4_r001", "subcategory_id": "vp_c10_s4", "name": "تقرير عن متابعة تحسين أداء المعلمين", "order": 1},
    {"id": "vp_c10_s4_r002", "subcategory_id": "vp_c10_s4", "name": "سجل خطط تحسين الأداء الفردية", "order": 2},
    {"id": "vp_c10_s4_r003", "subcategory_id": "vp_c10_s4", "name": "تقرير عن مؤشرات تحسن الأداء", "order": 3},
    {"id": "vp_c10_s4_r004", "subcategory_id": "vp_c10_s4", "name": "سجل زيارات متابعة", "order": 4},
    {"id": "vp_c10_s4_r005", "subcategory_id": "vp_c10_s4", "name": "تقرير عن أثر التطوير على الأداء", "order": 5},
    {"id": "vp_c10_s4_r006", "subcategory_id": "vp_c10_s4", "name": "سجل تغذية راجعة للمعلمين", "order": 6},
    {"id": "vp_c10_s4_r007", "subcategory_id": "vp_c10_s4", "name": "تقرير عن استدامة التحسين", "order": 7},
    {"id": "vp_c10_s4_r008", "subcategory_id": "vp_c10_s4", "name": "سجل تحسين آليات المتابعة", "order": 8},
    {"id": "vp_c10_s4_r009", "subcategory_id": "vp_c10_s4", "name": "تقرير عن مشاركة المعلمين في التحسين", "order": 9},
    {"id": "vp_c10_s4_r010", "subcategory_id": "vp_c10_s4", "name": "سجل تقييم تحسين الأداء", "order": 10},

    # vp_c11_s1 - تقويم أداء المرؤوسين بأساليب علمية
    {"id": "vp_c11_s1_r001", "subcategory_id": "vp_c11_s1", "name": "تقرير عن تطبيق أدوات التقويم العلمية", "order": 1},
    {"id": "vp_c11_s1_r002", "subcategory_id": "vp_c11_s1", "name": "سجل تقويم أداء المعلمين", "order": 2},
    {"id": "vp_c11_s1_r003", "subcategory_id": "vp_c11_s1", "name": "تقرير عن نتائج التقويم", "order": 3},
    {"id": "vp_c11_s1_r004", "subcategory_id": "vp_c11_s1", "name": "سجل تدريب المقومين", "order": 4},
    {"id": "vp_c11_s1_r005", "subcategory_id": "vp_c11_s1", "name": "تقرير عن معايير التقويم", "order": 5},
    {"id": "vp_c11_s1_r006", "subcategory_id": "vp_c11_s1", "name": "سجل موضوعية التقويم", "order": 6},
    {"id": "vp_c11_s1_r007", "subcategory_id": "vp_c11_s1", "name": "تقرير عن تحليل نتائج التقويم", "order": 7},
    {"id": "vp_c11_s1_r008", "subcategory_id": "vp_c11_s1", "name": "سجل تطوير أدوات التقويم", "order": 8},
    {"id": "vp_c11_s1_r009", "subcategory_id": "vp_c11_s1", "name": "تقرير عن رضا الموظفين عن التقويم", "order": 9},
    {"id": "vp_c11_s1_r010", "subcategory_id": "vp_c11_s1", "name": "سجل تقييم فاعلية التقويم", "order": 10},

    # vp_c11_s2 - استخدام أدوات تقويم متنوعة
    {"id": "vp_c11_s2_r001", "subcategory_id": "vp_c11_s2", "name": "تقرير عن تنوع أدوات التقويم", "order": 1},
    {"id": "vp_c11_s2_r002", "subcategory_id": "vp_c11_s2", "name": "سجل استخدام بطاقات الملاحظة", "order": 2},
    {"id": "vp_c11_s2_r003", "subcategory_id": "vp_c11_s2", "name": "تقرير عن تقويم الزملاء", "order": 3},
    {"id": "vp_c11_s2_r004", "subcategory_id": "vp_c11_s2", "name": "سجل التقويم الذاتي للمعلمين", "order": 4},
    {"id": "vp_c11_s2_r005", "subcategory_id": "vp_c11_s2", "name": "تقرير عن تقويم الأداء الإلكتروني", "order": 5},
    {"id": "vp_c11_s2_r006", "subcategory_id": "vp_c11_s2", "name": "سجل استبيانات الرضا الوظيفي", "order": 6},
    {"id": "vp_c11_s2_r007", "subcategory_id": "vp_c11_s2", "name": "تقرير عن تكامل الأدوات", "order": 7},
    {"id": "vp_c11_s2_r008", "subcategory_id": "vp_c11_s2", "name": "سجل تحديث الأدوات", "order": 8},
    {"id": "vp_c11_s2_r009", "subcategory_id": "vp_c11_s2", "name": "تقرير عن شمولية التقويم", "order": 9},
    {"id": "vp_c11_s2_r010", "subcategory_id": "vp_c11_s2", "name": "سجل تقييم فعالية الأدوات", "order": 10},

    # vp_c11_s3 - ملاحظة الأداء (تخطيط – تنفيذ – تقويم)
    {"id": "vp_c11_s3_r001", "subcategory_id": "vp_c11_s3", "name": "تقرير عن ملاحظة أداء المعلمين", "order": 1},
    {"id": "vp_c11_s3_r002", "subcategory_id": "vp_c11_s3", "name": "سجل زيارات صفية", "order": 2},
    {"id": "vp_c11_s3_r003", "subcategory_id": "vp_c11_s3", "name": "تقرير عن تقويم خطط الدروس", "order": 3},
    {"id": "vp_c11_s3_r004", "subcategory_id": "vp_c11_s3", "name": "سجل متابعة تنفيذ الدروس", "order": 4},
    {"id": "vp_c11_s3_r005", "subcategory_id": "vp_c11_s3", "name": "تقرير عن تقويم أداء الطلاب", "order": 5},
    {"id": "vp_c11_s3_r006", "subcategory_id": "vp_c11_s3", "name": "سجل تغذية راجعة للمعلمين", "order": 6},
    {"id": "vp_c11_s3_r007", "subcategory_id": "vp_c11_s3", "name": "تقرير عن أثر الملاحظة على التحسين", "order": 7},
    {"id": "vp_c11_s3_r008", "subcategory_id": "vp_c11_s3", "name": "سجل تطوير مهارات الملاحظة", "order": 8},
    {"id": "vp_c11_s3_r009", "subcategory_id": "vp_c11_s3", "name": "تقرير عن تكامل التخطيط والتنفيذ", "order": 9},
    {"id": "vp_c11_s3_r010", "subcategory_id": "vp_c11_s3", "name": "سجل تقييم جودة الملاحظة", "order": 10},

    # vp_c11_s4 - توظيف نتائج التقويم في تحسين الأداء
    {"id": "vp_c11_s4_r001", "subcategory_id": "vp_c11_s4", "name": "تقرير عن استخدام نتائج التقويم في التطوير", "order": 1},
    {"id": "vp_c11_s4_r002", "subcategory_id": "vp_c11_s4", "name": "سجل خطط تحسين الأداء بناءً على التقويم", "order": 2},
    {"id": "vp_c11_s4_r003", "subcategory_id": "vp_c11_s4", "name": "تقرير عن أثر توظيف النتائج", "order": 3},
    {"id": "vp_c11_s4_r004", "subcategory_id": "vp_c11_s4", "name": "سجل متابعة تحسين الأداء", "order": 4},
    {"id": "vp_c11_s4_r005", "subcategory_id": "vp_c11_s4", "name": "تقرير عن تحديد نقاط القوة والضعف", "order": 5},
    {"id": "vp_c11_s4_r006", "subcategory_id": "vp_c11_s4", "name": "سجل برامج تطويرية مبنية على التقويم", "order": 6},
    {"id": "vp_c11_s4_r007", "subcategory_id": "vp_c11_s4", "name": "تقرير عن استدامة التحسين", "order": 7},
    {"id": "vp_c11_s4_r008", "subcategory_id": "vp_c11_s4", "name": "سجل تحسين آليات توظيف النتائج", "order": 8},
    {"id": "vp_c11_s4_r009", "subcategory_id": "vp_c11_s4", "name": "تقرير عن مشاركة المعلمين في التحسين", "order": 9},
    {"id": "vp_c11_s4_r010", "subcategory_id": "vp_c11_s4", "name": "سجل تقييم فاعلية توظيف النتائج", "order": 10},

    # vp_c12_s1 - تشخيص أداء المتعلمين وتصنيفهم
    {"id": "vp_c12_s1_r001", "subcategory_id": "vp_c12_s1", "name": "تقرير عن تشخيص أداء الطلاب", "order": 1},
    {"id": "vp_c12_s1_r002", "subcategory_id": "vp_c12_s1", "name": "سجل تصنيف الطلاب حسب المستوى", "order": 2},
    {"id": "vp_c12_s1_r003", "subcategory_id": "vp_c12_s1", "name": "تقرير عن نتائج الاختبارات التشخيصية", "order": 3},
    {"id": "vp_c12_s1_r004", "subcategory_id": "vp_c12_s1", "name": "سجل تحديد الطلاب المتفوقين والمتعثرين", "order": 4},
    {"id": "vp_c12_s1_r005", "subcategory_id": "vp_c12_s1", "name": "تقرير عن تحليل الفجوات", "order": 5},
    {"id": "vp_c12_s1_r006", "subcategory_id": "vp_c12_s1", "name": "سجل استخدام أدوات التشخيص", "order": 6},
    {"id": "vp_c12_s1_r007", "subcategory_id": "vp_c12_s1", "name": "تقرير عن مشاركة المعلمين في التشخيص", "order": 7},
    {"id": "vp_c12_s1_r008", "subcategory_id": "vp_c12_s1", "name": "سجل تحديث تصنيف الطلاب", "order": 8},
    {"id": "vp_c12_s1_r009", "subcategory_id": "vp_c12_s1", "name": "تقرير عن دقة التشخيص", "order": 9},
    {"id": "vp_c12_s1_r010", "subcategory_id": "vp_c12_s1", "name": "سجل تطوير آليات التشخيص", "order": 10},

    # vp_c12_s2 - تحليل النتائج
    {"id": "vp_c12_s2_r001", "subcategory_id": "vp_c12_s2", "name": "تقرير تحليل نتائج الاختبارات", "order": 1},
    {"id": "vp_c12_s2_r002", "subcategory_id": "vp_c12_s2", "name": "سجل مقارنة النتائج بين الفصول", "order": 2},
    {"id": "vp_c12_s2_r003", "subcategory_id": "vp_c12_s2", "name": "تقرير عن تحليل نتائج المواد", "order": 3},
    {"id": "vp_c12_s2_r004", "subcategory_id": "vp_c12_s2", "name": "سجل مؤشرات أداء الطلاب", "order": 4},
    {"id": "vp_c12_s2_r005", "subcategory_id": "vp_c12_s2", "name": "تقرير عن تحليل نتائج الفصول السابقة", "order": 5},
    {"id": "vp_c12_s2_r006", "subcategory_id": "vp_c12_s2", "name": "سجل استخدام برامج تحليل البيانات", "order": 6},
    {"id": "vp_c12_s2_r007", "subcategory_id": "vp_c12_s2", "name": "تقرير عن نشر نتائج التحليل", "order": 7},
    {"id": "vp_c12_s2_r008", "subcategory_id": "vp_c12_s2", "name": "سجل توصيات التحليل", "order": 8},
    {"id": "vp_c12_s2_r009", "subcategory_id": "vp_c12_s2", "name": "تقرير عن تحديث خطط التعلم بناءً على التحليل", "order": 9},
    {"id": "vp_c12_s2_r010", "subcategory_id": "vp_c12_s2", "name": "سجل تحسين آليات التحليل", "order": 10},

    # vp_c12_s3 - تقديم معالجات تربوية
    {"id": "vp_c12_s3_r001", "subcategory_id": "vp_c12_s3", "name": "تقرير عن خطط علاجية للطلاب المتعثرين", "order": 1},
    {"id": "vp_c12_s3_r002", "subcategory_id": "vp_c12_s3", "name": "سجل تنفيذ برامج علاجية", "order": 2},
    {"id": "vp_c12_s3_r003", "subcategory_id": "vp_c12_s3", "name": "تقرير عن أثر المعالجات على التحصيل", "order": 3},
    {"id": "vp_c12_s3_r004", "subcategory_id": "vp_c12_s3", "name": "سجل متابعة تقدم الطلاب", "order": 4},
    {"id": "vp_c12_s3_r005", "subcategory_id": "vp_c12_s3", "name": "تقرير عن برامج إثرائية للمتفوقين", "order": 5},
    {"id": "vp_c12_s3_r006", "subcategory_id": "vp_c12_s3", "name": "سجل حصر الطلاب المستفيدين", "order": 6},
    {"id": "vp_c12_s3_r007", "subcategory_id": "vp_c12_s3", "name": "تقرير عن تكامل المعالجات مع المنهج", "order": 7},
    {"id": "vp_c12_s3_r008", "subcategory_id": "vp_c12_s3", "name": "سجل تحسين البرامج العلاجية", "order": 8},
    {"id": "vp_c12_s3_r009", "subcategory_id": "vp_c12_s3", "name": "تقرير عن استدامة التحسن", "order": 9},
    {"id": "vp_c12_s3_r010", "subcategory_id": "vp_c12_s3", "name": "سجل تقييم فاعلية المعالجات", "order": 10},

    # vp_c12_s4 - رصد نمو المتعلمين
    {"id": "vp_c12_s4_r001", "subcategory_id": "vp_c12_s4", "name": "تقرير عن رصد تطور أداء الطلاب", "order": 1},
    {"id": "vp_c12_s4_r002", "subcategory_id": "vp_c12_s4", "name": "سجل متابعة نمو المعارف والمهارات", "order": 2},
    {"id": "vp_c12_s4_r003", "subcategory_id": "vp_c12_s4", "name": "تقرير عن مقارنة أداء الطلاب بمراحل سابقة", "order": 3},
    {"id": "vp_c12_s4_r004", "subcategory_id": "vp_c12_s4", "name": "سجل توثيق نمو الطلاب", "order": 4},
    {"id": "vp_c12_s4_r005", "subcategory_id": "vp_c12_s4", "name": "تقرير عن مؤشرات النمو", "order": 5},
    {"id": "vp_c12_s4_r006", "subcategory_id": "vp_c12_s4", "name": "سجل تحليل معدلات النمو", "order": 6},
    {"id": "vp_c12_s4_r007", "subcategory_id": "vp_c12_s4", "name": "تقرير عن أثر البرامج على النمو", "order": 7},
    {"id": "vp_c12_s4_r008", "subcategory_id": "vp_c12_s4", "name": "سجل مشاركة أولياء الأمور في رصد النمو", "order": 8},
    {"id": "vp_c12_s4_r009", "subcategory_id": "vp_c12_s4", "name": "تقرير عن استدامة النمو", "order": 9},
    {"id": "vp_c12_s4_r010", "subcategory_id": "vp_c12_s4", "name": "سجل تطوير آليات الرصد", "order": 10},

    # vp_c12_s5 - تطوير عمليات التعليم والتعلم
    {"id": "vp_c12_s5_r001", "subcategory_id": "vp_c12_s5", "name": "تقرير عن تطوير استراتيجيات التدريس", "order": 1},
    {"id": "vp_c12_s5_r002", "subcategory_id": "vp_c12_s5", "name": "سجل تنفيذ ورش عمل لتطوير التعليم", "order": 2},
    {"id": "vp_c12_s5_r003", "subcategory_id": "vp_c12_s5", "name": "تقرير عن أثر التطوير على نواتج التعلم", "order": 3},
    {"id": "vp_c12_s5_r004", "subcategory_id": "vp_c12_s5", "name": "سجل تحديث المناهج", "order": 4},
    {"id": "vp_c12_s5_r005", "subcategory_id": "vp_c12_s5", "name": "تقرير عن دمج التقنية في التعليم", "order": 5},
    {"id": "vp_c12_s5_r006", "subcategory_id": "vp_c12_s5", "name": "سجل تطوير أساليب التقويم", "order": 6},
    {"id": "vp_c12_s5_r007", "subcategory_id": "vp_c12_s5", "name": "تقرير عن مشاركة المعلمين في التطوير", "order": 7},
    {"id": "vp_c12_s5_r008", "subcategory_id": "vp_c12_s5", "name": "سجل تحسين البيئة الصفية", "order": 8},
    {"id": "vp_c12_s5_r009", "subcategory_id": "vp_c12_s5", "name": "تقرير عن استدامة التطوير", "order": 9},
    {"id": "vp_c12_s5_r010", "subcategory_id": "vp_c12_s5", "name": "سجل تقييم عمليات التطوير", "order": 10},

    # vp_c12_s6 - التواصل مع أولياء الأمور بشأن نتائج التعلم
    {"id": "vp_c12_s6_r001", "subcategory_id": "vp_c12_s6", "name": "تقرير عن إشعار أولياء الأمور بنتائج الطلاب", "order": 1},
    {"id": "vp_c12_s6_r002", "subcategory_id": "vp_c12_s6", "name": "سجل اجتماعات مناقشة النتائج مع أولياء الأمور", "order": 2},
    {"id": "vp_c12_s6_r003", "subcategory_id": "vp_c12_s6", "name": "تقرير عن أثر التواصل على تحسين التعلم", "order": 3},
    {"id": "vp_c12_s6_r004", "subcategory_id": "vp_c12_s6", "name": "سجل توصيات أولياء الأمور بشأن النتائج", "order": 4},
    {"id": "vp_c12_s6_r005", "subcategory_id": "vp_c12_s6", "name": "تقرير عن رضا أولياء الأمور عن متابعة التحصيل", "order": 5},
    {"id": "vp_c12_s6_r006", "subcategory_id": "vp_c12_s6", "name": "سجل تقارير دورية لأولياء الأمور", "order": 6},
    {"id": "vp_c12_s6_r007", "subcategory_id": "vp_c12_s6", "name": "تقرير عن قنوات التواصل المستخدمة", "order": 7},
    {"id": "vp_c12_s6_r008", "subcategory_id": "vp_c12_s6", "name": "سجل استجابة المدرسة لاستفسارات أولياء الأمور", "order": 8},
    {"id": "vp_c12_s6_r009", "subcategory_id": "vp_c12_s6", "name": "تقرير عن تحسين التواصل", "order": 9},
    {"id": "vp_c12_s6_r010", "subcategory_id": "vp_c12_s6", "name": "سجل تقييم فعالية التواصل", "order": 10},

    # vp_c13_s1 - بناء خطط تحسينية
    {"id": "vp_c13_s1_r001", "subcategory_id": "vp_c13_s1", "name": "تقرير عن إعداد خطط تحسين الأداء", "order": 1},
    {"id": "vp_c13_s1_r002", "subcategory_id": "vp_c13_s1", "name": "سجل مشاركة المعنيين في بناء الخطط", "order": 2},
    {"id": "vp_c13_s1_r003", "subcategory_id": "vp_c13_s1", "name": "تقرير عن تحليل الواقع لتحديد مجالات التحسين", "order": 3},
    {"id": "vp_c13_s1_r004", "subcategory_id": "vp_c13_s1", "name": "سجل اعتماد الخطط", "order": 4},
    {"id": "vp_c13_s1_r005", "subcategory_id": "vp_c13_s1", "name": "تقرير عن مؤشرات قياس التحسين", "order": 5},
    {"id": "vp_c13_s1_r006", "subcategory_id": "vp_c13_s1", "name": "سجل توافق الخطط مع رؤية المدرسة", "order": 6},
    {"id": "vp_c13_s1_r007", "subcategory_id": "vp_c13_s1", "name": "تقرير عن تحديث الخطط", "order": 7},
    {"id": "vp_c13_s1_r008", "subcategory_id": "vp_c13_s1", "name": "سجل تخصيص موارد للتحسين", "order": 8},
    {"id": "vp_c13_s1_r009", "subcategory_id": "vp_c13_s1", "name": "تقرير عن جودة الخطط", "order": 9},
    {"id": "vp_c13_s1_r010", "subcategory_id": "vp_c13_s1", "name": "سجل تحسين إعداد الخطط", "order": 10},

    # vp_c13_s2 - متابعة مؤشرات الأداء
    {"id": "vp_c13_s2_r001", "subcategory_id": "vp_c13_s2", "name": "تقرير عن متابعة مؤشرات الأداء الرئيسية", "order": 1},
    {"id": "vp_c13_s2_r002", "subcategory_id": "vp_c13_s2", "name": "سجل قياس مؤشرات التحصيل", "order": 2},
    {"id": "vp_c13_s2_r003", "subcategory_id": "vp_c13_s2", "name": "تقرير عن تحليل مؤشرات الانضباط", "order": 3},
    {"id": "vp_c13_s2_r004", "subcategory_id": "vp_c13_s2", "name": "سجل متابعة مؤشرات رضا المستفيدين", "order": 4},
    {"id": "vp_c13_s2_r005", "subcategory_id": "vp_c13_s2", "name": "تقرير عن تحديث المؤشرات", "order": 5},
    {"id": "vp_c13_s2_r006", "subcategory_id": "vp_c13_s2", "name": "سجل استخدام المؤشرات في اتخاذ القرار", "order": 6},
    {"id": "vp_c13_s2_r007", "subcategory_id": "vp_c13_s2", "name": "تقرير عن نشر المؤشرات", "order": 7},
    {"id": "vp_c13_s2_r008", "subcategory_id": "vp_c13_s2", "name": "سجل تطوير آليات القياس", "order": 8},
    {"id": "vp_c13_s2_r009", "subcategory_id": "vp_c13_s2", "name": "تقرير عن استجابة الأداء للمؤشرات", "order": 9},
    {"id": "vp_c13_s2_r010", "subcategory_id": "vp_c13_s2", "name": "سجل تقييم فاعلية المؤشرات", "order": 10},

    # vp_c13_s3 - تعزيز الشراكات المجتمعية
    {"id": "vp_c13_s3_r001", "subcategory_id": "vp_c13_s3", "name": "تقرير عن الشراكات مع مؤسسات المجتمع", "order": 1},
    {"id": "vp_c13_s3_r002", "subcategory_id": "vp_c13_s3", "name": "سجل مبادرات الشراكة المجتمعية", "order": 2},
    {"id": "vp_c13_s3_r003", "subcategory_id": "vp_c13_s3", "name": "تقرير عن أثر الشراكات على أداء المدرسة", "order": 3},
    {"id": "vp_c13_s3_r004", "subcategory_id": "vp_c13_s3", "name": "سجل متابعة تنفيذ اتفاقيات الشراكة", "order": 4},
    {"id": "vp_c13_s3_r005", "subcategory_id": "vp_c13_s3", "name": "تقرير عن مشاركة أولياء الأمور في الأنشطة", "order": 5},
    {"id": "vp_c13_s3_r006", "subcategory_id": "vp_c13_s3", "name": "سجل استضافة خبراء من المجتمع", "order": 6},
    {"id": "vp_c13_s3_r007", "subcategory_id": "vp_c13_s3", "name": "تقرير عن استدامة الشراكات", "order": 7},
    {"id": "vp_c13_s3_r008", "subcategory_id": "vp_c13_s3", "name": "سجل تحسين الشراكات", "order": 8},
    {"id": "vp_c13_s3_r009", "subcategory_id": "vp_c13_s3", "name": "تقرير عن تكامل الشراكات مع خطط المدرسة", "order": 9},
    {"id": "vp_c13_s3_r010", "subcategory_id": "vp_c13_s3", "name": "سجل تقييم الشراكات", "order": 10},

    # vp_c14_s1 - إعداد الخطة التشغيلية
    {"id": "vp_c14_s1_r001", "subcategory_id": "vp_c14_s1", "name": "تقرير عن إعداد الخطة التشغيلية", "order": 1},
    {"id": "vp_c14_s1_r002", "subcategory_id": "vp_c14_s1", "name": "سجل مشاركة الأقسام في الخطة", "order": 2},
    {"id": "vp_c14_s1_r003", "subcategory_id": "vp_c14_s1", "name": "تقرير عن مواءمة الخطة مع الأهداف", "order": 3},
    {"id": "vp_c14_s1_r004", "subcategory_id": "vp_c14_s1", "name": "سجل اعتماد الخطة", "order": 4},
    {"id": "vp_c14_s1_r005", "subcategory_id": "vp_c14_s1", "name": "تقرير عن مؤشرات قياس الخطة", "order": 5},
    {"id": "vp_c14_s1_r006", "subcategory_id": "vp_c14_s1", "name": "سجل نشر الخطة", "order": 6},
    {"id": "vp_c14_s1_r007", "subcategory_id": "vp_c14_s1", "name": "تقرير عن تحديث الخطة", "order": 7},
    {"id": "vp_c14_s1_r008", "subcategory_id": "vp_c14_s1", "name": "سجل تقييم تنفيذ الخطة", "order": 8},
    {"id": "vp_c14_s1_r009", "subcategory_id": "vp_c14_s1", "name": "تقرير عن تحقيق أهداف الخطة", "order": 9},
    {"id": "vp_c14_s1_r010", "subcategory_id": "vp_c14_s1", "name": "سجل تحسين إعداد الخطة", "order": 10},

    # vp_c14_s2 - إعداد خطط بديلة
    {"id": "vp_c14_s2_r001", "subcategory_id": "vp_c14_s2", "name": "تقرير عن خطط بديلة للطوارئ", "order": 1},
    {"id": "vp_c14_s2_r002", "subcategory_id": "vp_c14_s2", "name": "سجل خطط بديلة لغياب المعلمين", "order": 2},
    {"id": "vp_c14_s2_r003", "subcategory_id": "vp_c14_s2", "name": "تقرير عن جاهزية الخطط البديلة", "order": 3},
    {"id": "vp_c14_s2_r004", "subcategory_id": "vp_c14_s2", "name": "سجل تفعيل الخطط البديلة", "order": 4},
    {"id": "vp_c14_s2_r005", "subcategory_id": "vp_c14_s2", "name": "تقرير عن مرونة الخطط", "order": 5},
    {"id": "vp_c14_s2_r006", "subcategory_id": "vp_c14_s2", "name": "سجل تحديث الخطط البديلة", "order": 6},
    {"id": "vp_c14_s2_r007", "subcategory_id": "vp_c14_s2", "name": "تقرير عن تدريب الموظفين على الخطط البديلة", "order": 7},
    {"id": "vp_c14_s2_r008", "subcategory_id": "vp_c14_s2", "name": "سجل تقييم فاعلية الخطط", "order": 8},
    {"id": "vp_c14_s2_r009", "subcategory_id": "vp_c14_s2", "name": "تقرير عن تكامل الخطط البديلة", "order": 9},
    {"id": "vp_c14_s2_r010", "subcategory_id": "vp_c14_s2", "name": "سجل تحسين إعداد الخطط البديلة", "order": 10},

    # vp_c14_s3 - إعداد خطط المخاطر والسلامة
    {"id": "vp_c14_s3_r001", "subcategory_id": "vp_c14_s3", "name": "تقرير عن خطة إدارة المخاطر", "order": 1},
    {"id": "vp_c14_s3_r002", "subcategory_id": "vp_c14_s3", "name": "سجل متابعة خطط الأمن والسلامة", "order": 2},
    {"id": "vp_c14_s3_r003", "subcategory_id": "vp_c14_s3", "name": "تقرير عن تجهيزات السلامة", "order": 3},
    {"id": "vp_c14_s3_r004", "subcategory_id": "vp_c14_s3", "name": "سجل تدريبات الإخلاء", "order": 4},
    {"id": "vp_c14_s3_r005", "subcategory_id": "vp_c14_s3", "name": "تقرير عن تحديد المخاطر المحتملة", "order": 5},
    {"id": "vp_c14_s3_r006", "subcategory_id": "vp_c14_s3", "name": "سجل تحديث خطط المخاطر", "order": 6},
    {"id": "vp_c14_s3_r007", "subcategory_id": "vp_c14_s3", "name": "تقرير عن الوعي بالسلامة", "order": 7},
    {"id": "vp_c14_s3_r008", "subcategory_id": "vp_c14_s3", "name": "سجل شراكات مع الدفاع المدني", "order": 8},
    {"id": "vp_c14_s3_r009", "subcategory_id": "vp_c14_s3", "name": "تقرير عن استجابة المدرسة للمخاطر", "order": 9},
    {"id": "vp_c14_s3_r010", "subcategory_id": "vp_c14_s3", "name": "سجل تقييم خطط السلامة", "order": 10},

    # vp_c15_s1 - متابعة تنفيذ الخطط
    {"id": "vp_c15_s1_r001", "subcategory_id": "vp_c15_s1", "name": "تقرير متابعة تنفيذ الخطط المدرسية", "order": 1},
    {"id": "vp_c15_s1_r002", "subcategory_id": "vp_c15_s1", "name": "سجل زيارات متابعة للخطط", "order": 2},
    {"id": "vp_c15_s1_r003", "subcategory_id": "vp_c15_s1", "name": "تقرير عن مدى التزام المنفذين", "order": 3},
    {"id": "vp_c15_s1_r004", "subcategory_id": "vp_c15_s1", "name": "سجل معوقات التنفيذ", "order": 4},
    {"id": "vp_c15_s1_r005", "subcategory_id": "vp_c15_s1", "name": "تقرير عن توفير الدعم أثناء التنفيذ", "order": 5},
    {"id": "vp_c15_s1_r006", "subcategory_id": "vp_c15_s1", "name": "سجل تحليل تقارير المتابعة", "order": 6},
    {"id": "vp_c15_s1_r007", "subcategory_id": "vp_c15_s1", "name": "تقرير عن تحديث الخطط بناءً على المتابعة", "order": 7},
    {"id": "vp_c15_s1_r008", "subcategory_id": "vp_c15_s1", "name": "سجل تحسين آليات المتابعة", "order": 8},
    {"id": "vp_c15_s1_r009", "subcategory_id": "vp_c15_s1", "name": "تقرير عن أثر المتابعة على الإنجاز", "order": 9},
    {"id": "vp_c15_s1_r010", "subcategory_id": "vp_c15_s1", "name": "سجل تقييم فاعلية المتابعة", "order": 10},

    # vp_c15_s2 - متابعة خطط المعلمين
    {"id": "vp_c15_s2_r001", "subcategory_id": "vp_c15_s2", "name": "تقرير عن متابعة خطط المعلمين", "order": 1},
    {"id": "vp_c15_s2_r002", "subcategory_id": "vp_c15_s2", "name": "سجل مراجعة خطط الدروس", "order": 2},
    {"id": "vp_c15_s2_r003", "subcategory_id": "vp_c15_s2", "name": "تقرير عن مدى التزام المعلمين بالخطط", "order": 3},
    {"id": "vp_c15_s2_r004", "subcategory_id": "vp_c15_s2", "name": "سجل تغذية راجعة حول خطط المعلمين", "order": 4},
    {"id": "vp_c15_s2_r005", "subcategory_id": "vp_c15_s2", "name": "تقرير عن تطوير خطط المعلمين", "order": 5},
    {"id": "vp_c15_s2_r006", "subcategory_id": "vp_c15_s2", "name": "سجل تكامل خطط المعلمين مع خطط المدرسة", "order": 6},
    {"id": "vp_c15_s2_r007", "subcategory_id": "vp_c15_s2", "name": "تقرير عن أثر المتابعة على أداء المعلمين", "order": 7},
    {"id": "vp_c15_s2_r008", "subcategory_id": "vp_c15_s2", "name": "سجل تحسين آليات متابعة المعلمين", "order": 8},
    {"id": "vp_c15_s2_r009", "subcategory_id": "vp_c15_s2", "name": "تقرير عن جودة خطط المعلمين", "order": 9},
    {"id": "vp_c15_s2_r010", "subcategory_id": "vp_c15_s2", "name": "سجل تقييم متابعة خطط المعلمين", "order": 10},

    # vp_c15_s3 - قياس أثر التنفيذ
    {"id": "vp_c15_s3_r001", "subcategory_id": "vp_c15_s3", "name": "تقرير عن قياس أثر تنفيذ الخطط", "order": 1},
    {"id": "vp_c15_s3_r002", "subcategory_id": "vp_c15_s3", "name": "سجل تحليل نتائج التنفيذ", "order": 2},
    {"id": "vp_c15_s3_r003", "subcategory_id": "vp_c15_s3", "name": "تقرير عن مؤشرات قياس الأثر", "order": 3},
    {"id": "vp_c15_s3_r004", "subcategory_id": "vp_c15_s3", "name": "سجل استبيانات قياس الأثر", "order": 4},
    {"id": "vp_c15_s3_r005", "subcategory_id": "vp_c15_s3", "name": "تقرير عن استدامة الأثر", "order": 5},
    {"id": "vp_c15_s3_r006", "subcategory_id": "vp_c15_s3", "name": "سجل تحسين الخطط بناءً على الأثر", "order": 6},
    {"id": "vp_c15_s3_r007", "subcategory_id": "vp_c15_s3", "name": "تقرير عن نشر نتائج قياس الأثر", "order": 7},
    {"id": "vp_c15_s3_r008", "subcategory_id": "vp_c15_s3", "name": "سجل تطوير أدوات القياس", "order": 8},
    {"id": "vp_c15_s3_r009", "subcategory_id": "vp_c15_s3", "name": "تقرير عن تكامل قياس الأثر", "order": 9},
    {"id": "vp_c15_s3_r010", "subcategory_id": "vp_c15_s3", "name": "سجل تقييم فاعلية القياس", "order": 10},

    # vp_c15_s4 - معالجة جوانب القصور
    {"id": "vp_c15_s4_r001", "subcategory_id": "vp_c15_s4", "name": "تقرير عن تحديد جوانب القصور في التنفيذ", "order": 1},
    {"id": "vp_c15_s4_r002", "subcategory_id": "vp_c15_s4", "name": "سجل إجراءات معالجة القصور", "order": 2},
    {"id": "vp_c15_s4_r003", "subcategory_id": "vp_c15_s4", "name": "تقرير عن أثر المعالجات على تحسين التنفيذ", "order": 3},
    {"id": "vp_c15_s4_r004", "subcategory_id": "vp_c15_s4", "name": "سجل متابعة تنفيذ المعالجات", "order": 4},
    {"id": "vp_c15_s4_r005", "subcategory_id": "vp_c15_s4", "name": "تقرير عن تحليل أسباب القصور", "order": 5},
    {"id": "vp_c15_s4_r006", "subcategory_id": "vp_c15_s4", "name": "سجل تحديث الخطط لمنع تكرار القصور", "order": 6},
    {"id": "vp_c15_s4_r007", "subcategory_id": "vp_c15_s4", "name": "تقرير عن مشاركة المعلمين في المعالجة", "order": 7},
    {"id": "vp_c15_s4_r008", "subcategory_id": "vp_c15_s4", "name": "سجل تحسين آليات المعالجة", "order": 8},
    {"id": "vp_c15_s4_r009", "subcategory_id": "vp_c15_s4", "name": "تقرير عن استدامة التحسين", "order": 9},
    {"id": "vp_c15_s4_r010", "subcategory_id": "vp_c15_s4", "name": "سجل تقييم فاعلية المعالجات", "order": 10},

    # vp_c16_s1 - دعم الأنشطة الصفية واللاصفية
    {"id": "vp_c16_s1_r001", "subcategory_id": "vp_c16_s1", "name": "تقرير عن دعم الأنشطة الصفية", "order": 1},
    {"id": "vp_c16_s1_r002", "subcategory_id": "vp_c16_s1", "name": "سجل توفير مواد للأنشطة اللاصفية", "order": 2},
    {"id": "vp_c16_s1_r003", "subcategory_id": "vp_c16_s1", "name": "تقرير عن مشاركة الطلاب في الأنشطة", "order": 3},
    {"id": "vp_c16_s1_r004", "subcategory_id": "vp_c16_s1", "name": "سجل حصر احتياجات الأنشطة", "order": 4},
    {"id": "vp_c16_s1_r005", "subcategory_id": "vp_c16_s1", "name": "تقرير عن أثر الأنشطة على التحصيل", "order": 5},
    {"id": "vp_c16_s1_r006", "subcategory_id": "vp_c16_s1", "name": "سجد تكريم الطلاب المتميزين في الأنشطة", "order": 6},
    {"id": "vp_c16_s1_r007", "subcategory_id": "vp_c16_s1", "name": "تقرير عن تنويع الأنشطة", "order": 7},
    {"id": "vp_c16_s1_r008", "subcategory_id": "vp_c16_s1", "name": "سجل تحسين الدعم المقدم", "order": 8},
    {"id": "vp_c16_s1_r009", "subcategory_id": "vp_c16_s1", "name": "تقرير عن استدامة الأنشطة", "order": 9},
    {"id": "vp_c16_s1_r010", "subcategory_id": "vp_c16_s1", "name": "سجل تقييم دعم الأنشطة", "order": 10},

    # vp_c16_s2 - دعم المشاركات الداخلية والخارجية
    {"id": "vp_c16_s2_r001", "subcategory_id": "vp_c16_s2", "name": "تقرير عن مشاركات الطلاب الداخلية", "order": 1},
    {"id": "vp_c16_s2_r002", "subcategory_id": "vp_c16_s2", "name": "سجل المشاركات الخارجية", "order": 2},
    {"id": "vp_c16_s2_r003", "subcategory_id": "vp_c16_s2", "name": "تقرير عن توفير الإمكانات للمشاركات", "order": 3},
    {"id": "vp_c16_s2_r004", "subcategory_id": "vp_c16_s2", "name": "سجل إنجازات الطلاب في المشاركات", "order": 4},
    {"id": "vp_c16_s2_r005", "subcategory_id": "vp_c16_s2", "name": "تقرير عن أثر المشاركات على شخصية الطالب", "order": 5},
    {"id": "vp_c16_s2_r006", "subcategory_id": "vp_c16_s2", "name": "سجل تحفيز الطلاب للمشاركة", "order": 6},
    {"id": "vp_c16_s2_r007", "subcategory_id": "vp_c16_s2", "name": "تقرير عن تذليل عقبات المشاركات", "order": 7},
    {"id": "vp_c16_s2_r008", "subcategory_id": "vp_c16_s2", "name": "سجل شراكات لدعم المشاركات", "order": 8},
    {"id": "vp_c16_s2_r009", "subcategory_id": "vp_c16_s2", "name": "تقرير عن استدامة المشاركات", "order": 9},
    {"id": "vp_c16_s2_r010", "subcategory_id": "vp_c16_s2", "name": "سجل تقييم دعم المشاركات", "order": 10},

    # vp_c16_s3 - توثيق الإنجازات الطلابية
    {"id": "vp_c16_s3_r001", "subcategory_id": "vp_c16_s3", "name": "تقرير عن توثيق إنجازات الطلاب", "order": 1},
    {"id": "vp_c16_s3_r002", "subcategory_id": "vp_c16_s3", "name": "سجل جوائز الطلاب", "order": 2},
    {"id": "vp_c16_s3_r003", "subcategory_id": "vp_c16_s3", "name": "تقرير عن نشر الإنجازات", "order": 3},
    {"id": "vp_c16_s3_r004", "subcategory_id": "vp_c16_s3", "name": "سجل تكريم الطلاب المتميزين", "order": 4},
    {"id": "vp_c16_s3_r005", "subcategory_id": "vp_c16_s3", "name": "تقرير عن أثر التوثيق على تحفيز الطلاب", "order": 5},
    {"id": "vp_c16_s3_r006", "subcategory_id": "vp_c16_s3", "name": "سجل إنشاء منصة لعرض الإنجازات", "order": 6},
    {"id": "vp_c16_s3_r007", "subcategory_id": "vp_c16_s3", "name": "تقرير عن تحديث سجل الإنجازات", "order": 7},
    {"id": "vp_c16_s3_r008", "subcategory_id": "vp_c16_s3", "name": "سجل تحسين آليات التوثيق", "order": 8},
    {"id": "vp_c16_s3_r009", "subcategory_id": "vp_c16_s3", "name": "تقرير عن مشاركة أولياء الأمور في التوثيق", "order": 9},
    {"id": "vp_c16_s3_r010", "subcategory_id": "vp_c16_s3", "name": "سجل تقييم فاعلية التوثيق", "order": 10},

    # vp_c17_s1 - متابعة استخدام المنصات
    {"id": "vp_c17_s1_r001", "subcategory_id": "vp_c17_s1", "name": "تقرير عن متابعة استخدام منصة مدرستي", "order": 1},
    {"id": "vp_c17_s1_r002", "subcategory_id": "vp_c17_s1", "name": "سجل حضور الطلاب عبر المنصات", "order": 2},
    {"id": "vp_c17_s1_r003", "subcategory_id": "vp_c17_s1", "name": "تقرير عن تفعيل المعلمين للمنصات", "order": 3},
    {"id": "vp_c17_s1_r004", "subcategory_id": "vp_c17_s1", "name": "سجل متابعة التفاعل الرقمي", "order": 4},
    {"id": "vp_c17_s1_r005", "subcategory_id": "vp_c17_s1", "name": "تقرير عن حل المشكلات التقنية", "order": 5},
    {"id": "vp_c17_s1_r006", "subcategory_id": "vp_c17_s1", "name": "سجل تدريب المعلمين على المنصات", "order": 6},
    {"id": "vp_c17_s1_r007", "subcategory_id": "vp_c17_s1", "name": "تقرير عن أثر المنصات على التعلم", "order": 7},
    {"id": "vp_c17_s1_r008", "subcategory_id": "vp_c17_s1", "name": "سجل تحسين استخدام المنصات", "order": 8},
    {"id": "vp_c17_s1_r009", "subcategory_id": "vp_c17_s1", "name": "تقرير عن تحديث المنصات", "order": 9},
    {"id": "vp_c17_s1_r010", "subcategory_id": "vp_c17_s1", "name": "سجل تقييم استخدام المنصات", "order": 10},

    # vp_c17_s2 - الالتزام بضوابط منصة مدرستي
    {"id": "vp_c17_s2_r001", "subcategory_id": "vp_c17_s2", "name": "تقرير عن التزام المعلمين بضوابط منصة مدرستي", "order": 1},
    {"id": "vp_c17_s2_r002", "subcategory_id": "vp_c17_s2", "name": "سجل متابعة التزام الطلاب بالضوابط", "order": 2},
    {"id": "vp_c17_s2_r003", "subcategory_id": "vp_c17_s2", "name": "تقرير عن الإجراءات تجاه المخالفين", "order": 3},
    {"id": "vp_c17_s2_r004", "subcategory_id": "vp_c17_s2", "name": "سجل توعية بالضوابط", "order": 4},
    {"id": "vp_c17_s2_r005", "subcategory_id": "vp_c17_s2", "name": "تقرير عن تحليل الالتزام", "order": 5},
    {"id": "vp_c17_s2_r006", "subcategory_id": "vp_c17_s2", "name": "سجل تحسين الالتزام", "order": 6},
    {"id": "vp_c17_s2_r007", "subcategory_id": "vp_c17_s2", "name": "تقرير عن أثر الالتزام على جودة التعليم", "order": 7},
    {"id": "vp_c17_s2_r008", "subcategory_id": "vp_c17_s2", "name": "سجل تطوير ضوابط المنصة", "order": 8},
    {"id": "vp_c17_s2_r009", "subcategory_id": "vp_c17_s2", "name": "تقرير عن رضا المستخدمين عن المنصة", "order": 9},
    {"id": "vp_c17_s2_r010", "subcategory_id": "vp_c17_s2", "name": "سجل تقييم الالتزام", "order": 10},

    # vp_c17_s3 - دعم التعليم الرقمي
    {"id": "vp_c17_s3_r001", "subcategory_id": "vp_c17_s3", "name": "تقرير عن دمج التقنية في الدروس", "order": 1},
    {"id": "vp_c17_s3_r002", "subcategory_id": "vp_c17_s3", "name": "سجل استخدام الأدوات الرقمية", "order": 2},
    {"id": "vp_c17_s3_r003", "subcategory_id": "vp_c17_s3", "name": "تقرير عن أثر التعليم الرقمي على التحصيل", "order": 3},
    {"id": "vp_c17_s3_r004", "subcategory_id": "vp_c17_s3", "name": "سجل تدريب الطلاب على المهارات الرقمية", "order": 4},
    {"id": "vp_c17_s3_r005", "subcategory_id": "vp_c17_s3", "name": "تقرير عن توفير بنية تحتية رقمية", "order": 5},
    {"id": "vp_c17_s3_r006", "subcategory_id": "vp_c17_s3", "name": "سجل مبادرات التعليم الرقمي", "order": 6},
    {"id": "vp_c17_s3_r007", "subcategory_id": "vp_c17_s3", "name": "تقرير عن تحسين المحتوى الرقمي", "order": 7},
    {"id": "vp_c17_s3_r008", "subcategory_id": "vp_c17_s3", "name": "سجل تحديث الأجهزة", "order": 8},
    {"id": "vp_c17_s3_r009", "subcategory_id": "vp_c17_s3", "name": "تقرير عن استدامة التعليم الرقمي", "order": 9},
    {"id": "vp_c17_s3_r010", "subcategory_id": "vp_c17_s3", "name": "سجل تقييم دعم التعليم الرقمي", "order": 10},

    # vp_c18_s1 - متابعة لجنة التوجيه الطلابي
    {"id": "vp_c18_s1_r001", "subcategory_id": "vp_c18_s1", "name": "تقرير عن متابعة أعمال لجنة التوجيه الطلابي", "order": 1},
    {"id": "vp_c18_s1_r002", "subcategory_id": "vp_c18_s1", "name": "سجل اجتماعات اللجنة", "order": 2},
    {"id": "vp_c18_s1_r003", "subcategory_id": "vp_c18_s1", "name": "تقرير عن برامج اللجنة لتعزيز السلوك", "order": 3},
    {"id": "vp_c18_s1_r004", "subcategory_id": "vp_c18_s1", "name": "سجل متابعة توصيات اللجنة", "order": 4},
    {"id": "vp_c18_s1_r005", "subcategory_id": "vp_c18_s1", "name": "تقرير عن أثر اللجنة على السلوك", "order": 5},
    {"id": "vp_c18_s1_r006", "subcategory_id": "vp_c18_s1", "name": "سجل تكامل اللجنة مع الإدارة", "order": 6},
    {"id": "vp_c18_s1_r007", "subcategory_id": "vp_c18_s1", "name": "تقرير عن تطوير أعمال اللجنة", "order": 7},
    {"id": "vp_c18_s1_r008", "subcategory_id": "vp_c18_s1", "name": "سجل تقييم أداء اللجنة", "order": 8},
    {"id": "vp_c18_s1_r009", "subcategory_id": "vp_c18_s1", "name": "تقرير عن مشاركة المعلمين في اللجنة", "order": 9},
    {"id": "vp_c18_s1_r010", "subcategory_id": "vp_c18_s1", "name": "سجل تحسين عمل اللجنة", "order": 10},

    # vp_c18_s2 - معالجة الحالات الفردية
    {"id": "vp_c18_s2_r001", "subcategory_id": "vp_c18_s2", "name": "تقرير عن متابعة الحالات الفردية للطلاب", "order": 1},
    {"id": "vp_c18_s2_r002", "subcategory_id": "vp_c18_s2", "name": "سجل جلسات الإرشاد الفردي", "order": 2},
    {"id": "vp_c18_s2_r003", "subcategory_id": "vp_c18_s2", "name": "تقرير عن تحسن سلوك الحالات", "order": 3},
    {"id": "vp_c18_s2_r004", "subcategory_id": "vp_c18_s2", "name": "سجل خطط علاجية فردية", "order": 4},
    {"id": "vp_c18_s2_r005", "subcategory_id": "vp_c18_s2", "name": "تقرير عن دور المرشد الطلابي", "order": 5},
    {"id": "vp_c18_s2_r006", "subcategory_id": "vp_c18_s2", "name": "سجل متابعة الحالات مع أولياء الأمور", "order": 6},
    {"id": "vp_c18_s2_r007", "subcategory_id": "vp_c18_s2", "name": "تقرير عن عدد الحالات المستهدفة", "order": 7},
    {"id": "vp_c18_s2_r008", "subcategory_id": "vp_c18_s2", "name": "سجل تقييم الإرشاد الفردي", "order": 8},
    {"id": "vp_c18_s2_r009", "subcategory_id": "vp_c18_s2", "name": "تقرير عن تطوير برامج التوجيه", "order": 9},
    {"id": "vp_c18_s2_r010", "subcategory_id": "vp_c18_s2", "name": "سجل تحسين آليات المتابعة", "order": 10},

    # vp_c18_s3 - تكريم الطلاب المتحسنين
    {"id": "vp_c18_s3_r001", "subcategory_id": "vp_c18_s3", "name": "تقرير عن تكريم الطلاب المتحسنين سلوكياً", "order": 1},
    {"id": "vp_c18_s3_r002", "subcategory_id": "vp_c18_s3", "name": "سجل حصر الطلاب المتحسنين", "order": 2},
    {"id": "vp_c18_s3_r003", "subcategory_id": "vp_c18_s3", "name": "تقرير عن فعاليات التكريم", "order": 3},
    {"id": "vp_c18_s3_r004", "subcategory_id": "vp_c18_s3", "name": "سجل أثر التكريم على الطلاب", "order": 4},
    {"id": "vp_c18_s3_r005", "subcategory_id": "vp_c18_s3", "name": "تقرير عن تحفيز الآخرين للتكريم", "order": 5},
    {"id": "vp_c18_s3_r006", "subcategory_id": "vp_c18_s3", "name": "سجل مشاركة أولياء الأمور في التكريم", "order": 6},
    {"id": "vp_c18_s3_r007", "subcategory_id": "vp_c18_s3", "name": "تقرير عن استمرارية التحسن بعد التكريم", "order": 7},
    {"id": "vp_c18_s3_r008", "subcategory_id": "vp_c18_s3", "name": "سجل شهادات التكريم", "order": 8},
    {"id": "vp_c18_s3_r009", "subcategory_id": "vp_c18_s3", "name": "تقرير عن تطوير نظام التكريم", "order": 9},
    {"id": "vp_c18_s3_r010", "subcategory_id": "vp_c18_s3", "name": "سجل تقييم فاعلية التكريم", "order": 10},

    # vp_c19_s1 - تطبيق معايير الأمن والسلامة
    {"id": "vp_c19_s1_r001", "subcategory_id": "vp_c19_s1", "name": "تقرير عن تطبيق معايير الأمن والسلامة", "order": 1},
    {"id": "vp_c19_s1_r002", "subcategory_id": "vp_c19_s1", "name": "سجل تجهيزات السلامة", "order": 2},
    {"id": "vp_c19_s1_r003", "subcategory_id": "vp_c19_s1", "name": "تقرير عن تدريبات الإخلاء", "order": 3},
    {"id": "vp_c19_s1_r004", "subcategory_id": "vp_c19_s1", "name": "سجل متابعة صيانة أجهزة السلامة", "order": 4},
    {"id": "vp_c19_s1_r005", "subcategory_id": "vp_c19_s1", "name": "تقرير عن الوعي بالسلامة", "order": 5},
    {"id": "vp_c19_s1_r006", "subcategory_id": "vp_c19_s1", "name": "سجل تقارير الدفاع المدني", "order": 6},
    {"id": "vp_c19_s1_r007", "subcategory_id": "vp_c19_s1", "name": "تقرير عن تحديث خطط السلامة", "order": 7},
    {"id": "vp_c19_s1_r008", "subcategory_id": "vp_c19_s1", "name": "سجل تحسين بيئة السلامة", "order": 8},
    {"id": "vp_c19_s1_r009", "subcategory_id": "vp_c19_s1", "name": "تقرير عن استجابة المدرسة للطوارئ", "order": 9},
    {"id": "vp_c19_s1_r010", "subcategory_id": "vp_c19_s1", "name": "سجل تقييم تطبيق السلامة", "order": 10},

    # vp_c19_s2 - متابعة البلاغات والأعطال
    {"id": "vp_c19_s2_r001", "subcategory_id": "vp_c19_s2", "name": "تقرير عن متابعة البلاغات الفنية", "order": 1},
    {"id": "vp_c19_s2_r002", "subcategory_id": "vp_c19_s2", "name": "سجل الأعطال وإصلاحها", "order": 2},
    {"id": "vp_c19_s2_r003", "subcategory_id": "vp_c19_s2", "name": "تقرير عن سرعة الاستجابة للبلاغات", "order": 3},
    {"id": "vp_c19_s2_r004", "subcategory_id": "vp_c19_s2", "name": "سجل تحليل الأعطال المتكررة", "order": 4},
    {"id": "vp_c19_s2_r005", "subcategory_id": "vp_c19_s2", "name": "تقرير عن رضا المستفيدين عن الصيانة", "order": 5},
    {"id": "vp_c19_s2_r006", "subcategory_id": "vp_c19_s2", "name": "سجل متابعة إنجاز الصيانة", "order": 6},
    {"id": "vp_c19_s2_r007", "subcategory_id": "vp_c19_s2", "name": "تقرير عن تحسين إجراءات البلاغات", "order": 7},
    {"id": "vp_c19_s2_r008", "subcategory_id": "vp_c19_s2", "name": "سجل تكامل البلاغات مع خطط الصيانة", "order": 8},
    {"id": "vp_c19_s2_r009", "subcategory_id": "vp_c19_s2", "name": "تقرير عن استدامة الخدمات", "order": 9},
    {"id": "vp_c19_s2_r010", "subcategory_id": "vp_c19_s2", "name": "سجل تقييم نظام البلاغات", "order": 10},

    # vp_c19_s3 - توفير بيئة جاذبة ومحفزة
    {"id": "vp_c19_s3_r001", "subcategory_id": "vp_c19_s3", "name": "تقرير عن تحسين البيئة المدرسية", "order": 1},
    {"id": "vp_c19_s3_r002", "subcategory_id": "vp_c19_s3", "name": "سجل توفير وسائل جذب للطلاب", "order": 2},
    {"id": "vp_c19_s3_r003", "subcategory_id": "vp_c19_s3", "name": "تقرير عن أثر البيئة على التحصيل", "order": 3},
    {"id": "vp_c19_s3_r004", "subcategory_id": "vp_c19_s3", "name": "سجل تجهيز الفصول", "order": 4},
    {"id": "vp_c19_s3_r005", "subcategory_id": "vp_c19_s3", "name": "تقرير عن تحفيز الطلاب", "order": 5},
    {"id": "vp_c19_s3_r006", "subcategory_id": "vp_c19_s3", "name": "سجل تحسين المرافق", "order": 6},
    {"id": "vp_c19_s3_r007", "subcategory_id": "vp_c19_s3", "name": "تقرير عن مشاركة الطلاب في تحسين البيئة", "order": 7},
    {"id": "vp_c19_s3_r008", "subcategory_id": "vp_c19_s3", "name": "سجل تطوير بيئة التعلم", "order": 8},
    {"id": "vp_c19_s3_r009", "subcategory_id": "vp_c19_s3", "name": "تقرير عن استدامة الجاذبية", "order": 9},
    {"id": "vp_c19_s3_r010", "subcategory_id": "vp_c19_s3", "name": "سجل تقييم البيئة المدرسية", "order": 10},
]
# vp_prompt.py (محدث)

VICE_PRINCIPAL_PROMPT_TEMPLATE = """أنت وكيل مدرسة، تمارس دورًا قياديًا تنفيذيًا يركز على تنظيم العمل المدرسي، ومتابعة تنفيذ الخطط، وضبط الانضباط، ودعم البيئة التعليمية بما يحقق كفاءة الأداء المدرسي.

المطلوب:
- عرض معيار الأداء الوظيفي.
- عرض التصنيف الفرعي.
- كتابة تقرير مهني متكامل يعكس الممارسات والإجراءات المرتبطة بهذا التصنيف، مع إبراز الجانب الإداري والتنفيذي.

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
- لغة إدارية رسمية دقيقة، تعكس طبيعة العمل التنفيذي والإشرافي.
- إبراز دور الوكيل في التنظيم، المتابعة، توزيع المهام، وضبط العمل.
- توضيح آليات التنفيذ والتوثيق والمتابعة.
- ربط الإجراءات بتحسين الانضباط المدرسي وجودة الأداء العام.
- الإشارة إلى التنسيق مع قائد المدرسة والمعلمين والجهات ذات العلاقة.
- إظهار أثر الممارسة على البيئة المدرسية وتحقيق مستهدفات المدرسة.
- تضمين جانب قياس الأثر والتحسين المستمر.
- صياغة عملية واقعية من 5–7 أسطر متماسكة لكل حقل.

نموذج توضيحي لدور الوكيل في التقرير:
1. تحسين الانضباط المدرسي ورفع كفاءة التنظيم الإداري بما ينعكس إيجابًا على استقرار البيئة التعليمية وجودة التعلم.
2. تنفيذ خطة تنظيمية لمتابعة الانضباط اليومي وتوزيع المهام الإشرافية بما يضمن سير اليوم الدراسي بسلاسة.
3. متابعة حضور الطلاب والمعلمين، وتنظيم جداول الإشراف، ومعالجة الملاحظات السلوكية فورًا، والتنسيق مع القيادة والمعلمين لضبط البيئة الصفية.
4. اعتماد المتابعة الميدانية المباشرة، وتحليل بيانات الغياب، والتواصل البناء مع المعلمين، وتفعيل الشراكة مع الأسرة.
5. المساهمة في تقليل التأخر الصباحي، وتحسين جاهزية الحصص، وتعزيز شعور الطلاب بالمسؤولية، ورفع التزام المعلمين بالخطة الزمنية.
6. تطوير أدوات تحليل البيانات لرصد أنماط الغياب، وتعزيز آليات التواصل الوقائي.
7. بناء لوحة مؤشرات أداء مدرسية دورية، وتكثيف اللقاءات التشاركية مع المعلمين، وتفعيل برامج توعوية للطلاب وأولياء الأمور.

**الحقول المطلوبة:**
1. الهدف الإداري
2. الإجراءات المنفذة
3. الاستراتيجيات المتبعة
4. النتائج
5. نقاط القوة
6. أولويات التطوير
7. خطة المتابعة

يرجى تقديم الإجابة باللغة العربية الفصحى، وتنظيمها بحيث يبدأ كل حقل برقمه فقط دون ذكر العنوان، مع مراعاة الترابط المنطقي بين الحقول.
"""