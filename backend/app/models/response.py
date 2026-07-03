from typing import List, Literal
from pydantic import BaseModel, Field


class AnalysisResponse(BaseModel):
    provider: str

    classification: Literal[
        "SCAM",
        "SAFE",
        "SUSPICIOUS"
    ]

    confidence: int = Field(ge=0, le=100)

    scam_type: str

    summary: str

    red_flags: List[str]

    action_steps: List[str]