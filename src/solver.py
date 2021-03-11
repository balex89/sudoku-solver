import sys
import os

from sudoku import Sudoku
from utils import *
from types import Path


def solve_file(file_path: Path) -> None:                                                         # чтение задания, решение, запись решения в файл
    sud = Sudoku(read_grid_from_file(file_path))                                                     # чтение задания из файла, создание объекта класа Sudoku
    sud.solve()                                                                                      # решение
    new_file_name = os.path.splitext(file_path)[0]+"-solution"+os.path.splitext(file_path)[1]        # добавляем к имени файла "-solution"
    write_grid_to_file(sud.get_grid(), new_file_name)                                                # запись решения в файл


if __name__ == "__main__":
    file_path = sys.argv[1]              # путь к файлу с заданием
    solve_file(file_path)
