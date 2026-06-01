## 2024-06-01 - HTTPx Connection Pooling in Agents
**Learning:** Using `httpx.get` creates a new client per request, bypassing connection pooling and hurting performance for singleton agents making repeated calls.
**Action:** Always use a persistent `httpx.Client` instance stored on the agent class, with an appropriate `__del__` method to prevent resource leaks.
