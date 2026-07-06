from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.health import router as health_router
from app.routes.dataset import router as dataset_router

from app.routers.analyze import router as analyze_router
from app.routers.image import router as image_router
from app.routers.voice import router as voice_router
from app.routers.qr import router as qr_router
from app.routers.url import router as url_router

app = FastAPI(

    title="SurakshaSathi AI API",
    description="AI Financial Scam Detection Backend",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to SurakshaSathi AI Backend 🚀"
    }
app.include_router(dataset_router)
app.include_router(analyze_router)
app.include_router(image_router)
app.include_router(voice_router)
app.include_router(qr_router)
app.include_router(url_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to SurakshaSathi AI Backend 🚀"
    }
