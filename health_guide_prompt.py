# health_guide_prompt.py

HG_CRITERIA = [
    {"id": "hg_c1", "name": "تنفيذ البرامج الصحية المدرسية", "weight": "10%", "order": 1},
    {"id": "hg_c2", "name": "رصد الحالات الصحية ومتابعتها", "weight": "10%", "order": 2},
    {"id": "hg_c3", "name": "تعزيز البيئة الصحية في المدرسة", "weight": "10%", "order": 3},
    {"id": "hg_c4", "name": "التوعية الصحية للطلاب والمجتمع", "weight": "10%", "order": 4},
    {"id": "hg_c5", "name": "التنسيق مع الجهات الصحية", "weight": "10%", "order": 5}
]

HG_SUBCATEGORIES = [
    # hg_c1
    {"id": "hg_c1_s1", "criterion_id": "hg_c1", "name": "تنظيم برامج التطعيمات", "order": 1},
    {"id": "hg_c1_s2", "criterion_id": "hg_c1", "name": "تنفيذ برامج الكشف المبكر", "order": 2},
    {"id": "hg_c1_s3", "criterion_id": "hg_c1", "name": "متابعة النظافة العامة والنظافة الشخصية", "order": 3},
    {"id": "hg_c1_s4", "criterion_id": "hg_c1", "name": "إدارة عيادة المدرسة", "order": 4},
    {"id": "hg_c1_s5", "criterion_id": "hg_c1", "name": "تنظيم حملات التبرع بالدم", "order": 5},
    # hg_c2
    {"id": "hg_c2_s1", "criterion_id": "hg_c2", "name": "رصد حالات الأمراض المعدية", "order": 1},
    {"id": "hg_c2_s2", "criterion_id": "hg_c2", "name": "متابعة الطلاب ذوي الأمراض المزمنة", "order": 2},
    {"id": "hg_c2_s3", "criterion_id": "hg_c2", "name": "تقديم الإسعافات الأولية", "order": 3},
    {"id": "hg_c2_s4", "criterion_id": "hg_c2", "name": "تحويل الحالات للرعاية الصحية", "order": 4},
    {"id": "hg_c2_s5", "criterion_id": "hg_c2", "name": "توثيق السجلات الصحية", "order": 5},
    # hg_c3
    {"id": "hg_c3_s1", "criterion_id": "hg_c3", "name": "الإشراف على نظافة المرافق", "order": 1},
    {"id": "hg_c3_s2", "criterion_id": "hg_c3", "name": "متابعة سلامة الأغذية في المقصف", "order": 2},
    {"id": "hg_c3_s3", "criterion_id": "hg_c3", "name": "التأكد من تهوية الفصول", "order": 3},
    {"id": "hg_c3_s4", "criterion_id": "hg_c3", "name": "تنظيم حملات مكافحة الحشرات", "order": 4},
    {"id": "hg_c3_s5", "criterion_id": "hg_c3", "name": "تعزيز السلوكيات الصحية", "order": 5},
    # hg_c4
    {"id": "hg_c4_s1", "criterion_id": "hg_c4", "name": "تقديم محاضرات توعوية عن التغذية", "order": 1},
    {"id": "hg_c4_s2", "criterion_id": "hg_c4", "name": "تنظيم ورش عن النظافة الشخصية", "order": 2},
    {"id": "hg_c4_s3", "criterion_id": "hg_c4", "name": "توعية حول الأمراض المزمنة", "order": 3},
    {"id": "hg_c4_s4", "criterion_id": "hg_c4", "name": "توعية حول الصحة النفسية", "order": 4},
    {"id": "hg_c4_s5", "criterion_id": "hg_c4", "name": "توعية حول الإسعافات الأولية", "order": 5},
    # hg_c5
    {"id": "hg_c5_s1", "criterion_id": "hg_c5", "name": "التنسيق مع المراكز الصحية", "order": 1},
    {"id": "hg_c5_s2", "criterion_id": "hg_c5", "name": "التعاون مع مستشفيات المنطقة", "order": 2},
    {"id": "hg_c5_s3", "criterion_id": "hg_c5", "name": "متابعة حملات التوعية مع الجهات الخارجية", "order": 3},
    {"id": "hg_c5_s4", "criterion_id": "hg_c5", "name": "المشاركة في لجان الصحة المدرسية", "order": 4},
    {"id": "hg_c5_s5", "criterion_id": "hg_c5", "name": "التنسيق مع الصحة العامة", "order": 5}
]

