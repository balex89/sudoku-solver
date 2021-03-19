from itertools import product

from cell import Cell


class Sudoku:

    def __init__(self, grid):
        self.__rows = [[Cell(item) for item in row] for row in grid]
        self.__columns = [[self.__rows[j][i] for j in range(9)] for i in range(9)]
        self.__squares = []
        for i, j in product((0, 3, 6), (0, 3, 6)):
            self.__squares.append([self.__rows[x][y] for x in range(i, i+3) for y in range(j, j+3)])

    def solve(self):
        pass  # TODO: implement

    def get_grid(self):
        return [[cell.value for cell in row] for row in self.__rows]

    def __get_square(self, i, j):
        return self.__squares[3*(i//3) + j//3]
