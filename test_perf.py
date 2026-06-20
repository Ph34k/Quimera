import time
import httpx

def test_no_pool():
    start = time.time()
    for _ in range(5):
        try:
            httpx.get("http://localhost:8000/api/v1/health")
        except Exception:
            pass
    return time.time() - start

def test_pool():
    start = time.time()
    client = httpx.Client()
    for _ in range(5):
        try:
            client.get("http://localhost:8000/api/v1/health")
        except Exception:
            pass
    client.close()
    return time.time() - start

print("No pool:", test_no_pool())
print("Pool:", test_pool())
