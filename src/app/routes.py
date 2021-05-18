from flask import request, jsonify

from app.main import app
from sudoku import Sudoku


@app.route("/health")
def health():
    return "OK"


@app.errorhandler(400)
def handle_bad_request(e):
    return jsonify(status="error", error=str(e)), 400


@app.route("/solve", methods=["POST"])
def solve():

    grid = request.json.get('grid')
    if grid is None:
        return jsonify(status="error", error="grid param is not provided"), 400
    try:
        sudoku = Sudoku(grid=grid)
        sudoku.solve()
        solution = sudoku.get_grid()
    except Exception as e:
        return jsonify(status="error", error=e.args[0]), 500
    return jsonify({"grid": solution})
