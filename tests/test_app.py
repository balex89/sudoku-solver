import json

from resources import EASY_TASK, EASY_SOLUTION


def test_health(client):
    response = client.get("/health")

    assert response.content_type == "text/html; charset=utf-8"
    assert response.data.decode("utf-8") == "OK"


def test_solve(client):
    mimetype = "application/json"
    headers = {
        "Content-Type": mimetype,
        "Accept": mimetype
    }
    data = {
        "grid": EASY_TASK
    }
    response = client.post(path='/solve', data=json.dumps(data), headers=headers)

    assert response.status_code == 200
    assert response.mimetype == mimetype
    assert response.json.get("grid") == EASY_SOLUTION
