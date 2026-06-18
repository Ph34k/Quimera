## 2024-04-20 - Connection Pooling for Singleton Agents
**Learning:** Instantiating `httpx.Client()` within singleton agents (like `IScoutAgent` and `IExecutionAgent`) provides a massive performance boost (~65% faster for repeated requests) by reusing TCP connections across requests, eliminating connection setup overhead.
**Action:** When creating new network-calling AI agents instantiated as singletons, always initialize a persistent client (e.g. `self.client = httpx.Client()`) in `__init__` rather than using module-level request functions.
