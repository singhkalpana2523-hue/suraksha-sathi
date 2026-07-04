from typing import Any, List

from fastapi import APIRouter

from app.models.dataset_record import DatasetRecord
from app.services.dataset_service import DatasetService

router = APIRouter(
    prefix="/dataset",
    tags=["Dataset"],
)

service = DatasetService()


def _serialize_record(record: DatasetRecord) -> dict[str, Any]:
    # Pydantic v1 vs v2 compatibility
    try:
        return record.model_dump()  # type: ignore[attr-defined]
    except AttributeError:
        return record.dict()  # type: ignore[call-arg]


@router.post("/save")
async def save_dataset(record: DatasetRecord):
    payload = _serialize_record(record)

    filename = service.save_record(payload)

    return {
        "status": "saved",
        "file": filename,
    }


@router.post("/official/import")
async def import_official_dataset(records: List[DatasetRecord]):
    """Import an official dataset (array of DatasetRecord)."""

    payloads = [_serialize_record(r) for r in records]
    filename = service.save_record(payloads)

    return {
        "status": "official_imported",
        "file": filename,
        "count": len(payloads),
    }

