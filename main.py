from fastapi import FastAPI, HTTPException, Depends, Header, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime, timedelta
import os
import itertools
import google.generativeai as genai
from database import init_db, get_connection
from create_key import create_key
from security import activation_required
import time

ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database
init_db()

# Request models
class Req(BaseModel):
    prompt: str

class GenerateKeyReq(BaseModel):
    expires_at: str | None = None
    usage_limit: int | None = None

class ActivationCheckReq(BaseModel):
    code: str

# Security tracking
activation_attempts = {}
MAX_ATTEMPTS = 5
LOCKOUT_MINUTES = 15

# API keys for Gemini
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

if not api_keys:
    raise RuntimeError("No GEMINI API KEYS found")

key_cycle = itertools.cycle(api_keys)

def get_api_key():
    return next(key_cycle)

def admin_auth(x_admin_token: str = Header(...)):
    if x_admin_token != ADMIN_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")

def check_activation_attempts(ip_address: str):
    """Check if IP is locked due to too many failed attempts"""
    if ip_address in activation_attempts:
        attempts_data = activation_attempts[ip_address]
        
        if attempts_data["locked_until"]:
            if time.time() < attempts_data["locked_until"]:
                remaining = int((attempts_data["locked_until"] - time.time()) / 60)
                raise HTTPException(
                    status_code=429,
                    detail=f"Too many attempts. Try again in {remaining} minutes"
                )
            else:
                # Reset lock if time has passed
                attempts_data["locked_until"] = None
        
        if attempts_data["count"] >= MAX_ATTEMPTS:
            # Lock for 15 minutes
            attempts_data["locked_until"] = time.time() + (LOCKOUT_MINUTES * 60)
            raise HTTPException(
                status_code=429,
                detail=f"Too many attempts. Locked for {LOCKOUT_MINUTES} minutes"
            )
    
    return True

def record_failed_attempt(ip_address: str):
    """Record a failed activation attempt"""
    if ip_address not in activation_attempts:
        activation_attempts[ip_address] = {
            "count": 0,
            "locked_until": None,
            "first_attempt": time.time()
        }
    
    attempts_data = activation_attempts[ip_address]
    attempts_data["count"] += 1
    attempts_data["last_attempt"] = time.time()
    
    # Reset attempts after 1 hour
    if time.time() - attempts_data["first_attempt"] > 3600:
        activation_attempts[ip_address] = {
            "count": 1,
            "locked_until": None,
            "first_attempt": time.time(),
            "last_attempt": time.time()
        }

@app.get("/health")
def health():
    return {"status": "ok", "server_time": datetime.now().isoformat()}

@app.post("/verify")
async def verify_code(req: ActivationCheckReq, request: Request):
    """Verify activation code with security checks"""
    ip_address = request.client.host
    
    # Check if IP is locked
    try:
        check_activation_attempts(ip_address)
    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={"valid": False, "message": e.detail}
        )
    
    # Code validation
    code = req.code.strip().upper()
    
    # Basic validation
    if len(code) != 20:
        record_failed_attempt(ip_address)
        return JSONResponse(
            status_code=400,
            content={"valid": False, "message": "Invalid code length"}
        )
    
    # Check code pattern
    import re
    if not re.match(r'^[A-Z0-9]{20}$', code):
        record_failed_attempt(ip_address)
        return JSONResponse(
            status_code=400,
            content={"valid": False, "message": "Invalid code format"}
        )
    
    # Check in database
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT id, is_active, usage_count, expires_at FROM activation_codes WHERE code = ?",
            (code,)
        )
        row = cur.fetchone()
        
        if not row:
            record_failed_attempt(ip_address)
            return JSONResponse(
                status_code=404,
                content={"valid": False, "message": "Code not found"}
            )
        
        code_id, is_active, usage_count, expires_at = row
        
        # Check if active
        if not is_active:
            record_failed_attempt(ip_address)
            return JSONResponse(
                status_code=403,
                content={"valid": False, "message": "Code is inactive"}
            )
        
        # Check expiration
        if expires_at:
            expires_date = datetime.strptime(expires_at, "%Y-%m-%d")
            if datetime.now() > expires_date:
                record_failed_attempt(ip_address)
                return JSONResponse(
                    status_code=403,
                    content={"valid": False, "message": "Code has expired"}
                )
        
        # Increment usage count
        cur.execute(
            "UPDATE activation_codes SET usage_count = usage_count + 1 WHERE id = ?",
            (code_id,)
        )
        conn.commit()
        
        # Reset attempts for this IP on successful verification
        if ip_address in activation_attempts:
            activation_attempts.pop(ip_address, None)
        
        return JSONResponse({
            "valid": True,
            "message": "Code verified successfully",
            "usage_count": usage_count + 1,
            "expires_at": expires_at
        })
        
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"valid": False, "message": f"Server error: {str(e)}"}
        )
    finally:
        conn.close()

@app.post("/ask")
async def ask(req: Req, _: None = Depends(activation_required), request: Request):
    """AI问答端点"""
    try:
        # 安全检查：验证请求频率
        ip_address = request.client.host
        if ip_address not in request.app.state.rate_limits:
            request.app.state.rate_limits[ip_address] = []
        
        # 清理旧的请求记录
        current_time = time.time()
        request.app.state.rate_limits[ip_address] = [
            t for t in request.app.state.rate_limits[ip_address]
            if current_time - t < 60  # 保留过去60秒的记录
        ]
        
        # 检查请求频率（每分钟最多10个请求）
        if len(request.app.state.rate_limits[ip_address]) >= 10:
            raise HTTPException(
                status_code=429,
                detail="Too many requests. Please wait 1 minute."
            )
        
        # 记录当前请求
        request.app.state.rate_limits[ip_address].append(current_time)
        
        # AI处理
        genai.configure(api_key=get_api_key())
        model = genai.GenerativeModel("models/gemini-2.5-flash-lite")
        response = model.generate_content(req.prompt)
        
        return {"answer": response.text}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/admin/generate", dependencies=[Depends(admin_auth)])
def admin_generate(req: GenerateKeyReq):
    """生成激活码"""
    return {"code": create_key(req.expires_at, req.usage_limit)}

@app.get("/admin/codes", dependencies=[Depends(admin_auth)])
def admin_codes():
    """获取所有激活码"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, code, is_active, usage_count, expires_at, created_at FROM activation_codes ORDER BY created_at DESC")
    rows = cur.fetchall()
    conn.close()
    return [
        {
            "id": r[0],
            "code": r[1],
            "active": bool(r[2]),
            "usage": r[3],
            "expires_at": r[4],
            "created_at": r[5]
        }
        for r in rows
    ]

@app.put("/admin/code/{code_id}/toggle", dependencies=[Depends(admin_auth)])
def admin_toggle(code_id: int):
    """切换激活码状态"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE activation_codes SET is_active = CASE WHEN is_active=1 THEN 0 ELSE 1 END WHERE id=?",
        (code_id,)
    )
    conn.commit()
    conn.close()
    return {"status": "ok"}

@app.delete("/admin/code/{code_id}", dependencies=[Depends(admin_auth)])
def admin_delete(code_id: int):
    """删除激活码"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM activation_codes WHERE id=?", (code_id,))
    conn.commit()
    conn.close()
    return {"status": "deleted"}

# 初始化速率限制
@app.on_event("startup")
async def startup_event():
    app.state.rate_limits = {}