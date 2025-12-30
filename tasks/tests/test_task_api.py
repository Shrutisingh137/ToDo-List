import json
import pytest
from django.urls import reverse
from tasks.models import Task

@pytest.mark.django_db
def test_create_task_success(client):
    payload = {
        "title": "Write tests",
        "description": "Add API test cases",
        "status": "pending"
    }

    response = client.post(
        "/api/tasks/create/",
        data=json.dumps(payload),
        content_type="application/json"
    )

    assert response.status_code == 201
    assert Task.objects.count() == 1
    assert Task.objects.first().title == "Write tests"


@pytest.mark.django_db
def test_create_task_without_title(client):
    payload = {"description": "Missing title"}

    response = client.post(
        "/api/tasks/create/",
        data=json.dumps(payload),
        content_type="application/json"
    )

    assert response.status_code == 400
    assert "Title is required" in response.json()["error"]


@pytest.mark.django_db
def test_get_tasks(client):
    Task.objects.create(title="Task 1")
    Task.objects.create(title="Task 2")

    response = client.get("/api/tasks/")

    assert response.status_code == 200
    assert len(response.json()["tasks"]) == 2


@pytest.mark.django_db
def test_update_task(client):
    task = Task.objects.create(title="Old Title")

    payload = {"title": "Updated Title"}

    response = client.put(
        f"/api/tasks/{task.id}/",
        data=json.dumps(payload),
        content_type="application/json"
    )

    task.refresh_from_db()
    assert response.status_code == 200
    assert task.title == "Updated Title"


@pytest.mark.django_db
def test_delete_task(client):
    task = Task.objects.create(title="Delete Me")

    response = client.delete(f"/api/tasks/{task.id}/delete/")

    assert response.status_code == 200
    assert Task.objects.count() == 0
