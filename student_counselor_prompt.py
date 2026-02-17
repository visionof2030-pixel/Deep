# student_counselor_prompt.py

SG_CRITERIA = [
    {"id": "sg_c1", "name": "تقديم الإرشاد الفردي والجماعي للطلاب", "weight": "10%", "order": 1},
    {"id": "sg_c2", "name": "متابعة الحالات السلوكية والنفسية", "weight": "10%", "order": 2},
    {"id": "sg_c3", "name": "تنفيذ برامج وقائية وتوعوية", "weight": "10%", "order": 3},
    {"id": "sg_c4", "name": "التنسيق مع أولياء الأمور والمعلمين", "weight": "10%", "order": 4},
    {"id": "sg_c5", "name": "توثيق الحالات وإعداد التقارير", "weight": "10%", "order": 5}
]

SG_SUBCATEGORIES = [
    # sg_c1
    {"id": "sg_c1_s1", "criterion_id": "sg_c1", "name": "إجراء مقابلات فردية مع الطلاب", "order": 1},
    {"id": "sg_c1_s2", "criterion_id": "sg_c1", "name": "تقديم إرشاد جماعي (ورش, مجموعات)", "order": 2},
    {"id": "sg_c1_s3", "criterion_id": "sg_c1", "name": "تقديم استشارات أكاديمية ومهنية", "order": 3},
    {"id": "sg_c1_s4", "criterion_id": "sg_c1", "name": "توجيه الطلاب ذوي الميول الخاصة", "order": 4},
    {"id": "sg_c1_s5", "criterion_id": "sg_c1", "name": "تعزيز الثقة بالنفس لدى الطلاب", "order": 5},
    # sg_c2
    {"id": "sg_c2_s1", "criterion_id": "sg_c2", "name": "دراسة الحالات الفردية وتشخيصها", "order": 1},
    {"id": "sg_c2_s2", "criterion_id": "sg_c2", "name": "التدخل في حالات التنمر والعنف", "order": 2},
    {"id": "sg_c2_s3", "criterion_id": "sg_c2", "name": "متابعة الطلاب المعرضين للخطر", "order": 3},
    {"id": "sg_c2_s4", "criterion_id": "sg_c2", "name": "التعامل مع القلق والاكتئاب", "order": 4},
    {"id": "sg_c2_s5", "criterion_id": "sg_c2", "name": "إحالة الحالات لمختصين عند الحاجة", "order": 5},
    # sg_c3
    {"id": "sg_c3_s1", "criterion_id": "sg_c3", "name": "تنفيذ برامج توعوية عن أضرار التدخين", "order": 1},
    {"id": "sg_c3_s2", "criterion_id": "sg_c3", "name": "تنظيم محاضرات عن الأمن الفكري", "order": 2},
    {"id": "sg_c3_s3", "criterion_id": "sg_c3", "name": "برامج توعوية عن الاستخدام الآمن للإنترنت", "order": 3},
    {"id": "sg_c3_s4", "criterion_id": "sg_c3", "name": "توعية حول المهارات الحياتية", "order": 4},
    {"id": "sg_c3_s5", "criterion_id": "sg_c3", "name": "تنظيم حملات ضد التنمر", "order": 5},
    # sg_c4
    {"id": "sg_c4_s1", "criterion_id": "sg_c4", "name": "التنسيق مع المعلمين لمتابعة الطلاب", "order": 1},
    {"id": "sg_c4_s2", "criterion_id": "sg_c4", "name": "التواصل مع أولياء الأمور بشأن سلوك الطلاب", "order": 2},
    {"id": "sg_c4_s3", "criterion_id": "sg_c4", "name": "عقد اجتماعات مع أولياء الأمور", "order": 3},
    {"id": "sg_c4_s4", "criterion_id": "sg_c4", "name": "التنسيق مع الإدارة والجهات الخارجية", "order": 4},
    {"id": "sg_c4_s5", "criterion_id": "sg_c4", "name": "المشاركة في لجنة التوجيه والإرشاد", "order": 5},
    # sg_c5
    {"id": "sg_c5_s1", "criterion_id": "sg_c5", "name": "توثيق الحالات الفردية وحفظها", "order": 1},
    {"id": "sg_c5_s2", "criterion_id": "sg_c5", "name": "إعداد تقارير دورية عن الأنشطة الإرشادية", "order": 2},
    {"id": "sg_c5_s3", "criterion_id": "sg_c5", "name": "تحليل البيانات السلوكية", "order": 3},
    {"id": "sg_c5_s4", "criterion_id": "sg_c5", "name": "رفع التقارير للإدارة", "order": 4},
    {"id": "sg_c5_s5", "criterion_id": "sg_c5", "name": "توثيق البرامج الوقائية المنفذة", "order": 5}
]

