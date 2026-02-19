# health_guide_prompt_updated.py
# -*- coding: utf-8 -*-

# قائمة المعايير مع النسب المئوية (weight)
TEACHER_CRITERIA = [
    {"id": "tc1", "name": "أداء الواجبات الوظيفية", "weight": 10, "order": 1},
    {"id": "tc2", "name": "التفاعل مع المجتمع المهني", "weight": 10, "order": 2},
    {"id": "tc3", "name": "التفاعل مع أولياء الأمور", "weight": 10, "order": 3},
    {"id": "tc4", "name": "التنويع في استراتيجيات التدريس", "weight": 5, "order": 4},
    {"id": "tc5", "name": "تحسين نتائج المتعلمين", "weight": 5, "order": 5},
    {"id": "tc6", "name": "إعداد وتنفيذ خطة التعلم", "weight": 5, "order": 6},
    {"id": "tc7", "name": "توظيف تقنيات ووسائل التعلم المناسبة", "weight": 5, "order": 7},
    {"id": "tc8", "name": "تهيئة بيئة تعليمية", "weight": 5, "order": 8},
    {"id": "tc9", "name": "تحليل نتائج المتعلمين وتشخيص مستوياتهم", "weight": 5, "order": 9},
    {"id": "tc10", "name": "تنوع أساليب التقويم", "weight": 5, "order": 10},
    {"id": "tc11", "name": "تنفيذ الخطة المشتركة للبرامج الصحية المدرسية", "weight": 15, "order": 11},
    {"id": "tc12", "name": "حصر الحالات الصحية للمتعلمين", "weight": 5, "order": 12},
    {"id": "tc13", "name": "تهيئة البيئة الصحية المدرسية", "weight": 10, "order": 13},
]

# التصنيفات الفرعية (مرتبطة بمعاييرها)
TEACHER_SUBCATEGORIES = [
    # tc1 - أداء الواجبات الوظيفية
    {"id": "tc1_s1", "criterion_id": "tc1", "name": "تطبيق الأنظمة وقواعد السلوك الوظيفية وأخلاقيات بيئة التعلم", "order": 1},
    {"id": "tc1_s2", "criterion_id": "tc1", "name": "حماية البيانات والمعلومات التي تتعلق بالعمل أو الأنشطة المهنية من الوصول غير المصرح به", "order": 2},
    {"id": "tc1_s3", "criterion_id": "tc1", "name": "التعاون مع المؤسسات الحكومية في المبادرات الوطنية", "order": 3},
    {"id": "tc1_s4", "criterion_id": "tc1", "name": "تنظيم أنشطة توعوية حول أهمية الانتماء الوطني", "order": 4},
    {"id": "tc1_s5", "criterion_id": "tc1", "name": "الامتثال للقوانين واللوائح وسياسات وإجراءات العمل", "order": 5},

    # tc2 - التفاعل مع المجتمع المهني
    {"id": "tc2_s1", "criterion_id": "tc2", "name": "حضور المؤتمرات والندوات التعليمية", "order": 1},
    {"id": "tc2_s2", "criterion_id": "tc2", "name": "المشاركة في ورش العمل التدريبية لتحسين المهارات التعليمية", "order": 2},
    {"id": "tc2_s3", "criterion_id": "tc2", "name": "الالتحاق ببرامج تدريبية لتعلم أساليب تدريس حديثة", "order": 3},
    {"id": "tc2_s4", "criterion_id": "tc2", "name": "الحصول على شهادات مهنية معتمدة في مجال التعليم", "order": 4},
    {"id": "tc2_s5", "criterion_id": "tc2", "name": "إطلاق مبادرات تعليمية لتحسين جودة التعليم", "order": 5},
    {"id": "tc2_s6", "criterion_id": "tc2", "name": "تقديم استشارات تربوية للمعلمين الجدد", "order": 6},
    {"id": "tc2_s7", "criterion_id": "tc2", "name": "تبادل الخبرات مع المعلمين في نفس التخصص أو تخصصات أخرى", "order": 7},
    {"id": "tc2_s8", "criterion_id": "tc2", "name": "التفكير الذاتي لتحسين الممارسات وبناء بيئة تعليمية تعزز التعلم المستمر", "order": 8},

    # tc3 - التفاعل مع أولياء الأمور
    {"id": "tc3_s1", "criterion_id": "tc3", "name": "تنظيم اجتماعات دورية مع أولياء الأمور لمناقشة تقدم الطلاب", "order": 1},
    {"id": "tc3_s2", "criterion_id": "tc3", "name": "إرسال تقارير منتظمة عن أداء الطلاب أكاديمياً وسلوكياً", "order": 2},
    {"id": "tc3_s3", "criterion_id": "tc3", "name": "استخدام وسائل التواصل الحديثة لإبقاء أولياء الأمور على اطلاع", "order": 3},
    {"id": "tc3_s4", "criterion_id": "tc3", "name": "الاستجابة والاستماع لملاحظات ومخاوف أولياء الأمور والعمل بشكل تعاوني لمعالجتها", "order": 4},
    {"id": "tc3_s5", "criterion_id": "tc3", "name": "تشجيع أولياء الأمور على المشاركة في العملية التعليمية", "order": 5},

    # tc4 - التنويع في استراتيجيات التدريس
    {"id": "tc4_s1", "criterion_id": "tc4", "name": "استخدام التعلم النشط مثل المناقشات الجماعية والعروض التقديمية", "order": 1},
    {"id": "tc4_s2", "criterion_id": "tc4", "name": "تطبيق التعلم القائم على المشاريع لتعزيز الإبداع وحل المشكلات", "order": 2},
    {"id": "tc4_s3", "criterion_id": "tc4", "name": "استخدام الوسائل البصرية والسمعية مثل الفيديوهات والصور", "order": 3},
    {"id": "tc4_s4", "criterion_id": "tc4", "name": "تخصيص أنشطة تعليمية تناسب أنماط التعلم المختلفة (بصري - سمعي - حركي)", "order": 4},

    # tc5 - تحسين نتائج المتعلمين
    {"id": "tc5_s1", "criterion_id": "tc5", "name": "تحديد أهداف ومعايير واضحة ليعرف المتعلمون ما يتوقع منهم تحقيقه", "order": 1},
    {"id": "tc5_s2", "criterion_id": "tc5", "name": "تقديم إفادة سريعة ومحددة فور ملاحظة الأداء مع التركيز على الإيجابيات وتقديم اقتراحات بناءة للتحسين", "order": 2},
    {"id": "tc5_s3", "criterion_id": "tc5", "name": "تكييف الإفادة وفق الاحتياجات الفردية", "order": 3},
    {"id": "tc5_s4", "criterion_id": "tc5", "name": "تعزيز الثقة وتشجيع التطور من خلال تقديم ملاحظات تشجيعية وفرص لتحسين الأداء", "order": 4},
    {"id": "tc5_s5", "criterion_id": "tc5", "name": "استخدام التكنولوجيا لتقديم الإفادة بطرق مبتكرة مثل البريد الإلكتروني ومنصات التعلم", "order": 5},

    # tc6 - إعداد وتنفيذ خطة التعلم
    {"id": "tc6_s1", "criterion_id": "tc6", "name": "وضع أهداف تعليمية واضحة وقابلة للقياس", "order": 1},
    {"id": "tc6_s2", "criterion_id": "tc6", "name": "تصميم خطة دراسية تتوافق مع المنهج الدراسي واحتياجات الطلاب", "order": 2},
    {"id": "tc6_s3", "criterion_id": "tc6", "name": "مراجعة الخطط بشكل دوري وتعديلها بناءً على نتائج الطلاب", "order": 3},
    {"id": "tc6_s4", "criterion_id": "tc6", "name": "مشاركة الخطط مع الزملاء للحصول على ملاحظات وتحسينها", "order": 4},
    {"id": "tc6_s5", "criterion_id": "tc6", "name": "تفهم الخصائص النفسية للمرحلة العمرية التي يقوم بتدريسها", "order": 5},

    # tc7 - توظيف تقنيات ووسائل التعلم المناسبة
    {"id": "tc7_s1", "criterion_id": "tc7", "name": "استخدام السبورات الذكية والأجهزة اللوحية في التدريس", "order": 1},
    {"id": "tc7_s2", "criterion_id": "tc7", "name": "تطبيق برامج التعلم الإلكتروني مثل منصات التعليم عن بعد", "order": 2},
    {"id": "tc7_s3", "criterion_id": "tc7", "name": "تشجيع الطلاب على استخدام التطبيقات التعليمية لتعزيز التعلم الذاتي", "order": 3},
    {"id": "tc7_s4", "criterion_id": "tc7", "name": "تنظيم ورش عمل حول استخدام التكنولوجيا في التعليم", "order": 4},

    # tc8 - تهيئة بيئة تعليمية
    {"id": "tc8_s1", "criterion_id": "tc8", "name": "تزيين الفصل بوسائل تعليمية جذابة", "order": 1},
    {"id": "tc8_s2", "criterion_id": "tc8", "name": "تنظيم الفصل بشكل يسهل الحركة والتفاعل", "order": 2},
    {"id": "tc8_s3", "criterion_id": "tc8", "name": "توفير الأدوات والموارد التعليمية اللازمة", "order": 3},
    {"id": "tc8_s4", "criterion_id": "tc8", "name": "توفير بيئة تعليمية آمنة وخالية من الأخطار المادية وتحقق الأمان النفسي", "order": 4},
    {"id": "tc8_s5", "criterion_id": "tc8", "name": "توفير بيئة تعليمية تمكن المتعلمين من التعبير عن أنفسهم ومشاركة أفكارهم مع أقرانهم", "order": 5},
    {"id": "tc8_s6", "criterion_id": "tc8", "name": "إثارة دافعية المتعلمين من خلال التنوع في أساليب التعلم", "order": 6},

    # tc9 - تحليل نتائج المتعلمين وتشخيص مستوياتهم
    {"id": "tc9_s1", "criterion_id": "tc9", "name": "استخدام اختبارات تقييمية دورية لقياس تقدم الطلاب", "order": 1},
    {"id": "tc9_s2", "criterion_id": "tc9", "name": "تحليل النتائج لتحديد نقاط القوة والضعف مع إشراك المتعلمين في فهم نتائجهم وتقديم ملاحظات تدعم التطور المستمر", "order": 2},
    {"id": "tc9_s3", "criterion_id": "tc9", "name": "توفير تغذية راجعة فردية للطلاب", "order": 3},
    {"id": "tc9_s4", "criterion_id": "tc9", "name": "تطبيق خطط علاجية للطلاب الذين يحتاجون إلى دعم", "order": 4},
    {"id": "tc9_s5", "criterion_id": "tc9", "name": "قياس التطبيق العملي للمعرفة عبر مواقف ومشاريع حقيقية", "order": 5},

    # tc10 - تنوع أساليب التقويم
    {"id": "tc10_s1", "criterion_id": "tc10", "name": "استخدام الاختبارات الكتابية والشفوية", "order": 1},
    {"id": "tc10_s2", "criterion_id": "tc10", "name": "تطبيق التقييم العملي من خلال المشاريع والعروض", "order": 2},
    {"id": "tc10_s3", "criterion_id": "tc10", "name": "استخدام التقييم التكويني لتتبع تقدم الطلاب", "order": 3},
    {"id": "tc10_s4", "criterion_id": "tc10", "name": "استخدام التقويم القبلي للوقوف على مدى استعداد المتعلمين وتشخيص امتلاكهم للمهارات والخبرات الأساسية السابقة", "order": 4},
    {"id": "tc10_s5", "criterion_id": "tc10", "name": "تطبيق التقويم الختامي لمعرفة مدى تحقق أهداف العملية التعليمية وقياس تقدم وإصدار أحكام عن مستويات الطلبة", "order": 5},

    # tc11 - تنفيذ الخطة المشتركة للبرامج الصحية المدرسية
    {"id": "tc11_s1", "criterion_id": "tc11", "name": "تنفيذ الخطة المشتركة للبرامج الصحية المدرسية", "order": 1},

    # tc12 - حصر الحالات الصحية للمتعلمين
    {"id": "tc12_s1", "criterion_id": "tc12", "name": "حصر الحالات الصحية للمتعلمين", "order": 1},

    # tc13 - تهيئة البيئة الصحية المدرسية
    {"id": "tc13_s1", "criterion_id": "tc13", "name": "تهيئة البيئة الصحية المدرسية", "order": 1},
]

