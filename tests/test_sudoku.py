from sudoku import Sudoku
from resources import EASY_TASK, EASY_SOLUTION, HARD_TASK, HARD_SOLUTION


def test_sudoku_solver_easy_task():
    s = Sudoku(EASY_TASK)
    s.solve()
    assert s.get_grid() == EASY_SOLUTION


def test_sudoku_solver_hard_task():
    s = Sudoku(HARD_TASK)
    s.solve()
    assert s.get_grid() == HARD_SOLUTION
