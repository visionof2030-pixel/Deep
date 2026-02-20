# activity_leader_prompt.py

# معايير رائد النشاط مع النسب المئوية
AL_CRITERIA = [
    {"id": "al_c1", "name": "أداء الواجبات الوظيفية", "weight": 10, "order": 1},
    {"id": "al_c2", "name": "التفاعل مع المجتمع المهني", "weight": 10, "order": 2},
    {"id": "al_c3", "name": "التفاعل مع أولياء الأمور", "weight": 10, "order": 3},
    {"id": "al_c4", "name": "التنويع في استراتيجيات التدريس", "weight": 5, "order": 4},
    {"id": "al_c5", "name": "تحسين نتائج المتعلمين", "weight": 5, "order": 5},
    {"id": "al_c6", "name": "إعداد وتنفيذ خطة التعلم", "weight": 5, "order": 6},
    {"id": "al_c7", "name": "توظيف تقنيات ووسائل التعلم المناسبة", "weight": 5, "order": 7},
    {"id": "al_c8", "name": "تهيئة البيئة التعليمية", "weight": 5, "order": 8},
    {"id": "al_c9", "name": "الإدارة الصفية", "weight": 5, "order": 9},
    {"id": "al_c10", "name": "تحليل نتائج المتعلمين وتشخيص مستوياتهم", "weight": 5, "order": 10},
    {"id": "al_c11", "name": "تنوع أساليب التقويم", "weight": 10, "order": 11},
    {"id": "al_c12", "name": "إعداد خطة مزمنة ومعتمدة لبرامج وفعاليات النشاط الطلابي", "weight": 10, "order": 12},
    {"id": "al_c13", "name": "تهيئة البيئة المدرسية للبرامج والأنشطة الطلابية", "weight": 5, "order": 13},
    {"id": "al_c14", "name": "يدعم المتعلمين وفق احتياجاتهم وميولهم للأنشطة", "weight": 5, "order": 14},
    {"id": "al_c15", "name": "يحفز المتعلمين على المشاركة في الأنشطة المدرسية", "weight": 10, "order": 15},
]

# التصنيفات الفرعية
AL_SUBCATEGORIES = [
    # ========== al_c1: أداء الواجبات الوظيفية ==========
    {"id": "al_c1_s1", "criterion_id": "al_c1", "name": "تطبيق الأنظمة وقواعد السلوك الوظيفي", "order": 1},
    {"id": "al_c1_s2", "criterion_id": "al_c1", "name": "حماية البيانات والمعلومات المهنية", "order": 2},
    {"id": "al_c1_s3", "criterion_id": "al_c1", "name": "التعاون مع المؤسسات الحكومية في المبادرات الوطنية", "order": 3},
    {"id": "al_c1_s4", "criterion_id": "al_c1", "name": "تنظيم أنشطة توعوية حول الانتماء الوطني", "order": 4},
    {"id": "al_c1_s5", "criterion_id": "al_c1", "name": "الامتثال للقوانين واللوائح وسياسات العمل", "order": 5},

    # ========== al_c2: التفاعل مع المجتمع المهني ==========
    {"id": "al_c2_s1", "criterion_id": "al_c2", "name": "حضور المؤتمرات والندوات التعليمية", "order": 1},
    {"id": "al_c2_s2", "criterion_id": "al_c2", "name": "المشاركة في ورش العمل التدريبية", "order": 2},
    {"id": "al_c2_s3", "criterion_id": "al_c2", "name": "الالتحاق ببرامج تدريبية لتعلم أساليب تدريس حديثة", "order": 3},
    {"id": "al_c2_s4", "criterion_id": "al_c2", "name": "الحصول على شهادات مهنية معتمدة", "order": 4},
    {"id": "al_c2_s5", "criterion_id": "al_c2", "name": "إطلاق مبادرات تعليمية لتحسين جودة التعليم", "order": 5},
    {"id": "al_c2_s6", "criterion_id": "al_c2", "name": "تقديم استشارات تربوية للمعلمين الجدد", "order": 6},
    {"id": "al_c2_s7", "criterion_id": "al_c2", "name": "تبادل الخبرات مع المعلمين من مدارس أخرى", "order": 7},
    {"id": "al_c2_s8", "criterion_id": "al_c2", "name": "التفكير الذاتي لتحسين الممارسات", "order": 8},

    # ========== al_c3: التفاعل مع أولياء الأمور ==========
    {"id": "al_c3_s1", "criterion_id": "al_c3", "name": "تنظيم اجتماعات دورية مع أولياء الأمور", "order": 1},
    {"id": "al_c3_s2", "criterion_id": "al_c3", "name": "إرسال تقارير منتظمة عن أداء الطلاب", "order": 2},
    {"id": "al_c3_s3", "criterion_id": "al_c3", "name": "استخدام وسائل التواصل الحديثة", "order": 3},
    {"id": "al_c3_s4", "criterion_id": "al_c3", "name": "الاستجابة لملاحظات ومخاوف أولياء الأمور", "order": 4},
    {"id": "al_c3_s5", "criterion_id": "al_c3", "name": "تشجيع أولياء الأمور على المشاركة في العملية التعليمية", "order": 5},

    # ========== al_c4: التنويع في استراتيجيات التدريس ==========
    {"id": "al_c4_s1", "criterion_id": "al_c4", "name": "استخدام التعلم النشط", "order": 1},
    {"id": "al_c4_s2", "criterion_id": "al_c4", "name": "تطبيق التعلم القائم على المشاريع", "order": 2},
    {"id": "al_c4_s3", "criterion_id": "al_c4", "name": "استخدام الوسائل البصرية والسمعية", "order": 3},
    {"id": "al_c4_s4", "criterion_id": "al_c4", "name": "تخصيص أنشطة تناسب أنماط التعلم المختلفة", "order": 4},

    # ========== al_c5: تحسين نتائج المتعلمين ==========
    {"id": "al_c5_s1", "criterion_id": "al_c5", "name": "تحديد أهداف ومعايير واضحة", "order": 1},
    {"id": "al_c5_s2", "criterion_id": "al_c5", "name": "تقديم إفادة سريعة ومحددة", "order": 2},
    {"id": "al_c5_s3", "criterion_id": "al_c5", "name": "تكييف الإفادة وفق الاحتياجات الفردية", "order": 3},
    {"id": "al_c5_s4", "criterion_id": "al_c5", "name": "تعزيز الثقة وتشجيع التطور", "order": 4},
    {"id": "al_c5_s5", "criterion_id": "al_c5", "name": "استخدام التكنولوجيا لتقديم الإفادة", "order": 5},

    # ========== al_c6: إعداد وتنفيذ خطة التعلم ==========
    {"id": "al_c6_s1", "criterion_id": "al_c6", "name": "وضع أهداف تعليمية واضحة وقابلة للقياس", "order": 1},
    {"id": "al_c6_s2", "criterion_id": "al_c6", "name": "تصميم خطط دراسية تتوافق مع المنهج", "order": 2},
    {"id": "al_c6_s3", "criterion_id": "al_c6", "name": "مراجعة الخطط بشكل دوري وتعديلها", "order": 3},
    {"id": "al_c6_s4", "criterion_id": "al_c6", "name": "مشاركة الخطط مع الزملاء", "order": 4},
    {"id": "al_c6_s5", "criterion_id": "al_c6", "name": "تفهم الخصائص النفسية للمرحلة العمرية", "order": 5},

    # ========== al_c7: توظيف تقنيات ووسائل التعلم المناسبة ==========
    {"id": "al_c7_s1", "criterion_id": "al_c7", "name": "استخدام السبورات الذكية والأجهزة اللوحية", "order": 1},
    {"id": "al_c7_s2", "criterion_id": "al_c7", "name": "تطبيق برامج التعلم الإلكتروني", "order": 2},
    {"id": "al_c7_s3", "criterion_id": "al_c7", "name": "تشجيع الطلاب على استخدام التطبيقات التعليمية", "order": 3},
    {"id": "al_c7_s4", "criterion_id": "al_c7", "name": "تنظيم ورش عمل حول استخدام التكنولوجيا", "order": 4},

    # ========== al_c8: تهيئة البيئة التعليمية ==========
    {"id": "al_c8_s1", "criterion_id": "al_c8", "name": "تزيين الفصل بوسائل تعليمية جذابة", "order": 1},
    {"id": "al_c8_s2", "criterion_id": "al_c8", "name": "تنظيم الفصل بشكل يسهل الحركة والتفاعل", "order": 2},
    {"id": "al_c8_s3", "criterion_id": "al_c8", "name": "توفير الأدوات والموارد التعليمية اللازمة", "order": 3},
    {"id": "al_c8_s4", "criterion_id": "al_c8", "name": "توفير بيئة آمنة وخالية من الأخطار", "order": 4},
    {"id": "al_c8_s5", "criterion_id": "al_c8", "name": "تمكين المتعلمين من التعبير عن أنفسهم", "order": 5},
    {"id": "al_c8_s6", "criterion_id": "al_c8", "name": "إثارة دافعية المتعلمين", "order": 6},

    # ========== al_c9: الإدارة الصفية ==========
    {"id": "al_c9_s1", "criterion_id": "al_c9", "name": "وضع قواعد واضحة للسلوك", "order": 1},
    {"id": "al_c9_s2", "criterion_id": "al_c9", "name": "استخدام أساليب تحفيزية", "order": 2},
    {"id": "al_c9_s3", "criterion_id": "al_c9", "name": "التعامل مع المشكلات السلوكية", "order": 3},
    {"id": "al_c9_s4", "criterion_id": "al_c9", "name": "تنظيم الوقت بشكل فعال", "order": 4},

    # ========== al_c10: تحليل نتائج المتعلمين وتشخيص مستوياتهم ==========
    {"id": "al_c10_s1", "criterion_id": "al_c10", "name": "استخدام اختبارات تقييمية دورية", "order": 1},
    {"id": "al_c10_s2", "criterion_id": "al_c10", "name": "تحليل النتائج لتحديد نقاط القوة والضعف", "order": 2},
    {"id": "al_c10_s3", "criterion_id": "al_c10", "name": "توفير تغذية راجعة فردية", "order": 3},
    {"id": "al_c10_s4", "criterion_id": "al_c10", "name": "تطبيق خطط علاجية", "order": 4},
    {"id": "al_c10_s5", "criterion_id": "al_c10", "name": "قياس التطبيق العملي للمعرفة", "order": 5},

    # ========== al_c11: تنوع أساليب التقويم ==========
    {"id": "al_c11_s1", "criterion_id": "al_c11", "name": "استخدام الاختبارات الكتابية والشفوية", "order": 1},
    {"id": "al_c11_s2", "criterion_id": "al_c11", "name": "تطبيق التقييم العملي", "order": 2},
    {"id": "al_c11_s3", "criterion_id": "al_c11", "name": "استخدام التقييم التكويني", "order": 3},
    {"id": "al_c11_s4", "criterion_id": "al_c11", "name": "استخدام التقويم القبلي", "order": 4},
    {"id": "al_c11_s5", "criterion_id": "al_c11", "name": "تطبيق التقويم الختامي", "order": 5},

    # ========== al_c12: إعداد خطة مزمنة ومعتمدة لبرامج وفعاليات النشاط الطلابي ==========
    {"id": "al_c12_s1", "criterion_id": "al_c12", "name": "تحليل الواقع الفعلي للمدرسة", "order": 1},
    {"id": "al_c12_s2", "criterion_id": "al_c12", "name": "تصميم خطة للبرامج مكتملة العناصر", "order": 2},
    {"id": "al_c12_s3", "criterion_id": "al_c12", "name": "قياس الأثر للبرامج والأنشطة", "order": 3},

    # ========== al_c13: تهيئة البيئة المدرسية للبرامج والأنشطة الطلابية ==========
    {"id": "al_c13_s1", "criterion_id": "al_c13", "name": "تنظيم وتجهيز البيئة بشكل آمن وفعال", "order": 1},

    # ========== al_c14: يدعم المتعلمين وفق احتياجاتهم وميولهم للأنشطة ==========
    {"id": "al_c14_s1", "criterion_id": "al_c14", "name": "حصر هوايات الطلاب", "order": 1},
    {"id": "al_c14_s2", "criterion_id": "al_c14", "name": "حصر إمكانيات المدرسة للأنشطة", "order": 2},
    {"id": "al_c14_s3", "criterion_id": "al_c14", "name": "البحث عن شراكات اجتماعية", "order": 3},
    {"id": "al_c14_s4", "criterion_id": "al_c14", "name": "توجيه الطلاب للأنشطة حسب ميولهم", "order": 4},
    {"id": "al_c14_s5", "criterion_id": "al_c14", "name": "تقديم تغذية راجعة للمتعلمين", "order": 5},

    # ========== al_c15: يحفز المتعلمين على المشاركة في الأنشطة المدرسية ==========
    {"id": "al_c15_s1", "criterion_id": "al_c15", "name": "تشجيع المشاركة في الأنشطة داخل المدرسة", "order": 1},
    {"id": "al_c15_s2", "criterion_id": "al_c15", "name": "تشجيع المشاركة في الأنشطة خارج المدرسة", "order": 2},
    {"id": "al_c15_s3", "criterion_id": "al_c15", "name": "تنمية قدرات الطلاب خارج المنهج", "order": 3},
    {"id": "al_c15_s4", "criterion_id": "al_c15", "name": "تعزيز قيم الطلاب خارج المنهج", "order": 4},
    {"id": "al_c15_s5", "criterion_id": "al_c15", "name": "تطوير مهارات الطلاب خارج المنهج", "order": 5},
    {"id": "al_c15_s6", "criterion_id": "al_c15", "name": "إثراء هوايات الطلاب خارج المنهج", "order": 6},
]

