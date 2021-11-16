import random

import pytest

from sudoku import Sudoku
from cell import Cell
from resources import (EASY_TASK, EASY_SOLUTION, HARD_TASK, HARD_SOLUTION,
                       HARD_TASK_2, HARD_TASK_SOLUTION_2, HARD_TASK_3,
                       HARD_TASK_SOLUTION_3, BUILD_GRID_SOLUTION)


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
    EEA_1ST_ROW_ALTERNATIVES = [
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

    EEA_1ST_ROW_ALTERNATIVES_SOLUTION = [
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

    grid_view = [
        [
            _cell_from_alternatives(EEA_1ST_ROW_ALTERNATIVES[i]) if j == 0 else Cell()
            for i in range(9)
        ]
        for j in range(9)
    ]
    Sudoku._Sudoku__exclude_equal_alternatives(grid_view)
    assert [cell._Cell__alternatives for cell in grid_view[0]] == EEA_1ST_ROW_ALTERNATIVES_SOLUTION
    assert all(
        grid_view[i][j]._Cell__alternatives == {1, 2, 3, 4, 5, 6, 7, 8, 9}
        for j in range(9) for i in range(1, 9)
    )


def test_sudoku_solver_hard_task_2():
    s = Sudoku(HARD_TASK_2)
    s.solve()
    assert s.get_grid() == HARD_TASK_SOLUTION_2


def test_sudoku_solver_hard_task_3():
    s = Sudoku(HARD_TASK_3)
    s.solve()
    assert s.get_grid() == HARD_TASK_SOLUTION_3


def test_LEA():
    LEA_1ST_ROW = [
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

    LEA_1ST_ROW_SOLUTION = [
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

    grid_view = [
        [
            _cell_from_alternatives(LEA_1ST_ROW[i]) if (j == 0) else Cell()
            for i in range(9)
        ]
        for j in range(9)
    ]
    Sudoku._Sudoku__leave_equal_alternatives(grid_view)

    assert [cell._Cell__alternatives for cell in grid_view[0]] == LEA_1ST_ROW_SOLUTION
    assert all(
        grid_view[i][j]._Cell__alternatives == {1, 2, 3, 4, 5, 6, 7, 8, 9}
        for j in range(9) for i in range(1, 9)
    )


def test_sudoku_build_grid():
    random.seed(10)
    sudoku = Sudoku(Sudoku.build_grid())
    assert sudoku.get_grid() == BUILD_GRID_SOLUTION


@pytest.mark.skip(reason="Recursion calls take too much time")
def test_valid_solution():
    _ = None
    grid = [
        [_, 9, _, 4, _, _, _, _, _],
        [3, _, _, _, _, _, _, 7, _],
        [4, _, _, 8, _, 9, 2, 5, _],
        [_, _, 8, _, 1, 6, _, _, 5],
        [_, 3, 4, 2, _, _, _, _, 6],
        [_, _, _, _, _, _, _, _, _],
        [_, _, _, _, 4, 5, 1, _, 9],
        [_, _, _, 1, 7, _, _, _, _],
        [_, 6, _, _, _, _, _, _, _],
    ]
    sudoku = Sudoku(grid)
    sudoku.solve()
    assert sudoku._is_valid() is True
