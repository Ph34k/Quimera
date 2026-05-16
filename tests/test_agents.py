import sys
import unittest
import unittest.mock as mock
import types

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

class TestAgents(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mock_httpx = MockHttpx()
        cls.mock_httpx.__name__ = 'httpx'
        cls.mock_httpx_patcher = mock.patch.dict('sys.modules', {'httpx': cls.mock_httpx})
        cls.mock_httpx_patcher.start()

        cls.mock_openai = mock.MagicMock()
        cls.mock_openai.__name__ = 'openai'
        cls.mock_openai_patcher = mock.patch.dict('sys.modules', {'openai': cls.mock_openai})
        cls.mock_openai_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.mock_httpx_patcher.stop()
        cls.mock_openai_patcher.stop()

    def test_ssrf_protection_blocks_localhost(self):
        from app.domain.agents import is_safe_url
        with mock.patch('app.domain.agents.socket.getaddrinfo') as mock_dns:
            mock_dns.return_value = [(2, 1, 6, '', ('127.0.0.1', 80))]
            self.assertFalse(is_safe_url("http://localhost/admin"))

    def test_ssrf_protection_allows_external(self):
        from app.domain.agents import is_safe_url
        with mock.patch('app.domain.agents.socket.getaddrinfo') as mock_dns:
            mock_dns.return_value = [(2, 1, 6, '', ('93.184.216.34', 80))]
            self.assertTrue(is_safe_url("http://example.com/"))

    def test_execution_agent_ssrf_raises_httpx_error(self):
        from app.domain.agents import IExecutionAgent
        agent = IExecutionAgent()
        with mock.patch('app.domain.agents.socket.getaddrinfo') as mock_dns:
            mock_dns.return_value = [(2, 1, 6, '', ('10.0.0.1', 80))]
            result = agent.execute({"action": "test", "target_url": "http://internal/service"})
            self.assertEqual(result["status"], "execution_failed")
            self.assertIn("URL is not safe", result["error"])

if __name__ == '__main__':
    unittest.main()
