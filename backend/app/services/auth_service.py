from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, Optional

from app.database.mongodb import get_users_collection
from app.models.user import User
from app.schemas.auth_schema import LoginRequest, SignupRequest
from app.utils.jwt_handler import create_access_token
from app.utils.password import hash_password, verify_password


class AuthService:
    def __init__(self) -> None:
        self._users = get_users_collection()

    def signup(self, req: SignupRequest) -> Dict[str, Any]:
        existing = self._users.find_one({"phone": req.phone})
        if existing is not None:
            raise ValueError("Phone number already registered")

        hashed_pw = hash_password(req.password)
        user = User(
            name=req.name,
            phone=req.phone,
            password=hashed_pw,
            created_at=datetime.now(timezone.utc),
        )
        self._users.insert_one(user.to_mongo_document())
        return {"status": "success"}

    def login(self, req: LoginRequest) -> Dict[str, Any]:
        existing = self._users.find_one({"phone": req.phone})
        if existing is None:
            raise ValueError("Invalid credentials")

        hashed_pw = existing.get("password")
        if not hashed_pw or not verify_password(req.password, hashed_pw):
            raise ValueError("Invalid credentials")

        token = create_access_token(subject=req.phone)
        return {"access_token": token, "token_type": "bearer"}

    def get_user_by_phone(self, phone: str) -> Optional[Dict[str, Any]]:
        return self._users.find_one({"phone": phone})

