import sys
import unittest.mock

# Dependency shimming for isolated testing
sys.modules['fastapi'] = unittest.mock.MagicMock()
sys.modules['pydantic'] = unittest.mock.MagicMock()
sys.modules['sqlalchemy'] = unittest.mock.MagicMock()
sys.modules['openai'] = unittest.mock.MagicMock()

import unittest
from unittest.mock import patch
import socket

from app.domain.agents import is_safe_url, IScoutAgent, IExecutionAgent, verify_request

class TestAgentsSSRF(unittest.TestCase):

    @patch('app.domain.agents.socket.getaddrinfo')
    def test_is_safe_url_public(self, mock_getaddrinfo):
        # Mock public IP resolution
        mock_getaddrinfo.return_value = [(socket.AF_INET, socket.SOCK_STREAM, 6, '', ('93.184.216.34', 80))]
        self.assertTrue(is_safe_url("http://example.com"))

    @patch('app.domain.agents.socket.getaddrinfo')
    def test_is_safe_url_private(self, mock_getaddrinfo):
        # Mock local/private IP resolution
        mock_getaddrinfo.return_value = [(socket.AF_INET, socket.SOCK_STREAM, 6, '', ('127.0.0.1', 80))]
        self.assertFalse(is_safe_url("http://localhost"))

    @patch('app.domain.agents.socket.getaddrinfo')
    def test_is_safe_url_metadata(self, mock_getaddrinfo):
        # Mock metadata IP resolution
        mock_getaddrinfo.return_value = [(socket.AF_INET, socket.SOCK_STREAM, 6, '', ('169.254.169.254', 80))]
        self.assertFalse(is_safe_url("http://169.254.169.254"))

    @patch('app.domain.agents.socket.getaddrinfo')
    def test_verify_request_unsafe(self, mock_getaddrinfo):
        # Test the hook directly
        mock_getaddrinfo.return_value = [(socket.AF_INET, socket.SOCK_STREAM, 6, '', ('127.0.0.1', 80))]
        request_mock = unittest.mock.MagicMock()
        request_mock.url = "http://localhost/admin"

        with self.assertRaises(ValueError) as context:
            verify_request(request_mock)
        self.assertIn("Unsafe target URL detected", str(context.exception))

    @patch('app.domain.agents.socket.getaddrinfo')
    def test_scout_agent_ssrf(self, mock_getaddrinfo):
        mock_getaddrinfo.return_value = [(socket.AF_INET, socket.SOCK_STREAM, 6, '', ('127.0.0.1', 80))]
        agent = IScoutAgent()

        # Test execution with unsafe URL
        result = agent.execute({"target_url": "http://127.0.0.1/internal-api"})
        self.assertEqual(result["status"], "failed")
        self.assertIn("Unsafe target URL detected", result["error"])

    @patch('app.domain.agents.socket.getaddrinfo')
    def test_execution_agent_ssrf(self, mock_getaddrinfo):
        mock_getaddrinfo.return_value = [(socket.AF_INET, socket.SOCK_STREAM, 6, '', ('169.254.169.254', 80))]
        agent = IExecutionAgent()

        # Test execution with unsafe URL
        result = agent.execute({"action": "click", "target_url": "http://169.254.169.254/latest/meta-data/"})
        self.assertEqual(result["status"], "execution_failed")
        self.assertIn("Unsafe target URL detected", result["error"])

if __name__ == '__main__':
    unittest.main()
