import importlib

is_anagram = importlib.import_module("codes.22_anagram_strings").is_anagram

def test_normal_anagram():
    assert is_anagram("listen", "silent") == True


def test_uppercase_anagram():
    assert is_anagram("LISTEN", "silent") == True


def test_spaces():
    assert is_anagram("Dormitory", "Dirty room") == True


def test_non_anagram():
    assert is_anagram("hello", "world") == False


def test_empty_strings():
    assert is_anagram("", "") == True


def test_different_lengths():
    assert is_anagram("abc", "abcd") == False