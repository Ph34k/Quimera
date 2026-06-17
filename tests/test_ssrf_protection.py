import pytest
from app.domain.agents import IScoutAgent, IExecutionAgent

def test_ssrf_scout_agent():
    agent = IScoutAgent()

    # Internal IP
    res = agent.execute({"target_url": "http://127.0.0.1:8000"})
    assert res["status"] == "failed"
    assert "SSRF Protection" in res["error"]

    # Internal DNS
    res = agent.execute({"target_url": "http://localhost:8000"})
    assert res["status"] == "failed"
    assert "SSRF Protection" in res["error"]

def test_ssrf_execution_agent():
    agent = IExecutionAgent()

    # Internal IP
    res = agent.execute({"action": "scan", "target_url": "http://127.0.0.1:8000"})
    assert res["status"] == "execution_failed"
    assert "SSRF Protection" in res["error"]
