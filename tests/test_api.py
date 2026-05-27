from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "online"
    assert "project" in data

def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_scout_mission_dispatch():
    payload = {
        "target_url": "https://httpbin.org/get",
        "depth": 2
    }
    response = client.post("/api/v1/scout/mission", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["target"] == "https://httpbin.org/get"
    assert "mission_id" in data
    assert data["http_status"] == 200
    assert data["content_length"] > 0
