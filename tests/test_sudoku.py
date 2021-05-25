from sudoku import Sudoku


EASY_TASK = [
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

EASY_SOLUTION = [
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

HARD_TASK = [
    [None, 8, None, None, None, 2, None, 4, None],
    [None, None, None, None, 3, None, 5, None, 1],
    [None, None, 2, None, 7, 9, 8, None, None],
    [2, 7, None, None, None, None, None, None, None],
    [None, None, 4, None, None, None, None, None, None],
    [5, None, None, 3, 4, None, None, None, None],
    [8, None, 3, 7, 5, None, None, None, None],
    [None, 1, 7, None, None, None, None, None, None],
    [9, None, None, 2, 1, None, None, None, 4]
    ]

HARD_SOLUTION = [
    [3, 8, 5, 1, 6, 2, 9, 4, 7],
    [7, 6, 9, 4, 3, 8, 5, 2, 1],
    [1, 4, 2, 5, 7, 9, 8, None, None],
    [2, 7, None, 6, None, None, 4, None, None],
    [6, 3, 4, None, 2, None, 1, None, None],
    [5, 9, None, 3, 4, None, 2, None, None],
    [8, 2, 3, 7, 5, 4, 6, 1, 9],
    [4, 1, 7, None, None, 6, 3, 5, 2],
    [9, 5, 6, 2, 1, 3, 7, 8, 4]
    ]


def test_sudoku_solver_easy_task():
    s = Sudoku(EASY_TASK)
    s.solve()
    assert s.get_grid() == EASY_SOLUTION


def test_sudoku_solver_hard_task():
    s = Sudoku(HARD_TASK)
    s.solve()
    assert s.get_grid() == HARD_SOLUTION
