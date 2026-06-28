from fastapi import APIRouter
from app.ai.engine import analyze_patient

router = APIRouter()

@router.post("/intake")
def intake(data: dict):
    return analyze_patient(data)