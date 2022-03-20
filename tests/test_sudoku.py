import random

import pytest

from sudoku import InvalidSudokuException, Sudoku
from cell import Cell
from resources import (EASY_TASK, EASY_SOLUTION, HARD_TASK, HARD_SOLUTION,
                       HARD_TASK_2, HARD_TASK_SOLUTION_2, HARD_TASK_3,
                       HARD_TASK_SOLUTION_3, BUILD_GRID_SOLUTION, TASK_GRID)
_ = None


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

    assert [cell._alternatives for cell in sud._rows[0]] == _1st_row_alts_solution
    for i in (1, 2):
        assert [sud._rows[i][j]._alternatives for j in range(9)] == _2nd_3rd_row_alts_solution
    for i in range(3, 9):
        assert (
            [sud._rows[i][j]._alternatives for j in range(9)] == [{1, 2, 3, 4, 5, 6, 7, 8, 9}] * 9
        )


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

    assert ([cell._alternatives for cell in sud._rows[0]] == _1st_row_alts_solution)
    for i in range(1, 9):
        assert (
            [sud._rows[i][j]._alternatives for j in range(9)] == [{1, 2, 3, 4, 5, 6, 7, 8, 9}] * 9
        )


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


def test_sudoku_get_task_definite_difficulty():
    random.seed(10)
    sudoku = Sudoku(Sudoku.get_task(-1, 3, 5))
    sudoku.solve()
    assert (sudoku._counter[sudoku._leave_equal_alternatives].solved
            + sudoku._counter[sudoku._exclude_equal_alternatives].solved) == 4


def test_fix_error_empty_alternatives_before_solution():
    task_grid = [
        [None, 2, None, None, None, None, None, 1, None],
        [8, 6, 7, 1, None, None, None, None, 2],
        [4, None, None, None, None, None, None, None, None],
        [9, 3, None, None, 4, None, None, None, None],
        [None, None, None, None, None, 8, None, None, 3],
        [7, None, 8, 5, 9, None, 2, None, 4],
        [None, None, None, 9, None, 4, None, 8, 5],
        [None, None, 6, None, None, None, 1, None, None],
        [None, None, None, None, 5, None, None, None, None]
    ]
    solution = [
        [3, 2, 5, 4, 6, 9, 7, 1, 8],
        [8, 6, 7, 1, 3, 5, 4, 9, 2],
        [4, 9, 1, 8, 7, 2, 5, 3, 6],
        [9, 3, 2, 7, 4, 6, 8, 5, 1],
        [6, 5, 4, 2, 1, 8, 9, 7, 3],
        [7, 1, 8, 5, 9, 3, 2, 6, 4],
        [1, 7, 3, 9, 2, 4, 6, 8, 5],
        [5, 4, 6, 3, 8, 7, 1, 2, 9],
        [2, 8, 9, 6, 5, 1, 3, 4, 7]
    ]

    sudoku = Sudoku(task_grid)
    sudoku.solve()
    assert sudoku.get_grid() == solution


def test_non_valid_task():
    task_grid = [
        [_, _, _, 4, 3, _, 9, 5, 6],
        [_, _, _, 6, 9, 7, 8, _, _],
        [_, _, _, _, _, _, _, _, _],
        [2, _, _, _, 5, _, _, _, _],
        [5, _, _, 7, _, _, _, 4, 2],
        [_, 1, _, _, _, _, _, 7, _],
        [_, _, 8, 3, _, _, _, 2, _],
        [4, _, 2, _, 7, 8, 3, _, 9],
        [_, _, _, _, 4, 2, _, _, _],
    ]

    sudoku = Sudoku(task_grid)
    with pytest.raises(InvalidSudokuException):
        sudoku.solve()
