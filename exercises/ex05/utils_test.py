"""Defining unit tests for utility functions."""

__author__ = "730767271"


from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test1_only_evens() -> None:
    """Should return a new list containing only the elements of the input list that were even."""
    input_1: list[int] = [7, 3, 10, 5, 2]
    assert only_evens(input_1) == [10, 2]
    # this is a use case testing what the function should return as it asserts what the specific return value of only_evens should be when called with a specific input.


def test2_only_evens() -> None:
    """Should NOT mutate the input_1 list that is given."""
    input_1: list[int] = [8, 1, 6, 9, 3]
    only_evens(input_1)
    assert input_1 == [8, 1, 6, 9, 3]
    # this is another use case testing how the function should NOT mutate its input as it asserts that when input_1 is called after only_evens, it should still contaim all the values user declared input_1 to contain


def test3_only_evens() -> None:
    """Should return a new empty list if input_1 is an empty list itself."""
    input_1: list[int] = []
    assert only_evens(input_1) == []
    # this is an edge case testing how when the function is given an untypical input value of an empty string, it should return the empty string itself.


def test1_sub() -> None:
    """Should generate a list which is a subset of the input list, between the specified start index and end index -1."""
    input_1: list[int] = [8, 12, 1, 5, 3]
    assert sub(input_1, 2, 4) == [1, 5]
    # this is a use case testing what the function should return as it asserts what specific list of ints to return when the function is called with a typicaly list of ints, start index, and end index.


def test2_sub() -> None:
    """Should NOT mutate the input_1 list that is given."""
    input_1: list[int] = [14, 6, 3, 5, 10]
    sub(input_1, 1, 3)
    assert input_1 == [14, 6, 3, 5, 10]
    # # this is another use case testing how the function should NOT mutate its input as it asserts that when input_1 is called after sub, it should still contaim all the values user declared input_1 to contain.


def test3_sub() -> None:
    """Should demonstrate that if start index is negative and end index is greater than length of list, function should start at beginning of list and end at end of list."""
    input_1: list[int] = [1, 2, 3, 4, 5]
    assert sub(input_1, -5, 8) == [1, 2, 3, 4, 5]
    # this an edge case testing how when the funcion is given untypical start index value of a negative and end index value that is greater than the length of the list, it should start at the beginning of the list and end at the end of the list, essentailly returning the entire list.


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    input_list: list[int] = [1, 2, 3, 5]
    with pytest.raises(IndexError):
        add_at_index(input_list, -1, -1)
    # an IndexError is raised for the case when the add_at_index is given a negative
    # index value.
    # this is an edge case as it tests how the function should raise an IndexEroor when
    # given an untypical index value (negative number).


def test1_add_at_index() -> None:
    """Should return nothing."""
    input_list: list[int] = [1, 2, 3, 5]
    assert add_at_index(input_list, 4, 3) is None
    # this is a use case testing how the function should return nothing when add_at_index is called.


def test2_add_at_index() -> None:
    """Should modify the input list to place the element at the given index"""
    input_list: list[int] = [1, 2, 3, 5]
    add_at_index(input_list, 4, 3)
    assert input_list == [1, 2, 3, 4, 5]
    # this is a use case testing how the function should modify its input list after being called as it asserts that when called with the input list, an element value, and a valid index value, the function should place the given element value at the desired index.
