from typing import List

from pydantic import BaseModel


class DatasetRecord(BaseModel):
    id: int
    title: str
    category: str
    subcategory: str
    severity: str
    language: str
    text: str
    summary: str
    red_flags: List[str]
    recommended_actions: List[str]
    keywords: List[str]
    source: str

