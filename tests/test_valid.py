from fastapi.testclient import TestClient


def test_stock_prices(client: TestClient):
    response = client.get("/prices/msft")
    data = response.json()
    assert response.status_code == 200


def test_read_root(client: TestClient):
    response = client.get("/prices/msft/5d")
    data = response.json()
    assert response.status_code == 200


def test_volumes_and_averages(client: TestClient):
    response = client.get("/volumes/msft/5d")
    data = response.json()
    assert response.status_code == 200

def test_create_requests(client: TestClient):
    response = client.post("/requests", json={
        "stock": "msft"
    })
    data = response.json()
    assert response.status_code == 200
    assert data["stock"] == "msft"


def test_read_request_on_time(client: TestClient):
    response = client.get("/check_db_full")
    data = response.json()
    assert response.status_code == 200
    

def test_read_request(client: TestClient):
    response = client.get("/check_db_full/1111999990")
    data = response.json()
    assert response.status_code == 200