from app.providers.gemini_provider import analyze_text as gemini_analyze
from app.providers.groq_provider import analyze_text as groq_analyze


class AIManager:

    @staticmethod
    def analyze(text: str):

        try:
            print("Using Gemini...")
            return gemini_analyze(text)

        except Exception as e:

            print(f"Gemini failed: {e}")

            print("Switching to Groq...")

            return groq_analyze(text)