from app.domain.agents import is_safe_url

def test_is_safe_url():
    assert is_safe_url("http://google.com") is True
    assert is_safe_url("http://localhost:8000") is False
    assert is_safe_url("http://127.0.0.1") is False
    assert is_safe_url("http://[::1]") is False
    assert is_safe_url("http://10.0.0.1") is False
    assert is_safe_url("http://169.254.169.254") is False
    assert is_safe_url("invalid_url") is False
