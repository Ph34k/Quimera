import sys
import unittest
from unittest.mock import MagicMock

# Dependency shimming for network-isolated environments
mock_httpx = MagicMock()
mock_openai = MagicMock()
mock_config = MagicMock()
mock_config.settings = MagicMock()
mock_config.settings.OPENAI_API_KEY = "mock_key"

class MockClient:
    pass

class TestAgents(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # We need to set up the mock modules before importing agents
        cls.patcher = unittest.mock.patch.dict(
            "sys.modules",
            {
                "httpx": mock_httpx,
                "openai": mock_openai,
                "app.core.config": mock_config,
            },
        )
        cls.patcher.start()

        # Now import the agents module
        global agents
        import app.domain.agents as agents

    @classmethod
    def tearDownClass(cls):
        cls.patcher.stop()

    def test_scribe_agent_missing_draft_text(self):
        """Test that IScribeAgent raises ValueError when draft_text is missing."""
        agent = agents.IScribeAgent()

        with self.assertRaises(ValueError) as context:
            agent.execute({})

        self.assertEqual(str(context.exception), "draft_text required for ScribeAgent")

        with self.assertRaises(ValueError) as context:
            agent.execute({"draft_text": ""})

        self.assertEqual(str(context.exception), "draft_text required for ScribeAgent")
