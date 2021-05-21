from itertools import product
from collections import Counter

from cell import Cell


class Sudoku:

    def __init__(self, grid):
        if not self.__is_valid_grid(grid):                  # если грид не 9 на 9 - поднимаем ошибку
            raise ValueError('Incorrect grid. Excepted grid 9x9')
        self.__rows = [[Cell(item) for item in row] for row in grid]
        self.__columns = [[self.__rows[j][i] for j in range(9)] for i in range(9)]
        self.__squares = []
        for i, j in product((0, 3, 6), (0, 3, 6)):
            self.__squares.append([self.__rows[x][y] for x in range(i, i+3) for y in range(j, j+3)])

    def __exclude_equal_alternatives(self, grid_view):
        is_any_cell_solved = False  # флаг что хоть одна клетка решена
        for i in range(9):
            twin_alternatives_counter = Counter(grid_view[i][j].alternatives for j in range(9))  # формируем словарь альтернативы в пачке(строка, столбец или квадрант):количество таких альтернатив в пачке 
            for alternatives in twin_alternatives_counter:
                if len(alternatives) == twin_alternatives_counter[alternatives]:  # ищем множество для исключения (альтернативы длинной N в количестве N в одной пачке)
                    for n in range(9):
                        if not grid_view[i][n].is_solved and grid_view[i][n].alternatives != alternatives:
                            grid_view[i][n].exclude(alternatives)
                            is_any_cell_solved |= grid_view[i][n].is_solved
                    break
        return is_any_cell_solved

    def solve(self):
        if not self.__is_valid():                           # если грид не удовлетворяет правилам судоку - поднимаем ошибку
            raise ValueError('Sudoku rules are violated')
        while True:
            is_any_cell_solved = False
            for i, j in product(range(9), range(9)):
                if not self.__rows[i][j].is_solved:
                    self.__rows[i][j].exclude(self.__rows[i])
                    self.__rows[i][j].exclude(self.__columns[j])
                    self.__rows[i][j].exclude(self.__get_square(i, j))
                    is_any_cell_solved |= self.__rows[i][j].is_solved
            if not is_any_cell_solved:
                for grid_view in [self.__rows, self.__columns, self.__squares]:
                    is_any_cell_solved |= self.__exclude_equal_alternatives(grid_view)
            if not is_any_cell_solved:
                break

    def get_grid(self):
        return [[cell.value for cell in row] for row in self.__rows]

    def __get_square(self, i, j):
        return self.__squares[3*(i//3) + j//3]

    @staticmethod
    def __is_valid_cell_sequence(cell_sequence):    # проверка что в "пачке" нет повторяющихся значений
        value_list = [cell.value for cell in cell_sequence if cell.value is not None]
        return len(value_list) == len(set(value_list))

    def __is_valid(self):         # проверка на выполнение правил судоку (нет повторяющихся значений в строках, столбцах, квадрантах)
        for grid_view in (self.__rows, self.__columns, self.__squares):
            for item in grid_view:
                if not self.__is_valid_cell_sequence(item):
                    return False
        return True

    def __is_valid_grid(self, grid):                # проверка что сетка 9 на 9
        return len(grid) == 9 and all(len(item) == 9 for item in grid)
