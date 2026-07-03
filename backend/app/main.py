from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.api.routes import router
from app.api.classify import router as classify_router

from app.reasoning.patient_context import PatientContext
from app.reasoning.reasoning_pipeline import ReasoningPipeline


class ChatRequest(BaseModel):
    session_id: str
    message: str


app = FastAPI(title="MaterDx.ai API")

session_store = {}

pipeline = ReasoningPipeline()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/chat")
async def chat(data: ChatRequest):

    session_id = data.session_id
    message = data.message

    if session_id not in session_store:

        session_store[session_id] = PatientContext()

    patient_context = session_store[session_id]

    patient_context = pipeline.run(
        patient_context,
        message,
    )

    # ------------------------------------
    # Remember the last question asked by the Judge.
    # This allows the Conversation Interpreter to
    # correctly interpret short replies such as
    # "Yes", "No", "Since yesterday", etc.
    # ------------------------------------
    patient_context.last_question = patient_context.judge_output.get(
        "next_question",
        "",
    )

    session_store[session_id] = patient_context

    print(patient_context)
    print(type(patient_context))

    return patient_context.judge_output


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