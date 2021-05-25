import os
from typing import Union, Literal


CellValue = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, None]
Grid = list[list[CellValue]]

#  https://www.python.org/dev/peps/pep-0519/#provide-specific-type-hinting-support
Path = Union[str, bytes, os.PathLike]
