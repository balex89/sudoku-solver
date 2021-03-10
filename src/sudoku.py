from cell import Cell


class Sudoku:

    def __init__(self, grid):
        self.__rows = [[Cell(item) for item in row] for row in grid]

    def solve(self):
        pass  # TODO: implement

    def get_grid(self):
        return [[cell.value for cell in row] for row in self.__rows]
