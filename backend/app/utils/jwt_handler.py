from __future__ import annotations

import os
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional

from jose import JWTError, jwt


JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "1440"))


def create_access_token(subject: str) -> str:
    if not JWT_SECRET_KEY:
        raise RuntimeError("JWT_SECRET_KEY is not set in environment")

    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode: Dict[str, Any] = {
        "sub": subject,
        "exp": expire,
    }
    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)


def decode_access_token(token: str) -> Optional[Dict[str, Any]]:
    if not JWT_SECRET_KEY:
        raise RuntimeError("JWT_SECRET_KEY is not set in environment")

    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload
    except JWTError:
        return None

