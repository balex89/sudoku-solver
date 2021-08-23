from collections.abc import Iterable
from typing import Union

from type_aliases import CellValue


class CellStateException(Exception):
    pass


class Cell:
    VALID_VALUES = frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, None})

    def __init__(self, init_value: CellValue = None, callback=None) -> None:
        if init_value in self.VALID_VALUES:
            self.callback = callback
            self.__value = init_value
            self.__alternatives: set[CellValue] = (set() if init_value is not None
                                                   else {1, 2, 3, 4, 5, 6, 7, 8, 9})
        else:
            raise ValueError('Incorrect value')

    def __eq__(self, other):
        return self.__value == other.__value

    @property
    def is_solved(self) -> bool:
        return self.__value is not None

    @property
    def value(self) -> CellValue:
        return self.__value

    @property
    def alternatives(self) -> frozenset:
        return frozenset(self.__alternatives)

    @value.setter
    def value(self, new_value):
        if new_value in self.__alternatives:
            self.exclude(self.__alternatives.difference({new_value}))
        else:
            raise ValueError('Incorrect value')

    def exclude(self, exclude_digitals: Union['Cell', CellValue,
                                              Iterable[Union['Cell', CellValue]]]) -> None:
        if len(self.__alternatives) > 0:
            if isinstance(exclude_digitals, Iterable):
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

            result_alternatives = self.__alternatives.difference(exclude_set)

            if len(result_alternatives) == 0:
                raise CellStateException('Empty alternatives before solution')
            else:
                len_current_alternatives = len(self.__alternatives)
                self.__alternatives = result_alternatives
                if len_current_alternatives != len(self.__alternatives):
                    if self.callback is not None:
                        self.callback

            if len(self.__alternatives) == 1:
                self.__value = self.__alternatives.pop()
