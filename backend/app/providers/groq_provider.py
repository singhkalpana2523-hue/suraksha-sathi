import json

from groq import Groq

from app.config import GROQ_API_KEY
from app.models.response import AnalysisResponse
from app.providers.base_provider import BaseProvider


class GroqProvider(BaseProvider):

    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def analyze(self, prompt: str) -> AnalysisResponse:

        completion = self.client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.2,

            response_format={
                "type": "json_object"
            }

        )

        result = json.loads(
            completion.choices[0].message.content
        )

        required = [
            "classification",
            "confidence",
            "scam_type",
            "summary",
            "red_flags",
            "action_steps"
        ]

        missing = [
            field
            for field in required
            if field not in result
        ]

        if missing:
            raise ValueError(
                f"Groq returned invalid JSON.\n"
                f"Missing fields: {missing}\n"
                f"Response: {result}"
            )

        result["provider"] = "groq"

        return AnalysisResponse(**result)