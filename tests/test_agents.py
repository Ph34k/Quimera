import unittest
from unittest.mock import patch

from app.domain.agents import IScoutAgent

class TestAgentsSSRF(unittest.TestCase):
    def setUp(self):
        self.scout_agent = IScoutAgent()

    @patch('app.domain.agents.socket.getaddrinfo')
    def test_ssrf_protection_blocks_localhost(self, mock_getaddrinfo):
        # Mock DNS resolution to return 127.0.0.1
        mock_getaddrinfo.return_value = [(2, 1, 6, '', ('127.0.0.1', 80))]

        result = self.scout_agent.execute({"target_url": "http://example.com"})

        self.assertEqual(result["status"], "failed")
        self.assertIn("Security Policy Violation", result["error"])

    @patch('app.domain.agents.socket.getaddrinfo')
    def test_ssrf_protection_allows_public_ip(self, mock_getaddrinfo):
        # Mock DNS resolution to return a public IP
        mock_getaddrinfo.return_value = [(2, 1, 6, '', ('8.8.8.8', 80))]

        # Test just the URL validation to ensure it doesn't raise
        from app.domain.agents import is_safe_url
        self.assertTrue(is_safe_url("http://example.com"))
