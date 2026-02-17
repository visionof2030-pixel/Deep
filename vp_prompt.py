# vp_prompt.py

VP_CRITERIA = [
    {"id": "vp_c1", "name": "تنظيم وإدارة العمل المدرسي", "weight": "10%", "order": 1},
    {"id": "vp_c2", "name": "متابعة الانضباط المدرسي والسلوك الطلابي", "weight": "10%", "order": 2},
    {"id": "vp_c3", "name": "الإشراف على تنفيذ الخطط والبرامج المدرسية", "weight": "10%", "order": 3},
    {"id": "vp_c4", "name": "تقييم أداء المعلمين وتحفيزهم", "weight": "10%", "order": 4},
    {"id": "vp_c5", "name": "التواصل مع أولياء الأمور والمجتمع", "weight": "10%", "order": 5}
]

VP_SUBCATEGORIES = [
    # vp_c1
    {"id": "vp_c1_s1", "criterion_id": "vp_c1", "name": "توزيع المهام والإشراف على المنادرين", "order": 1},
    {"id": "vp_c1_s2", "criterion_id": "vp_c1", "name": "تنظيم جداول الحصص والإشراف اليومي", "order": 2},
    {"id": "vp_c1_s3", "criterion_id": "vp_c1", "name": "متابعة تنفيذ خطط الإخلاء والسلامة", "order": 3},
    {"id": "vp_c1_s4", "criterion_id": "vp_c1", "name": "إدارة الموارد المدرسية والصيانة", "order": 4},
    {"id": "vp_c1_s5", "criterion_id": "vp_c1", "name": "تنظيم سجلات الحضور والانصراف", "order": 5},
    # vp_c2
    {"id": "vp_c2_s1", "criterion_id": "vp_c2", "name": "متابعة انضباط الطلاب في الطابور والفصول", "order": 1},
    {"id": "vp_c2_s2", "criterion_id": "vp_c2", "name": "معالجة حالات الغياب والتأخير", "order": 2},
    {"id": "vp_c2_s3", "criterion_id": "vp_c2", "name": "متابعة السلوك العام ومعالجة المشكلات", "order": 3},
    {"id": "vp_c2_s4", "criterion_id": "vp_c2", "name": "تفعيل لائحة السلوك والمواظبة", "order": 4},
    {"id": "vp_c2_s5", "criterion_id": "vp_c2", "name": "تنظيم برامج توعوية للطلاب", "order": 5},
    # vp_c3
    {"id": "vp_c3_s1", "criterion_id": "vp_c3", "name": "متابعة تنفيذ الخطط الدراسية", "order": 1},
    {"id": "vp_c3_s2", "criterion_id": "vp_c3", "name": "الإشراف على البرامج والأنشطة المدرسية", "order": 2},
    {"id": "vp_c3_s3", "criterion_id": "vp_c3", "name": "متابعة خطط التحسين المدرسي", "order": 3},
    {"id": "vp_c3_s4", "criterion_id": "vp_c3", "name": "الإشراف على الاختبارات والتقويم", "order": 4},
    {"id": "vp_c3_s5", "criterion_id": "vp_c3", "name": "متابعة تنفيذ المبادرات التعليمية", "order": 5},
    # vp_c4
    {"id": "vp_c4_s1", "criterion_id": "vp_c4", "name": "تقييم أداء المعلمين من خلال الزيارات الصفية", "order": 1},
    {"id": "vp_c4_s2", "criterion_id": "vp_c4", "name": "تقديم تغذية راجعة للمعلمين", "order": 2},
    {"id": "vp_c4_s3", "criterion_id": "vp_c4", "name": "تحفيز المعلمين المتميزين", "order": 3},
    {"id": "vp_c4_s4", "criterion_id": "vp_c4", "name": "تنظيم برامج تطوير مهني للمعلمين", "order": 4},
    {"id": "vp_c4_s5", "criterion_id": "vp_c4", "name": "متابعة خطط المعلمين العلاجية", "order": 5},
    # vp_c5
    {"id": "vp_c5_s1", "criterion_id": "vp_c5", "name": "التواصل مع أولياء الأمور وحضور مجالس الآباء", "order": 1},
    {"id": "vp_c5_s2", "criterion_id": "vp_c5", "name": "تنظيم لقاءات توعوية لأولياء الأمور", "order": 2},
    {"id": "vp_c5_s3", "criterion_id": "vp_c5", "name": "المشاركة في الفعاليات المجتمعية", "order": 3},
    {"id": "vp_c5_s4", "criterion_id": "vp_c5", "name": "بناء شراكات مجتمعية للمدرسة", "order": 4},
    {"id": "vp_c5_s5", "criterion_id": "vp_c5", "name": "التعامل مع شكاوى واقتراحات أولياء الأمور", "order": 5}
]

