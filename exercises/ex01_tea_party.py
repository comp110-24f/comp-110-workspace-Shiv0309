"""Planning a cute tea party!"""

__author__: str = "730767271"


def main_planner(guests: int) -> None:
    """Calls the previous functions and prints their rules"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


# keyword argument (people=guests) passes the local variable value of guests from main_planner function's input to all other functions. For the cost function, you have to use the other functions' output values to assign values to the input of this funtion. While running it in the Trailhead, I faced a problem when there was no sapce after the :. I realized to fix this, I had to add a space in the code itself after : before putting the ".


def tea_bags(people: int) -> int:
    """Doubles number of people to get number of tea bags needed"""
    return people * 2


# The r in return should be lowercase because I got an error when I tried to do REPL with uppercase R.


def treats(people: int) -> int:
    """Multiplies number of tea bags needed by 1.5"""
    return int(tea_bags(people=people) * 1.5)


# Keyword argument (people=people) passes the local variable value of people from tea_bags function to treats function.


def cost(tea_count: int, treat_count: int) -> float:
    """Adds the product of the number of tea bags by 0.50 and the product of the number of treat by 0.75"""
    return (tea_count * 0.50) + (treat_count * 0.75)


# The operation of addition must also be mentioned in docstring because I almost left it out.


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
