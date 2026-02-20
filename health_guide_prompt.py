# health_guide_prompt_updated.py
# -*- coding: utf-8 -*-

# قائمة المعايير مع نسبها المئوية (weights)
HG_CRITERIA = [
    {"id": "hg_c1", "name": "أداء الواجبات الوظيفية", "weight": 10, "order": 1},
    {"id": "hg_c2", "name": "التفاعل مع المجتمع المهني", "weight": 10, "order": 2},
    {"id": "hg_c3", "name": "التفاعل مع أولياء الأمور", "weight": 10, "order": 3},
    {"id": "hg_c4", "name": "التنويع في استراتيجيات التدريس", "weight": 5, "order": 4},
    {"id": "hg_c5", "name": "تحسين نتائج المتعلمين", "weight": 5, "order": 5},
    {"id": "hg_c6", "name": "إعداد وتنفيذ خطة التعلم", "weight": 5, "order": 6},
    {"id": "hg_c7", "name": "توظيف تقنيات ووسائل التعلم المناسبة", "weight": 5, "order": 7},
    {"id": "hg_c8", "name": "تهيئة بيئة تعليمية", "weight": 5, "order": 8},
    {"id": "hg_c9", "name": "تحليل نتائج المتعلمين وتشخيص مستوياتهم", "weight": 5, "order": 9},
    {"id": "hg_c10", "name": "تنوع أساليب التقويم", "weight": 5, "order": 10},
    {"id": "hg_c11", "name": "تنفيذ الخطة المشتركة للبرامج الصحية المدرسية", "weight": 15, "order": 11},
    {"id": "hg_c12", "name": "حصر الحالات الصحية للمتعلمين", "weight": 5, "order": 12},
    {"id": "hg_c13", "name": "تهيئة البيئة الصحية المدرسية", "weight": 10, "order": 13}
]

# التصنيفات الفرعية (مشتقة من البيانات أعلاه)
HG_SUBCATEGORIES = [
    # hg_c1 (أداء الواجبات الوظيفية)
    {"id": "hg_c1_s1", "criterion_id": "hg_c1", "name": "تطبيق الأنظمة وقواعد السلوك الوظيفية وأخلاقيات بيئة التعلم", "order": 1},
    {"id": "hg_c1_s2", "criterion_id": "hg_c1", "name": "حماية البيانات والمعلومات المتعلقة بالعمل من الوصول غير المصرح به", "order": 2},
    {"id": "hg_c1_s3", "criterion_id": "hg_c1", "name": "التعاون مع المؤسسات الحكومية في المبادرات الوطنية", "order": 3},
    {"id": "hg_c1_s4", "criterion_id": "hg_c1", "name": "تنظيم أنشطة توعوية حول أهمية الانتماء الوطني", "order": 4},
    {"id": "hg_c1_s5", "criterion_id": "hg_c1", "name": "تنظيم أنشطة توعوية حول أهمية الانتماء", "order": 5},
    {"id": "hg_c1_s6", "criterion_id": "hg_c1", "name": "الامتثال للقوانين واللوائح وسياسات وإجراءات العمل", "order": 6},
    # hg_c2 (التفاعل مع المجتمع المهني)
    {"id": "hg_c2_s1", "criterion_id": "hg_c2", "name": "حضور المؤتمرات والندوات التعليمية", "order": 1},
    {"id": "hg_c2_s2", "criterion_id": "hg_c2", "name": "المشاركة في ورش العمل التدريبية لتحسين المهارات التعليمية", "order": 2},
    {"id": "hg_c2_s3", "criterion_id": "hg_c2", "name": "الالتحاق ببرامج تدريبية لتعلم أساليب تدريس حديثة", "order": 3},
    {"id": "hg_c2_s4", "criterion_id": "hg_c2", "name": "الحصول على شهادات مهنية معتمدة في مجال التعليم", "order": 4},
    {"id": "hg_c2_s5", "criterion_id": "hg_c2", "name": "إطلاق مبادرات تعليمية لتحسين جودة التعليم", "order": 5},
    {"id": "hg_c2_s6", "criterion_id": "hg_c2", "name": "تقديم استشارات تربوية للمعلمين الجدد", "order": 6},
    {"id": "hg_c2_s7", "criterion_id": "hg_c2", "name": "تبادل الخبرات مع المعلمين في نفس التخصص أو تخصصات أخرى", "order": 7},
    {"id": "hg_c2_s8", "criterion_id": "hg_c2", "name": "التفكير الذاتي لتحسين الممارسات وبناء بيئة تعليمية تعزز التعلم المستمر", "order": 8},
    # hg_c3 (التفاعل مع أولياء الأمور)
    {"id": "hg_c3_s1", "criterion_id": "hg_c3", "name": "تنظيم اجتماعات دورية مع أولياء الأمور لمناقشة تقدم الطلاب", "order": 1},
    {"id": "hg_c3_s2", "criterion_id": "hg_c3", "name": "إرسال تقارير منتظمة عن أداء الطلاب أكاديمياً وسلوكياً", "order": 2},
    {"id": "hg_c3_s3", "criterion_id": "hg_c3", "name": "استخدام وسائل التواصل الحديثة لإبقاء أولياء الأمور على اطلاع", "order": 3},
    {"id": "hg_c3_s4", "criterion_id": "hg_c3", "name": "الاستجابة والاستماع لملاحظات ومخاوف أولياء الأمور ومعالجتها", "order": 4},
    {"id": "hg_c3_s5", "criterion_id": "hg_c3", "name": "تشجيع أولياء الأمور على المشاركة في العملية التعليمية", "order": 5},
    # hg_c4 (التنويع في استراتيجيات التدريس)
    {"id": "hg_c4_s1", "criterion_id": "hg_c4", "name": "استخدام التعلم النشط مثل المناقشات الجماعية والعروض التقديمية", "order": 1},
    {"id": "hg_c4_s2", "criterion_id": "hg_c4", "name": "تطبيق التعلم القائم على المشاريع لتعزيز الإبداع وحل المشكلات", "order": 2},
    {"id": "hg_c4_s3", "criterion_id": "hg_c4", "name": "استخدام الوسائل البصرية والسمعية مثل الفيديوهات والصور", "order": 3},
    {"id": "hg_c4_s4", "criterion_id": "hg_c4", "name": "تخصيص أنشطة تعليمية تناسب أنماط التعلم المختلفة", "order": 4},
    # hg_c5 (تحسين نتائج المتعلمين)
    {"id": "hg_c5_s1", "criterion_id": "hg_c5", "name": "تحديد أهداف ومعايير واضحة للمتعلمين", "order": 1},
    {"id": "hg_c5_s2", "criterion_id": "hg_c5", "name": "تقديم إفادة سريعة ومحددة فور ملاحظة الأداء", "order": 2},
    {"id": "hg_c5_s3", "criterion_id": "hg_c5", "name": "تكييف الإفادة وفق الاحتياجات الفردية", "order": 3},
    {"id": "hg_c5_s4", "criterion_id": "hg_c5", "name": "تعزيز الثقة وتشجيع التطور من خلال ملاحظات إيجابية", "order": 4},
    {"id": "hg_c5_s5", "criterion_id": "hg_c5", "name": "استخدام التكنولوجيا لتقديم الإفادة بطرق مبتكرة", "order": 5},
    # hg_c6 (إعداد وتنفيذ خطة التعلم)
    {"id": "hg_c6_s1", "criterion_id": "hg_c6", "name": "وضع أهداف تعليمية واضحة وقابلة للقياس", "order": 1},
    {"id": "hg_c6_s2", "criterion_id": "hg_c6", "name": "تصميم خطة دراسية تتوافق مع المنهج واحتياجات الطلاب", "order": 2},
    {"id": "hg_c6_s3", "criterion_id": "hg_c6", "name": "مراجعة الخطط بشكل دوري وتعديلها بناءً على نتائج الطلاب", "order": 3},
    {"id": "hg_c6_s4", "criterion_id": "hg_c6", "name": "مشاركة الخطط مع الزملاء للحصول على ملاحظات وتحسينها", "order": 4},
    {"id": "hg_c6_s5", "criterion_id": "hg_c6", "name": "تفهم الخصائص النفسية للمرحلة العمرية التي يتم تدريسها", "order": 5},
    # hg_c7 (توظيف تقنيات ووسائل التعلم المناسبة)
    {"id": "hg_c7_s1", "criterion_id": "hg_c7", "name": "استخدام السبورات الذكية والأجهزة اللوحية في التدريس", "order": 1},
    {"id": "hg_c7_s2", "criterion_id": "hg_c7", "name": "تطبيق برامج التعلم الإلكتروني مثل منصات التعليم عن بعد", "order": 2},
    {"id": "hg_c7_s3", "criterion_id": "hg_c7", "name": "تشجيع الطلاب على استخدام التطبيقات التعليمية لتعزيز التعلم الذاتي", "order": 3},
    {"id": "hg_c7_s4", "criterion_id": "hg_c7", "name": "تنظيم ورش عمل حول استخدام التكنولوجيا في التعليم", "order": 4},
    # hg_c8 (تهيئة بيئة تعليمية)
    {"id": "hg_c8_s1", "criterion_id": "hg_c8", "name": "تزيين الفصل بوسائل تعليمية جذابة", "order": 1},
    {"id": "hg_c8_s2", "criterion_id": "hg_c8", "name": "تنظيم الفصل بشكل يسهل الحركة والتفاعل", "order": 2},
    {"id": "hg_c8_s3", "criterion_id": "hg_c8", "name": "توفير الأدوات والموارد التعليمية اللازمة", "order": 3},
    {"id": "hg_c8_s4", "criterion_id": "hg_c8", "name": "توفير بيئة تعليمية آمنة وخالية من الأخطار وتحقق الأمان النفسي", "order": 4},
    {"id": "hg_c8_s5", "criterion_id": "hg_c8", "name": "تمكين المتعلمين من التعبير عن أنفسهم ومشاركة أفكارهم", "order": 5},
    {"id": "hg_c8_s6", "criterion_id": "hg_c8", "name": "إثارة دافعية المتعلمين من خلال التنوع في أساليب التعلم", "order": 6},
    # hg_c9 (تحليل نتائج المتعلمين وتشخيص مستوياتهم)
    {"id": "hg_c9_s1", "criterion_id": "hg_c9", "name": "استخدام اختبارات تقييمية دورية لقياس تقدم الطلاب", "order": 1},
    {"id": "hg_c9_s2", "criterion_id": "hg_c9", "name": "تحليل النتائج لتحديد نقاط القوة والضعف وإشراك المتعلمين", "order": 2},
    {"id": "hg_c9_s3", "criterion_id": "hg_c9", "name": "توفير تغذية راجعة فردية للطلاب", "order": 3},
    {"id": "hg_c9_s4", "criterion_id": "hg_c9", "name": "تطبيق خطط علاجية للطلاب الذين يحتاجون إلى دعم", "order": 4},
    {"id": "hg_c9_s5", "criterion_id": "hg_c9", "name": "قياس التطبيق العملي للمعرفة عبر مواقف ومشاريع حقيقية", "order": 5},
    # hg_c10 (تنوع أساليب التقويم)
    {"id": "hg_c10_s1", "criterion_id": "hg_c10", "name": "استخدام الاختبارات الكتابية والشفوية", "order": 1},
    {"id": "hg_c10_s2", "criterion_id": "hg_c10", "name": "تطبيق التقييم العملي من خلال المشاريع والعروض", "order": 2},
    {"id": "hg_c10_s3", "criterion_id": "hg_c10", "name": "استخدام التقييم التكويني لتتبع تقدم الطلاب", "order": 3},
    {"id": "hg_c10_s4", "criterion_id": "hg_c10", "name": "استخدام التقويم القبلي لتشخيص المهارات الأساسية", "order": 4},
    {"id": "hg_c10_s5", "criterion_id": "hg_c10", "name": "تطبيق التقويم الختامي لقياس مدى تحقيق الأهداف", "order": 5},
    # hg_c11 (تنفيذ الخطة المشتركة للبرامج الصحية المدرسية)
    {"id": "hg_c11_s1", "criterion_id": "hg_c11", "name": "تنفيذ الخطة المشتركة للبرامج الصحية المدرسية", "order": 1},
    # hg_c12 (حصر الحالات الصحية للمتعلمين)
    {"id": "hg_c12_s1", "criterion_id": "hg_c12", "name": "حصر الحالات الصحية للمتعلمين", "order": 1},
    # hg_c13 (تهيئة البيئة الصحية المدرسية)
    {"id": "hg_c13_s1", "criterion_id": "hg_c13", "name": "تهيئة البيئة الصحية المدرسية", "order": 1}
]