SG_REPORTS = [
    # sg_c1_s1
    {"id": "sg_c1_s1_r001", "subcategory_id": "sg_c1_s1", "name": "تقرير عن إجراء مقابلات فردية مع طلاب يعانون من صعوبات", "order": 1},
    {"id": "sg_c1_s1_r002", "subcategory_id": "sg_c1_s1", "name": "سجل استقبال الطلاب في مكتب الإرشاد", "order": 2},
    {"id": "sg_c1_s1_r003", "subcategory_id": "sg_c1_s1", "name": "تقرير عن متابعة حالة طالب موهوب", "order": 3},
    {"id": "sg_c1_s1_r004", "subcategory_id": "sg_c1_s1", "name": "توثيق مقابلات مع طلاب من ذوي الاحتياجات الخاصة", "order": 4},
    {"id": "sg_c1_s1_r005", "subcategory_id": "sg_c1_s1", "name": "تقرير عن جلسات إرشادية فردية لتحسين التحصيل", "order": 5},
    # sg_c1_s2
    {"id": "sg_c1_s2_r001", "subcategory_id": "sg_c1_s2", "name": "تقرير عن ورش عمل جماعية لتنمية المهارات الاجتماعية", "order": 1},
    {"id": "sg_c1_s2_r002", "subcategory_id": "sg_c1_s2", "name": "سجل إرشاد جماعي لمجموعة من الطلاب", "order": 2},
    {"id": "sg_c1_s2_r003", "subcategory_id": "sg_c1_s2", "name": "تقرير عن برنامج تدريب الطلاب على حل المشكلات", "order": 3},
    {"id": "sg_c1_s2_r004", "subcategory_id": "sg_c1_s2", "name": "توثيق جلسات جماعية للتوجيه المهني", "order": 4},
    {"id": "sg_c1_s2_r005", "subcategory_id": "sg_c1_s2", "name": "تقرير عن فعالية الإرشاد الجماعي في تحسين السلوك", "order": 5},
    # sg_c1_s3
    {"id": "sg_c1_s3_r001", "subcategory_id": "sg_c1_s3", "name": "تقرير عن تقديم استشارات أكاديمية لطلاب الثانوي", "order": 1},
    {"id": "sg_c1_s3_r002", "subcategory_id": "sg_c1_s3", "name": "سجل توجيه طلاب لتخصصات مهنية", "order": 2},
    {"id": "sg_c1_s3_r003", "subcategory_id": "sg_c1_s3", "name": "تقرير عن مساعدة الطلاب في اختيار المسار", "order": 3},
    {"id": "sg_c1_s3_r004", "subcategory_id": "sg_c1_s3", "name": "توثيق استشارات حول الجامعات والكليات", "order": 4},
    {"id": "sg_c1_s3_r005", "subcategory_id": "sg_c1_s3", "name": "تقرير عن أثر الإرشاد الأكاديمي على قرارات الطلاب", "order": 5},
    # sg_c1_s4
    {"id": "sg_c1_s4_r001", "subcategory_id": "sg_c1_s4", "name": "تقرير عن توجيه الطلاب ذوي الميول الفنية", "order": 1},
    {"id": "sg_c1_s4_r002", "subcategory_id": "sg_c1_s4", "name": "سجل متابعة الطلاب الموهوبين", "order": 2},
    {"id": "sg_c1_s4_r003", "subcategory_id": "sg_c1_s4", "name": "تقرير عن توجيه طلاب لتطوير مهاراتهم القيادية", "order": 3},
    {"id": "sg_c1_s4_r004", "subcategory_id": "sg_c1_s4", "name": "توثيق برامج لاكتشاف المواهب", "order": 4},
    {"id": "sg_c1_s4_r005", "subcategory_id": "sg_c1_s4", "name": "تقرير عن فعالية برامج تنمية الموهوبين", "order": 5},
    # sg_c1_s5
    {"id": "sg_c1_s5_r001", "subcategory_id": "sg_c1_s5", "name": "تقرير عن جلسات تعزيز الثقة بالنفس", "order": 1},
    {"id": "sg_c1_s5_r002", "subcategory_id": "sg_c1_s5", "name": "سجل أنشطة لتحسين صورة الذات لدى الطلاب", "order": 2},
    {"id": "sg_c1_s5_r003", "subcategory_id": "sg_c1_s5", "name": "تقرير عن برنامج 'أنا أستطيع'", "order": 3},
    {"id": "sg_c1_s5_r004", "subcategory_id": "sg_c1_s5", "name": "توثيق نتائج قياس الثقة بالنفس", "order": 4},
    {"id": "sg_c1_s5_r005", "subcategory_id": "sg_c1_s5", "name": "تقرير عن أثر البرامج على تحصيل الطلاب", "order": 5},
    # sg_c2_s1
    {"id": "sg_c2_s1_r001", "subcategory_id": "sg_c2_s1", "name": "تقرير دراسة حالة طالب يعاني من صعوبات تعلم", "order": 1},
    {"id": "sg_c2_s1_r002", "subcategory_id": "sg_c2_s1", "name": "سجل تشخيص حالات فرط الحركة", "order": 2},
    {"id": "sg_c2_s1_r003", "subcategory_id": "sg_c2_s1", "name": "تقرير عن تحليل سلوك طالب عدواني", "order": 3},
    {"id": "sg_c2_s1_r004", "subcategory_id": "sg_c2_s1", "name": "توثيق أدوات التشخيص المستخدمة", "order": 4},
    {"id": "sg_c2_s1_r005", "subcategory_id": "sg_c2_s1", "name": "تقرير عن فريق دراسة الحالة", "order": 5},
    # sg_c2_s2
    {"id": "sg_c2_s2_r001", "subcategory_id": "sg_c2_s2", "name": "تقرير عن التدخل في حالة تنمر", "order": 1},
    {"id": "sg_c2_s2_r002", "subcategory_id": "sg_c2_s2", "name": "سجل متابعة طالب متورط في مشاجرة", "order": 2},
    {"id": "sg_c2_s2_r003", "subcategory_id": "sg_c2_s2", "name": "تقرير عن برنامج تعديل سلوك لطالب عدواني", "order": 3},
    {"id": "sg_c2_s2_r004", "subcategory_id": "sg_c2_s2", "name": "توثيق اجتماعات مع أولياء الأمور بسبب سلوك", "order": 4},
    {"id": "sg_c2_s2_r005", "subcategory_id": "sg_c2_s2", "name": "تقرير عن نتائج التدخل السلوكي", "order": 5},
    # sg_c2_s3
    {"id": "sg_c2_s3_r001", "subcategory_id": "sg_c2_s3", "name": "تقرير عن متابعة طالب معرض للانقطاع عن المدرسة", "order": 1},
    {"id": "sg_c2_s3_r002", "subcategory_id": "sg_c2_s3", "name": "سجل زيارات منزلية لطلاب متغيبين", "order": 2},
    {"id": "sg_c2_s3_r003", "subcategory_id": "sg_c2_s3", "name": "تقرير عن متابعة طالب يعاني من إهمال أسري", "order": 3},
    {"id": "sg_c2_s3_r004", "subcategory_id": "sg_c2_s3", "name": "توثيق التنسيق مع خدمات حماية الطفل", "order": 4},
    {"id": "sg_c2_s3_r005", "subcategory_id": "sg_c2_s3", "name": "تقرير عن تحسن حالة طالب بعد المتابعة", "order": 5},
    # sg_c2_s4
    {"id": "sg_c2_s4_r001", "subcategory_id": "sg_c2_s4", "name": "تقرير عن جلسات دعم نفسي لطالب يعاني من قلق", "order": 1},
    {"id": "sg_c2_s4_r002", "subcategory_id": "sg_c2_s4", "name": "سجل متابعة طالب يعاني من اكتئاب", "order": 2},
    {"id": "sg_c2_s4_r003", "subcategory_id": "sg_c2_s4", "name": "تقرير عن استخدام تقنيات الاسترخاء مع الطلاب", "order": 3},
    {"id": "sg_c2_s4_r004", "subcategory_id": "sg_c2_s4", "name": "توثيق تحويل حالة لمرشد نفسي خارجي", "order": 4},
    {"id": "sg_c2_s4_r005", "subcategory_id": "sg_c2_s4", "name": "تقرير عن تحسن الحالة النفسية", "order": 5},
    # sg_c2_s5
    {"id": "sg_c2_s5_r001", "subcategory_id": "sg_c2_s5", "name": "تقرير عن إحالة طالب لطبيب نفسي", "order": 1},
    {"id": "sg_c2_s5_r002", "subcategory_id": "sg_c2_s5", "name": "سجل تحويل حالات لوحدة الخدمات", "order": 2},
    {"id": "sg_c2_s5_r003", "subcategory_id": "sg_c2_s5", "name": "تقرير عن التنسيق مع مستشفى الصحة النفسية", "order": 3},
    {"id": "sg_c2_s5_r004", "subcategory_id": "sg_c2_s5", "name": "توثيق متابعة حالة محولة", "order": 4},
    {"id": "sg_c2_s5_r005", "subcategory_id": "sg_c2_s5", "name": "تقرير عن إجراءات الإحالة والنتائج", "order": 5},
    # sg_c3_s1
    {"id": "sg_c3_s1_r001", "subcategory_id": "sg_c3_s1", "name": "تقرير عن برنامج توعوي عن أضرار التدخين", "order": 1},
    {"id": "sg_c3_s1_r002", "subcategory_id": "sg_c3_s1", "name": "سجل محاضرات عن مخاطر المخدرات", "order": 2},
    {"id": "sg_c3_s1_r003", "subcategory_id": "sg_c3_s1", "name": "تقرير عن مشاركة المدرسة في اليوم العالمي لمكافحة التدخين", "order": 3},
    {"id": "sg_c3_s1_r004", "subcategory_id": "sg_c3_s1", "name": "توثيق تعاون مع جمعية مكافحة التدخين", "order": 4},
    {"id": "sg_c3_s1_r005", "subcategory_id": "sg_c3_s1", "name": "تقرير عن وعي الطلاب بعد البرنامج", "order": 5},
    # sg_c3_s2
    {"id": "sg_c3_s2_r001", "subcategory_id": "sg_c3_s2", "name": "تقرير عن ندوة عن الأمن الفكري", "order": 1},
    {"id": "sg_c3_s2_r002", "subcategory_id": "sg_c3_s2", "name": "سجل محاضرات عن الوسطية والاعتدال", "order": 2},
    {"id": "sg_c3_s2_r003", "subcategory_id": "sg_c3_s2", "name": "تقرير عن برنامج التحذير من الأفكار المتطرفة", "order": 3},
    {"id": "sg_c3_s2_r004", "subcategory_id": "sg_c3_s2", "name": "توثيق مشاركة طلاب في مسابقات وطنية", "order": 4},
    {"id": "sg_c3_s2_r005", "subcategory_id": "sg_c3_s2", "name": "تقرير عن أثر البرنامج على وعي الطلاب", "order": 5},
    # sg_c3_s3
    {"id": "sg_c3_s3_r001", "subcategory_id": "sg_c3_s3", "name": "تقرير عن ورشة الاستخدام الآمن للإنترنت", "order": 1},
    {"id": "sg_c3_s3_r002", "subcategory_id": "sg_c3_s3", "name": "سجل محاضرات عن التنمر الإلكتروني", "order": 2},
    {"id": "sg_c3_s3_r003", "subcategory_id": "sg_c3_s3", "name": "تقرير عن برنامج حماية الخصوصية", "order": 3},
    {"id": "sg_c3_s3_r004", "subcategory_id": "sg_c3_s3", "name": "توثيق توزيع مطويات عن الأمن السيبراني", "order": 4},
    {"id": "sg_c3_s3_r005", "subcategory_id": "sg_c3_s3", "name": "تقرير عن تفاعل الطلاب مع البرنامج", "order": 5},
    # sg_c3_s4
    {"id": "sg_c3_s4_r001", "subcategory_id": "sg_c3_s4", "name": "تقرير عن برنامج تنمية المهارات الحياتية", "order": 1},
    {"id": "sg_c3_s4_r002", "subcategory_id": "sg_c3_s4", "name": "سجل ورش عمل عن حل المشكلات", "order": 2},
    {"id": "sg_c3_s4_r003", "subcategory_id": "sg_c3_s4", "name": "تقرير عن برنامج إدارة الوقت", "order": 3},
    {"id": "sg_c3_s4_r004", "subcategory_id": "sg_c3_s4", "name": "توثيق أنشطة عن التواصل الفعال", "order": 4},
    {"id": "sg_c3_s4_r005", "subcategory_id": "sg_c3_s4", "name": "تقرير عن تحسن مهارات الطلاب", "order": 5},
    # sg_c3_s5
    {"id": "sg_c3_s5_r001", "subcategory_id": "sg_c3_s5", "name": "تقرير عن حملة مكافحة التنمر", "order": 1},
    {"id": "sg_c3_s5_r002", "subcategory_id": "sg_c3_s5", "name": "سجل فعاليات اليوم العالمي لمكافحة التنمر", "order": 2},
    {"id": "sg_c3_s5_r003", "subcategory_id": "sg_c3_s5", "name": "تقرير عن ورش عمل للطلاب عن التنمر", "order": 3},
    {"id": "sg_c3_s5_r004", "subcategory_id": "sg_c3_s5", "name": "توثيق مسابقات للتوعية بالتنمر", "order": 4},
    {"id": "sg_c3_s5_r005", "subcategory_id": "sg_c3_s5", "name": "تقرير عن انخفاض حالات التنمر بعد الحملة", "order": 5},
    # sg_c4_s1
    {"id": "sg_c4_s1_r001", "subcategory_id": "sg_c4_s1", "name": "تقرير عن التنسيق مع معلمي الصفوف", "order": 1},
    {"id": "sg_c4_s1_r002", "subcategory_id": "sg_c4_s1", "name": "سجل اجتماعات مع المعلمين لمتابعة الطلاب", "order": 2},
    {"id": "sg_c4_s1_r003", "subcategory_id": "sg_c4_s1", "name": "تقرير عن تبادل المعلومات بين المرشد والمعلمين", "order": 3},
    {"id": "sg_c4_s1_r004", "subcategory_id": "sg_c4_s1", "name": "توثيق تقارير المعلمين عن الطلاب", "order": 4},
    {"id": "sg_c4_s1_r005", "subcategory_id": "sg_c4_s1", "name": "تقرير عن تحسن أداء الطلاب بفضل التعاون", "order": 5},
    # sg_c4_s2
    {"id": "sg_c4_s2_r001", "subcategory_id": "sg_c4_s2", "name": "تقرير عن التواصل مع أولياء الأمور بشأن سلوك الطالب", "order": 1},
    {"id": "sg_c4_s2_r002", "subcategory_id": "sg_c4_s2", "name": "سجل المكالمات الهاتفية مع أولياء الأمور", "order": 2},
    {"id": "sg_c4_s2_r003", "subcategory_id": "sg_c4_s2", "name": "تقرير عن اجتماعات مع أولياء الأمور لتحسين السلوك", "order": 3},
    {"id": "sg_c4_s2_r004", "subcategory_id": "sg_c4_s2", "name": "توثيق رسائل البريد الإلكتروني مع أولياء الأمور", "order": 4},
    {"id": "sg_c4_s2_r005", "subcategory_id": "sg_c4_s2", "name": "تقرير عن رضا أولياء الأمور عن متابعة المرشد", "order": 5},
    # sg_c4_s3
    {"id": "sg_c4_s3_r001", "subcategory_id": "sg_c4_s3", "name": "تقرير عن عقد اجتماعات مع أولياء الأمور", "order": 1},
    {"id": "sg_c4_s3_r002", "subcategory_id": "sg_c4_s3", "name": "سجل مجالس الآباء التي حضرها المرشد", "order": 2},
    {"id": "sg_c4_s3_r003", "subcategory_id": "sg_c4_s3", "name": "تقرير عن لقاءات توعوية لأولياء الأمور", "order": 3},
    {"id": "sg_c4_s3_r004", "subcategory_id": "sg_c4_s3", "name": "توثيق محاضر اجتماعات مع أولياء الأمور", "order": 4},
    {"id": "sg_c4_s3_r005", "subcategory_id": "sg_c4_s3", "name": "تقرير عن أثر الاجتماعات على متابعة أولياء الأمور", "order": 5},
    # sg_c4_s4
    {"id": "sg_c4_s4_r001", "subcategory_id": "sg_c4_s4", "name": "تقرير عن التنسيق مع الإدارة في قضايا الطلاب", "order": 1},
    {"id": "sg_c4_s4_r002", "subcategory_id": "sg_c4_s4", "name": "سجل التنسيق مع وحدة الخدمات الإرشادية", "order": 2},
    {"id": "sg_c4_s4_r003", "subcategory_id": "sg_c4_s4", "name": "تقرير عن التواصل مع مراكز الإرشاد الأسري", "order": 3},
    {"id": "sg_c4_s4_r004", "subcategory_id": "sg_c4_s4", "name": "توثيق خطابات التنسيق مع جهات خارجية", "order": 4},
    {"id": "sg_c4_s4_r005", "subcategory_id": "sg_c4_s4", "name": "تقرير عن فعالية التنسيق الخارجي", "order": 5},
    # sg_c4_s5
    {"id": "sg_c4_s5_r001", "subcategory_id": "sg_c4_s5", "name": "تقرير عن اجتماعات لجنة التوجيه والإرشاد", "order": 1},
    {"id": "sg_c4_s5_r002", "subcategory_id": "sg_c4_s5", "name": "سجل توصيات اللجنة ومتابعتها", "order": 2},
    {"id": "sg_c4_s5_r003", "subcategory_id": "sg_c4_s5", "name": "تقرير عن مساهمته في اللجنة", "order": 3},
    {"id": "sg_c4_s5_r004", "subcategory_id": "sg_c4_s5", "name": "توثيق محاضر اجتماعات اللجنة", "order": 4},
    {"id": "sg_c4_s5_r005", "subcategory_id": "sg_c4_s5", "name": "تقرير عن توصيات اللجنة المنفذة", "order": 5},
    # sg_c5_s1
    {"id": "sg_c5_s1_r001", "subcategory_id": "sg_c5_s1", "name": "تقرير عن توثيق حالات الطلاب في ملفات سرية", "order": 1},
    {"id": "sg_c5_s1_r002", "subcategory_id": "sg_c5_s1", "name": "سجل تحديث بيانات الحالات", "order": 2},
    {"id": "sg_c5_s1_r003", "subcategory_id": "sg_c5_s1", "name": "تقرير عن تنظيم أرشفة الحالات", "order": 3},
    {"id": "sg_c5_s1_r004", "subcategory_id": "sg_c5_s1", "name": "توثيق نموذج دراسة الحالة المستخدم", "order": 4},
    {"id": "sg_c5_s1_r005", "subcategory_id": "sg_c5_s1", "name": "تقرير عن مدى اكتمال ملفات الحالات", "order": 5},
    # sg_c5_s2
    {"id": "sg_c5_s2_r001", "subcategory_id": "sg_c5_s2", "name": "تقرير شهري عن أنشطة الإرشاد", "order": 1},
    {"id": "sg_c5_s2_r002", "subcategory_id": "sg_c5_s2", "name": "سجل إحصائي للحالات المستفيدة", "order": 2},
    {"id": "sg_c5_s2_r003", "subcategory_id": "sg_c5_s2", "name": "تقرير عن أعداد المستفيدين من البرامج", "order": 3},
    {"id": "sg_c5_s2_r004", "subcategory_id": "sg_c5_s2", "name": "توثيق تقارير نصف فصلية", "order": 4},
    {"id": "sg_c5_s2_r005", "subcategory_id": "sg_c5_s2", "name": "تقرير عن تطور الحالات خلال الفصل", "order": 5},
    # sg_c5_s3
    {"id": "sg_c5_s3_r001", "subcategory_id": "sg_c5_s3", "name": "تقرير تحليل بيانات الحالات السلوكية", "order": 1},
    {"id": "sg_c5_s3_r002", "subcategory_id": "sg_c5_s3", "name": "سجل مؤشرات الأداء الإرشادي", "order": 2},
    {"id": "sg_c5_s3_r003", "subcategory_id": "sg_c5_s3", "name": "تقرير إحصائي عن أنواع المشكلات", "order": 3},
    {"id": "sg_c5_s3_r004", "subcategory_id": "sg_c5_s3", "name": "توثيق نتائج استبيانات الرضا", "order": 4},
    {"id": "sg_c5_s3_r005", "subcategory_id": "sg_c5_s3", "name": "تقرير عن توصيات بناء على التحليل", "order": 5},
    # sg_c5_s4
    {"id": "sg_c5_s4_r001", "subcategory_id": "sg_c5_s4", "name": "تقرير عن رفع تقارير للإدارة", "order": 1},
    {"id": "sg_c5_s4_r002", "subcategory_id": "sg_c5_s4", "name": "سجل التقارير المرفوعة للإدارة", "order": 2},
    {"id": "sg_c5_s4_r003", "subcategory_id": "sg_c5_s4", "name": "تقرير عن متابعة توصيات الإدارة", "order": 3},
    {"id": "sg_c5_s4_r004", "subcategory_id": "sg_c5_s4", "name": "توثيق تقارير خاصة لقائد المدرسة", "order": 4},
    {"id": "sg_c5_s4_r005", "subcategory_id": "sg_c5_s4", "name": "تقرير عن أثر التقارير على قرارات الإدارة", "order": 5},
    # sg_c5_s5
    {"id": "sg_c5_s5_r001", "subcategory_id": "sg_c5_s5", "name": "تقرير عن توثيق البرامج الوقائية المنفذة", "order": 1},
    {"id": "sg_c5_s5_r002", "subcategory_id": "sg_c5_s5", "name": "سجل البرامج التوعوية", "order": 2},
    {"id": "sg_c5_s5_r003", "subcategory_id": "sg_c5_s5", "name": "تقرير عن عدد المستفيدين من البرامج", "order": 3},
    {"id": "sg_c5_s5_r004", "subcategory_id": "sg_c5_s5", "name": "توثيق صور من البرامج", "order": 4},
    {"id": "sg_c5_s5_r005", "subcategory_id": "sg_c5_s5", "name": "تقرير عن تقييم البرامج وأثرها", "order": 5}
]

STUDENT_GUIDE_PROMPT_TEMPLATE = """أنت موجه طلابي متخصص في التوجيه والإرشاد، وتعمل وفق المعايير المهنية المعتمدة لدعم النمو النفسي والتربوي للطلبة.

المطلوب:
- عرض معيار الأداء الوظيفي.
- عرض التصنيف الفرعي.
- كتابة تقرير مهني يوضح الممارسات والإجراءات المنفذة في هذا الجانب.

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
- لغة تربوية مهنية.
- إبراز دور الموجه في الوقاية، التدخل، والمتابعة.
- توضيح البرامج الإرشادية الفردية والجمعية عند الحاجة.
- بيان آلية دراسة الحالات وتصنيفها والتعامل معها.
- إبراز أثر الجهود على سلوك الطلبة وتحصيلهم ودافعيتهم.
- الإشارة إلى التعاون مع الأسرة والمعلمين والإدارة.
- توضيح جانب التوثيق وقياس الأثر والتحسين.
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