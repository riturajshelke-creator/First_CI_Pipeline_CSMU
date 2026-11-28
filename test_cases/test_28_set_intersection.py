import importlib

set_intersection = importlib.import_module("codes.28_set_intersection").set_intersection


def test_normal_intersection():
    assert set_intersection({1, 2, 3}, {2, 3, 4}) == {2, 3}


def test_no_intersection():
    assert set_intersection({1, 2}, {3, 4}) == set()


def test_identical_sets():
    assert set_intersection({1, 2, 3}, {1, 2, 3}) == {1, 2, 3}


def test_empty_first_set():
    assert set_intersection(set(), {1, 2}) == set()


def test_empty_second_set():
    assert set_intersection({1, 2}, set()) == set()


def test_single_element_intersection():
    assert set_intersection({5}, {5, 6}) == {5}