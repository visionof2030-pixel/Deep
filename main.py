# main.py
# الإصدار النهائي مع دعم JSON للمشرف التربوي

from fastapi import FastAPI, HTTPException, Depends, Header, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from pathlib import Path
from datetime import datetime
import os
import itertools
import json
from typing import Optional, Dict, Any

import google.generativeai as genai

from database import init_db, get_connection
from create_key import create_key
from key_logic import activation_required

# استيراد بيانات الأدوار والبرومبتات
from teacher_data import (
    TEACHER_CRITERIA,
    TEACHER_SUBCATEGORIES,
    TEACHER_REPORTS,
    TEACHER_PROMPT_TEMPLATE,
)
from vp_prompt import (
    VP_CRITERIA,
    VP_SUBCATEGORIES,
    VP_REPORTS,
    VICE_PRINCIPAL_PROMPT_TEMPLATE,
)
from student_counselor_prompt import (
    SG_CRITERIA,
    SG_SUBCATEGORIES,
    SG_REPORTS,
    STUDENT_GUIDE_PROMPT_TEMPLATE,
)
from health_guide_prompt import (
    HG_CRITERIA,
    HG_SUBCATEGORIES,
    HG_REPORTS,
    HEALTH_GUIDE_PROMPT_TEMPLATE,
)
from activity_leader_prompt import (
    AL_CRITERIA,
    AL_SUBCATEGORIES,
    AL_REPORTS,
    ACTIVITY_LEADER_PROMPT_TEMPLATE,
)

# استيراد بيانات الأدوار الجديدة
from kindergarten_teacher_prompt import (
    KG_CRITERIA,
    KG_SUBCATEGORIES,
    KG_REPORTS,
    KG_PROMPT_TEMPLATE,
)
from lab_preparer_prompt import (
    LAB_CRITERIA,
    LAB_SUBCATEGORIES,
    LAB_REPORTS,
    LAB_PROMPT_TEMPLATE,
)
from school_principal_prompt import (
    PRINCIPAL_CRITERIA,
    PRINCIPAL_SUBCATEGORIES,
    PRINCIPAL_REPORTS,
    PRINCIPAL_PROMPT_TEMPLATE,
)
from educational_supervisor_prompt import (
    SUPERVISOR_CRITERIA,
    SUPERVISOR_SUBCATEGORIES,
    SUPERVISOR_REPORTS,
    SUPERVISOR_ANALYTICAL_TEMPLATE,
    SUPERVISOR_PROJECT_TEMPLATE,
    SUPERVISOR_SUPPORT_TEMPLATE,
)

# ---------- تهيئة قاعدة البيانات ----------
init_db()

# ---------- تطبيق FastAPI ----------
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- مفتاح المشرف ----------
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN", "")

def admin_auth(x_admin_token: str = Header(...)):
    if x_admin_token != ADMIN_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")

# ---------- النماذج (Models) ----------
class Req(BaseModel):
    prompt: str

class GenerateKeyReq(BaseModel):
    plan: str

class GenerateReportRequest(BaseModel):
    criterion_id: Optional[str] = None
    subcategory_id: Optional[str] = None
    report_id: Optional[str] = None
    role: str = "teacher"
    report_data: Dict[str, Any] = {}

# ---------- خطط الاشتراك ----------
PLANS = {
    "5min_1":   {"minutes": 5,    "usage": 1},
    "15min_2":  {"minutes": 15,   "usage": 2},
    "30min_3":  {"minutes": 30,   "usage": 3},
    "1day_6":   {"days": 1,       "usage": 6},
    "3day_15":  {"days": 3,       "usage": 15},
    "7day_25":  {"days": 7,       "usage": 25},
    "1m_45":    {"days": 30,      "usage": 45},
    "2m_65":    {"days": 60,      "usage": 65},
    "3m_120":   {"days": 90,      "usage": 120},
    "5m_200":   {"days": 150,     "usage": 200},
}

# ---------- مفاتيح Gemini ----------
api_keys = [
    os.getenv("GEMINI_API_KEY_1"),
    os.getenv("GEMINI_API_KEY_2"),
    os.getenv("GEMINI_API_KEY_3"),
    os.getenv("GEMINI_API_KEY_4"),
    os.getenv("GEMINI_API_KEY_5"),
    os.getenv("GEMINI_API_KEY_6"),
    os.getenv("GEMINI_API_KEY_7"),
]
api_keys = [k for k in api_keys if k]
key_cycle = itertools.cycle(api_keys) if api_keys else None

