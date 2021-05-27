from flask import request, jsonify

from app.main import app
from sudoku import Sudoku


@app.route("/health")
def health():
    return "OK"


@app.route("/solve", methods=["POST"])
def solve():

    grid = request.json.get("grid", [])

    sudoku = Sudoku(grid)
    sudoku.solve()
    solution = sudoku.get_grid()

    return jsonify(status="ok", grid=solution)


@app.errorhandler(400)
def handle_bad_request(e):
    return jsonify(status="error", error=str(e)), 400


@app.errorhandler(Exception)
def handle_internal_error(e):
    return jsonify(status="error", error=str(e)), 500
