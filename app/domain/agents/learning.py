import time
from typing import Dict, Any
from app.domain.base import BaseAgent

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
