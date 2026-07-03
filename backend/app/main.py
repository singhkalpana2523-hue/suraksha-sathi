from fastapi import FastAPI
from app.routers.health import router as health_router

app = FastAPI(
    title="SurakshaSathi AI API",
    description="AI Financial Scam Detection Backend",
    version="1.0.0"
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to SurakshaSathi AI Backend 🚀"
    }