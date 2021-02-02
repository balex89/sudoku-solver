EMPTY_CELL_CHAR = " "                                        #символ пустой клетки
VALID_NUMBERS = ("1", "2", "3", "4", "5", "6", "7", "8", "9")  # кортеж допустимых символов, кроме символа пустой клетки
VALID_CHARS = (*VALID_NUMBERS,EMPTY_CELL_CHAR)
_decode_cell_char = lambda c: int(c) if c != EMPTY_CELL_CHAR else None  #функция возвращает валидный символ, либо цифру либо None

def read_grid_from_file(file_path):
    
    with open(file_path, "r", encoding="utf8") as f:                          # открываем файл
        text_all = f.readlines()                                               # считываем все строки в список
    grid_final = []                                                            # итоговый список
    for row in text_all:                                                       # перебор всех считанных строк
        grid_row = [_decode_cell_char(char) for char in row if char in VALID_CHARS ]  # если допустимый символ, добавляем его в список
        if len(grid_row) == 9:                                                 # если в списке ровно 9 символов
            grid_final.append(grid_row)                                        # добавляем список в итоговый список
    
    if len(grid_final) == 9:                                                   #если в итоговом списке 9 строк
        return grid_final                                                      #возвращаем список
    else:
        raise ValueError("Invalid input file: expected 9 rows of 9 cells") #поднимаем ошибку


def write_grid_to_file(grid, file_path):
    pass  # TODO: implement
