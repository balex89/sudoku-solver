import logging.handlers
import pathlib
import itertools

from type_aliases import CellValue, Grid, Path

EMPTY_CELL_CHAR = " "                                        #символ пустой клетки
VALID_NUMBERS = ("1", "2", "3", "4", "5", "6", "7", "8", "9")  # кортеж допустимых символов, кроме символа пустой клетки
VALID_CHARS = (*VALID_NUMBERS,EMPTY_CELL_CHAR)

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

_decode_cell_char = lambda c: int(c) if c != EMPTY_CELL_CHAR else None  #функция возвращает валидный символ, либо цифру либо None


def to_valid_char(value: CellValue) -> str:            # функция приводит значения в списке grid к символам
    if value is None:                                         # если значение None, то возвращает пробел
        return EMPTY_CELL_CHAR
    else:                                                     # в противном случае возвращает символ значения (числа)
        return str(value)


def read_grid_from_file(file_path: Path) -> Grid:

    with open(file_path, "r", encoding="utf8") as f:                          # открываем файл
        text_all = f.readlines()                                               # считываем все строки в список
    grid_final = []                                                            # итоговый список
    for row in text_all:                                                       # перебор всех считанных строк
        grid_row = [_decode_cell_char(char) for char in row if char in VALID_CHARS ]  # если допустимый символ, добавляем его в список
        if len(grid_row) == 9:                                                 # если в списке ровно 9 символов
            grid_final.append(grid_row)                                        # добавляем список в итоговый список

    if len(grid_final) == 9:                                                   #если в итоговом списке 9 строк
        return grid_final                                                      #возвращаем список
    else:
        raise ValueError("Invalid input file: expected 9 rows of 9 cells") #поднимаем ошибку


def write_grid_to_file(grid: Grid, file_path: Path) -> None:       # функция записи результата решения Судоку в файл
    with open(file_path, "w", encoding="utf8") as f:          # открываем файл на запись
        for line in grid:                                     # перебираем списки списка grid
            converted_line = [to_valid_char(value) for value in line]  # создаем список с символами
            line = ''.join(converted_line)                    # преобразуем полученный список в строку
            f.write(line + '\n')                              # записывам полученную строку в файл


def is_valid_grid(grid: Grid) -> bool:                        # проверка что сетка 9 на 9
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
        fillers = (">" if k == i*9 + j else " " for k in range(81))
    values = (v if v is not None else " " for v in itertools.chain(*grid))
    return GRID_PATTERN.format(*itertools.chain(*zip(fillers, values)))
