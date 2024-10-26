"""Implementing some list utility functions."""

__author__ = "730767271"


def only_evens(input_1: list[int]) -> list[int]:
    """Returns a list of integers, containing only the even elements of the input list."""
    index_1: int = 0
    return_list: list[int] = []
    while index_1 < len(input_1):
        if (
            input_1[index_1] % 2 == 0
        ):  # when something is divided by 2 and it returns a remiander of 0, the number is even.
            return_list.append(input_1[index_1])
        index_1 += 1  # don't forget to include this to prevent an infinite loop.
    return return_list


def sub(input_1: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Return a list which is a subset of the given list, between the start index and the end index -1."""
    idx: int = 0  # this should be here so that range funtion can know what idx is.
    return_list: list[int] = []
    if start_idx < 0:
        start_idx = 0
    if end_idx > len(input_1):
        end_idx = len(input_1)
    if len(input_1) == 0:
        return []
    if start_idx >= len(input_1):
        return []
    if end_idx == 0:
        return []
    for idx in range(start_idx, end_idx):
        return_list.append(
            input_1[idx]
        )  # adding the elements between the specified indexes to the the a new list that will be returned.
    return return_list


def add_at_index(input_list: list[int], int_element: int, input_index: int) -> None:
    if (input_index < 0) or (
        input_index > len(input_list)
    ):  # cannot be len(input_list) - 1 b/c this would mean that if a list had a length of 1, the index error would be raised.Rather, we want a list with a length of 1 to still be extended with the new input_element.
        raise IndexError("Index is out of bounds for the input list")
    input_list.append(
        3
    )  # doesn't matter what number to chose because it will get replaced when all values shift to the right in the next step.
    for idx in range(
        len(input_list) - 1, input_index, -1
    ):  # starting at the end of list, going until the input_index to iterate one element at a time but bakcwards by decreasing the incrementation value by 1. This loop is shifting all the elements to the right. Since the right most value was declared to be a randomly chosen value, we have empty space that can be filled at the end.
        input_list[idx] = input_list[idx - 1]
    input_list[input_index] = (
        int_element  # this allows us to achieve the final goal of inserting a new element at the wanted index value. In the end, none of the elements from the original list are lost as we created extra space, and shifted everything to the right before inserting the new element at the desired index.
    )