def get_api_key():
    if not key_cycle:
        raise HTTPException(status_code=500, detail="No Gemini API key configured")
    return next(key_cycle)

# ============================================================================
# الأدوار المتاحة
# ============================================================================
ROLES = [
    {"id": "teacher", "name": "معلم"},
    {"id": "vice_principal", "name": "وكيل المدرسة"},
    {"id": "student_guide", "name": "الموجه الطلابي"},
    {"id": "health_guide", "name": "الموجه الصحي"},
    {"id": "activity_leader", "name": "رائد النشاط"},
    {"id": "kindergarten_teacher", "name": "معلمة رياض الأطفال"},
    {"id": "lab_preparer", "name": "محضر المختبر"},
    {"id": "school_principal", "name": "مدير المدرسة"},
    {"id": "educational_supervisor", "name": "المشرف التربوي"},
]

# ============================================================================
# دمج جميع القوائم للبحث
# ============================================================================
ALL_CRITERIA = (
    TEACHER_CRITERIA
    + VP_CRITERIA
    + SG_CRITERIA
    + HG_CRITERIA
    + AL_CRITERIA
    + KG_CRITERIA
    + LAB_CRITERIA
    + PRINCIPAL_CRITERIA
    + SUPERVISOR_CRITERIA
)
ALL_SUBCATEGORIES = (
    TEACHER_SUBCATEGORIES
    + VP_SUBCATEGORIES
    + SG_SUBCATEGORIES
    + HG_SUBCATEGORIES
    + AL_SUBCATEGORIES
    + KG_SUBCATEGORIES
    + LAB_SUBCATEGORIES
    + PRINCIPAL_SUBCATEGORIES
    + SUPERVISOR_SUBCATEGORIES
)
ALL_REPORTS = (
    TEACHER_REPORTS
    + VP_REPORTS
    + SG_REPORTS
    + HG_REPORTS
    + AL_REPORTS
    + KG_REPORTS
    + LAB_REPORTS
    + PRINCIPAL_REPORTS
    + SUPERVISOR_REPORTS
)

# ============================================================================
# بيانات ثابتة (إدارات، مواد، صفوف، ...)
# ============================================================================
EDUCATION_OFFICES = [ ... ]  # (كما هي)
SCHOOL_SUBJECTS = [ ... ]     # (كما هي)
SCHOOL_GRADES = [ ... ]       # (كما هي)
TARGET_AUDIENCES = [ ... ]    # (كما هي)
IMPLEMENTATION_PLACES = [ ... ]  # (كما هي)
EDUCATIONAL_TOOLS = [ ... ]   # (كما هي)

# ============================================================================
# دالة بناء البرومبت (مع دعم JSON للمشرف التربوي)
# ============================================================================
def build_ai_prompt(
    role: str,
    report_name: str,
    subcategory_name: str,
    criterion_name: str,
    criterion_percentage: str = "",
    report_data: dict = None,
):
    if not report_data:
        report_data = {}

    subject_line = report_data.get("subject", "")
    lesson_line = report_data.get("lesson", "")
    grade_line = report_data.get("grade", "")
    target_line = report_data.get("target", "")
    place_line = report_data.get("place", "")
    count_line = report_data.get("count", "")
    field = report_data.get("field", "")
    initiative = report_data.get("initiative", "")
    duration = report_data.get("duration", "")

    # قوالب الأدوار الأخرى (نصية)
    templates = {
        "teacher": TEACHER_PROMPT_TEMPLATE,
        "vice_principal": VICE_PRINCIPAL_PROMPT_TEMPLATE,
        "student_guide": STUDENT_GUIDE_PROMPT_TEMPLATE,
        "health_guide": HEALTH_GUIDE_PROMPT_TEMPLATE,
        "activity_leader": ACTIVITY_LEADER_PROMPT_TEMPLATE,
        "kindergarten_teacher": KG_PROMPT_TEMPLATE,
        "lab_preparer": LAB_PROMPT_TEMPLATE,
        "school_principal": PRINCIPAL_PROMPT_TEMPLATE,
    }

    # المشرف التربوي: استخدام قوالب JSON
    if role == "educational_supervisor":
        report_lower = report_name.lower()
        if any(word in report_lower for word in ["تحليل", "مؤشر", "نتائج", "قياس", "اتجاهات"]):
            template = SUPERVISOR_ANALYTICAL_TEMPLATE
        elif any(word in report_lower for word in ["مبادرة", "مشروع", "برنامج", "تطبيق", "تنفيذ"]):
            template = SUPERVISOR_PROJECT_TEMPLATE
        else:
            template = SUPERVISOR_SUPPORT_TEMPLATE

        return template.format(
            report_name=report_name,
            subcategory_name=subcategory_name,
            criterion_name=criterion_name,
            criterion_percentage=criterion_percentage,
            subject_line=subject_line,
            grade_line=grade_line,
            target_line=target_line,
            place_line=place_line,
            count_line=count_line,
            field=field,
            initiative=initiative,
            duration=duration,
        )

    # باقي الأدوار (النصية)
    template = templates.get(role, TEACHER_PROMPT_TEMPLATE)
    return template.format(
        report_name=report_name,
        subcategory_name=subcategory_name,
        criterion_name=criterion_name,
        criterion_percentage=criterion_percentage,
        subject_line=subject_line,
        lesson_line=lesson_line,
        grade_line=grade_line,
        target_line=target_line,
        place_line=place_line,
        count_line=count_line,
        field=field,
        initiative=initiative,
        duration=duration,
    )

