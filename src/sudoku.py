from cell import Cell
from types import Grid


class Sudoku:

    def __init__(self, grid: Grid) -> None:
        self.__rows = [[Cell(item) for item in row] for row in grid]

    def solve(self):
        pass  # TODO: implement

    def get_grid(self) -> Grid:
        return [[cell.value for cell in row] for row in self.__rows]