HG_REPORTS = [
    # hg_c1_s1
    {"id": "hg_c1_s1_r001", "subcategory_id": "hg_c1_s1", "name": "تقرير عن تنظيم حملة التطعيمات بالمدرسة", "order": 1},
    {"id": "hg_c1_s1_r002", "subcategory_id": "hg_c1_s1", "name": "سجل متابعة تطعيم الطلاب", "order": 2},
    {"id": "hg_c1_s1_r003", "subcategory_id": "hg_c1_s1", "name": "تقرير عن التنسيق مع المركز الصحي للتطعيمات", "order": 3},
    {"id": "hg_c1_s1_r004", "subcategory_id": "hg_c1_s1", "name": "توثيق نسب التغطية بالتطعيمات", "order": 4},
    {"id": "hg_c1_s1_r005", "subcategory_id": "hg_c1_s1", "name": "تقرير عن توعية أولياء الأمور بالتطعيمات", "order": 5},
    # hg_c1_s2
    {"id": "hg_c1_s2_r001", "subcategory_id": "hg_c1_s2", "name": "تقرير عن تنفيذ برنامج الكشف المبكر عن السمنة", "order": 1},
    {"id": "hg_c1_s2_r002", "subcategory_id": "hg_c1_s2", "name": "سجل قياس الطول والوزن للطلاب", "order": 2},
    {"id": "hg_c1_s2_r003", "subcategory_id": "hg_c1_s2", "name": "تقرير عن فحص النظر للطلاب", "order": 3},
    {"id": "hg_c1_s2_r004", "subcategory_id": "hg_c1_s2", "name": "توثيق نتائج الكشف المبكر", "order": 4},
    {"id": "hg_c1_s2_r005", "subcategory_id": "hg_c1_s2", "name": "تقرير عن متابعة الحالات المكتشفة", "order": 5},
    # hg_c1_s3
    {"id": "hg_c1_s3_r001", "subcategory_id": "hg_c1_s3", "name": "تقرير عن متابعة نظافة الفصول", "order": 1},
    {"id": "hg_c1_s3_r002", "subcategory_id": "hg_c1_s3", "name": "سجل تفتيش دورات المياه", "order": 2},
    {"id": "hg_c1_s3_r003", "subcategory_id": "hg_c1_s3", "name": "تقرير عن حملات التوعية بالنظافة الشخصية", "order": 3},
    {"id": "hg_c1_s3_r004", "subcategory_id": "hg_c1_s3", "name": "توثيق توفير أدوات النظافة", "order": 4},
    {"id": "hg_c1_s3_r005", "subcategory_id": "hg_c1_s3", "name": "تقرير عن التزام الطلاب بالنظافة", "order": 5},
    # hg_c1_s4
    {"id": "hg_c1_s4_r001", "subcategory_id": "hg_c1_s4", "name": "تقرير عن إدارة عيادة المدرسة", "order": 1},
    {"id": "hg_c1_s4_r002", "subcategory_id": "hg_c1_s4", "name": "سجل زيارات الطلاب للعيادة", "order": 2},
    {"id": "hg_c1_s4_r003", "subcategory_id": "hg_c1_s4", "name": "تقرير عن تجهيزات العيادة والأدوية", "order": 3},
    {"id": "hg_c1_s4_r004", "subcategory_id": "hg_c1_s4", "name": "توثيق الصيانة الدورية لأجهزة العيادة", "order": 4},
    {"id": "hg_c1_s4_r005", "subcategory_id": "hg_c1_s4", "name": "تقرير عن طلب الاحتياجات الطبية", "order": 5},
    # hg_c1_s5
    {"id": "hg_c1_s5_r001", "subcategory_id": "hg_c1_s5", "name": "تقرير عن تنظيم حملة للتبرع بالدم", "order": 1},
    {"id": "hg_c1_s5_r002", "subcategory_id": "hg_c1_s5", "name": "سجل المشاركين في الحملة", "order": 2},
    {"id": "hg_c1_s5_r003", "subcategory_id": "hg_c1_s5", "name": "تقرير عن التنسيق مع مستشفى للتبرع", "order": 3},
    {"id": "hg_c1_s5_r004", "subcategory_id": "hg_c1_s5", "name": "توثيق الفعاليات المصاحبة", "order": 4},
    {"id": "hg_c1_s5_r005", "subcategory_id": "hg_c1_s5", "name": "تقرير عن أثر الحملة على الوعي الصحي", "order": 5},
    # hg_c2_s1
    {"id": "hg_c2_s1_r001", "subcategory_id": "hg_c2_s1", "name": "تقرير عن رصد حالات الأمراض المعدية", "order": 1},
    {"id": "hg_c2_s1_r002", "subcategory_id": "hg_c2_s1", "name": "سجل متابعة حالات العدوى", "order": 2},
    {"id": "hg_c2_s1_r003", "subcategory_id": "hg_c2_s1", "name": "تقرير عن إجراءات العزل المتبعة", "order": 3},
    {"id": "hg_c2_s1_r004", "subcategory_id": "hg_c2_s1", "name": "توثيق الإبلاغ عن الأمراض المعدية", "order": 4},
    {"id": "hg_c2_s1_r005", "subcategory_id": "hg_c2_s1", "name": "تقرير عن متابعة المخالطين", "order": 5},
    # hg_c2_s2
    {"id": "hg_c2_s2_r001", "subcategory_id": "hg_c2_s2", "name": "تقرير عن متابعة الطلاب المصابين بالسكري", "order": 1},
    {"id": "hg_c2_s2_r002", "subcategory_id": "hg_c2_s2", "name": "سجل متابعة الطلاب المصابين بالربو", "order": 2},
    {"id": "hg_c2_s2_r003", "subcategory_id": "hg_c2_s2", "name": "تقرير عن الطلاب ذوي الأمراض المزمنة", "order": 3},
    {"id": "hg_c2_s2_r004", "subcategory_id": "hg_c2_s2", "name": "توثيق خطط الرعاية للطلاب", "order": 4},
    {"id": "hg_c2_s2_r005", "subcategory_id": "hg_c2_s2", "name": "تقرير عن التنسيق مع أولياء الأمور بشأن الحالات المزمنة", "order": 5},
    # hg_c2_s3
    {"id": "hg_c2_s3_r001", "subcategory_id": "hg_c2_s3", "name": "تقرير عن تقديم الإسعافات الأولية للطلاب", "order": 1},
    {"id": "hg_c2_s3_r002", "subcategory_id": "hg_c2_s3", "name": "سجل حالات الإصابات والإسعافات", "order": 2},
    {"id": "hg_c2_s3_r003", "subcategory_id": "hg_c2_s3", "name": "تقرير عن تدريب الطلاب على الإسعافات", "order": 3},
    {"id": "hg_c2_s3_r004", "subcategory_id": "hg_c2_s3", "name": "توثيق صيانة حقيبة الإسعافات", "order": 4},
    {"id": "hg_c2_s3_r005", "subcategory_id": "hg_c2_s3", "name": "تقرير عن سرعة الاستجابة للحالات الطارئة", "order": 5},
    # hg_c2_s4
    {"id": "hg_c2_s4_r001", "subcategory_id": "hg_c2_s4", "name": "تقرير عن تحويل حالات للمستشفى", "order": 1},
    {"id": "hg_c2_s4_r002", "subcategory_id": "hg_c2_s4", "name": "سجل تحويل الحالات الصحية", "order": 2},
    {"id": "hg_c2_s4_r003", "subcategory_id": "hg_c2_s4", "name": "تقرير عن متابعة الحالات المحولة", "order": 3},
    {"id": "hg_c2_s4_r004", "subcategory_id": "hg_c2_s4", "name": "توثيق التنسيق مع الطواريء", "order": 4},
    {"id": "hg_c2_s4_r005", "subcategory_id": "hg_c2_s4", "name": "تقرير عن نتائج التحويل", "order": 5},
    # hg_c2_s5
    {"id": "hg_c2_s5_r001", "subcategory_id": "hg_c2_s5", "name": "تقرير عن توثيق السجلات الصحية للطلاب", "order": 1},
    {"id": "hg_c2_s5_r002", "subcategory_id": "hg_c2_s5", "name": "سجل تحديث السجلات الصحية", "order": 2},
    {"id": "hg_c2_s5_r003", "subcategory_id": "hg_c2_s5", "name": "تقرير عن تنظيم ملفات الطلاب الصحية", "order": 3},
    {"id": "hg_c2_s5_r004", "subcategory_id": "hg_c2_s5", "name": "توثيق إدخال البيانات في نظام نور الصحي", "order": 4},
    {"id": "hg_c2_s5_r005", "subcategory_id": "hg_c2_s5", "name": "تقرير عن مدى اكتمال السجلات", "order": 5},
    # hg_c3_s1
    {"id": "hg_c3_s1_r001", "subcategory_id": "hg_c3_s1", "name": "تقرير عن الإشراف على نظافة المدرسة", "order": 1},
    {"id": "hg_c3_s1_r002", "subcategory_id": "hg_c3_s1", "name": "سجل جولات تفقد النظافة", "order": 2},
    {"id": "hg_c3_s1_r003", "subcategory_id": "hg_c3_s1", "name": "تقرير عن التعاون مع مشرف النظافة", "order": 3},
    {"id": "hg_c3_s1_r004", "subcategory_id": "hg_c3_s1", "name": "توثيق حملات النظافة المدرسية", "order": 4},
    {"id": "hg_c3_s1_r005", "subcategory_id": "hg_c3_s1", "name": "تقرير عن نتائج تحسين النظافة", "order": 5},
    # hg_c3_s2
    {"id": "hg_c3_s2_r001", "subcategory_id": "hg_c3_s2", "name": "تقرير عن متابعة المقصف المدرسي", "order": 1},
    {"id": "hg_c3_s2_r002", "subcategory_id": "hg_c3_s2", "name": "سجل زيارات تفتيش المقصف", "order": 2},
    {"id": "hg_c3_s2_r003", "subcategory_id": "hg_c3_s2", "name": "تقرير عن عينات الأغذية المقدمة", "order": 3},
    {"id": "hg_c3_s2_r004", "subcategory_id": "hg_c3_s2", "name": "توثيق توعية العاملين بالمقصف", "order": 4},
    {"id": "hg_c3_s2_r005", "subcategory_id": "hg_c3_s2", "name": "تقرير عن التزام المقصف بالاشتراطات", "order": 5},
    # hg_c3_s3
    {"id": "hg_c3_s3_r001", "subcategory_id": "hg_c3_s3", "name": "تقرير عن متابعة تهوية الفصول", "order": 1},
    {"id": "hg_c3_s3_r002", "subcategory_id": "hg_c3_s3", "name": "سجل قياس جودة الهواء", "order": 2},
    {"id": "hg_c3_s3_r003", "subcategory_id": "hg_c3_s3", "name": "تقرير عن صيانة أجهزة التكييف", "order": 3},
    {"id": "hg_c3_s3_r004", "subcategory_id": "hg_c3_s3", "name": "توثيق توصيات بتحسين التهوية", "order": 4},
    {"id": "hg_c3_s3_r005", "subcategory_id": "hg_c3_s3", "name": "تقرير عن رضا الطلاب عن البيئة الصفية", "order": 5},
    # hg_c3_s4
    {"id": "hg_c3_s4_r001", "subcategory_id": "hg_c3_s4", "name": "تقرير عن تنظيم حملة مكافحة الحشرات", "order": 1},
    {"id": "hg_c3_s4_r002", "subcategory_id": "hg_c3_s4", "name": "سجل متابعة الرش الدوري", "order": 2},
    {"id": "hg_c3_s4_r003", "subcategory_id": "hg_c3_s4", "name": "تقرير عن التنسيق مع البلدية", "order": 3},
    {"id": "hg_c3_s4_r004", "subcategory_id": "hg_c3_s4", "name": "توثيق وعي الطلاب بأضرار الحشرات", "order": 4},
    {"id": "hg_c3_s4_r005", "subcategory_id": "hg_c3_s4", "name": "تقرير عن نتائج المكافحة", "order": 5},
    # hg_c3_s5
    {"id": "hg_c3_s5_r001", "subcategory_id": "hg_c3_s5", "name": "تقرير عن برنامج تعزيز السلوكيات الصحية", "order": 1},
    {"id": "hg_c3_s5_r002", "subcategory_id": "hg_c3_s5", "name": "سجل أنشطة تعزيز الصحة", "order": 2},
    {"id": "hg_c3_s5_r003", "subcategory_id": "hg_c3_s5", "name": "تقرير عن مسابقات أفضل فصل صحي", "order": 3},
    {"id": "hg_c3_s5_r004", "subcategory_id": "hg_c3_s5", "name": "توثيق إجراءات تعزيز غسل اليدين", "order": 4},
    {"id": "hg_c3_s5_r005", "subcategory_id": "hg_c3_s5", "name": "تقرير عن التزام الطلاب بالسلوكيات الصحية", "order": 5},
    # hg_c4_s1
    {"id": "hg_c4_s1_r001", "subcategory_id": "hg_c4_s1", "name": "تقرير عن محاضرات التوعية بالتغذية السليمة", "order": 1},
    {"id": "hg_c4_s1_r002", "subcategory_id": "hg_c4_s1", "name": "سجل ورش عمل عن الغذاء الصحي", "order": 2},
    {"id": "hg_c4_s1_r003", "subcategory_id": "hg_c4_s1", "name": "تقرير عن حملة الغذاء الصحي", "order": 3},
    {"id": "hg_c4_s1_r004", "subcategory_id": "hg_c4_s1", "name": "توثيق توزيع نشرات عن التغذية", "order": 4},
    {"id": "hg_c4_s1_r005", "subcategory_id": "hg_c4_s1", "name": "تقرير عن تحسن عادات الطلاب الغذائية", "order": 5},
    # hg_c4_s2
    {"id": "hg_c4_s2_r001", "subcategory_id": "hg_c4_s2", "name": "تقرير عن ورش النظافة الشخصية للطلاب", "order": 1},
    {"id": "hg_c4_s2_r002", "subcategory_id": "hg_c4_s2", "name": "سجل محاضرات عن العناية بالأسنان", "order": 2},
    {"id": "hg_c4_s2_r003", "subcategory_id": "hg_c4_s2", "name": "تقرير عن توزيع فرش ومعجون أسنان", "order": 3},
    {"id": "hg_c4_s2_r004", "subcategory_id": "hg_c4_s2", "name": "توثيق فعاليات يوم النظافة العالمي", "order": 4},
    {"id": "hg_c4_s2_r005", "subcategory_id": "hg_c4_s2", "name": "تقرير عن التزام الطلاب بالنظافة الشخصية", "order": 5},
    # hg_c4_s3
    {"id": "hg_c4_s3_r001", "subcategory_id": "hg_c4_s3", "name": "تقرير عن توعية الطلاب بالسكري", "order": 1},
    {"id": "hg_c4_s3_r002", "subcategory_id": "hg_c4_s3", "name": "سجل محاضرات عن ضغط الدم", "order": 2},
    {"id": "hg_c4_s3_r003", "subcategory_id": "hg_c4_s3", "name": "تقرير عن الربو وكيفية التعامل معه", "order": 3},
    {"id": "hg_c4_s3_r004", "subcategory_id": "hg_c4_s3", "name": "توثيق نشرات توعوية عن الأمراض المزمنة", "order": 4},
    {"id": "hg_c4_s3_r005", "subcategory_id": "hg_c4_s3", "name": "تقرير عن وعي الطلاب بالأمراض المزمنة", "order": 5},
    # hg_c4_s4
    {"id": "hg_c4_s4_r001", "subcategory_id": "hg_c4_s4", "name": "تقرير عن توعية الطلاب بالصحة النفسية", "order": 1},
    {"id": "hg_c4_s4_r002", "subcategory_id": "hg_c4_s4", "name": "سجل ورش عن إدارة التوتر", "order": 2},
    {"id": "hg_c4_s4_r003", "subcategory_id": "hg_c4_s4", "name": "تقرير عن التعاون مع المرشد الطلابي", "order": 3},
    {"id": "hg_c4_s4_r004", "subcategory_id": "hg_c4_s4", "name": "توثيق يوم الصحة النفسية", "order": 4},
    {"id": "hg_c4_s4_r005", "subcategory_id": "hg_c4_s4", "name": "تقرير عن تحسن الصحة النفسية للطلاب", "order": 5},
    # hg_c4_s5
    {"id": "hg_c4_s5_r001", "subcategory_id": "hg_c4_s5", "name": "تقرير عن تدريب الطلاب على الإسعافات الأولية", "order": 1},
    {"id": "hg_c4_s5_r002", "subcategory_id": "hg_c4_s5", "name": "سجل ورش عملية عن الإسعافات", "order": 2},
    {"id": "hg_c4_s5_r003", "subcategory_id": "hg_c4_s5", "name": "تقرير عن مسابقة في الإسعافات الأولية", "order": 3},
    {"id": "hg_c4_s5_r004", "subcategory_id": "hg_c4_s5", "name": "توثيق توزيع كتيبات إسعافات", "order": 4},
    {"id": "hg_c4_s5_r005", "subcategory_id": "hg_c4_s5", "name": "تقرير عن استعداد الطلاب للطوارئ", "order": 5},
    # hg_c5_s1
    {"id": "hg_c5_s1_r001", "subcategory_id": "hg_c5_s1", "name": "تقرير عن التنسيق مع المركز الصحي", "order": 1},
    {"id": "hg_c5_s1_r002", "subcategory_id": "hg_c5_s1", "name": "سجل اجتماعات مع فريق الصحة المدرسية", "order": 2},
    {"id": "hg_c5_s1_r003", "subcategory_id": "hg_c5_s1", "name": "تقرير عن تنفيذ برامج مشتركة مع المركز الصحي", "order": 3},
    {"id": "hg_c5_s1_r004", "subcategory_id": "hg_c5_s1", "name": "توثيق إحالة طلاب للمركز الصحي", "order": 4},
    {"id": "hg_c5_s1_r005", "subcategory_id": "hg_c5_s1", "name": "تقرير عن متابعة الحالات المحولة", "order": 5},
    # hg_c5_s2
    {"id": "hg_c5_s2_r001", "subcategory_id": "hg_c5_s2", "name": "تقرير عن التعاون مع مستشفى المنطقة", "order": 1},
    {"id": "hg_c5_s2_r002", "subcategory_id": "hg_c5_s2", "name": "سجل تنظيم زيارات طلابية للمستشفى", "order": 2},
    {"id": "hg_c5_s2_r003", "subcategory_id": "hg_c5_s2", "name": "تقرير عن حملات توعية مع المستشفى", "order": 3},
    {"id": "hg_c5_s2_r004", "subcategory_id": "hg_c5_s2", "name": "توثيق مشاركة أطباء في محاضرات بالمدرسة", "order": 4},
    {"id": "hg_c5_s2_r005", "subcategory_id": "hg_c5_s2", "name": "تقرير عن استفادة المدرسة من التعاون", "order": 5},
    # hg_c5_s3
    {"id": "hg_c5_s3_r001", "subcategory_id": "hg_c5_s3", "name": "تقرير عن متابعة حملات التوعية مع هيئة الغذاء والدواء", "order": 1},
    {"id": "hg_c5_s3_r002", "subcategory_id": "hg_c5_s3", "name": "سجل مشاركة في حملات وطنية للتوعية الصحية", "order": 2},
    {"id": "hg_c5_s3_r003", "subcategory_id": "hg_c5_s3", "name": "تقرير عن تفعيل اليوم العالمي للصحة", "order": 3},
    {"id": "hg_c5_s3_r004", "subcategory_id": "hg_c5_s3", "name": "توثيق استضافة جهات خارجية لتوعية الطلاب", "order": 4},
    {"id": "hg_c5_s3_r005", "subcategory_id": "hg_c5_s3", "name": "تقرير عن أثر الحملات على وعي الطلاب", "order": 5},
    # hg_c5_s4
    {"id": "hg_c5_s4_r001", "subcategory_id": "hg_c5_s4", "name": "تقرير عن المشاركة في لجنة الصحة المدرسية", "order": 1},
    {"id": "hg_c5_s4_r002", "subcategory_id": "hg_c5_s4", "name": "سجل اجتماعات اللجنة", "order": 2},
    {"id": "hg_c5_s4_r003", "subcategory_id": "hg_c5_s4", "name": "تقرير عن توصيات اللجنة وتنفيذها", "order": 3},
    {"id": "hg_c5_s4_r004", "subcategory_id": "hg_c5_s4", "name": "توثيق متابعة قرارات اللجنة", "order": 4},
    {"id": "hg_c5_s4_r005", "subcategory_id": "hg_c5_s4", "name": "تقرير عن تقييم أداء اللجنة", "order": 5},
    # hg_c5_s5
    {"id": "hg_c5_s5_r001", "subcategory_id": "hg_c5_s5", "name": "تقرير عن التنسيق مع الصحة العامة في الأوبئة", "order": 1},
    {"id": "hg_c5_s5_r002", "subcategory_id": "hg_c5_s5", "name": "سجل متابعة تعاميم وزارة الصحة", "order": 2},
    {"id": "hg_c5_s5_r003", "subcategory_id": "hg_c5_s5", "name": "تقرير عن تنفيذ إجراءات مكافحة العدوى", "order": 3},
    {"id": "hg_c5_s5_r004", "subcategory_id": "hg_c5_s5", "name": "توثيق الإبلاغ عن الأمراض المعدية", "order": 4},
    {"id": "hg_c5_s5_r005", "subcategory_id": "hg_c5_s5", "name": "تقرير عن التعاون مع فرق التقصي الوبائي", "order": 5}
]

