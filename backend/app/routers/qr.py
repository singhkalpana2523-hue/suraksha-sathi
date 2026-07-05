import os
import tempfile

from fastapi import APIRouter, UploadFile, File

from app.services.qr_service import QRService
from app.services.ai_manager import AIManager
from app.services.response_builder import ResponseBuilder

router = APIRouter(
    prefix="/analyze",
    tags=["QR"]
)

qr = QRService()
ai = AIManager()


@router.post("/qr")
async def analyze_qr(file: UploadFile = File(...)):

    suffix = os.path.splitext(file.filename)[1]

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix
    ) as temp:

        temp.write(await file.read())
        image_path = temp.name

    try:

        decoded = qr.decode_qr(image_path)

        if decoded is None:
            return {
                "status": "failed",
                "message": "No QR code found in the image."
            }

        analysis = ai.analyze(
            decoded["content"]
        )

        metadata = {

            "input_type": "qr",

            "qr_type": decoded["qr_type"],

            "decoded_content": decoded["content"]

        }

        return ResponseBuilder.build(
            analysis,
            metadata
        )

    finally:

        if os.path.exists(image_path):
            os.remove(image_path)