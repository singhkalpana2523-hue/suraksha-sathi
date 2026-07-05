from google import genai
from google.genai import types
import json

from app.config import GEMINI_API_KEY
from app.models.response import AnalysisResponse
from app.providers.base_provider import BaseProvider


class GeminiProvider(BaseProvider):

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def analyze(self, prompt: str) -> AnalysisResponse:

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=AnalysisResponse,
                temperature=0.2,
            ),
        )

        result = response.parsed
        result.provider = "gemini"

        return result

    from app.models.dataset import ScamDataset


def generate_dataset(self, category: str, count: int = 5):

    prompt = f"""
You are an expert cybersecurity dataset creator.

Generate exactly {count} UNIQUE scam examples.

Category:
{category}

Generate examples in:
- English
- Hindi
- Gujarati

Mix:
- SMS
- WhatsApp
- Email
- Phone Call

Severity:
Low
Medium
High
Critical

Return ONLY structured data.
"""

    response = self.client.models.generate_content(

        model="gemini-2.5-flash",

        contents=prompt,

        config=types.GenerateContentConfig(

            response_mime_type="application/json",

            response_schema=ScamDataset,

            temperature=0.8

        )
    )

    return response.parsed.records