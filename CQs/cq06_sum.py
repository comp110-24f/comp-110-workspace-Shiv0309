"""Summing the elements of a list using different loops"""

__author__ = "730767271"


def w_sum(vals: list[float]) -> float:
    index: int = 0
    return_value: float = 0.0
    if vals == []:
        return_value = 0.0  # has to be here to ensure that empty list will result in 0.0 as the sum.
    while index < len(vals):
        return_value += vals[index]
        index += 1
    return return_value


def f_sum(vals: list[float]) -> float:
    return_value: float = 0.0
    if vals == []:
        return_value = 0.0
    for a in vals:
        return_value += a  # increasing the return value each time we consider a new value by amount of the new vlaue.
    return return_value


def f_range_sum(vals: list[float]) -> float:
    return_value: float = 0.0
    if vals == []:
        return_value = 0.0
    for idx in range(0, len(vals)):
        return_value += vals[
            idx
        ]  # remeber: we have to add the value at the index, not the index itself
    return return_value
