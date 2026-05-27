# ✍️ Scribe Agent

The **Scribe Agent** is the "Persona" engine. It takes draft text and uses Natural Language Processing (NLP) to rewrite it, adapting the tone, style, and voice to match a specific persona (internally defined as "Alex", a confident and direct persona).

## API Endpoint

### `POST /api/v1/scribe/rewrite`

Rewrites a given draft text to match the system persona.

**Request Body (JSON)**

```json
{
  "payload": {
    "draft_text": "I think maybe we should consider updating the server."
  }
}
```

*   `payload.draft_text` (string, required): The initial text to be rewritten.

**Response**

```json
{
  "result": {
    "status": "scribe_rewrite_complete",
    "persona": "Alex",
    "rewritten_text": "Update the server immediately. It's a critical operational requirement."
  }
}
```

*(Note: Requires a valid `OPENAI_API_KEY` to function, otherwise returns a 400 error).*

## Example Usage

```bash
curl -X POST "http://localhost:8000/api/v1/scribe/rewrite" \
     -H "Content-Type: application/json" \
     -d '{"payload": {"draft_text": "Can someone help me with this bug please?"}}'
```
