import openai
from openai import OpenAI
import time
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

class LLMService:
    def __init__(self, api_key: str, model: str = "gpt-4o-mini", timeout: int = 30):
        self.api_key = api_key
        self.model = model
        self.timeout = timeout
        self.client = OpenAI(api_key=self.api_key, timeout=self.timeout)
        self._cache: Dict[str, str] = {} # In-memory cache for MVP

    def generate(self, prompt: str, system_message: Optional[str] = None, retries: int = 3) -> str:
        cache_key = f"{self.model}:{system_message}:{prompt}"
        if cache_key in self._cache:
            logger.info("LLM cache hit")
            return self._cache[cache_key]

        messages = []
        if system_message:
            messages.append({"role": "system", "content": system_message})
        messages.append({"role": "user", "content": prompt})

        attempt = 0
        while attempt < retries:
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                )
                result = response.choices[0].message.content
                if result is not None:
                    self._cache[cache_key] = result
                    return result
                return ""
            except Exception as e:
                attempt += 1
                logger.warning(f"LLM generate failed on attempt {attempt}: {e}")
                if attempt >= retries:
                    logger.error("LLM generate exhausted all retries")
                    raise e
                time.sleep(2 ** attempt) # Exponential backoff
        return ""
