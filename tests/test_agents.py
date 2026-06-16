import unittest
import pytest
import sys
from unittest.mock import MagicMock, patch

class TestIScoutAgent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mock_httpx = MagicMock()
        cls.mock_openai = MagicMock()

        cls.patcher = patch.dict('sys.modules', {
            'httpx': cls.mock_httpx,
            'openai': cls.mock_openai
        })
        cls.patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.patcher.stop()

    def test_execute_missing_target_url(self):
        from app.domain.agents import IScoutAgent
        agent = IScoutAgent()
        with pytest.raises(ValueError, match="target_url is required for ScoutAgent"):
            agent.execute({})

    def test_execute_empty_target_url(self):
        from app.domain.agents import IScoutAgent
        agent = IScoutAgent()
        with pytest.raises(ValueError, match="target_url is required for ScoutAgent"):
            agent.execute({"target_url": ""})
