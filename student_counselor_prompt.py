# student_counselor_prompt.py

# معايير الأداء الوظيفي مع نسبها المئوية
SG_CRITERIA = [
    {"id": "sg_c1", "name": "أداء الواجبات الوظيفية", "weight": 20, "order": 1},
    {"id": "sg_c2", "name": "التفاعل مع المجتمع المهني", "weight": 5, "order": 2},
    {"id": "sg_c3", "name": "التفاعل مع أولياء الأمور", "weight": 5, "order": 3},
    {"id": "sg_c4", "name": "يقدم التدخلات المناسبة لتعزيز الانضباط", "weight": 5, "order": 4},
    {"id": "sg_c5", "name": "تقديم برامج تربوية لتعزيز دافعية الطلبة للتعلم", "weight": 5, "order": 5},
    {"id": "sg_c6", "name": "اعداد خطة لبرامج التوجيه الطلابي", "weight": 10, "order": 6},
    {"id": "sg_c7", "name": "يصنف الحالات ويقدم برامج الداعم المناسبة", "weight": 10, "order": 7},
    {"id": "sg_c8", "name": "يعزز القيم والسلوكيات للمتعلمين", "weight": 10, "order": 8},
    {"id": "sg_c9", "name": "يقدم التدخلات النفسية والاجتماعية", "weight": 10, "order": 9},
    {"id": "sg_c10", "name": "يساعد المتعلمين على التخطيط المهني والتعليمي", "weight": 5, "order": 10},
    {"id": "sg_c11", "name": "يعزز التفوق الدراسي", "weight": 5, "order": 11},
    {"id": "sg_c12", "name": "يقدم تدخلات تربوية للمتأخرين دراسياً والمعيدين", "weight": 5, "order": 12},
    {"id": "sg_c13", "name": "توعية المتعلمين وأولياء امورهم بقواعد السلوك والمواظبة", "weight": 5, "order": 13},
]

# التصنيفات الفرعية (مرتبطة بكل معيار)
SG_SUBCATEGORIES = [
    # sg_c1 - أداء الواجبات الوظيفية (20%)
    {"id": "sg_c1_s1", "criterion_id": "sg_c1", "name": "يطبق الأنظمة وقواعد السلوك الوظيفية وأخلاقيات بيئة التعلم", "order": 1},
    {"id": "sg_c1_s2", "criterion_id": "sg_c1", "name": "حماية البيانات والمعلومات التي تتعلق بالعمل أو الانشطة المهنية من الوصول غير المصرح به", "order": 2},
    {"id": "sg_c1_s3", "criterion_id": "sg_c1", "name": "التعاون مع المؤسسات الحكومية في المبادرات الوطنية", "order": 3},
    {"id": "sg_c1_s4", "criterion_id": "sg_c1", "name": "تنظيم أنشطة توعوية حول أهمية الانتماء والولاء الوطني", "order": 4},
    {"id": "sg_c1_s5", "criterion_id": "sg_c1", "name": "الامتثال للقوانين واللوائح وسياسات وإجراءات العمل", "order": 5},
    
    # sg_c2 - التفاعل مع المجتمع المهني (5%)
    {"id": "sg_c2_s1", "criterion_id": "sg_c2", "name": "حضور المؤتمرات والندوات التعليمية", "order": 1},
    {"id": "sg_c2_s2", "criterion_id": "sg_c2", "name": "المشاركة في ورش العمل التدريبية وأنشطة المجتمع المهني", "order": 2},
    {"id": "sg_c2_s3", "criterion_id": "sg_c2", "name": "تقديم استشارات الارشاد والتوجيه لدعم المعلمين الجدد", "order": 3},
    {"id": "sg_c2_s4", "criterion_id": "sg_c2", "name": "إطلاق مبادرات تعليمية لتحسين جودة التعليم وبناء بيئة تعليمية", "order": 4},
    
    # sg_c3 - التفاعل مع أولياء الأمور (5%)
    {"id": "sg_c3_s1", "criterion_id": "sg_c3", "name": "سجل التواصل مع أولياء الأمور", "order": 1},
    {"id": "sg_c3_s2", "criterion_id": "sg_c3", "name": "اجتماعات مع أولياء الأمور حول أداء المتعلمين", "order": 2},
    {"id": "sg_c3_s3", "criterion_id": "sg_c3", "name": "تنظيم اجتماعات دورية مع أولياء الأمور لمناقشة تقدم الطلاب", "order": 3},
    {"id": "sg_c3_s4", "criterion_id": "sg_c3", "name": "استخدام وسائل التواصل الحديثة لإبقاء أولياء الأمور على اطلاع", "order": 4},
    {"id": "sg_c3_s5", "criterion_id": "sg_c3", "name": "الاستجابة والاستماع لملاحظات ومخاوف أولياء الأمور والعمل بشكل تعاوني لمعالجتها", "order": 5},
    
    # sg_c4 - يقدم التدخلات المناسبة لتعزيز الانضباط (5%)
    {"id": "sg_c4_s1", "criterion_id": "sg_c4", "name": "تقديم برامج وممارسات داعمة للانضباط المدرسي", "order": 1},
    
    # sg_c5 - تقديم برامج تربوية لتعزيز دافعية الطلبة للتعلم (5%)
    {"id": "sg_c5_s1", "criterion_id": "sg_c5", "name": "تقديم برامج نوعية لتنمية مهارات واتجاهات الطلبة نحو التعلم وفق خصائص النمو", "order": 1},
    {"id": "sg_c5_s2", "criterion_id": "sg_c5", "name": "التنويع في أساليب تنفيذ البرامج التي تنمي مهارات واتجاهات الطلبة نحو التعلم", "order": 2},
    
    # sg_c6 - اعداد خطة لبرامج التوجيه الطلابي (10%)
    {"id": "sg_c6_s1", "criterion_id": "sg_c6", "name": "تصميم خطة للبرامج مكتملة العناصر ومبنية على معلومات وتحليل لواقع العمل الفعلي", "order": 1},
    
    # sg_c7 - يصنف الحالات ويقدم برامج الداعم المناسبة (10%)
    {"id": "sg_c7_s1", "criterion_id": "sg_c7", "name": "تقديم برامج نوعية بناءً على تصنيف حالات الطلبة، والبرامج المناسبة لكل فئة", "order": 1},
    
    # sg_c8 - يعزز القيم والسلوكيات للمتعلمين (10%)
    {"id": "sg_c8_s1", "criterion_id": "sg_c8", "name": "تزويد الطلبة ومنسوبي المدرسة بالقيم والسلوكيات الإيجابية، والعمل على تعزيزها", "order": 1},
    
    # sg_c9 - يقدم التدخلات النفسية والاجتماعية (10%)
    {"id": "sg_c9_s1", "criterion_id": "sg_c9", "name": "استخدام استراتيجيات فنية فعالة للوقاية والحد من المشكلات النفسية والاجتماعية", "order": 1},
    {"id": "sg_c9_s2", "criterion_id": "sg_c9", "name": "ممارسة التدخل الفردي والجمعي (المقابلة - دراسة الحالة - التوجيه الجمعي)", "order": 2},
    {"id": "sg_c9_s3", "criterion_id": "sg_c9", "name": "الرعاية الطلابية والتحويل للجهات ذات العلاقة", "order": 3},
    
    # sg_c10 - يساعد المتعلمين على التخطيط المهني والتعليمي (5%)
    {"id": "sg_c10_s1", "criterion_id": "sg_c10", "name": "تنفيذ برامج التوجيه التعليمي والمهني وفق الأدلة المنظمة", "order": 1},
    {"id": "sg_c10_s2", "criterion_id": "sg_c10", "name": "تطبيق مقاييس الميول والاتجاهات لاكتشاف قدرات الطلبة وميولهم", "order": 2},
    {"id": "sg_c10_s3", "criterion_id": "sg_c10", "name": "توجيه الطلبة للتخصصات المناسبة وفق ميولهم وقدراتهم", "order": 3},
    {"id": "sg_c10_s4", "criterion_id": "sg_c10", "name": "تزويد الطلبة بالمفاهيم الصحيحة نحو العمل المهني ومهارات التخطيط للمستقبل", "order": 4},
    
    # sg_c11 - يعزز التفوق الدراسي (5%)
    {"id": "sg_c11_s1", "criterion_id": "sg_c11", "name": "تقديم برامج وممارسات نوعية بناءً على تحليل نتائج الطلبة وتحديد مستواهم", "order": 1},
    {"id": "sg_c11_s2", "criterion_id": "sg_c11", "name": "تعزيز المتفوقين وتحفيز التفوق لدى بقية الطلبة", "order": 2},
    
    # sg_c12 - يقدم تدخلات تربوية للمتأخرين دراسياً والمعيدين (5%)
    {"id": "sg_c12_s1", "criterion_id": "sg_c12", "name": "تقديم برامج وممارسات مناسبة بناء على نتائج تحليل الطلاب للرفع من مستوى التحصيل الدراسي", "order": 1},
    
    # sg_c13 - توعية المتعلمين وأولياء امورهم بقواعد السلوك والمواظبة (5%)
    {"id": "sg_c13_s1", "criterion_id": "sg_c13", "name": "نشر قواعد السلوك والمواظبة في المجتمع المدرسي والمحلي", "order": 1},
]