VP_REPORTS = [
    # vp_c1_s1
    {"id": "vp_c1_s1_r001", "subcategory_id": "vp_c1_s1", "name": "تقرير توزيع مهام الإشراف اليومي على المعلمين", "order": 1},
    {"id": "vp_c1_s1_r002", "subcategory_id": "vp_c1_s1", "name": "سجل متابعة أداء المنادرين في الفسحة", "order": 2},
    {"id": "vp_c1_s1_r003", "subcategory_id": "vp_c1_s1", "name": "تقرير متابعة تنفيذ مهام لجنة التوجيه والإرشاد", "order": 3},
    {"id": "vp_c1_s1_r004", "subcategory_id": "vp_c1_s1", "name": "توثيق توزيع المهام على المعلمين في المناسبات", "order": 4},
    {"id": "vp_c1_s1_r005", "subcategory_id": "vp_c1_s1", "name": "تقرير عن آلية متابعة تنفيذ المهام الإدارية", "order": 5},
    # vp_c1_s2
    {"id": "vp_c1_s2_r001", "subcategory_id": "vp_c1_s2", "name": "تقرير تنظيم جداول الحصص الدراسية", "order": 1},
    {"id": "vp_c1_s2_r002", "subcategory_id": "vp_c1_s2", "name": "سجل متابعة تنفيذ الجداول ومعالجة الفجوات", "order": 2},
    {"id": "vp_c1_s2_r003", "subcategory_id": "vp_c1_s2", "name": "تقرير الإشراف اليومي على الفسحة والطابور", "order": 3},
    {"id": "vp_c1_s2_r004", "subcategory_id": "vp_c1_s2", "name": "توثيق جدول مناوبة المعلمين", "order": 4},
    {"id": "vp_c1_s2_r005", "subcategory_id": "vp_c1_s2", "name": "تقرير عن انضباط المعلمين في الحضور", "order": 5},
    # vp_c1_s3
    {"id": "vp_c1_s3_r001", "subcategory_id": "vp_c1_s3", "name": "تقرير عن تنفيذ خطة الإخلاء في المدرسة", "order": 1},
    {"id": "vp_c1_s3_r002", "subcategory_id": "vp_c1_s3", "name": "سجل متابعة صيانة أدوات السلامة", "order": 2},
    {"id": "vp_c1_s3_r003", "subcategory_id": "vp_c1_s3", "name": "تقرير عن تدريب الطلاب على خطط الطوارئ", "order": 3},
    {"id": "vp_c1_s3_r004", "subcategory_id": "vp_c1_s3", "name": "توثيق التعاون مع الدفاع المدني", "order": 4},
    {"id": "vp_c1_s3_r005", "subcategory_id": "vp_c1_s3", "name": "تقرير عن توفير بيئة آمنة في المدرسة", "order": 5},
    # vp_c1_s4
    {"id": "vp_c1_s4_r001", "subcategory_id": "vp_c1_s4", "name": "تقرير عن متابعة نظافة المدرسة وفصولها", "order": 1},
    {"id": "vp_c1_s4_r002", "subcategory_id": "vp_c1_s4", "name": "سجل متابعة صيانة الأثاث والمرافق", "order": 2},
    {"id": "vp_c1_s4_r003", "subcategory_id": "vp_c1_s4", "name": "تقرير عن توفير الموارد التعليمية", "order": 3},
    {"id": "vp_c1_s4_r004", "subcategory_id": "vp_c1_s4", "name": "توثيق متابعة المخزون والمواد الاستهلاكية", "order": 4},
    {"id": "vp_c1_s4_r005", "subcategory_id": "vp_c1_s4", "name": "تقرير عن تجهيز الفصول الدراسية", "order": 5},
    # vp_c1_s5
    {"id": "vp_c1_s5_r001", "subcategory_id": "vp_c1_s5", "name": "تقرير عن متابعة سجلات حضور الطلاب", "order": 1},
    {"id": "vp_c1_s5_r002", "subcategory_id": "vp_c1_s5", "name": "سجل متابعة انصراف الطلاب نهاية اليوم", "order": 2},
    {"id": "vp_c1_s5_r003", "subcategory_id": "vp_c1_s5", "name": "تقرير عن حالات الغياب ومعالجتها", "order": 3},
    {"id": "vp_c1_s5_r004", "subcategory_id": "vp_c1_s5", "name": "توثيق نظام البصمة أو الحضور اليومي", "order": 4},
    {"id": "vp_c1_s5_r005", "subcategory_id": "vp_c1_s5", "name": "تقرير إحصائي عن انضباط الطلاب", "order": 5},
    # vp_c2_s1
    {"id": "vp_c2_s1_r001", "subcategory_id": "vp_c2_s1", "name": "تقرير متابعة انضباط الطلاب في الطابور الصباحي", "order": 1},
    {"id": "vp_c2_s1_r002", "subcategory_id": "vp_c2_s1", "name": "سجل متابعة حضور الطلاب للحصص الأولى", "order": 2},
    {"id": "vp_c2_s1_r003", "subcategory_id": "vp_c2_s1", "name": "تقرير عن انضباط الطلاب أثناء الحصص", "order": 3},
    {"id": "vp_c2_s1_r004", "subcategory_id": "vp_c2_s1", "name": "توثيق حالات التأخير وعلاجها", "order": 4},
    {"id": "vp_c2_s1_r005", "subcategory_id": "vp_c2_s1", "name": "تقرير عن دور المنادرين في ضبط الانضباط", "order": 5},
    # vp_c2_s2
    {"id": "vp_c2_s2_r001", "subcategory_id": "vp_c2_s2", "name": "تقرير عن متابعة الطلاب المتغيبين", "order": 1},
    {"id": "vp_c2_s2_r002", "subcategory_id": "vp_c2_s2", "name": "سجل التواصل مع أولياء أمور الطلاب المتغيبين", "order": 2},
    {"id": "vp_c2_s2_r003", "subcategory_id": "vp_c2_s2", "name": "تقرير عن تطبيق لائحة الغياب", "order": 3},
    {"id": "vp_c2_s2_r004", "subcategory_id": "vp_c2_s2", "name": "توثيق حالات التأخير المتكرر", "order": 4},
    {"id": "vp_c2_s2_r005", "subcategory_id": "vp_c2_s2", "name": "تقرير عن برامج تحسين الانضباط", "order": 5},
    # vp_c2_s3
    {"id": "vp_c2_s3_r001", "subcategory_id": "vp_c2_s3", "name": "تقرير عن متابعة السلوك العام في المدرسة", "order": 1},
    {"id": "vp_c2_s3_r002", "subcategory_id": "vp_c2_s3", "name": "سجل معالجة المشكلات السلوكية", "order": 2},
    {"id": "vp_c2_s3_r003", "subcategory_id": "vp_c2_s3", "name": "تقرير عن عدد حالات التنمر ومعالجتها", "order": 3},
    {"id": "vp_c2_s3_r004", "subcategory_id": "vp_c2_s3", "name": "توثيق اجتماعات لجنة التوجيه والإرشاد", "order": 4},
    {"id": "vp_c2_s3_r005", "subcategory_id": "vp_c2_s3", "name": "تقرير عن برامج تعزيز السلوك الإيجابي", "order": 5},
    # vp_c2_s4
    {"id": "vp_c2_s4_r001", "subcategory_id": "vp_c2_s4", "name": "تقرير عن تطبيق لائحة السلوك والمواظبة", "order": 1},
    {"id": "vp_c2_s4_r002", "subcategory_id": "vp_c2_s4", "name": "سجل حالات المخالفات والعقوبات", "order": 2},
    {"id": "vp_c2_s4_r003", "subcategory_id": "vp_c2_s4", "name": "تقرير عن فعاليات توعوية حول اللائحة", "order": 3},
    {"id": "vp_c2_s4_r004", "subcategory_id": "vp_c2_s4", "name": "توثيق توقيع الطلاب على تعهد بالسلوك", "order": 4},
    {"id": "vp_c2_s4_r005", "subcategory_id": "vp_c2_s4", "name": "تقرير عن مدى التزام الطلاب بالزي المدرسي", "order": 5},
    # vp_c2_s5
    {"id": "vp_c2_s5_r001", "subcategory_id": "vp_c2_s5", "name": "تقرير عن برامج توعوية للطلاب حول الانضباط", "order": 1},
    {"id": "vp_c2_s5_r002", "subcategory_id": "vp_c2_s5", "name": "سجل تنظيم محاضرات عن السلوك", "order": 2},
    {"id": "vp_c2_s5_r003", "subcategory_id": "vp_c2_s5", "name": "تقرير عن مسابقات أفضل فصل منضبط", "order": 3},
    {"id": "vp_c2_s5_r004", "subcategory_id": "vp_c2_s5", "name": "توثيق برامج رفق للإرشاد", "order": 4},
    {"id": "vp_c2_s5_r005", "subcategory_id": "vp_c2_s5", "name": "تقرير عن ورش عمل للطلاب حول المهارات الاجتماعية", "order": 5},
    # vp_c3_s1
    {"id": "vp_c3_s1_r001", "subcategory_id": "vp_c3_s1", "name": "تقرير متابعة تنفيذ الخطط الدراسية", "order": 1},
    {"id": "vp_c3_s1_r002", "subcategory_id": "vp_c3_s1", "name": "سجل متابعة دفاتر التحضير", "order": 2},
    {"id": "vp_c3_s1_r003", "subcategory_id": "vp_c3_s1", "name": "تقرير عن مدى التزام المعلمين بالمنهج", "order": 3},
    {"id": "vp_c3_s1_r004", "subcategory_id": "vp_c3_s1", "name": "توثيق اجتماعات تنسيق المواد", "order": 4},
    {"id": "vp_c3_s1_r005", "subcategory_id": "vp_c3_s1", "name": "تقرير عن تنفيذ الخطط العلاجية", "order": 5},
    # vp_c3_s2
    {"id": "vp_c3_s2_r001", "subcategory_id": "vp_c3_s2", "name": "تقرير عن الإشراف على الأنشطة المدرسية", "order": 1},
    {"id": "vp_c3_s2_r002", "subcategory_id": "vp_c3_s2", "name": "سجل متابعة برامج النشاط الطلابي", "order": 2},
    {"id": "vp_c3_s2_r003", "subcategory_id": "vp_c3_s2", "name": "تقرير عن مشاركات المدرسة الخارجية", "order": 3},
    {"id": "vp_c3_s2_r004", "subcategory_id": "vp_c3_s2", "name": "توثيق الفعاليات والمناسبات", "order": 4},
    {"id": "vp_c3_s2_r005", "subcategory_id": "vp_c3_s2", "name": "تقرير عن أثر الأنشطة على الطلاب", "order": 5},
    # vp_c3_s3
    {"id": "vp_c3_s3_r001", "subcategory_id": "vp_c3_s3", "name": "تقرير متابعة تنفيذ خطة التحسين المدرسي", "order": 1},
    {"id": "vp_c3_s3_r002", "subcategory_id": "vp_c3_s3", "name": "سجل اجتماعات فريق التحسين", "order": 2},
    {"id": "vp_c3_s3_r003", "subcategory_id": "vp_c3_s3", "name": "تقرير عن مؤشرات الأداء في الخطة", "order": 3},
    {"id": "vp_c3_s3_r004", "subcategory_id": "vp_c3_s3", "name": "توثيق المبادرات المرتبطة بالتحسين", "order": 4},
    {"id": "vp_c3_s3_r005", "subcategory_id": "vp_c3_s3", "name": "تقرير نتائج تقييم الخطة", "order": 5},
    # vp_c3_s4
    {"id": "vp_c3_s4_r001", "subcategory_id": "vp_c3_s4", "name": "تقرير عن الإشراف على الاختبارات", "order": 1},
    {"id": "vp_c3_s4_r002", "subcategory_id": "vp_c3_s4", "name": "سجل متابعة سير الاختبارات", "order": 2},
    {"id": "vp_c3_s4_r003", "subcategory_id": "vp_c3_s4", "name": "تقرير عن نتائج الاختبارات وتحليلها", "order": 3},
    {"id": "vp_c3_s4_r004", "subcategory_id": "vp_c3_s4", "name": "توثيق اجتماعات لجنة الاختبارات", "order": 4},
    {"id": "vp_c3_s4_r005", "subcategory_id": "vp_c3_s4", "name": "تقرير عن تطبيق لائحة تقويم الطالب", "order": 5},
    # vp_c3_s5
    {"id": "vp_c3_s5_r001", "subcategory_id": "vp_c3_s5", "name": "تقرير متابعة تنفيذ المبادرات التعليمية", "order": 1},
    {"id": "vp_c3_s5_r002", "subcategory_id": "vp_c3_s5", "name": "سجل متابعة مبادرة تنمية القدرات", "order": 2},
    {"id": "vp_c3_s5_r003", "subcategory_id": "vp_c3_s5", "name": "تقرير عن مشاركة المدرسة في مبادرات الوزارة", "order": 3},
    {"id": "vp_c3_s5_r004", "subcategory_id": "vp_c3_s5", "name": "توثيق أثر المبادرات على الطلاب", "order": 4},
    {"id": "vp_c3_s5_r005", "subcategory_id": "vp_c3_s5", "name": "تقرير عن برامج تنمية الموهوبين", "order": 5},
    # vp_c4_s1
    {"id": "vp_c4_s1_r001", "subcategory_id": "vp_c4_s1", "name": "تقرير الزيارات الصفية للمعلمين", "order": 1},
    {"id": "vp_c4_s1_r002", "subcategory_id": "vp_c4_s1", "name": "سجل جدول الزيارات الصفية", "order": 2},
    {"id": "vp_c4_s1_r003", "subcategory_id": "vp_c4_s1", "name": "تقرير تقييم أداء المعلمين بناءً على الزيارات", "order": 3},
    {"id": "vp_c4_s1_r004", "subcategory_id": "vp_c4_s1", "name": "توثيق تغذية راجعة للمعلمين بعد الزيارة", "order": 4},
    {"id": "vp_c4_s1_r005", "subcategory_id": "vp_c4_s1", "name": "تقرير عن تطور أداء المعلمين", "order": 5},
    # vp_c4_s2
    {"id": "vp_c4_s2_r001", "subcategory_id": "vp_c4_s2", "name": "تقرير عن تقديم تغذية راجعة للمعلمين", "order": 1},
    {"id": "vp_c4_s2_r002", "subcategory_id": "vp_c4_s2", "name": "سجل لقاءات المتابعة مع المعلمين", "order": 2},
    {"id": "vp_c4_s2_r003", "subcategory_id": "vp_c4_s2", "name": "تقرير عن خطط تحسين أداء المعلمين", "order": 3},
    {"id": "vp_c4_s2_r004", "subcategory_id": "vp_c4_s2", "name": "توثيق الإشادة بالمعلمين المتميزين", "order": 4},
    {"id": "vp_c4_s2_r005", "subcategory_id": "vp_c4_s2", "name": "تقرير متابعة تنفيذ توصيات الزيارات", "order": 5},
    # vp_c4_s3
    {"id": "vp_c4_s3_r001", "subcategory_id": "vp_c4_s3", "name": "تقرير عن تكريم المعلمين المتميزين", "order": 1},
    {"id": "vp_c4_s3_r002", "subcategory_id": "vp_c4_s3", "name": "سجل حصر المعلمين المتميزين", "order": 2},
    {"id": "vp_c4_s3_r003", "subcategory_id": "vp_c4_s3", "name": "تقرير عن برامج تحفيز المعلمين", "order": 3},
    {"id": "vp_c4_s3_r004", "subcategory_id": "vp_c4_s3", "name": "توثيق مشاركة المعلمين في المسابقات", "order": 4},
    {"id": "vp_c4_s3_r005", "subcategory_id": "vp_c4_s3", "name": "تقرير عن أثر التحفيز على الأداء", "order": 5},
    # vp_c4_s4
    {"id": "vp_c4_s4_r001", "subcategory_id": "vp_c4_s4", "name": "تقرير عن تنظيم برامج تطوير مهني للمعلمين", "order": 1},
    {"id": "vp_c4_s4_r002", "subcategory_id": "vp_c4_s4", "name": "سجل حضور المعلمين للدورات", "order": 2},
    {"id": "vp_c4_s4_r003", "subcategory_id": "vp_c4_s4", "name": "تقرير عن احتياجات التطوير المهني", "order": 3},
    {"id": "vp_c4_s4_r004", "subcategory_id": "vp_c4_s4", "name": "توثيق ورش العمل المنفذة داخل المدرسة", "order": 4},
    {"id": "vp_c4_s4_r005", "subcategory_id": "vp_c4_s4", "name": "تقرير عن أثر البرامج على أداء المعلمين", "order": 5},
    # vp_c4_s5
    {"id": "vp_c4_s5_r001", "subcategory_id": "vp_c4_s5", "name": "تقرير متابعة تنفيذ خطط المعلمين العلاجية", "order": 1},
    {"id": "vp_c4_s5_r002", "subcategory_id": "vp_c4_s5", "name": "سجل متابعة تطور المعلمين", "order": 2},
    {"id": "vp_c4_s5_r003", "subcategory_id": "vp_c4_s5", "name": "تقرير عن فعالية الخطط العلاجية", "order": 3},
    {"id": "vp_c4_s5_r004", "subcategory_id": "vp_c4_s5", "name": "توثيق اجتماعات المتابعة مع المعلمين", "order": 4},
    {"id": "vp_c4_s5_r005", "subcategory_id": "vp_c4_s5", "name": "تقرير عن توصيات لتحسين الخطط", "order": 5},
    # vp_c5_s1
    {"id": "vp_c5_s1_r001", "subcategory_id": "vp_c5_s1", "name": "تقرير عن التواصل مع أولياء الأمور", "order": 1},
    {"id": "vp_c5_s1_r002", "subcategory_id": "vp_c5_s1", "name": "سجل حضور مجالس الآباء", "order": 2},
    {"id": "vp_c5_s1_r003", "subcategory_id": "vp_c5_s1", "name": "تقرير عن قضايا أولياء الأمور ومعالجتها", "order": 3},
    {"id": "vp_c5_s1_r004", "subcategory_id": "vp_c5_s1", "name": "توثيق استبيانات رأي أولياء الأمور", "order": 4},
    {"id": "vp_c5_s1_r005", "subcategory_id": "vp_c5_s1", "name": "تقرير عن نسبة رضا أولياء الأمور", "order": 5},
    # vp_c5_s2
    {"id": "vp_c5_s2_r001", "subcategory_id": "vp_c5_s2", "name": "تقرير عن تنظيم لقاءات توعوية لأولياء الأمور", "order": 1},
    {"id": "vp_c5_s2_r002", "subcategory_id": "vp_c5_s2", "name": "سجل محاضرات لأولياء الأمور", "order": 2},
    {"id": "vp_c5_s2_r003", "subcategory_id": "vp_c5_s2", "name": "تقرير عن برامج توعوية عن الانضباط", "order": 3},
    {"id": "vp_c5_s2_r004", "subcategory_id": "vp_c5_s2", "name": "توثيق إرشادات لأولياء الأمور", "order": 4},
    {"id": "vp_c5_s2_r005", "subcategory_id": "vp_c5_s2", "name": "تقرير عن تفاعل أولياء الأمور", "order": 5},
    # vp_c5_s3
    {"id": "vp_c5_s3_r001", "subcategory_id": "vp_c5_s3", "name": "تقرير عن مشاركة المدرسة في الفعاليات المجتمعية", "order": 1},
    {"id": "vp_c5_s3_r002", "subcategory_id": "vp_c5_s3", "name": "سجل المشاركات الخارجية", "order": 2},
    {"id": "vp_c5_s3_r003", "subcategory_id": "vp_c5_s3", "name": "تقرير عن الشراكات المجتمعية", "order": 3},
    {"id": "vp_c5_s3_r004", "subcategory_id": "vp_c5_s3", "name": "توثيق الزيارات المتبادلة مع المؤسسات", "order": 4},
    {"id": "vp_c5_s3_r005", "subcategory_id": "vp_c5_s3", "name": "تقرير عن أثر المشاركات المجتمعية", "order": 5},
    # vp_c5_s4
    {"id": "vp_c5_s4_r001", "subcategory_id": "vp_c5_s4", "name": "تقرير عن بناء شراكات مجتمعية للمدرسة", "order": 1},
    {"id": "vp_c5_s4_r002", "subcategory_id": "vp_c5_s4", "name": "سجل الاتفاقيات ومذكرات التفاهم", "order": 2},
    {"id": "vp_c5_s4_r003", "subcategory_id": "vp_c5_s4", "name": "تقرير عن دعم المؤسسات للمدرسة", "order": 3},
    {"id": "vp_c5_s4_r004", "subcategory_id": "vp_c5_s4", "name": "توثيق فعاليات مشتركة مع المجتمع", "order": 4},
    {"id": "vp_c5_s4_r005", "subcategory_id": "vp_c5_s4", "name": "تقرير عن استدامة الشراكات", "order": 5},
    # vp_c5_s5
    {"id": "vp_c5_s5_r001", "subcategory_id": "vp_c5_s5", "name": "تقرير عن التعامل مع شكاوى أولياء الأمور", "order": 1},
    {"id": "vp_c5_s5_r002", "subcategory_id": "vp_c5_s5", "name": "سجل الشكاوى والاقتراحات", "order": 2},
    {"id": "vp_c5_s5_r003", "subcategory_id": "vp_c5_s5", "name": "تقرير عن تحليل الشكاوى ونتائجها", "order": 3},
    {"id": "vp_c5_s5_r004", "subcategory_id": "vp_c5_s5", "name": "توثيق آليات استقبال الشكاوى", "order": 4},
    {"id": "vp_c5_s5_r005", "subcategory_id": "vp_c5_s5", "name": "تقرير عن إجراءات تحسين الخدمة", "order": 5}
]

