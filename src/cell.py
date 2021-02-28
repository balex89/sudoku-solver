from collections.abc import Iterable


class Cell:

    def __init__(self, init_value=None):                                                        # инициализация объекта класса
        self.__value = init_value
        self.__alternatives = set() if init_value is not None else {1, 2, 3, 4, 5, 6, 7, 8, 9}    # если init_value число, то множество альтернатив пустое, клетка решена

    def __eq__(self, other):                                                      # сравнение объектов класса
        return self.__value == other.__value

    @property
    def is_solved(self):
        return self.__value is not None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value in self.__alternatives:                                       # если аргумент есть в cписке возможных вариантов
            self.exclude(self.__alternatives.difference({new_value}))              # исключаем из списка возможных вариантов все, кроме нового значения
        else:
            raise ValueError('Incorrect value')

    def exclude(self, exclude_digitals):                                # исключение цифр из аргумента из множества альтернатив
        if len(self.__alternatives) > 0:                                # что-то делаем, если множество альтернатив не пустое
            if isinstance(exclude_digitals, Iterable):                  # формируем множество для исключения (exclude_set) в зависимоти от аргумента (Iterable или нет)
                exclude_set = set()
                for item in exclude_digitals:
                    if isinstance(item, Cell):
                        exclude_set.add(item.value)
                    else:
                        exclude_set.add(int(item))
            elif isinstance(exclude_digitals, int):
                exclude_set = {exclude_digitals}
            elif isinstance(exclude_digitals, Cell):
                exclude_set = {exclude_digitals.value}
            else:
                raise ValueError('Incorrect value')

            result_alternatives = self.__alternatives.difference(exclude_set)                # result_alternatives - разность текущего множества альтернатив и множетсва для исключения

            if len(result_alternatives) == 0:                                                # если множество альтернатив опустошается до решения:
                raise Exception('Empty alternatives before solution')                        # вызов исключения
            else:
                self.__alternatives = result_alternatives                                 # если нет, то исключаем из множества альтернатив exclude_set

            if len(self.__alternatives) == 1:
                self.__value = self.__alternatives.pop()      # если после исключения осталась единственная альтернатива - присваиваем оставшееся возможное значение __value , и очищаем множество альтернатив
