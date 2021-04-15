from itertools import product

from cell import Cell


class Sudoku:

    def __init__(self, grid):
        self.__rows = [[Cell(item) for item in row] for row in grid]
        self.__columns = [[self.__rows[j][i] for j in range(9)] for i in range(9)]
        self.__squares = []
        for i, j in product((0, 3, 6), (0, 3, 6)):
            self.__squares.append([self.__rows[x][y] for x in range(i, i+3) for y in range(j, j+3)])

    def exclude_equal_alternatives(self, grid):
        is_any_cell_solved_ = False  #локалная переменная - флаг что хоть одна клетка решена
        for i in range(9):   # формируем  два массива - одинкакове альтернативы и их количество в пачке
            alternatives = []
            count = []
            for j in range(9):
                if not grid[i][j].alternatives in alternatives:
                    alternatives.append(grid[i][j].alternatives)
                    count.append(1)
                else:
                    count[alternatives.index(grid[i][j].alternatives)] += 1
            print("row ", str(i), "alternatives:", alternatives)
            print("row ", str(i), "count:", count)
            exclude_set = set()     # формируем множество для исключения (альтернативы длинной N в количестве N в одной пачке)
            for c in range(len(alternatives)):
                if len(alternatives[c]) == count[c]:
                    exclude_set = alternatives[c]
            print("row ", str(i), "exclude_set:", exclude_set)
            if len(exclude_set) > 0:     #если такое множество найдено, исключаем его из всех остальных клеток пачки
                for e in range(9):
                    if not grid[i][e].is_solved:
                        if grid[i][e].alternatives != exclude_set:
                            grid[i][e].exclude(exclude_set)
                            is_any_cell_solved_ |= grid[i][e].is_solved
                    print("alternatives after excluding :", grid[i][e].alternatives)
        return is_any_cell_solved_

    def solve(self):
        circus = 0
        while True:
            circus += 1
            is_any_cell_solved = False
            for i, j in product(range(9), range(9)):
                if not self.__rows[i][j].is_solved:
                    self.__rows[i][j].exclude(self.__rows[i])
                    self.__rows[i][j].exclude(self.__columns[j])
                    self.__rows[i][j].exclude(self.__get_square(i, j))
                    is_any_cell_solved |= self.__rows[i][j].is_solved
            if not is_any_cell_solved:
                is_any_cell_solved |= self.exclude_equal_alternatives(self.__rows)
                is_any_cell_solved |= self.exclude_equal_alternatives(self.__columns)
                is_any_cell_solved |= self.exclude_equal_alternatives(self.__squares)
            if not is_any_cell_solved:
                print("Кругов:", circus)
                break

    def get_grid(self):
        return [[cell.value for cell in row] for row in self.__rows]

    def __get_square(self, i, j):
        return self.__squares[3*(i//3) + j//3]
