"""EX04 - Reproducing tried and true abstractions of the past."""

__author__ = "730767271"


def all(a: list[int], num: int) -> bool:
    """Indicates whether or not all the ints in the list are the same as the given num value."""
    if len(a) == 0:
        return False  # added this line as autograder said function should return False when list is empty.
    index: int = (
        0  # allows us to keep track of index to iterate through each element of list.
    )
    count: int = (
        0  # keeps track of how many identical elements exist at the same place in both strings.
    )
    while index < len(a):
        if a[index] == num:
            count += (
                1  # increases as given num value is the same a value within the string
            )
        index += 1
    if count == len(
        a
    ):  # ensures that ALL ints of the lsit are the same as the given num value.
        return True
    else:
        return False


def max(input: list[int]) -> int:
    """Returns the largest value in the list or a ValueError if the list is empty."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        index: int = 0
        big_num: int = input[
            0
        ]  # this will keep track of the greatest value within the list, it CANNOT be 0 to start off with because if the list has all negative numbers within it, it will not be able to accurately find the largest value then.
        while index < len(input):
            if input[index] > big_num:
                big_num = input[
                    index
                ]  # each time an index is bigger than the previous indexes, the biggest number value is updates to reflect this new big number.
            index += 1
        return big_num


def is_equal(input_1: list[int], input_2: list[int]) -> bool:
    """Indicates if every element at every index in 2 strings are equal."""
    if len(input_1) == len(
        input_2
    ):  # assures that we are considering 2 strings with the same number of elements.
        index: int = 0
        count: int = 0
        while index < len(input_1):
            if input_1[index] == input_2[index]:
                count += 1  # increases the count every like a identical element is found at the same place in both lists.
            index += 1
        if count == len(
            input_1
        ):  # because every element must be identical at every index, the count has to equal the whole lenght of the strings.
            return True
        else:
            return False
    else:
        return False
    # two distinct objects can be deeply equal to one another if what they are made of is equal to each other in essence.


def extend(input_1: list[int], input_2: list[int]) -> None:
    """Modifies the first list by adding the second list to the end of it."""
    index = 0
    while index < len(input_2):
        input_1.append(input_2[index])
        index += 1  # don't forget to increase index value WITHIN the while loop. I forgot to do this at the beginning and it resulted in the no result being displayed in the trialhead (probably because it was running an infinite loop).
