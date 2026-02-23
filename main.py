# -*- coding: utf-8 -*-
from fastapi import FastAPI, HTTPException, Depends, Header, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
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

# ---------- Init DB ----------
init_db()

# ---------- App ----------
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# خدمة الملفات الثابتة (للـ templates)
app.mount("/templates", StaticFiles(directory="templates"), name="templates")

# ---------- Admin Auth ----------
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN", "")

def admin_auth(x_admin_token: str = Header(...)):
    if x_admin_token != ADMIN_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")

# ---------- Models ----------
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

# ---------- Plans ----------
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

# ---------- Gemini Keys ----------
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

# إدارات التعليم
EDUCATION_OFFICES = [...]  # نفس القائمة الموجودة (اختصاراً للطول)

# المواد الدراسية
SCHOOL_SUBJECTS = [...]    # نفس القائمة

# الصفوف الدراسية
SCHOOL_GRADES = [...]      # نفس القائمة

# المستهدفون
TARGET_AUDIENCES = [...]   # نفس القائمة

# أماكن التنفيذ
IMPLEMENTATION_PLACES = [...] # نفس القائمة

# الأدوات والوسائل التعليمية
EDUCATIONAL_TOOLS = [...]  # نفس القائمة

# ============================================================================
# برومبتات الذكاء الاصطناعي (نسخة JSON منظمة)
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

    subject_line = f"المادة: {report_data.get('subject', '')}"
    lesson_line = f"الدرس: {report_data.get('lesson', '')}"
    grade_line = f"الصف: {report_data.get('grade', '')}"
    target_line = f"المستهدفون: {report_data.get('target', '')}"
    place_line = f"مكان التنفيذ: {report_data.get('place', '')}"
    count_line = f"عدد الحضور: {report_data.get('count', '')}"

    json_structure = ""

    if "أداء الواجبات" in report_name:
        json_structure = """
أعد النتيجة بصيغة JSON فقط:

{
  "goal": "",
  "procedures": "",
  "application_level": "",
  "impact": "",
  "obstacles": "",
  "development_actions": "",
  "follow_up": ""
}
"""

    elif "المجتمع المهني" in report_name:
        json_structure = """
أعد النتيجة بصيغة JSON فقط:

{
  "partnership": "",
  "participation": "",
  "experience_exchange": "",
  "initiatives": "",
  "peer_support": "",
  "impact": "",
  "improvement_opportunities": ""
}
"""

    elif "أولياء الأمور" in report_name:
        json_structure = """
أعد النتيجة بصيغة JSON فقط:

{
  "goals": "",
  "communication_methods": "",
  "participation_level": "",
  "family_partnerships": "",
  "impact": "",
  "challenges": "",
  "improvement_opportunities": ""
}
"""

    final_prompt = f"""
التقرير المطلوب: {report_name}
يندرج تحت: {subcategory_name}
ضمن الجدارة: {criterion_name}

{subject_line}
{lesson_line}
{grade_line}
{target_line}
{place_line}
{count_line}

⚠️ أعد JSON فقط بدون شرح أو تنسيق.

{json_structure}
"""

    return final_prompt

# دوال مساعدة للبحث (get_criterion_by_id, etc) كما هي

# ============================================================================
# المسارات
# ============================================================================

@app.get("/")
def root():
    return {"status": "running", "message": "Teacher Reports API"}

@app.get("/health")
def health(_: int = Depends(activation_required)):
    return {"status": "ok"}

# ... باقي المسارات (subscription/status, ask, api/roles, api/criteria, ...) تبقى كما هي ...

# ============================================================================
# مسار توليد محتوى التقرير (المعدل)
# ============================================================================

@app.post("/api/generate-report-content")
def generate_report_content(
    req: GenerateReportRequest,
    code_id: int = Depends(activation_required),
):

    # ===== الوضع الحر بجودة احترافية =====
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
            response = model.generate_content(prompt)
            content = response.text
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"فشل توليد المحتوى: {str(e)}")

        # محاولة تحليل JSON
        try:
            structured_content = json.loads(content)
        except Exception:
            structured_content = {
                "error": "فشل تحليل JSON",
                "raw": content
            }

        if not isinstance(structured_content, dict):
            structured_content = {"error": "تنسيق غير صحيح من الذكاء الاصطناعي"}

        template_name = "duty-report" if "أداء الواجبات" in title else \
                        "professional-community-report" if "المجتمع المهني" in title else \
                        "parents-interaction-report" if "أولياء الأمور" in title else \
                        "default-report"

        return {
            "data": structured_content,
            "template": template_name,
            "report_name": title,
            "generated_at": datetime.utcnow().isoformat(),
        }

    # ===== الوضع المرتبط بالمعايير =====
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

    criterion_percentage = criterion.get("percentage", "")

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
        response = model.generate_content(prompt)
        content = response.text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"فشل توليد المحتوى: {str(e)}")

    try:
        structured_content = json.loads(content)
    except Exception:
        structured_content = {
            "error": "فشل تحليل JSON",
            "raw": content
        }

    if not isinstance(structured_content, dict):
        structured_content = {"error": "تنسيق غير صحيح من الذكاء الاصطناعي"}

    # تحديد القالب
    template_name = "duty-report" if "أداء الواجبات" in report["name"] else \
                    "professional-community-report" if "المجتمع المهني" in report["name"] else \
                    "parents-interaction-report" if "أولياء الأمور" in report["name"] else \
                    "default-report"

    return {
        "data": structured_content,
        "template": template_name,
        "report_name": report["name"],
        "generated_at": datetime.utcnow().isoformat(),
    }

# باقي المسارات الإدارية (admin/generate, admin/codes, ...) تبقى كما هي