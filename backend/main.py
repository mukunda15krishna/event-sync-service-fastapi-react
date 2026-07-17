from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.loader import load_crm, load_calendar
from services.reconciler import reconcile

app = FastAPI(
    title="Event Sync Service",
    version="1.0.0",
    description="Reconciles CRM and Calendar meetings."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "application": "Event Sync Service",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }


@app.get("/meetings")
def meetings():
    crm = load_crm()
    calendar = load_calendar()
    return reconcile(crm, calendar)