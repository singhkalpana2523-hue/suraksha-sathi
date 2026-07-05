import os
import tempfile
import time

from fastapi import APIRouter, UploadFile, File

from app.services.voice_service import VoiceService
from app.services.ai_manager import AIManager
from app.services.response_builder import ResponseBuilder

router = APIRouter(
    prefix="/analyze",
    tags=["Voice"]
)

voice = VoiceService()
ai = AIManager()


@router.post("/voice")
async def analyze_voice(file: UploadFile = File(...)):
    

    suffix = os.path.splitext(file.filename)[1]

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix
    ) as temp:

        temp.write(await file.read())
        audio_path = temp.name

    try:

        start = time.time()

        voice_result = voice.transcribe(audio_path)

        transcription_time = round(
            time.time() - start,
            2
        )

        if len(voice_result["text"].split()) < 4:
            return {
                "status": "failed",
                "message": "Audio is too short or unclear. Please upload a clearer recording."
            }

        analysis = ai.analyze(
            voice_result["text"]
        )

        metadata = {
            "input_type": "voice",
            "language": voice_result["language"],
            "duration_seconds": voice_result["duration"],
            "transcription_time_seconds": transcription_time,
            "transcribed_text": voice_result["text"]
        }

        return ResponseBuilder.build(
            analysis,
            metadata
        )

    finally:

        if os.path.exists(audio_path):
            os.remove(audio_path)