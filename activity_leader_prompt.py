# activity_leader_prompt.py

AL_CRITERIA = [
    {"id": "al_c1", "name": "تخطيط وتنظيم الأنشطة الطلابية", "weight": "10%", "order": 1},
    {"id": "al_c2", "name": "تنفيذ الفعاليات والبرامج", "weight": "10%", "order": 2},
    {"id": "al_c3", "name": "تنمية المهارات واكتشاف المواهب", "weight": "10%", "order": 3},
    {"id": "al_c4", "name": "المشاركات الخارجية والمسابقات", "weight": "10%", "order": 4},
    {"id": "al_c5", "name": "توثيق الأنشطة وقياس الأثر", "weight": "10%", "order": 5}
]

AL_SUBCATEGORIES = [
    # al_c1
    {"id": "al_c1_s1", "criterion_id": "al_c1", "name": "إعداد خطة النشاط السنوية", "order": 1},
    {"id": "al_c1_s2", "criterion_id": "al_c1", "name": "تشكيل الفرق الطلابية", "order": 2},
    {"id": "al_c1_s3", "criterion_id": "al_c1", "name": "تجهيز الأدوات والموارد", "order": 3},
    {"id": "al_c1_s4", "criterion_id": "al_c1", "name": "التنسيق مع المعلمين والإدارة", "order": 4},
    {"id": "al_c1_s5", "criterion_id": "al_c1", "name": "إعداد جداول الأنشطة", "order": 5},
    # al_c2
    {"id": "al_c2_s1", "criterion_id": "al_c2", "name": "تنظيم الفعاليات والمناسبات", "order": 1},
    {"id": "al_c2_s2", "criterion_id": "al_c2", "name": "الإشراف على الأندية المدرسية", "order": 2},
    {"id": "al_c2_s3", "criterion_id": "al_c2", "name": "تنظيم الرحلات المدرسية", "order": 3},
    {"id": "al_c2_s4", "criterion_id": "al_c2", "name": "إدارة المسابقات الداخلية", "order": 4},
    {"id": "al_c2_s5", "criterion_id": "al_c2", "name": "تنفيذ ورش العمل", "order": 5},
    # al_c3
    {"id": "al_c3_s1", "criterion_id": "al_c3", "name": "اكتشاف المواهب الطلابية", "order": 1},
    {"id": "al_c3_s2", "criterion_id": "al_c3", "name": "تنمية المهارات القيادية", "order": 2},
    {"id": "al_c3_s3", "criterion_id": "al_c3", "name": "تنمية المهارات الفنية والثقافية", "order": 3},
    {"id": "al_c3_s4", "criterion_id": "al_c3", "name": "تنمية المهارات الرياضية", "order": 4},
    {"id": "al_c3_s5", "criterion_id": "al_c3", "name": "تنمية المهارات الاجتماعية", "order": 5},
    # al_c4
    {"id": "al_c4_s1", "criterion_id": "al_c4", "name": "المشاركة في المسابقات الخارجية", "order": 1},
    {"id": "al_c4_s2", "criterion_id": "al_c4", "name": "تنظيم زيارات تبادلية", "order": 2},
    {"id": "al_c4_s3", "criterion_id": "al_c4", "name": "المشاركة في الفعاليات المجتمعية", "order": 3},
    {"id": "al_c4_s4", "criterion_id": "al_c4", "name": "التنسيق مع أندية الحي", "order": 4},
    {"id": "al_c4_s5", "criterion_id": "al_c4", "name": "المشاركة في المبادرات الوطنية", "order": 5},
    # al_c5
    {"id": "al_c5_s1", "criterion_id": "al_c5", "name": "توثيق الأنشطة (صور, تقارير)", "order": 1},
    {"id": "al_c5_s2", "criterion_id": "al_c5", "name": "قياس أثر الأنشطة على الطلاب", "order": 2},
    {"id": "al_c5_s3", "criterion_id": "al_c5", "name": "إعداد تقارير ختامية للأنشطة", "order": 3},
    {"id": "al_c5_s4", "criterion_id": "al_c5", "name": "تحليل المشاركات", "order": 4},
    {"id": "al_c5_s5", "criterion_id": "al_c5", "name": "رفع التقارير للإدارة", "order": 5}
]

