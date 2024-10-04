"""Some scope examples"""


def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char
    removed."""
    copy: str = ""  # Set up empty str to copy values over
    index: int = 0  # lcoal variables: copy, index, msg, and char
    print(word)
    while index < len(msg):
        if msg[index] != char:  # if the letter is NOT char
            copy += msg[index]  # add it to copy
        index += 1
    return copy


if __name__ == "__main__":
    # create a variable called word with the value “yoyo”
    word: str = (
        "yoyo"  # GLOBAL variable = exists throughout the program throughout the module)
    )
    # print the result of calling your function with arguments word and "y"
    print(remove_chars(msg=word, char="y"))  # with keyword arguments
    # print the result of calling your function with arguments word and "o"
    print(remove_chars(word, "o"))  # with positional arguments