# ============================================================================
# دوال مساعدة للبحث
# ============================================================================
def get_criterion_by_id(criterion_id: str):
    for c in ALL_CRITERIA:
        if c["id"] == criterion_id:
            return c
    return None

def get_subcategory_by_id(subcategory_id: str):
    for s in ALL_SUBCATEGORIES:
        if s["id"] == subcategory_id:
            return s
    return None

def get_report_by_id(report_id: str):
    for r in ALL_REPORTS:
        if r["id"] == report_id:
            return r
    return None

def get_subcategories_by_criterion(criterion_id: str):
    return [s for s in ALL_SUBCATEGORIES if s["criterion_id"] == criterion_id]

def get_reports_by_subcategory(subcategory_id: str):
    return [r for r in ALL_REPORTS if r["subcategory_id"] == subcategory_id]

def get_criteria_by_role(role: str):
    if role == "teacher":
        return TEACHER_CRITERIA
    elif role == "vice_principal":
        return VP_CRITERIA
    elif role == "student_guide":
        return SG_CRITERIA
    elif role == "health_guide":
        return HG_CRITERIA
    elif role == "activity_leader":
        return AL_CRITERIA
    elif role == "kindergarten_teacher":
        return KG_CRITERIA
    elif role == "lab_preparer":
        return LAB_CRITERIA
    elif role == "school_principal":
        return PRINCIPAL_CRITERIA
    elif role == "educational_supervisor":
        return SUPERVISOR_CRITERIA
    else:
        return TEACHER_CRITERIA

def get_subcategories_by_role(role: str):
    if role == "teacher":
        return TEACHER_SUBCATEGORIES
    elif role == "vice_principal":
        return VP_SUBCATEGORIES
    elif role == "student_guide":
        return SG_SUBCATEGORIES
    elif role == "health_guide":
        return HG_SUBCATEGORIES
    elif role == "activity_leader":
        return AL_SUBCATEGORIES
    elif role == "kindergarten_teacher":
        return KG_SUBCATEGORIES
    elif role == "lab_preparer":
        return LAB_SUBCATEGORIES
    elif role == "school_principal":
        return PRINCIPAL_SUBCATEGORIES
    elif role == "educational_supervisor":
        return SUPERVISOR_SUBCATEGORIES
    else:
        return TEACHER_SUBCATEGORIES

def get_reports_by_role(role: str):
    if role == "teacher":
        return TEACHER_REPORTS
    elif role == "vice_principal":
        return VP_REPORTS
    elif role == "student_guide":
        return SG_REPORTS
    elif role == "health_guide":
        return HG_REPORTS
    elif role == "activity_leader":
        return AL_REPORTS
    elif role == "kindergarten_teacher":
        return KG_REPORTS
    elif role == "lab_preparer":
        return LAB_REPORTS
    elif role == "school_principal":
        return PRINCIPAL_REPORTS
    elif role == "educational_supervisor":
        return SUPERVISOR_REPORTS
    else:
        return TEACHER_REPORTS

# ============================================================================
# المسارات العامة
# ============================================================================
@app.get("/")
def root():
    return {"status": "running", "message": "Teacher Reports API"}

@app.get("/health")
def health(_: int = Depends(activation_required)):
    return {"status": "ok"}

