from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class CreateHistoryRequest(BaseModel):
    title: str = Field(..., min_length=1)
    question: str = Field(..., min_length=1)
    answer: str = Field(..., min_length=1)
    category: Optional[str] = None


class HistoryResponse(BaseModel):
    id: str
    title: str
    question: str
    answer: str
    category: Optional[str] = None
    created_at: datetime

    model_config = {"from_attributes": True}


class HistoryListResponse(BaseModel):
    page: int
    limit: int
    total: int
    data: list[HistoryResponse]

