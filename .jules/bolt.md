## 2023-10-27 - Implement httpx connection pooling
**Learning:** Using `httpx.get()` directly for every request forces a new TCP handshake each time, adding significant latency overhead for external API calls.
**Action:** Implement a globally shared, persistent `httpx.Client()` to enable connection pooling and reduce request latency for external APIs.
