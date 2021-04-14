from sudoku import Sudoku


VALID_TASK = [
    [2, 4, 7, None, 9, 1, None, 6, 8],
    [1, None, 5, 7, 6, None, 3, None, None],
    [8, 6, None, 4, None, None, None, None, 7],
    [9, None, None, 2, None, 6, None, None, None],
    [None, None, None, 9, 4, 7, 6, 8, None],
    [6, None, 4, None, 5, None, None, 1, 9],
    [7, None, None, None, 3, None, 9, 2, None],
    [4, None, 9, 6, None, None, None, None, None],
    [None, None, None, None, None, None, 4, None, 3]
]

TEST_SOLUTION = [
    [2, 4, 7, 3, 9, 1, 5, 6, 8],
    [1, 9, 5, 7, 6, 8, 3, 4, 2],
    [8, 6, 3, 4, 2, 5, 1, 9, 7],
    [9, 5, 8, 2, 1, 6, 7, 3, 4],
    [3, 1, 2, 9, 4, 7, 6, 8, 5],
    [6, 7, 4, 8, 5, 3, 2, 1, 9],
    [7, 8, 1, 5, 3, 4, 9, 2, 6],
    [4, 3, 9, 6, 7, 2, 8, 5, 1],
    [5, 2, 6, 1, 8, 9, 4, 7, 3]
]


def test_sudoku_solver_valid_task():
    s = Sudoku(VALID_TASK)
    s.solve()
    assert s.get_grid() == TEST_SOLUTION
