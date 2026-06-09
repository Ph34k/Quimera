import time
import httpx

url = "https://httpbin.org/status/200"

def test_without_client():
    start = time.time()
    for _ in range(5):
        httpx.get(url)
    return time.time() - start

def test_with_client():
    client = httpx.Client()
    start = time.time()
    for _ in range(5):
        client.get(url)
    return time.time() - start

t1 = test_without_client()
t2 = test_with_client()
print(f"Without client: {t1:.4f}s")
print(f"With client: {t2:.4f}s")
