from itertools import product
from collections import Counter
import random
from typing import Sequence, Callable
import logging

from cell import Cell, CellStateException, ValueOutOfCellAlternativesException
from utils import is_valid_grid, draw_grid, wrap_in_method
from type_aliases import Grid

logger = logging.getLogger(__name__)

EVA_MAX_ALTERNATIVES_NUMBER = 2
MAX_SPECULATION_DEPTH = 4


class InvalidSudokuException(Exception):
    pass


class Sudoku:

    def burn_alternatives(self, i, j):

        for batch in [self._rows[i], self._columns[j], self._get_square(i, j)]:
            for cell in batch:
                if not cell.is_solved:
                    cell.exclude(self._rows[i][j].value)

    def __init__(self, grid: Grid = None, _max_speculation_depth=MAX_SPECULATION_DEPTH) -> None:

        def factory(i, j):
            def callback():
                self.burn_alternatives(i, j)
            return callback

        if grid is None:
            self._rows = [[Cell(None, factory(i, j)) for j in range(9)] for i in range(9)]
        elif not is_valid_grid(grid):
            raise ValueError('Incorrect grid. Expected grid 9x9')
        else:
            self._rows = [[Cell(grid[i][j], factory(i, j)) for j in range(9)] for i in range(9)]
        self._columns = [[self._rows[j][i] for j in range(9)] for i in range(9)]
        self._squares = []
        for i, j in product((0, 3, 6), (0, 3, 6)):
            self._squares.append(
                [self._rows[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            )
        self._speculation_depth = 0
        self._max_speculation_depth = _max_speculation_depth

    def _apply_batch_method(self, batch_func: Callable[[list[Cell]], bool]) -> bool:
        logger.debug("Using %s method...", batch_func.__name__)
        is_any_cell_solved = False
        for grid_view in [self._rows, self._columns, self._squares]:
            for batch in grid_view:
                is_any_cell_solved |= batch_func(batch)
        return is_any_cell_solved

    @wrap_in_method(_apply_batch_method)
    def _leave_equal_alternatives(batch: list[Cell]) -> bool:
        is_any_cell_solved = False
        list_of_alt_sets = [batch[j].alternatives for j in range(9)]
        alternative_to_cell_indexes = {
            m: frozenset(n for n in range(9) if m in list_of_alt_sets[n])
            for m in range(1, 10)
        }
        cell_indexes_counter = Counter(alternative_to_cell_indexes.values())
        for cell_indexes, alt_count in cell_indexes_counter.items():
            if len(cell_indexes) == alt_count:
                common_alts = {
                    k for k in alternative_to_cell_indexes
                    if (alternative_to_cell_indexes[k] == cell_indexes)
                }
                for j in cell_indexes:
                    batch[j].exclude(list_of_alt_sets[j] - common_alts)
                    is_any_cell_solved |= batch[j].is_solved
                break
        return is_any_cell_solved

    @wrap_in_method(_apply_batch_method)
    def _exclude_equal_alternatives(batch: list[Cell]) -> bool:
        is_any_cell_solved = False
        twin_alternatives_counter = Counter(batch[j].alternatives for j in range(9))
        for alternatives in twin_alternatives_counter:
            if len(alternatives) == twin_alternatives_counter[alternatives]:
                cell_indexes = [
                    index for index in range(9)
                    if (not batch[index].is_solved
                        and batch[index].alternatives != alternatives)
                ]
                for index in cell_indexes:
                    batch[index].exclude(alternatives)
                    is_any_cell_solved |= batch[index].is_solved
                break
        return is_any_cell_solved

    def _apply_basic_rules(self):
        logger.debug("Using basic rules...")
        for i, j in product(range(9), range(9)):
            if not self._rows[i][j].is_solved:
                self._rows[i][j].exclude(self._rows[i])
                self._rows[i][j].exclude(self._columns[j])
                self._rows[i][j].exclude(self._get_square(i, j))

    def solve(self) -> None:
        if not self._is_valid():
            raise ValueError('Sudoku rules are violated')

        self._apply_basic_rules()

        while True:
            logger.debug("New iteration. Current sudoku status: %s", draw_grid(self.get_grid()))
            if self._speculation_depth > 0 and not self._is_valid():
                raise InvalidSudokuException()
            for method in (self._leave_equal_alternatives,
                           self._exclude_equal_alternatives,
                           self._exclude_violating_alternative):
                if method():
                    logger.debug("Some new cells are solved")
                    break
            else:
                logger.debug("No cell was solved, stop iteration")
                break

    def get_grid(self) -> Grid:
        return [[cell.value for cell in row] for row in self._rows]

    def _get_square(self, i: int, j: int) -> list[Cell]:
        return self._squares[3 * (i // 3) + j // 3]

    @staticmethod
    def _is_valid_cell_sequence(cell_sequence: Sequence[Cell]) -> bool:
        value_list = [cell.value for cell in cell_sequence if cell.value is not None]
        return len(value_list) == len(set(value_list))

    def _is_valid(self) -> bool:
        for grid_view in (self._rows, self._columns, self._squares):
            for item in grid_view:
                if not self._is_valid_cell_sequence(item):
                    return False
        return True

    @property
    def is_solved(self) -> bool:
        return all(self._rows[i][j].is_solved for i in range(9) for j in range(9))

    def _exclude_violating_alternative(self):
        if self._speculation_depth > self._max_speculation_depth:
            logger.debug("Skipping Exclude Violating Alternatives method...")
            return False
        logger.debug("Using Exclude Violating Alternatives method...")
        for i, j in product(range(9), range(9)):
            if len(self._rows[i][j].alternatives) <= EVA_MAX_ALTERNATIVES_NUMBER:
                alternatives = sorted(self._rows[i][j].alternatives)
                while len(alternatives) > 0:
                    sudoku_copy = Sudoku(self.get_grid(), self._max_speculation_depth)
                    sudoku_copy._speculation_depth += 1
                    sudoku_copy._rows[i][j].value = alternatives.pop()
                    try:
                        sudoku_copy.solve()
                    except (InvalidSudokuException, CellStateException):
                        self._rows[i][j].exclude(sudoku_copy._rows[i][j].value)
                        return True
        return False

    @staticmethod
    def build_grid() -> Grid:
        sudokus = [Sudoku()]
        i = 1
        while i < 10:
            sudokus.append(Sudoku(sudokus[i - 1].get_grid()))
            for row in sudokus[i]._rows:
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
            i: int = index // 9
            j: int = index % 9
            true_cell_value = task[i][j]
            task[i][j] = None
            sudoku = cls(task, speculation_depth)
            sudoku.solve()
            if not sudoku.is_solved:
                task[i][j] = true_cell_value
        return task