@app.get("/subscription/status")
def subscription_status(code_id: int = Depends(activation_required)):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT started_at, expires_at, duration_minutes, duration_days, usage_limit, usage_count
        FROM activation_codes WHERE id = ?
        """,
        (code_id,),
    )
    row = cur.fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Subscription not found")
    (started_at, expires_at, duration_minutes, duration_days, usage_limit, usage_count) = row
    now = datetime.utcnow()
    expired = False
    remaining_seconds = None
    if expires_at:
        expiry = datetime.fromisoformat(expires_at)
        if expiry < now:
            expired = True
        else:
            remaining_seconds = int((expiry - now).total_seconds())
    if usage_limit is not None and usage_count >= usage_limit:
        expired = True
    return {
        "started_at": started_at,
        "expires_at": expires_at,
        "duration_minutes": duration_minutes,
        "duration_days": duration_days,
        "usage_limit": usage_limit,
        "usage_used": usage_count,
        "usage_remaining": max(usage_limit - usage_count, 0) if usage_limit is not None else None,
        "remaining_seconds": remaining_seconds,
        "expired": expired,
    }

@app.post("/ask")
def ask(req: Req, code_id: int = Depends(activation_required)):
    try:
        genai.configure(api_key=get_api_key())
        model = genai.GenerativeModel("models/gemini-2.5-flash-lite")
        response = model.generate_content(req.prompt)
        answer = response.text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"فشل الاتصال بالذكاء الاصطناعي: {str(e)}")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE activation_codes
        SET usage_count = usage_count + 1, last_used_at = ?
        WHERE id = ? AND (usage_limit IS NULL OR usage_count < usage_limit)
        """,
        (datetime.utcnow().isoformat(), code_id),
    )
    if cur.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=403, detail="تم استهلاك جميع الاستخدامات المسموحة")
    conn.commit()
    conn.close()
    return {"answer": answer}

# ============================================================================
# مسارات البيانات (API)
# ============================================================================
@app.get("/api/roles")
def get_roles():
    return ROLES

@app.get("/api/criteria")
def get_all_criteria(role: str = Query("teacher")):
    criteria = get_criteria_by_role(role)
    return {"criteria": criteria, "role": role}

@app.get("/api/criteria/{criterion_id}")
def get_criterion(criterion_id: str):
    criterion = get_criterion_by_id(criterion_id)
    if not criterion:
        raise HTTPException(status_code=404, detail="Criterion not found")
    return criterion

@app.get("/api/criteria/{criterion_id}/subcategories")
def get_subcategories(criterion_id: str):
    criterion = get_criterion_by_id(criterion_id)
    if not criterion:
        raise HTTPException(status_code=404, detail="Criterion not found")
    subcategories = get_subcategories_by_criterion(criterion_id)
    return {"criterion": criterion, "subcategories": subcategories}

@app.get("/api/subcategories/{subcategory_id}")
def get_subcategory(subcategory_id: str):
    subcategory = get_subcategory_by_id(subcategory_id)
    if not subcategory:
        raise HTTPException(status_code=404, detail="Subcategory not found")
    return subcategory

@app.get("/api/subcategories/{subcategory_id}/reports")
def get_reports(subcategory_id: str):
    subcategory = get_subcategory_by_id(subcategory_id)
    if not subcategory:
        raise HTTPException(status_code=404, detail="Subcategory not found")
    reports = get_reports_by_subcategory(subcategory_id)
    return {"subcategory": subcategory, "reports": reports}

@app.get("/api/reports/{report_id}")
def get_report(report_id: str):
    report = get_report_by_id(report_id)
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    subcategory = get_subcategory_by_id(report["subcategory_id"])
    criterion = get_criterion_by_id(subcategory["criterion_id"]) if subcategory else None
    return {"report": report, "subcategory": subcategory, "criterion": criterion}

@app.get("/api/full-structure")
def get_full_structure(role: Optional[str] = None):
    if role:
        criteria = get_criteria_by_role(role)
        subcategories = get_subcategories_by_role(role)
        reports = get_reports_by_role(role)
    else:
        criteria = ALL_CRITERIA
        subcategories = ALL_SUBCATEGORIES
        reports = ALL_REPORTS
    result = []
    for criterion in criteria:
        criterion_data = criterion.copy()
        criterion_subs = [s for s in subcategories if s["criterion_id"] == criterion["id"]]
        criterion_data["subcategories"] = []
        for sub in criterion_subs:
            sub_data = sub.copy()
            sub_reports = [r for r in reports if r["subcategory_id"] == sub["id"]]
            sub_data["reports"] = sub_reports
            criterion_data["subcategories"].append(sub_data)
        result.append(criterion_data)
    return {"structure": result, "role": role}

