from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseAgent(ABC):
    """Abstract Base Class for all Quimera Agents."""

    @abstractmethod
    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        pass

import httpx
import uuid
import urllib.parse
import ipaddress
import socket

def is_safe_url(url: str) -> bool:
    """Valida se uma URL é segura para evitar SSRF."""
    try:
        parsed = urllib.parse.urlparse(url)
        if parsed.scheme not in ("http", "https"):
            return False
        hostname = parsed.hostname
        if not hostname:
            return False

        # Ignora a resolução de nomes que possam levantar exceções
        ip_addr = socket.gethostbyname(hostname)
        ip = ipaddress.ip_address(ip_addr)

        # Bloqueia IPs privados, loopback, link local e multicast
        if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_multicast:
            return False

        return True
    except Exception:
        # Se houver erro na validação ou resolução DNS, negue por segurança
        return False

class IScoutAgent(BaseAgent):
    """Agente Batedor (Scout)
    Responsibility: OSINT, Web Scraping, Target Identification
    """
    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        target_url = payload.get("target_url")
        if not target_url:
            raise ValueError("target_url is required for ScoutAgent")

        if not is_safe_url(target_url):
            return {
                "status": "failed",
                "mission_id": str(uuid.uuid4()),
                "target": target_url,
                "error": "URL bloqueada: possível tentativa de SSRF."
            }

        try:
            # MVP: Real HTTP request instead of mock. Disabling redirects to prevent SSRF bypass
            response = httpx.get(target_url, timeout=5.0, follow_redirects=False)
            return {
                "status": "success",
                "mission_id": str(uuid.uuid4()),
                "target": target_url,
                "http_status": response.status_code,
                "content_length": len(response.text)
            }
        except Exception as e:
            return {
                "status": "failed",
                "mission_id": str(uuid.uuid4()),
                "target": target_url,
                "error": str(e)
            }

import time
from openai import OpenAI
from app.core.config import settings

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

class IExecutionAgent(BaseAgent):
    """Agente de Execução (Execution)
    Responsibility: Real Stealth web driving (via HTTPx with advanced headers).
    """
    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        action = payload.get("action")
        target_url = payload.get("target_url")
        if not action or not target_url:
            raise ValueError("action and target_url required for ExecutionAgent")

        if not is_safe_url(target_url):
            return {"status": "execution_failed", "error": "URL bloqueada: possível tentativa de SSRF."}

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
        try:
            # Desabilita follow_redirects para prevenir SSRF via redirecionamentos maliciosos
            resp = httpx.get(target_url, headers=headers, timeout=5.0, follow_redirects=False)
            return {
                "status": "execution_successful",
                "action": action,
                "target_http_status": resp.status_code,
                "content_length": len(resp.text)
            }
        except Exception as e:
            return {"status": "execution_failed", "error": str(e)}

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

# Global in-memory store for rate limiting
_LEARNING_DB = {}

class ILearningAgent(BaseAgent):
    """Agente de Aprendizagem (Learning)
    Responsibility: Heuristics, Shadow ban validation.
    Implemented locally via in-memory rate limit checking.
    """
    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        target_id = payload.get("target_id")
        if not target_id:
            raise ValueError("target_id required for LearningAgent")

        current_time = time.time()
        last_action = _LEARNING_DB.get(target_id, 0)

        # If action happened less than 60 seconds ago, flag as potential shadowban risk
        if current_time - last_action < 60:
            is_safe = False
            risk_level = "High - Cooldown Active"
        else:
            is_safe = True
            risk_level = "Low"
            _LEARNING_DB[target_id] = current_time

        return {
            "status": "learning_validation_complete",
            "target_id": target_id,
            "is_safe_to_engage": is_safe,
            "risk_level": risk_level
        }
