from fastapi import APIRouter

from app.models.request import AnalysisRequest
from app.services.ai_manager import AIManager
from app.services.response_builder import ResponseBuilder

router = APIRouter(tags=["AI"])

manager = AIManager()


@router.post("/analyze")
def analyze(req: AnalysisRequest):

    analysis = manager.analyze(req.text)

    metadata = {
        "input_type": "text",
        "original_text": req.text
    }

    return ResponseBuilder.build(
        analysis,
        metadata
    )