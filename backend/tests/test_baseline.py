from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_list_users():
    resp = client.get("/users")
    assert resp.status_code == 200
    assert len(resp.json()) == 3


def test_list_orders():
    resp = client.get("/orders")
    assert resp.status_code == 200
    assert len(resp.json()) == 4


def test_get_order_not_found():
    resp = client.get("/orders/999")
    assert resp.status_code == 404


def test_orders_for_user():
    resp = client.get("/orders/by-user/1")
    assert resp.status_code == 200
    assert len(resp.json()) == 2
