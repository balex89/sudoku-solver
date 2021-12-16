import random

import pytest

from sudoku import Sudoku
from cell import Cell
from resources import (EASY_TASK, EASY_SOLUTION, HARD_TASK, HARD_SOLUTION,
                       HARD_TASK_2, HARD_TASK_SOLUTION_2, HARD_TASK_3,
                       HARD_TASK_SOLUTION_3, BUILD_GRID_SOLUTION, TASK_GRID)


def test_sudoku_solver_easy_task():
    s = Sudoku(EASY_TASK)
    s.solve()
    assert s.get_grid() == EASY_SOLUTION


def test_sudoku_solver_hard_task():
    s = Sudoku(HARD_TASK)
    s.solve()
    assert s.get_grid() == HARD_SOLUTION


def _cell_from_alternatives(alternatives):
    c = Cell()
    c._Cell__alternatives = alternatives
    return c


def test_exclude_equal_alternatives():

    _1st_row_alts = [
        {1, 2, 3, 4},
        {1, 2, 3, 4},
        {1, 2, 3, 4},
        {1, 2, 3, 4},
        {1, 2, 3, 4, 5, 6},
        {1, 2, 3, 4, 6, 5},
        {1, 2, 3, 4, 7, 8, 9},
        {1, 2, 3, 4, 8, 9, 7},
        {1, 2, 3, 4, 9, 7, 8}
    ]

    _1st_row_alts_solution = [
        {1, 2, 3, 4},
        {1, 2, 3, 4},
        {1, 2, 3, 4},
        {1, 2, 3, 4},
        {6, 5},
        {6, 5},
        {7, 8, 9},
        {8, 9, 7},
        {9, 7, 8}
    ]

    _2nd_3rd_row_alts_solution = [
        {1, 2, 3, 4, 5, 6, 7, 8, 9},
        {1, 2, 3, 4, 5, 6, 7, 8, 9},
        {1, 2, 3, 4, 5, 6, 7, 8, 9},
        {1, 2, 3, 4, 7, 8, 9},
        {1, 2, 3, 4, 7, 8, 9},
        {1, 2, 3, 4, 7, 8, 9},
        {1, 2, 3, 4, 5, 6},
        {1, 2, 3, 4, 5, 6},
        {1, 2, 3, 4, 5, 6}
    ]

    sud = Sudoku()
    for cell, alts in zip(sud._rows[0], _1st_row_alts):
        cell._alternatives = alts

    sud._exclude_equal_alternatives()

    assert ([cell._alternatives for cell in sud._rows[0]]
            == _1st_row_alts_solution)
    for i in (1, 2):
        assert ([sud._rows[i][j]._alternatives for j in range(9)]
                == _2nd_3rd_row_alts_solution)
    for i in range(3, 9):
        assert ([sud._rows[i][j]._alternatives for j in range(9)]
                == [{1, 2, 3, 4, 5, 6, 7, 8, 9}] * 9)


def test_sudoku_solver_hard_task_2():
    s = Sudoku(HARD_TASK_2)
    s.solve()
    assert s.get_grid() == HARD_TASK_SOLUTION_2


def test_sudoku_solver_hard_task_3():
    s = Sudoku(HARD_TASK_3)
    s.solve()
    assert s.get_grid() == HARD_TASK_SOLUTION_3


def test_leave_equal_alternatives():
    _1st_row_alts = [
        {1, 2},
        {1, 2},
        {3, 4, 5, 7, 9},
        {6, 8},
        {1, 3, 4, 6, 7, 9},
        {2, 3, 4, 7, 8, 9},
        {1, 3},
        {6, 8},
        {3, 8}
    ]

    _1st_row_alts_solution = [
        {1, 2},
        {1, 2},
        {4, 7, 9},
        {6, 8},
        {4, 7, 9},
        {4, 7, 9},
        {1, 3},
        {6, 8},
        {3, 8}
    ]

    sud = Sudoku()
    for cell, alts in zip(sud._rows[0], _1st_row_alts):
        cell._alternatives = alts

    sud._leave_equal_alternatives()

    assert ([cell._alternatives for cell in sud._rows[0]]
            == _1st_row_alts_solution)
    for i in range(1, 9):
        assert ([sud._rows[i][j]._alternatives for j in range(9)]
                == [{1, 2, 3, 4, 5, 6, 7, 8, 9}] * 9)


def test_sudoku_build_grid():
    random.seed(10)
    sudoku = Sudoku(Sudoku.build_grid())
    assert sudoku.get_grid() == BUILD_GRID_SOLUTION


@pytest.mark.skip(reason="Recursion calls take too much time")
def test_valid_solution():
    _ = None
    grid = [
        [_, 9, _, 4, 3, 7, _, _, _],
        [3, 8, 6, 5, 2, 1, 9, 7, 4],
        [4, 1, 7, 8, 6, 9, 2, 5, 3],
        [_, _, 8, _, 1, 6, _, _, 5],
        [_, 3, 4, 2, 5, 8, 7, _, 6],
        [6, 5, _, _, 9, 4, _, _, _],
        [_, _, _, 6, 4, 5, 1, _, 9],
        [_, 4, _, 1, 7, _, _, _, _],
        [_, 6, _, 9, 8, _, _, _, _],
    ]
    sudoku = Sudoku(grid)
    sudoku.solve()
    assert sudoku._is_valid() is True


def test_sudoku_get_task():
    random.seed(10)
    assert Sudoku.get_task(-1) == TASK_GRID
