# 🚀 Execution Agent

The **Execution Agent** serves as the "armed branch" of the system. It interacts directly with external platforms, performing real web driving with stealth capabilities (via advanced HTTP headers).

## API Endpoint

### `POST /api/v1/execution/run`

Triggers an execution task against a specified target URL.

**Request Body (JSON)**

```json
{
  "payload": {
    "action": "ping",
    "target_url": "https://httpbin.org/status/200"
  }
}
```

*   `payload.action` (string, required): The specific action to execute (e.g., `ping`, `deploy`).
*   `payload.target_url` (string, required): The destination URL for the action.

**Response**

```json
{
  "result": {
    "status": "execution_successful",
    "action": "ping",
    "target_http_status": 200,
    "content_length": 0
  }
}
```

## Example Usage

```bash
curl -X POST "http://localhost:8000/api/v1/execution/run" \
     -H "Content-Type: application/json" \
     -d '{"payload": {"action": "ping", "target_url": "https://httpbin.org/status/200"}}'
```
