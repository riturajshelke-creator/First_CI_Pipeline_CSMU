import importlib

decimal_to_binary = importlib.import_module("codes.30_decimal_to_binary").decimal_to_binary


def test_normal_number():
    assert decimal_to_binary(10) == "1010"


def test_zero():
    assert decimal_to_binary(0) == "0"


def test_one():
    assert decimal_to_binary(1) == "1"


def test_large_number():
    assert decimal_to_binary(255) == "11111111"


def test_negative_number():
    try:
        decimal_to_binary(-5)
    except ValueError:
        assert True
    else:
        assert False