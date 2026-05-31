from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from sqlalchemy.orm import Session
import os

from app.database import SessionLocal
from app.models import User

# CONFIG
SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret_change_me")
ALGORITHM = "HS256"

# 🔥 Swagger will show ONE field (Bearer token)
security = HTTPBearer()


# DB SESSION
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# GET CURRENT USER FROM TOKEN
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials  # <-- this is the raw JWT

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        user_id = payload.get("user_id")
        if user_id is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise credentials_exception

    return {
    "id": user.id,
    "first_name": user.first_name,
    "last_name": user.last_name,
    "email": user.email,
    "role": user.role,
    "birth_date": user.birth_date
}


# ADMIN ONLY DEPENDENCY
def get_current_admin(user=Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin only"
        )
    return user