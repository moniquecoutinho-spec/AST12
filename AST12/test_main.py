from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "API funcionando!"}

def test_somar():
    response = client.get("/somar/2/3")
    assert response.status_code == 200
    assert response.json() == {"resultado": 5}

def test_multiplicar():
    response = client.get("/multiplicar/5/3")
    assert response.status_code == 200
    assert response.json() == {"resultado": 15}