import pathlib

import pytest

from utils import read_grid_from_file, write_grid_to_file

VALID_FILE_CONTENT = ("*************\n"
                      "*123*456*789*\n"
                      "*   *456*789*\n"
                      "*123*456*   *\n"
                      "*************\n"
                      "*123*   *789*\n"
                      "*   *   *   *\n"
                      "*1 4*56 * 9 *\n"
                      "*************\n"
                      " 22*456*78 **\n"
                      "*1  *   *  9*\n"
                      "*123*456*789*\n"
                      "*************\n")

INVALID_FILE_CONTENT = ("*************\n"
                        "*123*456*789*\n"
                        "*   *456*78**\n"  # << not enough digits
                        "*123*456*   *\n"
                        "*************\n"
                        "*123*   *789*\n"
                        "*   *   *   *\n"
                        "*1 4*56 * 9 *\n"
                        "*************\n"
                        " 22*456*78 **\n"
                        "*1  *   *  9*\n"
                        "*123*456*789*\n"
                        "*************\n")

_ = None
TEST_GRID = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [_, _, _, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, _, _, _],
    [1, 2, 3, _, _, _, 7, 8, 9],
    [_, _, _, _, _, _, _, _, _],
    [1, _, 4, 5, 6, _, _, 9, _],
    [_, 2, 2, 4, 5, 6, 7, 8, _],
    [1, _, _, _, _, _, _, _, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
]

OUTPUT_CONTENT = ("123456789\n"
                  "   456789\n"
                  "123456   \n"
                  "123   789\n"
                  "         \n"
                  "1 456  9 \n"
                  " 2245678 \n"
                  "1       9\n"
                  "123456789\n")


def test_read_grid_from_file(tmp_path: pathlib.Path):
    file_path = tmp_path / "test_sudoku.txt"
    file_path.write_text(data=VALID_FILE_CONTENT, encoding="utf8")
    grid = read_grid_from_file(file_path)

    assert grid == TEST_GRID


def test_read_invalid_grid_from_file(tmp_path: pathlib.Path):
    file_path = tmp_path / "test_sudoku.txt"
    file_path.write_text(data=INVALID_FILE_CONTENT, encoding="utf8")

    with pytest.raises(ValueError):
        read_grid_from_file(file_path)


def test_write_grid_to_file(tmp_path: pathlib.Path):
    file_path = tmp_path / "test_sudoku.txt"
    write_grid_to_file(TEST_GRID, file_path)
    file_content = file_path.read_text(encoding="utf8")

    assert file_content == OUTPUT_CONTENT
