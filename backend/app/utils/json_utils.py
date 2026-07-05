import json
import re


def extract_json(text: str):
    """
    Extract JSON from Gemini response.
    Handles:
    - ```json ... ```
    - Extra explanations
    - Plain JSON
    """

    text = text.strip()

    # Remove markdown code fences
    text = re.sub(r"^```json", "", text, flags=re.IGNORECASE).strip()
    text = re.sub(r"```$", "", text).strip()

    # Find first JSON array
    start = text.find("[")
    end = text.rfind("]")

    if start != -1 and end != -1:
        text = text[start:end + 1]

    return json.loads(text)