# التقارير (10 تقارير لكل تصنيف فرعي)
AL_REPORTS = [
    # ========== al_c1_s1 ==========
    {"id": "al_c1_s1_r001", "subcategory_id": "al_c1_s1", "name": "تقرير التزام رائد النشاط بالأنظمة الوظيفية", "order": 1},
    {"id": "al_c1_s1_r002", "subcategory_id": "al_c1_s1", "name": "سجل متابعة تطبيق قواعد السلوك الوظيفي", "order": 2},
    {"id": "al_c1_s1_r003", "subcategory_id": "al_c1_s1", "name": "توثيق الالتزام بأخلاقيات بيئة التعلم", "order": 3},
    {"id": "al_c1_s1_r004", "subcategory_id": "al_c1_s1", "name": "تقرير تعزيز الانضباط الوظيفي في الأنشطة", "order": 4},
    {"id": "al_c1_s1_r005", "subcategory_id": "al_c1_s1", "name": "سجل الإجراءات المتبعة لضمان الامتثال للوائح", "order": 5},
    {"id": "al_c1_s1_r006", "subcategory_id": "al_c1_s1", "name": "تقرير ورش عمل عن قواعد السلوك الوظيفي", "order": 6},
    {"id": "al_c1_s1_r007", "subcategory_id": "al_c1_s1", "name": "توثيق تطبيق اللوائح خلال الفعاليات", "order": 7},
    {"id": "al_c1_s1_r008", "subcategory_id": "al_c1_s1", "name": "تقرير تقييم الالتزام بالأنظمة", "order": 8},
    {"id": "al_c1_s1_r009", "subcategory_id": "al_c1_s1", "name": "سجل متابعة السلوك الوظيفي للفريق", "order": 9},
    {"id": "al_c1_s1_r010", "subcategory_id": "al_c1_s1", "name": "تقرير ختامي حول الامتثال الوظيفي", "order": 10},

    # ========== al_c1_s2 ==========
    {"id": "al_c1_s2_r001", "subcategory_id": "al_c1_s2", "name": "تقرير حماية بيانات الطلاب في الأنشطة", "order": 1},
    {"id": "al_c1_s2_r002", "subcategory_id": "al_c1_s2", "name": "سجل إجراءات أمن المعلومات", "order": 2},
    {"id": "al_c1_s2_r003", "subcategory_id": "al_c1_s2", "name": "توثيق سياسات الخصوصية المطبقة", "order": 3},
    {"id": "al_c1_s2_r004", "subcategory_id": "al_c1_s2", "name": "تقرير تدريب الفريق على حماية البيانات", "order": 4},
    {"id": "al_c1_s2_r005", "subcategory_id": "al_c1_s2", "name": "سجل مراجعة صلاحيات الوصول للمعلومات", "order": 5},
    {"id": "al_c1_s2_r006", "subcategory_id": "al_c1_s2", "name": "تقرير عن منع الوصول غير المصرح به", "order": 6},
    {"id": "al_c1_s2_r007", "subcategory_id": "al_c1_s2", "name": "توثيق التعامل مع المعلومات الحساسة", "order": 7},
    {"id": "al_c1_s2_r008", "subcategory_id": "al_c1_s2", "name": "تقرير تحديث بروتوكولات الأمان", "order": 8},
    {"id": "al_c1_s2_r009", "subcategory_id": "al_c1_s2", "name": "سجل التوعية بأمن المعلومات", "order": 9},
    {"id": "al_c1_s2_r010", "subcategory_id": "al_c1_s2", "name": "تقرير ختامي لحماية البيانات", "order": 10},

    # ========== al_c1_s3 ==========
    {"id": "al_c1_s3_r001", "subcategory_id": "al_c1_s3", "name": "تقرير التعاون مع المؤسسات الحكومية", "order": 1},
    {"id": "al_c1_s3_r002", "subcategory_id": "al_c1_s3", "name": "سجل المشاركة في المبادرات الوطنية", "order": 2},
    {"id": "al_c1_s3_r003", "subcategory_id": "al_c1_s3", "name": "توثيق الشراكات مع الجهات الرسمية", "order": 3},
    {"id": "al_c1_s3_r004", "subcategory_id": "al_c1_s3", "name": "تقرير فعالية وطنية بالتعاون مع الحكومة", "order": 4},
    {"id": "al_c1_s3_r005", "subcategory_id": "al_c1_s3", "name": "سجل اجتماعات التنسيق مع المؤسسات", "order": 5},
    {"id": "al_c1_s3_r006", "subcategory_id": "al_c1_s3", "name": "تقرير أثر المبادرات الوطنية على الطلاب", "order": 6},
    {"id": "al_c1_s3_r007", "subcategory_id": "al_c1_s3", "name": "توثيق حملات التوعية المشتركة", "order": 7},
    {"id": "al_c1_s3_r008", "subcategory_id": "al_c1_s3", "name": "تقرير مشاركة الطلاب في الفعاليات الحكومية", "order": 8},
    {"id": "al_c1_s3_r009", "subcategory_id": "al_c1_s3", "name": "سجل التقييم المشترك للمبادرات", "order": 9},
    {"id": "al_c1_s3_r010", "subcategory_id": "al_c1_s3", "name": "تقرير ختامي للتعاون الحكومي", "order": 10},

    # ========== al_c1_s4 ==========
    {"id": "al_c1_s4_r001", "subcategory_id": "al_c1_s4", "name": "تقرير تنظيم يوم الانتماء الوطني", "order": 1},
    {"id": "al_c1_s4_r002", "subcategory_id": "al_c1_s4", "name": "سجل أنشطة توعوية حول الوطنية", "order": 2},
    {"id": "al_c1_s4_r003", "subcategory_id": "al_c1_s4", "name": "توثيق فعاليات تعزيز الهوية", "order": 3},
    {"id": "al_c1_s4_r004", "subcategory_id": "al_c1_s4", "name": "تقرير مسابقات وطنية للطلاب", "order": 4},
    {"id": "al_c1_s4_r005", "subcategory_id": "al_c1_s4", "name": "سجل مشاركة الطلاب في الاحتفالات الوطنية", "order": 5},
    {"id": "al_c1_s4_r006", "subcategory_id": "al_c1_s4", "name": "تقرير ورش عمل عن المواطنة", "order": 6},
    {"id": "al_c1_s4_r007", "subcategory_id": "al_c1_s4", "name": "توثيق زيارات لمعالم وطنية", "order": 7},
    {"id": "al_c1_s4_r008", "subcategory_id": "al_c1_s4", "name": "تقرير أثر الأنشطة على الانتماء", "order": 8},
    {"id": "al_c1_s4_r009", "subcategory_id": "al_c1_s4", "name": "سجل إنتاج أعمال فنية وطنية", "order": 9},
    {"id": "al_c1_s4_r010", "subcategory_id": "al_c1_s4", "name": "تقرير ختامي للتوعية الوطنية", "order": 10},

    # ========== al_c1_s5 ==========
    {"id": "al_c1_s5_r001", "subcategory_id": "al_c1_s5", "name": "تقرير الامتثال للقوانين واللوائح", "order": 1},
    {"id": "al_c1_s5_r002", "subcategory_id": "al_c1_s5", "name": "سجل متابعة السياسات والإجراءات", "order": 2},
    {"id": "al_c1_s5_r003", "subcategory_id": "al_c1_s5", "name": "توثيق الالتزام باللوائح المحلية", "order": 3},
    {"id": "al_c1_s5_r004", "subcategory_id": "al_c1_s5", "name": "تقرير حول تطبيق المعايير الدولية", "order": 4},
    {"id": "al_c1_s5_r005", "subcategory_id": "al_c1_s5", "name": "سجل التدريب على السياسات الوظيفية", "order": 5},
    {"id": "al_c1_s5_r006", "subcategory_id": "al_c1_s5", "name": "تقرير مراجعة الامتثال في الأنشطة", "order": 6},
    {"id": "al_c1_s5_r007", "subcategory_id": "al_c1_s5", "name": "توثيق تحديث الإجراءات", "order": 7},
    {"id": "al_c1_s5_r008", "subcategory_id": "al_c1_s5", "name": "تقرير الالتزام بسياسات العمل", "order": 8},
    {"id": "al_c1_s5_r009", "subcategory_id": "al_c1_s5", "name": "سجل تقييم الامتثال", "order": 9},
    {"id": "al_c1_s5_r010", "subcategory_id": "al_c1_s5", "name": "تقرير ختامي للالتزام القانوني", "order": 10},

    # ========== al_c2_s1 ==========
    {"id": "al_c2_s1_r001", "subcategory_id": "al_c2_s1", "name": "تقرير حضور مؤتمر تربوي", "order": 1},
    {"id": "al_c2_s1_r002", "subcategory_id": "al_c2_s1", "name": "سجل المشاركة في ندوة تعليمية", "order": 2},
    {"id": "al_c2_s1_r003", "subcategory_id": "al_c2_s1", "name": "توثيق الاستفادة من المؤتمرات", "order": 3},
    {"id": "al_c2_s1_r004", "subcategory_id": "al_c2_s1", "name": "تقرير عن ورشة عمل في مؤتمر", "order": 4},
    {"id": "al_c2_s1_r005", "subcategory_id": "al_c2_s1", "name": "سجل التواصل مع خبراء في المؤتمرات", "order": 5},
    {"id": "al_c2_s1_r006", "subcategory_id": "al_c2_s1", "name": "تقرير تطبيق أفكار من مؤتمر", "order": 6},
    {"id": "al_c2_s1_r007", "subcategory_id": "al_c2_s1", "name": "توثيق شهادات حضور المؤتمرات", "order": 7},
    {"id": "al_c2_s1_r008", "subcategory_id": "al_c2_s1", "name": "تقرير مشاركة في مؤتمر دولي", "order": 8},
    {"id": "al_c2_s1_r009", "subcategory_id": "al_c2_s1", "name": "سجل التوصيات المستخلصة", "order": 9},
    {"id": "al_c2_s1_r010", "subcategory_id": "al_c2_s1", "name": "تقرير ختامي للمشاركات المهنية", "order": 10},

    # ========== al_c2_s2 ==========
    {"id": "al_c2_s2_r001", "subcategory_id": "al_c2_s2", "name": "تقرير المشاركة في ورش عمل تدريبية", "order": 1},
    {"id": "al_c2_s2_r002", "subcategory_id": "al_c2_s2", "name": "سجل تحسين المهارات عبر الورش", "order": 2},
    {"id": "al_c2_s2_r003", "subcategory_id": "al_c2_s2", "name": "توثيق تطبيق استراتيجيات من ورش", "order": 3},
    {"id": "al_c2_s2_r004", "subcategory_id": "al_c2_s2", "name": "تقرير عن ورشة في استراتيجيات التدريس", "order": 4},
    {"id": "al_c2_s2_r005", "subcategory_id": "al_c2_s2", "name": "سجل تقييم الورش", "order": 5},
    {"id": "al_c2_s2_r006", "subcategory_id": "al_c2_s2", "name": "تقرير تدريب المعلمين على ورش", "order": 6},
    {"id": "al_c2_s2_r007", "subcategory_id": "al_c2_s2", "name": "توثيق شهادات إتمام الورش", "order": 7},
    {"id": "al_c2_s2_r008", "subcategory_id": "al_c2_s2", "name": "تقرير أثر الورش على الأداء", "order": 8},
    {"id": "al_c2_s2_r009", "subcategory_id": "al_c2_s2", "name": "سجل متابعة التدريب", "order": 9},
    {"id": "al_c2_s2_r010", "subcategory_id": "al_c2_s2", "name": "تقرير ختامي للتدريب", "order": 10},

    # ========== al_c2_s3 ==========
    {"id": "al_c2_s3_r001", "subcategory_id": "al_c2_s3", "name": "تقرير الالتحاق ببرنامج تدريبي", "order": 1},
    {"id": "al_c2_s3_r002", "subcategory_id": "al_c2_s3", "name": "سجل تعلم أساليب تدريس حديثة", "order": 2},
    {"id": "al_c2_s3_r003", "subcategory_id": "al_c2_s3", "name": "توثيق تطبيق أساليب جديدة", "order": 3},
    {"id": "al_c2_s3_r004", "subcategory_id": "al_c2_s3", "name": "تقرير عن دورة تدريبية", "order": 4},
    {"id": "al_c2_s3_r005", "subcategory_id": "al_c2_s3", "name": "سجل شهادة البرنامج", "order": 5},
    {"id": "al_c2_s3_r006", "subcategory_id": "al_c2_s3", "name": "تقرير مشاركة الزملاء في البرنامج", "order": 6},
    {"id": "al_c2_s3_r007", "subcategory_id": "al_c2_s3", "name": "توثيق تحسين الممارسات", "order": 7},
    {"id": "al_c2_s3_r008", "subcategory_id": "al_c2_s3", "name": "تقرير أثر البرنامج على الطلاب", "order": 8},
    {"id": "al_c2_s3_r009", "subcategory_id": "al_c2_s3", "name": "سجل تقييم البرنامج", "order": 9},
    {"id": "al_c2_s3_r010", "subcategory_id": "al_c2_s3", "name": "تقرير ختامي للتطوير المهني", "order": 10},

    # ========== al_c2_s4 ==========
    {"id": "al_c2_s4_r001", "subcategory_id": "al_c2_s4", "name": "تقرير الحصول على شهادة مهنية", "order": 1},
    {"id": "al_c2_s4_r002", "subcategory_id": "al_c2_s4", "name": "سجل شهادات معتمدة في التعليم", "order": 2},
    {"id": "al_c2_s4_r003", "subcategory_id": "al_c2_s4", "name": "توثيق تأثير الشهادة على الأداء", "order": 3},
    {"id": "al_c2_s4_r004", "subcategory_id": "al_c2_s4", "name": "تقرير عن اجتياز اختبار مهني", "order": 4},
    {"id": "al_c2_s4_r005", "subcategory_id": "al_c2_s4", "name": "سجل تجديد الشهادات", "order": 5},
    {"id": "al_c2_s4_r006", "subcategory_id": "al_c2_s4", "name": "تقرير مشاركة الخبرة مع الزملاء", "order": 6},
    {"id": "al_c2_s4_r007", "subcategory_id": "al_c2_s4", "name": "توثيق الاعتماد المهني", "order": 7},
    {"id": "al_c2_s4_r008", "subcategory_id": "al_c2_s4", "name": "تقرير تطوير المهارات بالشهادة", "order": 8},
    {"id": "al_c2_s4_r009", "subcategory_id": "al_c2_s4", "name": "سجل متابعة المؤهلات", "order": 9},
    {"id": "al_c2_s4_r010", "subcategory_id": "al_c2_s4", "name": "تقرير ختامي للإنجازات المهنية", "order": 10},

    # ========== al_c2_s5 ==========
    {"id": "al_c2_s5_r001", "subcategory_id": "al_c2_s5", "name": "تقرير إطلاق مبادرة تعليمية", "order": 1},
    {"id": "al_c2_s5_r002", "subcategory_id": "al_c2_s5", "name": "سجل تحسين جودة التعليم", "order": 2},
    {"id": "al_c2_s5_r003", "subcategory_id": "al_c2_s5", "name": "توثيق أثر المبادرة على الطلاب", "order": 3},
    {"id": "al_c2_s5_r004", "subcategory_id": "al_c2_s5", "name": "تقرير عن مبادرة مبتكرة", "order": 4},
    {"id": "al_c2_s5_r005", "subcategory_id": "al_c2_s5", "name": "سجل شراكات في المبادرة", "order": 5},
    {"id": "al_c2_s5_r006", "subcategory_id": "al_c2_s5", "name": "تقرير مشاركة المعلمين في المبادرة", "order": 6},
    {"id": "al_c2_s5_r007", "subcategory_id": "al_c2_s5", "name": "توثيق استدامة المبادرة", "order": 7},
    {"id": "al_c2_s5_r008", "subcategory_id": "al_c2_s5", "name": "تقرير قياس أثر المبادرة", "order": 8},
    {"id": "al_c2_s5_r009", "subcategory_id": "al_c2_s5", "name": "سجل التغذية الراجعة", "order": 9},
    {"id": "al_c2_s5_r010", "subcategory_id": "al_c2_s5", "name": "تقرير ختامي للمبادرة", "order": 10},

    # ========== al_c2_s6 ==========
    {"id": "al_c2_s6_r001", "subcategory_id": "al_c2_s6", "name": "تقرير تقديم استشارات للمعلمين الجدد", "order": 1},
    {"id": "al_c2_s6_r002", "subcategory_id": "al_c2_s6", "name": "سجل الإرشاد التربوي", "order": 2},
    {"id": "al_c2_s6_r003", "subcategory_id": "al_c2_s6", "name": "توثيق لقاءات مع المعلمين الجدد", "order": 3},
    {"id": "al_c2_s6_r004", "subcategory_id": "al_c2_s6", "name": "تقرير برنامج توجيه المعلمين", "order": 4},
    {"id": "al_c2_s6_r005", "subcategory_id": "al_c2_s6", "name": "سجل استفادة المعلمين الجدد", "order": 5},
    {"id": "al_c2_s6_r006", "subcategory_id": "al_c2_s6", "name": "تقرير ورش للمعلمين الجدد", "order": 6},
    {"id": "al_c2_s6_r007", "subcategory_id": "al_c2_s6", "name": "توثيق التغذية الراجعة", "order": 7},
    {"id": "al_c2_s6_r008", "subcategory_id": "al_c2_s6", "name": "تقرير متابعة أداء المعلمين الجدد", "order": 8},
    {"id": "al_c2_s6_r009", "subcategory_id": "al_c2_s6", "name": "سجل تقييم الاستشارات", "order": 9},
    {"id": "al_c2_s6_r010", "subcategory_id": "al_c2_s6", "name": "تقرير ختامي للإرشاد", "order": 10},

    # ========== al_c2_s7 ==========
    {"id": "al_c2_s7_r001", "subcategory_id": "al_c2_s7", "name": "تقرير تبادل الخبرات مع مدارس أخرى", "order": 1},
    {"id": "al_c2_s7_r002", "subcategory_id": "al_c2_s7", "name": "سجل زيارات تبادلية", "order": 2},
    {"id": "al_c2_s7_r003", "subcategory_id": "al_c2_s7", "name": "توثيق اجتماعات مع معلمين", "order": 3},
    {"id": "al_c2_s7_r004", "subcategory_id": "al_c2_s7", "name": "تقرير عن ممارسات ناجحة", "order": 4},
    {"id": "al_c2_s7_r005", "subcategory_id": "al_c2_s7", "name": "سبل التعاون المشترك", "order": 5},
    {"id": "al_c2_s7_r006", "subcategory_id": "al_c2_s7", "name": "تقرير تطبيق خبرات مستفادة", "order": 6},
    {"id": "al_c2_s7_r007", "subcategory_id": "al_c2_s7", "name": "توثيق الشبكات المهنية", "order": 7},
    {"id": "al_c2_s7_r008", "subcategory_id": "al_c2_s7", "name": "تقرير تقييم التبادل", "order": 8},
    {"id": "al_c2_s7_r009", "subcategory_id": "al_c2_s7", "name": "سجل استضافة معلمين", "order": 9},
    {"id": "al_c2_s7_r010", "subcategory_id": "al_c2_s7", "name": "تقرير ختامي لتبادل الخبرات", "order": 10},

    # ========== al_c2_s8 ==========
    {"id": "al_c2_s8_r001", "subcategory_id": "al_c2_s8", "name": "تقرير التفكير الذاتي للممارسات", "order": 1},
    {"id": "al_c2_s8_r002", "subcategory_id": "al_c2_s8", "name": "سجل تحسين الأداء الشخصي", "order": 2},
    {"id": "al_c2_s8_r003", "subcategory_id": "al_c2_s8", "name": "توثيق التأمل المهني", "order": 3},
    {"id": "al_c2_s8_r004", "subcategory_id": "al_c2_s8", "name": "تقرير عن خطة تطوير ذاتي", "order": 4},
    {"id": "al_c2_s8_r005", "subcategory_id": "al_c2_s8", "name": "سجل ملاحظات التحسين", "order": 5},
    {"id": "al_c2_s8_r006", "subcategory_id": "al_c2_s8", "name": "تقرير ورش للتفكير التأملي", "order": 6},
    {"id": "al_c2_s8_r007", "subcategory_id": "al_c2_s8", "name": "توثيق التعلم المستمر", "order": 7},
    {"id": "al_c2_s8_r008", "subcategory_id": "al_c2_s8", "name": "تقرير تقييم التطور", "order": 8},
    {"id": "al_c2_s8_r009", "subcategory_id": "al_c2_s8", "name": "سجل تطبيق تحسينات", "order": 9},
    {"id": "al_c2_s8_r010", "subcategory_id": "al_c2_s8", "name": "تقرير ختامي للتفكير الذاتي", "order": 10},

    # ========== al_c3_s1 ==========
    {"id": "al_c3_s1_r001", "subcategory_id": "al_c3_s1", "name": "تقرير اجتماع دوري مع أولياء الأمور", "order": 1},
    {"id": "al_c3_s1_r002", "subcategory_id": "al_c3_s1", "name": "سجل مناقشة تقدم الطلاب", "order": 2},
    {"id": "al_c3_s1_r003", "subcategory_id": "al_c3_s1", "name": "توثيق محاضر الاجتماعات", "order": 3},
    {"id": "al_c3_s1_r004", "subcategory_id": "al_c3_s1", "name": "تقرير مشاركة أولياء الأمور", "order": 4},
    {"id": "al_c3_s1_r005", "subcategory_id": "al_c3_s1", "name": "سجل التوصيات المقدمة", "order": 5},
    {"id": "al_c3_s1_r006", "subcategory_id": "al_c3_s1", "name": "تقرير متابعة تنفيذ التوصيات", "order": 6},
    {"id": "al_c3_s1_r007", "subcategory_id": "al_c3_s1", "name": "توثيق استطلاعات الرضا", "order": 7},
    {"id": "al_c3_s1_r008", "subcategory_id": "al_c3_s1", "name": "تقرير اجتماعات فردية", "order": 8},
    {"id": "al_c3_s1_r009", "subcategory_id": "al_c3_s1", "name": "سجل تطور العلاقة مع أولياء الأمور", "order": 9},
    {"id": "al_c3_s1_r010", "subcategory_id": "al_c3_s1", "name": "تقرير ختامي للتواصل", "order": 10},

    # ========== al_c3_s2 ==========
    {"id": "al_c3_s2_r001", "subcategory_id": "al_c3_s2", "name": "تقرير إرسال تقارير أداء الطلاب", "order": 1},
    {"id": "al_c3_s2_r002", "subcategory_id": "al_c3_s2", "name": "سجل التقارير الأكاديمية والسلوكية", "order": 2},
    {"id": "al_c3_s2_r003", "subcategory_id": "al_c3_s2", "name": "توثيق متابعة أولياء الأمور للتقارير", "order": 3},
    {"id": "al_c3_s2_r004", "subcategory_id": "al_c3_s2", "name": "تقرير عن نموذج التقرير المستخدم", "order": 4},
    {"id": "al_c3_s2_r005", "subcategory_id": "al_c3_s2", "name": "سجل ملاحظات أولياء الأمور", "order": 5},
    {"id": "al_c3_s2_r006", "subcategory_id": "al_c3_s2", "name": "تقرير تحسين التقارير", "order": 6},
    {"id": "al_c3_s2_r007", "subcategory_id": "al_c3_s2", "name": "توثيق توزيع التقارير", "order": 7},
    {"id": "al_c3_s2_r008", "subcategory_id": "al_c3_s2", "name": "تقرير تقييم فاعلية التقارير", "order": 8},
    {"id": "al_c3_s2_r009", "subcategory_id": "al_c3_s2", "name": "سجل الشفافية في التواصل", "order": 9},
    {"id": "al_c3_s2_r010", "subcategory_id": "al_c3_s2", "name": "تقرير ختامي للتقارير", "order": 10},

    # ========== al_c3_s3 ==========
    {"id": "al_c3_s3_r001", "subcategory_id": "al_c3_s3", "name": "تقرير استخدام البريد الإلكتروني للتواصل", "order": 1},
    {"id": "al_c3_s3_r002", "subcategory_id": "al_c3_s3", "name": "سجل التطبيقات التعليمية المستخدمة", "order": 2},
    {"id": "al_c3_s3_r003", "subcategory_id": "al_c3_s3", "name": "توثيق تفاعل أولياء الأمور", "order": 3},
    {"id": "al_c3_s3_r004", "subcategory_id": "al_c3_s3", "name": "تقرير عن منصة التواصل", "order": 4},
    {"id": "al_c3_s3_r005", "subcategory_id": "al_c3_s3", "name": "سبل تحسين التواصل الرقمي", "order": 5},
    {"id": "al_c3_s3_r006", "subcategory_id": "al_c3_s3", "name": "تقرير تدريب أولياء الأمور على التطبيقات", "order": 6},
    {"id": "al_c3_s3_r007", "subcategory_id": "al_c3_s3", "name": "توثيق الإشعارات الفورية", "order": 7},
    {"id": "al_c3_s3_r008", "subcategory_id": "al_c3_s3", "name": "تقرير قياس رضا أولياء الأمور", "order": 8},
    {"id": "al_c3_s3_r009", "subcategory_id": "al_c3_s3", "name": "سجل تحديث وسائل التواصل", "order": 9},
    {"id": "al_c3_s3_r010", "subcategory_id": "al_c3_s3", "name": "تقرير ختامي للتواصل الرقمي", "order": 10},

    # ========== al_c3_s4 ==========
    {"id": "al_c3_s4_r001", "subcategory_id": "al_c3_s4", "name": "تقرير الاستماع لملاحظات أولياء الأمور", "order": 1},
    {"id": "al_c3_s4_r002", "subcategory_id": "al_c3_s4", "name": "سجل مخاوف أولياء الأمور ومعالجتها", "order": 2},
    {"id": "al_c3_s4_r003", "subcategory_id": "al_c3_s4", "name": "توثيق الاجتماعات مع أولياء الأمور", "order": 3},
    {"id": "al_c3_s4_r004", "subcategory_id": "al_c3_s4", "name": "تقرير حل المشكلات بالتعاون", "order": 4},
    {"id": "al_c3_s4_r005", "subcategory_id": "al_c3_s4", "name": "سبل تحسين الاستجابة", "order": 5},
    {"id": "al_c3_s4_r006", "subcategory_id": "al_c3_s4", "name": "تقرير متابعة تنفيذ الحلول", "order": 6},
    {"id": "al_c3_s4_r007", "subcategory_id": "al_c3_s4", "name": "توثيق التغذية الراجعة", "order": 7},
    {"id": "al_c3_s4_r008", "subcategory_id": "al_c3_s4", "name": "تقرير قياس الثقة", "order": 8},
    {"id": "al_c3_s4_r009", "subcategory_id": "al_c3_s4", "name": "سجل الشكاوى والمقترحات", "order": 9},
    {"id": "al_c3_s4_r010", "subcategory_id": "al_c3_s4", "name": "تقرير ختامي للتعاون", "order": 10},

    # ========== al_c3_s5 ==========
    {"id": "al_c3_s5_r001", "subcategory_id": "al_c3_s5", "name": "تقرير تشجيع مشاركة أولياء الأمور", "order": 1},
    {"id": "al_c3_s5_r002", "subcategory_id": "al_c3_s5", "name": "سجل فعاليات بمشاركة أولياء الأمور", "order": 2},
    {"id": "al_c3_s5_r003", "subcategory_id": "al_c3_s5", "name": "توثيق دور أولياء الأمور في الأنشطة", "order": 3},
    {"id": "al_c3_s5_r004", "subcategory_id": "al_c3_s5", "name": "تقرير عن يوم مفتوح لأولياء الأمور", "order": 4},
    {"id": "al_c3_s5_r005", "subcategory_id": "al_c3_s5", "name": "سبل تعزيز الشراكة", "order": 5},
    {"id": "al_c3_s5_r006", "subcategory_id": "al_c3_s5", "name": "تقرير متابعة مشاركتهم", "order": 6},
    {"id": "al_c3_s5_r007", "subcategory_id": "al_c3_s5", "name": "توثيق تطوع أولياء الأمور", "order": 7},
    {"id": "al_c3_s5_r008", "subcategory_id": "al_c3_s5", "name": "تقرير قياس الأثر", "order": 8},
    {"id": "al_c3_s5_r009", "subcategory_id": "al_c3_s5", "name": "سجل تحفيز المشاركة", "order": 9},
    {"id": "al_c3_s5_r010", "subcategory_id": "al_c3_s5", "name": "تقرير ختامي للشراكة", "order": 10},

    # ========== al_c4_s1 ==========
    {"id": "al_c4_s1_r001", "subcategory_id": "al_c4_s1", "name": "تقرير استخدام المناقشات الجماعية", "order": 1},
    {"id": "al_c4_s1_r002", "subcategory_id": "al_c4_s1", "name": "سجل العروض التقديمية للطلاب", "order": 2},
    {"id": "al_c4_s1_r003", "subcategory_id": "al_c4_s1", "name": "توثيق التعلم النشط في الفصل", "order": 3},
    {"id": "al_c4_s1_r004", "subcategory_id": "al_c4_s1", "name": "تقرير عن استراتيجية التعلم باللعب", "order": 4},
    {"id": "al_c4_s1_r005", "subcategory_id": "al_c4_s1", "name": "سجل تفاعل الطلاب", "order": 5},
    {"id": "al_c4_s1_r006", "subcategory_id": "al_c4_s1", "name": "تقرير تطبيق التعلم التعاوني", "order": 6},
    {"id": "al_c4_s1_r007", "subcategory_id": "al_c4_s1", "name": "توثيق حل المشكلات الجماعي", "order": 7},
    {"id": "al_c4_s1_r008", "subcategory_id": "al_c4_s1", "name": "تقرير قياس أثر التعلم النشط", "order": 8},
    {"id": "al_c4_s1_r009", "subcategory_id": "al_c4_s1", "name": "سجل تدريب المعلمين على التعلم النشط", "order": 9},
    {"id": "al_c4_s1_r010", "subcategory_id": "al_c4_s1", "name": "تقرير ختامي للاستراتيجيات", "order": 10},

    # ========== al_c4_s2 ==========
    {"id": "al_c4_s2_r001", "subcategory_id": "al_c4_s2", "name": "تقرير مشروع تعزيز الإبداع", "order": 1},
    {"id": "al_c4_s2_r002", "subcategory_id": "al_c4_s2", "name": "سجل حل المشكلات عبر المشاريع", "order": 2},
    {"id": "al_c4_s2_r003", "subcategory_id": "al_c4_s2", "name": "توثيق معرض المشاريع الطلابية", "order": 3},
    {"id": "al_c4_s2_r004", "subcategory_id": "al_c4_s2", "name": "تقرير عن مشروع بحثي", "order": 4},
    {"id": "al_c4_s2_r005", "subcategory_id": "al_c4_s2", "name": "سجل تقييم المشاريع", "order": 5},
    {"id": "al_c4_s2_r006", "subcategory_id": "al_c4_s2", "name": "تقرير تطبيق التعلم القائم على المشاريع", "order": 6},
    {"id": "al_c4_s2_r007", "subcategory_id": "al_c4_s2", "name": "توثيق تعاون الطلاب في المشاريع", "order": 7},
    {"id": "al_c4_s2_r008", "subcategory_id": "al_c4_s2", "name": "تقرير أثر المشاريع على المهارات", "order": 8},
    {"id": "al_c4_s2_r009", "subcategory_id": "al_c4_s2", "name": "سبل تحسين المشاريع", "order": 9},
    {"id": "al_c4_s2_r010", "subcategory_id": "al_c4_s2", "name": "تقرير ختامي للمشاريع", "order": 10},

    # ========== al_c4_s3 ==========
    {"id": "al_c4_s3_r001", "subcategory_id": "al_c4_s3", "name": "تقرير استخدام الفيديوهات التعليمية", "order": 1},
    {"id": "al_c4_s3_r002", "subcategory_id": "al_c4_s3", "name": "سجل الوسائل البصرية في الدروس", "order": 2},
    {"id": "al_c4_s3_r003", "subcategory_id": "al_c4_s3", "name": "توثيق استخدام الصور والرسوم", "order": 3},
    {"id": "al_c4_s3_r004", "subcategory_id": "al_c4_s3", "name": "تقرير عن عروض تقديمية", "order": 4},
    {"id": "al_c4_s3_r005", "subcategory_id": "al_c4_s3", "name": "سجل تفاعل الطلاب مع الوسائل", "order": 5},
    {"id": "al_c4_s3_r006", "subcategory_id": "al_c4_s3", "name": "تقرير تطبيق الوسائل السمعية", "order": 6},
    {"id": "al_c4_s3_r007", "subcategory_id": "al_c4_s3", "name": "توثيق إنتاج طلاب لوسائل", "order": 7},
    {"id": "al_c4_s3_r008", "subcategory_id": "al_c4_s3", "name": "تقرير قياس الفهم بالوسائل", "order": 8},
    {"id": "al_c4_s3_r009", "subcategory_id": "al_c4_s3", "name": "سجل تطوير الوسائل", "order": 9},
    {"id": "al_c4_s3_r010", "subcategory_id": "al_c4_s3", "name": "تقرير ختامي للوسائل", "order": 10},

    # ========== al_c4_s4 ==========
    {"id": "al_c4_s4_r001", "subcategory_id": "al_c4_s4", "name": "تقرير أنشطة للطلاب البصريين", "order": 1},
    {"id": "al_c4_s4_r002", "subcategory_id": "al_c4_s4", "name": "سجل أنشطة للطلاب السمعيين", "order": 2},
    {"id": "al_c4_s4_r003", "subcategory_id": "al_c4_s4", "name": "توثيق أنشطة للطلاب الحركيين", "order": 3},
    {"id": "al_c4_s4_r004", "subcategory_id": "al_c4_s4", "name": "تقرير عن تخصيص التعلم", "order": 4},
    {"id": "al_c4_s4_r005", "subcategory_id": "al_c4_s4", "name": "سجل مراعاة أنماط التعلم", "order": 5},
    {"id": "al_c4_s4_r006", "subcategory_id": "al_c4_s4", "name": "تقرير تطبيق استراتيجيات متنوعة", "order": 6},
    {"id": "al_c4_s4_r007", "subcategory_id": "al_c4_s4", "name": "توثيق تحسين الأداء", "order": 7},
    {"id": "al_c4_s4_r008", "subcategory_id": "al_c4_s4", "name": "تقرير قياس الرضا", "order": 8},
    {"id": "al_c4_s4_r009", "subcategory_id": "al_c4_s4", "name": "سبل تنويع الأنشطة", "order": 9},
    {"id": "al_c4_s4_r010", "subcategory_id": "al_c4_s4", "name": "تقرير ختامي للتخصيص", "order": 10},

    # ========== al_c5_s1 ==========
    {"id": "al_c5_s1_r001", "subcategory_id": "al_c5_s1", "name": "تقرير تحديد أهداف التعلم", "order": 1},
    {"id": "al_c5_s1_r002", "subcategory_id": "al_c5_s1", "name": "سجل معايير النجاح", "order": 2},
    {"id": "al_c5_s1_r003", "subcategory_id": "al_c5_s1", "name": "توثيق مشاركة الطلاب في وضع الأهداف", "order": 3},
    {"id": "al_c5_s1_r004", "subcategory_id": "al_c5_s1", "name": "تقرير وضوح الأهداف للطلاب", "order": 4},
    {"id": "al_c5_s1_r005", "subcategory_id": "al_c5_s1", "name": "سجل متابعة تحقيق الأهداف", "order": 5},
    {"id": "al_c5_s1_r006", "subcategory_id": "al_c5_s1", "name": "تقرير تقييم الأهداف", "order": 6},
    {"id": "al_c5_s1_r007", "subcategory_id": "al_c5_s1", "name": "توثيق تحديث الأهداف", "order": 7},
    {"id": "al_c5_s1_r008", "subcategory_id": "al_c5_s1", "name": "تقرير أثر الأهداف على التحصيل", "order": 8},
    {"id": "al_c5_s1_r009", "subcategory_id": "al_c5_s1", "name": "سبل تحسين وضوح الأهداف", "order": 9},
    {"id": "al_c5_s1_r010", "subcategory_id": "al_c5_s1", "name": "تقرير ختامي للأهداف", "order": 10},

    # ========== al_c5_s2 ==========
    {"id": "al_c5_s2_r001", "subcategory_id": "al_c5_s2", "name": "تقرير تقديم تغذية راجعة فورية", "order": 1},
    {"id": "al_c5_s2_r002", "subcategory_id": "al_c5_s2", "name": "سجل ملاحظات الأداء", "order": 2},
    {"id": "al_c5_s2_r003", "subcategory_id": "al_c5_s2", "name": "توثيق التركيز على الإيجابيات", "order": 3},
    {"id": "al_c5_s2_r004", "subcategory_id": "al_c5_s2", "name": "تقرير اقتراحات تحسين الأداء", "order": 4},
    {"id": "al_c5_s2_r005", "subcategory_id": "al_c5_s2", "name": "سجل استجابة الطلاب", "order": 5},
    {"id": "al_c5_s2_r006", "subcategory_id": "al_c5_s2", "name": "تقرير فاعلية التغذية الراجعة", "order": 6},
    {"id": "al_c5_s2_r007", "subcategory_id": "al_c5_s2", "name": "توثيق تحسينات بناءً على التغذية", "order": 7},
    {"id": "al_c5_s2_r008", "subcategory_id": "al_c5_s2", "name": "تقرير تدريب على التغذية الراجعة", "order": 8},
    {"id": "al_c5_s2_r009", "subcategory_id": "al_c5_s2", "name": "سبل تحسين التغذية", "order": 9},
    {"id": "al_c5_s2_r010", "subcategory_id": "al_c5_s2", "name": "تقرير ختامي للتغذية", "order": 10},

    # ========== al_c5_s3 ==========
    {"id": "al_c5_s3_r001", "subcategory_id": "al_c5_s3", "name": "تقرير تكييف التغذية للطلاب", "order": 1},
    {"id": "al_c5_s3_r002", "subcategory_id": "al_c5_s3", "name": "سجل تخصيص الملاحظات", "order": 2},
    {"id": "al_c5_s3_r003", "subcategory_id": "al_c5_s3", "name": "توثيق مراعاة الاحتياجات الفردية", "order": 3},
    {"id": "al_c5_s3_r004", "subcategory_id": "al_c5_s3", "name": "تقرير عن خطط دعم فردية", "order": 4},
    {"id": "al_c5_s3_r005", "subcategory_id": "al_c5_s3", "name": "سجل متابعة تقدم كل طالب", "order": 5},
    {"id": "al_c5_s3_r006", "subcategory_id": "al_c5_s3", "name": "تقرير فعالية التكييف", "order": 6},
    {"id": "al_c5_s3_r007", "subcategory_id": "al_c5_s3", "name": "توثيق تحسين الأداء", "order": 7},
    {"id": "al_c5_s3_r008", "subcategory_id": "al_c5_s3", "name": "تقرير قياس رضا الطلاب", "order": 8},
    {"id": "al_c5_s3_r009", "subcategory_id": "al_c5_s3", "name": "سبل تطوير التكييف", "order": 9},
    {"id": "al_c5_s3_r010", "subcategory_id": "al_c5_s3", "name": "تقرير ختامي للتخصيص", "order": 10},

    # ========== al_c5_s4 ==========
    {"id": "al_c5_s4_r001", "subcategory_id": "al_c5_s4", "name": "تقرير تعزيز الثقة لدى الطلاب", "order": 1},
    {"id": "al_c5_s4_r002", "subcategory_id": "al_c5_s4", "name": "سجل ملاحظات تشجيعية", "order": 2},
    {"id": "al_c5_s4_r003", "subcategory_id": "al_c5_s4", "name": "توثيق فرص تحسين الأداء", "order": 3},
    {"id": "al_c5_s4_r004", "subcategory_id": "al_c5_s4", "name": "تقرير عن أنشطة تحفيزية", "order": 4},
    {"id": "al_c5_s4_r005", "subcategory_id": "al_c5_s4", "name": "سجل تطور ثقة الطلاب", "order": 5},
    {"id": "al_c5_s4_r006", "subcategory_id": "al_c5_s4", "name": "تقرير أثر التحفيز", "order": 6},
    {"id": "al_c5_s4_r007", "subcategory_id": "al_c5_s4", "name": "توثيق قصص نجاح", "order": 7},
    {"id": "al_c5_s4_r008", "subcategory_id": "al_c5_s4", "name": "تقرير ورش تحفيزية", "order": 8},
    {"id": "al_c5_s4_r009", "subcategory_id": "al_c5_s4", "name": "سبل تعزيز الثقة", "order": 9},
    {"id": "al_c5_s4_r010", "subcategory_id": "al_c5_s4", "name": "تقرير ختامي للتحفيز", "order": 10},

    # ========== al_c5_s5 ==========
    {"id": "al_c5_s5_r001", "subcategory_id": "al_c5_s5", "name": "تقرير استخدام البريد الإلكتروني للتغذية", "order": 1},
    {"id": "al_c5_s5_r002", "subcategory_id": "al_c5_s5", "name": "سجل منصات التعلم", "order": 2},
    {"id": "al_c5_s5_r003", "subcategory_id": "al_c5_s5", "name": "توثيق تقديم تغذية عبر التطبيقات", "order": 3},
    {"id": "al_c5_s5_r004", "subcategory_id": "al_c5_s5", "name": "تقرير عن أدوات التكنولوجيا", "order": 4},
    {"id": "al_c5_s5_r005", "subcategory_id": "al_c5_s5", "name": "سجل تفاعل الطلاب مع التغذية الرقمية", "order": 5},
    {"id": "al_c5_s5_r006", "subcategory_id": "al_c5_s5", "name": "تقرير فاعلية التكنولوجيا", "order": 6},
    {"id": "al_c5_s5_r007", "subcategory_id": "al_c5_s5", "name": "توثيق تحسينات باستخدام التكنولوجيا", "order": 7},
    {"id": "al_c5_s5_r008", "subcategory_id": "al_c5_s5", "name": "تقرير تدريب على الأدوات", "order": 8},
    {"id": "al_c5_s5_r009", "subcategory_id": "al_c5_s5", "name": "سبل تطبيق التكنولوجيا", "order": 9},
    {"id": "al_c5_s5_r010", "subcategory_id": "al_c5_s5", "name": "تقرير ختامي للتغذية الرقمية", "order": 10},

    # ========== al_c6_s1 ==========
    {"id": "al_c6_s1_r001", "subcategory_id": "al_c6_s1", "name": "تقرير وضع أهداف تعليمية", "order": 1},
    {"id": "al_c6_s1_r002", "subcategory_id": "al_c6_s1", "name": "سجل قياس الأهداف", "order": 2},
    {"id": "al_c6_s1_r003", "subcategory_id": "al_c6_s1", "name": "توثيق وضوح الأهداف للطلاب", "order": 3},
    {"id": "al_c6_s1_r004", "subcategory_id": "al_c6_s1", "name": "تقرير عن أهداف خطة التعلم", "order": 4},
    {"id": "al_c6_s1_r005", "subcategory_id": "al_c6_s1", "name": "سجل متابعة تحقيق الأهداف", "order": 5},
    {"id": "al_c6_s1_r006", "subcategory_id": "al_c6_s1", "name": "تقرير تقييم الأهداف", "order": 6},
    {"id": "al_c6_s1_r007", "subcategory_id": "al_c6_s1", "name": "توثيق تحديث الأهداف", "order": 7},
    {"id": "al_c6_s1_r008", "subcategory_id": "al_c6_s1", "name": "تقرير أثر الأهداف على التعلم", "order": 8},
    {"id": "al_c6_s1_r009", "subcategory_id": "al_c6_s1", "name": "سبل تحسين الأهداف", "order": 9},
    {"id": "al_c6_s1_r010", "subcategory_id": "al_c6_s1", "name": "تقرير ختامي للأهداف", "order": 10},

    # ========== al_c6_s2 ==========
    {"id": "al_c6_s2_r001", "subcategory_id": "al_c6_s2", "name": "تقرير تصميم خطة دراسية", "order": 1},
    {"id": "al_c6_s2_r002", "subcategory_id": "al_c6_s2", "name": "سجل توافق الخطة مع المنهج", "order": 2},
    {"id": "al_c6_s2_r003", "subcategory_id": "al_c6_s2", "name": "توثيق مراعاة احتياجات الطلاب", "order": 3},
    {"id": "al_c6_s2_r004", "subcategory_id": "al_c6_s2", "name": "تقرير عن عناصر الخطة", "order": 4},
    {"id": "al_c6_s2_r005", "subcategory_id": "al_c6_s2", "name": "سجل مشاركة الطلاب في التخطيط", "order": 5},
    {"id": "al_c6_s2_r006", "subcategory_id": "al_c6_s2", "name": "تقرير تطبيق الخطة", "order": 6},
    {"id": "al_c6_s2_r007", "subcategory_id": "al_c6_s2", "name": "توثيق تعديلات الخطة", "order": 7},
    {"id": "al_c6_s2_r008", "subcategory_id": "al_c6_s2", "name": "تقرير قياس فاعلية الخطة", "order": 8},
    {"id": "al_c6_s2_r009", "subcategory_id": "al_c6_s2", "name": "سبل تطوير التصميم", "order": 9},
    {"id": "al_c6_s2_r010", "subcategory_id": "al_c6_s2", "name": "تقرير ختامي للخطة", "order": 10},

    # ========== al_c6_s3 ==========
    {"id": "al_c6_s3_r001", "subcategory_id": "al_c6_s3", "name": "تقرير مراجعة دورية للخطط", "order": 1},
    {"id": "al_c6_s3_r002", "subcategory_id": "al_c6_s3", "name": "سجل تعديل الخطط بناءً على النتائج", "order": 2},
    {"id": "al_c6_s3_r003", "subcategory_id": "al_c6_s3", "name": "توثيق تحسينات الخطة", "order": 3},
    {"id": "al_c6_s3_r004", "subcategory_id": "al_c6_s3", "name": "تقرير عن ملاحظات الطلاب", "order": 4},
    {"id": "al_c6_s3_r005", "subcategory_id": "al_c6_s3", "name": "سجل تحليل نتائج الطلاب", "order": 5},
    {"id": "al_c6_s3_r006", "subcategory_id": "al_c6_s3", "name": "تقرير فاعلية التعديلات", "order": 6},
    {"id": "al_c6_s3_r007", "subcategory_id": "al_c6_s3", "name": "توثيق اجتماعات المراجعة", "order": 7},
    {"id": "al_c6_s3_r008", "subcategory_id": "al_c6_s3", "name": "تقرير تحديث الخطط", "order": 8},
    {"id": "al_c6_s3_r009", "subcategory_id": "al_c6_s3", "name": "سبل تحسين المراجعة", "order": 9},
    {"id": "al_c6_s3_r010", "subcategory_id": "al_c6_s3", "name": "تقرير ختامي للمراجعة", "order": 10},

    # ========== al_c6_s4 ==========
    {"id": "al_c6_s4_r001", "subcategory_id": "al_c6_s4", "name": "تقرير مشاركة الخطط مع الزملاء", "order": 1},
    {"id": "al_c6_s4_r002", "subcategory_id": "al_c6_s4", "name": "سجل ملاحظات الزملاء", "order": 2},
    {"id": "al_c6_s4_r003", "subcategory_id": "al_c6_s4", "name": "توثيق تحسين الخطط بملاحظاتهم", "order": 3},
    {"id": "al_c6_s4_r004", "subcategory_id": "al_c6_s4", "name": "تقرير عن اجتماعات تبادل الخطط", "order": 4},
    {"id": "al_c6_s4_r005", "subcategory_id": "al_c6_s4", "name": "سجل التعاون في التخطيط", "order": 5},
    {"id": "al_c6_s4_r006", "subcategory_id": "al_c6_s4", "name": "تقرير فاعلية المشاركة", "order": 6},
    {"id": "al_c6_s4_r007", "subcategory_id": "al_c6_s4", "name": "توثيق تطوير الخطط", "order": 7},
    {"id": "al_c6_s4_r008", "subcategory_id": "al_c6_s4", "name": "تقرير قياس التعاون", "order": 8},
    {"id": "al_c6_s4_r009", "subcategory_id": "al_c6_s4", "name": "سبل تعزيز المشاركة", "order": 9},
    {"id": "al_c6_s4_r010", "subcategory_id": "al_c6_s4", "name": "تقرير ختامي للتعاون", "order": 10},

    # ========== al_c6_s5 ==========
    {"id": "al_c6_s5_r001", "subcategory_id": "al_c6_s5", "name": "تقرير فهم خصائص المرحلة العمرية", "order": 1},
    {"id": "al_c6_s5_r002", "subcategory_id": "al_c6_s5", "name": "سجل مراعاة الخصائص النفسية", "order": 2},
    {"id": "al_c6_s5_r003", "subcategory_id": "al_c6_s5", "name": "توثيق تكييف الخطط للمرحلة", "order": 3},
    {"id": "al_c6_s5_r004", "subcategory_id": "al_c6_s5", "name": "تقرير عن ورش عن النمو", "order": 4},
    {"id": "al_c6_s5_r005", "subcategory_id": "al_c6_s5", "name": "سجل تطبيق المعرفة النفسية", "order": 5},
    {"id": "al_c6_s5_r006", "subcategory_id": "al_c6_s5", "name": "تقرير أثر التكييف", "order": 6},
    {"id": "al_c6_s5_r007", "subcategory_id": "al_c6_s5", "name": "توثيق تحسين التفاعل", "order": 7},
    {"id": "al_c6_s5_r008", "subcategory_id": "al_c6_s5", "name": "تقرير قياس الفهم", "order": 8},
    {"id": "al_c6_s5_r009", "subcategory_id": "al_c6_s5", "name": "سبل تعزيز الفهم", "order": 9},
    {"id": "al_c6_s5_r010", "subcategory_id": "al_c6_s5", "name": "تقرير ختامي للخصائص", "order": 10},

    # ========== al_c7_s1 ==========
    {"id": "al_c7_s1_r001", "subcategory_id": "al_c7_s1", "name": "تقرير استخدام السبورة الذكية", "order": 1},
    {"id": "al_c7_s1_r002", "subcategory_id": "al_c7_s1", "name": "سجل تطبيق الأجهزة اللوحية", "order": 2},
    {"id": "al_c7_s1_r003", "subcategory_id": "al_c7_s1", "name": "توثيق تفاعل الطلاب مع التكنولوجيا", "order": 3},
    {"id": "al_c7_s1_r004", "subcategory_id": "al_c7_s1", "name": "تقرير عن دروس باستخدام السبورة", "order": 4},
    {"id": "al_c7_s1_r005", "subcategory_id": "al_c7_s1", "name": "سجل تدريب على الأجهزة", "order": 5},
    {"id": "al_c7_s1_r006", "subcategory_id": "al_c7_s1", "name": "تقرير فاعلية التقنية", "order": 6},
    {"id": "al_c7_s1_r007", "subcategory_id": "al_c7_s1", "name": "توثيق تحسين التعلم", "order": 7},
    {"id": "al_c7_s1_r008", "subcategory_id": "al_c7_s1", "name": "تقرير تحديث الأجهزة", "order": 8},
    {"id": "al_c7_s1_r009", "subcategory_id": "al_c7_s1", "name": "سبل تطوير الاستخدام", "order": 9},
    {"id": "al_c7_s1_r010", "subcategory_id": "al_c7_s1", "name": "تقرير ختامي للتقنية", "order": 10},

    # ========== al_c7_s2 ==========
    {"id": "al_c7_s2_r001", "subcategory_id": "al_c7_s2", "name": "تقرير استخدام منصات التعلم", "order": 1},
    {"id": "al_c7_s2_r002", "subcategory_id": "al_c7_s2", "name": "سجل تطبيق برامج إلكترونية", "order": 2},
    {"id": "al_c7_s2_r003", "subcategory_id": "al_c7_s2", "name": "توثيق تفاعل الطلاب عن بعد", "order": 3},
    {"id": "al_c7_s2_r004", "subcategory_id": "al_c7_s2", "name": "تقرير عن منصة مدرستي", "order": 4},
    {"id": "al_c7_s2_r005", "subcategory_id": "al_c7_s2", "name": "سجل تدريب على المنصات", "order": 5},
    {"id": "al_c7_s2_r006", "subcategory_id": "al_c7_s2", "name": "تقرير فاعلية التعلم الإلكتروني", "order": 6},
    {"id": "al_c7_s2_r007", "subcategory_id": "al_c7_s2", "name": "توثيق تحسين الأداء", "order": 7},
    {"id": "al_c7_s2_r008", "subcategory_id": "al_c7_s2", "name": "تقرير تحديث البرامج", "order": 8},
    {"id": "al_c7_s2_r009", "subcategory_id": "al_c7_s2", "name": "سبل تطوير المنصات", "order": 9},
    {"id": "al_c7_s2_r010", "subcategory_id": "al_c7_s2", "name": "تقرير ختامي للتعلم الإلكتروني", "order": 10},

    # ========== al_c7_s3 ==========
    {"id": "al_c7_s3_r001", "subcategory_id": "al_c7_s3", "name": "تقرير تشجيع استخدام التطبيقات", "order": 1},
    {"id": "al_c7_s3_r002", "subcategory_id": "al_c7_s3", "name": "سجل التطبيقات التعليمية", "order": 2},
    {"id": "al_c7_s3_r003", "subcategory_id": "al_c7_s3", "name": "توثيق تعزيز التعلم الذاتي", "order": 3},
    {"id": "al_c7_s3_r004", "subcategory_id": "al_c7_s3", "name": "تقرير عن تطبيقات موصى بها", "order": 4},
    {"id": "al_c7_s3_r005", "subcategory_id": "al_c7_s3", "name": "سجل متابعة استخدام الطلاب", "order": 5},
    {"id": "al_c7_s3_r006", "subcategory_id": "al_c7_s3", "name": "تقرير فاعلية التطبيقات", "order": 6},
    {"id": "al_c7_s3_r007", "subcategory_id": "al_c7_s3", "name": "توثيق تحسين المهارات", "order": 7},
    {"id": "al_c7_s3_r008", "subcategory_id": "al_c7_s3", "name": "تقرير تحديث التطبيقات", "order": 8},
    {"id": "al_c7_s3_r009", "subcategory_id": "al_c7_s3", "name": "سبل تعزيز الاستخدام", "order": 9},
    {"id": "al_c7_s3_r010", "subcategory_id": "al_c7_s3", "name": "تقرير ختامي للتطبيقات", "order": 10},

    # ========== al_c7_s4 ==========
    {"id": "al_c7_s4_r001", "subcategory_id": "al_c7_s4", "name": "تقرير تنظيم ورش تقنية", "order": 1},
    {"id": "al_c7_s4_r002", "subcategory_id": "al_c7_s4", "name": "سجل مشاركة المعلمين في الورش", "order": 2},
    {"id": "al_c7_s4_r003", "subcategory_id": "al_c7_s4", "name": "توثيق تدريب الطلاب على التكنولوجيا", "order": 3},
    {"id": "al_c7_s4_r004", "subcategory_id": "al_c7_s4", "name": "تقرير عن ورش برمجيات", "order": 4},
    {"id": "al_c7_s4_r005", "subcategory_id": "al_c7_s4", "name": "سجل تقييم الورش", "order": 5},
    {"id": "al_c7_s4_r006", "subcategory_id": "al_c7_s4", "name": "تقرير أثر الورش على الأداء", "order": 6},
    {"id": "al_c7_s4_r007", "subcategory_id": "al_c7_s4", "name": "توثيق تطبيق المهارات", "order": 7},
    {"id": "al_c7_s4_r008", "subcategory_id": "al_c7_s4", "name": "تقرير تحديث محتوى الورش", "order": 8},
    {"id": "al_c7_s4_r009", "subcategory_id": "al_c7_s4", "name": "سبل تطوير الورش", "order": 9},
    {"id": "al_c7_s4_r010", "subcategory_id": "al_c7_s4", "name": "تقرير ختامي للورش", "order": 10},

    # ========== al_c8_s1 ==========
    {"id": "al_c8_s1_r001", "subcategory_id": "al_c8_s1", "name": "تقرير تزيين الفصل بالوسائل", "order": 1},
    {"id": "al_c8_s1_r002", "subcategory_id": "al_c8_s1", "name": "سجل الوسائل الجذابة", "order": 2},
    {"id": "al_c8_s1_r003", "subcategory_id": "al_c8_s1", "name": "توثيق مشاركة الطلاب في التزيين", "order": 3},
    {"id": "al_c8_s1_r004", "subcategory_id": "al_c8_s1", "name": "تقرير عن لوحات الفصل", "order": 4},
    {"id": "al_c8_s1_r005", "subcategory_id": "al_c8_s1", "name": "سجل تحديث الوسائل", "order": 5},
    {"id": "al_c8_s1_r006", "subcategory_id": "al_c8_s1", "name": "تقرير أثر التزيين على التحفيز", "order": 6},
    {"id": "al_c8_s1_r007", "subcategory_id": "al_c8_s1", "name": "توثيق مسابقات تزيين", "order": 7},
    {"id": "al_c8_s1_r008", "subcategory_id": "al_c8_s1", "name": "تقرير قياس رضا الطلاب", "order": 8},
    {"id": "al_c8_s1_r009", "subcategory_id": "al_c8_s1", "name": "سبل تحسين التزيين", "order": 9},
    {"id": "al_c8_s1_r010", "subcategory_id": "al_c8_s1", "name": "تقرير ختامي للتزيين", "order": 10},

    # ========== al_c8_s2 ==========
    {"id": "al_c8_s2_r001", "subcategory_id": "al_c8_s2", "name": "تقرير تنظيم الفصل للتفاعل", "order": 1},
    {"id": "al_c8_s2_r002", "subcategory_id": "al_c8_s2", "name": "سجل تسهيل الحركة", "order": 2},
    {"id": "al_c8_s2_r003", "subcategory_id": "al_c8_s2", "name": "توثيق توزيع المقاعد", "order": 3},
    {"id": "al_c8_s2_r004", "subcategory_id": "al_c8_s2", "name": "تقرير عن مرونة التنظيم", "order": 4},
    {"id": "al_c8_s2_r005", "subcategory_id": "al_c8_s2", "name": "سبل تحسين التفاعل", "order": 5},
    {"id": "al_c8_s2_r006", "subcategory_id": "al_c8_s2", "name": "تقرير أثر التنظيم", "order": 6},
    {"id": "al_c8_s2_r007", "subcategory_id": "al_c8_s2", "name": "توثيق تعديلات التنظيم", "order": 7},
    {"id": "al_c8_s2_r008", "subcategory_id": "al_c8_s2", "name": "تقرير قياس المشاركة", "order": 8},
    {"id": "al_c8_s2_r009", "subcategory_id": "al_c8_s2", "name": "سبل تطوير التنظيم", "order": 9},
    {"id": "al_c8_s2_r010", "subcategory_id": "al_c8_s2", "name": "تقرير ختامي للتنظيم", "order": 10},

    # ========== al_c8_s3 ==========
    {"id": "al_c8_s3_r001", "subcategory_id": "al_c8_s3", "name": "تقرير توفير الأدوات التعليمية", "order": 1},
    {"id": "al_c8_s3_r002", "subcategory_id": "al_c8_s3", "name": "سجل الموارد المتاحة", "order": 2},
    {"id": "al_c8_s3_r003", "subcategory_id": "al_c8_s3", "name": "توثيق استخدام الأدوات", "order": 3},
    {"id": "al_c8_s3_r004", "subcategory_id": "al_c8_s3", "name": "تقرير عن احتياجات الفصل", "order": 4},
    {"id": "al_c8_s3_r005", "subcategory_id": "al_c8_s3", "name": "سجل صيانة الأدوات", "order": 5},
    {"id": "al_c8_s3_r006", "subcategory_id": "al_c8_s3", "name": "تقرير توفير المواد", "order": 6},
    {"id": "al_c8_s3_r007", "subcategory_id": "al_c8_s3", "name": "توثيق تحديث الموارد", "order": 7},
    {"id": "al_c8_s3_r008", "subcategory_id": "al_c8_s3", "name": "تقرير قياس الكفاية", "order": 8},
    {"id": "al_c8_s3_r009", "subcategory_id": "al_c8_s3", "name": "سبل تحسين التوفير", "order": 9},
    {"id": "al_c8_s3_r010", "subcategory_id": "al_c8_s3", "name": "تقرير ختامي للموارد", "order": 10},

    # ========== al_c8_s4 ==========
    {"id": "al_c8_s4_r001", "subcategory_id": "al_c8_s4", "name": "تقرير تأمين بيئة آمنة", "order": 1},
    {"id": "al_c8_s4_r002", "subcategory_id": "al_c8_s4", "name": "سجل خلو الفصل من الأخطار", "order": 2},
    {"id": "al_c8_s4_r003", "subcategory_id": "al_c8_s4", "name": "توثيق تحقيق الأمان النفسي", "order": 3},
    {"id": "al_c8_s4_r004", "subcategory_id": "al_c8_s4", "name": "تقرير عن إجراءات السلامة", "order": 4},
    {"id": "al_c8_s4_r005", "subcategory_id": "al_c8_s4", "name": "سجل تدريب على الأمان", "order": 5},
    {"id": "al_c8_s4_r006", "subcategory_id": "al_c8_s4", "name": "تقرير فاعلية الأمان", "order": 6},
    {"id": "al_c8_s4_r007", "subcategory_id": "al_c8_s4", "name": "توثيق تحسين البيئة", "order": 7},
    {"id": "al_c8_s4_r008", "subcategory_id": "al_c8_s4", "name": "تقرير قياس الشعور بالأمان", "order": 8},
    {"id": "al_c8_s4_r009", "subcategory_id": "al_c8_s4", "name": "سبل تعزيز الأمان", "order": 9},
    {"id": "al_c8_s4_r010", "subcategory_id": "al_c8_s4", "name": "تقرير ختامي للأمان", "order": 10},

    # ========== al_c8_s5 ==========
    {"id": "al_c8_s5_r001", "subcategory_id": "al_c8_s5", "name": "تقرير تمكين التعبير عن الذات", "order": 1},
    {"id": "al_c8_s5_r002", "subcategory_id": "al_c8_s5", "name": "سجل مشاركة الأفكار", "order": 2},
    {"id": "al_c8_s5_r003", "subcategory_id": "al_c8_s5", "name": "توثيق تفاعل الطلاب", "order": 3},
    {"id": "al_c8_s5_r004", "subcategory_id": "al_c8_s5", "name": "تقرير عن مناقشات مفتوحة", "order": 4},
    {"id": "al_c8_s5_r005", "subcategory_id": "al_c8_s5", "name": "سبل تعزيز التعبير", "order": 5},
    {"id": "al_c8_s5_r006", "subcategory_id": "al_c8_s5", "name": "تقرير أثر التمكين", "order": 6},
    {"id": "al_c8_s5_r007", "subcategory_id": "al_c8_s5", "name": "توثيق تحسين الثقة", "order": 7},
    {"id": "al_c8_s5_r008", "subcategory_id": "al_c8_s5", "name": "تقرير قياس المشاركة", "order": 8},
    {"id": "al_c8_s5_r009", "subcategory_id": "al_c8_s5", "name": "سبل تطوير البيئة", "order": 9},
    {"id": "al_c8_s5_r010", "subcategory_id": "al_c8_s5", "name": "تقرير ختامي للتعبير", "order": 10},

    # ========== al_c8_s6 ==========
    {"id": "al_c8_s6_r001", "subcategory_id": "al_c8_s6", "name": "تقرير إثارة دافعية الطلاب", "order": 1},
    {"id": "al_c8_s6_r002", "subcategory_id": "al_c8_s6", "name": "سجل تنوع أساليب التحفيز", "order": 2},
    {"id": "al_c8_s6_r003", "subcategory_id": "al_c8_s6", "name": "توثيق استخدام المكافآت", "order": 3},
    {"id": "al_c8_s6_r004", "subcategory_id": "al_c8_s6", "name": "تقرير عن أنشطة تحفيزية", "order": 4},
    {"id": "al_c8_s6_r005", "subcategory_id": "al_c8_s6", "name": "سجل تفاعل الطلاب", "order": 5},
    {"id": "al_c8_s6_r006", "subcategory_id": "al_c8_s6", "name": "تقرير أثر التحفيز", "order": 6},
    {"id": "al_c8_s6_r007", "subcategory_id": "al_c8_s6", "name": "توثيق تحسين الأداء", "order": 7},
    {"id": "al_c8_s6_r008", "subcategory_id": "al_c8_s6", "name": "تقرير قياس الدافعية", "order": 8},
    {"id": "al_c8_s6_r009", "subcategory_id": "al_c8_s6", "name": "سبل تعزيز الدافعية", "order": 9},
    {"id": "al_c8_s6_r010", "subcategory_id": "al_c8_s6", "name": "تقرير ختامي للتحفيز", "order": 10},

    # ========== al_c9_s1 ==========
    {"id": "al_c9_s1_r001", "subcategory_id": "al_c9_s1", "name": "تقرير وضع قواعد السلوك", "order": 1},
    {"id": "al_c9_s1_r002", "subcategory_id": "al_c9_s1", "name": "سجل وضوح القواعد للطلاب", "order": 2},
    {"id": "al_c9_s1_r003", "subcategory_id": "al_c9_s1", "name": "توثيق مشاركة الطلاب في وضع القواعد", "order": 3},
    {"id": "al_c9_s1_r004", "subcategory_id": "al_c9_s1", "name": "تقرير عن تطبيق القواعد", "order": 4},
    {"id": "al_c9_s1_r005", "subcategory_id": "al_c9_s1", "name": "سجل متابعة الالتزام", "order": 5},
    {"id": "al_c9_s1_r006", "subcategory_id": "al_c9_s1", "name": "تقرير تحديث القواعد", "order": 6},
    {"id": "al_c9_s1_r007", "subcategory_id": "al_c9_s1", "name": "توثيق تقييم القواعد", "order": 7},
    {"id": "al_c9_s1_r008", "subcategory_id": "al_c9_s1", "name": "تقرير أثر القواعد", "order": 8},
    {"id": "al_c9_s1_r009", "subcategory_id": "al_c9_s1", "name": "سبل تحسين القواعد", "order": 9},
    {"id": "al_c9_s1_r010", "subcategory_id": "al_c9_s1", "name": "تقرير ختامي للقواعد", "order": 10},

    # ========== al_c9_s2 ==========
    {"id": "al_c9_s2_r001", "subcategory_id": "al_c9_s2", "name": "تقرير استخدام أساليب تحفيزية", "order": 1},
    {"id": "al_c9_s2_r002", "subcategory_id": "al_c9_s2", "name": "سجل تحفيز الالتزام", "order": 2},
    {"id": "al_c9_s2_r003", "subcategory_id": "al_c9_s2", "name": "توثيق المكافآت المعنوية", "order": 3},
    {"id": "al_c9_s2_r004", "subcategory_id": "al_c9_s2", "name": "تقرير عن نظام التعزيز", "order": 4},
    {"id": "al_c9_s2_r005", "subcategory_id": "al_c9_s2", "name": "سجل استجابة الطلاب", "order": 5},
    {"id": "al_c9_s2_r006", "subcategory_id": "al_c9_s2", "name": "تقرير فاعلية التحفيز", "order": 6},
    {"id": "al_c9_s2_r007", "subcategory_id": "al_c9_s2", "name": "توثيق تحسين السلوك", "order": 7},
    {"id": "al_c9_s2_r008", "subcategory_id": "al_c9_s2", "name": "تقرير قياس الدافعية", "order": 8},
    {"id": "al_c9_s2_r009", "subcategory_id": "al_c9_s2", "name": "سبل تطوير التحفيز", "order": 9},
    {"id": "al_c9_s2_r010", "subcategory_id": "al_c9_s2", "name": "تقرير ختامي للتحفيز", "order": 10},

    # ========== al_c9_s3 ==========
    {"id": "al_c9_s3_r001", "subcategory_id": "al_c9_s3", "name": "تقرير التعامل مع المشكلات السلوكية", "order": 1},
    {"id": "al_c9_s3_r002", "subcategory_id": "al_c9_s3", "name": "سجل الإجراءات العادلة", "order": 2},
    {"id": "al_c9_s3_r003", "subcategory_id": "al_c9_s3", "name": "توثيق حل النزاعات", "order": 3},
    {"id": "al_c9_s3_r004", "subcategory_id": "al_c9_s3", "name": "تقرير عن استراتيجيات الحزم", "order": 4},
    {"id": "al_c9_s3_r005", "subcategory_id": "al_c9_s3", "name": "سجل متابعة الحالات", "order": 5},
    {"id": "al_c9_s3_r006", "subcategory_id": "al_c9_s3", "name": "تقرير فاعلية التدخلات", "order": 6},
    {"id": "al_c9_s3_r007", "subcategory_id": "al_c9_s3", "name": "توثيق تحسين السلوك", "order": 7},
    {"id": "al_c9_s3_r008", "subcategory_id": "al_c9_s3", "name": "تقرير قياس الانضباط", "order": 8},
    {"id": "al_c9_s3_r009", "subcategory_id": "al_c9_s3", "name": "سبل تحسين التعامل", "order": 9},
    {"id": "al_c9_s3_r010", "subcategory_id": "al_c9_s3", "name": "تقرير ختامي للسلوك", "order": 10},

    # ========== al_c9_s4 ==========
    {"id": "al_c9_s4_r001", "subcategory_id": "al_c9_s4", "name": "تقرير تنظيم الوقت في الحصة", "order": 1},
    {"id": "al_c9_s4_r002", "subcategory_id": "al_c9_s4", "name": "سجل إدارة الوقت بفعالية", "order": 2},
    {"id": "al_c9_s4_r003", "subcategory_id": "al_c9_s4", "name": "توثيق توزيع الأنشطة زمنياً", "order": 3},
    {"id": "al_c9_s4_r004", "subcategory_id": "al_c9_s4", "name": "تقرير عن جدول الحصة", "order": 4},
    {"id": "al_c9_s4_r005", "subcategory_id": "al_c9_s4", "name": "سجل التزام الطلاب بالوقت", "order": 5},
    {"id": "al_c9_s4_r006", "subcategory_id": "al_c9_s4", "name": "تقرير فاعلية التنظيم", "order": 6},
    {"id": "al_c9_s4_r007", "subcategory_id": "al_c9_s4", "name": "توثيق تحسين الإدارة", "order": 7},
    {"id": "al_c9_s4_r008", "subcategory_id": "al_c9_s4", "name": "تقرير قياس الإنتاجية", "order": 8},
    {"id": "al_c9_s4_r009", "subcategory_id": "al_c9_s4", "name": "سبل تطوير الوقت", "order": 9},
    {"id": "al_c9_s4_r010", "subcategory_id": "al_c9_s4", "name": "تقرير ختامي لإدارة الوقت", "order": 10},

    # ========== al_c10_s1 ==========
    {"id": "al_c10_s1_r001", "subcategory_id": "al_c10_s1", "name": "تقرير استخدام اختبارات دورية", "order": 1},
    {"id": "al_c10_s1_r002", "subcategory_id": "al_c10_s1", "name": "سجل قياس تقدم الطلاب", "order": 2},
    {"id": "al_c10_s1_r003", "subcategory_id": "al_c10_s1", "name": "توثيق نتائج الاختبارات", "order": 3},
    {"id": "al_c10_s1_r004", "subcategory_id": "al_c10_s1", "name": "تقرير عن تحليل الاختبارات", "order": 4},
    {"id": "al_c10_s1_r005", "subcategory_id": "al_c10_s1", "name": "سجل تنويع أدوات التقييم", "order": 5},
    {"id": "al_c10_s1_r006", "subcategory_id": "al_c10_s1", "name": "تقرير فاعلية الاختبارات", "order": 6},
    {"id": "al_c10_s1_r007", "subcategory_id": "al_c10_s1", "name": "توثيق تحسين الأداء", "order": 7},
    {"id": "al_c10_s1_r008", "subcategory_id": "al_c10_s1", "name": "تقرير تحديث الاختبارات", "order": 8},
    {"id": "al_c10_s1_r009", "subcategory_id": "al_c10_s1", "name": "سبل تطوير التقييم", "order": 9},
    {"id": "al_c10_s1_r010", "subcategory_id": "al_c10_s1", "name": "تقرير ختامي للتقييم", "order": 10},

    # ========== al_c10_s2 ==========
    {"id": "al_c10_s2_r001", "subcategory_id": "al_c10_s2", "name": "تقرير تحليل نقاط القوة والضعف", "order": 1},
    {"id": "al_c10_s2_r002", "subcategory_id": "al_c10_s2", "name": "سجل إشراك الطلاب في التحليل", "order": 2},
    {"id": "al_c10_s2_r003", "subcategory_id": "al_c10_s2", "name": "توثيق ملاحظات التطور", "order": 3},
    {"id": "al_c10_s2_r004", "subcategory_id": "al_c10_s2", "name": "تقرير عن فهم الطلاب لنتائجهم", "order": 4},
    {"id": "al_c10_s2_r005", "subcategory_id": "al_c10_s2", "name": "سجل خطط التحسين", "order": 5},
    {"id": "al_c10_s2_r006", "subcategory_id": "al_c10_s2", "name": "تقرير فاعلية التحليل", "order": 6},
    {"id": "al_c10_s2_r007", "subcategory_id": "al_c10_s2", "name": "توثيق تحسين النتائج", "order": 7},
    {"id": "al_c10_s2_r008", "subcategory_id": "al_c10_s2", "name": "تقرير قياس التقدم", "order": 8},
    {"id": "al_c10_s2_r009", "subcategory_id": "al_c10_s2", "name": "سبل تطوير التحليل", "order": 9},
    {"id": "al_c10_s2_r010", "subcategory_id": "al_c10_s2", "name": "تقرير ختامي للتحليل", "order": 10},

    # ========== al_c10_s3 ==========
    {"id": "al_c10_s3_r001", "subcategory_id": "al_c10_s3", "name": "تقرير توفير تغذية راجعة فردية", "order": 1},
    {"id": "al_c10_s3_r002", "subcategory_id": "al_c10_s3", "name": "سجل ملاحظات لكل طالب", "order": 2},
    {"id": "al_c10_s3_r003", "subcategory_id": "al_c10_s3", "name": "توثيق متابعة التقدم الفردي", "order": 3},
    {"id": "al_c10_s3_r004", "subcategory_id": "al_c10_s3", "name": "تقرير عن جلسات فردية", "order": 4},
    {"id": "al_c10_s3_r005", "subcategory_id": "al_c10_s3", "name": "سجل استجابة الطلاب", "order": 5},
    {"id": "al_c10_s3_r006", "subcategory_id": "al_c10_s3", "name": "تقرير فاعلية التغذية", "order": 6},
    {"id": "al_c10_s3_r007", "subcategory_id": "al_c10_s3", "name": "توثيق تحسين الأداء", "order": 7},
    {"id": "al_c10_s3_r008", "subcategory_id": "al_c10_s3", "name": "تقرير قياس الرضا", "order": 8},
    {"id": "al_c10_s3_r009", "subcategory_id": "al_c10_s3", "name": "سبل تطوير التغذية", "order": 9},
    {"id": "al_c10_s3_r010", "subcategory_id": "al_c10_s3", "name": "تقرير ختامي للتغذية", "order": 10},

    # ========== al_c10_s4 ==========
    {"id": "al_c10_s4_r001", "subcategory_id": "al_c10_s4", "name": "تقرير تطبيق خطط علاجية", "order": 1},
    {"id": "al_c10_s4_r002", "subcategory_id": "al_c10_s4", "name": "سجل دعم الطلاب المحتاجين", "order": 2},
    {"id": "al_c10_s4_r003", "subcategory_id": "al_c10_s4", "name": "توثيق متابعة الخطة العلاجية", "order": 3},
    {"id": "al_c10_s4_r004", "subcategory_id": "al_c10_s4", "name": "تقرير عن برامج التقوية", "order": 4},
    {"id": "al_c10_s4_r005", "subcategory_id": "al_c10_s4", "name": "سجل تقييم الخطة", "order": 5},
    {"id": "al_c10_s4_r006", "subcategory_id": "al_c10_s4", "name": "تقرير فاعلية العلاج", "order": 6},
    {"id": "al_c10_s4_r007", "subcategory_id": "al_c10_s4", "name": "توثيق تحسين المستوى", "order": 7},
    {"id": "al_c10_s4_r008", "subcategory_id": "al_c10_s4", "name": "تقرير قياس التقدم", "order": 8},
    {"id": "al_c10_s4_r009", "subcategory_id": "al_c10_s4", "name": "سبل تطوير الخطط", "order": 9},
    {"id": "al_c10_s4_r010", "subcategory_id": "al_c10_s4", "name": "تقرير ختامي للخطط", "order": 10},

    # ========== al_c10_s5 ==========
    {"id": "al_c10_s5_r001", "subcategory_id": "al_c10_s5", "name": "تقرير قياس التطبيق العملي", "order": 1},
    {"id": "al_c10_s5_r002", "subcategory_id": "al_c10_s5", "name": "سجل مشاريع تطبيقية", "order": 2},
    {"id": "al_c10_s5_r003", "subcategory_id": "al_c10_s5", "name": "توثيق مواقف حقيقية", "order": 3},
    {"id": "al_c10_s5_r004", "subcategory_id": "al_c10_s5", "name": "تقرير عن تقييم الأداء العملي", "order": 4},
    {"id": "al_c10_s5_r005", "subcategory_id": "al_c10_s5", "name": "سجل تطبيق المعرفة", "order": 5},
    {"id": "al_c10_s5_r006", "subcategory_id": "al_c10_s5", "name": "تقرير فاعلية التطبيق", "order": 6},
    {"id": "al_c10_s5_r007", "subcategory_id": "al_c10_s5", "name": "توثيق تحسين المهارات", "order": 7},
    {"id": "al_c10_s5_r008", "subcategory_id": "al_c10_s5", "name": "تقرير قياس الكفاءة", "order": 8},
    {"id": "al_c10_s5_r009", "subcategory_id": "al_c10_s5", "name": "سبل تطوير القياس", "order": 9},
    {"id": "al_c10_s5_r010", "subcategory_id": "al_c10_s5", "name": "تقرير ختامي للتطبيق", "order": 10},

    # ========== al_c11_s1 ==========
    {"id": "al_c11_s1_r001", "subcategory_id": "al_c11_s1", "name": "تقرير استخدام الاختبارات الكتابية", "order": 1},
    {"id": "al_c11_s1_r002", "subcategory_id": "al_c11_s1", "name": "سجل الاختبارات الشفوية", "order": 2},
    {"id": "al_c11_s1_r003", "subcategory_id": "al_c11_s1", "name": "توثيق تنوع أدوات التقويم", "order": 3},
    {"id": "al_c11_s1_r004", "subcategory_id": "al_c11_s1", "name": "تقرير عن موازنة بين الكتابي والشفوي", "order": 4},
    {"id": "al_c11_s1_r005", "subcategory_id": "al_c11_s1", "name": "سجل نتائج الاختبارات", "order": 5},
    {"id": "al_c11_s1_r006", "subcategory_id": "al_c11_s1", "name": "تقرير فاعلية التنوع", "order": 6},
    {"id": "al_c11_s1_r007", "subcategory_id": "al_c11_s1", "name": "توثيق تحسين الأداء", "order": 7},
    {"id": "al_c11_s1_r008", "subcategory_id": "al_c11_s1", "name": "تقرير تحديث الاختبارات", "order": 8},
    {"id": "al_c11_s1_r009", "subcategory_id": "al_c11_s1", "name": "سبل تطوير التقويم", "order": 9},
    {"id": "al_c11_s1_r010", "subcategory_id": "al_c11_s1", "name": "تقرير ختامي للاختبارات", "order": 10},

    # ========== al_c11_s2 ==========
    {"id": "al_c11_s2_r001", "subcategory_id": "al_c11_s2", "name": "تقرير تقييم المشاريع", "order": 1},
    {"id": "al_c11_s2_r002", "subcategory_id": "al_c11_s2", "name": "سجل العروض التقديمية", "order": 2},
    {"id": "al_c11_s2_r003", "subcategory_id": "al_c11_s2", "name": "توثيق معايير التقييم العملي", "order": 3},
    {"id": "al_c11_s2_r004", "subcategory_id": "al_c11_s2", "name": "تقرير عن تقييم الأداء", "order": 4},
    {"id": "al_c11_s2_r005", "subcategory_id": "al_c11_s2", "name": "سجل ملاحظات المحكمين", "order": 5},
    {"id": "al_c11_s2_r006", "subcategory_id": "al_c11_s2", "name": "تقرير فاعلية التقييم العملي", "order": 6},
    {"id": "al_c11_s2_r007", "subcategory_id": "al_c11_s2", "name": "توثيق تحسين المشاريع", "order": 7},
    {"id": "al_c11_s2_r008", "subcategory_id": "al_c11_s2", "name": "تقرير قياس المهارات", "order": 8},
    {"id": "al_c11_s2_r009", "subcategory_id": "al_c11_s2", "name": "سبل تطوير التقييم", "order": 9},
    {"id": "al_c11_s2_r010", "subcategory_id": "al_c11_s2", "name": "تقرير ختامي للتقييم العملي", "order": 10},

    # ========== al_c11_s3 ==========
    {"id": "al_c11_s3_r001", "subcategory_id": "al_c11_s3", "name": "تقرير استخدام التقييم التكويني", "order": 1},
    {"id": "al_c11_s3_r002", "subcategory_id": "al_c11_s3", "name": "سجل متابعة التقدم المستمر", "order": 2},
    {"id": "al_c11_s3_r003", "subcategory_id": "al_c11_s3", "name": "توثيق ملاحظات يومية", "order": 3},
    {"id": "al_c11_s3_r004", "subcategory_id": "al_c11_s3", "name": "تقرير عن تغذية راجعة تكوينية", "order": 4},
    {"id": "al_c11_s3_r005", "subcategory_id": "al_c11_s3", "name": "سجل تحسين الأداء", "order": 5},
    {"id": "al_c11_s3_r006", "subcategory_id": "al_c11_s3", "name": "تقرير فاعلية التقييم", "order": 6},
    {"id": "al_c11_s3_r007", "subcategory_id": "al_c11_s3", "name": "توثيق تعديل الخطط", "order": 7},
    {"id": "al_c11_s3_r008", "subcategory_id": "al_c11_s3", "name": "تقرير قياس التفاعل", "order": 8},
    {"id": "al_c11_s3_r009", "subcategory_id": "al_c11_s3", "name": "سبل تطوير التقييم", "order": 9},
    {"id": "al_c11_s3_r010", "subcategory_id": "al_c11_s3", "name": "تقرير ختامي للتكويني", "order": 10},

    # ========== al_c11_s4 ==========
    {"id": "al_c11_s4_r001", "subcategory_id": "al_c11_s4", "name": "تقرير استخدام التقويم القبلي", "order": 1},
    {"id": "al_c11_s4_r002", "subcategory_id": "al_c11_s4", "name": "سجل تشخيص استعداد الطلاب", "order": 2},
    {"id": "al_c11_s4_r003", "subcategory_id": "al_c11_s4", "name": "توثيق قياس الخبرات السابقة", "order": 3},
    {"id": "al_c11_s4_r004", "subcategory_id": "al_c11_s4", "name": "تقرير عن اختبار قبلي", "order": 4},
    {"id": "al_c11_s4_r005", "subcategory_id": "al_c11_s4", "name": "سجل نتائج التقويم", "order": 5},
    {"id": "al_c11_s4_r006", "subcategory_id": "al_c11_s4", "name": "تقرير تكييف التدريس", "order": 6},
    {"id": "al_c11_s4_r007", "subcategory_id": "al_c11_s4", "name": "توثيق تحسين التخطيط", "order": 7},
    {"id": "al_c11_s4_r008", "subcategory_id": "al_c11_s4", "name": "تقرير فاعلية القبلي", "order": 8},
    {"id": "al_c11_s4_r009", "subcategory_id": "al_c11_s4", "name": "سبل تطوير التقويم", "order": 9},
    {"id": "al_c11_s4_r010", "subcategory_id": "al_c11_s4", "name": "تقرير ختامي للقبلي", "order": 10},

    # ========== al_c11_s5 ==========
    {"id": "al_c11_s5_r001", "subcategory_id": "al_c11_s5", "name": "تقرير تطبيق التقويم الختامي", "order": 1},
    {"id": "al_c11_s5_r002", "subcategory_id": "al_c11_s5", "name": "سجل قياس تحقيق الأهداف", "order": 2},
    {"id": "al_c11_s5_r003", "subcategory_id": "al_c11_s5", "name": "توثيق أحكام مستويات الطلاب", "order": 3},
    {"id": "al_c11_s5_r004", "subcategory_id": "al_c11_s5", "name": "تقرير عن نتائج الفصل", "order": 4},
    {"id": "al_c11_s5_r005", "subcategory_id": "al_c11_s5", "name": "سجل تحليل النتائج الختامية", "order": 5},
    {"id": "al_c11_s5_r006", "subcategory_id": "al_c11_s5", "name": "تقرير فاعلية التقويم", "order": 6},
    {"id": "al_c11_s5_r007", "subcategory_id": "al_c11_s5", "name": "توثيق توصيات للتحسين", "order": 7},
    {"id": "al_c11_s5_r008", "subcategory_id": "al_c11_s5", "name": "تقرير قياس التقدم", "order": 8},
    {"id": "al_c11_s5_r009", "subcategory_id": "al_c11_s5", "name": "سبل تطوير الختامي", "order": 9},
    {"id": "al_c11_s5_r010", "subcategory_id": "al_c11_s5", "name": "تقرير ختامي للتقويم", "order": 10},

    # ========== al_c12_s1 ==========
    {"id": "al_c12_s1_r001", "subcategory_id": "al_c12_s1", "name": "تقرير تحليل الواقع الفعلي للمدرسة", "order": 1},
    {"id": "al_c12_s1_r002", "subcategory_id": "al_c12_s1", "name": "سجل احتياجات الأنشطة", "order": 2},
    {"id": "al_c12_s1_r003", "subcategory_id": "al_c12_s1", "name": "توثيق الإمكانات المتاحة", "order": 3},
    {"id": "al_c12_s1_r004", "subcategory_id": "al_c12_s1", "name": "تقرير عن استبيان للمجتمع المدرسي", "order": 4},
    {"id": "al_c12_s1_r005", "subcategory_id": "al_c12_s1", "name": "سجل تحليل نقاط القوة والضعف", "order": 5},
    {"id": "al_c12_s1_r006", "subcategory_id": "al_c12_s1", "name": "تقرير توصيات التحليل", "order": 6},
    {"id": "al_c12_s1_r007", "subcategory_id": "al_c12_s1", "name": "توثيق مشاركة المعلمين في التحليل", "order": 7},
    {"id": "al_c12_s1_r008", "subcategory_id": "al_c12_s1", "name": "تقرير تحديث التحليل", "order": 8},
    {"id": "al_c12_s1_r009", "subcategory_id": "al_c12_s1", "name": "سبل تحسين التحليل", "order": 9},
    {"id": "al_c12_s1_r010", "subcategory_id": "al_c12_s1", "name": "تقرير ختامي للتحليل", "order": 10},

    # ========== al_c12_s2 ==========
    {"id": "al_c12_s2_r001", "subcategory_id": "al_c12_s2", "name": "تقرير تصميم خطة البرامج", "order": 1},
    {"id": "al_c12_s2_r002", "subcategory_id": "al_c12_s2", "name": "سجل عناصر الخطة", "order": 2},
    {"id": "al_c12_s2_r003", "subcategory_id": "al_c12_s2", "name": "توثيق توافق الخطة مع وزارة التعليم", "order": 3},
    {"id": "al_c12_s2_r004", "subcategory_id": "al_c12_s2", "name": "تقرير عن أهداف الخطة", "order": 4},
    {"id": "al_c12_s2_r005", "subcategory_id": "al_c12_s2", "name": "سجل اعتماد الخطة", "order": 5},
    {"id": "al_c12_s2_r006", "subcategory_id": "al_c12_s2", "name": "تقرير توزيع الخطة", "order": 6},
    {"id": "al_c12_s2_r007", "subcategory_id": "al_c12_s2", "name": "توثيق مشاركة الطلاب", "order": 7},
    {"id": "al_c12_s2_r008", "subcategory_id": "al_c12_s2", "name": "تقرير مراجعة الخطة", "order": 8},
    {"id": "al_c12_s2_r009", "subcategory_id": "al_c12_s2", "name": "سبل تطوير الخطة", "order": 9},
    {"id": "al_c12_s2_r010", "subcategory_id": "al_c12_s2", "name": "تقرير ختامي للتصميم", "order": 10},

    # ========== al_c12_s3 ==========
    {"id": "al_c12_s3_r001", "subcategory_id": "al_c12_s3", "name": "تقرير قياس أثر البرامج", "order": 1},
    {"id": "al_c12_s3_r002", "subcategory_id": "al_c12_s3", "name": "سجل تحليل نتائج الأنشطة", "order": 2},
    {"id": "al_c12_s3_r003", "subcategory_id": "al_c12_s3", "name": "توثيق استبيانات الرضا", "order": 3},
    {"id": "al_c12_s3_r004", "subcategory_id": "al_c12_s3", "name": "تقرير عن أثر على الطلاب", "order": 4},
    {"id": "al_c12_s3_r005", "subcategory_id": "al_c12_s3", "name": "سجل توصيات التحسين", "order": 5},
    {"id": "al_c12_s3_r006", "subcategory_id": "al_c12_s3", "name": "تقرير فاعلية القياس", "order": 6},
    {"id": "al_c12_s3_r007", "subcategory_id": "al_c12_s3", "name": "توثيق تحسين البرامج", "order": 7},
    {"id": "al_c12_s3_r008", "subcategory_id": "al_c12_s3", "name": "تقرير تحديث القياس", "order": 8},
    {"id": "al_c12_s3_r009", "subcategory_id": "al_c12_s3", "name": "سبل تطوير الأثر", "order": 9},
    {"id": "al_c12_s3_r010", "subcategory_id": "al_c12_s3", "name": "تقرير ختامي لقياس الأثر", "order": 10},

    # ========== al_c13_s1 ==========
    {"id": "al_c13_s1_r001", "subcategory_id": "al_c13_s1", "name": "تقرير تنظيم البيئة المدرسية", "order": 1},
    {"id": "al_c13_s1_r002", "subcategory_id": "al_c13_s1", "name": "سجل تجهيز آمن للأنشطة", "order": 2},
    {"id": "al_c13_s1_r003", "subcategory_id": "al_c13_s1", "name": "توثيق فعالية التجهيز", "order": 3},
    {"id": "al_c13_s1_r004", "subcategory_id": "al_c13_s1", "name": "تقرير عن سلامة المرافق", "order": 4},
    {"id": "al_c13_s1_r005", "subcategory_id": "al_c13_s1", "name": "سجل متابعة النظافة", "order": 5},
    {"id": "al_c13_s1_r006", "subcategory_id": "al_c13_s1", "name": "تقرير توفير الموارد", "order": 6},
    {"id": "al_c13_s1_r007", "subcategory_id": "al_c13_s1", "name": "توثيق تحسين البيئة", "order": 7},
    {"id": "al_c13_s1_r008", "subcategory_id": "al_c13_s1", "name": "تقرير قياس الجاهزية", "order": 8},
    {"id": "al_c13_s1_r009", "subcategory_id": "al_c13_s1", "name": "سبل تطوير التجهيز", "order": 9},
    {"id": "al_c13_s1_r010", "subcategory_id": "al_c13_s1", "name": "تقرير ختامي للبيئة", "order": 10},

    # ========== al_c14_s1 ==========
    {"id": "al_c14_s1_r001", "subcategory_id": "al_c14_s1", "name": "تقرير حصر هوايات الطلاب", "order": 1},
    {"id": "al_c14_s1_r002", "subcategory_id": "al_c14_s1", "name": "سجل قاعدة بيانات الهوايات", "order": 2},
    {"id": "al_c14_s1_r003", "subcategory_id": "al_c14_s1", "name": "توثيق استبيانات الميول", "order": 3},
    {"id": "al_c14_s1_r004", "subcategory_id": "al_c14_s1", "name": "تقرير عن تنوع الهوايات", "order": 4},
    {"id": "al_c14_s1_r005", "subcategory_id": "al_c14_s1", "name": "سجل تحديث الحصر", "order": 5},
    {"id": "al_c14_s1_r006", "subcategory_id": "al_c14_s1", "name": "تقرير مشاركة الطلاب", "order": 6},
    {"id": "al_c14_s1_r007", "subcategory_id": "al_c14_s1", "name": "توثيق تحليل الهوايات", "order": 7},
    {"id": "al_c14_s1_r008", "subcategory_id": "al_c14_s1", "name": "تقرير توصيات للأنشطة", "order": 8},
    {"id": "al_c14_s1_r009", "subcategory_id": "al_c14_s1", "name": "سبل تحسين الحصر", "order": 9},
    {"id": "al_c14_s1_r010", "subcategory_id": "al_c14_s1", "name": "تقرير ختامي للحصر", "order": 10},

    # ========== al_c14_s2 ==========
    {"id": "al_c14_s2_r001", "subcategory_id": "al_c14_s2", "name": "تقرير حصر إمكانيات المدرسة", "order": 1},
    {"id": "al_c14_s2_r002", "subcategory_id": "al_c14_s2", "name": "سجل الموارد المتاحة للأنشطة", "order": 2},
    {"id": "al_c14_s2_r003", "subcategory_id": "al_c14_s2", "name": "توثيق مرافق المدرسة", "order": 3},
    {"id": "al_c14_s2_r004", "subcategory_id": "al_c14_s2", "name": "تقرير عن تجهيزات الأنشطة", "order": 4},
    {"id": "al_c14_s2_r005", "subcategory_id": "al_c14_s2", "name": "سجل تحديث الإمكانيات", "order": 5},
    {"id": "al_c14_s2_r006", "subcategory_id": "al_c14_s2", "name": "تقرير استغلال الإمكانيات", "order": 6},
    {"id": "al_c14_s2_r007", "subcategory_id": "al_c14_s2", "name": "توثيق تحسين الموارد", "order": 7},
    {"id": "al_c14_s2_r008", "subcategory_id": "al_c14_s2", "name": "تقرير قياس الكفاية", "order": 8},
    {"id": "al_c14_s2_r009", "subcategory_id": "al_c14_s2", "name": "سبل تطوير الحصر", "order": 9},
    {"id": "al_c14_s2_r010", "subcategory_id": "al_c14_s2", "name": "تقرير ختامي للإمكانيات", "order": 10},

    # ========== al_c14_s3 ==========
    {"id": "al_c14_s3_r001", "subcategory_id": "al_c14_s3", "name": "تقرير البحث عن شراكات اجتماعية", "order": 1},
    {"id": "al_c14_s3_r002", "subcategory_id": "al_c14_s3", "name": "سجل الاتفاقيات مع مؤسسات", "order": 2},
    {"id": "al_c14_s3_r003", "subcategory_id": "al_c14_s3", "name": "توثيق تنفيذ أنشطة لاصفية", "order": 3},
    {"id": "al_c14_s3_r004", "subcategory_id": "al_c14_s3", "name": "تقرير عن شراكات ناجحة", "order": 4},
    {"id": "al_c14_s3_r005", "subcategory_id": "al_c14_s3", "name": "سجل تقييم الشركاء", "order": 5},
    {"id": "al_c14_s3_r006", "subcategory_id": "al_c14_s3", "name": "تقرير استدامة الشراكات", "order": 6},
    {"id": "al_c14_s3_r007", "subcategory_id": "al_c14_s3", "name": "توثيق أثر الشراكات", "order": 7},
    {"id": "al_c14_s3_r008", "subcategory_id": "al_c14_s3", "name": "تقرير توسيع الشراكات", "order": 8},
    {"id": "al_c14_s3_r009", "subcategory_id": "al_c14_s3", "name": "سبل تحسين البحث", "order": 9},
    {"id": "al_c14_s3_r010", "subcategory_id": "al_c14_s3", "name": "تقرير ختامي للشراكات", "order": 10},

    # ========== al_c14_s4 ==========
    {"id": "al_c14_s4_r001", "subcategory_id": "al_c14_s4", "name": "تقرير توجيه الطلاب للأنشطة", "order": 1},
    {"id": "al_c14_s4_r002", "subcategory_id": "al_c14_s4", "name": "سجل توزيع الطلاب حسب الميول", "order": 2},
    {"id": "al_c14_s4_r003", "subcategory_id": "al_c14_s4", "name": "توثيق برامج إرشادية", "order": 3},
    {"id": "al_c14_s4_r004", "subcategory_id": "al_c14_s4", "name": "تقرير عن ملاءمة الأنشطة", "order": 4},
    {"id": "al_c14_s4_r005", "subcategory_id": "al_c14_s4", "name": "سجل متابعة رضا الطلاب", "order": 5},
    {"id": "al_c14_s4_r006", "subcategory_id": "al_c14_s4", "name": "تقرير فاعلية التوجيه", "order": 6},
    {"id": "al_c14_s4_r007", "subcategory_id": "al_c14_s4", "name": "توثيق تحسين المشاركة", "order": 7},
    {"id": "al_c14_s4_r008", "subcategory_id": "al_c14_s4", "name": "تقرير قياس التوجيه", "order": 8},
    {"id": "al_c14_s4_r009", "subcategory_id": "al_c14_s4", "name": "سبل تطوير التوجيه", "order": 9},
    {"id": "al_c14_s4_r010", "subcategory_id": "al_c14_s4", "name": "تقرير ختامي للتوجيه", "order": 10},

    # ========== al_c14_s5 ==========
    {"id": "al_c14_s5_r001", "subcategory_id": "al_c14_s5", "name": "تقرير تقديم تغذية راجعة للمتعلمين", "order": 1},
    {"id": "al_c14_s5_r002", "subcategory_id": "al_c14_s5", "name": "سجل نقاط القوة والتحسين", "order": 2},
    {"id": "al_c14_s5_r003", "subcategory_id": "al_c14_s5", "name": "توثيق متابعة التطور", "order": 3},
    {"id": "al_c14_s5_r004", "subcategory_id": "al_c14_s5", "name": "تقرير عن جلسات تغذية", "order": 4},
    {"id": "al_c14_s5_r005", "subcategory_id": "al_c14_s5", "name": "سجل استجابة الطلاب", "order": 5},
    {"id": "al_c14_s5_r006", "subcategory_id": "al_c14_s5", "name": "تقرير فاعلية التغذية", "order": 6},
    {"id": "al_c14_s5_r007", "subcategory_id": "al_c14_s5", "name": "توثيق تحسين الأداء", "order": 7},
    {"id": "al_c14_s5_r008", "subcategory_id": "al_c14_s5", "name": "تقرير قياس الرضا", "order": 8},
    {"id": "al_c14_s5_r009", "subcategory_id": "al_c14_s5", "name": "سبل تطوير التغذية", "order": 9},
    {"id": "al_c14_s5_r010", "subcategory_id": "al_c14_s5", "name": "تقرير ختامي للتغذية", "order": 10},

    # ========== al_c15_s1 ==========
    {"id": "al_c15_s1_r001", "subcategory_id": "al_c15_s1", "name": "تقرير تشجيع المشاركة داخل المدرسة", "order": 1},
    {"id": "al_c15_s1_r002", "subcategory_id": "al_c15_s1", "name": "سجل أنشطة داخلية", "order": 2},
    {"id": "al_c15_s1_r003", "subcategory_id": "al_c15_s1", "name": "توثيق تفاعل الطلاب", "order": 3},
    {"id": "al_c15_s1_r004", "subcategory_id": "al_c15_s1", "name": "تقرير عن مسابقات داخلية", "order": 4},
    {"id": "al_c15_s1_r005", "subcategory_id": "al_c15_s1", "name": "سجل أندية مدرسية", "order": 5},
    {"id": "al_c15_s1_r006", "subcategory_id": "al_c15_s1", "name": "تقرير فاعلية التحفيز", "order": 6},
    {"id": "al_c15_s1_r007", "subcategory_id": "al_c15_s1", "name": "توثيق زيادة المشاركة", "order": 7},
    {"id": "al_c15_s1_r008", "subcategory_id": "al_c15_s1", "name": "تقرير قياس الإقبال", "order": 8},
    {"id": "al_c15_s1_r009", "subcategory_id": "al_c15_s1", "name": "سبل تطوير التشجيع", "order": 9},
    {"id": "al_c15_s1_r010", "subcategory_id": "al_c15_s1", "name": "تقرير ختامي للمشاركة", "order": 10},

    # ========== al_c15_s2 ==========
    {"id": "al_c15_s2_r001", "subcategory_id": "al_c15_s2", "name": "تقرير تشجيع المشاركة خارج المدرسة", "order": 1},
    {"id": "al_c15_s2_r002", "subcategory_id": "al_c15_s2", "name": "سجل مشاركات خارجية", "order": 2},
    {"id": "al_c15_s2_r003", "subcategory_id": "al_c15_s2", "name": "توثيق مسابقات خارجية", "order": 3},
    {"id": "al_c15_s2_r004", "subcategory_id": "al_c15_s2", "name": "تقرير عن فعاليات مجتمعية", "order": 4},
    {"id": "al_c15_s2_r005", "subcategory_id": "al_c15_s2", "name": "سجل تنسيق مع جهات خارجية", "order": 5},
    {"id": "al_c15_s2_r006", "subcategory_id": "al_c15_s2", "name": "تقرير فاعلية التشجيع", "order": 6},
    {"id": "al_c15_s2_r007", "subcategory_id": "al_c15_s2", "name": "توثيق تحسين المهارات", "order": 7},
    {"id": "al_c15_s2_r008", "subcategory_id": "al_c15_s2", "name": "تقرير قياس المشاركة", "order": 8},
    {"id": "al_c15_s2_r009", "subcategory_id": "al_c15_s2", "name": "سبل تطوير الخارجية", "order": 9},
    {"id": "al_c15_s2_r010", "subcategory_id": "al_c15_s2", "name": "تقرير ختامي للخارجية", "order": 10},

    # ========== al_c15_s3 ==========
    {"id": "al_c15_s3_r001", "subcategory_id": "al_c15_s3", "name": "تقرير تنمية قدرات الطلاب خارج المنهج", "order": 1},
    {"id": "al_c15_s3_r002", "subcategory_id": "al_c15_s3", "name": "سجل برامج تنموية", "order": 2},
    {"id": "al_c15_s3_r003", "subcategory_id": "al_c15_s3", "name": "توثيق ورش مهارية", "order": 3},
    {"id": "al_c15_s3_r004", "subcategory_id": "al_c15_s3", "name": "تقرير عن دورات تدريبية", "order": 4},
    {"id": "al_c15_s3_r005", "subcategory_id": "al_c15_s3", "name": "سجل تحسين القدرات", "order": 5},
    {"id": "al_c15_s3_r006", "subcategory_id": "al_c15_s3", "name": "تقرير فاعلية التنمية", "order": 6},
    {"id": "al_c15_s3_r007", "subcategory_id": "al_c15_s3", "name": "توثيق إنجازات الطلاب", "order": 7},
    {"id": "al_c15_s3_r008", "subcategory_id": "al_c15_s3", "name": "تقرير قياس التطور", "order": 8},
    {"id": "al_c15_s3_r009", "subcategory_id": "al_c15_s3", "name": "سبل تطوير التنمية", "order": 9},
    {"id": "al_c15_s3_r010", "subcategory_id": "al_c15_s3", "name": "تقرير ختامي للتنمية", "order": 10},

    # ========== al_c15_s4 ==========
    {"id": "al_c15_s4_r001", "subcategory_id": "al_c15_s4", "name": "تقرير تعزيز قيم الطلاب", "order": 1},
    {"id": "al_c15_s4_r002", "subcategory_id": "al_c15_s4", "name": "سجل أنشطة قيمية", "order": 2},
    {"id": "al_c15_s4_r003", "subcategory_id": "al_c15_s4", "name": "توثيق برامج أخلاقية", "order": 3},
    {"id": "al_c15_s4_r004", "subcategory_id": "al_c15_s4", "name": "تقرير عن قيم المواطنة", "order": 4},
    {"id": "al_c15_s4_r005", "subcategory_id": "al_c15_s4", "name": "سجل تحسين السلوك", "order": 5},
    {"id": "al_c15_s4_r006", "subcategory_id": "al_c15_s4", "name": "تقرير فاعلية التعزيز", "order": 6},
    {"id": "al_c15_s4_r007", "subcategory_id": "al_c15_s4", "name": "توثيق تطبيق القيم", "order": 7},
    {"id": "al_c15_s4_r008", "subcategory_id": "al_c15_s4", "name": "تقرير قياس الالتزام", "order": 8},
    {"id": "al_c15_s4_r009", "subcategory_id": "al_c15_s4", "name": "سبل تطوير التعزيز", "order": 9},
    {"id": "al_c15_s4_r010", "subcategory_id": "al_c15_s4", "name": "تقرير ختامي للقيم", "order": 10},

    # ========== al_c15_s5 ==========
    {"id": "al_c15_s5_r001", "subcategory_id": "al_c15_s5", "name": "تقرير تطوير مهارات الطلاب", "order": 1},
    {"id": "al_c15_s5_r002", "subcategory_id": "al_c15_s5", "name": "سجل مهارات مكتسبة", "order": 2},
    {"id": "al_c15_s5_r003", "subcategory_id": "al_c15_s5", "name": "توثيق ورش تدريبية", "order": 3},
    {"id": "al_c15_s5_r004", "subcategory_id": "al_c15_s5", "name": "تقرير عن مهارات القيادة", "order": 4},
    {"id": "al_c15_s5_r005", "subcategory_id": "al_c15_s5", "name": "سجل تحسين المهارات", "order": 5},
    {"id": "al_c15_s5_r006", "subcategory_id": "al_c15_s5", "name": "تقرير فاعلية التطوير", "order": 6},
    {"id": "al_c15_s5_r007", "subcategory_id": "al_c15_s5", "name": "توثيق إتقان المهارات", "order": 7},
    {"id": "al_c15_s5_r008", "subcategory_id": "al_c15_s5", "name": "تقرير قياس الكفاءة", "order": 8},
    {"id": "al_c15_s5_r009", "subcategory_id": "al_c15_s5", "name": "سبل تطوير المهارات", "order": 9},
    {"id": "al_c15_s5_r010", "subcategory_id": "al_c15_s5", "name": "تقرير ختامي للمهارات", "order": 10},

    # ========== al_c15_s6 ==========
    {"id": "al_c15_s6_r001", "subcategory_id": "al_c15_s6", "name": "تقرير إثراء هوايات الطلاب", "order": 1},
    {"id": "al_c15_s6_r002", "subcategory_id": "al_c15_s6", "name": "سجل نوادي الهوايات", "order": 2},
    {"id": "al_c15_s6_r003", "subcategory_id": "al_c15_s6", "name": "توثيق أنشطة هوايات", "order": 3},
    {"id": "al_c15_s6_r004", "subcategory_id": "al_c15_s6", "name": "تقرير عن معارض الهوايات", "order": 4},
    {"id": "al_c15_s6_r005", "subcategory_id": "al_c15_s6", "name": "سجل تطوير الهوايات", "order": 5},
    {"id": "al_c15_s6_r006", "subcategory_id": "al_c15_s6", "name": "تقرير فاعلية الإثراء", "order": 6},
    {"id": "al_c15_s6_r007", "subcategory_id": "al_c15_s6", "name": "توثيق إبداعات الطلاب", "order": 7},
    {"id": "al_c15_s6_r008", "subcategory_id": "al_c15_s6", "name": "تقرير قياس الرضا", "order": 8},
    {"id": "al_c15_s6_r009", "subcategory_id": "al_c15_s6", "name": "سبل تطوير الإثراء", "order": 9},
    {"id": "al_c15_s6_r010", "subcategory_id": "al_c15_s6", "name": "تقرير ختامي للهوايات", "order": 10},
]

