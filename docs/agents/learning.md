# ⏱️ Learning Agent

The **Learning Agent** applies heuristics and performs shadow-ban validation. In its current implementation, it acts as a behavioral rate limiter, tracking target interactions and calculating risk levels based on interaction frequency.

## API Endpoint

### `POST /api/v1/learning/check`

Checks if it is safe to engage with a specific target based on historical interaction timing.

**Request Body (JSON)**

```json
{
  "payload": {
    "target_id": "user_42"
  }
}
```

*   `payload.target_id` (string, required): A unique identifier for the target being checked (e.g., user ID, IP address).

**Response**

If safe (no recent interactions within the cooldown window):
```json
{
  "result": {
    "status": "learning_validation_complete",
    "target_id": "user_42",
    "is_safe_to_engage": true,
    "risk_level": "Low"
  }
}
```

If unsafe (an interaction occurred within the last 60 seconds):
```json
{
  "result": {
    "status": "learning_validation_complete",
    "target_id": "user_42",
    "is_safe_to_engage": false,
    "risk_level": "High - Cooldown Active"
  }
}
```

## Example Usage

```bash
# First request (Safe)
curl -X POST "http://localhost:8000/api/v1/learning/check" \
     -H "Content-Type: application/json" \
     -d '{"payload": {"target_id": "forum_thread_99"}}'

# Immediate second request (Unsafe/High Risk)
curl -X POST "http://localhost:8000/api/v1/learning/check" \
     -H "Content-Type: application/json" \
     -d '{"payload": {"target_id": "forum_thread_99"}}'
```
