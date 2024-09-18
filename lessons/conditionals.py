""" Practice with conditionals."""


def less_than_10(num: int) -> None:
    """Tell me if num is < 10."""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")
    print("Have a nice day!")


less_than_10(num=5)


# if statement is false, we get none because we never clarified that it should return false) in the firs place
# indentations are also important, ensure you are indenting properly.


def should_i_eat(hungry: bool) -> None:
    """Tells me whether or not to eat based on hunger."""
    if hungry:  # conditional/boolean expression
        print("Eat some food silly goose!")  # "then" block
    else:
        print("Do your COMP 110 homework instead.")  # "else" block
    print("I'm proud of you <3")  # either way, be kind to yourself


should_i_eat(hungry=True)
# if I add print to above line, it will print our "None" too because it prints the return value of the should_i_eat funtion which we specificed in line 20 is "None"


def check_first_letter(word: str, letter: str) -> str:
    """Checks if first letter of a word matches to a given letter."""
    if (
        word[0] == letter
    ):  # to access the first letter of a word, you must use the built-in indexing function.
        print("match!")  # be sure to not leave a speace after print to put (
    else:
        print("no match!")


check_first_letter(
    word="happy", letter="s"
)  # make sure to put "" around the input values as they are strings, otherwise, you will get an error.


def get_weather_report() -> None:
    "Advises you based on weather."
    weather: str = input("What is the weather?")
    if (
        weather == "rainy" or weather == "cold"
    ):  # have a boolean on either side of the or operator.
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


get_weather_report()
