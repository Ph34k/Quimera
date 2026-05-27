# 💬 Persuasion Agent

The **Persuasion Agent** applies Robert Cialdini's psychological triggers (such as reciprocity, scarcity, and social proof) to generate highly effective, context-aware copy using LLMs.

## API Endpoint

### `POST /api/v1/persuasion/generate`

Generates persuasive text based on a specified psychological trigger and context.

**Request Body (JSON)**

```json
{
  "payload": {
    "trigger": "social_proof",
    "context": "Convince developers to adopt the new framework."
  }
}
```

*   `payload.trigger` (string, optional, defaults to "reciprocity"): The psychological trigger to apply.
*   `payload.context` (string, optional, defaults to "networking"): The context or objective of the message.

**Response**

```json
{
  "result": {
    "status": "persuasion_generated",
    "trigger_used": "social_proof",
    "persuasive_text": "Join the 10,000+ developers who have already sped up their workflow..."
  }
}
```

*(Note: Requires a valid `OPENAI_API_KEY` to function, otherwise returns a 400 error).*

## Example Usage

```bash
curl -X POST "http://localhost:8000/api/v1/persuasion/generate" \
     -H "Content-Type: application/json" \
     -d '{"payload": {"trigger": "scarcity", "context": "Limited time offer for API access."}}'
```
