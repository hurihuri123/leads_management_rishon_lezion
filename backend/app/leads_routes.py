from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.dependencies import get_db, get_current_user, get_current_admin
from app.models import Lead
from app.schemas import LeadCreate, LeadUpdate

router = APIRouter(prefix="/leads", tags=["leads"])


# =========================
# CREATE LEAD
# =========================
@router.post("/")
def create_lead(
    data: LeadCreate,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    new_lead = Lead(
        full_name=data.full_name,
        phone=data.phone,
        email=data.email,
        city=data.city,
        source=data.source,
        assigned_to=user["id"]
    )

    db.add(new_lead)
    db.commit()
    db.refresh(new_lead)

    return new_lead


# =========================
# GET ALL LEADS (שיפור תגובה)
# =========================
@router.get("/")
def get_leads(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    query = db.query(Lead)

    if user["role"] != "admin":
        query = query.filter(Lead.assigned_to == user["id"])

    leads = query.all()

    return {
        "count": len(leads),
        "results": leads
    }

# GET LEAD BY ID
@router.get("/{lead_id}")
def get_lead(
    lead_id: int,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    lead = db.query(Lead).filter(Lead.id == lead_id).first()

    if not lead:
        return {"error": "Lead not found"}

    if user["role"] != "admin" and lead.assigned_to != user["id"]:
        return {"error": "Not allowed"}

    return lead


# SEARCH + PAGINATION
@router.get("/search/")
def search_leads(
    city: str = None,
    status: str = None,
    page: int = 1,
    limit: int = 10,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    query = db.query(Lead)

    if user["role"] != "admin":
        query = query.filter(Lead.assigned_to == user["id"])

    if city:
        query = query.filter(Lead.city.ilike(f"%{city}%"))

    if status:
        query = query.filter(Lead.status == status)

    total = query.count()

    leads = query.offset((page - 1) * limit).limit(limit).all()

    return {
        "total": total,
        "page": page,
        "limit": limit,
        "results": leads
    }


# UPDATE LEAD
@router.put("/{lead_id}")
def update_lead(
    lead_id: int,
    data: LeadUpdate,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    lead = db.query(Lead).filter(Lead.id == lead_id).first()

    if not lead:
        return {"error": "Lead not found"}

    if user["role"] != "admin" and lead.assigned_to != user["id"]:
        return {"error": "Not allowed"}

    allowed_status = ["new", "in_progress", "closed"]

    if data.status and data.status not in allowed_status:
        return {"error": "Invalid status"}

    for field, value in data.dict(exclude_unset=True).items():
        setattr(lead, field, value)

    lead.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(lead)

    return lead

# DELETE LEAD (ADMIN ONLY)
@router.delete("/{lead_id}")
def delete_lead(
    lead_id: int,
    admin=Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    lead = db.query(Lead).filter(Lead.id == lead_id).first()

    if not lead:
        return {"error": "Lead not found"}

    db.delete(lead)
    db.commit()

    return {"message": "Lead deleted successfully"}