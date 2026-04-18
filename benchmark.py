import time
import httpx
from app.domain.agents import IScoutAgent

def test_without_pool():
    start = time.time()
    for _ in range(5):
        try:
            httpx.get("http://example.com", timeout=5.0)
        except Exception:
            pass
    return time.time() - start

def test_with_pool():
    client = httpx.Client()
    start = time.time()
    for _ in range(5):
        try:
            client.get("http://example.com", timeout=5.0)
        except Exception:
            pass
    client.close()
    return time.time() - start

if __name__ == "__main__":
    t1 = test_without_pool()
    t2 = test_with_pool()
    print(f"Without pool: {t1:.4f}s")
    print(f"With pool: {t2:.4f}s")
