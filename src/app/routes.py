import logging

from flask import request, jsonify

from app.main import app
from sudoku import Sudoku
from utils import draw_grid

logger = logging.getLogger(__name__)


def init():
    logger.info("Init app routes")


@app.route("/v1/health")
def health():
    logger.info("Call health. Returning \"OK\"")
    return "OK"


@app.route("/v1/solve", methods=["POST"])
def solve():

    grid = request.json.get("grid", [])
    logger.info("Call sudoku solver with grid: %s", grid)

    logger.info("Initializing sudoku...")
    sudoku = Sudoku(grid)
    logger.info("Sudoku initialized: %s", draw_grid(grid))

    logger.info("Try to solve sudoku")
    sudoku.solve()
    logger.info("Sudoku solved!")
    solution = sudoku.get_grid()
    logger.info("Returning solution for sudoku: %s", draw_grid(solution))
    return jsonify(status="ok", grid=solution)


@app.route("/get_task", methods=["GET"])
def get_task():
    logger.info("Generating task...")
    task = Sudoku.get_task(-1)
    logger.info("Task generated!")
    logger.info("Returning task: %s", draw_grid(task))
    return jsonify(status="ok", grid=task)


@app.errorhandler(400)
def handle_bad_request(e):
    logger.exception("Bad request")
    return jsonify(status="error", error=str(e)), 400


@app.errorhandler(Exception)
def handle_internal_error(e):
    logger.exception("Internal Server Error")
    return jsonify(status="error", error=str(e)), 500
