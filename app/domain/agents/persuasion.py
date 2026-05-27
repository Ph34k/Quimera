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

class IPersuasionAgent(BaseAgent):
    """Motor de Persuasão (Persuasion)
    Responsibility: Application of Cialdini triggers via OpenAI.
    """
    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        trigger = payload.get("trigger", "reciprocity")
        context = payload.get("context", "networking")

        if not client:
            raise ValueError("OPENAI_API_KEY is not set or is mock default. Cannot run actual Persuasion logic.")

        prompt = f"Write a short, persuasive message applying the Cialdini principle of '{trigger}' for the following context: '{context}'."

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert copywriter specialized in Cialdini's persuasion triggers."},
                {"role": "user", "content": prompt}
            ]
        )

        return {
            "status": "persuasion_generated",
            "trigger_used": trigger,
            "persuasive_text": response.choices[0].message.content
        }
