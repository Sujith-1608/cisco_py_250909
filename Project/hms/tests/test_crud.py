import json

def test_create_patient(client):
    patient = {"id": 1, "name": "John Doe", "age": 45, "disease": "Flu"}
    response = client.post("/patients", data=json.dumps(patient), content_type="application/json")
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "John Doe"
    assert data["disease"] == "Flu"

def test_read_all_patients(client):
    patient = {"id": 2, "name": "Jane Smith", "age": 32, "disease": "Diabetes"}
    client.post("/patients", data=json.dumps(patient), content_type="application/json")

    response = client.get("/patients")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) >= 1

def test_update_patient(client):
    patient = {"id": 3, "name": "Michael Johnson", "age": 29, "disease": "Hypertension"}
    client.post("/patients", data=json.dumps(patient), content_type="application/json")

    updated_patient = {"id": 3, "name": "Michael Johnson", "age": 60, "disease": "Hypertension"}
    response = client.put("/patients/3", data=json.dumps(updated_patient), content_type="application/json")
    assert response.status_code == 200
    data = response.get_json()
    assert data["age"] == 60

def test_delete_patient(client):
    patient = {"id": 4, "name": "Emily Davis", "age": 28, "disease": "Asthama"}
    client.post("/patients", data=json.dumps(patient), content_type="application/json")

    response = client.delete("/patients/4")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Deleted Successfully"
