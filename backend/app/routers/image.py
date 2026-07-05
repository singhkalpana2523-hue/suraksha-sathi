import os
import time
import tempfile

from fastapi import APIRouter, File, UploadFile

from app.services.ai_manager import AIManager
from app.services.ocr_service import OCRService
from app.services.response_builder import ResponseBuilder

router = APIRouter(
    prefix="/analyze",
    tags=["OCR"]
)

ocr = OCRService()
ai = AIManager()


@router.post("/image")
async def analyze_image(file: UploadFile = File(...)):

    suffix = os.path.splitext(file.filename)[1]

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix
    ) as temp:

        temp.write(await file.read())
        image_path = temp.name

    try:

        start = time.time()

        text = ocr.extract_text(image_path)

        ocr_time = round(time.time() - start, 2)

        print(f"OCR Time: {ocr_time}s")

        analysis = ai.analyze(text)

        metadata = {
            "input_type": "image",
            "ocr_time_seconds": ocr_time,
            "extracted_text": text
        }

        return ResponseBuilder.build(
            analysis,
            metadata
        )

    finally:

        if os.path.exists(image_path):
            os.remove(image_path)