# قائمة التقارير الموسعة (10 تقارير لكل تصنيف فرعي)
HG_REPORTS = [
    # hg_c1_s1 (تطبيق الأنظمة وقواعد السلوك الوظيفية)
    {"id": "hg_c1_s1_r01", "subcategory_id": "hg_c1_s1", "name": "تقرير عن تطبيق لائحة السلوك الوظيفي في المدرسة", "order": 1},
    {"id": "hg_c1_s1_r02", "subcategory_id": "hg_c1_s1", "name": "سجل متابعة التزام المعلمين بقواعد السلوك", "order": 2},
    {"id": "hg_c1_s1_r03", "subcategory_id": "hg_c1_s1", "name": "خطة تعزيز أخلاقيات بيئة التعلم", "order": 3},
    {"id": "hg_c1_s1_r04", "subcategory_id": "hg_c1_s1", "name": "إحصائية المخالفات السلوكية والإجراءات التصحيحية", "order": 4},
    {"id": "hg_c1_s1_r05", "subcategory_id": "hg_c1_s1", "name": "تقييم ورش العمل حول الأنظمة الوظيفية", "order": 5},
    {"id": "hg_c1_s1_r06", "subcategory_id": "hg_c1_s1", "name": "توعية الموظفين بأخلاقيات المهنة", "order": 6},
    {"id": "hg_c1_s1_r07", "subcategory_id": "hg_c1_s1", "name": "تنسيق مع إدارة الموارد البشرية لتحديث الأدلة", "order": 7},
    {"id": "hg_c1_s1_r08", "subcategory_id": "hg_c1_s1", "name": "تحسين آليات الإبلاغ عن المخالفات", "order": 8},
    {"id": "hg_c1_s1_r09", "subcategory_id": "hg_c1_s1", "name": "متابعة تنفيذ برامج النزاهة الوظيفية", "order": 9},
    {"id": "hg_c1_s1_r10", "subcategory_id": "hg_c1_s1", "name": "إنجازات تعزيز السلوك الوظيفي خلال العام", "order": 10},

    # hg_c1_s2 (حماية البيانات)
    {"id": "hg_c1_s2_r01", "subcategory_id": "hg_c1_s2", "name": "تقرير عن تطبيق سياسة حماية البيانات الشخصية", "order": 1},
    {"id": "hg_c1_s2_r02", "subcategory_id": "hg_c1_s2", "name": "سجل صلاحيات الوصول لنظام المعلومات", "order": 2},
    {"id": "hg_c1_s2_r03", "subcategory_id": "hg_c1_s2", "name": "خطة التدريب على أمن المعلومات", "order": 3},
    {"id": "hg_c1_s2_r04", "subcategory_id": "hg_c1_s2", "name": "إحصائية محاولات الاختراق والإجراءات", "order": 4},
    {"id": "hg_c1_s2_r05", "subcategory_id": "hg_c1_s2", "name": "تقييم فعالية أنظمة الحماية", "order": 5},
    {"id": "hg_c1_s2_r06", "subcategory_id": "hg_c1_s2", "name": "توعية الموظفين بأمن المعلومات", "order": 6},
    {"id": "hg_c1_s2_r07", "subcategory_id": "hg_c1_s2", "name": "تنسيق مع وحدة التحول الرقمي", "order": 7},
    {"id": "hg_c1_s2_r08", "subcategory_id": "hg_c1_s2", "name": "تحسين كلمات المرور وتحديثها", "order": 8},
    {"id": "hg_c1_s2_r09", "subcategory_id": "hg_c1_s2", "name": "متابعة التزام الجهات الخارجية بالسرية", "order": 9},
    {"id": "hg_c1_s2_r10", "subcategory_id": "hg_c1_s2", "name": "إنجازات برنامج حماية البيانات", "order": 10},

    # hg_c1_s3 (التعاون مع المؤسسات الحكومية)
    {"id": "hg_c1_s3_r01", "subcategory_id": "hg_c1_s3", "name": "تقرير عن المشاركة في المبادرات الوطنية", "order": 1},
    {"id": "hg_c1_s3_r02", "subcategory_id": "hg_c1_s3", "name": "سجل الشراكات مع الجهات الحكومية", "order": 2},
    {"id": "hg_c1_s3_r03", "subcategory_id": "hg_c1_s3", "name": "خطة التعاون مع المؤسسات في الفعاليات", "order": 3},
    {"id": "hg_c1_s3_r04", "subcategory_id": "hg_c1_s3", "name": "إحصائية عدد المبادرات المشتركة", "order": 4},
    {"id": "hg_c1_s3_r05", "subcategory_id": "hg_c1_s3", "name": "تقييم أثر التعاون على المجتمع المدرسي", "order": 5},
    {"id": "hg_c1_s3_r06", "subcategory_id": "hg_c1_s3", "name": "توعية الطلاب بالمبادرات الحكومية", "order": 6},
    {"id": "hg_c1_s3_r07", "subcategory_id": "hg_c1_s3", "name": "تنسيق مع وزارة التعليم في البرامج", "order": 7},
    {"id": "hg_c1_s3_r08", "subcategory_id": "hg_c1_s3", "name": "تحسين آليات المشاركة المجتمعية", "order": 8},
    {"id": "hg_c1_s3_r09", "subcategory_id": "hg_c1_s3", "name": "متابعة تنفيذ الاتفاقيات", "order": 9},
    {"id": "hg_c1_s3_r10", "subcategory_id": "hg_c1_s3", "name": "إنجازات التعاون الحكومي", "order": 10},

    # hg_c1_s4 (تنظيم أنشطة توعوية حول الانتماء الوطني)
    {"id": "hg_c1_s4_r01", "subcategory_id": "hg_c1_s4", "name": "تقرير عن أنشطة اليوم الوطني", "order": 1},
    {"id": "hg_c1_s4_r02", "subcategory_id": "hg_c1_s4", "name": "سجل الفعاليات الوطنية المنفذة", "order": 2},
    {"id": "hg_c1_s4_r03", "subcategory_id": "hg_c1_s4", "name": "خطة تعزيز قيم المواطنة", "order": 3},
    {"id": "hg_c1_s4_r04", "subcategory_id": "hg_c1_s4", "name": "إحصائية مشاركة الطلاب في الأنشطة", "order": 4},
    {"id": "hg_c1_s4_r05", "subcategory_id": "hg_c1_s4", "name": "تقييم أثر الأنشطة على الوعي الوطني", "order": 5},
    {"id": "hg_c1_s4_r06", "subcategory_id": "hg_c1_s4", "name": "توعية الطلاب برموز الوطن", "order": 6},
    {"id": "hg_c1_s4_r07", "subcategory_id": "hg_c1_s4", "name": "تنسيق مع الجهات المعنية بالمناسبات", "order": 7},
    {"id": "hg_c1_s4_r08", "subcategory_id": "hg_c1_s4", "name": "تحسين محتوى الأنشطة الوطنية", "order": 8},
    {"id": "hg_c1_s4_r09", "subcategory_id": "hg_c1_s4", "name": "متابعة تنفيذ برامج الانتماء", "order": 9},
    {"id": "hg_c1_s4_r10", "subcategory_id": "hg_c1_s4", "name": "إنجازات الأنشطة الوطنية", "order": 10},

    # hg_c1_s5 (تنظيم أنشطة توعوية حول أهمية الانتماء)
    {"id": "hg_c1_s5_r01", "subcategory_id": "hg_c1_s5", "name": "تقرير عن أنشطة تعزيز الانتماء المدرسي", "order": 1},
    {"id": "hg_c1_s5_r02", "subcategory_id": "hg_c1_s5", "name": "سجل فعاليات روح الفريق", "order": 2},
    {"id": "hg_c1_s5_r03", "subcategory_id": "hg_c1_s5", "name": "خطة تنمية الانتماء للمدرسة", "order": 3},
    {"id": "hg_c1_s5_r04", "subcategory_id": "hg_c1_s5", "name": "إحصائية مشاركة الطلاب في الأنشطة", "order": 4},
    {"id": "hg_c1_s5_r05", "subcategory_id": "hg_c1_s5", "name": "تقييم أثر الأنشطة على الانتماء", "order": 5},
    {"id": "hg_c1_s5_r06", "subcategory_id": "hg_c1_s5", "name": "توعية الطلاب بقيمة الانتماء", "order": 6},
    {"id": "hg_c1_s5_r07", "subcategory_id": "hg_c1_s5", "name": "تنسيق مع رائد النشاط", "order": 7},
    {"id": "hg_c1_s5_r08", "subcategory_id": "hg_c1_s5", "name": "تحسين برامج الاحتفاء بالطلاب", "order": 8},
    {"id": "hg_c1_s5_r09", "subcategory_id": "hg_c1_s5", "name": "متابعة استدامة الأنشطة", "order": 9},
    {"id": "hg_c1_s5_r10", "subcategory_id": "hg_c1_s5", "name": "إنجازات تعزيز الانتماء", "order": 10},

    # hg_c1_s6 (الامتثال للقوانين واللوائح)
    {"id": "hg_c1_s6_r01", "subcategory_id": "hg_c1_s6", "name": "تقرير عن مدى الامتثال للوائح وزارة التعليم", "order": 1},
    {"id": "hg_c1_s6_r02", "subcategory_id": "hg_c1_s6", "name": "سجل تحديث الإجراءات وفق الأنظمة", "order": 2},
    {"id": "hg_c1_s6_r03", "subcategory_id": "hg_c1_s6", "name": "خطة نشر الوعي القانوني", "order": 3},
    {"id": "hg_c1_s6_r04", "subcategory_id": "hg_c1_s6", "name": "إحصائية عدد التعاميم المنفذة", "order": 4},
    {"id": "hg_c1_s6_r05", "subcategory_id": "hg_c1_s6", "name": "تقييم تطبيق سياسات العمل", "order": 5},
    {"id": "hg_c1_s6_r06", "subcategory_id": "hg_c1_s6", "name": "توعية الموظفين باللوائح", "order": 6},
    {"id": "hg_c1_s6_r07", "subcategory_id": "hg_c1_s6", "name": "تنسيق مع المستشار القانوني", "order": 7},
    {"id": "hg_c1_s6_r08", "subcategory_id": "hg_c1_s6", "name": "تحسين دليل الإجراءات", "order": 8},
    {"id": "hg_c1_s6_r09", "subcategory_id": "hg_c1_s6", "name": "متابعة التحديثات النظامية", "order": 9},
    {"id": "hg_c1_s6_r10", "subcategory_id": "hg_c1_s6", "name": "إنجازات الامتثال للوائح", "order": 10},

    # hg_c2_s1 (حضور المؤتمرات والندوات)
    {"id": "hg_c2_s1_r01", "subcategory_id": "hg_c2_s1", "name": "تقرير عن حضور المؤتمر التربوي السنوي", "order": 1},
    {"id": "hg_c2_s1_r02", "subcategory_id": "hg_c2_s1", "name": "سجل المشاركات في الندوات التعليمية", "order": 2},
    {"id": "hg_c2_s1_r03", "subcategory_id": "hg_c2_s1", "name": "خطة الاستفادة من المؤتمرات في التطوير", "order": 3},
    {"id": "hg_c2_s1_r04", "subcategory_id": "hg_c2_s1", "name": "إحصائية عدد المؤتمرات المحلية", "order": 4},
    {"id": "hg_c2_s1_r05", "subcategory_id": "hg_c2_s1", "name": "تقييم أثر المؤتمرات على الأداء", "order": 5},
    {"id": "hg_c2_s1_r06", "subcategory_id": "hg_c2_s1", "name": "توعية الزملاء بأهمية المؤتمرات", "order": 6},
    {"id": "hg_c2_s1_r07", "subcategory_id": "hg_c2_s1", "name": "تنسيق مع جهات تنظيم المؤتمرات", "order": 7},
    {"id": "hg_c2_s1_r08", "subcategory_id": "hg_c2_s1", "name": "تحسين المشاركة الفعالة", "order": 8},
    {"id": "hg_c2_s1_r09", "subcategory_id": "hg_c2_s1", "name": "متابعة توصيات المؤتمرات", "order": 9},
    {"id": "hg_c2_s1_r10", "subcategory_id": "hg_c2_s1", "name": "إنجازات المشاركة المهنية", "order": 10},

    # hg_c2_s2 (المشاركة في ورش العمل التدريبية)
    {"id": "hg_c2_s2_r01", "subcategory_id": "hg_c2_s2", "name": "تقرير عن ورشة استراتيجيات التعلم النشط", "order": 1},
    {"id": "hg_c2_s2_r02", "subcategory_id": "hg_c2_s2", "name": "سجل المشاركة في ورش القيادة التربوية", "order": 2},
    {"id": "hg_c2_s2_r03", "subcategory_id": "hg_c2_s2", "name": "خطة تطوير المهارات عبر الورش", "order": 3},
    {"id": "hg_c2_s2_r04", "subcategory_id": "hg_c2_s2", "name": "إحصائية عدد ساعات التدريب", "order": 4},
    {"id": "hg_c2_s2_r05", "subcategory_id": "hg_c2_s2", "name": "تقييم جودة الورش المنفذة", "order": 5},
    {"id": "hg_c2_s2_r06", "subcategory_id": "hg_c2_s2", "name": "توعية المعلمين بأهمية التدريب", "order": 6},
    {"id": "hg_c2_s2_r07", "subcategory_id": "hg_c2_s2", "name": "تنسيق مع مركز التدريب", "order": 7},
    {"id": "hg_c2_s2_r08", "subcategory_id": "hg_c2_s2", "name": "تحسين نقل أثر التدريب", "order": 8},
    {"id": "hg_c2_s2_r09", "subcategory_id": "hg_c2_s2", "name": "متابعة تطبيق المهارات", "order": 9},
    {"id": "hg_c2_s2_r10", "subcategory_id": "hg_c2_s2", "name": "إنجازات برنامج التدريب", "order": 10},

    # hg_c2_s3 (الالتحاق ببرامج تدريبية لأساليب حديثة)
    {"id": "hg_c2_s3_r01", "subcategory_id": "hg_c2_s3", "name": "تقرير عن دورة التعلم المدمج", "order": 1},
    {"id": "hg_c2_s3_r02", "subcategory_id": "hg_c2_s3", "name": "سجل البرامج التدريبية المعتمدة", "order": 2},
    {"id": "hg_c2_s3_r03", "subcategory_id": "hg_c2_s3", "name": "خطة الالتحاق بالبرامج المتخصصة", "order": 3},
    {"id": "hg_c2_s3_r04", "subcategory_id": "hg_c2_s3", "name": "إحصائية عدد الدورات المكتملة", "order": 4},
    {"id": "hg_c2_s3_r05", "subcategory_id": "hg_c2_s3", "name": "تقييم فاعلية البرامج", "order": 5},
    {"id": "hg_c2_s3_r06", "subcategory_id": "hg_c2_s3", "name": "توعية الزملاء بالفرص التدريبية", "order": 6},
    {"id": "hg_c2_s3_r07", "subcategory_id": "hg_c2_s3", "name": "تنسيق مع مقدمي البرامج", "order": 7},
    {"id": "hg_c2_s3_r08", "subcategory_id": "hg_c2_s3", "name": "تحسين توظيف الأساليب الجديدة", "order": 8},
    {"id": "hg_c2_s3_r09", "subcategory_id": "hg_c2_s3", "name": "متابعة مستجدات التدريس", "order": 9},
    {"id": "hg_c2_s3_r10", "subcategory_id": "hg_c2_s3", "name": "إنجازات التطوير المهني", "order": 10},

    # hg_c2_s4 (الحصول على شهادات مهنية)
    {"id": "hg_c2_s4_r01", "subcategory_id": "hg_c2_s4", "name": "تقرير عن الحصول على شهادة معلم خبير", "order": 1},
    {"id": "hg_c2_s4_r02", "subcategory_id": "hg_c2_s4", "name": "سجل الشهادات المهنية للمعلمين", "order": 2},
    {"id": "hg_c2_s4_r03", "subcategory_id": "hg_c2_s4", "name": "خطة تحفيز للحصول على شهادات", "order": 3},
    {"id": "hg_c2_s4_r04", "subcategory_id": "hg_c2_s4", "name": "إحصائية عدد الشهادات المحصل عليها", "order": 4},
    {"id": "hg_c2_s4_r05", "subcategory_id": "hg_c2_s4", "name": "تقييم أثر الشهادات على الأداء", "order": 5},
    {"id": "hg_c2_s4_r06", "subcategory_id": "hg_c2_s4", "name": "توعية بأهمية الاعتماد المهني", "order": 6},
    {"id": "hg_c2_s4_r07", "subcategory_id": "hg_c2_s4", "name": "تنسيق مع هيئة تقويم التعليم", "order": 7},
    {"id": "hg_c2_s4_r08", "subcategory_id": "hg_c2_s4", "name": "تحسين فرص الترشح", "order": 8},
    {"id": "hg_c2_s4_r09", "subcategory_id": "hg_c2_s4", "name": "متابعة تجديد الشهادات", "order": 9},
    {"id": "hg_c2_s4_r10", "subcategory_id": "hg_c2_s4", "name": "إنجازات الاعتماد المهني", "order": 10},

    # hg_c2_s5 (إطلاق مبادرات تعليمية)
    {"id": "hg_c2_s5_r01", "subcategory_id": "hg_c2_s5", "name": "تقرير عن مبادرة تحسين القراءة", "order": 1},
    {"id": "hg_c2_s5_r02", "subcategory_id": "hg_c2_s5", "name": "سجل المبادرات التعليمية المنفذة", "order": 2},
    {"id": "hg_c2_s5_r03", "subcategory_id": "hg_c2_s5", "name": "خطة إطلاق مبادرة الرياضيات", "order": 3},
    {"id": "hg_c2_s5_r04", "subcategory_id": "hg_c2_s5", "name": "إحصائية عدد المستفيدين من المبادرات", "order": 4},
    {"id": "hg_c2_s5_r05", "subcategory_id": "hg_c2_s5", "name": "تقييم أثر المبادرات على التعلم", "order": 5},
    {"id": "hg_c2_s5_r06", "subcategory_id": "hg_c2_s5", "name": "توعية المجتمع بالمبادرات", "order": 6},
    {"id": "hg_c2_s5_r07", "subcategory_id": "hg_c2_s5", "name": "تنسيق مع مؤسسات داعمة", "order": 7},
    {"id": "hg_c2_s5_r08", "subcategory_id": "hg_c2_s5", "name": "تحسين استدامة المبادرات", "order": 8},
    {"id": "hg_c2_s5_r09", "subcategory_id": "hg_c2_s5", "name": "متابعة تطوير المبادرات", "order": 9},
    {"id": "hg_c2_s5_r10", "subcategory_id": "hg_c2_s5", "name": "إنجازات المبادرات التعليمية", "order": 10},

    # hg_c2_s6 (تقديم استشارات تربوية للمعلمين الجدد)
    {"id": "hg_c2_s6_r01", "subcategory_id": "hg_c2_s6", "name": "تقرير عن برنامج إرشاد المعلمين الجدد", "order": 1},
    {"id": "hg_c2_s6_r02", "subcategory_id": "hg_c2_s6", "name": "سجل جلسات الإرشاد الفردي", "order": 2},
    {"id": "hg_c2_s6_r03", "subcategory_id": "hg_c2_s6", "name": "خطة دعم المعلمين المستجدين", "order": 3},
    {"id": "hg_c2_s6_r04", "subcategory_id": "hg_c2_s6", "name": "إحصائية عدد المستفيدين من الاستشارات", "order": 4},
    {"id": "hg_c2_s6_r05", "subcategory_id": "hg_c2_s6", "name": "تقييم أثر الإرشاد على أدائهم", "order": 5},
    {"id": "hg_c2_s6_r06", "subcategory_id": "hg_c2_s6", "name": "توعية المعلمين الجدد بخدمات الإرشاد", "order": 6},
    {"id": "hg_c2_s6_r07", "subcategory_id": "hg_c2_s6", "name": "تنسيق مع لجنة التدريب", "order": 7},
    {"id": "hg_c2_s6_r08", "subcategory_id": "hg_c2_s6", "name": "تحسين جودة الاستشارات", "order": 8},
    {"id": "hg_c2_s6_r09", "subcategory_id": "hg_c2_s6", "name": "متابعة تطور المعلمين", "order": 9},
    {"id": "hg_c2_s6_r10", "subcategory_id": "hg_c2_s6", "name": "إنجازات برنامج الإرشاد", "order": 10},

    # hg_c2_s7 (تبادل الخبرات مع المعلمين)
    {"id": "hg_c2_s7_r01", "subcategory_id": "hg_c2_s7", "name": "تقرير عن لقاءات تبادل الخبرات", "order": 1},
    {"id": "hg_c2_s7_r02", "subcategory_id": "hg_c2_s7", "name": "سجل الزيارات الصفية المتبادلة", "order": 2},
    {"id": "hg_c2_s7_r03", "subcategory_id": "hg_c2_s7", "name": "خطة مجتمعات التعلم المهنية", "order": 3},
    {"id": "hg_c2_s7_r04", "subcategory_id": "hg_c2_s7", "name": "إحصائية عدد اللقاءات التشاركية", "order": 4},
    {"id": "hg_c2_s7_r05", "subcategory_id": "hg_c2_s7", "name": "تقييم أثر التبادل على الممارسات", "order": 5},
    {"id": "hg_c2_s7_r06", "subcategory_id": "hg_c2_s7", "name": "توعية بأهمية المشاركة", "order": 6},
    {"id": "hg_c2_s7_r07", "subcategory_id": "hg_c2_s7", "name": "تنسيق مع التخصصات الأخرى", "order": 7},
    {"id": "hg_c2_s7_r08", "subcategory_id": "hg_c2_s7", "name": "تحسين منصات التشارك", "order": 8},
    {"id": "hg_c2_s7_r09", "subcategory_id": "hg_c2_s7", "name": "متابعة تطبيق الأفكار المتبادلة", "order": 9},
    {"id": "hg_c2_s7_r10", "subcategory_id": "hg_c2_s7", "name": "إنجازات مجتمعات التعلم", "order": 10},

    # hg_c2_s8 (التفكير الذاتي)
    {"id": "hg_c2_s8_r01", "subcategory_id": "hg_c2_s8", "name": "تقرير عن تطبيق التفكير التأملي", "order": 1},
    {"id": "hg_c2_s8_r02", "subcategory_id": "hg_c2_s8", "name": "سجل ملاحظات التأمل الذاتي", "order": 2},
    {"id": "hg_c2_s8_r03", "subcategory_id": "hg_c2_s8", "name": "خطة تحسين الأداء بناءً على التأمل", "order": 3},
    {"id": "hg_c2_s8_r04", "subcategory_id": "hg_c2_s8", "name": "إحصائية مدى ممارسة التأمل", "order": 4},
    {"id": "hg_c2_s8_r05", "subcategory_id": "hg_c2_s8", "name": "تقييم أثر التأمل على التطور", "order": 5},
    {"id": "hg_c2_s8_r06", "subcategory_id": "hg_c2_s8", "name": "توعية المعلمين بأدوات التأمل", "order": 6},
    {"id": "hg_c2_s8_r07", "subcategory_id": "hg_c2_s8", "name": "تنسيق مع مشرفي التطوير", "order": 7},
    {"id": "hg_c2_s8_r08", "subcategory_id": "hg_c2_s8", "name": "تحسين نماذج التأمل", "order": 8},
    {"id": "hg_c2_s8_r09", "subcategory_id": "hg_c2_s8", "name": "متابعة خطط التطوير الشخصي", "order": 9},
    {"id": "hg_c2_s8_r10", "subcategory_id": "hg_c2_s8", "name": "إنجازات ثقافة التأمل", "order": 10},

    # hg_c3_s1 (تنظيم اجتماعات دورية مع أولياء الأمور)
    {"id": "hg_c3_s1_r01", "subcategory_id": "hg_c3_s1", "name": "تقرير عن اجتماع مجلس أولياء الأمور", "order": 1},
    {"id": "hg_c3_s1_r02", "subcategory_id": "hg_c3_s1", "name": "سجل محاضر اجتماعات الفصل", "order": 2},
    {"id": "hg_c3_s1_r03", "subcategory_id": "hg_c3_s1", "name": "خطة اللقاءات الدورية مع أولياء الأمور", "order": 3},
    {"id": "hg_c3_s1_r04", "subcategory_id": "hg_c3_s1", "name": "إحصائية عدد الحضور في الاجتماعات", "order": 4},
    {"id": "hg_c3_s1_r05", "subcategory_id": "hg_c3_s1", "name": "تقييم فعالية التواصل مع أولياء الأمور", "order": 5},
    {"id": "hg_c3_s1_r06", "subcategory_id": "hg_c3_s1", "name": "توعية أولياء الأمور بأهمية الحضور", "order": 6},
    {"id": "hg_c3_s1_r07", "subcategory_id": "hg_c3_s1", "name": "تنسيق مع إدارة المدرسة لجدولة الاجتماعات", "order": 7},
    {"id": "hg_c3_s1_r08", "subcategory_id": "hg_c3_s1", "name": "تحسين جودة الاجتماعات", "order": 8},
    {"id": "hg_c3_s1_r09", "subcategory_id": "hg_c3_s1", "name": "متابعة تنفيذ التوصيات", "order": 9},
    {"id": "hg_c3_s1_r10", "subcategory_id": "hg_c3_s1", "name": "إنجازات التواصل الأسري", "order": 10},

    # hg_c3_s2 (إرسال تقارير منتظمة عن أداء الطلاب)
    {"id": "hg_c3_s2_r01", "subcategory_id": "hg_c3_s2", "name": "تقرير عن تقارير نهاية الفصل الدراسي", "order": 1},
    {"id": "hg_c3_s2_r02", "subcategory_id": "hg_c3_s2", "name": "سجل إرسال تقارير السلوك", "order": 2},
    {"id": "hg_c3_s2_r03", "subcategory_id": "hg_c3_s2", "name": "خطة تحسين جودة التقارير", "order": 3},
    {"id": "hg_c3_s2_r04", "subcategory_id": "hg_c3_s2", "name": "إحصائية مدى رضا أولياء الأمور عن التقارير", "order": 4},
    {"id": "hg_c3_s2_r05", "subcategory_id": "hg_c3_s2", "name": "تقييم وضوح التقارير", "order": 5},
    {"id": "hg_c3_s2_r06", "subcategory_id": "hg_c3_s2", "name": "توعية أولياء الأمور بقراءة التقارير", "order": 6},
    {"id": "hg_c3_s2_r07", "subcategory_id": "hg_c3_s2", "name": "تنسيق مع نظام نور", "order": 7},
    {"id": "hg_c3_s2_r08", "subcategory_id": "hg_c3_s2", "name": "تحسين محتوى التقارير", "order": 8},
    {"id": "hg_c3_s2_r09", "subcategory_id": "hg_c3_s2", "name": "متابعة استلام التقارير", "order": 9},
    {"id": "hg_c3_s2_r10", "subcategory_id": "hg_c3_s2", "name": "إنجازات الشفافية مع الأسر", "order": 10},

    # hg_c3_s3 (استخدام وسائل التواصل الحديثة)
    {"id": "hg_c3_s3_r01", "subcategory_id": "hg_c3_s3", "name": "تقرير عن تفعيل تطبيق المدرسة", "order": 1},
    {"id": "hg_c3_s3_r02", "subcategory_id": "hg_c3_s3", "name": "سجل الرسائل الجماعية عبر الواتساب", "order": 2},
    {"id": "hg_c3_s3_r03", "subcategory_id": "hg_c3_s3", "name": "خطة استخدام البريد الإلكتروني", "order": 3},
    {"id": "hg_c3_s3_r04", "subcategory_id": "hg_c3_s3", "name": "إحصائية عدد المتابعين للمنصات", "order": 4},
    {"id": "hg_c3_s3_r05", "subcategory_id": "hg_c3_s3", "name": "تقييم فعالية وسائل التواصل", "order": 5},
    {"id": "hg_c3_s3_r06", "subcategory_id": "hg_c3_s3", "name": "توعية أولياء الأمور بالتطبيقات", "order": 6},
    {"id": "hg_c3_s3_r07", "subcategory_id": "hg_c3_s3", "name": "تنسيق مع تقنية المعلومات", "order": 7},
    {"id": "hg_c3_s3_r08", "subcategory_id": "hg_c3_s3", "name": "تحسين سرعة الاستجابة", "order": 8},
    {"id": "hg_c3_s3_r09", "subcategory_id": "hg_c3_s3", "name": "متابعة تحديث البيانات", "order": 9},
    {"id": "hg_c3_s3_r10", "subcategory_id": "hg_c3_s3", "name": "إنجازات التحول الرقمي في التواصل", "order": 10},

    # hg_c3_s4 (الاستجابة لملاحظات أولياء الأمور)
    {"id": "hg_c3_s4_r01", "subcategory_id": "hg_c3_s4", "name": "تقرير عن آلية استقبال شكاوى أولياء الأمور", "order": 1},
    {"id": "hg_c3_s4_r02", "subcategory_id": "hg_c3_s4", "name": "سجل ملاحظات أولياء الأمور والإجراءات", "order": 2},
    {"id": "hg_c3_s4_r03", "subcategory_id": "hg_c3_s4", "name": "خطة تحسين الاستجابة", "order": 3},
    {"id": "hg_c3_s4_r04", "subcategory_id": "hg_c3_s4", "name": "إحصائية أنواع الملاحظات", "order": 4},
    {"id": "hg_c3_s4_r05", "subcategory_id": "hg_c3_s4", "name": "تقييم رضا أولياء الأمور عن المعالجة", "order": 5},
    {"id": "hg_c3_s4_r06", "subcategory_id": "hg_c3_s4", "name": "توعية أولياء الأمور بقنوات التواصل", "order": 6},
    {"id": "hg_c3_s4_r07", "subcategory_id": "hg_c3_s4", "name": "تنسيق مع لجنة التوجيه", "order": 7},
    {"id": "hg_c3_s4_r08", "subcategory_id": "hg_c3_s4", "name": "تحسين زمن الاستجابة", "order": 8},
    {"id": "hg_c3_s4_r09", "subcategory_id": "hg_c3_s4", "name": "متابعة حل المشكلات", "order": 9},
    {"id": "hg_c3_s4_r10", "subcategory_id": "hg_c3_s4", "name": "إنجازات التواصل الفعال", "order": 10},

    # hg_c3_s5 (تشجيع أولياء الأمور على المشاركة)
    {"id": "hg_c3_s5_r01", "subcategory_id": "hg_c3_s5", "name": "تقرير عن مشاركة أولياء الأمور في الأنشطة", "order": 1},
    {"id": "hg_c3_s5_r02", "subcategory_id": "hg_c3_s5", "name": "سجل التطوع المدرسي للأسر", "order": 2},
    {"id": "hg_c3_s5_r03", "subcategory_id": "hg_c3_s5", "name": "خطة تفعيل دور أولياء الأمور", "order": 3},
    {"id": "hg_c3_s5_r04", "subcategory_id": "hg_c3_s5", "name": "إحصائية عدد المشاركات", "order": 4},
    {"id": "hg_c3_s5_r05", "subcategory_id": "hg_c3_s5", "name": "تقييم أثر المشاركة على الطلاب", "order": 5},
    {"id": "hg_c3_s5_r06", "subcategory_id": "hg_c3_s5", "name": "توعية بأهمية الشراكة", "order": 6},
    {"id": "hg_c3_s5_r07", "subcategory_id": "hg_c3_s5", "name": "تنسيق مع مجلس الآباء", "order": 7},
    {"id": "hg_c3_s5_r08", "subcategory_id": "hg_c3_s5", "name": "تحسين برامج التطوع", "order": 8},
    {"id": "hg_c3_s5_r09", "subcategory_id": "hg_c3_s5", "name": "متابعة استدامة المشاركة", "order": 9},
    {"id": "hg_c3_s5_r10", "subcategory_id": "hg_c3_s5", "name": "إنجازات الشراكة الأسرية", "order": 10},

    # hg_c4_s1 (استخدام التعلم النشط)
    {"id": "hg_c4_s1_r01", "subcategory_id": "hg_c4_s1", "name": "تقرير عن تطبيق المناقشات الجماعية", "order": 1},
    {"id": "hg_c4_s1_r02", "subcategory_id": "hg_c4_s1", "name": "سجل العروض التقديمية للطلاب", "order": 2},
    {"id": "hg_c4_s1_r03", "subcategory_id": "hg_c4_s1", "name": "خطة تنويع استراتيجيات التعلم النشط", "order": 3},
    {"id": "hg_c4_s1_r04", "subcategory_id": "hg_c4_s1", "name": "إحصائية عدد الحصص النشطة", "order": 4},
    {"id": "hg_c4_s1_r05", "subcategory_id": "hg_c4_s1", "name": "تقييم أثر التعلم النشط على التحصيل", "order": 5},
    {"id": "hg_c4_s1_r06", "subcategory_id": "hg_c4_s1", "name": "توعية الطلاب بأهمية المشاركة", "order": 6},
    {"id": "hg_c4_s1_r07", "subcategory_id": "hg_c4_s1", "name": "تنسيق مع مشرفي المواد", "order": 7},
    {"id": "hg_c4_s1_r08", "subcategory_id": "hg_c4_s1", "name": "تحسين إدارة الصف", "order": 8},
    {"id": "hg_c4_s1_r09", "subcategory_id": "hg_c4_s1", "name": "متابعة تنفيذ الأنشطة", "order": 9},
    {"id": "hg_c4_s1_r10", "subcategory_id": "hg_c4_s1", "name": "إنجازات التعلم النشط", "order": 10},

    # hg_c4_s2 (تطبيق التعلم القائم على المشاريع)
    {"id": "hg_c4_s2_r01", "subcategory_id": "hg_c4_s2", "name": "تقرير عن مشروع العلوم التفاعلي", "order": 1},
    {"id": "hg_c4_s2_r02", "subcategory_id": "hg_c4_s2", "name": "سجل المشاريع المنفذة", "order": 2},
    {"id": "hg_c4_s2_r03", "subcategory_id": "hg_c4_s2", "name": "خطة دمج المشاريع في المنهج", "order": 3},
    {"id": "hg_c4_s2_r04", "subcategory_id": "hg_c4_s2", "name": "إحصائية عدد المشاريع", "order": 4},
    {"id": "hg_c4_s2_r05", "subcategory_id": "hg_c4_s2", "name": "تقييم مهارات حل المشكلات", "order": 5},
    {"id": "hg_c4_s2_r06", "subcategory_id": "hg_c4_s2", "name": "توعية الطلاب بفوائد المشاريع", "order": 6},
    {"id": "hg_c4_s2_r07", "subcategory_id": "hg_c4_s2", "name": "تنسيق مع المجتمع المحلي", "order": 7},
    {"id": "hg_c4_s2_r08", "subcategory_id": "hg_c4_s2", "name": "تحسين معايير التقييم", "order": 8},
    {"id": "hg_c4_s2_r09", "subcategory_id": "hg_c4_s2", "name": "متابعة تنفيذ المشاريع", "order": 9},
    {"id": "hg_c4_s2_r10", "subcategory_id": "hg_c4_s2", "name": "إنجازات التعلم القائم على المشاريع", "order": 10},

    # hg_c4_s3 (استخدام الوسائل البصرية والسمعية)
    {"id": "hg_c4_s3_r01", "subcategory_id": "hg_c4_s3", "name": "تقرير عن استخدام الفيديوهات التعليمية", "order": 1},
    {"id": "hg_c4_s3_r02", "subcategory_id": "hg_c4_s3", "name": "سجل الصور والرسوم التوضيحية", "order": 2},
    {"id": "hg_c4_s3_r03", "subcategory_id": "hg_c4_s3", "name": "خطة توظيف الوسائط المتعددة", "order": 3},
    {"id": "hg_c4_s3_r04", "subcategory_id": "hg_c4_s3", "name": "إحصائية عدد الدروس المدعومة", "order": 4},
    {"id": "hg_c4_s3_r05", "subcategory_id": "hg_c4_s3", "name": "تقييم جاذبية الوسائل", "order": 5},
    {"id": "hg_c4_s3_r06", "subcategory_id": "hg_c4_s3", "name": "توعية المعلمين بالمصادر", "order": 6},
    {"id": "hg_c4_s3_r07", "subcategory_id": "hg_c4_s3", "name": "تنسيق مع مركز المصادر", "order": 7},
    {"id": "hg_c4_s3_r08", "subcategory_id": "hg_c4_s3", "name": "تحسين جودة المحتوى", "order": 8},
    {"id": "hg_c4_s3_r09", "subcategory_id": "hg_c4_s3", "name": "متابعة استخدام الطلاب", "order": 9},
    {"id": "hg_c4_s3_r10", "subcategory_id": "hg_c4_s3", "name": "إنجازات التعلم البصري", "order": 10},

    # hg_c4_s4 (تخصيص أنشطة تناسب أنماط التعلم)
    {"id": "hg_c4_s4_r01", "subcategory_id": "hg_c4_s4", "name": "تقرير عن أنشطة للطلاب البصريين", "order": 1},
    {"id": "hg_c4_s4_r02", "subcategory_id": "hg_c4_s4", "name": "سجل أنشطة التعلم الحركي", "order": 2},
    {"id": "hg_c4_s4_r03", "subcategory_id": "hg_c4_s4", "name": "خطة مراعاة الفروق الفردية", "order": 3},
    {"id": "hg_c4_s4_r04", "subcategory_id": "hg_c4_s4", "name": "إحصائية مدى تنوع الأنشطة", "order": 4},
    {"id": "hg_c4_s4_r05", "subcategory_id": "hg_c4_s4", "name": "تقييم استجابة الطلاب", "order": 5},
    {"id": "hg_c4_s4_r06", "subcategory_id": "hg_c4_s4", "name": "توعية المعلمين بأنماط التعلم", "order": 6},
    {"id": "hg_c4_s4_r07", "subcategory_id": "hg_c4_s4", "name": "تنسيق مع وحدة صعوبات التعلم", "order": 7},
    {"id": "hg_c4_s4_r08", "subcategory_id": "hg_c4_s4", "name": "تحسين أدوات تشخيص الأنماط", "order": 8},
    {"id": "hg_c4_s4_r09", "subcategory_id": "hg_c4_s4", "name": "متابعة تنفيذ الأنشطة المخصصة", "order": 9},
    {"id": "hg_c4_s4_r10", "subcategory_id": "hg_c4_s4", "name": "إنجازات التعلم المتنوع", "order": 10},

    # hg_c5_s1 (تحديد أهداف ومعايير واضحة)
    {"id": "hg_c5_s1_r01", "subcategory_id": "hg_c5_s1", "name": "تقرير عن توزيع الأهداف على الدروس", "order": 1},
    {"id": "hg_c5_s1_r02", "subcategory_id": "hg_c5_s1", "name": "سجل معايير النجاح لكل مرحلة", "order": 2},
    {"id": "hg_c5_s1_r03", "subcategory_id": "hg_c5_s1", "name": "خطة مشاركة الطلاب بالأهداف", "order": 3},
    {"id": "hg_c5_s1_r04", "subcategory_id": "hg_c5_s1", "name": "إحصائية وضوح الأهداف للطلاب", "order": 4},
    {"id": "hg_c5_s1_r05", "subcategory_id": "hg_c5_s1", "name": "تقييم مدى تحقيق الأهداف", "order": 5},
    {"id": "hg_c5_s1_r06", "subcategory_id": "hg_c5_s1", "name": "توعية الطلاب بمعايير التقييم", "order": 6},
    {"id": "hg_c5_s1_r07", "subcategory_id": "hg_c5_s1", "name": "تنسيق مع مشرفي المناهج", "order": 7},
    {"id": "hg_c5_s1_r08", "subcategory_id": "hg_c5_s1", "name": "تحسين صياغة الأهداف", "order": 8},
    {"id": "hg_c5_s1_r09", "subcategory_id": "hg_c5_s1", "name": "متابعة مراجعة الأهداف", "order": 9},
    {"id": "hg_c5_s1_r10", "subcategory_id": "hg_c5_s1", "name": "إنجازات وضوح التعلم", "order": 10},

    # hg_c5_s2 (تقديم إفادة سريعة)
    {"id": "hg_c5_s2_r01", "subcategory_id": "hg_c5_s2", "name": "تقرير عن التغذية الراجعة الفورية", "order": 1},
    {"id": "hg_c5_s2_r02", "subcategory_id": "hg_c5_s2", "name": "سجل الملاحظات على أداء الطلاب", "order": 2},
    {"id": "hg_c5_s2_r03", "subcategory_id": "hg_c5_s2", "name": "خطة تحسين جودة الإفادة", "order": 3},
    {"id": "hg_c5_s2_r04", "subcategory_id": "hg_c5_s2", "name": "إحصائية مدى سرعة التصحيح", "order": 4},
    {"id": "hg_c5_s2_r05", "subcategory_id": "hg_c5_s2", "name": "تقييم أثر الإفادة على التحسن", "order": 5},
    {"id": "hg_c5_s2_r06", "subcategory_id": "hg_c5_s2", "name": "توعية المعلمين بأهمية التوقيت", "order": 6},
    {"id": "hg_c5_s2_r07", "subcategory_id": "hg_c5_s2", "name": "تنسيق مع التقويم المستمر", "order": 7},
    {"id": "hg_c5_s2_r08", "subcategory_id": "hg_c5_s2", "name": "تحسين دقة الإفادة", "order": 8},
    {"id": "hg_c5_s2_r09", "subcategory_id": "hg_c5_s2", "name": "متابعة استجابة الطلاب", "order": 9},
    {"id": "hg_c5_s2_r10", "subcategory_id": "hg_c5_s2", "name": "إنجازات التغذية الراجعة", "order": 10},

    # hg_c5_s3 (تكييف الإفادة وفق الاحتياجات)
    {"id": "hg_c5_s3_r01", "subcategory_id": "hg_c5_s3", "name": "تقرير عن تخصيص الإفادة لضعاف التحصيل", "order": 1},
    {"id": "hg_c5_s3_r02", "subcategory_id": "hg_c5_s3", "name": "سجل خطط الدعم الفردية", "order": 2},
    {"id": "hg_c5_s3_r03", "subcategory_id": "hg_c5_s3", "name": "خطة تنويع أساليب الإفادة", "order": 3},
    {"id": "hg_c5_s3_r04", "subcategory_id": "hg_c5_s3", "name": "إحصائية عدد الطلاب المستفيدين", "order": 4},
    {"id": "hg_c5_s3_r05", "subcategory_id": "hg_c5_s3", "name": "تقييم فعالية الإفادة المكيفة", "order": 5},
    {"id": "hg_c5_s3_r06", "subcategory_id": "hg_c5_s3", "name": "توعية المعلمين بالفروق الفردية", "order": 6},
    {"id": "hg_c5_s3_r07", "subcategory_id": "hg_c5_s3", "name": "تنسيق مع التربية الخاصة", "order": 7},
    {"id": "hg_c5_s3_r08", "subcategory_id": "hg_c5_s3", "name": "تحسين أدوات التشخيص", "order": 8},
    {"id": "hg_c5_s3_r09", "subcategory_id": "hg_c5_s3", "name": "متابعة تقدم الحالات", "order": 9},
    {"id": "hg_c5_s3_r10", "subcategory_id": "hg_c5_s3", "name": "إنجازات الدعم الفردي", "order": 10},

    # hg_c5_s4 (تعزيز الثقة وتشجيع التطور)
    {"id": "hg_c5_s4_r01", "subcategory_id": "hg_c5_s4", "name": "تقرير عن برنامج تحفيز الطلاب", "order": 1},
    {"id": "hg_c5_s4_r02", "subcategory_id": "hg_c5_s4", "name": "سجل عبارات التشجيع اليومية", "order": 2},
    {"id": "hg_c5_s4_r03", "subcategory_id": "hg_c5_s4", "name": "خطة تعزيز الثقة بالنفس", "order": 3},
    {"id": "hg_c5_s4_r04", "subcategory_id": "hg_c5_s4", "name": "إحصائية عدد الطلاب المكرمين", "order": 4},
    {"id": "hg_c5_s4_r05", "subcategory_id": "hg_c5_s4", "name": "تقييم أثر التحفيز على الأداء", "order": 5},
    {"id": "hg_c5_s4_r06", "subcategory_id": "hg_c5_s4", "name": "توعية المعلمين بأهمية الثناء", "order": 6},
    {"id": "hg_c5_s4_r07", "subcategory_id": "hg_c5_s4", "name": "تنسيق مع الإذاعة المدرسية", "order": 7},
    {"id": "hg_c5_s4_r08", "subcategory_id": "hg_c5_s4", "name": "تحسين جوائز التميز", "order": 8},
    {"id": "hg_c5_s4_r09", "subcategory_id": "hg_c5_s4", "name": "متابعة دوافع الطلاب", "order": 9},
    {"id": "hg_c5_s4_r10", "subcategory_id": "hg_c5_s4", "name": "إنجازات التحفيز والتشجيع", "order": 10},

    # hg_c5_s5 (استخدام التكنولوجيا لتقديم الإفادة)
    {"id": "hg_c5_s5_r01", "subcategory_id": "hg_c5_s5", "name": "تقرير عن التصحيح الإلكتروني", "order": 1},
    {"id": "hg_c5_s5_r02", "subcategory_id": "hg_c5_s5", "name": "سجل الإفادة عبر منصة مدرستي", "order": 2},
    {"id": "hg_c5_s5_r03", "subcategory_id": "hg_c5_s5", "name": "خطة توظيف البريد الإلكتروني", "order": 3},
    {"id": "hg_c5_s5_r04", "subcategory_id": "hg_c5_s5", "name": "إحصائية عدد الإفادات الرقمية", "order": 4},
    {"id": "hg_c5_s5_r05", "subcategory_id": "hg_c5_s5", "name": "تقييم وصول الإفادة للطلاب", "order": 5},
    {"id": "hg_c5_s5_r06", "subcategory_id": "hg_c5_s5", "name": "توعية الطلاب باستخدام التقنية", "order": 6},
    {"id": "hg_c5_s5_r07", "subcategory_id": "hg_c5_s5", "name": "تنسيق مع الدعم التقني", "order": 7},
    {"id": "hg_c5_s5_r08", "subcategory_id": "hg_c5_s5", "name": "تحسين أدوات الإفادة", "order": 8},
    {"id": "hg_c5_s5_r09", "subcategory_id": "hg_c5_s5", "name": "متابعة تفاعل الطلاب", "order": 9},
    {"id": "hg_c5_s5_r10", "subcategory_id": "hg_c5_s5", "name": "إنجازات التقنية في التقييم", "order": 10},

    # hg_c6_s1 (وضع أهداف تعليمية واضحة)
    {"id": "hg_c6_s1_r01", "subcategory_id": "hg_c6_s1", "name": "تقرير عن صياغة أهداف الوحدات الدراسية", "order": 1},
    {"id": "hg_c6_s1_r02", "subcategory_id": "hg_c6_s1", "name": "سجل مراجعة الأهداف مع الفريق", "order": 2},
    {"id": "hg_c6_s1_r03", "subcategory_id": "hg_c6_s1", "name": "خطة ربط الأهداف بالتقويم", "order": 3},
    {"id": "hg_c6_s1_r04", "subcategory_id": "hg_c6_s1", "name": "إحصائية مدى وضوح الأهداف للمعلمين", "order": 4},
    {"id": "hg_c6_s1_r05", "subcategory_id": "hg_c6_s1", "name": "تقييم قابلية الأهداف للقياس", "order": 5},
    {"id": "hg_c6_s1_r06", "subcategory_id": "hg_c6_s1", "name": "توعية المعلمين بصياغة الأهداف", "order": 6},
    {"id": "hg_c6_s1_r07", "subcategory_id": "hg_c6_s1", "name": "تنسيق مع مشرفي المناهج", "order": 7},
    {"id": "hg_c6_s1_r08", "subcategory_id": "hg_c6_s1", "name": "تحسين دليل الأهداف", "order": 8},
    {"id": "hg_c6_s1_r09", "subcategory_id": "hg_c6_s1", "name": "متابعة تحديث الأهداف", "order": 9},
    {"id": "hg_c6_s1_r10", "subcategory_id": "hg_c6_s1", "name": "إنجازات التخطيط الجيد", "order": 10},

    # hg_c6_s2 (تصميم خطة دراسية)
    {"id": "hg_c6_s2_r01", "subcategory_id": "hg_c6_s2", "name": "تقرير عن توزيع المنهج السنوي", "order": 1},
    {"id": "hg_c6_s2_r02", "subcategory_id": "hg_c6_s2", "name": "سجل تحضير الدروس الأسبوعي", "order": 2},
    {"id": "hg_c6_s2_r03", "subcategory_id": "hg_c6_s2", "name": "خطة تكييف المنهج لذوي الاحتياجات", "order": 3},
    {"id": "hg_c6_s2_r04", "subcategory_id": "hg_c6_s2", "name": "إحصائية مدى تطابق الخطة مع المنهج", "order": 4},
    {"id": "hg_c6_s2_r05", "subcategory_id": "hg_c6_s2", "name": "تقييم مرونة الخطة", "order": 5},
    {"id": "hg_c6_s2_r06", "subcategory_id": "hg_c6_s2", "name": "توعية المعلمين بأهمية التخطيط", "order": 6},
    {"id": "hg_c6_s2_r07", "subcategory_id": "hg_c6_s2", "name": "تنسيق مع رؤساء الأقسام", "order": 7},
    {"id": "hg_c6_s2_r08", "subcategory_id": "hg_c6_s2", "name": "تحسين نماذج التحضير", "order": 8},
    {"id": "hg_c6_s2_r09", "subcategory_id": "hg_c6_s2", "name": "متابعة تنفيذ الخطة", "order": 9},
    {"id": "hg_c6_s2_r10", "subcategory_id": "hg_c6_s2", "name": "إنجازات التخطيط الفعال", "order": 10},

    # hg_c6_s3 (مراجعة الخطط بشكل دوري)
    {"id": "hg_c6_s3_r01", "subcategory_id": "hg_c6_s3", "name": "تقرير عن مراجعة خطط الفصل الأول", "order": 1},
    {"id": "hg_c6_s3_r02", "subcategory_id": "hg_c6_s3", "name": "سجل التعديلات على الخطط", "order": 2},
    {"id": "hg_c6_s3_r03", "subcategory_id": "hg_c6_s3", "name": "خطة التغذية الراجعة للتخطيط", "order": 3},
    {"id": "hg_c6_s3_r04", "subcategory_id": "hg_c6_s3", "name": "إحصائية عدد المراجعات", "order": 4},
    {"id": "hg_c6_s3_r05", "subcategory_id": "hg_c6_s3", "name": "تقييم أثر التعديلات على النتائج", "order": 5},
    {"id": "hg_c6_s3_r06", "subcategory_id": "hg_c6_s3", "name": "توعية المعلمين بمرونة الخطط", "order": 6},
    {"id": "hg_c6_s3_r07", "subcategory_id": "hg_c6_s3", "name": "تنسيق مع وحدة الجودة", "order": 7},
    {"id": "hg_c6_s3_r08", "subcategory_id": "hg_c6_s3", "name": "تحسين آليات المراجعة", "order": 8},
    {"id": "hg_c6_s3_r09", "subcategory_id": "hg_c6_s3", "name": "متابعة تطبيق التعديلات", "order": 9},
    {"id": "hg_c6_s3_r10", "subcategory_id": "hg_c6_s3", "name": "إنجازات التطوير المستمر", "order": 10},

    # hg_c6_s4 (مشاركة الخطط مع الزملاء)
    {"id": "hg_c6_s4_r01", "subcategory_id": "hg_c6_s4", "name": "تقرير عن اجتماعات التخطيط المشترك", "order": 1},
    {"id": "hg_c6_s4_r02", "subcategory_id": "hg_c6_s4", "name": "سجل تبادل خطط الدروس", "order": 2},
    {"id": "hg_c6_s4_r03", "subcategory_id": "hg_c6_s4", "name": "خطة بناء بنك خطط", "order": 3},
    {"id": "hg_c6_s4_r04", "subcategory_id": "hg_c6_s4", "name": "إحصائية عدد الخطط المتشاركة", "order": 4},
    {"id": "hg_c6_s4_r05", "subcategory_id": "hg_c6_s4", "name": "تقييم فائدة المشاركة", "order": 5},
    {"id": "hg_c6_s4_r06", "subcategory_id": "hg_c6_s4", "name": "توعية بأهمية العمل الجماعي", "order": 6},
    {"id": "hg_c6_s4_r07", "subcategory_id": "hg_c6_s4", "name": "تنسيق مع قائد المدرسة", "order": 7},
    {"id": "hg_c6_s4_r08", "subcategory_id": "hg_c6_s4", "name": "تحسين منصات المشاركة", "order": 8},
    {"id": "hg_c6_s4_r09", "subcategory_id": "hg_c6_s4", "name": "متابعة تطبيق الملاحظات", "order": 9},
    {"id": "hg_c6_s4_r10", "subcategory_id": "hg_c6_s4", "name": "إنجازات التعاون المهني", "order": 10},

    # hg_c6_s5 (تفهم الخصائص النفسية للمرحلة العمرية)
    {"id": "hg_c6_s5_r01", "subcategory_id": "hg_c6_s5", "name": "تقرير عن دراسة خصائص المرحلة الابتدائية", "order": 1},
    {"id": "hg_c6_s5_r02", "subcategory_id": "hg_c6_s5", "name": "سجل تطبيقات على نظريات النمو", "order": 2},
    {"id": "hg_c6_s5_r03", "subcategory_id": "hg_c6_s5", "name": "خطة تدريب المعلمين على الخصائص النفسية", "order": 3},
    {"id": "hg_c6_s5_r04", "subcategory_id": "hg_c6_s5", "name": "إحصائية مدى مراعاة الخصائص", "order": 4},
    {"id": "hg_c6_s5_r05", "subcategory_id": "hg_c6_s5", "name": "تقييم أثر ذلك على التفاعل", "order": 5},
    {"id": "hg_c6_s5_r06", "subcategory_id": "hg_c6_s5", "name": "توعية المعلمين بالمرونة", "order": 6},
    {"id": "hg_c6_s5_r07", "subcategory_id": "hg_c6_s5", "name": "تنسيق مع المرشد الطلابي", "order": 7},
    {"id": "hg_c6_s5_r08", "subcategory_id": "hg_c6_s5", "name": "تحسين استراتيجيات التدريس", "order": 8},
    {"id": "hg_c6_s5_r09", "subcategory_id": "hg_c6_s5", "name": "متابعة تكيف الطلاب", "order": 9},
    {"id": "hg_c6_s5_r10", "subcategory_id": "hg_c6_s5", "name": "إنجازات الفهم النفسي", "order": 10},

    # hg_c7_s1 (استخدام السبورات الذكية)
    {"id": "hg_c7_s1_r01", "subcategory_id": "hg_c7_s1", "name": "تقرير عن تفعيل السبورة التفاعلية", "order": 1},
    {"id": "hg_c7_s1_r02", "subcategory_id": "hg_c7_s1", "name": "سجل استخدام الأجهزة اللوحية", "order": 2},
    {"id": "hg_c7_s1_r03", "subcategory_id": "hg_c7_s1", "name": "خطة صيانة الأجهزة", "order": 3},
    {"id": "hg_c7_s1_r04", "subcategory_id": "hg_c7_s1", "name": "إحصائية عدد الحصص المستخدمة", "order": 4},
    {"id": "hg_c7_s1_r05", "subcategory_id": "hg_c7_s1", "name": "تقييم كفاءة استخدام التقنية", "order": 5},
    {"id": "hg_c7_s1_r06", "subcategory_id": "hg_c7_s1", "name": "توعية المعلمين بالميزات", "order": 6},
    {"id": "hg_c7_s1_r07", "subcategory_id": "hg_c7_s1", "name": "تنسيق مع تقنية المعلومات", "order": 7},
    {"id": "hg_c7_s1_r08", "subcategory_id": "hg_c7_s1", "name": "تحسين محتوى العروض", "order": 8},
    {"id": "hg_c7_s1_r09", "subcategory_id": "hg_c7_s1", "name": "متابعة تحديث البرامج", "order": 9},
    {"id": "hg_c7_s1_r10", "subcategory_id": "hg_c7_s1", "name": "إنجازات التعلم التفاعلي", "order": 10},

    # hg_c7_s2 (تطبيق برامج التعلم الإلكتروني)
    {"id": "hg_c7_s2_r01", "subcategory_id": "hg_c7_s2", "name": "تقرير عن استخدام منصة مدرستي", "order": 1},
    {"id": "hg_c7_s2_r02", "subcategory_id": "hg_c7_s2", "name": "سجل الدروس الافتراضية", "order": 2},
    {"id": "hg_c7_s2_r03", "subcategory_id": "hg_c7_s2", "name": "خطة دمج المنصات في التعليم", "order": 3},
    {"id": "hg_c7_s2_r04", "subcategory_id": "hg_c7_s2", "name": "إحصائية تفاعل الطلاب", "order": 4},
    {"id": "hg_c7_s2_r05", "subcategory_id": "hg_c7_s2", "name": "تقييم فعالية المحتوى الرقمي", "order": 5},
    {"id": "hg_c7_s2_r06", "subcategory_id": "hg_c7_s2", "name": "توعية الطلاب بالمنصات", "order": 6},
    {"id": "hg_c7_s2_r07", "subcategory_id": "hg_c7_s2", "name": "تنسيق مع الدعم الفني", "order": 7},
    {"id": "hg_c7_s2_r08", "subcategory_id": "hg_c7_s2", "name": "تحسين جودة المواد", "order": 8},
    {"id": "hg_c7_s2_r09", "subcategory_id": "hg_c7_s2", "name": "متابعة تقارير المنصة", "order": 9},
    {"id": "hg_c7_s2_r10", "subcategory_id": "hg_c7_s2", "name": "إنجازات التعليم عن بعد", "order": 10},

    # hg_c7_s3 (تشجيع الطلاب على استخدام التطبيقات التعليمية)
    {"id": "hg_c7_s3_r01", "subcategory_id": "hg_c7_s3", "name": "تقرير عن مسابقة أفضل تطبيق تعليمي", "order": 1},
    {"id": "hg_c7_s3_r02", "subcategory_id": "hg_c7_s3", "name": "سجل التطبيقات الموصى بها", "order": 2},
    {"id": "hg_c7_s3_r03", "subcategory_id": "hg_c7_s3", "name": "خطة تحفيز التعلم الذاتي", "order": 3},
    {"id": "hg_c7_s3_r04", "subcategory_id": "hg_c7_s3", "name": "إحصائية عدد الطلاب المستخدمين", "order": 4},
    {"id": "hg_c7_s3_r05", "subcategory_id": "hg_c7_s3", "name": "تقييم أثر التطبيقات على التحصيل", "order": 5},
    {"id": "hg_c7_s3_r06", "subcategory_id": "hg_c7_s3", "name": "توعية أولياء الأمور", "order": 6},
    {"id": "hg_c7_s3_r07", "subcategory_id": "hg_c7_s3", "name": "تنسيق مع مختصي التقنية", "order": 7},
    {"id": "hg_c7_s3_r08", "subcategory_id": "hg_c7_s3", "name": "تحسين قائمة التطبيقات", "order": 8},
    {"id": "hg_c7_s3_r09", "subcategory_id": "hg_c7_s3", "name": "متابعة تحديث التطبيقات", "order": 9},
    {"id": "hg_c7_s3_r10", "subcategory_id": "hg_c7_s3", "name": "إنجازات التعلم الذاتي", "order": 10},

    # hg_c7_s4 (تنظيم ورش عمل حول استخدام التكنولوجيا)
    {"id": "hg_c7_s4_r01", "subcategory_id": "hg_c7_s4", "name": "تقرير عن ورشة تصميم الدروس التفاعلية", "order": 1},
    {"id": "hg_c7_s4_r02", "subcategory_id": "hg_c7_s4", "name": "سجل حضور ورش التقنية", "order": 2},
    {"id": "hg_c7_s4_r03", "subcategory_id": "hg_c7_s4", "name": "خطة تطوير كفايات المعلمين الرقمية", "order": 3},
    {"id": "hg_c7_s4_r04", "subcategory_id": "hg_c7_s4", "name": "إحصائية عدد الورش المنفذة", "order": 4},
    {"id": "hg_c7_s4_r05", "subcategory_id": "hg_c7_s4", "name": "تقييم رضا المشاركين", "order": 5},
    {"id": "hg_c7_s4_r06", "subcategory_id": "hg_c7_s4", "name": "توعية بأهمية التطوير التقني", "order": 6},
    {"id": "hg_c7_s4_r07", "subcategory_id": "hg_c7_s4", "name": "تنسيق مع خبراء خارجيين", "order": 7},
    {"id": "hg_c7_s4_r08", "subcategory_id": "hg_c7_s4", "name": "تحسين محتوى الورش", "order": 8},
    {"id": "hg_c7_s4_r09", "subcategory_id": "hg_c7_s4", "name": "متابعة تطبيق المهارات", "order": 9},
    {"id": "hg_c7_s4_r10", "subcategory_id": "hg_c7_s4", "name": "إنجازات التمكين الرقمي", "order": 10},

    # hg_c8_s1 (تزيين الفصل بوسائل جذابة)
    {"id": "hg_c8_s1_r01", "subcategory_id": "hg_c8_s1", "name": "تقرير عن لوحات الفصل التفاعلية", "order": 1},
    {"id": "hg_c8_s1_r02", "subcategory_id": "hg_c8_s1", "name": "سجل تحديث الوسائل البصرية", "order": 2},
    {"id": "hg_c8_s1_r03", "subcategory_id": "hg_c8_s1", "name": "خطة تزيين الفصول", "order": 3},
    {"id": "hg_c8_s1_r04", "subcategory_id": "hg_c8_s1", "name": "إحصائية مشاركة الطلاب في التزيين", "order": 4},
    {"id": "hg_c8_s1_r05", "subcategory_id": "hg_c8_s1", "name": "تقييم جاذبية الفصل", "order": 5},
    {"id": "hg_c8_s1_r06", "subcategory_id": "hg_c8_s1", "name": "توعية بأثر البيئة على التعلم", "order": 6},
    {"id": "hg_c8_s1_r07", "subcategory_id": "hg_c8_s1", "name": "تنسيق مع رائد الفصل", "order": 7},
    {"id": "hg_c8_s1_r08", "subcategory_id": "hg_c8_s1", "name": "تحسين استخدام الألوان", "order": 8},
    {"id": "hg_c8_s1_r09", "subcategory_id": "hg_c8_s1", "name": "متابعة تجديد الوسائل", "order": 9},
    {"id": "hg_c8_s1_r10", "subcategory_id": "hg_c8_s1", "name": "إنجازات البيئة المحفزة", "order": 10},

    # hg_c8_s2 (تنظيم الفصل يسهل الحركة)
    {"id": "hg_c8_s2_r01", "subcategory_id": "hg_c8_s2", "name": "تقرير عن توزيع المقاعد", "order": 1},
    {"id": "hg_c8_s2_r02", "subcategory_id": "hg_c8_s2", "name": "سجل تجارب التنظيم المختلفة", "order": 2},
    {"id": "hg_c8_s2_r03", "subcategory_id": "hg_c8_s2", "name": "خطة مرونة تنظيم الفصل", "order": 3},
    {"id": "hg_c8_s2_r04", "subcategory_id": "hg_c8_s2", "name": "إحصائية راحة الطلاب", "order": 4},
    {"id": "hg_c8_s2_r05", "subcategory_id": "hg_c8_s2", "name": "تقييم تأثير التنظيم على التفاعل", "order": 5},
    {"id": "hg_c8_s2_r06", "subcategory_id": "hg_c8_s2", "name": "توعية المعلمين بأهمية التهيئة", "order": 6},
    {"id": "hg_c8_s2_r07", "subcategory_id": "hg_c8_s2", "name": "تنسيق مع إدارة المدرسة", "order": 7},
    {"id": "hg_c8_s2_r08", "subcategory_id": "hg_c8_s2", "name": "تحسين مسارات الحركة", "order": 8},
    {"id": "hg_c8_s2_r09", "subcategory_id": "hg_c8_s2", "name": "متابعة تطبيق الأنشطة", "order": 9},
    {"id": "hg_c8_s2_r10", "subcategory_id": "hg_c8_s2", "name": "إنجازات التنظيم الفعال", "order": 10},

    # hg_c8_s3 (توفير الأدوات والموارد)
    {"id": "hg_c8_s3_r01", "subcategory_id": "hg_c8_s3", "name": "تقرير عن جرد الوسائل التعليمية", "order": 1},
    {"id": "hg_c8_s3_r02", "subcategory_id": "hg_c8_s3", "name": "سجل توفير المواد الاستهلاكية", "order": 2},
    {"id": "hg_c8_s3_r03", "subcategory_id": "hg_c8_s3", "name": "خطة تأمين الاحتياجات", "order": 3},
    {"id": "hg_c8_s3_r04", "subcategory_id": "hg_c8_s3", "name": "إحصائية توفر الموارد", "order": 4},
    {"id": "hg_c8_s3_r05", "subcategory_id": "hg_c8_s3", "name": "تقييم كفاية الأدوات", "order": 5},
    {"id": "hg_c8_s3_r06", "subcategory_id": "hg_c8_s3", "name": "توعية الطلاب بالمحافظة", "order": 6},
    {"id": "hg_c8_s3_r07", "subcategory_id": "hg_c8_s3", "name": "تنسيق مع قسم المشتريات", "order": 7},
    {"id": "hg_c8_s3_r08", "subcategory_id": "hg_c8_s3", "name": "تحسين آليات الصيانة", "order": 8},
    {"id": "hg_c8_s3_r09", "subcategory_id": "hg_c8_s3", "name": "متابعة استبدال التالف", "order": 9},
    {"id": "hg_c8_s3_r10", "subcategory_id": "hg_c8_s3", "name": "إنجازات تجهيز الفصول", "order": 10},

    # hg_c8_s4 (بيئة آمنة وخالية من الأخطار)
    {"id": "hg_c8_s4_r01", "subcategory_id": "hg_c8_s4", "name": "تقرير عن خطة الإخلاء في الطوارئ", "order": 1},
    {"id": "hg_c8_s4_r02", "subcategory_id": "hg_c8_s4", "name": "سجل صيانة مخارج الطوارئ", "order": 2},
    {"id": "hg_c8_s4_r03", "subcategory_id": "hg_c8_s4", "name": "خطة تعزيز الأمان النفسي", "order": 3},
    {"id": "hg_c8_s4_r04", "subcategory_id": "hg_c8_s4", "name": "إحصائية عدد تدريبات السلامة", "order": 4},
    {"id": "hg_c8_s4_r05", "subcategory_id": "hg_c8_s4", "name": "تقييم وعي الطلاب بالسلامة", "order": 5},
    {"id": "hg_c8_s4_r06", "subcategory_id": "hg_c8_s4", "name": "توعية بالسلوك الآمن", "order": 6},
    {"id": "hg_c8_s4_r07", "subcategory_id": "hg_c8_s4", "name": "تنسيق مع الدفاع المدني", "order": 7},
    {"id": "hg_c8_s4_r08", "subcategory_id": "hg_c8_s4", "name": "تحسين إجراءات الوقاية", "order": 8},
    {"id": "hg_c8_s4_r09", "subcategory_id": "hg_c8_s4", "name": "متابعة رصد المخاطر", "order": 9},
    {"id": "hg_c8_s4_r10", "subcategory_id": "hg_c8_s4", "name": "إنجازات الأمن والسلامة", "order": 10},

    # hg_c8_s5 (تمكين التعبير عن الذات)
    {"id": "hg_c8_s5_r01", "subcategory_id": "hg_c8_s5", "name": "تقرير عن مشاركة الطلاب في القرارات", "order": 1},
    {"id": "hg_c8_s5_r02", "subcategory_id": "hg_c8_s5", "name": "سجل آراء الطلاب في الأنشطة", "order": 2},
    {"id": "hg_c8_s5_r03", "subcategory_id": "hg_c8_s5", "name": "خطة تعزيز الحوار الصفي", "order": 3},
    {"id": "hg_c8_s5_r04", "subcategory_id": "hg_c8_s5", "name": "إحصائية عدد المشاركات", "order": 4},
    {"id": "hg_c8_s5_r05", "subcategory_id": "hg_c8_s5", "name": "تقييم حرية التعبير", "order": 5},
    {"id": "hg_c8_s5_r06", "subcategory_id": "hg_c8_s5", "name": "توعية بأهمية الاستماع", "order": 6},
    {"id": "hg_c8_s5_r07", "subcategory_id": "hg_c8_s5", "name": "تنسيق مع مجلس الطلاب", "order": 7},
    {"id": "hg_c8_s5_r08", "subcategory_id": "hg_c8_s5", "name": "تحسين قنوات الاقتراح", "order": 8},
    {"id": "hg_c8_s5_r09", "subcategory_id": "hg_c8_s5", "name": "متابعة تنفيذ الأفكار", "order": 9},
    {"id": "hg_c8_s5_r10", "subcategory_id": "hg_c8_s5", "name": "إنجازات المشاركة الطلابية", "order": 10},

    # hg_c8_s6 (إثارة دافعية المتعلمين)
    {"id": "hg_c8_s6_r01", "subcategory_id": "hg_c8_s6", "name": "تقرير عن استخدام الألعاب التعليمية", "order": 1},
    {"id": "hg_c8_s6_r02", "subcategory_id": "hg_c8_s6", "name": "سجل قصص النجاح التحفيزية", "order": 2},
    {"id": "hg_c8_s6_r03", "subcategory_id": "hg_c8_s6", "name": "خطة تنويع المثيرات", "order": 3},
    {"id": "hg_c8_s6_r04", "subcategory_id": "hg_c8_s6", "name": "إحصائية مستويات الحماس", "order": 4},
    {"id": "hg_c8_s6_r05", "subcategory_id": "hg_c8_s6", "name": "تقييم أثر التحفيز", "order": 5},
    {"id": "hg_c8_s6_r06", "subcategory_id": "hg_c8_s6", "name": "توعية المعلمين باستراتيجيات التحفيز", "order": 6},
    {"id": "hg_c8_s6_r07", "subcategory_id": "hg_c8_s6", "name": "تنسيق مع الأنشطة اللاصفية", "order": 7},
    {"id": "hg_c8_s6_r08", "subcategory_id": "hg_c8_s6", "name": "تحسين أساليب الثناء", "order": 8},
    {"id": "hg_c8_s6_r09", "subcategory_id": "hg_c8_s6", "name": "متابعة دوافع الطلاب", "order": 9},
    {"id": "hg_c8_s6_r10", "subcategory_id": "hg_c8_s6", "name": "إنجازات رفع الدافعية", "order": 10},

    # hg_c9_s1 (استخدام اختبارات تقييمية دورية)
    {"id": "hg_c9_s1_r01", "subcategory_id": "hg_c9_s1", "name": "تقرير عن جدول الاختبارات القصيرة", "order": 1},
    {"id": "hg_c9_s1_r02", "subcategory_id": "hg_c9_s1", "name": "سجل نتائج الاختبارات الشهرية", "order": 2},
    {"id": "hg_c9_s1_r03", "subcategory_id": "hg_c9_s1", "name": "خطة تنويع أدوات القياس", "order": 3},
    {"id": "hg_c9_s1_r04", "subcategory_id": "hg_c9_s1", "name": "إحصائية مدى انتظام الاختبارات", "order": 4},
    {"id": "hg_c9_s1_r05", "subcategory_id": "hg_c9_s1", "name": "تقييم جودة الاختبارات", "order": 5},
    {"id": "hg_c9_s1_r06", "subcategory_id": "hg_c9_s1", "name": "توعية الطلاب بأهمية التقويم", "order": 6},
    {"id": "hg_c9_s1_r07", "subcategory_id": "hg_c9_s1", "name": "تنسيق مع لجنة الاختبارات", "order": 7},
    {"id": "hg_c9_s1_r08", "subcategory_id": "hg_c9_s1", "name": "تحسين أسئلة الاختبارات", "order": 8},
    {"id": "hg_c9_s1_r09", "subcategory_id": "hg_c9_s1", "name": "متابعة تصحيح الاختبارات", "order": 9},
    {"id": "hg_c9_s1_r10", "subcategory_id": "hg_c9_s1", "name": "إنجازات التقويم المستمر", "order": 10},

    # hg_c9_s2 (تحليل النتائج وتحديد نقاط القوة والضعف)
    {"id": "hg_c9_s2_r01", "subcategory_id": "hg_c9_s2", "name": "تقرير تحليل نتائج الفصل الأول", "order": 1},
    {"id": "hg_c9_s2_r02", "subcategory_id": "hg_c9_s2", "name": "سجل اجتماعات تحليل النتائج", "order": 2},
    {"id": "hg_c9_s2_r03", "subcategory_id": "hg_c9_s2", "name": "خطة مشاركة الطلاب في تحليل أدائهم", "order": 3},
    {"id": "hg_c9_s2_r04", "subcategory_id": "hg_c9_s2", "name": "إحصائية المهارات الضعيفة", "order": 4},
    {"id": "hg_c9_s2_r05", "subcategory_id": "hg_c9_s2", "name": "تقييم دقة التحليل", "order": 5},
    {"id": "hg_c9_s2_r06", "subcategory_id": "hg_c9_s2", "name": "توعية المعلمين بتحليل البيانات", "order": 6},
    {"id": "hg_c9_s2_r07", "subcategory_id": "hg_c9_s2", "name": "تنسيق مع وحدة القياس", "order": 7},
    {"id": "hg_c9_s2_r08", "subcategory_id": "hg_c9_s2", "name": "تحسين أدوات التحليل", "order": 8},
    {"id": "hg_c9_s2_r09", "subcategory_id": "hg_c9_s2", "name": "متابعة خطط التحسين", "order": 9},
    {"id": "hg_c9_s2_r10", "subcategory_id": "hg_c9_s2", "name": "إنجازات التحليل التربوي", "order": 10},

    # hg_c9_s3 (توفير تغذية راجعة فردية)
    {"id": "hg_c9_s3_r01", "subcategory_id": "hg_c9_s3", "name": "تقرير عن لقاءات التوجيه الفردي", "order": 1},
    {"id": "hg_c9_s3_r02", "subcategory_id": "hg_c9_s3", "name": "سجل الملاحظات الشخصية لكل طالب", "order": 2},
    {"id": "hg_c9_s3_r03", "subcategory_id": "hg_c9_s3", "name": "خطة تخصيص التغذية الراجعة", "order": 3},
    {"id": "hg_c9_s3_r04", "subcategory_id": "hg_c9_s3", "name": "إحصائية عدد الطلاب المستفيدين", "order": 4},
    {"id": "hg_c9_s3_r05", "subcategory_id": "hg_c9_s3", "name": "تقييم أثر التغذية الفردية", "order": 5},
    {"id": "hg_c9_s3_r06", "subcategory_id": "hg_c9_s3", "name": "توعية بأهمية المتابعة الفردية", "order": 6},
    {"id": "hg_c9_s3_r07", "subcategory_id": "hg_c9_s3", "name": "تنسيق مع أولياء الأمور", "order": 7},
    {"id": "hg_c9_s3_r08", "subcategory_id": "hg_c9_s3", "name": "تحسين جودة اللقاءات", "order": 8},
    {"id": "hg_c9_s3_r09", "subcategory_id": "hg_c9_s3", "name": "متابعة تنفيذ التوصيات", "order": 9},
    {"id": "hg_c9_s3_r10", "subcategory_id": "hg_c9_s3", "name": "إنجازات الرعاية الفردية", "order": 10},

    # hg_c9_s4 (تطبيق خطط علاجية)
    {"id": "hg_c9_s4_r01", "subcategory_id": "hg_c9_s4", "name": "تقرير عن برنامج التقوية في الرياضيات", "order": 1},
    {"id": "hg_c9_s4_r02", "subcategory_id": "hg_c9_s4", "name": "سجل حضور الطلاب للخطة العلاجية", "order": 2},
    {"id": "hg_c9_s4_r03", "subcategory_id": "hg_c9_s4", "name": "خطة تصميم البرامج العلاجية", "order": 3},
    {"id": "hg_c9_s4_r04", "subcategory_id": "hg_c9_s4", "name": "إحصائية تحسن الطلاب", "order": 4},
    {"id": "hg_c9_s4_r05", "subcategory_id": "hg_c9_s4", "name": "تقييم فعالية الخطط", "order": 5},
    {"id": "hg_c9_s4_r06", "subcategory_id": "hg_c9_s4", "name": "توعية المعلمين بالاستراتيجيات العلاجية", "order": 6},
    {"id": "hg_c9_s4_r07", "subcategory_id": "hg_c9_s4", "name": "تنسيق مع معلمي المواد", "order": 7},
    {"id": "hg_c9_s4_r08", "subcategory_id": "hg_c9_s4", "name": "تحسين أنشطة العلاج", "order": 8},
    {"id": "hg_c9_s4_r09", "subcategory_id": "hg_c9_s4", "name": "متابعة استمرارية الدعم", "order": 9},
    {"id": "hg_c9_s4_r10", "subcategory_id": "hg_c9_s4", "name": "إنجازات البرامج العلاجية", "order": 10},

    # hg_c9_s5 (قياس التطبيق العملي للمعرفة)
    {"id": "hg_c9_s5_r01", "subcategory_id": "hg_c9_s5", "name": "تقرير عن معرض المشاريع العلمية", "order": 1},
    {"id": "hg_c9_s5_r02", "subcategory_id": "hg_c9_s5", "name": "سجل تقييم الأداء العملي", "order": 2},
    {"id": "hg_c9_s5_r03", "subcategory_id": "hg_c9_s5", "name": "خطة دمج المواقف الحقيقية", "order": 3},
    {"id": "hg_c9_s5_r04", "subcategory_id": "hg_c9_s5", "name": "إحصائية عدد المشاريع", "order": 4},
    {"id": "hg_c9_s5_r05", "subcategory_id": "hg_c9_s5", "name": "تقييم مهارات التطبيق", "order": 5},
    {"id": "hg_c9_s5_r06", "subcategory_id": "hg_c9_s5", "name": "توعية بأهمية التطبيق", "order": 6},
    {"id": "hg_c9_s5_r07", "subcategory_id": "hg_c9_s5", "name": "تنسيق مع مؤسسات خارجية", "order": 7},
    {"id": "hg_c9_s5_r08", "subcategory_id": "hg_c9_s5", "name": "تحسين معايير التقييم العملي", "order": 8},
    {"id": "hg_c9_s5_r09", "subcategory_id": "hg_c9_s5", "name": "متابعة تنفيذ المشاريع", "order": 9},
    {"id": "hg_c9_s5_r10", "subcategory_id": "hg_c9_s5", "name": "إنجازات التعلم التطبيقي", "order": 10},

    # hg_c10_s1 (استخدام الاختبارات الكتابية والشفوية)
    {"id": "hg_c10_s1_r01", "subcategory_id": "hg_c10_s1", "name": "تقرير عن مواصفات الاختبارات النهائية", "order": 1},
    {"id": "hg_c10_s1_r02", "subcategory_id": "hg_c10_s1", "name": "سجل نتائج الاختبارات الشفوية", "order": 2},
    {"id": "hg_c10_s1_r03", "subcategory_id": "hg_c10_s1", "name": "خطة تنويع أسئلة الاختبارات", "order": 3},
    {"id": "hg_c10_s1_r04", "subcategory_id": "hg_c10_s1", "name": "إحصائية التوازن بين كتابي وشفوي", "order": 4},
    {"id": "hg_c10_s1_r05", "subcategory_id": "hg_c10_s1", "name": "تقييم شمولية الاختبارات", "order": 5},
    {"id": "hg_c10_s1_r06", "subcategory_id": "hg_c10_s1", "name": "توعية الطلاب بأنماط الاختبارات", "order": 6},
    {"id": "hg_c10_s1_r07", "subcategory_id": "hg_c10_s1", "name": "تنسيق مع لجنة التطوير", "order": 7},
    {"id": "hg_c10_s1_r08", "subcategory_id": "hg_c10_s1", "name": "تحسين دقة التصحيح", "order": 8},
    {"id": "hg_c10_s1_r09", "subcategory_id": "hg_c10_s1", "name": "متابعة تطبيق الاختبارات", "order": 9},
    {"id": "hg_c10_s1_r10", "subcategory_id": "hg_c10_s1", "name": "إنجازات التقويم المتوازن", "order": 10},

    # hg_c10_s2 (تطبيق التقييم العملي)
    {"id": "hg_c10_s2_r01", "subcategory_id": "hg_c10_s2", "name": "تقرير عن تقييم المشاريع الجماعية", "order": 1},
    {"id": "hg_c10_s2_r02", "subcategory_id": "hg_c10_s2", "name": "سجل أداء الطلاب في العروض", "order": 2},
    {"id": "hg_c10_s2_r03", "subcategory_id": "hg_c10_s2", "name": "خطة تطوير التقييم العملي", "order": 3},
    {"id": "hg_c10_s2_r04", "subcategory_id": "hg_c10_s2", "name": "إحصائية عدد الأنشطة العملية", "order": 4},
    {"id": "hg_c10_s2_r05", "subcategory_id": "hg_c10_s2", "name": "تقييم مدى موضوعية التقييم", "order": 5},
    {"id": "hg_c10_s2_r06", "subcategory_id": "hg_c10_s2", "name": "توعية المعلمين بأدوات التقييم", "order": 6},
    {"id": "hg_c10_s2_r07", "subcategory_id": "hg_c10_s2", "name": "تنسيق مع المختبرات", "order": 7},
    {"id": "hg_c10_s2_r08", "subcategory_id": "hg_c10_s2", "name": "تحسين معايير التقييم", "order": 8},
    {"id": "hg_c10_s2_r09", "subcategory_id": "hg_c10_s2", "name": "متابعة تنفيذ المشاريع", "order": 9},
    {"id": "hg_c10_s2_r10", "subcategory_id": "hg_c10_s2", "name": "إنجازات التقييم الأدائي", "order": 10},

    # hg_c10_s3 (استخدام التقييم التكويني)
    {"id": "hg_c10_s3_r01", "subcategory_id": "hg_c10_s3", "name": "تقرير عن استخدام بطاقات الملاحظة", "order": 1},
    {"id": "hg_c10_s3_r02", "subcategory_id": "hg_c10_s3", "name": "سجل التقييمات الأسبوعية", "order": 2},
    {"id": "hg_c10_s3_r03", "subcategory_id": "hg_c10_s3", "name": "خطة دمج التكويني في الدروس", "order": 3},
    {"id": "hg_c10_s3_r04", "subcategory_id": "hg_c10_s3", "name": "إحصائية عدد التقييمات التكوينية", "order": 4},
    {"id": "hg_c10_s3_r05", "subcategory_id": "hg_c10_s3", "name": "تقييم فاعليته في التحسين", "order": 5},
    {"id": "hg_c10_s3_r06", "subcategory_id": "hg_c10_s3", "name": "توعية المعلمين بأهميته", "order": 6},
    {"id": "hg_c10_s3_r07", "subcategory_id": "hg_c10_s3", "name": "تنسيق مع الإشراف التربوي", "order": 7},
    {"id": "hg_c10_s3_r08", "subcategory_id": "hg_c10_s3", "name": "تحسين أدوات التقييم", "order": 8},
    {"id": "hg_c10_s3_r09", "subcategory_id": "hg_c10_s3", "name": "متابعة استجابة الطلاب", "order": 9},
    {"id": "hg_c10_s3_r10", "subcategory_id": "hg_c10_s3", "name": "إنجازات التقويم المستمر", "order": 10},

    # hg_c10_s4 (استخدام التقويم القبلي)
    {"id": "hg_c10_s4_r01", "subcategory_id": "hg_c10_s4", "name": "تقرير عن اختبارات تحديد المستوى", "order": 1},
    {"id": "hg_c10_s4_r02", "subcategory_id": "hg_c10_s4", "name": "سجل نتائج التقويم القبلي", "order": 2},
    {"id": "hg_c10_s4_r03", "subcategory_id": "hg_c10_s4", "name": "خطة تشخيص المعرفة السابقة", "order": 3},
    {"id": "hg_c10_s4_r04", "subcategory_id": "hg_c10_s4", "name": "إحصائية مدى الاستعداد", "order": 4},
    {"id": "hg_c10_s4_r05", "subcategory_id": "hg_c10_s4", "name": "تقييم دقة التشخيص", "order": 5},
    {"id": "hg_c10_s4_r06", "subcategory_id": "hg_c10_s4", "name": "توعية المعلمين بأهمية القبلي", "order": 6},
    {"id": "hg_c10_s4_r07", "subcategory_id": "hg_c10_s4", "name": "تنسيق مع التخطيط", "order": 7},
    {"id": "hg_c10_s4_r08", "subcategory_id": "hg_c10_s4", "name": "تحسين أدوات القبلي", "order": 8},
    {"id": "hg_c10_s4_r09", "subcategory_id": "hg_c10_s4", "name": "متابعة تكييف الخطط", "order": 9},
    {"id": "hg_c10_s4_r10", "subcategory_id": "hg_c10_s4", "name": "إنجازات التشخيص المبكر", "order": 10},

    # hg_c10_s5 (تطبيق التقويم الختامي)
    {"id": "hg_c10_s5_r01", "subcategory_id": "hg_c10_s5", "name": "تقرير عن نتائج الفصل الدراسي", "order": 1},
    {"id": "hg_c10_s5_r02", "subcategory_id": "hg_c10_s5", "name": "سجل نسب النجاح", "order": 2},
    {"id": "hg_c10_s5_r03", "subcategory_id": "hg_c10_s5", "name": "خطة تحسين نتائج الختامي", "order": 3},
    {"id": "hg_c10_s5_r04", "subcategory_id": "hg_c10_s5", "name": "إحصائية توزيع الدرجات", "order": 4},
    {"id": "hg_c10_s5_r05", "subcategory_id": "hg_c10_s5", "name": "تقييم مصداقية الاختبارات", "order": 5},
    {"id": "hg_c10_s5_r06", "subcategory_id": "hg_c10_s5", "name": "توعية بأهمية الختامي", "order": 6},
    {"id": "hg_c10_s5_r07", "subcategory_id": "hg_c10_s5", "name": "تنسيق مع الكنترول", "order": 7},
    {"id": "hg_c10_s5_r08", "subcategory_id": "hg_c10_s5", "name": "تحسين إجراءات التصحيح", "order": 8},
    {"id": "hg_c10_s5_r09", "subcategory_id": "hg_c10_s5", "name": "متابعة إعلان النتائج", "order": 9},
    {"id": "hg_c10_s5_r10", "subcategory_id": "hg_c10_s5", "name": "إنجازات التقويم النهائي", "order": 10},

    # hg_c11_s1 (تنفيذ الخطة المشتركة للبرامج الصحية المدرسية)
    {"id": "hg_c11_s1_r01", "subcategory_id": "hg_c11_s1", "name": "تقرير عن تنفيذ برنامج التطعيمات المدرسية", "order": 1},
    {"id": "hg_c11_s1_r02", "subcategory_id": "hg_c11_s1", "name": "سجل متابعة الخطة الصحية السنوية", "order": 2},
    {"id": "hg_c11_s1_r03", "subcategory_id": "hg_c11_s1", "name": "خطة تفعيل البرامج الصحية المشتركة", "order": 3},
    {"id": "hg_c11_s1_r04", "subcategory_id": "hg_c11_s1", "name": "إحصائية عدد المستفيدين من البرامج", "order": 4},
    {"id": "hg_c11_s1_r05", "subcategory_id": "hg_c11_s1", "name": "تقييم التعاون مع الجهات الصحية", "order": 5},
    {"id": "hg_c11_s1_r06", "subcategory_id": "hg_c11_s1", "name": "توعية الطلاب بالبرامج الصحية", "order": 6},
    {"id": "hg_c11_s1_r07", "subcategory_id": "hg_c11_s1", "name": "تنسيق مع وزارة الصحة", "order": 7},
    {"id": "hg_c11_s1_r08", "subcategory_id": "hg_c11_s1", "name": "تحسين تنفيذ الحملات الصحية", "order": 8},
    {"id": "hg_c11_s1_r09", "subcategory_id": "hg_c11_s1", "name": "متابعة تقارير البرامج", "order": 9},
    {"id": "hg_c11_s1_r10", "subcategory_id": "hg_c11_s1", "name": "إنجازات الخطة الصحية", "order": 10},

    # hg_c12_s1 (حصر الحالات الصحية للمتعلمين)
    {"id": "hg_c12_s1_r01", "subcategory_id": "hg_c12_s1", "name": "تقرير عن مسح الحالات الصحية للطلاب", "order": 1},
    {"id": "hg_c12_s1_r02", "subcategory_id": "hg_c12_s1", "name": "سجل الأمراض المزمنة (سكري - ربو)", "order": 2},
    {"id": "hg_c12_s1_r03", "subcategory_id": "hg_c12_s1", "name": "خطة متابعة الحالات المحصورة", "order": 3},
    {"id": "hg_c12_s1_r04", "subcategory_id": "hg_c12_s1", "name": "إحصائية أنواع الحالات الصحية", "order": 4},
    {"id": "hg_c12_s1_r05", "subcategory_id": "hg_c12_s1", "name": "تقييم دقة الحصر", "order": 5},
    {"id": "hg_c12_s1_r06", "subcategory_id": "hg_c12_s1", "name": "توعية أولياء الأمور بأهمية الإبلاغ", "order": 6},
    {"id": "hg_c12_s1_r07", "subcategory_id": "hg_c12_s1", "name": "تنسيق مع العيادة المدرسية", "order": 7},
    {"id": "hg_c12_s1_r08", "subcategory_id": "hg_c12_s1", "name": "تحسين قاعدة البيانات الصحية", "order": 8},
    {"id": "hg_c12_s1_r09", "subcategory_id": "hg_c12_s1", "name": "متابعة تحديث الحالات", "order": 9},
    {"id": "hg_c12_s1_r10", "subcategory_id": "hg_c12_s1", "name": "إنجازات الحصر الصحي", "order": 10},

    # hg_c13_s1 (تهيئة البيئة الصحية المدرسية)
    {"id": "hg_c13_s1_r01", "subcategory_id": "hg_c13_s1", "name": "تقرير عن نظافة المرافق الصحية", "order": 1},
    {"id": "hg_c13_s1_r02", "subcategory_id": "hg_c13_s1", "name": "سجل جودة التهوية في الفصول", "order": 2},
    {"id": "hg_c13_s1_r03", "subcategory_id": "hg_c13_s1", "name": "خطة تحسين البيئة الصحية", "order": 3},
    {"id": "hg_c13_s1_r04", "subcategory_id": "hg_c13_s1", "name": "إحصائية مدى الالتزام بالاشتراطات الصحية", "order": 4},
    {"id": "hg_c13_s1_r05", "subcategory_id": "hg_c13_s1", "name": "تقييم سلامة مياه الشرب", "order": 5},
    {"id": "hg_c13_s1_r06", "subcategory_id": "hg_c13_s1", "name": "توعية الطلاب بالنظافة العامة", "order": 6},
    {"id": "hg_c13_s1_r07", "subcategory_id": "hg_c13_s1", "name": "تنسيق مع البلدية", "order": 7},
    {"id": "hg_c13_s1_r08", "subcategory_id": "hg_c13_s1", "name": "تحسين إجراءات مكافحة العدوى", "order": 8},
    {"id": "hg_c13_s1_r09", "subcategory_id": "hg_c13_s1", "name": "متابعة تعقيم الأسطح", "order": 9},
    {"id": "hg_c13_s1_r10", "subcategory_id": "hg_c13_s1", "name": "إنجازات البيئة الصحية", "order": 10}
]

