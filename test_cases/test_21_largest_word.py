import importlib

largest_word = importlib.import_module("codes.21_largest_word").largest_word


def test_normal_sentence():
    assert largest_word("I love programming") == "programming"


def test_equal_length_words():
    assert largest_word("Python Java Ruby") == "Python"


def test_punctuation():
    assert largest_word("Hello, beautiful world!") == "beautiful"


def test_empty_sentence():
    assert largest_word("") == ""


def test_single_word():
    assert largest_word("Python") == "Python"


def test_only_punctuation():
    assert largest_word("!!! ...") == ""