# قائمة التقارير (10 لكل تصنيف فرعي)
TEACHER_REPORTS = [
    # tc1_s1
    {"id": "tc1_s1_r01", "subcategory_id": "tc1_s1", "name": "تقرير عن تطبيق لائحة السلوك الوظيفي في المدرسة", "order": 1},
    {"id": "tc1_s1_r02", "subcategory_id": "tc1_s1", "name": "سجل متابعة التزام المعلمين بأخلاقيات المهنة", "order": 2},
    {"id": "tc1_s1_r03", "subcategory_id": "tc1_s1", "name": "خطة تعزيز قيم النزاهة والشفافية لدى الكادر التعليمي", "order": 3},
    {"id": "tc1_s1_r04", "subcategory_id": "tc1_s1", "name": "إحصائية حالات المخالفات السلوكية والإجراءات المتخذة", "order": 4},
    {"id": "tc1_s1_r05", "subcategory_id": "tc1_s1", "name": "تقييم مدى الالتزام بالأنظمة خلال العام الدراسي", "order": 5},
    {"id": "tc1_s1_r06", "subcategory_id": "tc1_s1", "name": "توعية الموظفين الجدد بقواعد السلوك الوظيفي", "order": 6},
    {"id": "tc1_s1_r07", "subcategory_id": "tc1_s1", "name": "تنسيق مع إدارة المدرسة لتطوير دليل السلوك", "order": 7},
    {"id": "tc1_s1_r08", "subcategory_id": "tc1_s1", "name": "تحسين آليات الإبلاغ عن المخالفات", "order": 8},
    {"id": "tc1_s1_r09", "subcategory_id": "tc1_s1", "name": "متابعة تنفيذ برنامج تعزيز القيم المهنية", "order": 9},
    {"id": "tc1_s1_r10", "subcategory_id": "tc1_s1", "name": "إنجازات وحدة السلوك الوظيفي خلال العام", "order": 10},

    # tc1_s2
    {"id": "tc1_s2_r01", "subcategory_id": "tc1_s2", "name": "تقرير عن حماية بيانات الطلاب في نظام نور", "order": 1},
    {"id": "tc1_s2_r02", "subcategory_id": "tc1_s2", "name": "سجل الصلاحيات الممنوحة للموظفين للوصول للمعلومات", "order": 2},
    {"id": "tc1_s2_r03", "subcategory_id": "tc1_s2", "name": "خطة تأمين البيانات والمستندات الإلكترونية", "order": 3},
    {"id": "tc1_s2_r04", "subcategory_id": "tc1_s2", "name": "إحصائية محاولات الاختراق والإجراءات الوقائية", "order": 4},
    {"id": "tc1_s2_r05", "subcategory_id": "tc1_s2", "name": "تقييم وعي الموظفين بسرية المعلومات", "order": 5},
    {"id": "tc1_s2_r06", "subcategory_id": "tc1_s2", "name": "توعية العاملين بسياسات حماية البيانات", "order": 6},
    {"id": "tc1_s2_r07", "subcategory_id": "tc1_s2", "name": "تنسيق مع قسم تقنية المعلومات لتعزيز الحماية", "order": 7},
    {"id": "tc1_s2_r08", "subcategory_id": "tc1_s2", "name": "تحسين كلمات المرور وآليات الدخول", "order": 8},
    {"id": "tc1_s2_r09", "subcategory_id": "tc1_s2", "name": "متابعة الالتزام بسياسة الخصوصية", "order": 9},
    {"id": "tc1_s2_r10", "subcategory_id": "tc1_s2", "name": "إنجازات برنامج أمن المعلومات", "order": 10},

    # tc1_s3
    {"id": "tc1_s3_r01", "subcategory_id": "tc1_s3", "name": "تقرير عن المشاركة في اليوم الوطني", "order": 1},
    {"id": "tc1_s3_r02", "subcategory_id": "tc1_s3", "name": "سجل المبادرات الوطنية المنفذة بالمدرسة", "order": 2},
    {"id": "tc1_s3_r03", "subcategory_id": "tc1_s3", "name": "خطة التعاون مع المؤسسات الحكومية في الفعاليات", "order": 3},
    {"id": "tc1_s3_r04", "subcategory_id": "tc1_s3", "name": "إحصائية عدد المشاركات في المبادرات الوطنية", "order": 4},
    {"id": "tc1_s3_r05", "subcategory_id": "tc1_s3", "name": "تقييم أثر المشاركة في تعزيز الانتماء", "order": 5},
    {"id": "tc1_s3_r06", "subcategory_id": "tc1_s3", "name": "توعية الطلاب بأهمية العمل التطوعي", "order": 6},
    {"id": "tc1_s3_r07", "subcategory_id": "tc1_s3", "name": "تنسيق مع الجهات الحكومية لتنظيم الزيارات", "order": 7},
    {"id": "tc1_s3_r08", "subcategory_id": "tc1_s3", "name": "تحسين جودة المشاركات الوطنية", "order": 8},
    {"id": "tc1_s3_r09", "subcategory_id": "tc1_s3", "name": "متابعة تنفيذ برامج الشراكة المجتمعية", "order": 9},
    {"id": "tc1_s3_r10", "subcategory_id": "tc1_s3", "name": "إنجازات التعاون مع المؤسسات الحكومية", "order": 10},

    # tc1_s4
    {"id": "tc1_s4_r01", "subcategory_id": "tc1_s4", "name": "تقرير عن فعاليات أسبوع الانتماء الوطني", "order": 1},
    {"id": "tc1_s4_r02", "subcategory_id": "tc1_s4", "name": "سجل الأنشطة المنفذة لتعزيز المواطنة", "order": 2},
    {"id": "tc1_s4_r03", "subcategory_id": "tc1_s4", "name": "خطة تنظيم مسابقات وطنية", "order": 3},
    {"id": "tc1_s4_r04", "subcategory_id": "tc1_s4", "name": "إحصائية عدد المستفيدين من الأنشطة", "order": 4},
    {"id": "tc1_s4_r05", "subcategory_id": "tc1_s4", "name": "تقييم أثر الأنشطة على قيم الانتماء", "order": 5},
    {"id": "tc1_s4_r06", "subcategory_id": "tc1_s4", "name": "توعية الطلاب بالرموز الوطنية", "order": 6},
    {"id": "tc1_s4_r07", "subcategory_id": "tc1_s4", "name": "تنسيق مع الإذاعة المدرسية لتعزيز الانتماء", "order": 7},
    {"id": "tc1_s4_r08", "subcategory_id": "tc1_s4", "name": "تحسين محتوى الأنشطة الوطنية", "order": 8},
    {"id": "tc1_s4_r09", "subcategory_id": "tc1_s4", "name": "متابعة مشاركة الطلاب في الفعاليات", "order": 9},
    {"id": "tc1_s4_r10", "subcategory_id": "tc1_s4", "name": "إنجازات برنامج تعزيز الانتماء الوطني", "order": 10},

    # tc1_s5
    {"id": "tc1_s5_r01", "subcategory_id": "tc1_s5", "name": "تقرير عن الامتثال للوائح العمل", "order": 1},
    {"id": "tc1_s5_r02", "subcategory_id": "tc1_s5", "name": "سجل متابعة تطبيق السياسات المدرسية", "order": 2},
    {"id": "tc1_s5_r03", "subcategory_id": "tc1_s5", "name": "خطة نشر الوعي باللوائح الداخلية", "order": 3},
    {"id": "tc1_s5_r04", "subcategory_id": "tc1_s5", "name": "إحصائية حالات عدم الامتثال والإجراءات", "order": 4},
    {"id": "tc1_s5_r05", "subcategory_id": "tc1_s5", "name": "تقييم مدى تطبيق القوانين المحلية", "order": 5},
    {"id": "tc1_s5_r06", "subcategory_id": "tc1_s5", "name": "توعية الموظفين بالأنظمة المالية والإدارية", "order": 6},
    {"id": "tc1_s5_r07", "subcategory_id": "tc1_s5", "name": "تنسيق مع الإدارة لمراجعة السياسات", "order": 7},
    {"id": "tc1_s5_r08", "subcategory_id": "tc1_s5", "name": "تحسين آليات الرقابة الداخلية", "order": 8},
    {"id": "tc1_s5_r09", "subcategory_id": "tc1_s5", "name": "متابعة تحديث الوثائق القانونية", "order": 9},
    {"id": "tc1_s5_r10", "subcategory_id": "tc1_s5", "name": "إنجازات برنامج الامتثال", "order": 10},

    # tc2_s1
    {"id": "tc2_s1_r01", "subcategory_id": "tc2_s1", "name": "تقرير عن حضور المؤتمر التربوي السنوي", "order": 1},
    {"id": "tc2_s1_r02", "subcategory_id": "tc2_s1", "name": "سجل الندوات التعليمية المنعقدة", "order": 2},
    {"id": "tc2_s1_r03", "subcategory_id": "tc2_s1", "name": "خطة المشاركة في الفعاليات المهنية", "order": 3},
    {"id": "tc2_s1_r04", "subcategory_id": "tc2_s1", "name": "إحصائية عدد المؤتمرات التي حضرها المعلمون", "order": 4},
    {"id": "tc2_s1_r05", "subcategory_id": "tc2_s1", "name": "تقييم الاستفادة من المؤتمرات", "order": 5},
    {"id": "tc2_s1_r06", "subcategory_id": "tc2_s1", "name": "توعية المعلمين بأهمية التطوير المهني", "order": 6},
    {"id": "tc2_s1_r07", "subcategory_id": "tc2_s1", "name": "تنسيق مع الجهات المنظمة للمؤتمرات", "order": 7},
    {"id": "tc2_s1_r08", "subcategory_id": "tc2_s1", "name": "تحسين فرص المشاركة للجميع", "order": 8},
    {"id": "tc2_s1_r09", "subcategory_id": "tc2_s1", "name": "متابعة تطبيق ما تم تعلمه", "order": 9},
    {"id": "tc2_s1_r10", "subcategory_id": "tc2_s1", "name": "إنجازات المشاركة في المؤتمرات", "order": 10},

    # tc2_s2
    {"id": "tc2_s2_r01", "subcategory_id": "tc2_s2", "name": "تقرير عن ورش العمل التدريبية المنفذة", "order": 1},
    {"id": "tc2_s2_r02", "subcategory_id": "tc2_s2", "name": "سجل المشاركين في ورش التطوير", "order": 2},
    {"id": "tc2_s2_r03", "subcategory_id": "tc2_s2", "name": "خطة التدريب السنوية للمعلمين", "order": 3},
    {"id": "tc2_s2_r04", "subcategory_id": "tc2_s2", "name": "إحصائية عدد ساعات التدريب لكل معلم", "order": 4},
    {"id": "tc2_s2_r05", "subcategory_id": "tc2_s2", "name": "تقييم فعالية ورش العمل", "order": 5},
    {"id": "tc2_s2_r06", "subcategory_id": "tc2_s2", "name": "توعية المعلمين ببرامج التدريب المتاحة", "order": 6},
    {"id": "tc2_s2_r07", "subcategory_id": "tc2_s2", "name": "تنسيق مع مدربين خارجيين", "order": 7},
    {"id": "tc2_s2_r08", "subcategory_id": "tc2_s2", "name": "تحسين جودة المواد التدريبية", "order": 8},
    {"id": "tc2_s2_r09", "subcategory_id": "tc2_s2", "name": "متابعة أثر التدريب على الأداء", "order": 9},
    {"id": "tc2_s2_r10", "subcategory_id": "tc2_s2", "name": "إنجازات برنامج التدريب", "order": 10},

    # tc2_s3
    {"id": "tc2_s3_r01", "subcategory_id": "tc2_s3", "name": "تقرير عن الالتحاق ببرامج أساليب التدريس الحديثة", "order": 1},
    {"id": "tc2_s3_r02", "subcategory_id": "tc2_s3", "name": "سجل الدورات المتخصصة في استراتيجيات التعليم", "order": 2},
    {"id": "tc2_s3_r03", "subcategory_id": "tc2_s3", "name": "خطة تطوير مهارات التدريس", "order": 3},
    {"id": "tc2_s3_r04", "subcategory_id": "tc2_s3", "name": "إحصائية عدد المعلمين الملتحقين ببرامج جديدة", "order": 4},
    {"id": "tc2_s3_r05", "subcategory_id": "tc2_s3", "name": "تقييم مدى اكتساب مهارات تدريسية حديثة", "order": 5},
    {"id": "tc2_s3_r06", "subcategory_id": "tc2_s3", "name": "توعية المعلمين بالاتجاهات الحديثة", "order": 6},
    {"id": "tc2_s3_r07", "subcategory_id": "tc2_s3", "name": "تنسيق مع الجامعات لتقديم برامج", "order": 7},
    {"id": "tc2_s3_r08", "subcategory_id": "tc2_s3", "name": "تحسين اختيار البرامج المناسبة", "order": 8},
    {"id": "tc2_s3_r09", "subcategory_id": "tc2_s3", "name": "متابعة تطبيق الأساليب الجديدة", "order": 9},
    {"id": "tc2_s3_r10", "subcategory_id": "tc2_s3", "name": "إنجازات برنامج التطوير المهني", "order": 10},

    # tc2_s4
    {"id": "tc2_s4_r01", "subcategory_id": "tc2_s4", "name": "تقرير عن الحصول على شهادات مهنية", "order": 1},
    {"id": "tc2_s4_r02", "subcategory_id": "tc2_s4", "name": "سجل الشهادات المعتمدة للمعلمين", "order": 2},
    {"id": "tc2_s4_r03", "subcategory_id": "tc2_s4", "name": "خطة تحفيز المعلمين للحصول على شهادات", "order": 3},
    {"id": "tc2_s4_r04", "subcategory_id": "tc2_s4", "name": "إحصائية عدد الشهادات التي تم الحصول عليها", "order": 4},
    {"id": "tc2_s4_r05", "subcategory_id": "tc2_s4", "name": "تقييم أثر الشهادات على جودة التعليم", "order": 5},
    {"id": "tc2_s4_r06", "subcategory_id": "tc2_s4", "name": "توعية المعلمين بأهمية الشهادات", "order": 6},
    {"id": "tc2_s4_r07", "subcategory_id": "tc2_s4", "name": "تنسيق مع هيئات الاعتماد المهني", "order": 7},
    {"id": "tc2_s4_r08", "subcategory_id": "tc2_s4", "name": "تحسين الدعم المالي للمعلمين", "order": 8},
    {"id": "tc2_s4_r09", "subcategory_id": "tc2_s4", "name": "متابعة تجديد الشهادات", "order": 9},
    {"id": "tc2_s4_r10", "subcategory_id": "tc2_s4", "name": "إنجازات برنامج الشهادات المهنية", "order": 10},

    # tc2_s5
    {"id": "tc2_s5_r01", "subcategory_id": "tc2_s5", "name": "تقرير عن إطلاق مبادرات تعليمية", "order": 1},
    {"id": "tc2_s5_r02", "subcategory_id": "tc2_s5", "name": "سجل المبادرات التطويرية", "order": 2},
    {"id": "tc2_s5_r03", "subcategory_id": "tc2_s5", "name": "خطة تحفيز الإبداع لدى المعلمين", "order": 3},
    {"id": "tc2_s5_r04", "subcategory_id": "tc2_s5", "name": "إحصائية عدد المبادرات المنفذة", "order": 4},
    {"id": "tc2_s5_r05", "subcategory_id": "tc2_s5", "name": "تقييم أثر المبادرات على التعلم", "order": 5},
    {"id": "tc2_s5_r06", "subcategory_id": "tc2_s5", "name": "توعية المعلمين بأهمية المبادرات", "order": 6},
    {"id": "tc2_s5_r07", "subcategory_id": "tc2_s5", "name": "تنسيق مع جهات داعمة للمبادرات", "order": 7},
    {"id": "tc2_s5_r08", "subcategory_id": "tc2_s5", "name": "تحسين آليات تقييم المبادرات", "order": 8},
    {"id": "tc2_s5_r09", "subcategory_id": "tc2_s5", "name": "متابعة استدامة المبادرات", "order": 9},
    {"id": "tc2_s5_r10", "subcategory_id": "tc2_s5", "name": "إنجازات المبادرات التعليمية", "order": 10},

    # tc2_s6
    {"id": "tc2_s6_r01", "subcategory_id": "tc2_s6", "name": "تقرير عن تقديم استشارات للمعلمين الجدد", "order": 1},
    {"id": "tc2_s6_r02", "subcategory_id": "tc2_s6", "name": "سجل جلسات الإرشاد التربوي", "order": 2},
    {"id": "tc2_s6_r03", "subcategory_id": "tc2_s6", "name": "خطة دعم المعلمين المستجدين", "order": 3},
    {"id": "tc2_s6_r04", "subcategory_id": "tc2_s6", "name": "إحصائية عدد المستفيدين من الاستشارات", "order": 4},
    {"id": "tc2_s6_r05", "subcategory_id": "tc2_s6", "name": "تقييم فعالية برنامج الإرشاد", "order": 5},
    {"id": "tc2_s6_r06", "subcategory_id": "tc2_s6", "name": "توعية المعلمين بأهمية الإرشاد", "order": 6},
    {"id": "tc2_s6_r07", "subcategory_id": "tc2_s6", "name": "تنسيق مع خبراء تربويين", "order": 7},
    {"id": "tc2_s6_r08", "subcategory_id": "tc2_s6", "name": "تحسين جودة الاستشارات", "order": 8},
    {"id": "tc2_s6_r09", "subcategory_id": "tc2_s6", "name": "متابعة تطور أداء المعلمين الجدد", "order": 9},
    {"id": "tc2_s6_r10", "subcategory_id": "tc2_s6", "name": "إنجازات برنامج الإرشاد", "order": 10},

    # tc2_s7
    {"id": "tc2_s7_r01", "subcategory_id": "tc2_s7", "name": "تقرير عن تبادل الخبرات بين المعلمين", "order": 1},
    {"id": "tc2_s7_r02", "subcategory_id": "tc2_s7", "name": "سجل اجتماعات التخصص", "order": 2},
    {"id": "tc2_s7_r03", "subcategory_id": "tc2_s7", "name": "خطة تنظيم ورش تبادل الخبرات", "order": 3},
    {"id": "tc2_s7_r04", "subcategory_id": "tc2_s7", "name": "إحصائية عدد اللقاءات التبادلية", "order": 4},
    {"id": "tc2_s7_r05", "subcategory_id": "tc2_s7", "name": "تقييم أثر التبادل على الممارسات", "order": 5},
    {"id": "tc2_s7_r06", "subcategory_id": "tc2_s7", "name": "توعية المعلمين بأهمية التعاون", "order": 6},
    {"id": "tc2_s7_r07", "subcategory_id": "tc2_s7", "name": "تنسيق مع مدارس أخرى للتبادل", "order": 7},
    {"id": "tc2_s7_r08", "subcategory_id": "tc2_s7", "name": "تحسين قنوات التواصل المهني", "order": 8},
    {"id": "tc2_s7_r09", "subcategory_id": "tc2_s7", "name": "متابعة تطبيق الأفكار المتبادلة", "order": 9},
    {"id": "tc2_s7_r10", "subcategory_id": "tc2_s7", "name": "إنجازات برنامج تبادل الخبرات", "order": 10},

    # tc2_s8
    {"id": "tc2_s8_r01", "subcategory_id": "tc2_s8", "name": "تقرير عن ممارسات التفكير الذاتي", "order": 1},
    {"id": "tc2_s8_r02", "subcategory_id": "tc2_s8", "name": "سجل التأمل الذاتي للمعلمين", "order": 2},
    {"id": "tc2_s8_r03", "subcategory_id": "tc2_s8", "name": "خطة تعزيز ثقافة التفكير الذاتي", "order": 3},
    {"id": "tc2_s8_r04", "subcategory_id": "tc2_s8", "name": "إحصائية عدد المشاركين في برامج التأمل", "order": 4},
    {"id": "tc2_s8_r05", "subcategory_id": "tc2_s8", "name": "تقييم أثر التأمل على التطوير", "order": 5},
    {"id": "tc2_s8_r06", "subcategory_id": "tc2_s8", "name": "توعية المعلمين بأدوات التأمل", "order": 6},
    {"id": "tc2_s8_r07", "subcategory_id": "tc2_s8", "name": "تنسيق مع مشرفين لتوجيه التأمل", "order": 7},
    {"id": "tc2_s8_r08", "subcategory_id": "tc2_s8", "name": "تحسين استمارات التأمل", "order": 8},
    {"id": "tc2_s8_r09", "subcategory_id": "tc2_s8", "name": "متابعة خطط التطوير الشخصي", "order": 9},
    {"id": "tc2_s8_r10", "subcategory_id": "tc2_s8", "name": "إنجازات برنامج التفكير الذاتي", "order": 10},

    # tc3_s1
    {"id": "tc3_s1_r01", "subcategory_id": "tc3_s1", "name": "تقرير عن اجتماعات أولياء الأمور الدورية", "order": 1},
    {"id": "tc3_s1_r02", "subcategory_id": "tc3_s1", "name": "سجل حضور أولياء الأمور", "order": 2},
    {"id": "tc3_s1_r03", "subcategory_id": "tc3_s1", "name": "خطة تنظيم لقاءات مفتوحة مع الأسر", "order": 3},
    {"id": "tc3_s1_r04", "subcategory_id": "tc3_s1", "name": "إحصائية عدد الاجتماعات المنعقدة", "order": 4},
    {"id": "tc3_s1_r05", "subcategory_id": "tc3_s1", "name": "تقييم فعالية الاجتماعات في تحسين الأداء", "order": 5},
    {"id": "tc3_s1_r06", "subcategory_id": "tc3_s1", "name": "توعية أولياء الأمور بأهمية الحضور", "order": 6},
    {"id": "tc3_s1_r07", "subcategory_id": "tc3_s1", "name": "تنسيق مع المعلمين للتحضير للاجتماعات", "order": 7},
    {"id": "tc3_s1_r08", "subcategory_id": "tc3_s1", "name": "تحسين جدولة الاجتماعات", "order": 8},
    {"id": "tc3_s1_r09", "subcategory_id": "tc3_s1", "name": "متابعة توصيات الاجتماعات", "order": 9},
    {"id": "tc3_s1_r10", "subcategory_id": "tc3_s1", "name": "إنجازات برنامج التواصل مع الأسر", "order": 10},

    # tc3_s2
    {"id": "tc3_s2_r01", "subcategory_id": "tc3_s2", "name": "تقرير عن تقارير أداء الطلاب الشهرية", "order": 1},
    {"id": "tc3_s2_r02", "subcategory_id": "tc3_s2", "name": "سجل إرسال التقارير السلوكية", "order": 2},
    {"id": "tc3_s2_r03", "subcategory_id": "tc3_s2", "name": "خطة تطوير نظام التقارير", "order": 3},
    {"id": "tc3_s2_r04", "subcategory_id": "tc3_s2", "name": "إحصائية عدد التقارير المرسلة", "order": 4},
    {"id": "tc3_s2_r05", "subcategory_id": "tc3_s2", "name": "تقييم دقة التقارير ووضوحها", "order": 5},
    {"id": "tc3_s2_r06", "subcategory_id": "tc3_s2", "name": "توعية أولياء الأمور بكيفية قراءة التقارير", "order": 6},
    {"id": "tc3_s2_r07", "subcategory_id": "tc3_s2", "name": "تنسيق مع المعلمين لتوحيد التقارير", "order": 7},
    {"id": "tc3_s2_r08", "subcategory_id": "tc3_s2", "name": "تحسين نموذج التقرير", "order": 8},
    {"id": "tc3_s2_r09", "subcategory_id": "tc3_s2", "name": "متابعة استجابة الأسر للتقارير", "order": 9},
    {"id": "tc3_s2_r10", "subcategory_id": "tc3_s2", "name": "إنجازات نظام التقارير", "order": 10},

    # tc3_s3
    {"id": "tc3_s3_r01", "subcategory_id": "tc3_s3", "name": "تقرير عن استخدام البريد الإلكتروني في التواصل", "order": 1},
    {"id": "tc3_s3_r02", "subcategory_id": "tc3_s3", "name": "سجل تفعيل التطبيقات التعليمية", "order": 2},
    {"id": "tc3_s3_r03", "subcategory_id": "tc3_s3", "name": "خطة تعزيز التواصل الإلكتروني", "order": 3},
    {"id": "tc3_s3_r04", "subcategory_id": "tc3_s3", "name": "إحصائية عدد أولياء الأمور المستخدمين للتطبيقات", "order": 4},
    {"id": "tc3_s3_r05", "subcategory_id": "tc3_s3", "name": "تقييم فاعلية وسائل التواصل", "order": 5},
    {"id": "tc3_s3_r06", "subcategory_id": "tc3_s3", "name": "توعية أولياء الأمور بكيفية استخدام التطبيقات", "order": 6},
    {"id": "tc3_s3_r07", "subcategory_id": "tc3_s3", "name": "تنسيق مع شركات التقنية", "order": 7},
    {"id": "tc3_s3_r08", "subcategory_id": "tc3_s3", "name": "تحسين سهولة استخدام التطبيقات", "order": 8},
    {"id": "tc3_s3_r09", "subcategory_id": "tc3_s3", "name": "متابعة تفعيل الحسابات", "order": 9},
    {"id": "tc3_s3_r10", "subcategory_id": "tc3_s3", "name": "إنجازات التواصل الرقمي", "order": 10},

    # tc3_s4
    {"id": "tc3_s4_r01", "subcategory_id": "tc3_s4", "name": "تقرير عن الاستجابة لملاحظات أولياء الأمور", "order": 1},
    {"id": "tc3_s4_r02", "subcategory_id": "tc3_s4", "name": "سجل الشكاوى والمقترحات", "order": 2},
    {"id": "tc3_s4_r03", "subcategory_id": "tc3_s4", "name": "خطة تحسين آلية التعامل مع المخاوف", "order": 3},
    {"id": "tc3_s4_r04", "subcategory_id": "tc3_s4", "name": "إحصائية عدد الملاحظات الواردة", "order": 4},
    {"id": "tc3_s4_r05", "subcategory_id": "tc3_s4", "name": "تقييم سرعة الاستجابة", "order": 5},
    {"id": "tc3_s4_r06", "subcategory_id": "tc3_s4", "name": "توعية أولياء الأمور بقنوات التواصل", "order": 6},
    {"id": "tc3_s4_r07", "subcategory_id": "tc3_s4", "name": "تنسيق مع الإدارة لحل المشكلات", "order": 7},
    {"id": "tc3_s4_r08", "subcategory_id": "tc3_s4", "name": "تحسين جودة الردود", "order": 8},
    {"id": "tc3_s4_r09", "subcategory_id": "tc3_s4", "name": "متابعة تنفيذ الحلول", "order": 9},
    {"id": "tc3_s4_r10", "subcategory_id": "tc3_s4", "name": "إنجازات خدمة أولياء الأمور", "order": 10},

    # tc3_s5
    {"id": "tc3_s5_r01", "subcategory_id": "tc3_s5", "name": "تقرير عن مشاركة أولياء الأمور في الأنشطة", "order": 1},
    {"id": "tc3_s5_r02", "subcategory_id": "tc3_s5", "name": "سجل المتطوعين من الأسر", "order": 2},
    {"id": "tc3_s5_r03", "subcategory_id": "tc3_s5", "name": "خطة إشراك الأسر في العملية التعليمية", "order": 3},
    {"id": "tc3_s5_r04", "subcategory_id": "tc3_s5", "name": "إحصائية عدد المشاركات", "order": 4},
    {"id": "tc3_s5_r05", "subcategory_id": "tc3_s5", "name": "تقييم أثر المشاركة على الطلاب", "order": 5},
    {"id": "tc3_s5_r06", "subcategory_id": "tc3_s5", "name": "توعية أولياء الأمور بأهمية المشاركة", "order": 6},
    {"id": "tc3_s5_r07", "subcategory_id": "tc3_s5", "name": "تنسيق مع المعلمين لتحديد أدوار الأسر", "order": 7},
    {"id": "tc3_s5_r08", "subcategory_id": "tc3_s5", "name": "تحسين برامج التطوع", "order": 8},
    {"id": "tc3_s5_r09", "subcategory_id": "tc3_s5", "name": "متابعة استمرارية المشاركة", "order": 9},
    {"id": "tc3_s5_r10", "subcategory_id": "tc3_s5", "name": "إنجازات برنامج مشاركة الأسر", "order": 10},

    # tc4_s1
    {"id": "tc4_s1_r01", "subcategory_id": "tc4_s1", "name": "تقرير عن استخدام المناقشات الجماعية", "order": 1},
    {"id": "tc4_s1_r02", "subcategory_id": "tc4_s1", "name": "سجل العروض التقديمية للطلاب", "order": 2},
    {"id": "tc4_s1_r03", "subcategory_id": "tc4_s1", "name": "خطة تنويع استراتيجيات التعلم النشط", "order": 3},
    {"id": "tc4_s1_r04", "subcategory_id": "tc4_s1", "name": "إحصائية عدد الحصص التي طبق فيها التعلم النشط", "order": 4},
    {"id": "tc4_s1_r05", "subcategory_id": "tc4_s1", "name": "تقييم أثر المناقشات على التفكير الناقد", "order": 5},
    {"id": "tc4_s1_r06", "subcategory_id": "tc4_s1", "name": "توعية المعلمين بأساليب التعلم النشط", "order": 6},
    {"id": "tc4_s1_r07", "subcategory_id": "tc4_s1", "name": "تنسيق مع مشرفين لتطبيق الاستراتيجيات", "order": 7},
    {"id": "tc4_s1_r08", "subcategory_id": "tc4_s1", "name": "تحسين بيئة الصف للتعلم النشط", "order": 8},
    {"id": "tc4_s1_r09", "subcategory_id": "tc4_s1", "name": "متابعة تفاعل الطلاب", "order": 9},
    {"id": "tc4_s1_r10", "subcategory_id": "tc4_s1", "name": "إنجازات برنامج التعلم النشط", "order": 10},

    # tc4_s2
    {"id": "tc4_s2_r01", "subcategory_id": "tc4_s2", "name": "تقرير عن مشاريع الطلاب الإبداعية", "order": 1},
    {"id": "tc4_s2_r02", "subcategory_id": "tc4_s2", "name": "سجل المشاريع المنفذة", "order": 2},
    {"id": "tc4_s2_r03", "subcategory_id": "tc4_s2", "name": "خطة دمج التعلم القائم على المشاريع", "order": 3},
    {"id": "tc4_s2_r04", "subcategory_id": "tc4_s2", "name": "إحصائية عدد المشاريع المنجزة", "order": 4},
    {"id": "tc4_s2_r05", "subcategory_id": "tc4_s2", "name": "تقييم أثر المشاريع على حل المشكلات", "order": 5},
    {"id": "tc4_s2_r06", "subcategory_id": "tc4_s2", "name": "توعية الطلاب بأهمية المشاريع", "order": 6},
    {"id": "tc4_s2_r07", "subcategory_id": "tc4_s2", "name": "تنسيق مع جهات داعمة للمشاريع", "order": 7},
    {"id": "tc4_s2_r08", "subcategory_id": "tc4_s2", "name": "تحسين معايير تقييم المشاريع", "order": 8},
    {"id": "tc4_s2_r09", "subcategory_id": "tc4_s2", "name": "متابعة مراحل تنفيذ المشاريع", "order": 9},
    {"id": "tc4_s2_r10", "subcategory_id": "tc4_s2", "name": "إنجازات برنامج المشاريع", "order": 10},

    # tc4_s3
    {"id": "tc4_s3_r01", "subcategory_id": "tc4_s3", "name": "تقرير عن استخدام الفيديوهات التعليمية", "order": 1},
    {"id": "tc4_s3_r02", "subcategory_id": "tc4_s3", "name": "سجل الوسائل البصرية المستخدمة", "order": 2},
    {"id": "tc4_s3_r03", "subcategory_id": "tc4_s3", "name": "خطة تطوير المحتوى البصري", "order": 3},
    {"id": "tc4_s3_r04", "subcategory_id": "tc4_s3", "name": "إحصائية عدد الدروس المدعومة بالوسائط", "order": 4},
    {"id": "tc4_s3_r05", "subcategory_id": "tc4_s3", "name": "تقييم تأثير الوسائل على الفهم", "order": 5},
    {"id": "tc4_s3_r06", "subcategory_id": "tc4_s3", "name": "توعية المعلمين بمصادر الوسائط", "order": 6},
    {"id": "tc4_s3_r07", "subcategory_id": "tc4_s3", "name": "تنسيق مع مختبر الوسائط", "order": 7},
    {"id": "tc4_s3_r08", "subcategory_id": "tc4_s3", "name": "تحسين جودة الفيديوهات", "order": 8},
    {"id": "tc4_s3_r09", "subcategory_id": "tc4_s3", "name": "متابعة تفاعل الطلاب مع الوسائط", "order": 9},
    {"id": "tc4_s3_r10", "subcategory_id": "tc4_s3", "name": "إنجازات استخدام الوسائل", "order": 10},

    # tc4_s4
    {"id": "tc4_s4_r01", "subcategory_id": "tc4_s4", "name": "تقرير عن أنشطة تناسب المتعلمين بصرياً", "order": 1},
    {"id": "tc4_s4_r02", "subcategory_id": "tc4_s4", "name": "سجل الأنشطة الحركية", "order": 2},
    {"id": "tc4_s4_r03", "subcategory_id": "tc4_s4", "name": "خطة تخصيص التعليم حسب الأنماط", "order": 3},
    {"id": "tc4_s4_r04", "subcategory_id": "tc4_s4", "name": "إحصائية مدى مراعاة الفروق الفردية", "order": 4},
    {"id": "tc4_s4_r05", "subcategory_id": "tc4_s4", "name": "تقييم أثر التخصيص على التحصيل", "order": 5},
    {"id": "tc4_s4_r06", "subcategory_id": "tc4_s4", "name": "توعية المعلمين بأنماط التعلم", "order": 6},
    {"id": "tc4_s4_r07", "subcategory_id": "tc4_s4", "name": "تنسيق مع وحدة الموهوبين", "order": 7},
    {"id": "tc4_s4_r08", "subcategory_id": "tc4_s4", "name": "تحسين أدوات تشخيص الأنماط", "order": 8},
    {"id": "tc4_s4_r09", "subcategory_id": "tc4_s4", "name": "متابعة تكيف الطلاب", "order": 9},
    {"id": "tc4_s4_r10", "subcategory_id": "tc4_s4", "name": "إنجازات برنامج مراعاة الأنماط", "order": 10},

    # tc5_s1
    {"id": "tc5_s1_r01", "subcategory_id": "tc5_s1", "name": "تقرير عن تحديد الأهداف التعليمية", "order": 1},
    {"id": "tc5_s1_r02", "subcategory_id": "tc5_s1", "name": "سجل المعايير الواضحة لكل وحدة", "order": 2},
    {"id": "tc5_s1_r03", "subcategory_id": "tc5_s1", "name": "خطة إشراك الطلاب في وضع الأهداف", "order": 3},
    {"id": "tc5_s1_r04", "subcategory_id": "tc5_s1", "name": "إحصائية مدى فهم الطلاب للأهداف", "order": 4},
    {"id": "tc5_s1_r05", "subcategory_id": "tc5_s1", "name": "تقييم وضوح الأهداف في الخطط", "order": 5},
    {"id": "tc5_s1_r06", "subcategory_id": "tc5_s1", "name": "توعية الطلاب بأهمية الأهداف", "order": 6},
    {"id": "tc5_s1_r07", "subcategory_id": "tc5_s1", "name": "تنسيق مع مشرفين لمراجعة الأهداف", "order": 7},
    {"id": "tc5_s1_r08", "subcategory_id": "tc5_s1", "name": "تحسين صياغة الأهداف", "order": 8},
    {"id": "tc5_s1_r09", "subcategory_id": "tc5_s1", "name": "متابعة تحقيق الأهداف", "order": 9},
    {"id": "tc5_s1_r10", "subcategory_id": "tc5_s1", "name": "إنجازات وضوح الأهداف", "order": 10},

    # tc5_s2
    {"id": "tc5_s2_r01", "subcategory_id": "tc5_s2", "name": "تقرير عن تقديم تغذية راجعة فورية", "order": 1},
    {"id": "tc5_s2_r02", "subcategory_id": "tc5_s2", "name": "سجل التعليقات البناءة", "order": 2},
    {"id": "tc5_s2_r03", "subcategory_id": "tc5_s2", "name": "خطة تحسين جودة التغذية الراجعة", "order": 3},
    {"id": "tc5_s2_r04", "subcategory_id": "tc5_s2", "name": "إحصائية عدد مرات تقديم الإفادة", "order": 4},
    {"id": "tc5_s2_r05", "subcategory_id": "tc5_s2", "name": "تقييم أثر التغذية على التحسين", "order": 5},
    {"id": "tc5_s2_r06", "subcategory_id": "tc5_s2", "name": "توعية المعلمين بأهمية الإفادة", "order": 6},
    {"id": "tc5_s2_r07", "subcategory_id": "tc5_s2", "name": "تنسيق مع مختصين لتدريب على الإفادة", "order": 7},
    {"id": "tc5_s2_r08", "subcategory_id": "tc5_s2", "name": "تحسين سرعة التغذية", "order": 8},
    {"id": "tc5_s2_r09", "subcategory_id": "tc5_s2", "name": "متابعة تفاعل الطلاب مع الإفادة", "order": 9},
    {"id": "tc5_s2_r10", "subcategory_id": "tc5_s2", "name": "إنجازات التغذية الراجعة", "order": 10},

    # tc5_s3
    {"id": "tc5_s3_r01", "subcategory_id": "tc5_s3", "name": "تقرير عن تكييف التغذية حسب الاحتياجات", "order": 1},
    {"id": "tc5_s3_r02", "subcategory_id": "tc5_s3", "name": "سجل خطط الدعم الفردية", "order": 2},
    {"id": "tc5_s3_r03", "subcategory_id": "tc5_s3", "name": "خطة تخصيص التغذية للطلاب", "order": 3},
    {"id": "tc5_s3_r04", "subcategory_id": "tc5_s3", "name": "إحصائية عدد الطلاب المستفيدين من التكييف", "order": 4},
    {"id": "tc5_s3_r05", "subcategory_id": "tc5_s3", "name": "تقييم مناسبة التغذية للفرد", "order": 5},
    {"id": "tc5_s3_r06", "subcategory_id": "tc5_s3", "name": "توعية المعلمين بأساليب التكييف", "order": 6},
    {"id": "tc5_s3_r07", "subcategory_id": "tc5_s3", "name": "تنسيق مع وحدة التربية الخاصة", "order": 7},
    {"id": "tc5_s3_r08", "subcategory_id": "tc5_s3", "name": "تحسين أدوات التشخيص", "order": 8},
    {"id": "tc5_s3_r09", "subcategory_id": "tc5_s3", "name": "متابعة تقدم الطلاب", "order": 9},
    {"id": "tc5_s3_r10", "subcategory_id": "tc5_s3", "name": "إنجازات برنامج التكييف", "order": 10},

    # tc5_s4
    {"id": "tc5_s4_r01", "subcategory_id": "tc5_s4", "name": "تقرير عن تعزيز ثقة الطلاب", "order": 1},
    {"id": "tc5_s4_r02", "subcategory_id": "tc5_s4", "name": "سجل الملاحظات التشجيعية", "order": 2},
    {"id": "tc5_s4_r03", "subcategory_id": "tc5_s4", "name": "خطة تحفيز الطلاب", "order": 3},
    {"id": "tc5_s4_r04", "subcategory_id": "tc5_s4", "name": "إحصائية عدد فرص التحسين المقدمة", "order": 4},
    {"id": "tc5_s4_r05", "subcategory_id": "tc5_s4", "name": "تقييم أثر التشجيع على الدافعية", "order": 5},
    {"id": "tc5_s4_r06", "subcategory_id": "tc5_s4", "name": "توعية المعلمين بأساليب التحفيز", "order": 6},
    {"id": "tc5_s4_r07", "subcategory_id": "tc5_s4", "name": "تنسيق مع المرشد الطلابي", "order": 7},
    {"id": "tc5_s4_r08", "subcategory_id": "tc5_s4", "name": "تحسين برامج المكافآت", "order": 8},
    {"id": "tc5_s4_r09", "subcategory_id": "tc5_s4", "name": "متابعة تحسن الأداء", "order": 9},
    {"id": "tc5_s4_r10", "subcategory_id": "tc5_s4", "name": "إنجازات برنامج التحفيز", "order": 10},

    # tc5_s5
    {"id": "tc5_s5_r01", "subcategory_id": "tc5_s5", "name": "تقرير عن استخدام البريد الإلكتروني في الإفادة", "order": 1},
    {"id": "tc5_s5_r02", "subcategory_id": "tc5_s5", "name": "سجل التغذية عبر منصات التعلم", "order": 2},
    {"id": "tc5_s5_r03", "subcategory_id": "tc5_s5", "name": "خطة توظيف التكنولوجيا في التغذية", "order": 3},
    {"id": "tc5_s5_r04", "subcategory_id": "tc5_s5", "name": "إحصائية عدد التفاعلات الرقمية", "order": 4},
    {"id": "tc5_s5_r05", "subcategory_id": "tc5_s5", "name": "تقييم فاعلية الإفادة الإلكترونية", "order": 5},
    {"id": "tc5_s5_r06", "subcategory_id": "tc5_s5", "name": "توعية المعلمين بالأدوات الرقمية", "order": 6},
    {"id": "tc5_s5_r07", "subcategory_id": "tc5_s5", "name": "تنسيق مع قسم تقنية المعلومات", "order": 7},
    {"id": "tc5_s5_r08", "subcategory_id": "tc5_s5", "name": "تحسين واجهات المنصات", "order": 8},
    {"id": "tc5_s5_r09", "subcategory_id": "tc5_s5", "name": "متابعة تفاعل الطلاب", "order": 9},
    {"id": "tc5_s5_r10", "subcategory_id": "tc5_s5", "name": "إنجازات التغذية الرقمية", "order": 10},

    # tc6_s1
    {"id": "tc6_s1_r01", "subcategory_id": "tc6_s1", "name": "تقرير عن وضع أهداف تعليمية قابلة للقياس", "order": 1},
    {"id": "tc6_s1_r02", "subcategory_id": "tc6_s1", "name": "سجل الأهداف لكل مادة", "order": 2},
    {"id": "tc6_s1_r03", "subcategory_id": "tc6_s1", "name": "خطة مراجعة الأهداف", "order": 3},
    {"id": "tc6_s1_r04", "subcategory_id": "tc6_s1", "name": "إحصائية مدى تحقيق الأهداف", "order": 4},
    {"id": "tc6_s1_r05", "subcategory_id": "tc6_s1", "name": "تقييم دقة صياغة الأهداف", "order": 5},
    {"id": "tc6_s1_r06", "subcategory_id": "tc6_s1", "name": "توعية المعلمين بصياغة الأهداف", "order": 6},
    {"id": "tc6_s1_r07", "subcategory_id": "tc6_s1", "name": "تنسيق مع مشرفين لتحسين الأهداف", "order": 7},
    {"id": "tc6_s1_r08", "subcategory_id": "tc6_s1", "name": "تحسين ربط الأهداف بالمنهج", "order": 8},
    {"id": "tc6_s1_r09", "subcategory_id": "tc6_s1", "name": "متابعة تنفيذ الأهداف", "order": 9},
    {"id": "tc6_s1_r10", "subcategory_id": "tc6_s1", "name": "إنجازات وضوح الأهداف", "order": 10},

    # tc6_s2
    {"id": "tc6_s2_r01", "subcategory_id": "tc6_s2", "name": "تقرير عن تصميم خطة دراسية", "order": 1},
    {"id": "tc6_s2_r02", "subcategory_id": "tc6_s2", "name": "سجل الخطط الفصلية", "order": 2},
    {"id": "tc6_s2_r03", "subcategory_id": "tc6_s2", "name": "خطة تطوير الخطط الدراسية", "order": 3},
    {"id": "tc6_s2_r04", "subcategory_id": "tc6_s2", "name": "إحصائية عدد الخطط المحدثة", "order": 4},
    {"id": "tc6_s2_r05", "subcategory_id": "tc6_s2", "name": "تقييم ملاءمة الخطط لاحتياجات الطلاب", "order": 5},
    {"id": "tc6_s2_r06", "subcategory_id": "tc6_s2", "name": "توعية المعلمين بأهمية التخطيط", "order": 6},
    {"id": "tc6_s2_r07", "subcategory_id": "tc6_s2", "name": "تنسيق مع رؤساء الأقسام", "order": 7},
    {"id": "tc6_s2_r08", "subcategory_id": "tc6_s2", "name": "تحسين نموذج الخطة", "order": 8},
    {"id": "tc6_s2_r09", "subcategory_id": "tc6_s2", "name": "متابعة تنفيذ الخطط", "order": 9},
    {"id": "tc6_s2_r10", "subcategory_id": "tc6_s2", "name": "إنجازات التخطيط الدراسي", "order": 10},

    # tc6_s3
    {"id": "tc6_s3_r01", "subcategory_id": "tc6_s3", "name": "تقرير عن مراجعة الخطط بشكل دوري", "order": 1},
    {"id": "tc6_s3_r02", "subcategory_id": "tc6_s3", "name": "سجل تعديلات الخطط", "order": 2},
    {"id": "tc6_s3_r03", "subcategory_id": "tc6_s3", "name": "خطة تحسين الخطط بناءً على النتائج", "order": 3},
    {"id": "tc6_s3_r04", "subcategory_id": "tc6_s3", "name": "إحصائية عدد التعديلات", "order": 4},
    {"id": "tc6_s3_r05", "subcategory_id": "tc6_s3", "name": "تقييم أثر التعديل على التحصيل", "order": 5},
    {"id": "tc6_s3_r06", "subcategory_id": "tc6_s3", "name": "توعية المعلمين بأهمية المراجعة", "order": 6},
    {"id": "tc6_s3_r07", "subcategory_id": "tc6_s3", "name": "تنسيق مع مشرفين لمراجعة الخطط", "order": 7},
    {"id": "tc6_s3_r08", "subcategory_id": "tc6_s3", "name": "تحسين آلية المراجعة", "order": 8},
    {"id": "tc6_s3_r09", "subcategory_id": "tc6_s3", "name": "متابعة تطبيق التعديلات", "order": 9},
    {"id": "tc6_s3_r10", "subcategory_id": "tc6_s3", "name": "إنجازات مراجعة الخطط", "order": 10},

    # tc6_s4
    {"id": "tc6_s4_r01", "subcategory_id": "tc6_s4", "name": "تقرير عن مشاركة الخطط مع الزملاء", "order": 1},
    {"id": "tc6_s4_r02", "subcategory_id": "tc6_s4", "name": "سجل ملاحظات الزملاء", "order": 2},
    {"id": "tc6_s4_r03", "subcategory_id": "tc6_s4", "name": "خطة تعزيز التعاون المهني", "order": 3},
    {"id": "tc6_s4_r04", "subcategory_id": "tc6_s4", "name": "إحصائية عدد الخطط المشتركة", "order": 4},
    {"id": "tc6_s4_r05", "subcategory_id": "tc6_s4", "name": "تقييم أثر التغذية الراجعة من الزملاء", "order": 5},
    {"id": "tc6_s4_r06", "subcategory_id": "tc6_s4", "name": "توعية المعلمين بفوائد المشاركة", "order": 6},
    {"id": "tc6_s4_r07", "subcategory_id": "tc6_s4", "name": "تنسيق مع قادة الفرق", "order": 7},
    {"id": "tc6_s4_r08", "subcategory_id": "tc6_s4", "name": "تحسين آليات المشاركة", "order": 8},
    {"id": "tc6_s4_r09", "subcategory_id": "tc6_s4", "name": "متابعة تحسين الخطط", "order": 9},
    {"id": "tc6_s4_r10", "subcategory_id": "tc6_s4", "name": "إنجازات التعاون المهني", "order": 10},

    # tc6_s5
    {"id": "tc6_s5_r01", "subcategory_id": "tc6_s5", "name": "تقرير عن فهم الخصائص النفسية للمرحلة العمرية", "order": 1},
    {"id": "tc6_s5_r02", "subcategory_id": "tc6_s5", "name": "سجل تطبيقات علم النفس في التدريس", "order": 2},
    {"id": "tc6_s5_r03", "subcategory_id": "tc6_s5", "name": "خطة تدريب المعلمين على خصائص النمو", "order": 3},
    {"id": "tc6_s5_r04", "subcategory_id": "tc6_s5", "name": "إحصائية مدى مراعاة الخصائص في الخطط", "order": 4},
    {"id": "tc6_s5_r05", "subcategory_id": "tc6_s5", "name": "تقييم أثر مراعاة الخصائص على التفاعل", "order": 5},
    {"id": "tc6_s5_r06", "subcategory_id": "tc6_s5", "name": "توعية المعلمين بمراحل النمو", "order": 6},
    {"id": "tc6_s5_r07", "subcategory_id": "tc6_s5", "name": "تنسيق مع المرشد الطلابي", "order": 7},
    {"id": "tc6_s5_r08", "subcategory_id": "tc6_s5", "name": "تحسين الأنشطة حسب المرحلة", "order": 8},
    {"id": "tc6_s5_r09", "subcategory_id": "tc6_s5", "name": "متابعة تكيف الطلاب", "order": 9},
    {"id": "tc6_s5_r10", "subcategory_id": "tc6_s5", "name": "إنجازات مراعاة الخصائص", "order": 10},

    # tc7_s1
    {"id": "tc7_s1_r01", "subcategory_id": "tc7_s1", "name": "تقرير عن استخدام السبورات الذكية", "order": 1},
    {"id": "tc7_s1_r02", "subcategory_id": "tc7_s1", "name": "سجل الأجهزة اللوحية في الفصول", "order": 2},
    {"id": "tc7_s1_r03", "subcategory_id": "tc7_s1", "name": "خطة تفعيل التقنيات في الدروس", "order": 3},
    {"id": "tc7_s1_r04", "subcategory_id": "tc7_s1", "name": "إحصائية عدد الحصص المستخدمة للتقنية", "order": 4},
    {"id": "tc7_s1_r05", "subcategory_id": "tc7_s1", "name": "تقييم كفاءة استخدام الأجهزة", "order": 5},
    {"id": "tc7_s1_r06", "subcategory_id": "tc7_s1", "name": "توعية المعلمين بكيفية استخدام السبورات", "order": 6},
    {"id": "tc7_s1_r07", "subcategory_id": "tc7_s1", "name": "تنسيق مع مختبر الحاسب للصيانة", "order": 7},
    {"id": "tc7_s1_r08", "subcategory_id": "tc7_s1", "name": "تحسين البرامج المستخدمة", "order": 8},
    {"id": "tc7_s1_r09", "subcategory_id": "tc7_s1", "name": "متابعة أعطال الأجهزة", "order": 9},
    {"id": "tc7_s1_r10", "subcategory_id": "tc7_s1", "name": "إنجازات توظيف التقنية", "order": 10},

    # tc7_s2
    {"id": "tc7_s2_r01", "subcategory_id": "tc7_s2", "name": "تقرير عن استخدام منصات التعليم عن بعد", "order": 1},
    {"id": "tc7_s2_r02", "subcategory_id": "tc7_s2", "name": "سجل تفعيل الفصول الافتراضية", "order": 2},
    {"id": "tc7_s2_r03", "subcategory_id": "tc7_s2", "name": "خطة تطبيق برامج التعلم الإلكتروني", "order": 3},
    {"id": "tc7_s2_r04", "subcategory_id": "tc7_s2", "name": "إحصائية عدد الدروس عن بعد", "order": 4},
    {"id": "tc7_s2_r05", "subcategory_id": "tc7_s2", "name": "تقييم تفاعل الطلاب مع المنصات", "order": 5},
    {"id": "tc7_s2_r06", "subcategory_id": "tc7_s2", "name": "توعية الطلاب باستخدام المنصات", "order": 6},
    {"id": "tc7_s2_r07", "subcategory_id": "tc7_s2", "name": "تنسيق مع فريق الدعم التقني", "order": 7},
    {"id": "tc7_s2_r08", "subcategory_id": "tc7_s2", "name": "تحسين محتوى المنصة", "order": 8},
    {"id": "tc7_s2_r09", "subcategory_id": "tc7_s2", "name": "متابعة حل المشكلات التقنية", "order": 9},
    {"id": "tc7_s2_r10", "subcategory_id": "tc7_s2", "name": "إنجازات التعلم الإلكتروني", "order": 10},

    # tc7_s3
    {"id": "tc7_s3_r01", "subcategory_id": "tc7_s3", "name": "تقرير عن تشجيع الطلاب على استخدام التطبيقات التعليمية", "order": 1},
    {"id": "tc7_s3_r02", "subcategory_id": "tc7_s3", "name": "سجل التطبيقات الموصى بها", "order": 2},
    {"id": "tc7_s3_r03", "subcategory_id": "tc7_s3", "name": "خطة تعزيز التعلم الذاتي بالتطبيقات", "order": 3},
    {"id": "tc7_s3_r04", "subcategory_id": "tc7_s3", "name": "إحصائية عدد الطلاب المستخدمين", "order": 4},
    {"id": "tc7_s3_r05", "subcategory_id": "tc7_s3", "name": "تقييم أثر التطبيقات على التحصيل", "order": 5},
    {"id": "tc7_s3_r06", "subcategory_id": "tc7_s3", "name": "توعية أولياء الأمور بالتطبيقات", "order": 6},
    {"id": "tc7_s3_r07", "subcategory_id": "tc7_s3", "name": "تنسيق مع مطوري التطبيقات", "order": 7},
    {"id": "tc7_s3_r08", "subcategory_id": "tc7_s3", "name": "تحسين اختيار التطبيقات", "order": 8},
    {"id": "tc7_s3_r09", "subcategory_id": "tc7_s3", "name": "متابعة استخدام الطلاب", "order": 9},
    {"id": "tc7_s3_r10", "subcategory_id": "tc7_s3", "name": "إنجازات التعلم الذاتي", "order": 10},

    # tc7_s4
    {"id": "tc7_s4_r01", "subcategory_id": "tc7_s4", "name": "تقرير عن تنظيم ورش عمل عن التكنولوجيا", "order": 1},
    {"id": "tc7_s4_r02", "subcategory_id": "tc7_s4", "name": "سجل المشاركين في ورش التقنية", "order": 2},
    {"id": "tc7_s4_r03", "subcategory_id": "tc7_s4", "name": "خطة تدريب المعلمين على التقنيات", "order": 3},
    {"id": "tc7_s4_r04", "subcategory_id": "tc7_s4", "name": "إحصائية عدد الورش المنفذة", "order": 4},
    {"id": "tc7_s4_r05", "subcategory_id": "tc7_s4", "name": "تقييم فاعلية الورش", "order": 5},
    {"id": "tc7_s4_r06", "subcategory_id": "tc7_s4", "name": "توعية المعلمين بأهمية التدريب", "order": 6},
    {"id": "tc7_s4_r07", "subcategory_id": "tc7_s4", "name": "تنسيق مع مدربين متخصصين", "order": 7},
    {"id": "tc7_s4_r08", "subcategory_id": "tc7_s4", "name": "تحسين محتوى الورش", "order": 8},
    {"id": "tc7_s4_r09", "subcategory_id": "tc7_s4", "name": "متابعة تطبيق المهارات", "order": 9},
    {"id": "tc7_s4_r10", "subcategory_id": "tc7_s4", "name": "إنجازات برنامج التدريب التقني", "order": 10},

    # tc8_s1
    {"id": "tc8_s1_r01", "subcategory_id": "tc8_s1", "name": "تقرير عن تزيين الفصول بالوسائل التعليمية", "order": 1},
    {"id": "tc8_s1_r02", "subcategory_id": "tc8_s1", "name": "سجل اللوحات الجدارية", "order": 2},
    {"id": "tc8_s1_r03", "subcategory_id": "tc8_s1", "name": "خطة تحسين المظهر البصري للفصول", "order": 3},
    {"id": "tc8_s1_r04", "subcategory_id": "tc8_s1", "name": "إحصائية عدد الوسائل الجديدة", "order": 4},
    {"id": "tc8_s1_r05", "subcategory_id": "tc8_s1", "name": "تقييم أثر التزيين على التحفيز", "order": 5},
    {"id": "tc8_s1_r06", "subcategory_id": "tc8_s1", "name": "توعية المعلمين بأهمية التزيين", "order": 6},
    {"id": "tc8_s1_r07", "subcategory_id": "tc8_s1", "name": "تنسيق مع إدارة المدرسة لتوفير المواد", "order": 7},
    {"id": "tc8_s1_r08", "subcategory_id": "tc8_s1", "name": "تحسين دورية تغيير اللوحات", "order": 8},
    {"id": "tc8_s1_r09", "subcategory_id": "tc8_s1", "name": "متابعة مشاركة الطلاب في التزيين", "order": 9},
    {"id": "tc8_s1_r10", "subcategory_id": "tc8_s1", "name": "إنجازات برنامج تزيين الفصول", "order": 10},

    # tc8_s2
    {"id": "tc8_s2_r01", "subcategory_id": "tc8_s2", "name": "تقرير عن تنظيم الفصل لتسهيل الحركة", "order": 1},
    {"id": "tc8_s2_r02", "subcategory_id": "tc8_s2", "name": "سجل توزيع المقاعد", "order": 2},
    {"id": "tc8_s2_r03", "subcategory_id": "tc8_s2", "name": "خطة تهيئة الفصل للتفاعل", "order": 3},
    {"id": "tc8_s2_r04", "subcategory_id": "tc8_s2", "name": "إحصائية عدد الفصول المنظمة", "order": 4},
    {"id": "tc8_s2_r05", "subcategory_id": "tc8_s2", "name": "تقييم تأثير التنظيم على التفاعل", "order": 5},
    {"id": "tc8_s2_r06", "subcategory_id": "tc8_s2", "name": "توعية المعلمين باستراتيجيات التنظيم", "order": 6},
    {"id": "tc8_s2_r07", "subcategory_id": "tc8_s2", "name": "تنسيق مع مشرفي الصفوف", "order": 7},
    {"id": "tc8_s2_r08", "subcategory_id": "tc8_s2", "name": "تحسين توزيع المساحات", "order": 8},
    {"id": "tc8_s2_r09", "subcategory_id": "tc8_s2", "name": "متابعة تجارب التنظيم", "order": 9},
    {"id": "tc8_s2_r10", "subcategory_id": "tc8_s2", "name": "إنجازات تنظيم الفصول", "order": 10},

    # tc8_s3
    {"id": "tc8_s3_r01", "subcategory_id": "tc8_s3", "name": "تقرير عن توفير الأدوات والموارد التعليمية", "order": 1},
    {"id": "tc8_s3_r02", "subcategory_id": "tc8_s3", "name": "سجل الاحتياجات من الموارد", "order": 2},
    {"id": "tc8_s3_r03", "subcategory_id": "tc8_s3", "name": "خطة تزويد الفصول بالمواد", "order": 3},
    {"id": "tc8_s3_r04", "subcategory_id": "tc8_s3", "name": "إحصائية توفر الموارد", "order": 4},
    {"id": "tc8_s3_r05", "subcategory_id": "tc8_s3", "name": "تقييم كفاية الموارد", "order": 5},
    {"id": "tc8_s3_r06", "subcategory_id": "tc8_s3", "name": "توعية المعلمين بترشيد الاستهلاك", "order": 6},
    {"id": "tc8_s3_r07", "subcategory_id": "tc8_s3", "name": "تنسيق مع الموردين", "order": 7},
    {"id": "tc8_s3_r08", "subcategory_id": "tc8_s3", "name": "تحسين جودة الأدوات", "order": 8},
    {"id": "tc8_s3_r09", "subcategory_id": "tc8_s3", "name": "متابعة صيانة الموارد", "order": 9},
    {"id": "tc8_s3_r10", "subcategory_id": "tc8_s3", "name": "إنجازات توفير الموارد", "order": 10},

    # tc8_s4
    {"id": "tc8_s4_r01", "subcategory_id": "tc8_s4", "name": "تقرير عن توفير بيئة آمنة نفسياً", "order": 1},
    {"id": "tc8_s4_r02", "subcategory_id": "tc8_s4", "name": "سجل إجراءات السلامة", "order": 2},
    {"id": "tc8_s4_r03", "subcategory_id": "tc8_s4", "name": "خطة تحسين الأمان المادي", "order": 3},
    {"id": "tc8_s4_r04", "subcategory_id": "tc8_s4", "name": "إحصائية عدد الحوادث", "order": 4},
    {"id": "tc8_s4_r05", "subcategory_id": "tc8_s4", "name": "تقييم جاهزية الطوارئ", "order": 5},
    {"id": "tc8_s4_r06", "subcategory_id": "tc8_s4", "name": "توعية الطلاب بالسلامة", "order": 6},
    {"id": "tc8_s4_r07", "subcategory_id": "tc8_s4", "name": "تنسيق مع الدفاع المدني", "order": 7},
    {"id": "tc8_s4_r08", "subcategory_id": "tc8_s4", "name": "تحسين إجراءات الإخلاء", "order": 8},
    {"id": "tc8_s4_r09", "subcategory_id": "tc8_s4", "name": "متابعة صيانة معدات السلامة", "order": 9},
    {"id": "tc8_s4_r10", "subcategory_id": "tc8_s4", "name": "إنجازات برنامج الأمان", "order": 10},

    # tc8_s5
    {"id": "tc8_s5_r01", "subcategory_id": "tc8_s5", "name": "تقرير عن تمكين المتعلمين من التعبير", "order": 1},
    {"id": "tc8_s5_r02", "subcategory_id": "tc8_s5", "name": "سجل مشاركات الطلاب", "order": 2},
    {"id": "tc8_s5_r03", "subcategory_id": "tc8_s5", "name": "خطة تعزيز حرية التعبير", "order": 3},
    {"id": "tc8_s5_r04", "subcategory_id": "tc8_s5", "name": "إحصائية عدد المشاركات", "order": 4},
    {"id": "tc8_s5_r05", "subcategory_id": "tc8_s5", "name": "تقييم أثر التعبير على الثقة", "order": 5},
    {"id": "tc8_s5_r06", "subcategory_id": "tc8_s5", "name": "توعية الطلاب بأهمية المشاركة", "order": 6},
    {"id": "tc8_s5_r07", "subcategory_id": "tc8_s5", "name": "تنسيق مع رائد الفصل", "order": 7},
    {"id": "tc8_s5_r08", "subcategory_id": "tc8_s5", "name": "تحسين آليات الاستماع", "order": 8},
    {"id": "tc8_s5_r09", "subcategory_id": "tc8_s5", "name": "متابعة تطور مهارات التعبير", "order": 9},
    {"id": "tc8_s5_r10", "subcategory_id": "tc8_s5", "name": "إنجازات برنامج التعبير", "order": 10},

    # tc8_s6
    {"id": "tc8_s6_r01", "subcategory_id": "tc8_s6", "name": "تقرير عن إثارة دافعية المتعلمين", "order": 1},
    {"id": "tc8_s6_r02", "subcategory_id": "tc8_s6", "name": "سجل أساليب التحفيز", "order": 2},
    {"id": "tc8_s6_r03", "subcategory_id": "tc8_s6", "name": "خطة تنويع أساليب التعلم", "order": 3},
    {"id": "tc8_s6_r04", "subcategory_id": "tc8_s6", "name": "إحصائية مدى تفاعل الطلاب", "order": 4},
    {"id": "tc8_s6_r05", "subcategory_id": "tc8_s6", "name": "تقييم أثر التنويع على الدافعية", "order": 5},
    {"id": "tc8_s6_r06", "subcategory_id": "tc8_s6", "name": "توعية المعلمين بأساليب التحفيز", "order": 6},
    {"id": "tc8_s6_r07", "subcategory_id": "tc8_s6", "name": "تنسيق مع وحدة الإرشاد", "order": 7},
    {"id": "tc8_s6_r08", "subcategory_id": "tc8_s6", "name": "تحسين استخدام المكافآت", "order": 8},
    {"id": "tc8_s6_r09", "subcategory_id": "tc8_s6", "name": "متابعة استجابة الطلاب", "order": 9},
    {"id": "tc8_s6_r10", "subcategory_id": "tc8_s6", "name": "إنجازات برنامج الدافعية", "order": 10},

    # tc9_s1
    {"id": "tc9_s1_r01", "subcategory_id": "tc9_s1", "name": "تقرير عن استخدام الاختبارات الدورية", "order": 1},
    {"id": "tc9_s1_r02", "subcategory_id": "tc9_s1", "name": "سجل نتائج التقييمات", "order": 2},
    {"id": "tc9_s1_r03", "subcategory_id": "tc9_s1", "name": "خطة تطوير أدوات التقييم", "order": 3},
    {"id": "tc9_s1_r04", "subcategory_id": "tc9_s1", "name": "إحصائية عدد الاختبارات", "order": 4},
    {"id": "tc9_s1_r05", "subcategory_id": "tc9_s1", "name": "تقييم دقة الاختبارات", "order": 5},
    {"id": "tc9_s1_r06", "subcategory_id": "tc9_s1", "name": "توعية الطلاب بأهمية الاختبارات", "order": 6},
    {"id": "tc9_s1_r07", "subcategory_id": "tc9_s1", "name": "تنسيق مع لجنة الاختبارات", "order": 7},
    {"id": "tc9_s1_r08", "subcategory_id": "tc9_s1", "name": "تحسين تنوع الأسئلة", "order": 8},
    {"id": "tc9_s1_r09", "subcategory_id": "tc9_s1", "name": "متابعة تصحيح الاختبارات", "order": 9},
    {"id": "tc9_s1_r10", "subcategory_id": "tc9_s1", "name": "إنجازات التقييم الدوري", "order": 10},

    # tc9_s2
    {"id": "tc9_s2_r01", "subcategory_id": "tc9_s2", "name": "تقرير عن تحليل نتائج الطلاب", "order": 1},
    {"id": "tc9_s2_r02", "subcategory_id": "tc9_s2", "name": "سجل نقاط القوة والضعف", "order": 2},
    {"id": "tc9_s2_r03", "subcategory_id": "tc9_s2", "name": "خطة إشراك الطلاب في تحليل نتائجهم", "order": 3},
    {"id": "tc9_s2_r04", "subcategory_id": "tc9_s2", "name": "إحصائية مدى فهم الطلاب لنتائجهم", "order": 4},
    {"id": "tc9_s2_r05", "subcategory_id": "tc9_s2", "name": "تقييم أثر التحليل على التحسن", "order": 5},
    {"id": "tc9_s2_r06", "subcategory_id": "tc9_s2", "name": "توعية المعلمين بأساليب التحليل", "order": 6},
    {"id": "tc9_s2_r07", "subcategory_id": "tc9_s2", "name": "تنسيق مع مشرفي المواد", "order": 7},
    {"id": "tc9_s2_r08", "subcategory_id": "tc9_s2", "name": "تحسين أدوات التحليل", "order": 8},
    {"id": "tc9_s2_r09", "subcategory_id": "tc9_s2", "name": "متابعة خطط التحسين", "order": 9},
    {"id": "tc9_s2_r10", "subcategory_id": "tc9_s2", "name": "إنجازات تحليل النتائج", "order": 10},

    # tc9_s3
    {"id": "tc9_s3_r01", "subcategory_id": "tc9_s3", "name": "تقرير عن توفير تغذية راجعة فردية", "order": 1},
    {"id": "tc9_s3_r02", "subcategory_id": "tc9_s3", "name": "سجل اللقاءات الفردية", "order": 2},
    {"id": "tc9_s3_r03", "subcategory_id": "tc9_s3", "name": "خطة تخصيص التغذية", "order": 3},
    {"id": "tc9_s3_r04", "subcategory_id": "tc9_s3", "name": "إحصائية عدد الطلاب المستفيدين", "order": 4},
    {"id": "tc9_s3_r05", "subcategory_id": "tc9_s3", "name": "تقييم أثر التغذية الفردية", "order": 5},
    {"id": "tc9_s3_r06", "subcategory_id": "tc9_s3", "name": "توعية المعلمين بأهمية التخصيص", "order": 6},
    {"id": "tc9_s3_r07", "subcategory_id": "tc9_s3", "name": "تنسيق مع المرشد الطلابي", "order": 7},
    {"id": "tc9_s3_r08", "subcategory_id": "tc9_s3", "name": "تحسين جدولة اللقاءات", "order": 8},
    {"id": "tc9_s3_r09", "subcategory_id": "tc9_s3", "name": "متابعة تطور الطلاب", "order": 9},
    {"id": "tc9_s3_r10", "subcategory_id": "tc9_s3", "name": "إنجازات التغذية الفردية", "order": 10},

    # tc9_s4
    {"id": "tc9_s4_r01", "subcategory_id": "tc9_s4", "name": "تقرير عن تطبيق خطط علاجية", "order": 1},
    {"id": "tc9_s4_r02", "subcategory_id": "tc9_s4", "name": "سجل الطلاب المشمولين بالدعم", "order": 2},
    {"id": "tc9_s4_r03", "subcategory_id": "tc9_s4", "name": "خطة برامج العلاج", "order": 3},
    {"id": "tc9_s4_r04", "subcategory_id": "tc9_s4", "name": "إحصائية عدد الطلاب في الخطط", "order": 4},
    {"id": "tc9_s4_r05", "subcategory_id": "tc9_s4", "name": "تقييم فعالية الخطط", "order": 5},
    {"id": "tc9_s4_r06", "subcategory_id": "tc9_s4", "name": "توعية أولياء الأمور بالخطط", "order": 6},
    {"id": "tc9_s4_r07", "subcategory_id": "tc9_s4", "name": "تنسيق مع معلمي المواد", "order": 7},
    {"id": "tc9_s4_r08", "subcategory_id": "tc9_s4", "name": "تحسين أنشطة العلاج", "order": 8},
    {"id": "tc9_s4_r09", "subcategory_id": "tc9_s4", "name": "متابعة تقدم الطلاب", "order": 9},
    {"id": "tc9_s4_r10", "subcategory_id": "tc9_s4", "name": "إنجازات الخطط العلاجية", "order": 10},

    # tc9_s5
    {"id": "tc9_s5_r01", "subcategory_id": "tc9_s5", "name": "تقرير عن قياس التطبيق العملي للمعرفة", "order": 1},
    {"id": "tc9_s5_r02", "subcategory_id": "tc9_s5", "name": "سجل المشاريع التطبيقية", "order": 2},
    {"id": "tc9_s5_r03", "subcategory_id": "tc9_s5", "name": "خطة دمج التطبيق في التقييم", "order": 3},
    {"id": "tc9_s5_r04", "subcategory_id": "tc9_s5", "name": "إحصائية عدد المواقف العملية", "order": 4},
    {"id": "tc9_s5_r05", "subcategory_id": "tc9_s5", "name": "تقييم مهارات التطبيق", "order": 5},
    {"id": "tc9_s5_r06", "subcategory_id": "tc9_s5", "name": "توعية الطلاب بأهمية التطبيق", "order": 6},
    {"id": "tc9_s5_r07", "subcategory_id": "tc9_s5", "name": "تنسيق مع جهات خارجية", "order": 7},
    {"id": "tc9_s5_r08", "subcategory_id": "tc9_s5", "name": "تحسين معايير التقييم", "order": 8},
    {"id": "tc9_s5_r09", "subcategory_id": "tc9_s5", "name": "متابعة تنفيذ المشاريع", "order": 9},
    {"id": "tc9_s5_r10", "subcategory_id": "tc9_s5", "name": "إنجازات التقييم العملي", "order": 10},

    # tc10_s1
    {"id": "tc10_s1_r01", "subcategory_id": "tc10_s1", "name": "تقرير عن استخدام الاختبارات الكتابية", "order": 1},
    {"id": "tc10_s1_r02", "subcategory_id": "tc10_s1", "name": "سجل الاختبارات الشفوية", "order": 2},
    {"id": "tc10_s1_r03", "subcategory_id": "tc10_s1", "name": "خطة تنويع أساليب التقويم", "order": 3},
    {"id": "tc10_s1_r04", "subcategory_id": "tc10_s1", "name": "إحصائية عدد الاختبارات", "order": 4},
    {"id": "tc10_s1_r05", "subcategory_id": "tc10_s1", "name": "تقييم موثوقية الاختبارات", "order": 5},
    {"id": "tc10_s1_r06", "subcategory_id": "tc10_s1", "name": "توعية المعلمين بأساليب التقويم", "order": 6},
    {"id": "tc10_s1_r07", "subcategory_id": "tc10_s1", "name": "تنسيق مع مشرفي المواد", "order": 7},
    {"id": "tc10_s1_r08", "subcategory_id": "tc10_s1", "name": "تحسين نماذج الاختبارات", "order": 8},
    {"id": "tc10_s1_r09", "subcategory_id": "tc10_s1", "name": "متابعة تطبيق الشفوي", "order": 9},
    {"id": "tc10_s1_r10", "subcategory_id": "tc10_s1", "name": "إنجازات تنويع التقويم", "order": 10},

    # tc10_s2
    {"id": "tc10_s2_r01", "subcategory_id": "tc10_s2", "name": "تقرير عن تقييم المشاريع", "order": 1},
    {"id": "tc10_s2_r02", "subcategory_id": "tc10_s2", "name": "سجل العروض التقييمية", "order": 2},
    {"id": "tc10_s2_r03", "subcategory_id": "tc10_s2", "name": "خطة تطوير التقييم العملي", "order": 3},
    {"id": "tc10_s2_r04", "subcategory_id": "tc10_s2", "name": "إحصائية عدد المشاريع المقيّمة", "order": 4},
    {"id": "tc10_s2_r05", "subcategory_id": "tc10_s2", "name": "تقييم موضوعية التقييم", "order": 5},
    {"id": "tc10_s2_r06", "subcategory_id": "tc10_s2", "name": "توعية الطلاب بمعايير التقييم", "order": 6},
    {"id": "tc10_s2_r07", "subcategory_id": "tc10_s2", "name": "تنسيق مع لجنة التقييم", "order": 7},
    {"id": "tc10_s2_r08", "subcategory_id": "tc10_s2", "name": "تحسين معايير التقييم", "order": 8},
    {"id": "tc10_s2_r09", "subcategory_id": "tc10_s2", "name": "متابعة تقديم العروض", "order": 9},
    {"id": "tc10_s2_r10", "subcategory_id": "tc10_s2", "name": "إنجازات التقييم العملي", "order": 10},

    # tc10_s3
    {"id": "tc10_s3_r01", "subcategory_id": "tc10_s3", "name": "تقرير عن استخدام التقييم التكويني", "order": 1},
    {"id": "tc10_s3_r02", "subcategory_id": "tc10_s3", "name": "سجل متابعة التقدم", "order": 2},
    {"id": "tc10_s3_r03", "subcategory_id": "tc10_s3", "name": "خطة تطبيق التقييم المستمر", "order": 3},
    {"id": "tc10_s3_r04", "subcategory_id": "tc10_s3", "name": "إحصائية عدد مرات التقييم التكويني", "order": 4},
    {"id": "tc10_s3_r05", "subcategory_id": "tc10_s3", "name": "تقييم أثر التقييم على التعلم", "order": 5},
    {"id": "tc10_s3_r06", "subcategory_id": "tc10_s3", "name": "توعية المعلمين بأهمية التكويني", "order": 6},
    {"id": "tc10_s3_r07", "subcategory_id": "tc10_s3", "name": "تنسيق مع مشرفين", "order": 7},
    {"id": "tc10_s3_r08", "subcategory_id": "tc10_s3", "name": "تحسين أدوات التقييم", "order": 8},
    {"id": "tc10_s3_r09", "subcategory_id": "tc10_s3", "name": "متابعة استجابة الطلاب", "order": 9},
    {"id": "tc10_s3_r10", "subcategory_id": "tc10_s3", "name": "إنجازات التقييم التكويني", "order": 10},

    # tc10_s4
    {"id": "tc10_s4_r01", "subcategory_id": "tc10_s4", "name": "تقرير عن استخدام التقويم القبلي", "order": 1},
    {"id": "tc10_s4_r02", "subcategory_id": "tc10_s4", "name": "سجل تشخيص المعرفة السابقة", "order": 2},
    {"id": "tc10_s4_r03", "subcategory_id": "tc10_s4", "name": "خطة تطبيق التقويم القبلي", "order": 3},
    {"id": "tc10_s4_r04", "subcategory_id": "tc10_s4", "name": "إحصائية عدد مرات التقويم القبلي", "order": 4},
    {"id": "tc10_s4_r05", "subcategory_id": "tc10_s4", "name": "تقييم دقة التشخيص", "order": 5},
    {"id": "tc10_s4_r06", "subcategory_id": "tc10_s4", "name": "توعية المعلمين بأهمية التقويم القبلي", "order": 6},
    {"id": "tc10_s4_r07", "subcategory_id": "tc10_s4", "name": "تنسيق مع رؤساء الأقسام", "order": 7},
    {"id": "tc10_s4_r08", "subcategory_id": "tc10_s4", "name": "تحسين أدوات القياس", "order": 8},
    {"id": "tc10_s4_r09", "subcategory_id": "tc10_s4", "name": "متابعة تكييف الخطط بناءً على النتائج", "order": 9},
    {"id": "tc10_s4_r10", "subcategory_id": "tc10_s4", "name": "إنجازات التقويم القبلي", "order": 10},

    # tc10_s5
    {"id": "tc10_s5_r01", "subcategory_id": "tc10_s5", "name": "تقرير عن تطبيق التقويم الختامي", "order": 1},
    {"id": "tc10_s5_r02", "subcategory_id": "tc10_s5", "name": "سجل نتائج الاختبارات النهائية", "order": 2},
    {"id": "tc10_s5_r03", "subcategory_id": "tc10_s5", "name": "خطة تحسين التقويم الختامي", "order": 3},
    {"id": "tc10_s5_r04", "subcategory_id": "tc10_s5", "name": "إحصائية مستويات الطلاب", "order": 4},
    {"id": "tc10_s5_r05", "subcategory_id": "tc10_s5", "name": "تقييم تحقيق الأهداف", "order": 5},
    {"id": "tc10_s5_r06", "subcategory_id": "tc10_s5", "name": "توعية الطلاب بأهمية الختامي", "order": 6},
    {"id": "tc10_s5_r07", "subcategory_id": "tc10_s5", "name": "تنسيق مع كنترول الامتحانات", "order": 7},
    {"id": "tc10_s5_r08", "subcategory_id": "tc10_s5", "name": "تحسين إجراءات التصحيح", "order": 8},
    {"id": "tc10_s5_r09", "subcategory_id": "tc10_s5", "name": "متابعة إصدار النتائج", "order": 9},
    {"id": "tc10_s5_r10", "subcategory_id": "tc10_s5", "name": "إنجازات التقويم الختامي", "order": 10},

    # tc11_s1
    {"id": "tc11_s1_r01", "subcategory_id": "tc11_s1", "name": "تقرير عن تنفيذ الخطة المشتركة للبرامج الصحية", "order": 1},
    {"id": "tc11_s1_r02", "subcategory_id": "tc11_s1", "name": "سجل متابعة الأنشطة الصحية", "order": 2},
    {"id": "tc11_s1_r03", "subcategory_id": "tc11_s1", "name": "خطة تنفيذ البرامج الصحية", "order": 3},
    {"id": "tc11_s1_r04", "subcategory_id": "tc11_s1", "name": "إحصائية عدد البرامج المنفذة", "order": 4},
    {"id": "tc11_s1_r05", "subcategory_id": "tc11_s1", "name": "تقييم فعالية البرامج", "order": 5},
    {"id": "tc11_s1_r06", "subcategory_id": "tc11_s1", "name": "توعية الطلاب بأهمية البرامج الصحية", "order": 6},
    {"id": "tc11_s1_r07", "subcategory_id": "tc11_s1", "name": "تنسيق مع وزارة الصحة", "order": 7},
    {"id": "tc11_s1_r08", "subcategory_id": "tc11_s1", "name": "تحسين توقيت البرامج", "order": 8},
    {"id": "tc11_s1_r09", "subcategory_id": "tc11_s1", "name": "متابعة مشاركة الطلاب", "order": 9},
    {"id": "tc11_s1_r10", "subcategory_id": "tc11_s1", "name": "إنجازات البرامج الصحية", "order": 10},

    # tc12_s1
    {"id": "tc12_s1_r01", "subcategory_id": "tc12_s1", "name": "تقرير عن حصر الحالات الصحية للطلاب", "order": 1},
    {"id": "tc12_s1_r02", "subcategory_id": "tc12_s1", "name": "سجل الأمراض المزمنة", "order": 2},
    {"id": "tc12_s1_r03", "subcategory_id": "tc12_s1", "name": "خطة تحديث قاعدة البيانات الصحية", "order": 3},
    {"id": "tc12_s1_r04", "subcategory_id": "tc12_s1", "name": "إحصائية عدد الحالات المحصورة", "order": 4},
    {"id": "tc12_s1_r05", "subcategory_id": "tc12_s1", "name": "تقييم دقة الحصر", "order": 5},
    {"id": "tc12_s1_r06", "subcategory_id": "tc12_s1", "name": "توعية أولياء الأمور بأهمية الإبلاغ", "order": 6},
    {"id": "tc12_s1_r07", "subcategory_id": "tc12_s1", "name": "تنسيق مع المرشد الصحي", "order": 7},
    {"id": "tc12_s1_r08", "subcategory_id": "tc12_s1", "name": "تحسين نظام نور الصحي", "order": 8},
    {"id": "tc12_s1_r09", "subcategory_id": "tc12_s1", "name": "متابعة تحديث السجلات", "order": 9},
    {"id": "tc12_s1_r10", "subcategory_id": "tc12_s1", "name": "إنجازات برنامج الحصر الصحي", "order": 10},

    # tc13_s1
    {"id": "tc13_s1_r01", "subcategory_id": "tc13_s1", "name": "تقرير عن تهيئة البيئة الصحية المدرسية", "order": 1},
    {"id": "tc13_s1_r02", "subcategory_id": "tc13_s1", "name": "سجل جولات تفقد النظافة", "order": 2},
    {"id": "tc13_s1_r03", "subcategory_id": "tc13_s1", "name": "خطة تحسين البيئة المدرسية", "order": 3},
    {"id": "tc13_s1_r04", "subcategory_id": "tc13_s1", "name": "إحصائية مدى الالتزام بالمعايير الصحية", "order": 4},
    {"id": "tc13_s1_r05", "subcategory_id": "tc13_s1", "name": "تقييم جاهزية المدرسة صحياً", "order": 5},
    {"id": "tc13_s1_r06", "subcategory_id": "tc13_s1", "name": "توعية الطلاب بالحفاظ على البيئة", "order": 6},
    {"id": "tc13_s1_r07", "subcategory_id": "tc13_s1", "name": "تنسيق مع البلدية", "order": 7},
    {"id": "tc13_s1_r08", "subcategory_id": "tc13_s1", "name": "تحسين خدمات النظافة", "order": 8},
    {"id": "tc13_s1_r09", "subcategory_id": "tc13_s1", "name": "متابعة تطبيق الإجراءات", "order": 9},
    {"id": "tc13_s1_r10", "subcategory_id": "tc13_s1", "name": "إنجازات برنامج البيئة الصحية", "order": 10},
]

