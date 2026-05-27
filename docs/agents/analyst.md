# 🧠 Analyst Agent

The **Analyst Agent** is responsible for Semantic Processing and Profile Analysis. It leverages Large Language Models (LLMs) to extract intelligence, parse data, and make logical inferences.

## API Endpoint

### `POST /api/v1/analyst/process`

Executes the Analyst Agent logic on a provided block of text.

**Request Body (JSON)**

```json
{
  "payload": {
    "text": "The quick brown fox jumps over the lazy dog."
  }
}
```

*   `payload.text` (string, required): The text to be semantically analyzed.

**Response**

```json
{
  "result": {
    "status": "analysis_complete",
    "analysis_result": "Extracted Keywords: fox, dog. Sentiment: Neutral."
  }
}
```

*(Note: If the `OPENAI_API_KEY` is not properly configured, the API will return a 400 error indicating that the actual Analyst logic cannot run).*

## Example Usage

```bash
curl -X POST "http://localhost:8000/api/v1/analyst/process" \
     -H "Content-Type: application/json" \
     -d '{"payload": {"text": "Evaluate this user forum post for spam."}}'
```
