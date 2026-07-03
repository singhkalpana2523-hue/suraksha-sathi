from google import genai
from google.genai import types

from app.config import GEMINI_API_KEY
from app.prompts.prompt_service import SYSTEM_PROMPT
from app.models.response import AnalysisResponse

client = genai.Client(api_key=GEMINI_API_KEY)


def analyze_text(text: str) -> AnalysisResponse:

    response = client.models.generate_content(
        model="gemini-2.5-flash",

        contents=f"""
{SYSTEM_PROMPT}

User Message:
{text}
""",

        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=AnalysisResponse,
            temperature=0.2,
        ),
    )

    data = response.parsed

    data.provider = "gemini"

    return data