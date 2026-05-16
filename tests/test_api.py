import sys
import unittest.mock as mock

class MockHttpx:
    class RequestError(Exception):
        def __init__(self, message, request=None):
            super().__init__(message)
            self.request = request
    class Client:
        def __init__(self, *args, **kwargs):
            self.event_hooks = kwargs.get('event_hooks', {})
            self.follow_redirects = kwargs.get('follow_redirects', False)
            self.timeout = kwargs.get('timeout', None)

        def get(self, url, *args, **kwargs):
            import collections
            Request = collections.namedtuple('Request', ['url'])
            req = Request(url=url)
            for hook in self.event_hooks.get('request', []):
                hook(req)
            Response = collections.namedtuple('Response', ['status_code', 'text'])
            return Response(status_code=200, text="Mocked")

        def close(self):
            pass

    def get(self, url, *args, **kwargs):
        import collections
        Response = collections.namedtuple('Response', ['status_code', 'text'])
        return Response(status_code=200, text="Mocked")

mock_httpx = MockHttpx()
mock_httpx.__name__ = 'httpx'
sys.modules['httpx'] = mock_httpx

mock_openai = mock.MagicMock()
mock_openai.__name__ = 'openai'
sys.modules['openai'] = mock_openai

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "online"
    assert "project" in data

def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_scout_mission_dispatch():
    payload = {
        "target_url": "https://httpbin.org/get",
        "depth": 2
    }
    response = client.post("/api/v1/scout/mission", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["target"] == "https://httpbin.org/get"
    assert "mission_id" in data
    assert data["http_status"] == 200
    assert data["content_length"] > 0

def test_analyst_agent():
    payload = {"payload": {"text": "hello world from analyst test the test"}}
    response = client.post("/api/v1/analyst/process", json=payload)
    # Since we are using the dummy key from .env.example, it should gracefully return a 400
    # showing the code path reached the external check
    assert response.status_code == 400
    assert "Cannot run actual Analyst logic" in response.json()["detail"]

def test_execution_agent():
    payload = {"payload": {"action": "ping", "target_url": "https://httpbin.org/status/200"}}
    response = client.post("/api/v1/execution/run", json=payload)
    assert response.status_code == 200
    data = response.json()["result"]
    assert data["status"] == "execution_successful"
    assert data["target_http_status"] == 200

def test_persuasion_agent():
    payload = {"payload": {"trigger": "social_proof", "context": "testing"}}
    response = client.post("/api/v1/persuasion/generate", json=payload)
    assert response.status_code == 400
    assert "Cannot run actual Persuasion logic" in response.json()["detail"]

def test_scribe_agent():
    payload = {"payload": {"draft_text": "bom dia, por favor me ajude."}}
    response = client.post("/api/v1/scribe/rewrite", json=payload)
    assert response.status_code == 400
    assert "Cannot run actual Scribe logic" in response.json()["detail"]

def test_learning_agent():
    payload = {"payload": {"target_id": "user_42"}}
    response = client.post("/api/v1/learning/check", json=payload)
    assert response.status_code == 200
    data = response.json()["result"]
    assert data["is_safe_to_engage"] is True

    # Second request immediately should be flagged due to rate limit simulation
    response2 = client.post("/api/v1/learning/check", json=payload)
    data2 = response2.json()["result"]
    assert data2["is_safe_to_engage"] is False
