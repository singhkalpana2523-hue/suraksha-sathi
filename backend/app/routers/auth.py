from __future__ import annotations

from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.schemas.auth_schema import LoginRequest, SignupRequest
from app.services.auth_service import AuthService
from app.utils.jwt_handler import decode_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])
service = AuthService()

bearer_scheme = HTTPBearer(auto_error=False)


def get_current_user(credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme)):
    if credentials is None or credentials.scheme.lower() != "bearer":
        raise HTTPException(status_code=401, detail="Not authenticated")

    payload = decode_access_token(credentials.credentials)
    if not payload:
        raise HTTPException(status_code=401, detail="Token expired")

    phone = payload.get("sub")
    if not phone:
        raise HTTPException(status_code=401, detail="Token expired")

    user = service.get_user_by_phone(phone)
    if not user:
        raise HTTPException(status_code=401, detail="Token expired")

    return user


@router.post("/signup")
async def signup(payload: SignupRequest):
    try:
        return service.signup(payload)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))


@router.post("/login")
async def login(payload: LoginRequest):
    try:
        return service.login(payload)
    except ValueError as e:
        # invalid credentials
        raise HTTPException(status_code=401, detail=str(e))


@router.get("/me")
async def me(user=Depends(get_current_user)):
    return {"name": user.get("name"), "phone": user.get("phone")}

