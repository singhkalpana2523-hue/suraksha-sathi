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

You are an expert AI that detects online scams.

Use the retrieved scam knowledge below while analysing the user's message.

==========================
Retrieved Scam Knowledge
==========================

{knowledge}

==========================
User Message
==========================

{text}

Return ONLY valid JSON.

{{
  "classification":"SCAM | SUSPICIOUS | SAFE",

  "confidence":95,

  "scam_type":"Phishing",

  "summary":{{
      "en":"Fake SBI KYC message.",
      "hi":"फर्जी SBI KYC संदेश।",
      "gu":"નકલી SBI KYC સંદેશ."
  }},

  "red_flags":[
      {{
          "en":"Fake Link",
          "hi":"फर्जी लिंक",
          "gu":"નકલી લિંક"
      }},
      {{
          "en":"Urgent Request",
          "hi":"तुरंत कार्यवाही",
          "gu":"તાત્કાલિક કાર્યવાહી"
      }},
      {{
          "en":"Unknown Sender",
          "hi":"अज्ञात प्रेषक",
          "gu":"અજાણ્યો મોકલનાર"
      }},
      {{
          "en":"Requests OTP",
          "hi":"OTP मांगता है",
          "gu":"OTP માંગે છે"
      }}
  ],

  "action_steps":[
      {{
          "en":"Ignore Message",
          "hi":"संदेश अनदेखा करें",
          "gu":"સંદેશ અવગણો"
      }},
      {{
          "en":"Don't Click",
          "hi":"लिंक न खोलें",
          "gu":"લિંક ન ખોલો"
      }},
      {{
          "en":"Call Bank",
          "hi":"बैंक से संपर्क करें",
          "gu":"બેંકમાં ફોન કરો"
      }},
      {{
          "en":"Report 1930",
          "hi":"1930 पर रिपोर्ट करें",
          "gu":"1930 પર ફરિયાદ કરો"
      }}
  ]
}}

Rules:

1. Return ONLY JSON.
2. Never use markdown.
3. confidence must be an integer between 0 and 100.
4. summary must be ONE sentence (maximum 10 words).
5. scam_type must contain at most 3 words.
6. red_flags must contain exactly 4 short items.
7. action_steps must contain exactly 4 short items.
8. Translate summary, red_flags and action_steps into:
   - English
   - Hindi
   - Gujarati
"""

        return prompt, matched_patterns

    def analyze(self, text: str):

        prompt, matched_patterns = self.build_prompt(text)

        start = time.time()

        try:

            logger.info("Using Gemini")

            # PRIMARY MODEL
            response = self.primary.analyze(prompt)

        except Exception as gemini_error:

            logger.exception(f"Gemini failed: {gemini_error}")

            logger.info("Switching to Groq...")

            try:

                # FALLBACK MODEL
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