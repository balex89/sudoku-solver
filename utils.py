EMPTY_CELL_CHAR = " "


def to_valid_char(value):
    if value==None
        return EMPTY_CELL_CHAR
    else
        return str(value)


def read_grid_from_file(file_path):
    pass  # TODO: implement


def write_grid_to_file(grid, file_path):

    with open(file_path, "w", encoding="utf8") as f:  # открываем файл
        for sp in grid:
            itog_sp = [to_valid_char(value) for value in sp]
            line='|',join(itog_sp)
            f.write(line + '\n')
            f.write("---------" + '\n')

