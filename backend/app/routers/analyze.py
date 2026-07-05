from fastapi import APIRouter

from app.models.request import AnalysisRequest
from app.services.ai_manager import AIManager

router = APIRouter(tags=["AI"])

manager = AIManager()


@router.post("/analyze")
def analyze(req: AnalysisRequest):

    return manager.analyze(req.text)