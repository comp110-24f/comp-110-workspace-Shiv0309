"""EX06 - Practice with dictionary functions."""

__author__ = "730767271"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dict."""
    return_dict: dict[str, str] = {}
    for key in input_dict:  # iterating through each key valye in the dict
        if (
            input_dict[key] in return_dict
        ):  # if duplicate values are contianed in the input_dict, we need to raise a KeyErorr while making the inverted return_dict as when the values become keys, it will meant the there are identical keys in the return_dict which is not possible.
            raise KeyError(
                "KeyError"
            )  # if the value from the input_list is already in the return_list (as a key), we are raising a KeyError as dicts CANNOT contain identical key values.
        else:
            return_dict[input_dict[key]] = (
                key  # if the value from the input_list is not a duplicate, then we are adding it to the return dict as a key.
            )
    return return_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Returns the color that appears most frequently in the input_dict."""
    dict_1: dict[str, int] = (
        {}
    )  # creating empty dict to keep track of how many times each color appears in the input_dict.
    for key in input_dict:
        if (
            input_dict[key] in dict_1
        ):  # if the color has already appeared before in the input_dict and thus is already in dict_1, we are increasing the color's value by 1.
            dict_1[input_dict[key]] += 1
        else:  # if this is the first time the color has appeared in the input_dict, then we are establishing a value of 1 for that specific color in dict_1.
            dict_1[input_dict[key]] = 1
    most_frequent_color: str = (
        ""  # creating empty string so we can later modify to be the color that appears most frequently in the input_dict.
    )
    count: int = 0
    for key in dict_1:
        if (
            dict_1[key] > count
        ):  # Not >= because if there is a tie for the most popular color, the color that appeared in the input_dict first has to be returned, meaning it must remian the most_frequent_color.
            count = dict_1[
                key
            ]  # updating count to reflect the new highest frequency value of the color.
            most_frequent_color = str(
                key
            )  # updating the color to be one with the new highest frequency value.
    return most_frequent_color


def count(input_list: list[str]) -> dict[str, int]:
    """Returns a dict with each unique value in the input_list and how many times the value appears in the input_list."""
    return_dict: dict[str, int] = (
        {}
    )  # initializing an empty dict to add on to and return at the end
    for elem in input_list:  # looping through each element in the input_list
        if (
            elem in return_dict
        ):  # if the element from the input_list has already been found before in the input_list and is thus a duplicate value, then increase the count associated with that element by 1 in the return_dict.
            return_dict[elem] += 1
        else:  # if the element is not a duplicate of the previous values of the list, then assign it an initial count of 1 in the return_dict
            return_dict[elem] = 1
    return return_dict


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """Returns a dict where each key is a unique letter in the alphabet and each value is a list of the words that begin with that letter from the input_list."""
    return_dict: dict[str, list[str]] = (
        {}
    )  # initializing an empty dict to add on to and return at the end
    for elem in input_list:  # looping through each element in the input_list
        key: str = elem[
            0
        ].lower()  # creating key variable for return_dict and initialzing it to be the lower case version of the first letter of the element we are looping through from the input_list. .lower() is built-in Python method that takes in no arguments and returns the lower cased string of a given string.
        if (
            key in return_dict
        ):  # if the first letter of this string element already appeared before as the first letter of a previous word in the list, then we simply add this element to the list in the return_dict that is associated with this particular first letter key value.
            return_dict[key].append(elem)
        else:  # if none of the previous words in the string began with the same first letter as the word we are iterating through now, then we add the first letter as a key and start a new empty list as its value in the return_dict. Then, we add the word to the list.
            return_dict[key] = []
            return_dict[key].append(elem)
    return return_dict


def update_attendance(input_dict: dict[str, list[str]], day: str, student: str) -> None:
    """Mutates the input_dict to reflect new attendance status of various students throughout the week."""
    if (
        day in input_dict
    ):  # if the given day already exists as a key in the input_dict and thus has an associated list with it, then we simply add the given student's name the list associated with the day.
        if (
            student not in input_dict[day]
        ):  # added this here as autograder didn't want duplicate student names in the list for a day. Thus, function will only add the given student's name to the list if it is not already in it.
            input_dict[day].append(student)
    else:  # if the given day doesn't exist in the in the input_dict, then add the day as key to the input_dict and assign it a value of an empty list. Then, we add the given student's name to the list.
        input_dict[day] = []
        input_dict[day].append(student)
