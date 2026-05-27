# 🧩 Adding a New Agent

The Quimera ecosystem is built on a strict **Clean Architecture**. Adding a new agent requires defining its core domain logic independently of the web framework, and then exposing it via the API layer.

Here is the step-by-step developer workflow to add a new agent.

## Step 1: Define the Domain Logic

All agents must inherit from the `BaseAgent` abstract base class located in `app/domain/agents.py`.

1. Open `app/domain/agents.py`.
2. Create your new class implementing the `execute` method.

```python
# app/domain/agents.py
from typing import Dict, Any
from app.domain.agents import BaseAgent

class IMyNewAgent(BaseAgent):
    """My New Agent
    Responsibility: Does something cool.
    """
    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        data = payload.get("data")
        if not data:
            raise ValueError("data is required")

        # Your custom logic here
        result_value = f"Processed {data}"

        return {
            "status": "success",
            "result_value": result_value
        }
```

## Step 2: Wire the Agent in the Router

Now expose the agent through the FastAPI router.

1. Open `app/api/router.py`.
2. Import your new agent class.
3. Instantiate the agent.
4. Create the POST route using the `GenericRequest` and `GenericResponse` schemas (or create custom Pydantic schemas if needed).

```python
# app/api/router.py
from app.domain.agents import IMyNewAgent

# ... existing instantiations
my_new_agent = IMyNewAgent()

@api_router.post("/my_new_agent/run", response_model=GenericResponse)
def run_my_new_agent(request: GenericRequest):
    """Executes the My New Agent."""
    try:
        result = my_new_agent.execute(request.payload)
        return GenericResponse(result=result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```

## Step 3: Write Tests

Always ensure your new agent is covered by tests.

1. Open `tests/test_api.py`.
2. Add a test function for your route.

```python
# tests/test_api.py

def test_my_new_agent():
    payload = {"payload": {"data": "test input"}}
    response = client.post("/api/v1/my_new_agent/run", json=payload)
    assert response.status_code == 200
    assert response.json()["result"]["status"] == "success"
```

## Step 4: Update Documentation

Finally, create a Markdown file in `docs/agents/` describing your new agent, its payload, and provide a `curl` example!
