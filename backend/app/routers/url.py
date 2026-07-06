from fastapi import APIRouter

from app.models.url_models import URLRequest
from app.services.url_service import URLService
from app.services.ai_manager import AIManager

router = APIRouter(
    prefix="/analyze",
    tags=["URL Analysis"]
)

url_service = URLService()
ai_manager = AIManager()


@router.post("/url")
async def analyze_url(request: URLRequest):

    # Rule-Based Analysis
    url_result = url_service.analyze(request.url)

    # AI Explanation
    ai_result = ai_manager.analyze(
        f"""
Analyze the following URL for phishing or scam.

URL:
{request.url}

Rule Based Analysis:
Risk Score: {url_result.risk_score}
Risk Level: {url_result.risk_level}

Reasons:
{", ".join(url_result.reasons)}

Explain to the user in simple language:
1. Whether the URL is safe.
2. Why it is suspicious (if applicable).
3. What precautions they should take.
"""
    )

    return {
        "url_analysis": url_result.model_dump(),
        "ai_analysis": ai_result
    }