# قائمة التقارير (10 لكل تصنيف فرعي)
SG_REPORTS = [
    # ========== sg_c1_s1 ==========
    {"id": "sg_c1_s1_r001", "subcategory_id": "sg_c1_s1", "name": "تقرير عن التزام المرشد الطلابي بتطبيق قواعد السلوك الوظيفي في المدرسة", "order": 1},
    {"id": "sg_c1_s1_r002", "subcategory_id": "sg_c1_s1", "name": "سجل متابعة تطبيق أخلاقيات بيئة التعلم لدى الطلاب", "order": 2},
    {"id": "sg_c1_s1_r003", "subcategory_id": "sg_c1_s1", "name": "تقرير عن ورش عمل للمعلمين حول قواعد السلوك الوظيفي", "order": 3},
    {"id": "sg_c1_s1_r004", "subcategory_id": "sg_c1_s1", "name": "توثيق تفعيل لائحة السلوك الطلابي في الفصول الدراسية", "order": 4},
    {"id": "sg_c1_s1_r005", "subcategory_id": "sg_c1_s1", "name": "تقرير عن مدى التزام الطلاب بقواعد السلوك المدرسي", "order": 5},
    {"id": "sg_c1_s1_r006", "subcategory_id": "sg_c1_s1", "name": "سجل اجتماعات مع الإدارة لمناقشة تطبيق الأنظمة", "order": 6},
    {"id": "sg_c1_s1_r007", "subcategory_id": "sg_c1_s1", "name": "تقرير عن حملات توعوية حول أخلاقيات الحوار داخل الفصل", "order": 7},
    {"id": "sg_c1_s1_r008", "subcategory_id": "sg_c1_s1", "name": "توثيق حالات مخالفة السلوك والإجراءات المتخذة", "order": 8},
    {"id": "sg_c1_s1_r009", "subcategory_id": "sg_c1_s1", "name": "تقرير عن تقييم الانضباط الوظيفي للمرشدين", "order": 9},
    {"id": "sg_c1_s1_r010", "subcategory_id": "sg_c1_s1", "name": "سجل تدريب الطلاب على حقوقهم وواجباتهم المدرسية", "order": 10},

    # ========== sg_c1_s2 ==========
    {"id": "sg_c1_s2_r001", "subcategory_id": "sg_c1_s2", "name": "تقرير عن تطبيق سياسات حماية بيانات الطلاب في مكتب الإرشاد", "order": 1},
    {"id": "sg_c1_s2_r002", "subcategory_id": "sg_c1_s2", "name": "سجل صلاحيات الوصول لملفات الطلاب الإلكترونية", "order": 2},
    {"id": "sg_c1_s2_r003", "subcategory_id": "sg_c1_s2", "name": "تقرير عن توعية الطلاب بأهمية الحفاظ على خصوصية معلوماتهم", "order": 3},
    {"id": "sg_c1_s2_r004", "subcategory_id": "sg_c1_s2", "name": "توثيق إجراءات تأمين الوثائق والمستندات السرية", "order": 4},
    {"id": "sg_c1_s2_r005", "subcategory_id": "sg_c1_s2", "name": "تقرير عن التزام الكادر التعليمي بسرية معلومات الطلاب", "order": 5},
    {"id": "sg_c1_s2_r006", "subcategory_id": "sg_c1_s2", "name": "سجل تدريب الموظفين على أمن المعلومات", "order": 6},
    {"id": "sg_c1_s2_r007", "subcategory_id": "sg_c1_s2", "name": "تقرير عن سياسات حماية البيانات في المنصات التعليمية", "order": 7},
    {"id": "sg_c1_s2_r008", "subcategory_id": "sg_c1_s2", "name": "توثيق موافقات أولياء الأمور على مشاركة بيانات أبنائهم", "order": 8},
    {"id": "sg_c1_s2_r009", "subcategory_id": "sg_c1_s2", "name": "تقرير عن آليات حفظ التقارير النفسية والسلوكية", "order": 9},
    {"id": "sg_c1_s2_r010", "subcategory_id": "sg_c1_s2", "name": "سجل المراجعة الدورية لأنظمة الحماية", "order": 10},

    # ========== sg_c1_s3 ==========
    {"id": "sg_c1_s3_r001", "subcategory_id": "sg_c1_s3", "name": "تقرير عن مشاركة المدرسة في المبادرات الوطنية (كيوم التأسيس)", "order": 1},
    {"id": "sg_c1_s3_r002", "subcategory_id": "sg_c1_s3", "name": "سجل التعاون مع المؤسسات الحكومية في برامج التوعية", "order": 2},
    {"id": "sg_c1_s3_r003", "subcategory_id": "sg_c1_s3", "name": "تقرير عن تنظيم زيارات طلابية للجهات الحكومية", "order": 3},
    {"id": "sg_c1_s3_r004", "subcategory_id": "sg_c1_s3", "name": "توثيق الشراكة مع وزارة الصحة في برامج الإرشاد الصحي", "order": 4},
    {"id": "sg_c1_s3_r005", "subcategory_id": "sg_c1_s3", "name": "تقرير عن تفعيل الأيام الوطنية والمناسبات الرسمية", "order": 5},
    {"id": "sg_c1_s3_r006", "subcategory_id": "sg_c1_s3", "name": "سجل مشاركة الطلاب في حملات التطوع المجتمعي", "order": 6},
    {"id": "sg_c1_s3_r007", "subcategory_id": "sg_c1_s3", "name": "تقرير عن التنسيق مع الدفاع المدني في برامج السلامة", "order": 7},
    {"id": "sg_c1_s3_r008", "subcategory_id": "sg_c1_s3", "name": "توثيق لقاءات مع مسؤولي المبادرات الوطنية", "order": 8},
    {"id": "sg_c1_s3_r009", "subcategory_id": "sg_c1_s3", "name": "تقرير عن أثر المبادرات الوطنية في تعزيز المواطنة", "order": 9},
    {"id": "sg_c1_s3_r010", "subcategory_id": "sg_c1_s3", "name": "سجل تكريم الطلاب المشاركين في الأنشطة الوطنية", "order": 10},

    # ========== sg_c1_s4 ==========
    {"id": "sg_c1_s4_r001", "subcategory_id": "sg_c1_s4", "name": "تقرير عن تنظيم احتفالية اليوم الوطني لتعزيز الانتماء", "order": 1},
    {"id": "sg_c1_s4_r002", "subcategory_id": "sg_c1_s4", "name": "سجل مسابقات ثقافية عن تاريخ المملكة وإنجازاتها", "order": 2},
    {"id": "sg_c1_s4_r003", "subcategory_id": "sg_c1_s4", "name": "تقرير عن برنامج 'الولاء والانتماء' في الإذاعة المدرسية", "order": 3},
    {"id": "sg_c1_s4_r004", "subcategory_id": "sg_c1_s4", "name": "توثيق ورش عمل عن التضحية والفداء للمملكة", "order": 4},
    {"id": "sg_c1_s4_r005", "subcategory_id": "sg_c1_s4", "name": "تقرير عن رحلات مدرسية للمعالم الوطنية", "order": 5},
    {"id": "sg_c1_s4_r006", "subcategory_id": "sg_c1_s4", "name": "سجل محاضرات عن فضل القيادة وواجبنا نحو الوطن", "order": 6},
    {"id": "sg_c1_s4_r007", "subcategory_id": "sg_c1_s4", "name": "تقرير عن مسابقة 'أنا السعودي' في الرسم والمقال", "order": 7},
    {"id": "sg_c1_s4_r008", "subcategory_id": "sg_c1_s4", "name": "توثيق زيارات للمراكز الوطنية كالدرعية", "order": 8},
    {"id": "sg_c1_s4_r009", "subcategory_id": "sg_c1_s4", "name": "تقرير عن تفعيل برامج الأمن الفكري في المدرسة", "order": 9},
    {"id": "sg_c1_s4_r010", "subcategory_id": "sg_c1_s4", "name": "سجل إنتاج مطويات وملصقات عن حب الوطن", "order": 10},

    # ========== sg_c1_s5 ==========
    {"id": "sg_c1_s5_r001", "subcategory_id": "sg_c1_s5", "name": "تقرير عن التزام المدرسة باللوائح والإجراءات الداخلية", "order": 1},
    {"id": "sg_c1_s5_r002", "subcategory_id": "sg_c1_s5", "name": "سجل تحديث السياسات وفق القوانين المحلية والدولية", "order": 2},
    {"id": "sg_c1_s5_r003", "subcategory_id": "sg_c1_s5", "name": "تقرير عن تدريب الموظفين على القوانين المنظمة للعمل", "order": 3},
    {"id": "sg_c1_s5_r004", "subcategory_id": "sg_c1_s5", "name": "توثيق الامتثال للوائح الصحة والسلامة المهنية", "order": 4},
    {"id": "sg_c1_s5_r005", "subcategory_id": "sg_c1_s5", "name": "تقرير عن تطبيق لائحة حقوق الطفل في المدرسة", "order": 5},
    {"id": "sg_c1_s5_r006", "subcategory_id": "sg_c1_s5", "name": "سجل متابعة التعديلات على الأنظمة التعليمية", "order": 6},
    {"id": "sg_c1_s5_r007", "subcategory_id": "sg_c1_s5", "name": "تقرير عن سياسات مكافحة التحرش والتمييز", "order": 7},
    {"id": "sg_c1_s5_r008", "subcategory_id": "sg_c1_s5", "name": "توثيق التعامل مع الهيئات الرقابية", "order": 8},
    {"id": "sg_c1_s5_r009", "subcategory_id": "sg_c1_s5", "name": "تقرير عن مراجعة السياسات بما يتوافق مع رؤية 2030", "order": 9},
    {"id": "sg_c1_s5_r010", "subcategory_id": "sg_c1_s5", "name": "سجل الإجراءات التصحيحية عند مخالفة اللوائح", "order": 10},

    # ========== sg_c2_s1 ==========
    {"id": "sg_c2_s1_r001", "subcategory_id": "sg_c2_s1", "name": "تقرير عن حضور المؤتمر السنوي للتوجيه والإرشاد", "order": 1},
    {"id": "sg_c2_s1_r002", "subcategory_id": "sg_c2_s1", "name": "سجل المشاركة في الندوات التربوية عن الصحة النفسية", "order": 2},
    {"id": "sg_c2_s1_r003", "subcategory_id": "sg_c2_s1", "name": "تقرير عن الاستفادة من أوراق العمل في المؤتمرات", "order": 3},
    {"id": "sg_c2_s1_r004", "subcategory_id": "sg_c2_s1", "name": "توثيق شهادات حضور المؤتمرات التعليمية", "order": 4},
    {"id": "sg_c2_s1_r005", "subcategory_id": "sg_c2_s1", "name": "تقرير عن تطبيق مخرجات المؤتمر في المدرسة", "order": 5},
    {"id": "sg_c2_s1_r006", "subcategory_id": "sg_c2_s1", "name": "سجل المشاركة في المؤتمرات الافتراضية", "order": 6},
    {"id": "sg_c2_s1_r007", "subcategory_id": "sg_c2_s1", "name": "تقرير عن ملخص لأهم التوصيات من الندوات", "order": 7},
    {"id": "sg_c2_s1_r008", "subcategory_id": "sg_c2_s1", "name": "توثيق عرض تجارب ناجحة من المؤتمرات", "order": 8},
    {"id": "sg_c2_s1_r009", "subcategory_id": "sg_c2_s1", "name": "تقرير عن التواصل مع خبراء في المؤتمرات", "order": 9},
    {"id": "sg_c2_s1_r010", "subcategory_id": "sg_c2_s1", "name": "سجل الإفادة من الأبحاث المقدمة في المؤتمرات", "order": 10},

    # ========== sg_c2_s2 ==========
    {"id": "sg_c2_s2_r001", "subcategory_id": "sg_c2_s2", "name": "تقرير عن المشاركة في ورش عمل مهارات الإرشاد", "order": 1},
    {"id": "sg_c2_s2_r002", "subcategory_id": "sg_c2_s2", "name": "سجل حضور الدورات التدريبية المتخصصة", "order": 2},
    {"id": "sg_c2_s2_r003", "subcategory_id": "sg_c2_s2", "name": "تقرير عن فعالية أنشطة المجتمع المهني", "order": 3},
    {"id": "sg_c2_s2_r004", "subcategory_id": "sg_c2_s2", "name": "توثيق شهادات حضور ورش العمل", "order": 4},
    {"id": "sg_c2_s2_r005", "subcategory_id": "sg_c2_s2", "name": "تقرير عن تطبيق مهارات جديدة من ورش العمل", "order": 5},
    {"id": "sg_c2_s2_r006", "subcategory_id": "sg_c2_s2", "name": "سجل المشاركة في مجموعات النقاش المهنية", "order": 6},
    {"id": "sg_c2_s2_r007", "subcategory_id": "sg_c2_s2", "name": "تقرير عن استضافة مدربين متخصصين للمدرسة", "order": 7},
    {"id": "sg_c2_s2_r008", "subcategory_id": "sg_c2_s2", "name": "توثيق المشاركة في اللقاءات الشهرية للمرشدين", "order": 8},
    {"id": "sg_c2_s2_r009", "subcategory_id": "sg_c2_s2", "name": "تقرير عن تبادل الخبرات مع مدارس أخرى", "order": 9},
    {"id": "sg_c2_s2_r010", "subcategory_id": "sg_c2_s2", "name": "سجل الانضمام للجمعيات المهنية", "order": 10},

    # ========== sg_c2_s3 ==========
    {"id": "sg_c2_s3_r001", "subcategory_id": "sg_c2_s3", "name": "تقرير عن برنامج دعم المعلمين الجدد في الإرشاد", "order": 1},
    {"id": "sg_c2_s3_r002", "subcategory_id": "sg_c2_s3", "name": "سجل اجتماعات الإرشاد والتوجيه مع المعلمين", "order": 2},
    {"id": "sg_c2_s3_r003", "subcategory_id": "sg_c2_s3", "name": "تقرير عن تقديم استشارات للمعلمين في التعامل مع الطلاب", "order": 3},
    {"id": "sg_c2_s3_r004", "subcategory_id": "sg_c2_s3", "name": "توثيق برنامج التوجيه والإرشاد للمعلمين المستجدين", "order": 4},
    {"id": "sg_c2_s3_r005", "subcategory_id": "sg_c2_s3", "name": "تقرير عن أثر الإرشاد على أداء المعلمين", "order": 5},
    {"id": "sg_c2_s3_r006", "subcategory_id": "sg_c2_s3", "name": "سجل ورش عمل للمعلمين عن اكتشاف الحالات", "order": 6},
    {"id": "sg_c2_s3_r007", "subcategory_id": "sg_c2_s3", "name": "تقرير عن توجيه المعلمين في تعديل السلوك", "order": 7},
    {"id": "sg_c2_s3_r008", "subcategory_id": "sg_c2_s3", "name": "توثيق لقاءات فردية مع المعلمين", "order": 8},
    {"id": "sg_c2_s3_r009", "subcategory_id": "sg_c2_s3", "name": "تقرير عن دعم المعلمين في التواصل مع أولياء الأمور", "order": 9},
    {"id": "sg_c2_s3_r010", "subcategory_id": "sg_c2_s3", "name": "سجل تقييم برنامج دعم المعلمين الجدد", "order": 10},

    # ========== sg_c2_s4 ==========
    {"id": "sg_c2_s4_r001", "subcategory_id": "sg_c2_s4", "name": "تقرير عن إطلاق مبادرة تعليمية لتحسين البيئة الصفية", "order": 1},
    {"id": "sg_c2_s4_r002", "subcategory_id": "sg_c2_s4", "name": "سجل مبادرات تعزيز الصحة النفسية للطلاب", "order": 2},
    {"id": "sg_c2_s4_r003", "subcategory_id": "sg_c2_s4", "name": "تقرير عن أثر المبادرات التعليمية على جودة التعليم", "order": 3},
    {"id": "sg_c2_s4_r004", "subcategory_id": "sg_c2_s4", "name": "توثيق شراكات مجتمعية لإطلاق مبادرات", "order": 4},
    {"id": "sg_c2_s4_r005", "subcategory_id": "sg_c2_s4", "name": "تقرير عن مبادرة 'مدرستي ملاذي الآمن'", "order": 5},
    {"id": "sg_c2_s4_r006", "subcategory_id": "sg_c2_s4", "name": "سجل مشاركة الطلاب في المبادرات", "order": 6},
    {"id": "sg_c2_s4_r007", "subcategory_id": "sg_c2_s4", "name": "تقرير عن مبادرة تعزيز القراءة الحرة", "order": 7},
    {"id": "sg_c2_s4_r008", "subcategory_id": "sg_c2_s4", "name": "توثيق قصص نجاح المبادرات التعليمية", "order": 8},
    {"id": "sg_c2_s4_r009", "subcategory_id": "sg_c2_s4", "name": "تقرير عن نشر ثقافة المبادرات بين المعلمين", "order": 9},
    {"id": "sg_c2_s4_r010", "subcategory_id": "sg_c2_s4", "name": "سجل تقييم أثر المبادرات على التحصيل", "order": 10},

    # ========== sg_c3_s1 ==========
    {"id": "sg_c3_s1_r001", "subcategory_id": "sg_c3_s1", "name": "تقرير عن سجل التواصل الشهري مع أولياء الأمور", "order": 1},
    {"id": "sg_c3_s1_r002", "subcategory_id": "sg_c3_s1", "name": "توثيق المكالمات الهاتفية مع أولياء الأمور", "order": 2},
    {"id": "sg_c3_s1_r003", "subcategory_id": "sg_c3_s1", "name": "سجل زيارات أولياء الأمور لمكتب الإرشاد", "order": 3},
    {"id": "sg_c3_s1_r004", "subcategory_id": "sg_c3_s1", "name": "تقرير عن أثر التواصل على متابعة أولياء الأمور", "order": 4},
    {"id": "sg_c3_s1_r005", "subcategory_id": "sg_c3_s1", "name": "توثيق الردود على استفسارات أولياء الأمور", "order": 5},
    {"id": "sg_c3_s1_r006", "subcategory_id": "sg_c3_s1", "name": "سجل إشعارات أولياء الأمور بسلوك الطلاب", "order": 6},
    {"id": "sg_c3_s1_r007", "subcategory_id": "sg_c3_s1", "name": "تقرير عن إحصائيات التواصل الأسبوعي", "order": 7},
    {"id": "sg_c3_s1_r008", "subcategory_id": "sg_c3_s1", "name": "توثيق التواصل مع أولياء الأمور عبر البريد الإلكتروني", "order": 8},
    {"id": "sg_c3_s1_r009", "subcategory_id": "sg_c3_s1", "name": "سجل استقبال شكاوى وملاحظات أولياء الأمور", "order": 9},
    {"id": "sg_c3_s1_r010", "subcategory_id": "sg_c3_s1", "name": "تقرير عن رضا أولياء الأمور عن التواصل", "order": 10},

    # ========== sg_c3_s2 ==========
    {"id": "sg_c3_s2_r001", "subcategory_id": "sg_c3_s2", "name": "تقرير عن اجتماعات مع أولياء الأمور لمتابعة التحصيل", "order": 1},
    {"id": "sg_c3_s2_r002", "subcategory_id": "sg_c3_s2", "name": "سجل مناقشة نتائج الاختبارات مع أولياء الأمور", "order": 2},
    {"id": "sg_c3_s2_r003", "subcategory_id": "sg_c3_s2", "name": "تقرير عن اجتماعات تحسين سلوك الطالب", "order": 3},
    {"id": "sg_c3_s2_r004", "subcategory_id": "sg_c3_s2", "name": "توثيق محاضر اجتماعات أولياء الأمور", "order": 4},
    {"id": "sg_c3_s2_r005", "subcategory_id": "sg_c3_s2", "name": "تقرير عن أثر الاجتماعات على أداء الطلاب", "order": 5},
    {"id": "sg_c3_s2_r006", "subcategory_id": "sg_c3_s2", "name": "سجل اجتماعات مع أولياء أمور المتفوقين", "order": 6},
    {"id": "sg_c3_s2_r007", "subcategory_id": "sg_c3_s2", "name": "تقرير عن اجتماعات مع أولياء أمور المتعثرين", "order": 7},
    {"id": "sg_c3_s2_r008", "subcategory_id": "sg_c3_s2", "name": "توثيق توصيات اجتماعات أولياء الأمور", "order": 8},
    {"id": "sg_c3_s2_r009", "subcategory_id": "sg_c3_s2", "name": "تقرير عن متابعة تنفيذ توصيات الاجتماعات", "order": 9},
    {"id": "sg_c3_s2_r010", "subcategory_id": "sg_c3_s2", "name": "سجل استبانات رضا أولياء الأمور عن الاجتماعات", "order": 10},

    # ========== sg_c3_s3 ==========
    {"id": "sg_c3_s3_r001", "subcategory_id": "sg_c3_s3", "name": "تقرير عن تنظيم اجتماعات دورية مع أولياء الأمور", "order": 1},
    {"id": "sg_c3_s3_r002", "subcategory_id": "sg_c3_s3", "name": "سجل جدول الاجتماعات الفصلية لأولياء الأمور", "order": 2},
    {"id": "sg_c3_s3_r003", "subcategory_id": "sg_c3_s3", "name": "تقرير عن مناقشة تقدم الطلاب في الاجتماعات", "order": 3},
    {"id": "sg_c3_s3_r004", "subcategory_id": "sg_c3_s3", "name": "توثيق حضور أولياء الأمور للاجتماعات", "order": 4},
    {"id": "sg_c3_s3_r005", "subcategory_id": "sg_c3_s3", "name": "تقرير عن موضوعات الاجتماعات الدورية", "order": 5},
    {"id": "sg_c3_s3_r006", "subcategory_id": "sg_c3_s3", "name": "سجل محاضر اجتماعات مجلس الآباء", "order": 6},
    {"id": "sg_c3_s3_r007", "subcategory_id": "sg_c3_s3", "name": "تقرير عن توصيات الاجتماعات الدورية", "order": 7},
    {"id": "sg_c3_s3_r008", "subcategory_id": "sg_c3_s3", "name": "توثيق تفعيل مقترحات أولياء الأمور", "order": 8},
    {"id": "sg_c3_s3_r009", "subcategory_id": "sg_c3_s3", "name": "تقرير عن أثر الاجتماعات على متابعة الأسرة", "order": 9},
    {"id": "sg_c3_s3_r010", "subcategory_id": "sg_c3_s3", "name": "سجل إشعارات دعوة أولياء الأمور للاجتماعات", "order": 10},

    # ========== sg_c3_s4 ==========
    {"id": "sg_c3_s4_r001", "subcategory_id": "sg_c3_s4", "name": "تقرير عن استخدام تطبيقات التواصل مع أولياء الأمور", "order": 1},
    {"id": "sg_c3_s4_r002", "subcategory_id": "sg_c3_s4", "name": "سجل إرسال الإشعارات عبر البريد الإلكتروني", "order": 2},
    {"id": "sg_c3_s4_r003", "subcategory_id": "sg_c3_s4", "name": "تقرير عن تفعيل المجموعات في واتس آب", "order": 3},
    {"id": "sg_c3_s4_r004", "subcategory_id": "sg_c3_s4", "name": "توثيق استخدام نظام نور للتواصل", "order": 4},
    {"id": "sg_c3_s4_r005", "subcategory_id": "sg_c3_s4", "name": "تقرير عن أثر وسائل التواصل على سرعة الاستجابة", "order": 5},
    {"id": "sg_c3_s4_r006", "subcategory_id": "sg_c3_s4", "name": "سجل نشرات دورية لأولياء الأمور", "order": 6},
    {"id": "sg_c3_s4_r007", "subcategory_id": "sg_c3_s4", "name": "تقرير عن استطلاعات الرأي الإلكترونية", "order": 7},
    {"id": "sg_c3_s4_r008", "subcategory_id": "sg_c3_s4", "name": "توثيق منصات التواصل المدرسية", "order": 8},
    {"id": "sg_c3_s4_r009", "subcategory_id": "sg_c3_s4", "name": "تقرير عن تدريب أولياء الأمور على التطبيقات", "order": 9},
    {"id": "sg_c3_s4_r010", "subcategory_id": "sg_c3_s4", "name": "سجل إحصائيات استخدام وسائل التواصل", "order": 10},

    # ========== sg_c3_s5 ==========
    {"id": "sg_c3_s5_r001", "subcategory_id": "sg_c3_s5", "name": "تقرير عن الاستجابة لملاحظات أولياء الأمور", "order": 1},
    {"id": "sg_c3_s5_r002", "subcategory_id": "sg_c3_s5", "name": "سجل مخاوف أولياء الأمور وآليات معالجتها", "order": 2},
    {"id": "sg_c3_s5_r003", "subcategory_id": "sg_c3_s5", "name": "تقرير عن العمل التعاوني مع أولياء الأمور لحل المشكلات", "order": 3},
    {"id": "sg_c3_s5_r004", "subcategory_id": "sg_c3_s5", "name": "توثيق اجتماعات الاستماع لأولياء الأمور", "order": 4},
    {"id": "sg_c3_s5_r005", "subcategory_id": "sg_c3_s5", "name": "تقرير عن رضا أولياء الأمور عن معالجة المخاوف", "order": 5},
    {"id": "sg_c3_s5_r006", "subcategory_id": "sg_c3_s5", "name": "سجل متابعة تنفيذ حلول مشكلات أولياء الأمور", "order": 6},
    {"id": "sg_c3_s5_r007", "subcategory_id": "sg_c3_s5", "name": "تقرير عن استبيان قياس رضا أولياء الأمور", "order": 7},
    {"id": "sg_c3_s5_r008", "subcategory_id": "sg_c3_s5", "name": "توثيق نماذج معالجة الشكاوى", "order": 8},
    {"id": "sg_c3_s5_r009", "subcategory_id": "sg_c3_s5", "name": "تقرير عن تحسين العلاقة مع أولياء الأمور", "order": 9},
    {"id": "sg_c3_s5_r010", "subcategory_id": "sg_c3_s5", "name": "سجل قصص نجاح في التعاون مع أولياء الأمور", "order": 10},

    # ========== sg_c4_s1 ==========
    {"id": "sg_c4_s1_r001", "subcategory_id": "sg_c4_s1", "name": "تقرير عن برنامج تعزيز الانضباط المدرسي", "order": 1},
    {"id": "sg_c4_s1_r002", "subcategory_id": "sg_c4_s1", "name": "سجل تطبيق لائحة السلوك والمواظبة", "order": 2},
    {"id": "sg_c4_s1_r003", "subcategory_id": "sg_c4_s1", "name": "تقرير عن ممارسات تعزيز السلوك الإيجابي", "order": 3},
    {"id": "sg_c4_s1_r004", "subcategory_id": "sg_c4_s1", "name": "توثيق حصص توعوية عن الانضباط", "order": 4},
    {"id": "sg_c4_s1_r005", "subcategory_id": "sg_c4_s1", "name": "تقرير عن انخفاض حالات المخالفات بعد البرامج", "order": 5},
    {"id": "sg_c4_s1_r006", "subcategory_id": "sg_c4_s1", "name": "سجل تكريم الطلاب المنضبطين", "order": 6},
    {"id": "sg_c4_s1_r007", "subcategory_id": "sg_c4_s1", "name": "تقرير عن برنامج 'انضباطي مسؤوليتي'", "order": 7},
    {"id": "sg_c4_s1_r008", "subcategory_id": "sg_c4_s1", "name": "توثيق ورش عمل للطلاب عن قواعد الانضباط", "order": 8},
    {"id": "sg_c4_s1_r009", "subcategory_id": "sg_c4_s1", "name": "تقرير عن دور الإذاعة المدرسية في تعزيز الانضباط", "order": 9},
    {"id": "sg_c4_s1_r010", "subcategory_id": "sg_c4_s1", "name": "سجل متابعة حالات عدم الانضباط", "order": 10},

    # ========== sg_c5_s1 ==========
    {"id": "sg_c5_s1_r001", "subcategory_id": "sg_c5_s1", "name": "تقرير عن برنامج تحفيز دافعية التعلم للطلاب", "order": 1},
    {"id": "sg_c5_s1_r002", "subcategory_id": "sg_c5_s1", "name": "سجل أنشطة تعزيز حب الاستطلاع العلمي", "order": 2},
    {"id": "sg_c5_s1_r003", "subcategory_id": "sg_c5_s1", "name": "تقرير عن برنامج 'أتعلم لأبدع'", "order": 3},
    {"id": "sg_c5_s1_r004", "subcategory_id": "sg_c5_s1", "name": "توثيق مسابقات تحفيزية للتعلم", "order": 4},
    {"id": "sg_c5_s1_r005", "subcategory_id": "sg_c5_s1", "name": "تقرير عن أثر البرامج على دافعية الطلاب", "order": 5},
    {"id": "sg_c5_s1_r006", "subcategory_id": "sg_c5_s1", "name": "سجل ورش عمل عن استراتيجيات التعلم النشط", "order": 6},
    {"id": "sg_c5_s1_r007", "subcategory_id": "sg_c5_s1", "name": "تقرير عن برنامج تعزيز الثقة بالقدرات الذهنية", "order": 7},
    {"id": "sg_c5_s1_r008", "subcategory_id": "sg_c5_s1", "name": "توثيق قصص نجاح لطلاب زادت دافعيتهم", "order": 8},
    {"id": "sg_c5_s1_r009", "subcategory_id": "sg_c5_s1", "name": "تقرير عن ملصقات تحفيزية في الفصول", "order": 9},
    {"id": "sg_c5_s1_r010", "subcategory_id": "sg_c5_s1", "name": "سجل استبيان قياس الدافعية للتعلم", "order": 10},

    # ========== sg_c5_s2 ==========
    {"id": "sg_c5_s2_r001", "subcategory_id": "sg_c5_s2", "name": "تقرير عن التنويع في أساليب تنفيذ البرامج", "order": 1},
    {"id": "sg_c5_s2_r002", "subcategory_id": "sg_c5_s2", "name": "سجل استخدام الألعاب التعليمية في البرامج", "order": 2},
    {"id": "sg_c5_s2_r003", "subcategory_id": "sg_c5_s2", "name": "تقرير عن توظيف التكنولوجيا في البرامج", "order": 3},
    {"id": "sg_c5_s2_r004", "subcategory_id": "sg_c5_s2", "name": "توثيق أنشطة تفاعلية لتنمية المهارات", "order": 4},
    {"id": "sg_c5_s2_r005", "subcategory_id": "sg_c5_s2", "name": "تقرير عن استراتيجيات التعلم باللعب", "order": 5},
    {"id": "sg_c5_s2_r006", "subcategory_id": "sg_c5_s2", "name": "سجل استخدام القصص في البرامج التربوية", "order": 6},
    {"id": "sg_c5_s2_r007", "subcategory_id": "sg_c5_s2", "name": "تقرير عن تنفيذ برامج بالتعلم التعاوني", "order": 7},
    {"id": "sg_c5_s2_r008", "subcategory_id": "sg_c5_s2", "name": "توثيق مسرحيات تعليمية هادفة", "order": 8},
    {"id": "sg_c5_s2_r009", "subcategory_id": "sg_c5_s2", "name": "تقرير عن توظيف الفنون في البرامج", "order": 9},
    {"id": "sg_c5_s2_r010", "subcategory_id": "sg_c5_s2", "name": "سجل تقييم فعالية الأساليب المستخدمة", "order": 10},

    # ========== sg_c6_s1 ==========
    {"id": "sg_c6_s1_r001", "subcategory_id": "sg_c6_s1", "name": "تقرير عن تصميم خطة البرامج السنوية", "order": 1},
    {"id": "sg_c6_s1_r002", "subcategory_id": "sg_c6_s1", "name": "سجل تحليل واقع العمل لبناء الخطة", "order": 2},
    {"id": "sg_c6_s1_r003", "subcategory_id": "sg_c6_s1", "name": "تقرير عن عناصر الخطة المكتملة", "order": 3},
    {"id": "sg_c6_s1_r004", "subcategory_id": "sg_c6_s1", "name": "توثيق مؤشرات قياس الخطة", "order": 4},
    {"id": "sg_c6_s1_r005", "subcategory_id": "sg_c6_s1", "name": "تقرير عن مشاركة المعلمين في إعداد الخطة", "order": 5},
    {"id": "sg_c6_s1_r006", "subcategory_id": "sg_c6_s1", "name": "سجل اعتماد الخطة من الإدارة", "order": 6},
    {"id": "sg_c6_s1_r007", "subcategory_id": "sg_c6_s1", "name": "تقرير عن توزيع البرامج على الفصول الدراسية", "order": 7},
    {"id": "sg_c6_s1_r008", "subcategory_id": "sg_c6_s1", "name": "توثيق مراجعة الخطة وتحديثها", "order": 8},
    {"id": "sg_c6_s1_r009", "subcategory_id": "sg_c6_s1", "name": "تقرير عن مدى تحقيق الخطة لأهدافها", "order": 9},
    {"id": "sg_c6_s1_r010", "subcategory_id": "sg_c6_s1", "name": "سجل تغذية راجعة حول الخطة من المعنيين", "order": 10},

    # ========== sg_c7_s1 ==========
    {"id": "sg_c7_s1_r001", "subcategory_id": "sg_c7_s1", "name": "تقرير عن تصنيف حالات الطلاب السلوكية", "order": 1},
    {"id": "sg_c7_s1_r002", "subcategory_id": "sg_c7_s1", "name": "سجل تقديم برامج داعمة لكل فئة", "order": 2},
    {"id": "sg_c7_s1_r003", "subcategory_id": "sg_c7_s1", "name": "تقرير عن برامج للطلاب الموهوبين", "order": 3},
    {"id": "sg_c7_s1_r004", "subcategory_id": "sg_c7_s1", "name": "توثيق برامج لذوي صعوبات التعلم", "order": 4},
    {"id": "sg_c7_s1_r005", "subcategory_id": "sg_c7_s1", "name": "تقرير عن برامج للطلاب المضطربين سلوكياً", "order": 5},
    {"id": "sg_c7_s1_r006", "subcategory_id": "sg_c7_s1", "name": "سجل متابعة البرامج حسب التصنيف", "order": 6},
    {"id": "sg_c7_s1_r007", "subcategory_id": "sg_c7_s1", "name": "تقرير عن برامج الدعم النفسي", "order": 7},
    {"id": "sg_c7_s1_r008", "subcategory_id": "sg_c7_s1", "name": "توثيق معايير تصنيف الحالات", "order": 8},
    {"id": "sg_c7_s1_r009", "subcategory_id": "sg_c7_s1", "name": "تقرير عن تحديث تصنيف الحالات", "order": 9},
    {"id": "sg_c7_s1_r010", "subcategory_id": "sg_c7_s1", "name": "سجل قياس أثر البرامج على كل فئة", "order": 10},

    # ========== sg_c8_s1 ==========
    {"id": "sg_c8_s1_r001", "subcategory_id": "sg_c8_s1", "name": "تقرير عن برنامج تعزيز القيم الإيجابية", "order": 1},
    {"id": "sg_c8_s1_r002", "subcategory_id": "sg_c8_s1", "name": "سجل توعية الطلاب بالصدق والأمانة", "order": 2},
    {"id": "sg_c8_s1_r003", "subcategory_id": "sg_c8_s1", "name": "تقرير عن تعزيز قيمة الاحترام", "order": 3},
    {"id": "sg_c8_s1_r004", "subcategory_id": "sg_c8_s1", "name": "توثيق إذاعات مدرسية عن القيم", "order": 4},
    {"id": "sg_c8_s1_r005", "subcategory_id": "sg_c8_s1", "name": "تقرير عن أثر البرامج على سلوك الطلاب", "order": 5},
    {"id": "sg_c8_s1_r006", "subcategory_id": "sg_c8_s1", "name": "سجل ورش عمل للمعلمين عن تعزيز القيم", "order": 6},
    {"id": "sg_c8_s1_r007", "subcategory_id": "sg_c8_s1", "name": "تقرير عن مسابقات في القيم والسلوك", "order": 7},
    {"id": "sg_c8_s1_r008", "subcategory_id": "sg_c8_s1", "name": "توثيق أنشطة لاصفية لتعزيز القيم", "order": 8},
    {"id": "sg_c8_s1_r009", "subcategory_id": "sg_c8_s1", "name": "تقرير عن تكريم الطلاب المتمثلين بالقيم", "order": 9},
    {"id": "sg_c8_s1_r010", "subcategory_id": "sg_c8_s1", "name": "سجل استبيان قياس القيم لدى الطلاب", "order": 10},

    # ========== sg_c9_s1 ==========
    {"id": "sg_c9_s1_r001", "subcategory_id": "sg_c9_s1", "name": "تقرير عن استخدام المقابلة في التدخل النفسي", "order": 1},
    {"id": "sg_c9_s1_r002", "subcategory_id": "sg_c9_s1", "name": "سجل دراسة حالات نفسية واجتماعية", "order": 2},
    {"id": "sg_c9_s1_r003", "subcategory_id": "sg_c9_s1", "name": "تقرير عن التوجيه الجمعي للطلاب", "order": 3},
    {"id": "sg_c9_s1_r004", "subcategory_id": "sg_c9_s1", "name": "توثيق الرعاية الطلابية للحالات", "order": 4},
    {"id": "sg_c9_s1_r005", "subcategory_id": "sg_c9_s1", "name": "تقرير عن تحويل الحالات للجهات المختصة", "order": 5},
    {"id": "sg_c9_s1_r006", "subcategory_id": "sg_c9_s1", "name": "سجل استخدام استراتيجيات وقائية", "order": 6},
    {"id": "sg_c9_s1_r007", "subcategory_id": "sg_c9_s1", "name": "تقرير عن برامج الحد من المشكلات النفسية", "order": 7},
    {"id": "sg_c9_s1_r008", "subcategory_id": "sg_c9_s1", "name": "توثيق حالات تمت معالجتها", "order": 8},
    {"id": "sg_c9_s1_r009", "subcategory_id": "sg_c9_s1", "name": "تقرير عن أثر التدخلات على استقرار الطلاب", "order": 9},
    {"id": "sg_c9_s1_r010", "subcategory_id": "sg_c9_s1", "name": "سجل متابعة الحالات المحولة", "order": 10},

    # ========== sg_c9_s2 ==========
    {"id": "sg_c9_s2_r001", "subcategory_id": "sg_c9_s2", "name": "تقرير عن جلسات التدخل الفردي للطلاب", "order": 1},
    {"id": "sg_c9_s2_r002", "subcategory_id": "sg_c9_s2", "name": "سجل برامج التدخل الجمعي", "order": 2},
    {"id": "sg_c9_s2_r003", "subcategory_id": "sg_c9_s2", "name": "تقرير عن استخدام المقابلات التشخيصية", "order": 3},
    {"id": "sg_c9_s2_r004", "subcategory_id": "sg_c9_s2", "name": "توثيق دراسة الحالة الشاملة", "order": 4},
    {"id": "sg_c9_s2_r005", "subcategory_id": "sg_c9_s2", "name": "تقرير عن أثر التدخل الجمعي على الفئة المستهدفة", "order": 5},
    {"id": "sg_c9_s2_r006", "subcategory_id": "sg_c9_s2", "name": "سجل لقاءات فردية أسبوعية", "order": 6},
    {"id": "sg_c9_s2_r007", "subcategory_id": "sg_c9_s2", "name": "تقرير عن جلسات جماعية لإدارة الغضب", "order": 7},
    {"id": "sg_c9_s2_r008", "subcategory_id": "sg_c9_s2", "name": "توثيق خطط التدخل الفردي", "order": 8},
    {"id": "sg_c9_s2_r009", "subcategory_id": "sg_c9_s2", "name": "تقرير عن نتائج التوجيه الجمعي", "order": 9},
    {"id": "sg_c9_s2_r010", "subcategory_id": "sg_c9_s2", "name": "سجل تقييم استراتيجيات التدخل", "order": 10},

    # ========== sg_c9_s3 ==========
    {"id": "sg_c9_s3_r001", "subcategory_id": "sg_c9_s3", "name": "تقرير عن برامج الرعاية الطلابية", "order": 1},
    {"id": "sg_c9_s3_r002", "subcategory_id": "sg_c9_s3", "name": "سجل تحويل الحالات للأخصائي النفسي", "order": 2},
    {"id": "sg_c9_s3_r003", "subcategory_id": "sg_c9_s3", "name": "تقرير عن التنسيق مع وحدة الخدمات", "order": 3},
    {"id": "sg_c9_s3_r004", "subcategory_id": "sg_c9_s3", "name": "توثيق حالات تم تحويلها لجهات متخصصة", "order": 4},
    {"id": "sg_c9_s3_r005", "subcategory_id": "sg_c9_s3", "name": "تقرير عن متابعة الحالات بعد التحويل", "order": 5},
    {"id": "sg_c9_s3_r006", "subcategory_id": "sg_c9_s3", "name": "سجل شراكات مع مراكز الإرشاد", "order": 6},
    {"id": "sg_c9_s3_r007", "subcategory_id": "sg_c9_s3", "name": "تقرير عن إجراءات التحويل", "order": 7},
    {"id": "sg_c9_s3_r008", "subcategory_id": "sg_c9_s3", "name": "توثيق نماذج الإحالة", "order": 8},
    {"id": "sg_c9_s3_r009", "subcategory_id": "sg_c9_s3", "name": "تقرير عن الاستفادة من الجهات الخارجية", "order": 9},
    {"id": "sg_c9_s3_r010", "subcategory_id": "sg_c9_s3", "name": "سجل رضا الأسر عن خدمات التحويل", "order": 10},

    # ========== sg_c10_s1 ==========
    {"id": "sg_c10_s1_r001", "subcategory_id": "sg_c10_s1", "name": "تقرير عن تنفيذ برنامج التوجيه المهني", "order": 1},
    {"id": "sg_c10_s1_r002", "subcategory_id": "sg_c10_s1", "name": "سجل توعية الطلاب بالتخصصات الجامعية", "order": 2},
    {"id": "sg_c10_s1_r003", "subcategory_id": "sg_c10_s1", "name": "تقرير عن أيام المهنة في المدرسة", "order": 3},
    {"id": "sg_c10_s1_r004", "subcategory_id": "sg_c10_s1", "name": "توثيق زيارات للجامعات والكليات", "order": 4},
    {"id": "sg_c10_s1_r005", "subcategory_id": "sg_c10_s1", "name": "تقرير عن تطبيق أدلة التوجيه المهني", "order": 5},
    {"id": "sg_c10_s1_r006", "subcategory_id": "sg_c10_s1", "name": "سجل لقاءات مع مختصين مهنيين", "order": 6},
    {"id": "sg_c10_s1_r007", "subcategory_id": "sg_c10_s1", "name": "تقرير عن برنامج التخطيط للمستقبل", "order": 7},
    {"id": "sg_c10_s1_r008", "subcategory_id": "sg_c10_s1", "name": "توثيق مشاركة أولياء الأمور في التوجيه", "order": 8},
    {"id": "sg_c10_s1_r009", "subcategory_id": "sg_c10_s1", "name": "تقرير عن أثر البرامج على اختيارات الطلاب", "order": 9},
    {"id": "sg_c10_s1_r010", "subcategory_id": "sg_c10_s1", "name": "سجل تقييم برامج التوجيه المهني", "order": 10},

    # ========== sg_c10_s2 ==========
    {"id": "sg_c10_s2_r001", "subcategory_id": "sg_c10_s2", "name": "تقرير عن تطبيق مقاييس الميول المهنية", "order": 1},
    {"id": "sg_c10_s2_r002", "subcategory_id": "sg_c10_s2", "name": "سجل اكتشاف قدرات الطلاب", "order": 2},
    {"id": "sg_c10_s2_r003", "subcategory_id": "sg_c10_s2", "name": "تقرير عن تحليل نتائج المقاييس", "order": 3},
    {"id": "sg_c10_s2_r004", "subcategory_id": "sg_c10_s2", "name": "توثيق استخدام مقياس هولاند", "order": 4},
    {"id": "sg_c10_s2_r005", "subcategory_id": "sg_c10_s2", "name": "تقرير عن ربط الميول بالتخصصات", "order": 5},
    {"id": "sg_c10_s2_r006", "subcategory_id": "sg_c10_s2", "name": "سجل جلسات تفسير نتائج المقاييس", "order": 6},
    {"id": "sg_c10_s2_r007", "subcategory_id": "sg_c10_s2", "name": "تقرير عن اتجاهات الطلاب المهنية", "order": 7},
    {"id": "sg_c10_s2_r008", "subcategory_id": "sg_c10_s2", "name": "توثيق تحديث بيانات الميول", "order": 8},
    {"id": "sg_c10_s2_r009", "subcategory_id": "sg_c10_s2", "name": "تقرير عن مقارنة الميول بين الفصول", "order": 9},
    {"id": "sg_c10_s2_r010", "subcategory_id": "sg_c10_s2", "name": "سجل توصيات بناءً على المقاييس", "order": 10},

    # ========== sg_c10_s3 ==========
    {"id": "sg_c10_s3_r001", "subcategory_id": "sg_c10_s3", "name": "تقرير عن توجيه الطلاب للتخصصات المناسبة", "order": 1},
    {"id": "sg_c10_s3_r002", "subcategory_id": "sg_c10_s3", "name": "سجل إرشاد طلاب المسار العلمي والأدبي", "order": 2},
    {"id": "sg_c10_s3_r003", "subcategory_id": "sg_c10_s3", "name": "تقرير عن متابعة اختيارات الطلاب", "order": 3},
    {"id": "sg_c10_s3_r004", "subcategory_id": "sg_c10_s3", "name": "توثيق استشارات فردية حول التخصص", "order": 4},
    {"id": "sg_c10_s3_r005", "subcategory_id": "sg_c10_s3", "name": "تقرير عن توافق التخصص مع الميول", "order": 5},
    {"id": "sg_c10_s3_r006", "subcategory_id": "sg_c10_s3", "name": "سجل ورش عمل عن التخصصات", "order": 6},
    {"id": "sg_c10_s3_r007", "subcategory_id": "sg_c10_s3", "name": "تقرير عن توجيه الطلاب الموهوبين", "order": 7},
    {"id": "sg_c10_s3_r008", "subcategory_id": "sg_c10_s3", "name": "توثيق قصص نجاح في اختيار التخصص", "order": 8},
    {"id": "sg_c10_s3_r009", "subcategory_id": "sg_c10_s3", "name": "تقرير عن التنسيق مع جامعة", "order": 9},
    {"id": "sg_c10_s3_r010", "subcategory_id": "sg_c10_s3", "name": "سجل رضا الطلاب عن التوجيه", "order": 10},

    # ========== sg_c10_s4 ==========
    {"id": "sg_c10_s4_r001", "subcategory_id": "sg_c10_s4", "name": "تقرير عن توعية الطلاب بمفاهيم العمل المهني", "order": 1},
    {"id": "sg_c10_s4_r002", "subcategory_id": "sg_c10_s4", "name": "سجل تدريب الطلاب على مهارات المستقبل", "order": 2},
    {"id": "sg_c10_s4_r003", "subcategory_id": "sg_c10_s4", "name": "تقرير عن برنامج التخطيط المهني", "order": 3},
    {"id": "sg_c10_s4_r004", "subcategory_id": "sg_c10_s4", "name": "توثيق ورش عمل عن ريادة الأعمال", "order": 4},
    {"id": "sg_c10_s4_r005", "subcategory_id": "sg_c10_s4", "name": "تقرير عن تصحيح المفاهيم الخاطئة عن العمل", "order": 5},
    {"id": "sg_c10_s4_r006", "subcategory_id": "sg_c10_s4", "name": "سجل لقاءات مع رواد أعمال", "order": 6},
    {"id": "sg_c10_s4_r007", "subcategory_id": "sg_c10_s4", "name": "تقرير عن مهارات كتابة السيرة الذاتية", "order": 7},
    {"id": "sg_c10_s4_r008", "subcategory_id": "sg_c10_s4", "name": "توثيق محاضرات عن سوق العمل", "order": 8},
    {"id": "sg_c10_s4_r009", "subcategory_id": "sg_c10_s4", "name": "تقرير عن أثر البرامج على التخطيط", "order": 9},
    {"id": "sg_c10_s4_r010", "subcategory_id": "sg_c10_s4", "name": "سجل استبيان الوعي المهني", "order": 10},

    # ========== sg_c11_s1 ==========
    {"id": "sg_c11_s1_r001", "subcategory_id": "sg_c11_s1", "name": "تقرير عن تحليل نتائج الطلاب لتعزيز التفوق", "order": 1},
    {"id": "sg_c11_s1_r002", "subcategory_id": "sg_c11_s1", "name": "سجل برامج دعم المتفوقين", "order": 2},
    {"id": "sg_c11_s1_r003", "subcategory_id": "sg_c11_s1", "name": "تقرير عن تحديد مستويات الطلاب", "order": 3},
    {"id": "sg_c11_s1_r004", "subcategory_id": "sg_c11_s1", "name": "توثيق أنشطة إثرائية للمتفوقين", "order": 4},
    {"id": "sg_c11_s1_r005", "subcategory_id": "sg_c11_s1", "name": "تقرير عن أثر البرامج على التفوق", "order": 5},
    {"id": "sg_c11_s1_r006", "subcategory_id": "sg_c11_s1", "name": "سجل مسابقات للمتفوقين", "order": 6},
    {"id": "sg_c11_s1_r007", "subcategory_id": "sg_c11_s1", "name": "تقرير عن رعاية المتفوقين", "order": 7},
    {"id": "sg_c11_s1_r008", "subcategory_id": "sg_c11_s1", "name": "توثيق شراكات لرعاية المتفوقين", "order": 8},
    {"id": "sg_c11_s1_r009", "subcategory_id": "sg_c11_s1", "name": "تقرير عن تحليل فجوات التفوق", "order": 9},
    {"id": "sg_c11_s1_r010", "subcategory_id": "sg_c11_s1", "name": "سجل تحديث برامج التفوق", "order": 10},

    # ========== sg_c11_s2 ==========
    {"id": "sg_c11_s2_r001", "subcategory_id": "sg_c11_s2", "name": "تقرير عن حفل تكريم المتفوقين", "order": 1},
    {"id": "sg_c11_s2_r002", "subcategory_id": "sg_c11_s2", "name": "سجل تحفيز الطلاب للتفوق", "order": 2},
    {"id": "sg_c11_s2_r003", "subcategory_id": "sg_c11_s2", "name": "تقرير عن برنامج 'مفاتيح التفوق'", "order": 3},
    {"id": "sg_c11_s2_r004", "subcategory_id": "sg_c11_s2", "name": "توثيق مشاركة المتفوقين في تحفيز الآخرين", "order": 4},
    {"id": "sg_c11_s2_r005", "subcategory_id": "sg_c11_s2", "name": "تقرير عن أثر التكريم على دافعية الطلاب", "order": 5},
    {"id": "sg_c11_s2_r006", "subcategory_id": "sg_c11_s2", "name": "سجل لوحة شرف المتفوقين", "order": 6},
    {"id": "sg_c11_s2_r007", "subcategory_id": "sg_c11_s2", "name": "تقرير عن نشر قصص نجاح المتفوقين", "order": 7},
    {"id": "sg_c11_s2_r008", "subcategory_id": "sg_c11_s2", "name": "توثيق جوائز التفوق", "order": 8},
    {"id": "sg_c11_s2_r009", "subcategory_id": "sg_c11_s2", "name": "تقرير عن برامج تحفيزية للمتوسطين", "order": 9},
    {"id": "sg_c11_s2_r010", "subcategory_id": "sg_c11_s2", "name": "سجل استبيان أثر التحفيز", "order": 10},

    # ========== sg_c12_s1 ==========
    {"id": "sg_c12_s1_r001", "subcategory_id": "sg_c12_s1", "name": "تقرير عن تحليل نتائج المتأخرين دراسياً", "order": 1},
    {"id": "sg_c12_s1_r002", "subcategory_id": "sg_c12_s1", "name": "سجل برامج علاجية للمتعثرين", "order": 2},
    {"id": "sg_c12_s1_r003", "subcategory_id": "sg_c12_s1", "name": "تقرير عن تدخلات للمعيدين", "order": 3},
    {"id": "sg_c12_s1_r004", "subcategory_id": "sg_c12_s1", "name": "توثيق حصص تقوية للمتأخرين", "order": 4},
    {"id": "sg_c12_s1_r005", "subcategory_id": "sg_c12_s1", "name": "تقرير عن متابعة تحسن المتأخرين", "order": 5},
    {"id": "sg_c12_s1_r006", "subcategory_id": "sg_c12_s1", "name": "سجل ورش عمل مهارات الدراسة", "order": 6},
    {"id": "sg_c12_s1_r007", "subcategory_id": "sg_c12_s1", "name": "تقرير عن برنامج تحسين التحصيل", "order": 7},
    {"id": "sg_c12_s1_r008", "subcategory_id": "sg_c12_s1", "name": "توثيق تنسيق مع معلمي المواد", "order": 8},
    {"id": "sg_c12_s1_r009", "subcategory_id": "sg_c12_s1", "name": "تقرير عن أثر البرامج على رفع المستوى", "order": 9},
    {"id": "sg_c12_s1_r010", "subcategory_id": "sg_c12_s1", "name": "سجل استبيان رضا الطلاب عن البرامج", "order": 10},

    # ========== sg_c13_s1 ==========
    {"id": "sg_c13_s1_r001", "subcategory_id": "sg_c13_s1", "name": "تقرير عن نشر قواعد السلوك في المدرسة", "order": 1},
    {"id": "sg_c13_s1_r002", "subcategory_id": "sg_c13_s1", "name": "سجل توعية الطلاب بقواعد المواظبة", "order": 2},
    {"id": "sg_c13_s1_r003", "subcategory_id": "sg_c13_s1", "name": "تقرير عن اجتماعات مع أولياء الأمور لقواعد السلوك", "order": 3},
    {"id": "sg_c13_s1_r004", "subcategory_id": "sg_c13_s1", "name": "توثيق توزيع مطويات عن قواعد السلوك", "order": 4},
    {"id": "sg_c13_s1_r005", "subcategory_id": "sg_c13_s1", "name": "تقرير عن مدى التزام الطلاب بالقواعد", "order": 5},
    {"id": "sg_c13_s1_r006", "subcategory_id": "sg_c13_s1", "name": "سجل إذاعات مدرسية عن السلوك", "order": 6},
    {"id": "sg_c13_s1_r007", "subcategory_id": "sg_c13_s1", "name": "تقرير عن مسابقات في قواعد السلوك", "order": 7},
    {"id": "sg_c13_s1_r008", "subcategory_id": "sg_c13_s1", "name": "توثيق ورش عمل لأولياء الأمور", "order": 8},
    {"id": "sg_c13_s1_r009", "subcategory_id": "sg_c13_s1", "name": "تقرير عن نشر القواعد عبر المنصات", "order": 9},
    {"id": "sg_c13_s1_r010", "subcategory_id": "sg_c13_s1", "name": "سجل استبيان وعي الطلاب بالقواعد", "order": 10},
]

