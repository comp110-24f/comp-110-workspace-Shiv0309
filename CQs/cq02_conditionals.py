"""CQ02: Writing a simple number guessing game."""

__author__ = "730767271"


def guess_a_number() -> None:
    secret: int = 7

    x: int = int(input("Guess a number: "))
    print("Your guess was " + str(x))
    if x == 7:
        print("You got it!")
    elif x < 7:
        print("Your guess was too low! The secret number is", secret)
    elif x > 7:
        print("Your guess was too high! The secret number is", secret)


if __name__ == "__main__":
    guess_a_number()
