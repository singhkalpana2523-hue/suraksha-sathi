import json

from groq import Groq

from app.config import GROQ_API_KEY
from app.prompts.prompt_service import SYSTEM_PROMPT
from app.models.response import AnalysisResponse


client = Groq(api_key=GROQ_API_KEY)


def analyze_text(text: str):

    completion = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": text
            }
        ],

        temperature=0.2,

        response_format={
            "type": "json_object"
        }

    )

    result = completion.choices[0].message.content

    data = json.loads(result)

    data["provider"] = "groq"

    return AnalysisResponse(**data)