# نموذج كتابة التقرير
STUDENT_GUIDE_PROMPT_TEMPLATE = """أنت موجه طلابي متخصص في التوجيه والإرشاد، وتعمل وفق المعايير المهنية المعتمدة لدعم النمو النفسي والتربوي للطلبة.

المطلوب:
- عرض معيار الأداء الوظيفي مع نسبته المئوية.
- عرض التصنيف الفرعي.
- كتابة تقرير مهني يوضح الممارسات والإجراءات المنفذة في هذا الجانب.

التقرير المطلوب: "{report_name}"
وهو يندرج تحت التصنيف الفرعي: "{subcategory_name}"
ضمن المعيار التربوي: "{criterion_name}" ({criterion_percentage})

{subject_line}
{lesson_line}
{grade_line}
{target_line}
{place_line}
{count_line}

ضوابط الكتابة:
- لغة تربوية مهنية.
- إبراز دور الموجه في الوقاية، التدخل، والمتابعة.
- توضيح البرامج الإرشادية الفردية والجمعية عند الحاجة.
- بيان آلية دراسة الحالات وتصنيفها والتعامل معها.
- إبراز أثر الجهود على سلوك الطلبة وتحصيلهم ودافعيتهم.
- الإشارة إلى التعاون مع الأسرة والمعلمين والإدارة.
- توضيح جانب التوثيق وقياس الأثر والتحسين.
- صياغة واقعية تطبيقية من 5–7 أسطر.

دورك كموجه طلابي

1. تعزيز الصحة النفسية والاجتماعية للطلاب بما يدعم تحصيلهم الدراسي ويعزز توافقهم السلوكي داخل البيئة المدرسية.

2. قدمت برنامجًا إرشاديًا يستهدف دعم الطلاب في مهارات إدارة الضغوط وبناء الثقة بالنفس بما ينعكس على مشاركتهم الصفية واستقرارهم الأكاديمي.

3. نفذت جلسات إرشاد فردي وجماعي، ورصدت الحالات ذات الأولوية، ونسقت مع المعلمين لمتابعة الأثر داخل الصف، وتواصلت مع الأسرة عند الحاجة.

4. استخدمت الإرشاد المعرفي السلوكي، والحوار الموجه، وأنشطة التعلم الاجتماعي العاطفي، والتغذية الراجعة المستمرة لتعزيز وعي الطلاب بسلوكهم.

5. تحسن تفاعل الطلاب داخل الحصص، وانخفضت المشكلات السلوكية البسيطة، وظهر أثر إيجابي على دافعية التعلم والتواصل مع المعلمين.

6. الحاجة إلى توسيع نطاق البرامج الوقائية لتشمل جميع الصفوف، وتعزيز أدوات قياس الأثر لضمان استدامة التحسن السلوكي.

7. أوصي بإدماج مهارات التعلم الاجتماعي ضمن الخطة المدرسية، وتكثيف الشراكة مع المعلمين لرصد المؤشرات المبكرة، وتنظيم ورش توعوية لأولياء الأمور.

**الحقول المطلوبة:**
1. الهدف التربوي
2. نبذة مختصرة
3. إجراءات التنفيذ
4. الاستراتيجيات المستخدمة
5. نقاط القوة
6. نقاط التحسين
7. التوصيات

يرجى تقديم الإجابة باللغة العربية الفصحى، وتنظيمها بحيث يكون كل حقل في سطر منفصل يبدأ برقمه فقط دون ذكر العنوان."""