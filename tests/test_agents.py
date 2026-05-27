import unittest
from unittest.mock import patch

class TestAgents(unittest.TestCase):
    def test_scout_agent_exception_handling(self):
        """
        Test that IScoutAgent.execute() correctly catches exceptions from httpx.get
        and returns the expected failure dictionary.
        """
        from app.domain.agents import IScoutAgent

        agent = IScoutAgent()

        # We patch app.domain.agents.httpx.get specifically for this test
        with patch('app.domain.agents.httpx.get') as mock_get:
            # Configure the mock to raise an exception when called
            mock_error_message = "Connection timeout"
            mock_get.side_effect = Exception(mock_error_message)

            payload = {"target_url": "https://example.com"}

            # Execute the agent
            result = agent.execute(payload)

            # Assertions
            self.assertEqual(result["status"], "failed")
            self.assertEqual(result["target"], "https://example.com")
            self.assertEqual(result["error"], mock_error_message)
            self.assertIn("mission_id", result)

if __name__ == '__main__':
    unittest.main()
