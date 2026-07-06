from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, Optional

from bson import ObjectId

from app.database.mongodb import get_history_collection
from app.models.history import History
from app.schemas.history_schema import CreateHistoryRequest


class HistoryService:
    def __init__(self) -> None:
        self._history = get_history_collection()

    def create_history(self, user_id: str, req: CreateHistoryRequest) -> Dict[str, Any]:
        now = datetime.now(timezone.utc)
        history = History(
            user_id=user_id,
            title=req.title,
            question=req.question,
            answer=req.answer,
            category=req.category,
            created_at=now,
            updated_at=now,
        )
        res = self._history.insert_one(history.to_mongo_document())
        return {"id": str(res.inserted_id), "status": "success"}

    def list_histories(
        self,
        user_id: str,
        *,
        page: int,
        limit: int,
        sort: str = "desc",
    ) -> dict[str, Any]:
        page = max(page, 1)
        limit = max(min(limit, 100), 1)
        skip = (page - 1) * limit

        sort_order = -1 if sort == "asc" and False else -1  # default desc
        if sort == "asc":
            sort_order = 1

        query = {"user_id": user_id}
        total = self._history.count_documents(query)
        cursor = (
            self._history.find(query)
            .sort("created_at", sort_order)
            .skip(skip)
            .limit(limit)
        )
        data = [self._serialize_history(doc) for doc in cursor]
        return {"page": page, "limit": limit, "total": total, "data": data}

    def get_history(self, user_id: str, history_id: str) -> Optional[dict[str, Any]]:
        try:
            oid = ObjectId(history_id)
        except Exception:
            return None

        doc = self._history.find_one({"_id": oid, "user_id": user_id})
        if not doc:
            return None
        return self._serialize_history(doc)

    def delete_history(self, user_id: str, history_id: str) -> bool:
        try:
            oid = ObjectId(history_id)
        except Exception:
            return False

        res = self._history.delete_one({"_id": oid, "user_id": user_id})
        return res.deleted_count == 1

    def delete_all_histories(self, user_id: str) -> int:
        res = self._history.delete_many({"user_id": user_id})
        return int(res.deleted_count)

    def search_histories(
        self,
        user_id: str,
        query: str,
        *,
        page: int,
        limit: int,
        sort: str = "desc",
    ) -> dict[str, Any]:
        page = max(page, 1)
        limit = max(min(limit, 100), 1)
        skip = (page - 1) * limit

        sort_order = -1
        if sort == "asc":
            sort_order = 1

        regex = {"$regex": query, "$options": "i"}
        mongo_query = {
            "user_id": user_id,
            "$or": [
                {"title": regex},
                {"question": regex},
                {"answer": regex},
            ],
        }
        total = self._history.count_documents(mongo_query)
        cursor = (
            self._history.find(mongo_query)
            .sort("created_at", sort_order)
            .skip(skip)
            .limit(limit)
        )
        data = [self._serialize_history(doc) for doc in cursor]
        return {"page": page, "limit": limit, "total": total, "data": data}

    def _serialize_history(self, doc: Dict[str, Any]) -> dict[str, Any]:
        return {
            "id": str(doc.get("_id")),
            "title": doc.get("title"),
            "question": doc.get("question"),
            "answer": doc.get("answer"),
            "category": doc.get("category"),
            "created_at": doc.get("created_at"),
        }

