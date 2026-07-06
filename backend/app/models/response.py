from typing import List
from pydantic import BaseModel


class Translation(BaseModel):
    en: str
    hi: str
    gu: str


class AnalysisResponse(BaseModel):
    provider: str = "gemini"

    classification: str
    confidence: int
    scam_type: str

    summary: Translation

    red_flags: List[Translation]

    action_steps: List[Translation]

    matched_patterns: list = []

    recommended_actions: list = []