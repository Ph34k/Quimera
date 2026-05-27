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

class IScribeAgent(BaseAgent):
    """Agente Escriba (Scribe)
    Responsibility: The 'Persona', NLP generation via OpenAI.
    """
    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        draft = payload.get("draft_text", "")
        if not draft:
            raise ValueError("draft_text required for ScribeAgent")

        if not client:
            raise ValueError("OPENAI_API_KEY is not set or is mock default. Cannot run actual Scribe logic.")

        prompt = f"Rewrite the following draft to match the confident, direct persona of 'Alex'. Draft: {draft}"

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are 'Alex', acting as a confident persona rewriting text."},
                {"role": "user", "content": prompt}
            ]
        )

        return {
            "status": "scribe_rewrite_complete",
            "persona": "Alex",
            "rewritten_text": response.choices[0].message.content
        }
