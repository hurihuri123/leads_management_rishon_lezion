from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
import os

from app.models import User

SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret_change_me")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# PASSWORD
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# TOKEN
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# REGISTER
def register_user(db: Session, first_name: str, last_name: str, email: str, password: str, birth_date=None):

    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise Exception("Email already exists")

    new_user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        birth_date=birth_date,
        password_hash=hash_password(password),
        role="agent"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# LOGIN
def authenticate_user(db: Session, email: str, password: str):

    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise Exception("Invalid credentials")

    if not verify_password(password, user.password_hash):
        raise Exception("Invalid credentials")

    token = create_access_token({
        "sub": user.email,
        "role": user.role,
        "user_id": user.id
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "email": user.email,
            "role": user.role
        }
    }