# قالب إنشاء التقرير
ACTIVITY_LEADER_PROMPT_TEMPLATE = """أنت رائد نشاط طلابي مسؤول عن تخطيط وتنفيذ البرامج والفعاليات الطلابية وفق معايير النشاط المعتمدة.

المطلوب:
- عرض المعيار.
- عرض التصنيف الفرعي.
- كتابة تقرير مهني يوضح كيفية تنفيذ الأنشطة المرتبطة بهذا التصنيف.

التقرير المطلوب: "{report_name}"
وهو يندرج تحت التصنيف الفرعي: "{subcategory_name}"
ضمن المعيار التربوي: "{criterion_name}"

ضوابط الكتابة:
- لغة تربوية رسمية.
- إبراز التخطيط المسبق للبرامج وبنائها على احتياج المدرسة.
- توضيح آلية التنفيذ وتنظيم الفعاليات.
- بيان دور الأنشطة في تنمية مهارات الطلبة وقيمهم.
- الإشارة إلى قياس الأثر وتحليل نتائج المشاركة.
- إبراز الشراكات المجتمعية والمشاركات الخارجية إن وجدت.
- توضيح دور التحفيز واكتشاف المواهب.
- صياغة واقعية تطبيقية من 5–7 أسطر.

دورك كرائد النشاط

1. تنمية مهارات الطلاب القيادية والاجتماعية من خلال برامج نشاط هادفة تعزز الانتماء المدرسي وتدعم التكامل بين التعلم الصفي واللاصفّي.

2. صممت برنامجًا نشاطيًا يعزز روح الفريق والمسؤولية لدى الطلاب ويربط مهاراتهم العملية بالقيم التربوية الداعمة للتعلم.

3. شكلت فرق عمل طلابية، وحددت أدوارًا واضحة، ونظمت أنشطة تطبيقية داخل مرافق المدرسة، وتابعت الأداء لضمان تحقيق الأهداف التربوية.

4. استخدمت التعلم بالمشروعات، والعمل التعاوني، والتكليفات العملية، والتحفيز المعنوي لتعزيز مشاركة الطلاب الفاعلة.

5. أظهر الطلاب تفاعلًا مرتفعًا وتحسنًا في مهارات التواصل وتحمل المسؤولية، وانعكس ذلك إيجابًا على سلوكهم داخل الصف.

6. الحاجة إلى تنويع مجالات الأنشطة لتناسب ميول جميع الطلاب، وتطوير أدوات تقويم أثر النشاط على التحصيل والسلوك.

7. أوصي ببناء خطة نشاط سنوية متدرجة، وتعزيز تكامل الأنشطة مع أهداف المدرسة، وتوسيع الشراكات لدعم استدامة البرامج الطلابية.

**الحقول المطلوبة:**
1. الهدف التربوي
2. نبذة مختصرة
3. إجراءات التنفيذ
4. الاستراتيجيات المستخدمة
5. نقاط القوة
6. نقاط التحسين
7. التوصيات

يرجى تقديم الإجابة باللغة العربية الفصحى، وتنظيمها بحيث يكون كل حقل في سطر منفصل يبدأ برقمه فقط دون ذكر العنوان."""