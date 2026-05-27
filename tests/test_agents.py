import unittest
import sys
from unittest.mock import MagicMock, patch

# Dependency shimming for network-isolated environment
mock_httpx = MagicMock()
mock_openai = MagicMock()

# Since we might need specific exceptions, let's just make sure the modules load
with patch.dict(sys.modules, {'httpx': mock_httpx, 'openai': mock_openai}):
    from app.domain.agents import IScoutAgent

class TestIScoutAgent(unittest.TestCase):
    def test_scout_agent_missing_target_url(self):
        """Test that IScoutAgent.execute raises ValueError when target_url is missing."""
        agent = IScoutAgent()

        # Payload missing target_url
        payload = {}

        with self.assertRaises(ValueError) as context:
            agent.execute(payload)

        self.assertEqual(str(context.exception), "target_url is required for ScoutAgent")

if __name__ == '__main__':
    unittest.main()
