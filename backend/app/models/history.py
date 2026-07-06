from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional


@dataclass
class History:
    user_id: str
    title: str
    question: str
    answer: str
    category: Optional[str]
    created_at: datetime
    updated_at: datetime

    def to_mongo_document(self) -> dict[str, Any]:
        doc: dict[str, Any] = {
            "user_id": self.user_id,
            "title": self.title,
            "question": self.question,
            "answer": self.answer,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
        if self.category is not None:
            doc["category"] = self.category
        return doc

