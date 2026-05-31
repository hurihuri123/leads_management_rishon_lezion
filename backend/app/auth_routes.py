from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.dependencies import get_current_user

from app.database import SessionLocal
from app.auth import register_user, authenticate_user

router = APIRouter(prefix="/auth", tags=["auth"])

security = HTTPBearer()

# DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# SCHEMAS
class RegisterRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str

# REGISTER
@router.post("/register")
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    try:
        return register_user(
            db,
            data.first_name,
            data.last_name,
            data.email,
            data.password
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# LOGIN
@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    try:
        return authenticate_user(db, data.email, data.password)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

# PROTECTED ROUTE (JWT TEST)
@router.get("/me")
def get_me(user=Depends(get_current_user)):
    return user