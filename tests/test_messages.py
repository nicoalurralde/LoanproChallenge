from utils.calculator import Calculator

calc = Calculator(operation_type="add")

divide_zero = "Error: Cannot divide by zero"
unknown_operation = "Error: Unknown operation: "
invalid_argument = "Invalid argument. Must be a numeric value."
not_a_number = "Result: NaN"
supported_operations = "Supported operations: add, subtract, multiply, divide"


def test_positive_zero_division_message():
    assert divide_zero in Calculator(operation_type="divide").operation_raw(number_a="1", number_b="0")


def test_negative_zero_division_message():
    assert divide_zero in Calculator(operation_type="divide").operation_raw(number_a="-1", number_b="0")


def test_unknown_operation_message():
    _operation_type = "test"
    assert (unknown_operation + _operation_type) in Calculator(
        operation_type=_operation_type).operation_raw(number_a="1", number_b="1")


def test_invalid_argument_message():
    assert invalid_argument in Calculator(operation_type="multiply").operation_raw(number_a="a", number_b="b")


def test_not_a_number_message():
    assert not_a_number in Calculator(operation_type="divide").operation_raw(number_a="1e1000", number_b="1e1000")


def test_supported_operations_message():
    assert supported_operations in Calculator(operation_type="divide").operation_no_numbers()
