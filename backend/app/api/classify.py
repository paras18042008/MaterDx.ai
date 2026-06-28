from fastapi import APIRouter
from app.ai.classifier import classify_symptom
from app.core.question_engine import get_next_questions

router = APIRouter()


@router.post("/classify")
def classify(state: dict):
    result = classify_symptom(state)

    category = result.get("category", "general")
    risk = result.get("risk", "LOW")

    next_questions = get_next_questions(category, risk)

    return {
        "classification": result,
        "next_questions": next_questions
    }