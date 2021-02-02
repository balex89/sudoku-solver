EMPTY_CELL_CHAR = " "                                         # константа "пробел"


def to_valid_char(value):                                     # функция приводит значения в списке grid к символам
    if value is None:                                         # если значение None, то возвращает пробел
        return EMPTY_CELL_CHAR
    else:                                                     # в противном случае возвращает символ значения (числа)
        return str(value)


def read_grid_from_file(file_path):
    pass  # TODO: implement


def write_grid_to_file(grid, file_path):                      # функция записи результата решения Судоку в файл
    with open(file_path, "w", encoding="utf8") as f:          # открываем файл на запись
        for line in grid:                                     # перебираем списки списка grid
            converted_line = [to_valid_char(value) for value in line]  # создаем список с символами
            line = ''.join(converted_line)                    # преобразуем полученный список в строку
            f.write(line + '\n')                              # записывам полученную строку в файл
