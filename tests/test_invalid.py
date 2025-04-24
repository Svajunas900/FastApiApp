from fastapi.testclient import TestClient


def test_stock_prices_invalid(client: TestClient):
    response = client.get("/pricasdes/msftad")
    assert response.status_code == 404


def test_read_root_invalid(client: TestClient):
    response = client.get("/priasdces/msftbf/5dads")
    assert response.status_code == 404


def test_volumes_and_averages_invalid(client: TestClient):
    response = client.get("/volumedsfs/msfttrb/5d")
    assert response.status_code == 404


def test_create_requests_invalid(client: TestClient):
    response = client.post("/requestsdfs", json={
        "stock": "msft"
    })
    assert response.status_code == 404


def test_read_request_on_time_invalid(client: TestClient):
    response = client.get("/check_dbfgb_full")
    assert response.status_code == 404


def test_read_request_invalid(client: TestClient):
    response = client.get("/check_dbasd_full/1111999990")
    assert response.status_code == 404
