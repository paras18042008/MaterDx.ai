from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router
from app.api.classify import router as classify_router

app = FastAPI(title="MaterDx.ai API")


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