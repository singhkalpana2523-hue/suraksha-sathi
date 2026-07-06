from faster_whisper import WhisperModel


class VoiceService:

    def __init__(self):

        print("Loading Faster-Whisper model...")

        self.model = WhisperModel(
            "tiny",
            device="cpu",
            compute_type="int8"
        )

        print("Faster-Whisper Loaded!")

    def transcribe(self, audio_path: str):

        segments, info = self.model.transcribe(
            audio_path,
            beam_size=5
        )

        text = ""

        for segment in segments:
            text += segment.text + " "

        return {
            "text": text.strip(),
            "language": info.language,
            "duration": round(info.duration, 2)
        }