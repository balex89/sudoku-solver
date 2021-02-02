EMPTY_CELL_CHAR = " "                                         # константа "пробел"


def to_valid_char(value):                                     # функция приводит значения в списке grid к символам
    if value == None:                                         # если значение None, то возвращает пробел
        return EMPTY_CELL_CHAR
    else:                                                     # в противном случае возвращает символ значения (числа)
        return str(value)


def read_grid_from_file(file_path):
    pass  # TODO: implement


def write_grid_to_file(grid, file_path):                      # функция записи результата решения Судоку в файл

    with open(file_path, "w", encoding="utf8") as f:          # открываем файл на запись
        for sp in grid:                                       # перебираем списки списка grid
            itog_sp = [to_valid_char(value) for value in sp]  # создаем список с приведенными значениями к символам
            line='|'.join(itog_sp)                            # преобразуем полученный список в строку 
            f.write(line + '\n')                              # записывам полученную строку в файл
            f.write("---------" + '\n')                       # записываем горизонтальную разделительную черту в файл

