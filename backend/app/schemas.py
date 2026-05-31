from pydantic import BaseModel
from typing import Optional


# LEAD SCHEMAS
class LeadCreate(BaseModel):
    full_name: str
    phone: str
    email: Optional[str] = None
    city: Optional[str] = None
    source: Optional[str] = None


class LeadUpdate(BaseModel):
    full_name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    city: Optional[str] = None
    source: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None


class LeadOut(BaseModel):
    id: int
    full_name: str
    phone: str
    email: Optional[str]
    city: Optional[str]
    source: Optional[str]
    status: str
    notes: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]
    assigned_to: Optional[int]

    class Config:
        from_attributes = True


# USER SCHEMAS
class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    role: str

    class Config:
        from_attributes = True