# مسارات البيانات الإضافية
@app.get("/api/education-offices")
def get_education_offices():
    return EDUCATION_OFFICES

@app.get("/api/school-subjects")
def get_school_subjects():
    return SCHOOL_SUBJECTS

@app.get("/api/school-grades")
def get_school_grades():
    return SCHOOL_GRADES

@app.get("/api/target-audiences")
def get_target_audiences():
    return TARGET_AUDIENCES

@app.get("/api/implementation-places")
def get_implementation_places():
    return IMPLEMENTATION_PLACES

@app.get("/api/educational-tools")
def get_educational_tools():
    return EDUCATIONAL_TOOLS

@app.get("/api/search-reports")
def search_reports(q: str = Query(..., min_length=2), role: Optional[str] = None):
    results = []
    q_lower = q.lower()
    reports_to_search = get_reports_by_role(role) if role else ALL_REPORTS
    for report in reports_to_search:
        if q_lower in report["name"].lower():
            subcategory = get_subcategory_by_id(report["subcategory_id"])
            criterion = get_criterion_by_id(subcategory["criterion_id"]) if subcategory else None
            results.append({
                "report": report,
                "subcategory_name": subcategory["name"] if subcategory else None,
                "criterion_name": criterion["name"] if criterion else None,
            })
    return {"results": results[:20]}