VICE_PRINCIPAL_PROMPT_TEMPLATE = """أنت وكيل مدرسة تعمل وفق معايير الأداء الوظيفي المعتمدة في التعليم العام، وتمارس دورك القيادي التنفيذي في تنظيم العمل المدرسي ومتابعته.

المطلوب:
- عرض معيار الأداء الوظيفي.
- عرض التصنيف الفرعي.
- كتابة تقرير مهني متكامل يوضح الممارسات والإجراءات المرتبطة بهذا التصنيف.

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
- لغة إدارية رسمية دقيقة.
- إبراز دور الوكيل في التنظيم، المتابعة، توزيع المهام، وضبط العمل.
- توضيح آلية التنفيذ والتوثيق.
- ربط العمل بتحسين الانضباط المدرسي وجودة الأداء العام.
- الإشارة إلى التنسيق مع قائد المدرسة والمعلمين والجهات ذات العلاقة.
- إبراز أثر الممارسة على البيئة المدرسية وتحقيق مستهدفات المدرسة.
- إظهار جانب المتابعة وقياس الأثر والتحسين المستمر.
- صياغة عملية واقعية من 5–7 أسطر متماسكة.

**الحقول المطلوبة:**
1. الهدف التربوي
2. نبذة مختصرة
3. إجراءات التنفيذ
4. الاستراتيجيات المستخدمة
5. نقاط القوة
6. نقاط التحسين
7. التوصيات

يرجى تقديم الإجابة باللغة العربية الفصحى، وتنظيمها بحيث يكون كل حقل في سطر منفصل يبدأ برقمه فقط دون ذكر العنوان."""