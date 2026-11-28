import importlib

is_armstrong = importlib.import_module("codes.29_armstrong_number").is_armstrong


def test_153():
    assert is_armstrong(153) == True


def test_370():
    assert is_armstrong(370) == True


def test_9474():
    assert is_armstrong(9474) == True


def test_non_armstrong():
    assert is_armstrong(123) == False


def test_zero():
    assert is_armstrong(0) == True


def test_negative_number():
    assert is_armstrong(-153) == False