import logging.handlers
import pathlib
import itertools

from type_aliases import CellValue, Grid, Path

EMPTY_CELL_CHAR = " "
VALID_NUMBERS = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
VALID_CHARS = (*VALID_NUMBERS, EMPTY_CELL_CHAR)

GRID_PATTERN = """
╔═══════╤═══════╤═══════╗
║{}{}{}{}{}{} │{}{}{}{}{}{} │{}{}{}{}{}{} ║
║{}{}{}{}{}{} │{}{}{}{}{}{} │{}{}{}{}{}{} ║
║{}{}{}{}{}{} │{}{}{}{}{}{} │{}{}{}{}{}{} ║
╟───────┼───────┼───────╢
║{}{}{}{}{}{} │{}{}{}{}{}{} │{}{}{}{}{}{} ║
║{}{}{}{}{}{} │{}{}{}{}{}{} │{}{}{}{}{}{} ║
║{}{}{}{}{}{} │{}{}{}{}{}{} │{}{}{}{}{}{} ║
╟───────┼───────┼───────╢
║{}{}{}{}{}{} │{}{}{}{}{}{} │{}{}{}{}{}{} ║
║{}{}{}{}{}{} │{}{}{}{}{}{} │{}{}{}{}{}{} ║
║{}{}{}{}{}{} │{}{}{}{}{}{} │{}{}{}{}{}{} ║
╚═══════╧═══════╧═══════╝"""


def _decode_cell_char(c):
    return int(c) if c != EMPTY_CELL_CHAR else None


def to_valid_char(value: CellValue) -> str:
    if value is None:
        return EMPTY_CELL_CHAR
    else:
        return str(value)


def read_grid_from_file(file_path: Path) -> Grid:

    with open(file_path, "r", encoding="utf8") as f:
        text_all = f.readlines()
    grid_final = []
    for row in text_all:
        grid_row = [_decode_cell_char(char) for char in row if char in VALID_CHARS]
        if len(grid_row) == 9:
            grid_final.append(grid_row)

    if len(grid_final) == 9:
        return grid_final
    else:
        raise ValueError("Invalid input file: expected 9 rows of 9 cells")


def write_grid_to_file(grid: Grid, file_path: Path) -> None:
    with open(file_path, "w", encoding="utf8") as f:
        for line in grid:
            converted_line = [to_valid_char(value) for value in line]
            line = ''.join(converted_line)
            f.write(line + '\n')


def is_valid_grid(grid: Grid) -> bool:
    return len(grid) == 9 and all(len(item) == 9 for item in grid)


class MakeDirRotatingFileHandler(logging.handlers.RotatingFileHandler):
    """
    Log Handler similar to built-in RotatingFileHandler but ensures logs folder exists.
    """
    def __init__(self, filename, mode='a', maxBytes=0,
                 backupCount=0, encoding=None, delay=False, errors=None):
        pathlib.Path(filename).parent.mkdir(exist_ok=True)
        super().__init__(filename, mode, maxBytes, backupCount, encoding, delay, errors)


def draw_grid(grid: Grid, i: CellValue = None, j: CellValue = None):
    """
    Converts sudoku grid to a beautified human-readable multiline string.
    Adds visual pointer to cell in row i column j if i, j specified.
    """
    if i is None or j is None:
        fillers = (" " for _ in range(81))
    else:
        fillers = (">" if k == i * 9 + j else " " for k in range(81))
    values = (v if v is not None else " " for v in itertools.chain(*grid))
    return GRID_PATTERN.format(*itertools.chain(*zip(fillers, values)))


def wrap_in_method(wrapper_method):
    def wrapper(func):
        def method(self):
            return wrapper_method(self, func)
        return method
    return wrapper
