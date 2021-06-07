from sudoku import Sudoku
from cell import Cell
from resources import EASY_TASK, EASY_SOLUTION, HARD_TASK, HARD_SOLUTION


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

    grid_view = [[_cell_from_alternatives(EEA_1ST_ROW_ALTERNATIVES[i]) if j == 0 else Cell() for i in range(9)] for j in range(9)]
    Sudoku._Sudoku__exclude_equal_alternatives(grid_view)
    assert [cell._Cell__alternatives for cell in grid_view[0]] == EEA_1ST_ROW_ALTERNATIVES_SOLUTION # проверяем альтернативы в первой строке
    assert all([grid_view[i][j]._Cell__alternatives == {1, 2, 3, 4, 5, 6, 7, 8, 9} for j in range(9)] for i in range(1,9)) # проверяем, что альтернативы в других строках не изменлись
