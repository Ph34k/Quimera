## 2024-06-21 - [HTTPx Connection Pooling]
**Learning:** Instantiating a new `httpx` client for every request (e.g., `httpx.get(...)`) misses the opportunity to reuse TCP connections, leading to high latency for repeated requests.
**Action:** Use a globally instantiated `httpx.Client()` object to preserve connection pools across agent executions.
