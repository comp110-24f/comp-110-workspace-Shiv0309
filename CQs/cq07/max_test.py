"""Practice writing unit tests."""

__author__ = "730767271"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max() -> None:
    input_1: list[int] = [10, 9, 8, 7, 10]
    find_and_remove_max(input_1)
    assert find_and_remove_max(input_1) == 10


def test1_find_and_remove_max() -> None:
    input_1: list[int] = [10, 9, 8, 7, 10]
    find_and_remove_max(input_1)
    assert input_1 == [9, 8, 7]


def test2_find_and_remove_max() -> None:
    input_1: list[int] = []
    find_and_remove_max(input_1)
    assert find_and_remove_max(input_1) == -1