AL_REPORTS = [
    # al_c1_s1
    {"id": "al_c1_s1_r001", "subcategory_id": "al_c1_s1", "name": "تقرير إعداد خطة النشاط السنوية", "order": 1},
    {"id": "al_c1_s1_r002", "subcategory_id": "al_c1_s1", "name": "سجل مسودة خطة النشاط", "order": 2},
    {"id": "al_c1_s1_r003", "subcategory_id": "al_c1_s1", "name": "تقرير عن اعتماد الخطة من الإدارة", "order": 3},
    {"id": "al_c1_s1_r004", "subcategory_id": "al_c1_s1", "name": "توثيق توزيع الخطة على المعنيين", "order": 4},
    {"id": "al_c1_s1_r005", "subcategory_id": "al_c1_s1", "name": "تقرير عن مراجعة الخطة وتحديثها", "order": 5},
    # al_c1_s2
    {"id": "al_c1_s2_r001", "subcategory_id": "al_c1_s2", "name": "تقرير عن تشكيل الفرق الطلابية", "order": 1},
    {"id": "al_c1_s2_r002", "subcategory_id": "al_c1_s2", "name": "سجل الفرق الطلابية وأعضائها", "order": 2},
    {"id": "al_c1_s2_r003", "subcategory_id": "al_c1_s2", "name": "تقرير عن انتخاب قادة الفرق", "order": 3},
    {"id": "al_c1_s2_r004", "subcategory_id": "al_c1_s2", "name": "توثيق اجتماعات الفرق", "order": 4},
    {"id": "al_c1_s2_r005", "subcategory_id": "al_c1_s2", "name": "تقرير عن أداء الفرق", "order": 5},
    # al_c1_s3
    {"id": "al_c1_s3_r001", "subcategory_id": "al_c1_s3", "name": "تقرير عن تجهيز أدوات الأنشطة", "order": 1},
    {"id": "al_c1_s3_r002", "subcategory_id": "al_c1_s3", "name": "سجل طلب احتياجات الأنشطة", "order": 2},
    {"id": "al_c1_s3_r003", "subcategory_id": "al_c1_s3", "name": "تقرير عن تجهيز مكان النشاط", "order": 3},
    {"id": "al_c1_s3_r004", "subcategory_id": "al_c1_s3", "name": "توثيق متابعة الصيانة للأدوات", "order": 4},
    {"id": "al_c1_s3_r005", "subcategory_id": "al_c1_s3", "name": "تقرير عن توفير المواد الاستهلاكية", "order": 5},
    # al_c1_s4
    {"id": "al_c1_s4_r001", "subcategory_id": "al_c1_s4", "name": "تقرير عن التنسيق مع المعلمين للأنشطة", "order": 1},
    {"id": "al_c1_s4_r002", "subcategory_id": "al_c1_s4", "name": "سجل اجتماعات تنسيق الأنشطة", "order": 2},
    {"id": "al_c1_s4_r003", "subcategory_id": "al_c1_s4", "name": "تقرير عن مشاركة المعلمين في الأنشطة", "order": 3},
    {"id": "al_c1_s4_r004", "subcategory_id": "al_c1_s4", "name": "توثيق التعاون مع الإدارة", "order": 4},
    {"id": "al_c1_s4_r005", "subcategory_id": "al_c1_s4", "name": "تقرير عن تذليل الصعوبات", "order": 5},
    # al_c1_s5
    {"id": "al_c1_s5_r001", "subcategory_id": "al_c1_s5", "name": "تقرير إعداد جداول الأنشطة الأسبوعية", "order": 1},
    {"id": "al_c1_s5_r002", "subcategory_id": "al_c1_s5", "name": "سجل توزيع الجداول", "order": 2},
    {"id": "al_c1_s5_r003", "subcategory_id": "al_c1_s5", "name": "تقرير عن التزام الفرق بالجدول", "order": 3},
    {"id": "al_c1_s5_r004", "subcategory_id": "al_c1_s5", "name": "توثيق تعديلات الجدول", "order": 4},
    {"id": "al_c1_s5_r005", "subcategory_id": "al_c1_s5", "name": "تقرير عن تقييم الجداول", "order": 5},
    # al_c2_s1
    {"id": "al_c2_s1_r001", "subcategory_id": "al_c2_s1", "name": "تقرير عن تنظيم يوم المهنة", "order": 1},
    {"id": "al_c2_s1_r002", "subcategory_id": "al_c2_s1", "name": "سجل فعاليات اليوم الوطني", "order": 2},
    {"id": "al_c2_s1_r003", "subcategory_id": "al_c2_s1", "name": "تقرير عن تنظيم معرض المواهب", "order": 3},
    {"id": "al_c2_s1_r004", "subcategory_id": "al_c2_s1", "name": "توثيق حفلات التكريم", "order": 4},
    {"id": "al_c2_s1_r005", "subcategory_id": "al_c2_s1", "name": "تقرير عن تنظيم الأسبوع الثقافي", "order": 5},
    # al_c2_s2
    {"id": "al_c2_s2_r001", "subcategory_id": "al_c2_s2", "name": "تقرير عن الإشراف على نادي الرياضيات", "order": 1},
    {"id": "al_c2_s2_r002", "subcategory_id": "al_c2_s2", "name": "سجل أنشطة نادي اللغة الإنجليزية", "order": 2},
    {"id": "al_c2_s2_r003", "subcategory_id": "al_c2_s2", "name": "تقرير عن نادي المسرح", "order": 3},
    {"id": "al_c2_s2_r004", "subcategory_id": "al_c2_s2", "name": "توثيق اجتماعات الأندية", "order": 4},
    {"id": "al_c2_s2_r005", "subcategory_id": "al_c2_s2", "name": "تقرير عن إنجازات الأندية", "order": 5},
    # al_c2_s3
    {"id": "al_c2_s3_r001", "subcategory_id": "al_c2_s3", "name": "تقرير عن تنظيم رحلة علمية", "order": 1},
    {"id": "al_c2_s3_r002", "subcategory_id": "al_c2_s3", "name": "سجل الموافقات للرحلات", "order": 2},
    {"id": "al_c2_s3_r003", "subcategory_id": "al_c2_s3", "name": "تقرير عن رحلة ترفيهية", "order": 3},
    {"id": "al_c2_s3_r004", "subcategory_id": "al_c2_s3", "name": "توثيق تقييم الرحلات", "order": 4},
    {"id": "al_c2_s3_r005", "subcategory_id": "al_c2_s3", "name": "تقرير عن أثر الرحلات على الطلاب", "order": 5},
    # al_c2_s4
    {"id": "al_c2_s4_r001", "subcategory_id": "al_c2_s4", "name": "تقرير عن تنظيم مسابقة الخطابة", "order": 1},
    {"id": "al_c2_s4_r002", "subcategory_id": "al_c2_s4", "name": "سجل نتائج مسابقة القرآن", "order": 2},
    {"id": "al_c2_s4_r003", "subcategory_id": "al_c2_s4", "name": "تقرير عن مسابقة الروبوت", "order": 3},
    {"id": "al_c2_s4_r004", "subcategory_id": "al_c2_s4", "name": "توثيق تحكيم المسابقات", "order": 4},
    {"id": "al_c2_s4_r005", "subcategory_id": "al_c2_s4", "name": "تقرير عن جوائز الفائزين", "order": 5},
    # al_c2_s5
    {"id": "al_c2_s5_r001", "subcategory_id": "al_c2_s5", "name": "تقرير عن ورش عمل الرسم", "order": 1},
    {"id": "al_c2_s5_r002", "subcategory_id": "al_c2_s5", "name": "سجل ورش التصوير", "order": 2},
    {"id": "al_c2_s5_r003", "subcategory_id": "al_c2_s5", "name": "تقرير عن ورش الخط العربي", "order": 3},
    {"id": "al_c2_s5_r004", "subcategory_id": "al_c2_s5", "name": "توثيق ورش الإسعافات الأولية", "order": 4},
    {"id": "al_c2_s5_r005", "subcategory_id": "al_c2_s5", "name": "تقرير عن تفاعل الطلاب مع الورش", "order": 5},
    # al_c3_s1
    {"id": "al_c3_s1_r001", "subcategory_id": "al_c3_s1", "name": "تقرير عن اكتشاف المواهب الفنية", "order": 1},
    {"id": "al_c3_s1_r002", "subcategory_id": "al_c3_s1", "name": "سجل قاعدة بيانات الموهوبين", "order": 2},
    {"id": "al_c3_s1_r003", "subcategory_id": "al_c3_s1", "name": "تقرير عن مسابقة المواهب", "order": 3},
    {"id": "al_c3_s1_r004", "subcategory_id": "al_c3_s1", "name": "توثيق اختبارات اكتشاف المواهب", "order": 4},
    {"id": "al_c3_s1_r005", "subcategory_id": "al_c3_s1", "name": "تقرير عن متابعة الموهوبين", "order": 5},
    # al_c3_s2
    {"id": "al_c3_s2_r001", "subcategory_id": "al_c3_s2", "name": "تقرير عن برنامج تنمية القيادات الطلابية", "order": 1},
    {"id": "al_c3_s2_r002", "subcategory_id": "al_c3_s2", "name": "سجل تدريب الطلاب على القيادة", "order": 2},
    {"id": "al_c3_s2_r003", "subcategory_id": "al_c3_s2", "name": "تقرير عن إعداد قائد المستقبل", "order": 3},
    {"id": "al_c3_s2_r004", "subcategory_id": "al_c3_s2", "name": "توثيق مشاركة الطلاب في القيادة", "order": 4},
    {"id": "al_c3_s2_r005", "subcategory_id": "al_c3_s2", "name": "تقرير عن تطور مهارات القيادة", "order": 5},
    # al_c3_s3
    {"id": "al_c3_s3_r001", "subcategory_id": "al_c3_s3", "name": "تقرير عن ورش تنمية الإبداع", "order": 1},
    {"id": "al_c3_s3_r002", "subcategory_id": "al_c3_s3", "name": "سجل مسابقات ثقافية", "order": 2},
    {"id": "al_c3_s3_r003", "subcategory_id": "al_c3_s3", "name": "تقرير عن إنتاج أعمال فنية", "order": 3},
    {"id": "al_c3_s3_r004", "subcategory_id": "al_c3_s3", "name": "توثيق معرض المواهب الفنية", "order": 4},
    {"id": "al_c3_s3_r005", "subcategory_id": "al_c3_s3", "name": "تقرير عن تطور المهارات الفنية", "order": 5},
    # al_c3_s4
    {"id": "al_c3_s4_r001", "subcategory_id": "al_c3_s4", "name": "تقرير عن الأنشطة الرياضية", "order": 1},
    {"id": "al_c3_s4_r002", "subcategory_id": "al_c3_s4", "name": "سجل مشاركة الطلاب في الرياضة", "order": 2},
    {"id": "al_c3_s4_r003", "subcategory_id": "al_c3_s4", "name": "تقرير عن دوري المدرسة", "order": 3},
    {"id": "al_c3_s4_r004", "subcategory_id": "al_c3_s4", "name": "توثيق اكتشاف المواهب الرياضية", "order": 4},
    {"id": "al_c3_s4_r005", "subcategory_id": "al_c3_s4", "name": "تقرير عن تحسين اللياقة البدنية", "order": 5},
    # al_c3_s5
    {"id": "al_c3_s5_r001", "subcategory_id": "al_c3_s5", "name": "تقرير عن ورش العمل الجماعي", "order": 1},
    {"id": "al_c3_s5_r002", "subcategory_id": "al_c3_s5", "name": "سجل أنشطة التعاون", "order": 2},
    {"id": "al_c3_s5_r003", "subcategory_id": "al_c3_s5", "name": "تقرير عن برامج التواصل", "order": 3},
    {"id": "al_c3_s5_r004", "subcategory_id": "al_c3_s5", "name": "توثيق مبادرات خدمة المجتمع", "order": 4},
    {"id": "al_c3_s5_r005", "subcategory_id": "al_c3_s5", "name": "تقرير عن تطور المهارات الاجتماعية", "order": 5},
    # al_c4_s1
    {"id": "al_c4_s1_r001", "subcategory_id": "al_c4_s1", "name": "تقرير عن المشاركة في مسابقة الإبداع", "order": 1},
    {"id": "al_c4_s1_r002", "subcategory_id": "al_c4_s1", "name": "سجل المشاركات الخارجية", "order": 2},
    {"id": "al_c4_s1_r003", "subcategory_id": "al_c4_s1", "name": "تقرير عن نتائج المشاركات", "order": 3},
    {"id": "al_c4_s1_r004", "subcategory_id": "al_c4_s1", "name": "توثيق شهادات التكريم", "order": 4},
    {"id": "al_c4_s1_r005", "subcategory_id": "al_c4_s1", "name": "تقرير عن أثر المشاركات", "order": 5},
    # al_c4_s2
    {"id": "al_c4_s2_r001", "subcategory_id": "al_c4_s2", "name": "تقرير عن زيارة مدرسة أخرى", "order": 1},
    {"id": "al_c4_s2_r002", "subcategory_id": "al_c4_s2", "name": "سجل تبادل الزيارات", "order": 2},
    {"id": "al_c4_s2_r003", "subcategory_id": "al_c4_s2", "name": "تقرير عن استقبال وفود طلابية", "order": 3},
    {"id": "al_c4_s2_r004", "subcategory_id": "al_c4_s2", "name": "توثيق تبادل الخبرات", "order": 4},
    {"id": "al_c4_s2_r005", "subcategory_id": "al_c4_s2", "name": "تقرير عن استفادة الطلاب", "order": 5},
    # al_c4_s3
    {"id": "al_c4_s3_r001", "subcategory_id": "al_c4_s3", "name": "تقرير عن مشاركة في مهرجان الحي", "order": 1},
    {"id": "al_c4_s3_r002", "subcategory_id": "al_c4_s3", "name": "سجل المشاركة في الفعاليات المجتمعية", "order": 2},
    {"id": "al_c4_s3_r003", "subcategory_id": "al_c4_s3", "name": "تقرير عن تنظيم حملة تطوعية", "order": 3},
    {"id": "al_c4_s3_r004", "subcategory_id": "al_c4_s3", "name": "توثيق شراكة مع مؤسسة", "order": 4},
    {"id": "al_c4_s3_r005", "subcategory_id": "al_c4_s3", "name": "تقرير عن أثر المشاركة المجتمعية", "order": 5},
    # al_c4_s4
    {"id": "al_c4_s4_r001", "subcategory_id": "al_c4_s4", "name": "تقرير عن التنسيق مع نادي الحي", "order": 1},
    {"id": "al_c4_s4_r002", "subcategory_id": "al_c4_s4", "name": "سجل اتفاقيات الشراكة", "order": 2},
    {"id": "al_c4_s4_r003", "subcategory_id": "al_c4_s4", "name": "تقرير عن أنشطة مشتركة مع النادي", "order": 3},
    {"id": "al_c4_s4_r004", "subcategory_id": "al_c4_s4", "name": "توثيق استفادة الطلاب من النادي", "order": 4},
    {"id": "al_c4_s4_r005", "subcategory_id": "al_c4_s4", "name": "تقرير عن استمرارية الشراكة", "order": 5},
    # al_c4_s5
    {"id": "al_c4_s5_r001", "subcategory_id": "al_c4_s5", "name": "تقرير عن المشاركة في مبادرات وطنية", "order": 1},
    {"id": "al_c4_s5_r002", "subcategory_id": "al_c4_s5", "name": "سجل تفعيل اليوم الوطني", "order": 2},
    {"id": "al_c4_s5_r003", "subcategory_id": "al_c4_s5", "name": "تقرير عن مسيرة الولاء", "order": 3},
    {"id": "al_c4_s5_r004", "subcategory_id": "al_c4_s5", "name": "توثيق تفعيل رؤية 2030", "order": 4},
    {"id": "al_c4_s5_r005", "subcategory_id": "al_c4_s5", "name": "تقرير عن أثر المبادرات الوطنية", "order": 5},
    # al_c5_s1
    {"id": "al_c5_s1_r001", "subcategory_id": "al_c5_s1", "name": "تقرير عن توثيق الأنشطة بالصور", "order": 1},
    {"id": "al_c5_s1_r002", "subcategory_id": "al_c5_s1", "name": "سجل أرشفة التقارير", "order": 2},
    {"id": "al_c5_s1_r003", "subcategory_id": "al_c5_s1", "name": "تقرير عن إصدار مجلة النشاط", "order": 3},
    {"id": "al_c5_s1_r004", "subcategory_id": "al_c5_s1", "name": "توثيق فيديوهات الأنشطة", "order": 4},
    {"id": "al_c5_s1_r005", "subcategory_id": "al_c5_s1", "name": "تقرير عن حفظ الوثائق", "order": 5},
    # al_c5_s2
    {"id": "al_c5_s2_r001", "subcategory_id": "al_c5_s2", "name": "تقرير عن استبيان رضا الطلاب", "order": 1},
    {"id": "al_c5_s2_r002", "subcategory_id": "al_c5_s2", "name": "سجل قياس أثر الأنشطة", "order": 2},
    {"id": "al_c5_s2_r003", "subcategory_id": "al_c5_s2", "name": "تقرير عن تحسين المهارات بعد الأنشطة", "order": 3},
    {"id": "al_c5_s2_r004", "subcategory_id": "al_c5_s2", "name": "توثيق قصص نجاح", "order": 4},
    {"id": "al_c5_s2_r005", "subcategory_id": "al_c5_s2", "name": "تقرير عن أثر الأنشطة على التحصيل", "order": 5},
    # al_c5_s3
    {"id": "al_c5_s3_r001", "subcategory_id": "al_c5_s3", "name": "تقرير ختامي عن النشاط", "order": 1},
    {"id": "al_c5_s3_r002", "subcategory_id": "al_c5_s3", "name": "سجل إحصاءات المشاركة", "order": 2},
    {"id": "al_c5_s3_r003", "subcategory_id": "al_c5_s3", "name": "تقرير عن إنجازات النشاط", "order": 3},
    {"id": "al_c5_s3_r004", "subcategory_id": "al_c5_s3", "name": "توثيق التوصيات", "order": 4},
    {"id": "al_c5_s3_r005", "subcategory_id": "al_c5_s3", "name": "تقرير عن خطة العام القادم", "order": 5},
    # al_c5_s4
    {"id": "al_c5_s4_r001", "subcategory_id": "al_c5_s4", "name": "تقرير تحليل المشاركات", "order": 1},
    {"id": "al_c5_s4_r002", "subcategory_id": "al_c5_s4", "name": "سجل نسب المشاركة", "order": 2},
    {"id": "al_c5_s4_r003", "subcategory_id": "al_c5_s4", "name": "تقرير عن الفئات المستهدفة", "order": 3},
    {"id": "al_c5_s4_r004", "subcategory_id": "al_c5_s4", "name": "توثيق تطور المشاركة", "order": 4},
    {"id": "al_c5_s4_r005", "subcategory_id": "al_c5_s4", "name": "تقرير عن توصيات التحسين", "order": 5},
    # al_c5_s5
    {"id": "al_c5_s5_r001", "subcategory_id": "al_c5_s5", "name": "تقرير رفع للإدارة عن النشاط", "order": 1},
    {"id": "al_c5_s5_r002", "subcategory_id": "al_c5_s5", "name": "سجل التقارير المرفوعة", "order": 2},
    {"id": "al_c5_s5_r003", "subcategory_id": "al_c5_s5", "name": "تقرير عن اجتماعات عرض النتائج", "order": 3},
    {"id": "al_c5_s5_r004", "subcategory_id": "al_c5_s5", "name": "توثيق متابعة توصيات الإدارة", "order": 4},
    {"id": "al_c5_s5_r005", "subcategory_id": "al_c5_s5", "name": "تقرير عن استفادة الإدارة من التقارير", "order": 5}
]

