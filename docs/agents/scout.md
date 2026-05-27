# 🕵️ Scout Agent

The **Scout Agent** acts as the reconnaissance component of the Quimera ecosystem. Its primary responsibilities include OSINT (Open Source Intelligence), Web Scraping, and Target Identification.

## API Endpoint

### `POST /api/v1/scout/mission`

Dispatches the Scout Agent to analyze an HTTP target URL.

**Request Body (JSON)**

```json
{
  "target_url": "https://example.com",
  "depth": 1
}
```

*   `target_url` (string, required): The URL the agent should scout.
*   `depth` (integer, optional, defaults to 1): The recursion depth for scraping.

**Response**

```json
{
  "status": "success",
  "mission_id": "550e8400-e29b-41d4-a716-446655440000",
  "target": "https://example.com",
  "http_status": 200,
  "content_length": 1256,
  "error": null
}
```

## Example Usage

Using `curl` to initiate a scout mission:

```bash
curl -X POST "http://localhost:8000/api/v1/scout/mission" \
     -H "Content-Type: application/json" \
     -d '{"target_url": "https://httpbin.org/get", "depth": 1}'
```
