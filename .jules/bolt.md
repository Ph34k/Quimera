## 2024-06-10 - Persistent HTTPx Client for Agents
**Learning:** Synchronous agents in FastAPI making multiple requests benefit significantly from connection pooling using a persistent `httpx.Client()`. Repeatedly calling `httpx.get()` creates a new connection each time.
**Action:** Use a global persistent `httpx.Client()` for synchronous agent logic to enable TCP connection reuse without requiring a full async architectural rewrite.
