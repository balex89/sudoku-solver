import json
import random

from resources import EASY_TASK, EASY_SOLUTION, TASK_GRID, INVALID_TASK


def test_health(client):
    response = client.get("/v1/health")

    assert response.mimetype == "text/html"
    assert response.data.decode(response.charset) == "OK"


def test_solve(client):
    mimetype = "application/json"
    headers = {
        "Content-Type": mimetype,
        "Accept": mimetype
    }
    data = {
        "grid": EASY_TASK
    }
    response = client.post(path="/v1/solve", data=json.dumps(data), headers=headers)

    assert response.status_code == 200
    assert response.mimetype == mimetype
    assert response.json.get("grid") == EASY_SOLUTION


def test_get_task(client):
    random.seed(10)
    mimetype = "application/json"
    response = client.get("/v1/get_task")

    assert response.status_code == 200
    assert response.mimetype == mimetype
    assert response.json.get("grid") == TASK_GRID


def test_solve_with_InvalidSudokuException(client):

    mimetype = "application/json"
    headers = {
        "Content-Type": mimetype,
        "Accept": mimetype
    }
    data = {
        "grid": INVALID_TASK
    }
    response = client.post(path="/v1/solve", data=json.dumps(data), headers=headers)

    assert response.status_code == 400
    assert response.mimetype == mimetype
    assert response.json.get("status") == "error"
    assert response.json.get("error") == "Sudoku has no correct solution"
