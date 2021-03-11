import os
from typing import Union


CellValue = Union[int, None]
Grid = list[list[CellValue]]

#  https://www.python.org/dev/peps/pep-0519/#provide-specific-type-hinting-support
Path = Union[str, bytes, os.PathLike]
