from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class User:
    name: str
    phone: str
    password: str  # stored hashed by Person 2
    created_at: datetime

    def to_mongo_document(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "phone": self.phone,
            "password": self.password,
            "created_at": self.created_at,
        }

