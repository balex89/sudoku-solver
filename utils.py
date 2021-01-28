def read_grid_from_file(file_path):
    f = open(file_path, "r")                         # открываем файл
    text_all = f.readlines()                         # считываем все строки в список
    f.close()                                        # закрываем файл
    valid_chars = ["1", "2", "3", "4", "5", "6", "7", "8", "9", " "]  # список допустимых символов
    m_final = []                                     # итоговый список

    for row in text_all:                             # перебор всех считанных строк
        m_temp = []                                  # в этот список добавляем допустимые символы из текущей строки
        for char in row:                             # пербор символов в текущей строке
            if char in valid_chars:                  # если допустимый символ, добавляем его в список
                if char != " ":
                    m_temp.append(int(char))
                else:
                    m_temp.append(None)
        if len(m_temp) > 0:                          # если список не пустой (в строке есть допустимые символы)
            m_final.append(m_temp)                   # добавляем список в итоговый список
    return m_final


def write_grid_to_file(grid, file_path):
    pass  # TODO: implement
