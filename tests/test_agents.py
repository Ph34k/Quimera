import sys
import unittest
from unittest.mock import patch, MagicMock

class MockHttpx(MagicMock):
    class RequestError(Exception):
        pass

class TestAgents(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.modules_patcher = patch.dict('sys.modules', {
            'httpx': MockHttpx(),
            'openai': MagicMock(),
        })
        cls.modules_patcher.start()

        # Safely import the agents module now that dependencies are mocked
        from app.domain.agents import IScoutAgent
        cls.IScoutAgent = IScoutAgent

    @classmethod
    def tearDownClass(cls):
        # Remove the cached module so it doesn't pollute other tests with mocked dependencies
        if 'app.domain.agents' in sys.modules:
            del sys.modules['app.domain.agents']
        cls.modules_patcher.stop()

    def test_scout_agent_exception_handling(self):
        agent = self.IScoutAgent()

        # Mock httpx.get inside the test specifically
        with patch('app.domain.agents.httpx.get') as mock_get:
            mock_get.side_effect = Exception("Simulated network timeout")

            payload = {"target_url": "http://example.com"}
            result = agent.execute(payload)

            self.assertEqual(result["status"], "failed")
            self.assertEqual(result["target"], "http://example.com")
            self.assertEqual(result["error"], "Simulated network timeout")
            self.assertIn("mission_id", result)

if __name__ == '__main__':
    unittest.main()
