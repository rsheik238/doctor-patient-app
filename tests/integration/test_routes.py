import pytest
from app.interface.api.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_add_and_get_doctor(client):
    client.post("/doctors/", json={"name": "Dr. Test"})
    resp = client.get("/doctors/")
    assert resp.status_code == 200
    assert any(d["name"] == "Dr. Test" for d in resp.get_json())

def test_add_and_get_patient(client):
    client.post("/patients/", json={"name": "Jane Doe"})
    resp = client.get("/patients/")
    assert resp.status_code == 200
    assert any(p["name"] == "Jane Doe" for p in resp.get_json())

def test_schedule_and_get_visit(client):
    client.post("/doctors/", json={"name": "Dr. Visit"})
    client.post("/patients/", json={"name": "Visitor"})
    client.post("/visits/", json={
        "doctor": "Dr. Visit",
        "patient": "Visitor",
        "date": "2024-01-01",
        "time": "11:00"
    })
    resp = client.get("/visits/")
    assert resp.status_code == 200
    assert any(v["date"] == "2024-01-01" for v in resp.get_json())
