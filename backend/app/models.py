from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Text
from app.database import Base
from datetime import datetime

# USERS TABLE
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    birth_date = Column(Date, nullable=True)

    email = Column(String, unique=True, nullable=False)

    password_hash = Column(String, nullable=False)

    role = Column(String, default="agent")


# LEADS TABLE
class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    email = Column(String)
    city = Column(String)
    source = Column(String)

    status = Column(String, default="new")
    notes = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    closed_at = Column(DateTime, nullable=True)

    assigned_to = Column(Integer, ForeignKey("users.id"))