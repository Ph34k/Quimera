import pytest
from app.domain.agents import IAnalystAgent

def test_analyst_agent_missing_text():
    agent = IAnalystAgent()
    with pytest.raises(ValueError, match="text is required for AnalystAgent"):
        agent.execute({})
