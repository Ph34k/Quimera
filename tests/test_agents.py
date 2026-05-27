import sys
from unittest.mock import MagicMock
import pytest

# Shim dependencies before importing the module under test
mock_modules = {
    'openai': MagicMock(),
    'httpx': MagicMock()
}
sys.modules.update(mock_modules)

from app.domain.agents import IAnalystAgent

def test_analyst_agent_missing_text_raises_value_error():
    agent = IAnalystAgent()

    with pytest.raises(ValueError, match="text is required for AnalystAgent"):
        agent.execute({})

    with pytest.raises(ValueError, match="text is required for AnalystAgent"):
        agent.execute({"text": ""})