# قالب البرومبت (محدث ليشمل الجوانب التربوية والصحية)
HEALTH_GUIDE_PROMPT_TEMPLATE = """أنت موجه صحي وتربوي مسؤول عن تنفيذ البرامج الصحية المدرسية وتعزيز بيئة تعليمية آمنة ومحفزة وفق الأنظمة المعتمدة.

المطلوب:
- عرض معيار الأداء الوظيفي.
- عرض التصنيف الفرعي.
- كتابة تقرير مهني يوضح الإجراءات والممارسات المرتبطة بهذا التصنيف.

التقرير المطلوب: "{report_name}"
وهو يندرج تحت التصنيف الفرعي: "{subcategory_name}"
ضمن المعيار التربوي: "{criterion_name}"

{subject_line}
{lesson_line}
{grade_line}
{target_line}
{place_line}
{count_line}

ضوابط الكتابة:- كن مهنيًا وموضوعيًا ومتزنًا بصيغة إدارية تربوية صحية رسمية.  
- أبرز دورك في الوقاية والتوعية والمتابعة الصحية والتربوية داخل المدرسة.  
- وضّح آلية تنفيذ البرامج والمبادرات بدقة مع بيان الأثر.  
- أشر إلى رصد الحالات الصحية والسلوكية والتنسيق مع الجهات المختصة.  
- بيّن دورك في تهيئة بيئة مدرسية آمنة وصحية ومحفزة للتعلم.  
- أبرز استخدام التقنية أو النماذج المعتمدة في التوثيق والمتابعة.  
- وضّح أثر الجهود على سلامة الطلاب واستقرار العملية التعليمية.  

⚠️ **ضوابط بنائية إلزامية للتقرير (تنطبق على جميع الحقول):**

1) **الفئة المستهدفة:**  
   يجب أن تنعكس الفئة المذكورة في (المستهدفون) في جميع الحقول دون استثناء، مع اتساق كامل بين الهدف والتنفيذ والنتائج.

2) **السياق التنفيذي:**  
   إذا ذُكر برنامج صحي تربوي محدد، يجب أن ترتبط جميع الحقول بطبيعته وآلية تطبيقه داخل المدرسة دون تعميم.

3) **في حال عدم ذكر برنامج محدد:**  
   يكون المحتوى متعلقًا بالممارسة العامة للموجه الصحي التربوي دون إدراج تفاصيل مبادرة بعينها.

4) **مكان التنفيذ:**  
   يجب أن تتوافق الإجراءات مع البيئة المدرسية الفعلية، مع منع وصف أدوار لا ترتبط بالمجال الصحي التربوي.

5) **الترابط الداخلي:**  
   يجب أن تكون الإجراءات مكملة للهدف، والاستراتيجيات مناسبة للتنفيذ، ونقاط القوة والتحسين مبنية على ما ورد، والتوصيات منبثقة من التحسين.

أي إخلال بهذه الضوابط يُعد خللاً مهنيًا في بناء التقرير.  
تحقق داخليًا من الاتساق الكامل قبل إخراج الإجابة.  

**شروط المحتوى:**  
- يكتب كل حقل في حدود 25 كلمة تقريبًا.  
- تُكتب إجراءات التنفيذ في 4–5 نقاط مختصرة واضحة.  
- لا يُذكر عنوان الحقل داخل المحتوى.  
- يبدأ بالمضمون مباشرة دون تمهيد.  
- صياغة دقيقة مترابطة تعكس أثرًا صحيًا تربويًا واضحًا.  

**الحقول المطلوبة:**  
1. الهدف التربوي  
2. نبذة مختصرة  
3. إجراءات التنفيذ (4–5 نقاط)  
4. الاستراتيجيات المستخدمة  
5. نقاط القوة  
6. نقاط التحسين  
7. التوصيات  
**الحقول المطلوبة:**
1. الهدف التربوي
2. نبذة مختصرة
3. إجراءات التنفيذ
4. الاستراتيجيات المستخدمة
5. نقاط القوة
6. نقاط التحسين
7. التوصيات

يرجى تقديم الإجابة باللغة العربية الفصحى، وتنظيمها بحيث يكون كل حقل في سطر منفصل يبدأ برقمه فقط دون ذكر العنوان."""