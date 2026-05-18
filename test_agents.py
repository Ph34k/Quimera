import sys
from unittest.mock import MagicMock

# Create a proper custom mock for httpx that defines RequestError
class MockRequestError(Exception):
    def __init__(self, message, request=None):
        super().__init__(message)
        self.request = request

class MockHttpxClient(MagicMock):
    pass

mock_httpx = type('MockHttpx', (), {
    'RequestError': MockRequestError,
    'Client': MockHttpxClient,
    'Request': MagicMock
})()

sys.modules['httpx'] = mock_httpx
sys.modules['openai'] = type('MockOpenAI', (), {'OpenAI': MagicMock()})()

from app.domain.agents import IScoutAgent, IExecutionAgent

scout = IScoutAgent()
exec_agent = IExecutionAgent()

# Basic smoke test for instantiation
print("Scout instance created.")
print("Exec instance created.")
