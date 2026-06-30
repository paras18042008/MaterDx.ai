from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router
from app.api.classify import router as classify_router
from fastapi import Request
from app.reasoning.feature_extractor import extract_features
from app.reasoning.clinical_state import ClinicalState
from app.reasoning.clinical_updater import update_state
from app.reasoning.question_planner import get_next_question
from pydantic import BaseModel

class ChatRequest(BaseModel):
    session_id: str
    message: str

app = FastAPI(title="MaterDx.ai API")
session_store = {}

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(data: ChatRequest):
    print("RECEIVED:", data)
    session_id = data.session_id
    message = data.message

    if session_id not in session_store:
        session_store[session_id] = ClinicalState()

    state = session_store[session_id]

    extracted = extract_features(message)

    state = update_state(state, extracted)

    next_q = get_next_question(state)

    session_store[session_id] = state

    return {
        "extracted": extracted,
        "risk": state.risk,
        "missing_features": state.missing_features,
        "next_question": next_q
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

app.include_router(classify_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to MaterDx.ai"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "MaterDx.ai Backend"
    }