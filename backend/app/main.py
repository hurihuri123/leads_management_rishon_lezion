from fastapi import FastAPI

from app.auth_routes import router as auth_router
from app.leads_routes import router as leads_router
from app.dashboard_routes import router as dashboard_router

app = FastAPI(title="Leads Management API")

app.include_router(auth_router)
app.include_router(leads_router)
app.include_router(dashboard_router)