import pytest
from utils.calculator import Calculator
from utils.python_calculation import PythonCalculation as PyC
from data.number_list import *
calc = Calculator(operation_type="divide")
zero_replacement = 0.01


# Results are done with Python's calculator to avoid human error with typos
@pytest.mark.parametrize(
    "num_a, num_b",
    list_positive_integer)
def test_positive_integer(num_a, num_b):
    _num_b = num_b
    if num_b == 0:
        _num_b = zero_replacement
    assert calc.operation(number_a=num_a, number_b=_num_b) == PyC.format_float(num_a / _num_b)


@pytest.mark.parametrize(
    "num_a, num_b",
    list_positive_big_integer)
def test_positive_big_integer(num_a, num_b):
    _num_b = num_b
    if num_b == 0:
        _num_b = zero_replacement
    assert calc.operation(number_a=num_a, number_b=_num_b) == PyC.format_float(num_a / _num_b)


@pytest.mark.parametrize(
    "num_a, num_b",
    list_negative_positive_integer)
def test_negative_positive_integer(num_a, num_b):
    _num_b = num_b
    if num_b == 0:
        _num_b = zero_replacement
    assert calc.operation(number_a=num_a, number_b=_num_b) == PyC.format_float(num_a / _num_b)


@pytest.mark.parametrize(
    "num_a, num_b",
    list_negative_negative_integer)
def test_negative_negative_integer(num_a, num_b):
    _num_b = num_b
    if num_b == 0:
        _num_b = zero_replacement
    assert calc.operation(number_a=num_a, number_b=_num_b) == PyC.format_float(num_a / _num_b)


@pytest.mark.parametrize(
    "num_a, num_b",
    list_negative_big_integer)
def test_negative_big_integer(num_a, num_b):
    _num_b = num_b
    if num_b == 0:
        _num_b = zero_replacement
    assert calc.operation(number_a=num_a, number_b=_num_b) == PyC.format_float(num_a / _num_b)


@pytest.mark.parametrize(
    "num_a, num_b",
    list_positive_real_numbers)
def test_positive_real_numbers(num_a, num_b):
    _num_b = num_b
    if num_b == 0:
        _num_b = zero_replacement
    assert calc.operation(number_a=num_a, number_b=_num_b) == PyC.format_float(num_a / _num_b)


@pytest.mark.parametrize(
    "num_a, num_b",
    list_negative_real_numbers)
def test_negative_real_numbers(num_a, num_b):
    _num_b = num_b
    if num_b == 0:
        _num_b = zero_replacement
    assert calc.operation(number_a=num_a, number_b=_num_b) == PyC.format_float(num_a / _num_b)


@pytest.mark.parametrize(
    "num_a, num_b",
    list_zero_positive_real_numbers)
def test_zero_positive_real_numbers(num_a, num_b):
    _num_b = num_b
    if num_b == 0:
        _num_b = zero_replacement
    assert calc.operation(number_a=num_a, number_b=_num_b) == PyC.format_float(num_a / _num_b)


@pytest.mark.parametrize(
    "num_a, num_b",
    list_zero_negative_real_numbers)
def test_zero_negative_real_numbers(num_a, num_b):
    _num_b = num_b
    if num_b == 0:
        _num_b = zero_replacement
    assert calc.operation(number_a=num_a, number_b=_num_b) == PyC.format_float(num_a / _num_b)