# قالب البرومبت المعدل ليكون أكثر عمومية
GENERIC_EDUCATION_PROMPT_TEMPLATE = """أنت مسؤول تربوي (معلم، مرشد صحي، أو قائد مدرسي) تعمل على تنفيذ البرامج والممارسات التعليمية والصحية وفق الأنظمة المعتمدة، بهدف تحقيق بيئة تعليمية آمنة ومحفزة.

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

ضوابط الكتابة:
- لغة إدارية تربوية رسمية.
- إبراز دورك في التخطيط والتنفيذ والمتابعة والتقييم.
- توضيح آلية تنفيذ البرامج والمبادرات التعليمية/الصحية.
- الإشارة إلى رصد النتائج وتحليلها والتنسيق مع الجهات ذات العلاقة.
- بيان دورك في تهيئة بيئة تعليمية آمنة نفسياً وجسدياً.
- إبراز استخدام التقنية أو النماذج المعتمدة في التوثيق.
- توضيح أثر الجهود على تحسين نواتج التعلم وسلامة الطلاب واستقرار العملية التعليمية.
- صياغة عملية دقيقة من 5–7 أسطر.

دورك التربوي:
1. رفع الوعي لدى الطلاب والمجتمع المدرسي وتعزيز السلوكيات الإيجابية بما يدعم جاهزيتهم للتعلم ويقلل من المشكلات المؤثرة على التحصيل.
2. نفذت مبادرة/برنامجاً يستهدف تحسين الممارسات التعليمية أو الصحية داخل المدرسة.
3. قدمت إجراءات عملية، ووزعت مواد إرشادية، وتابعت الحالات، ونسقت مع الزملاء لملاحظة أثر الجهود على الأداء.
4. اعتمدت استراتيجيات متنوعة مثل التعلم النشط، والتعلم القائم على المشاريع، والمناقشة الموجهة، وربط المفاهيم بالحياة اليومية.
5. ارتفع وعي الطلاب، وتحسن مستوى الأداء، وقلت المشكلات، وظهر أثر إيجابي على البيئة المدرسية.
6. الحاجة إلى تفعيل برامج متابعة مستمرة، وتعزيز مشاركة الأسرة، وبناء شراكات مجتمعية.
7. أوصي بإدراج خطة سنوية تكاملية، وتنفيذ حملات دورية، وبناء شراكات مجتمعية تدعم الثقافة التربوية والصحية المدرسية.

**الحقول المطلوبة:**
1. الهدف التربوي
2. نبذة مختصرة
3. إجراءات التنفيذ
4. الاستراتيجيات المستخدمة
5. نقاط القوة
6. نقاط التحسين
7. التوصيات

يرجى تقديم الإجابة باللغة العربية الفصحى، وتنظيمها بحيث يكون كل حقل في سطر منفصل يبدأ برقمه فقط دون ذكر العنوان.
"""

# يمكنك استخدام هذه المتغيرات في تطبيقك حسب الحاجة