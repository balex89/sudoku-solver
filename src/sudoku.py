from itertools import product
from collections import Counter
import random
from typing import Sequence
import logging

from cell import Cell, CellStateException, ValueOutOfCellAlternativesException
from utils import is_valid_grid, draw_grid
from type_aliases import Grid

logger = logging.getLogger(__name__)

EVA_MAX_ALTERNATIVES_NUMBER = 2
MAX_SPECULATION_DEPTH = 4


class InvalidSudokuException(Exception):
    pass


class Sudoku:

    def burn_alternatives(self, i, j):

        for batch in [self.__rows[i], self.__columns[j], self.__get_square(i, j)]:
            for cell in batch:
                if not cell.is_solved:
                    cell.exclude(self.__rows[i][j].value)

    def __init__(self, grid: Grid = None, _max_speculation_depth=MAX_SPECULATION_DEPTH) -> None:

        def factory(i, j):
            def callback():
                self.burn_alternatives(i, j)
            return callback

        if grid is None:
            self.__rows = [[Cell(None, factory(i, j)) for j in range(9)] for i in range(9)]
        elif not is_valid_grid(grid):
            raise ValueError('Incorrect grid. Expected grid 9x9')
        else:
            self.__rows = [[Cell(grid[i][j], factory(i, j)) for j in range(9)] for i in range(9)]
        self.__columns = [[self.__rows[j][i] for j in range(9)] for i in range(9)]
        self.__squares = []
        for i, j in product((0, 3, 6), (0, 3, 6)):
            self.__squares.append(
                [self.__rows[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            )
        self._speculation_depth = 0
        self._max_speculation_depth = _max_speculation_depth

    @staticmethod
    def __leave_equal_alternatives(grid_view: list[list[Cell]]) -> bool:
        is_any_cell_solved = False
        for batch in grid_view:
            list_of_alt_sets = [batch[j].alternatives for j in range(9)]
            alternative_to_cell_indexes = {m: frozenset(
                n for n in range(9) if m in list_of_alt_sets[n]) for m in range(1, 10)}
            for cell_indexes, alt_count in Counter(alternative_to_cell_indexes.values()).items():
                if len(cell_indexes) == alt_count:
                    common_alts = {k for k in alternative_to_cell_indexes if (
                        alternative_to_cell_indexes[k] == cell_indexes)}
                    for j in cell_indexes:
                        batch[j].exclude(list_of_alt_sets[j] - common_alts)
                        is_any_cell_solved |= batch[j].is_solved
                    break
        return is_any_cell_solved

    @staticmethod
    def __exclude_equal_alternatives(grid_view: list[list[Cell]]) -> bool:
        is_any_cell_solved = False
        for batch in grid_view:
            twin_alternatives_counter = Counter(batch[j].alternatives for j in range(9))
            for alternatives in twin_alternatives_counter:
                if len(alternatives) == twin_alternatives_counter[alternatives]:
                    for index in [
                        index for index in range(9) if
                        not batch[index].is_solved and batch[index].alternatives != alternatives
                    ]:
                        batch[index].exclude(alternatives)
                        is_any_cell_solved |= batch[index].is_solved
                    break
        return is_any_cell_solved

    def solve(self) -> None:
        if not self._is_valid():
            raise ValueError('Sudoku rules are violated')

        logger.debug("Using basic rules...")
        for i, j in product(range(9), range(9)):
            if not self.__rows[i][j].is_solved:
                self.__rows[i][j].exclude(self.__rows[i])
                self.__rows[i][j].exclude(self.__columns[j])
                self.__rows[i][j].exclude(self.__get_square(i, j))

        while True:
            is_any_cell_solved = False
            logger.debug("New iteration. Current sudoku status: %s", draw_grid(self.get_grid()))
            if self._speculation_depth > 0 and not self._is_valid():
                raise InvalidSudokuException()
            logger.debug("Using Leave Equal Alternatives method...")
            for grid_view in [self.__rows, self.__columns, self.__squares]:
                is_any_cell_solved |= self.__leave_equal_alternatives(grid_view)
            if not is_any_cell_solved:
                logger.debug("Using Exclude Equal Alternatives method...")
                for grid_view in [self.__rows, self.__columns, self.__squares]:
                    is_any_cell_solved |= self.__exclude_equal_alternatives(grid_view)
            if not is_any_cell_solved and self._speculation_depth <= self._max_speculation_depth:
                logger.debug("Using Exclude Violating Alternatives method...")
                is_any_cell_solved |= self.__exclude_violating_alternative()
            if not is_any_cell_solved:
                break
            logger.debug("Some new cells are solved")

    def get_grid(self) -> Grid:
        return [[cell.value for cell in row] for row in self.__rows]

    def __get_square(self, i: int, j: int) -> list[Cell]:
        return self.__squares[3 * (i // 3) + j // 3]

    @staticmethod
    def __is_valid_cell_sequence(cell_sequence: Sequence[Cell]) -> bool:
        value_list = [cell.value for cell in cell_sequence if cell.value is not None]
        return len(value_list) == len(set(value_list))

    def _is_valid(self) -> bool:
        for grid_view in (self.__rows, self.__columns, self.__squares):
            for item in grid_view:
                if not self.__is_valid_cell_sequence(item):
                    return False
        return True

    @property
    def is_solved(self) -> bool:
        return all(self.__rows[i][j].is_solved for i in range(9) for j in range(9))

    def __exclude_violating_alternative(self):
        for i, j in product(range(9), range(9)):
            if len(self.__rows[i][j].alternatives) <= EVA_MAX_ALTERNATIVES_NUMBER:
                alternatives = sorted(self.__rows[i][j].alternatives)
                while len(alternatives) > 0:
                    sudoku_copy = Sudoku(self.get_grid(), self._max_speculation_depth)
                    sudoku_copy._speculation_depth += 1
                    sudoku_copy.__rows[i][j].value = alternatives.pop()
                    try:
                        sudoku_copy.solve()
                    except (InvalidSudokuException, CellStateException):
                        self.__rows[i][j].exclude(sudoku_copy.__rows[i][j].value)
                        return True
        return False

    @staticmethod
    def build_grid():
        sudokus = [Sudoku()]
        i = 1
        while i < 10:
            sudokus.append(Sudoku(sudokus[i - 1].get_grid()))
            for row in sudokus[i].__rows:
                cell_indexes = random.sample(range(9), 9)
                for k in cell_indexes:
                    if not row[k].is_solved:
                        try:
                            row[k].value = i
                        except ValueOutOfCellAlternativesException:
                            row[k].value = None
                        else:
                            break
                else:
                    sudokus.pop()
                    sudokus.pop()
                    i -= 2
                    break
            i += 1
        return sudokus[9].get_grid()

    @classmethod
    def get_task(cls, speculation_depth):
        task = cls.build_grid()
        for index in random.sample(range(81), 81):
            i = index // 9
            j = index % 9
            true_cell_value = task[i][j]
            task[i][j] = None
            sudoku = cls(task, speculation_depth)
            sudoku.solve()
            if not sudoku.is_solved:
                task[i][j] = true_cell_value
        return task
