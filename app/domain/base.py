from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseAgent(ABC):
    """Abstract Base Class for all Quimera Agents."""

    @abstractmethod
    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        pass
