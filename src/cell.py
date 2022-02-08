from collections.abc import Iterable
from typing import Union

from type_aliases import CellValue


class CellStateException(Exception):
    pass


class ValueOutOfCellAlternativesException(Exception):
    pass


class Cell:
    VALID_VALUES = frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, None})

    def __init__(self, init_value: CellValue = None, callback=lambda: None) -> None:
        if init_value in self.VALID_VALUES:
            self.callback = callback
            self._value = init_value
            self._alternatives: set[CellValue] = (set() if init_value is not None
                                                  else {1, 2, 3, 4, 5, 6, 7, 8, 9})
        else:
            raise ValueError('Incorrect value', init_value)

    def __eq__(self, other: 'Cell'):
        return self._value == other._value

    @property
    def is_solved(self) -> bool:
        return self._value is not None

    @property
    def value(self) -> CellValue:
        return self._value

    @property
    def alternatives(self) -> frozenset:
        return frozenset(self._alternatives)

    @value.setter
    def value(self, new_value):
        if new_value in self._alternatives:
            self.exclude(self._alternatives.difference({new_value}))
        elif new_value is None:
            self.__init__()
        else:
            raise ValueOutOfCellAlternativesException('Incorrect value', new_value)

    def exclude(self, arg_to_exclude: Union['Cell', CellValue,
                                            Iterable[Union['Cell', CellValue]]]) -> None:
        if len(self._alternatives) > 0:
            if isinstance(arg_to_exclude, Iterable):
                exclude_set = set()
                for item in arg_to_exclude:
                    if isinstance(item, Cell):
                        exclude_set.add(item.value)
                    else:
                        exclude_set.add(int(item))
            elif isinstance(arg_to_exclude, int):
                exclude_set = {arg_to_exclude}
            elif isinstance(arg_to_exclude, Cell):
                exclude_set = {arg_to_exclude.value}
            else:
                raise ValueError('Incorrect value')

            result_alternatives = self._alternatives.difference(exclude_set)

            if len(result_alternatives) == 0:
                raise CellStateException('Empty alternatives before solution')
            else:
                self._alternatives = result_alternatives

            if len(self._alternatives) == 1:
                self._value = self._alternatives.pop()
                self.callback()
