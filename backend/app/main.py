from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.api.routes import router
from app.api.classify import router as classify_router

from app.reasoning.reasoning_context import ReasoningContext
from app.reasoning.reasoning_pipeline import ReasoningPipeline

from app.reasoning.conversation_interpreter import ConversationInterpreter

# Request Model

class ChatRequest(BaseModel):
    session_id: str
    message: str


# FastAPI

app = FastAPI(title="MaterDx.ai API")

session_store = {}

pipeline = ReasoningPipeline()

interpreter = ConversationInterpreter()


# CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Chat Endpoint

@app.post("/chat")
async def chat(data: ChatRequest):

    print("RECEIVED:", data)

    session_id = data.session_id
    message = data.message

    if session_id not in session_store:
        session_store[session_id] = ReasoningContext()

    context = session_store[session_id]

    context.current_message = message

    context.conversation_history.append(
        {
            "role": "user",
            "content": message
        }
    )


    context.interpreted_reply = interpreter.interpret(context)
    print(context.interpreted_reply)

    context = pipeline.process(context)

    session_store[session_id] = context

    return {
        "risk": context.clinical_state.risk,
        "evidence": [
            {
                "type": e.type,
                "name": e.name,
                "status": e.status,
                "value": e.value,
            }
            for e in context.evidence
        ],
        "hypotheses": [
            {
                "name": h.name,
                "confidence": h.confidence,
            }
            for h in context.diagnostic.hypotheses
        ],
        "next_question": context.diagnostic.next_question,
        "ready_for_report": context.diagnostic.ready_for_report,
    }


# Routes

app.include_router(router)
app.include_router(classify_router)


# Root

@app.get("/")
def root():
    return {
        "message": "Welcome to MaterDx.ai"
    }


# Health

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "MaterDx.ai Backend"
    }