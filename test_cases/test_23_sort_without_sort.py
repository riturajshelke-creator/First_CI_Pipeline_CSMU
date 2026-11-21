import importlib

bubble_sort = importlib.import_module("codes.23_sort_without_sort").bubble_sort


def test_normal_sort():
    assert bubble_sort([5, 2, 9, 1]) == [1, 2, 5, 9]


def test_already_sorted():
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_reverse_sorted():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_empty_list():
    assert bubble_sort([]) == []


def test_single_element():
    assert bubble_sort([7]) == [7]


def test_original_list_unchanged():
    numbers = [3, 1, 2]
    bubble_sort(numbers)
    assert numbers == [3, 1, 2]