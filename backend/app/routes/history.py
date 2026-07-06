from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.schemas.history_schema import CreateHistoryRequest
from app.services.history_service import HistoryService
from app.utils.jwt_handler import decode_access_token

router = APIRouter(prefix="/history", tags=["History"])
service = HistoryService()

bearer_scheme = HTTPBearer(auto_error=False)


def get_current_user_id(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
) -> str:
    if credentials is None or credentials.scheme.lower() != "bearer":
        raise HTTPException(status_code=401, detail="Not authenticated")

    payload = decode_access_token(credentials.credentials)
    if not payload:
        raise HTTPException(status_code=401, detail="Token expired")

    phone = payload.get("sub")
    if not phone:
        raise HTTPException(status_code=401, detail="Token expired")

    # We use phone as user_id for now (matches auth_service.create_access_token(subject=phone)).
    return str(phone)


@router.post("")
async def create_history(req: CreateHistoryRequest, user_id: str = Depends(get_current_user_id)):
    return service.create_history(user_id=user_id, req=req)


@router.get("")
async def list_history(
    user_id: str = Depends(get_current_user_id),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    sort: str = Query("desc", pattern="^(asc|desc)$"),
):
    data = service.list_histories(user_id=user_id, page=page, limit=limit, sort=sort)
    if not data.get("data") and data.get("total", 0) == 0:
        return {"message": "No history available"}
    return data


@router.get("/search")
async def search_history(
    q: str = Query(..., min_length=1),
    user_id: str = Depends(get_current_user_id),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    sort: str = Query("desc", pattern="^(asc|desc)$"),
):
    data = service.search_histories(user_id=user_id, query=q, page=page, limit=limit, sort=sort)
    if data.get("total", 0) == 0:
        return {"message": "No history available"}
    return data


@router.get("/{history_id}")
async def get_history(
    history_id: str,
    user_id: str = Depends(get_current_user_id),
):
    doc = service.get_history(user_id=user_id, history_id=history_id)
    if not doc:
        raise HTTPException(status_code=404, detail="History not found")
    return doc


@router.delete("/{history_id}")
async def delete_history(
    history_id: str,
    user_id: str = Depends(get_current_user_id),
):
    ok = service.delete_history(user_id=user_id, history_id=history_id)
    if not ok:
        raise HTTPException(status_code=404, detail="History not found")
    return {"message": "History deleted successfully"}


@router.delete("")
async def delete_all_history(user_id: str = Depends(get_current_user_id)):
    deleted = service.delete_all_histories(user_id=user_id)
    return {"message": "All history deleted", "deleted": deleted}

