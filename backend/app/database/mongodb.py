from __future__ import annotations

import os
from typing import Any

from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()


def _get_mongo_client() -> MongoClient:
    mongodb_uri = os.getenv("MONGODB_URI")
    if not mongodb_uri:
        raise RuntimeError("MONGODB_URI is not set. Check backend/.env")
    return MongoClient(mongodb_uri)


def get_users_collection() -> Any:
    """Return the MongoDB `users` collection."""
    client = _get_mongo_client()
    db_name = os.getenv("MONGODB_DB", "suraksha_sathi")
    collection_name = os.getenv("MONGODB_USERS_COLLECTION", "users")
    return client[db_name][collection_name]


def get_history_collection() -> Any:
    """Return the MongoDB `history` collection."""
    client = _get_mongo_client()
    db_name = os.getenv("MONGODB_DB", "suraksha_sathi")
    collection_name = os.getenv("MONGODB_HISTORY_COLLECTION", "history")
    return client[db_name][collection_name]


