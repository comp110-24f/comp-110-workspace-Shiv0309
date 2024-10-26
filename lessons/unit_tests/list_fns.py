def get_first(input: list[str]) -> str:
    """Returns the first element of the list."""
    if len(input) == 0:
        return []
    return input[0]


def remove_first(input: list[str]) -> None:
    """Doesn't return anything but removes the first element of the list"""
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    """Remove AND return the first element"""
    first_element: str = input[0]
    input.pop(0)
    return first_element


# need to restart repel and reimport function every time you edit code
