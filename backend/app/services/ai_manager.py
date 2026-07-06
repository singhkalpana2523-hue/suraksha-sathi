import logging
import time

from app.providers.gemini_provider import GeminiProvider
from app.providers.groq_provider import GroqProvider
from app.services.rag_service import get_default_rag_service

logger = logging.getLogger(__name__)


class AIManager:

    def __init__(self):
        self.primary = GeminiProvider()
        self.secondary = GroqProvider()
        self.rag = get_default_rag_service()

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
{", ".join(item.get("red_flags", []))}

Recommended Actions:
{", ".join(item.get("recommended_actions", []))}

Similarity:
{item["similarity"]}

----------------------------------------
"""

        prompt = f"""
You are SurakshaSathi.

You are an expert AI that detects financial scams.

Use the scam knowledge below while analyzing the user's message.

=====================
Retrieved Knowledge
=====================

{knowledge}

=====================
User Message
=====================

{text}

Return ONLY valid JSON.

{{
    "classification":"SCAM",
    "confidence":95,
    "scam_type":"Phishing",

    "summary":{{
        "en":"Short sentence",
        "hi":"छोटा वाक्य",
        "gu":"ટૂંકું વાક્ય"
    }},

    "red_flags":[
        {{
            "en":"Fake Link",
            "hi":"फर्जी लिंक",
            "gu":"નકલી લિંક"
        }}
    ],

    "action_steps":[
        {{
            "en":"Don't Click",
            "hi":"क्लिक मत करें",
            "gu":"ક્લિક કરશો નહીં"
        }}
    ]
}}

Rules:

1. Return ONLY JSON.
2. No markdown.
3. confidence = integer (0-100).
4. summary = one short sentence.
5. red_flags = max 4 items.
6. action_steps = max 4 items.
"""

        return prompt, matched_patterns

    def analyze(self, text: str):

        prompt, matched_patterns = self.build_prompt(text)

        start = time.time()

        response = None

        try:

            logger.info("Using Gemini")

            response = self.secondary.analyze(prompt)

        except Exception as gemini_error:

            logger.exception(f"Gemini failed: {gemini_error}")

            logger.info("Switching to Groq...")

            try:

                response = self.secondary.analyze(prompt)

            except Exception as groq_error:

                logger.exception(f"Groq also failed: {groq_error}")

                raise

        elapsed = int((time.time() - start) * 1000)

        result = response.model_dump()

        result["matched_patterns"] = matched_patterns

        if "red_flags" not in result:
            result["red_flags"] = []

        if "action_steps" not in result:
            result["action_steps"] = []

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