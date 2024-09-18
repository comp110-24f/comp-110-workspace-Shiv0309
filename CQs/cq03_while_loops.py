"""CQ03: using a while loop to iterate over a string."""

__author__ = "730767271"


def num_instances(phrase: str, search_char: str) -> int:
    """Returns the number of times search_char can be found in phrase."""
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            index += 1  # increases the index count to allow us to consider the next character of the phrase. AKA keeps the while loop going.
            count += 1  # increases the final count so that if this character was in the phrase, it can be accounted for.
        else:
            index += 1  # increases the index count to allow us to consider the next character of the phrase. AKA keeps the while loop going.
    return count  # displays the final number of instances the character was found in the given phrase.
