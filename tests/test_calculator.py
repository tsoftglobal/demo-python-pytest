import pytest
from app.calculator import add, divide, multiply, subtract


def test_add_integers():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, 1) == 0


def test_add_floats():
    assert add(1.5, 2.5) == 4.0


def test_add_zero():
    assert add(0, 0) == 0
    assert add(5, 0) == 5


def test_divide():
    assert divide(10, 2) == 5, "PYTHON_CALC_DIVIDE_EXPECTED_5"


def test_divide_floats():
    assert divide(7.5, 2.5) == 3.0


def test_divide_by_one():
    assert divide(10, 1) == 10


def test_multiply():
    assert multiply(3, 4) == 12


def test_multiply_by_zero():
    assert multiply(5, 0) == 0


def test_multiply_negative():
    assert multiply(-2, 3) == -6


def test_subtract():
    assert subtract(5, 3) == 2


def test_subtract_negative():
    assert subtract(1, 2) == -1


def test_subtract_zero():
    assert subtract(5, 0) == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
