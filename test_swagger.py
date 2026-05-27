from fastapi.testclient import TestClient
from app.main import app
import json

client = TestClient(app)

def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    schema = response.json()
    assert "openapi" in schema

    with open("openapi.json", "w") as f:
        json.dump(schema, f, indent=2)

if __name__ == "__main__":
    test_openapi_schema()
    print("Schema generated successfully!")
