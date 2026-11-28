import importlib

find_max_min = importlib.import_module("codes.25_max_min_list").find_max_min

def test_normal_list():
    assert find_max_min([4, 9, 1, 7]) == (9, 1)

def test_negative_numbers():
    assert find_max_min([-5, -2, -9]) == (-2, -9)


def test_single_element():
    assert find_max_min([10]) == (10, 10)


def test_duplicates():
    assert find_max_min([5, 5, 5]) == (5, 5)


def test_empty_list():
    try:
        find_max_min([])
    except ValueError:
        assert True
    else:
        assert False