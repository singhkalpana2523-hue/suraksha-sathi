from pydantic import BaseModel
from typing import List


class URLRequest(BaseModel):
    url: str


class URLAnalysisResponse(BaseModel):

    url: str

    risk_score: int

    risk_level: str

    is_suspicious: bool

    reasons: List[str]

    detected_features: List[str]