import sys
import os
import logging

from sudoku import Sudoku
import utils
from type_aliases import Path

logging.basicConfig(
    style='{',
    format='{asctime}.{msecs:03.0f} {name}:{lineno} {levelname} - {message}',
    datefmt='%Y.%m.%d %H:%M:%S',
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)


def solve_file(file_path: Path) -> None:
    logger.info("Solving sudoku from file %s", file_path)
    sud = Sudoku(utils.read_grid_from_file(file_path))
    sud.solve()
    logger.info("Sudoku solved")
    new_file_name = os.path.splitext(file_path)[0]+"-solution"+os.path.splitext(file_path)[1]
    logger.info("Writing solution to %s", new_file_name)
    utils.write_grid_to_file(sud.get_grid(), new_file_name)


if __name__ == "__main__":
    file_path = sys.argv[1]              # путь к файлу с заданием
    solve_file(file_path)
