"""Run with: pytest -v"""

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from database import get_session
from main import app


@pytest.fixture
def client():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)

    def get_test_session():
        with Session(engine) as session:
            yield session

    app.dependency_overrides[get_session] = get_test_session
    yield TestClient(app)
    app.dependency_overrides.clear()


def test_health(client):
    assert client.get("/health").json() == {"status": "ok"}


def test_create_and_read_task(client):
    response = client.post(
        "/tasks",
        json={"title": "Learn FastAPI", "priority": 5}
    )
    assert response.status_code == 201
    task = response.json()
    assert task["id"] == 1
    assert task["done"] is False

    response = client.get(f"/tasks/{task['id']}")
    assert response.json()["title"] == "Learn FastAPI"


def test_validation_errors_return_422(client):
    assert client.post("/tasks", json={"title": "ab"}).status_code == 422
    assert client.post(
        "/tasks",
        json={"title": "Valid", "priority": 9}
    ).status_code == 422


def test_partial_update(client):
    task_id = client.post(
        "/tasks",
        json={"title": "Write README"}
    ).json()["id"]

    response = client.patch(
        f"/tasks/{task_id}",
        json={"done": True}
    )
    assert response.json()["done"] is True
    assert response.json()["title"] == "Write README"


def test_delete_then_404(client):
    task_id = client.post(
        "/tasks",
        json={"title": "Temporary task"}
    ).json()["id"]

    assert client.delete(f"/tasks/{task_id}").status_code == 204
    assert client.get(f"/tasks/{task_id}").status_code == 404