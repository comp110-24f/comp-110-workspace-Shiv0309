"""Mutating functions."""

__author__ = "730767271"


def manual_append(a: list[int], num: int) -> None:
    """Mutates its input by appending num to end of a."""
    a.append(num)


def double(a: list[int]) -> None:
    """Mutates its input by looping through the list and multiplying every element in a by 2."""
    index: int = 0
    while index < len(a):
        new_value = a[index] * 2
        a[index] = (
            new_value  # changing the current index value to a value that is its double.
        )
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
