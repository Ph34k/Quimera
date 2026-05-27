from typing import Dict, Any
from openai import OpenAI
from app.core.config import settings
from app.domain.base import BaseAgent

# Initialize real OpenAI client
_openai_api_key = settings.OPENAI_API_KEY
if _openai_api_key == "sk-your-openai-api-key-here" or not _openai_api_key:
    client = None
else:
    client = OpenAI(api_key=_openai_api_key)

class IAnalystAgent(BaseAgent):
    """Agente Analista (Analyst)
    Responsibility: Semantic Processing, Profile Analysis.
    Implemented via real OpenAI API logic.
    """
    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        text = payload.get("text", "")
        if not text:
            raise ValueError("text is required for AnalystAgent")

        if not client:
            raise ValueError("OPENAI_API_KEY is not set or is mock default. Cannot run actual Analyst logic.")

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a senior analyst. Analyze the following text and extract keywords and sentiment."},
                {"role": "user", "content": text}
            ]
        )

        return {
            "status": "analysis_complete",
            "analysis_result": response.choices[0].message.content
        }