# ============================================================================
# المسار الرئيسي لتوليد محتوى التقرير (مع دعم JSON)
# ============================================================================
@app.post("/api/generate-report-content")
def generate_report_content(
    req: GenerateReportRequest,
    code_id: int = Depends(activation_required),
):
    # ---------- الوضع الحر (بدون معايير) ----------
    if not req.criterion_id or not req.subcategory_id or not req.report_id:
        title = req.report_data.get("title", "تقرير مدرسي")
        prompt = build_ai_prompt(
            role=req.role,
            report_name=title,
            subcategory_name="عام",
            criterion_name="عام",
            criterion_percentage="",
            report_data=req.report_data,
        )
        try:
            genai.configure(api_key=get_api_key())
            model = genai.GenerativeModel("models/gemini-2.5-flash-lite")
            response = model.generate_content(
                prompt,
                generation_config={
                    "temperature": 0.3,
                    "max_output_tokens": 3072
                }
            )
            content = response.text
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"فشل توليد المحتوى: {str(e)}")
    else:
        # ---------- الوضع المرتبط بالمعايير ----------
        report = get_report_by_id(req.report_id)
        if not report:
            raise HTTPException(status_code=404, detail="Report not found")
        subcategory = get_subcategory_by_id(req.subcategory_id)
        if not subcategory:
            raise HTTPException(status_code=404, detail="Subcategory not found")
        if report["subcategory_id"] != req.subcategory_id:
            raise HTTPException(status_code=400, detail="Report does not belong to this subcategory")
        criterion = get_criterion_by_id(req.criterion_id)
        if not criterion:
            raise HTTPException(status_code=404, detail="Criterion not found")
        if subcategory["criterion_id"] != req.criterion_id:
            raise HTTPException(status_code=400, detail="Subcategory does not belong to this criterion")
        criterion_percentage = f"{criterion.get('weight', '')}%"
        prompt = build_ai_prompt(
            role=req.role,
            report_name=report["name"],
            subcategory_name=subcategory["name"],
            criterion_name=criterion["name"],
            criterion_percentage=criterion_percentage,
            report_data=req.report_data,
        )
        try:
            genai.configure(api_key=get_api_key())
            model = genai.GenerativeModel("models/gemini-2.5-flash-lite")
            response = model.generate_content(
                prompt,
                generation_config={
                    "temperature": 0.3,
                    "max_output_tokens": 3072
                }
            )
            content = response.text
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"فشل توليد المحتوى: {str(e)}")

    # ---------- معالجة الاستجابة: محاولة تحليل JSON أولاً ----------
    sections = {}
    try:
        # تنظيف النص من علامات markdown إن وجدت
        cleaned = content.strip()
        if cleaned.startswith("```json"):
            cleaned = cleaned[7:]
        if cleaned.endswith("```"):
            cleaned = cleaned[:-3]
        cleaned = cleaned.strip()
        data = json.loads(cleaned)
        # التأكد من وجود جميع الحقول المطلوبة (بالإنجليزية)
        required_keys = ["goals", "procedures", "performance", "strengths", "improvements", "recommendations"]
        if all(key in data for key in required_keys):
            sections = {f"[{key}]": data[key] for key in required_keys}
            # إعادة بناء النص الكامل للعرض (اختياري)
            full_text = "\n\n".join([f"{k}\n{v}" for k, v in sections.items()])
            content = full_text
        else:
            # إذا كان JSON ناقصاً، نستخدم الطريقة القديمة
            raise ValueError("JSON missing required keys")
    except Exception:
        # ---------- الطريقة القديمة: تقسيم النص حسب العناوين ----------
        sections = {}
        current_section = None
        lines = content.splitlines()
        for line in lines:
            clean_line = line.strip()
            if clean_line.startswith("[") and clean_line.endswith("]"):
                current_section = clean_line
                sections[current_section] = ""
            elif current_section:
                sections[current_section] += clean_line + "\n"

    # تنظيف بسيط (إزالة ** و ## مع الإبقاء على الأقواس والشرطات)
    content_clean = (
        content.replace("**", "")
               .replace("*", "")
               .replace("##", "")
               .replace("#", "")
               .replace("`", "")
    )

    # تحديث الاستخدام
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE activation_codes
        SET usage_count = usage_count + 1, last_used_at = ?
        WHERE id = ? AND (usage_limit IS NULL OR usage_count < usage_limit)
        """,
        (datetime.utcnow().isoformat(), code_id),
    )
    if cur.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=403, detail="تم استهلاك جميع الاستخدامات المسموحة")
    conn.commit()
    conn.close()

    return {
        "content": content_clean,
        "sections": sections,
        "report_id": req.report_id,
        "report_name": report["name"] if not req.report_id else title if 'title' in locals() else None,
        "subcategory_name": subcategory["name"] if not req.report_id and 'subcategory' in locals() else None,
        "criterion_name": criterion["name"] if not req.report_id and 'criterion' in locals() else None,
        "generated_at": datetime.utcnow().isoformat(),
    }

# ============================================================================
# مسارات المشرف (Admin)
# ============================================================================
@app.post("/admin/generate", dependencies=[Depends(admin_auth)])
def admin_generate(req: GenerateKeyReq):
    if req.plan not in PLANS:
        raise HTTPException(status_code=400, detail="Invalid plan")
    plan = PLANS[req.plan]
    duration_minutes = plan.get("minutes")
    duration_days = plan.get("days")
    usage_limit = plan["usage"]
    code = create_key(
        duration_minutes=duration_minutes, duration_days=duration_days, usage_limit=usage_limit
    )
    return {
        "code": code,
        "duration_minutes": duration_minutes,
        "duration_days": duration_days,
        "usage_limit": usage_limit,
    }

@app.get("/admin/codes", dependencies=[Depends(admin_auth)])
def admin_codes():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT id, code, is_active, created_at, started_at, expires_at,
               duration_minutes, duration_days, usage_limit, usage_count, last_used_at
        FROM activation_codes ORDER BY id DESC
        """
    )
    rows = cur.fetchall()
    conn.close()
    now = datetime.utcnow()
    result = []
    for r in rows:
        (id, code, is_active, created_at, started_at, expires_at,
         duration_minutes, duration_days, usage_limit, usage_count, last_used_at) = r
        expired = False
        if expires_at and datetime.fromisoformat(expires_at) < now:
            expired = True
        if usage_limit is not None and usage_count >= usage_limit:
            expired = True
        result.append({
            "id": id,
            "code": code,
            "is_active": bool(is_active),
            "created_at": created_at,
            "started_at": started_at,
            "expires_at": expires_at,
            "duration_minutes": duration_minutes,
            "duration_days": duration_days,
            "usage_limit": usage_limit,
            "usage_count": usage_count,
            "last_used_at": last_used_at,
            "expired": expired,
        })
    return result

@app.put("/admin/code/{code_id}/toggle", dependencies=[Depends(admin_auth)])
def admin_toggle(code_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE activation_codes SET is_active = CASE WHEN is_active=1 THEN 0 ELSE 1 END WHERE id = ?",
        (code_id,),
    )
    conn.commit()
    conn.close()
    return {"status": "ok"}

@app.delete("/admin/code/{code_id}", dependencies=[Depends(admin_auth)])
def admin_delete(code_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM activation_codes WHERE id=?", (code_id,))
    conn.commit()
    conn.close()
    return {"status": "deleted"}

@app.get("/admin/panel", response_class=HTMLResponse)
def admin_panel():
    return Path("admin.html").read_text(encoding="utf-8")