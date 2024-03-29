_ = None

EASY_TASK = [
    [2, 4, 7, _, 9, 1, _, 6, 8],
    [1, _, 5, 7, 6, _, 3, _, _],
    [8, 6, _, 4, _, _, _, _, 7],
    [9, _, _, 2, _, 6, _, _, _],
    [_, _, _, 9, 4, 7, 6, 8, _],
    [6, _, 4, _, 5, _, _, 1, 9],
    [7, _, _, _, 3, _, 9, 2, _],
    [4, _, 9, 6, _, _, _, _, _],
    [_, _, _, _, _, _, 4, _, 3]
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
    [_, 8, _, _, _, 2, _, 4, _],
    [_, _, _, _, 3, _, 5, _, 1],
    [_, _, 2, _, 7, 9, 8, _, _],
    [2, 7, _, _, _, _, _, _, _],
    [_, _, 4, _, _, _, _, _, _],
    [5, _, _, 3, 4, _, _, _, _],
    [8, _, 3, 7, 5, _, _, _, _],
    [_, 1, 7, _, _, _, _, _, _],
    [9, _, _, 2, 1, _, _, _, 4]
]

INVALID_TASK = [
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

HARD_SOLUTION = [
    [3, 8, 5, 1, 6, 2, 9, 4, 7],
    [7, 6, 9, 4, 3, 8, 5, 2, 1],
    [1, 4, 2, 5, 7, 9, 8, 6, 3],
    [2, 7, 1, 6, 9, 5, 4, 3, 8],
    [6, 3, 4, 8, 2, 7, 1, 9, 5],
    [5, 9, 8, 3, 4, 1, 2, 7, 6],
    [8, 2, 3, 7, 5, 4, 6, 1, 9],
    [4, 1, 7, 9, 8, 6, 3, 5, 2],
    [9, 5, 6, 2, 1, 3, 7, 8, 4]
]

HARD_TASK_2 = [
    [None, 6, None, None, 1, None, None, 8, 2],
    [8, None, 3, None, None, None, 7, 6, 4],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [2, None, None, None, None, 6, None, None, 7],
    [None, 7, 8, None, None, 1, 2, None, None],
    [None, None, 1, None, None, None, None, None, 8],
    [3, 2, None, None, None, None, 9, 7, None],
    [None, None, 9, 2, 4, None, None, None, 1],
]

HARD_TASK_SOLUTION_2 = [
    [9, 6, 7, 4, 1, 3, 5, 8, 2],
    [8, 1, 3, 9, 5, 2, 7, 6, 4],
    [5, 4, 2, 6, 8, 7, 3, 1, 9],
    [1, 9, 6, 7, 2, 4, 8, 5, 3],
    [2, 3, 5, 8, 9, 6, 1, 4, 7],
    [4, 7, 8, 5, 3, 1, 2, 9, 6],
    [6, 5, 1, 3, 7, 9, 4, 2, 8],
    [3, 2, 4, 1, 6, 8, 9, 7, 5],
    [7, 8, 9, 2, 4, 5, 6, 3, 1]
]

HARD_TASK_3 = [
    [8, None, None, None, None, None, None, None, None],
    [None, None, 3, 6, None, None, None, None, None],
    [None, 7, None, None, 9, None, 2, None, None],
    [None, 5, None, None, None, 7, None, None, None],
    [None, None, None, None, 4, 5, 7, None, None],
    [None, None, None, 1, None, None, None, 3, None],
    [None, None, 1, None, None, None, None, 6, 8],
    [None, None, 8, 5, None, None, None, 1, None],
    [None, 9, None, None, None, None, 4, None, None]
]
HARD_TASK_SOLUTION_3 = [
    [8, 1, 2, 7, 5, 3, 6, 4, 9],
    [9, 4, 3, 6, 8, 2, 1, 7, 5],
    [6, 7, 5, 4, 9, 1, 2, 8, 3],
    [1, 5, 4, 2, 3, 7, 8, 9, 6],
    [3, 6, 9, 8, 4, 5, 7, 2, 1],
    [2, 8, 7, 1, 6, 9, 5, 3, 4],
    [5, 2, 1, 9, 7, 4, 3, 6, 8],
    [4, 3, 8, 5, 2, 6, 9, 1, 7],
    [7, 9, 6, 3, 1, 8, 4, 5, 2]
]

BUILD_GRID_SOLUTION = [
    [5, 9, 2, 4, 3, 7, 6, 8, 1],
    [3, 8, 6, 5, 2, 1, 9, 7, 4],
    [4, 1, 7, 8, 6, 9, 2, 5, 3],
    [7, 2, 8, 3, 1, 6, 4, 9, 5],
    [9, 3, 4, 2, 5, 8, 7, 1, 6],
    [6, 5, 1, 7, 9, 4, 8, 3, 2],
    [8, 7, 3, 6, 4, 5, 1, 2, 9],
    [2, 4, 9, 1, 7, 3, 5, 6, 8],
    [1, 6, 5, 9, 8, 2, 3, 4, 7]
]

TASK_GRID = [
    [None, 9, None, 4, None, None, None, None, None],
    [3, None, None, None, None, None, None, 7, None],
    [4, None, None, 8, None, 9, 2, 5, None],
    [None, None, None, None, 1, 6, None, None, 5],
    [None, 3, 4, 2, None, None, None, None, 6],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, 4, 5, 1, None, 9],
    [2, None, None, 1, 7, None, None, None, None],
    [None, 6, None, None, None, None, None, None, None]
]

TASK_GRID_WITH_DIFFICULTY = [
    [None, 7, None, 4, None, 3, None, None, None],
    [6, None, None, 7, None, 5, 3, None, 9],
    [None, None, 9, None, 2, None, 8, None, None],
    [None, None, None, None, None, None, None, None, 5],
    [None, 4, 6, 3, None, None, None, None, None],
    [3, None, 1, None, None, 4, None, None, None],
    [None, None, None, 1, None, None, 9, None, 4],
    [None, None, None, None, None, None, None, None, None],
    [2, 1, None, 5, None, None, None, None, 3]
]
