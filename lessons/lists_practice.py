"""Basic syntax of lists."""

# Create an empty list
my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

# String Analogy
my_name: str = ""  # literal for string
my_name: str = str()  # constructor

# Adding values to a list
my_numbers.append(1.5)
my_numbers.append(2.3)
# print(my_numbers)  # print has to go after appending values if you want to see new values in the printed out verison.

# Creating an already populated list
game_points: list[int] = [102, 86, 94]

# Subscription Notation/Indexing
game_points[2]
last_game: int = game_points[2]  # storing indexed access as a variable

# Modifying a list (because lists are mutable UNLIKE str)
game_points[1] = 72  # changing 86 to 62 within game_points list

# Checking length of a list
len(game_points)

# Removing an item from a list
game_points.pop(1)  # removes 72 from game_points list


# Practice Problem:
# Funtion name: display
# parameters: list of integers
# RV: None
# Print every element in the input list
# Call display on game_points
def display(int_list: list[int]) -> None:
    """Prints out every element in the input list"""
    index: int = 0

    while index < len(int_list):
        print((int_list[index]))
        index += 1


display(game_points)
