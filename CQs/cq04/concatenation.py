"""CQ04: Importing functions from different files."""

__author__ = "730767271"


def concat(input1: str, input2: str) -> str:
    """Returns the concatenation of the two input strings."""
    return input1 + input2


word1: str = "happy"
word2: str = "tuesday"

print(concat(word1, word2))
