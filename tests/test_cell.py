import pytest

from cell import Cell


def _as_digit(digit: int):
    return digit


@pytest.mark.xfail(reason="No check for value in Cell constructor")
def test_init_with_invalid_value():

    with pytest.raises(Exception):
        Cell(10)


@pytest.mark.parametrize("repr_fun", [_as_digit, Cell])
def test_exclude_and_solve(repr_fun):

    cell = Cell()
    cell.exclude([repr_fun(i) for i in range(1, 8)])  # 1, ..., 7

    assert cell.value is None
    assert cell.is_solved is False

    cell.exclude(repr_fun(8))

    assert cell.value == 9
    assert cell.is_solved is True


def test_set_unexpected_value():

    cell = Cell()
    cell.exclude(1)

    with pytest.raises(Exception):
        cell.value = 1
