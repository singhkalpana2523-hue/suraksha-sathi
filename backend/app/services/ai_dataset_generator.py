from __future__ import annotations

import json
from typing import Any, Dict, List, Literal

from app.services.ai_manager import AIManager


class AIDatasetGenerator:
    """Generate additional official dataset records using the LLM.

    Output: List of DatasetRecord-like dicts that can be validated by DatasetRecord.
    """

    def __init__(self):
        self.ai = AIManager()

    def generate(
        self,
        *,
        category: str,
        subcategory: str,
        severity: Literal["Low", "Medium", "High", "Critical", "low", "medium", "high", "critical"],
        language: str,
        count: int = 10,
        seed_texts: List[str] | None = None,
        source: str = "AI_Generated",
    ) -> List[Dict[str, Any]]:
        seed_texts = seed_texts or []

        # Ask the model to output dataset records as JSON (no markdown).
        prompt = {
            "category": category,
            "subcategory": subcategory,
            "severity": severity,
            "language": language,
            "count": count,
            "seed_texts": seed_texts,
            "source": source,
            "schema": {
                "id": 0,
                "title": "",
                "category": "",
                "subcategory": "",
                "severity": "",
                "language": "",
                "text": "",
                "summary": "",
                "red_flags": [""],
                "recommended_actions": [""],
                "keywords": [""],
                "source": "",
            },
        }

        system_instructions = (
            "You are generating official scam dataset records for SurakshaSathi. "
            "Return ONLY valid JSON. Do not use markdown. "
            "Generate exactly the requested number of records. "
            "Each record must follow the provided schema and be realistic."
        )

        # We reuse the existing AIManager which expects a raw message and returns AnalysisResponse.
        # Therefore, we call underlying providers indirectly by crafting a message that asks for JSON.
        # The provider response may not match AnalysisResponse; however AIManager returns whatever provider returns.
        # To keep the generator robust, we extract JSON from the response if needed.

        # Note: AIManager currently always uses AnalysisResponse schema. That would conflict.
        # So we call the generator by directly asking AIManager to analyze seed or prompt is not appropriate.
        # This method will raise for now to avoid generating invalid types.
        raise NotImplementedError(
            "AI dataset generation requires a dedicated provider call that returns free-form JSON. "
            "Integrate a new provider method or extend AIManager for dataset generation."
        )