HEALTH_GUIDE_PROMPT_TEMPLATE = """أنت موجه صحي مسؤول عن تنفيذ البرامج الصحية المدرسية وتعزيز بيئة تعليمية آمنة وفق الأنظمة المعتمدة.

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
- لغة إدارية صحية رسمية.
- إبراز دورك في الوقاية والتوعية والمتابعة الصحية.
- توضيح آلية تنفيذ البرامج الصحية المدرسية.
- الإشارة إلى رصد الحالات الصحية والتنسيق مع الجهات المختصة.
- بيان دورك في تهيئة بيئة مدرسية آمنة وصحية.
- إبراز استخدام التقنية أو النماذج المعتمدة في التوثيق.
- توضيح أثر الجهود على سلامة الطلاب واستقرار العملية التعليمية.
- صياغة عملية دقيقة من 5–7 أسطر.

**الحقول المطلوبة:**
1. الهدف التربوي
2. نبذة مختصرة
3. إجراءات التنفيذ
4. الاستراتيجيات المستخدمة
5. نقاط القوة
6. نقاط التحسين
7. التوصيات

يرجى تقديم الإجابة باللغة العربية الفصحى، وتنظيمها بحيث يكون كل حقل في سطر منفصل يبدأ برقمه فقط دون ذكر العنوان."""