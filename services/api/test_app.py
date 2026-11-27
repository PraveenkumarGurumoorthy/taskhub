import app as taskhub


def setup_function():
    taskhub.tasks.clear()


def test_health():
    client = taskhub.app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_title_is_required():
    client = taskhub.app.test_client()
    response = client.post("/tasks", json={})
    assert response.status_code == 400


def test_add_task():
    client = taskhub.app.test_client()
    response = client.post("/tasks", json={"title": "Learn pytest"})
    assert response.status_code == 201
    assert response.get_json()["title"] == "Learn pytest"


def test_list_tasks():
    client = taskhub.app.test_client()
    client.post("/tasks", json={"title": "Learn pytest"})
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.get_json()) == 1