ACTIVITY_LEADER_PROMPT_TEMPLATE = """أنت رائد نشاط طلابي مسؤول عن تخطيط وتنفيذ البرامج والفعاليات الطلابية وفق معايير النشاط المعتمدة.

المطلوب:
- عرض معيار الأداء الوظيفي.
- عرض التصنيف الفرعي.
- كتابة تقرير مهني يوضح كيفية تنفيذ الأنشطة المرتبطة بهذا التصنيف.

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
- لغة تربوية رسمية.
- إبراز التخطيط المسبق للبرامج وبنائها على احتياج المدرسة.
- توضيح آلية التنفيذ وتنظيم الفعاليات.
- بيان دور الأنشطة في تنمية مهارات الطلبة وقيمهم.
- الإشارة إلى قياس الأثر وتحليل نتائج المشاركة.
- إبراز الشراكات المجتمعية والمشاركات الخارجية إن وجدت.
- توضيح دور التحفيز واكتشاف المواهب.
- صياغة واقعية تطبيقية من 5–7 أسطر.

**الحقول المطلوبة:**
1. الهدف التربوي
2. نبذة مختصرة
3. إجراءات التنفيذ
4. الاستراتيجيات المستخدمة
5. نقاط القوة
6. نقاط التحسين
7. التوصيات

يرجى تقديم الإجابة باللغة العربية الفصحى، وتنظيمها بحيث يكون كل حقل في سطر منفصل يبدأ برقمه فقط دون ذكر العنوان."""