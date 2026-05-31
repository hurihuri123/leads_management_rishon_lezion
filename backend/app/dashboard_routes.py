from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db, get_current_user
from app.models import Lead

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/")
def dashboard(user=Depends(get_current_user), db: Session = Depends(get_db)):

    query = db.query(Lead)

    if user["role"] != "admin":
        query = query.filter(Lead.assigned_to == user["id"])

    total = query.count()
    new = query.filter(Lead.status == "new").count()
    in_progress = query.filter(Lead.status == "in_progress").count()
    closed = query.filter(Lead.status == "closed").count()

    return {
        "total_leads": total,
        "new": new,
        "in_progress": in_progress,
        "closed": closed,
        "conversion_rate": round((closed / total) * 100, 2) if total > 0 else 0
    }