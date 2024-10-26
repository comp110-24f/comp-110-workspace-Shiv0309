"""Practice wiritng a function that modifies a list."""

__author__ = "730767271"


def find_and_remove_max(input_1: list[int]) -> int:
    """Will find and return the largest number in the input list while also removing all instances of the largest number from the list."""
    if len(input_1) == 0:
        return -1
    else:
        max_value: int = input_1[0]
        a_index: int = 0
        while a_index < len(input_1):
            if input_1[a_index] > max_value:
                max_value = input_1[a_index]
            a_index += 1
        idx2: int = 0
        while idx2 < len(input_1):
            if input_1[idx2] == max_value:
                input_1.pop(idx2)
            else:
                idx2 += 1
        return max_value
