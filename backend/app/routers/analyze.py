from fastapi import APIRouter
import re

from app.models.request import AnalysisRequest
from app.services.ai_manager import AIManager
from app.services.response_builder import ResponseBuilder
from app.services.url_service import URLService

router = APIRouter(tags=["AI"])

manager = AIManager()
url_service = URLService()

URL_REGEX = re.compile(
    r'((?:https?://)?(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?)',
    re.IGNORECASE
)


@router.post("/analyze")
def analyze(req: AnalysisRequest):

    # -----------------------------
    # URL Detection
    # -----------------------------
    url_matches = URL_REGEX.findall(req.text)

    url_context = ""

    if url_matches:

        url_context += "Detected URL Analysis\n\n"

        for url in url_matches:

            if not url.startswith(("http://", "https://")):
                url = "https://" + url

            try:

                result = url_service.analyze(url)

                url_context += f"""
URL: {url}

Risk Score: {result.risk_score}

Risk Level: {result.risk_level}

Reasons:
{chr(10).join(result.reasons)}

---------------------------------------
"""

            except Exception:

                url_context += f"""
URL: {url}

Could not analyze this URL.

---------------------------------------
"""

    # -----------------------------
    # AI Analysis
    # -----------------------------
    analysis = manager.analyze(
        text=req.text,
        url_context=url_context
    )

    metadata = {
        "input_type": "text",
        "original_text": req.text
    }

    return ResponseBuilder.build(
        analysis,
        metadata
    )