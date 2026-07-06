from app.services.voice_service import VoiceService
from app.services.ai_manager import AIManager

print("Loading services...")

voice = VoiceService()
ai = AIManager()

print("Transcribing audio...")

text = voice.transcribe("test_files/scam_voice.mp3")

print("\n===== Extracted Text =====")
print(text)

print("\nAnalyzing with AI...")

result = ai.analyze(text)

print("\n===== Final Analysis =====")
print(result)