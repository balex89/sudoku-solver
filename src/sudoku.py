from cell import Cell


class Sudoku:

    def __init__(self, grid):
        self.__rows = [[Cell(item) for item in row] for row in grid]
        self.__columns = [[self.__rows[j][i] for j in range(9)] for i in range(9)]
        self.__squares = []
        for s in range(9):
            i = (s//3)*3            # i , j  - координаты левого верхнерго угла квадрата
            j = (s-i)*3
            sqr = [self.__rows[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            self.__squares.append(sqr)

    def solve(self):
        pass  # TODO: implement

    def get_grid(self):
        return [[cell.value for cell in row] for row in self.__rows]
