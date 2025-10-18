from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["ok"] is True

def test_list_sensors():
    r = client.get("/api/sensors/")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

def test_bayesian_monthly():
    r = client.get("/api/metrics/bayesian-monthly?m=7")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
