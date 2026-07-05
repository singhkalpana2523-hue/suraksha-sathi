import logging
import time

from app.providers.gemini_provider import GeminiProvider
from app.providers.groq_provider import GroqProvider
from app.services.rag_service import RAGService

logger = logging.getLogger(__name__)


class AIManager:

    def __init__(self):
        self.primary = GeminiProvider()
        self.secondary = GroqProvider()
        self.rag = RAGService()

    def build_prompt(self, text: str):

        matches = self.rag.search(text)

        matched_patterns = []

        knowledge = ""

        for i, item in enumerate(matches, start=1):

            matched_patterns.append({
                "title": item["title"],
                "category": item["category"],
                "similarity": item["similarity"],
                "source": item.get("source", "Unknown")
            })

            knowledge += f"""
Reference {i}

Title:
{item['title']}

Category:
{item['category']}

Summary:
{item.get('summary', '')}

Red Flags:
{', '.join(item.get('red_flags', []))}

Recommended Actions:
{', '.join(item.get('recommended_actions', []))}

Similarity:
{item['similarity']}

--------------------------------
"""

        prompt = f"""
You are SurakshaSathi.

You are an expert cybersecurity assistant specializing in detecting scams.

Use the retrieved knowledge below to analyze the user's message.

Retrieved Scam Knowledge:

{knowledge}

User Message:

{text}

Return ONLY structured JSON matching the AnalysisResponse schema.
"""

        return prompt, matched_patterns

    def analyze(self, text: str):

        prompt, matched_patterns = self.build_prompt(text)

        start = time.time()

        try:

            logger.info("Using Gemini")

            response = self.primary.analyze(prompt)

        except Exception:

            logger.exception("Gemini failed")

            logger.info("Switching to Groq")

            response = self.secondary.analyze(prompt)

        elapsed = int((time.time() - start) * 1000)

        result = response.model_dump()

        result["matched_patterns"] = matched_patterns

        if "recommended_actions" not in result:
          result["recommended_actions"] = []

        if "red_flags" not in result:
         result["red_flags"] = []

        return {

            "provider": response.provider,

            "model": (
                "gemini-2.5-flash"
                if response.provider == "gemini"
                else "llama-3.3-70b-versatile"
            ),

            "response_time_ms": elapsed,

            "analysis": result

        }