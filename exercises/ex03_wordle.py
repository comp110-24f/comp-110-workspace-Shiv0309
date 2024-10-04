"""EX03 - Wordle!"""

__author__ = "730767271"


def input_guess(secret_word_len: int) -> str:
    """Prompts user to enter a guess until they provide a guess of the  desired length."""
    user_word: str = input(
        f"Enter a {secret_word_len} character word: "
    )  # the f is an alterantive method to concatenate the string by also converting int values.  # Asking the user for a word of the desired length and storing it as a local variable.
    while (
        len(user_word) != secret_word_len
    ):  # this has to be a loop because the system must keep prompting the user for a new input word until they provide an input word of the desired length.
        user_word = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return user_word  # has to be in the same indent level as the while as the word is only printed after the it exists the while loop since it is of the desired lenght.


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks if a given character is in the secret word or not."""
    assert (
        len(char_guess) == 1
    )  # asserting the assumption that the length of char_guess has to 1.
    index: int = 0
    count: int = 0
    while index < len(secret_word):
        if (
            secret_word[index] == char_guess
        ):  # allows us to iterate through the string and check if the given character can be found anywhere within in.
            count += 1
        index += 1  # we have to increase the index value in order to move on from 1 character of the string and consider the other one. Also this provides a way for us to exit the while loop.
    if (
        count > 0
    ):  # # this confirms to the user that their guess was found to be in the secret_word.
        return True
    else:  # this confirms to the user that their guess was nowhere to be found in the secret_word.
        return False


def emojified(guess: str, secret: str) -> str:
    """Returns a string of green, yellow, or white boxes to let user know if character is in right place, wrong place, or not needed at all, respectively."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    copy: str = (
        ""  # Set up empty str as a basis to add boxes to. When I did not have this variable, only the first square would print, indicating to me that the while loop did not repeat. Thus, I realized that I needed a string of emojis not just one emoji. So, I built this empty string to start off with and built it on.
    )

    index: int = 0
    while index < len(secret):
        if guess[index] == secret[index]:
            copy += GREEN_BOX  # indicates that the character of user's guess word is in right place.
        else:
            if contains_char(secret, guess[index]):
                copy += YELLOW_BOX  # indicates that the character of user's guess word is in the secret word but is in wrong place.
            else:
                copy += WHITE_BOX  # indicates that the character of user's guess word is not in the secret word.
        index += 1  # allows for next character in user's guess word to be compared to the next character in secret word. After all characters have be checked, allows us to exit while loop.
    return copy


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    X: int = 1  # created this variable to keep track of which turn player is on.
    won: bool = (
        False  # created this variable so that when player does win in the future, we can update this value to True and exit out of the while loop to declare victory.
    )
    while (X <= 6) and (
        won == False
    ):  # remember to use == because it is a boolean operator (for False). Also parentheses are required due to and operator.
        print(f"=== Turn {X}/6 ===")
        user_guess: str = input_guess(
            len(secret)
        )  # using input_guess function to prompt the user to guess a word. len(secret) assures that the main game is winnable with any word as the secret.
        print(
            emojified(user_guess, secret)
        )  # converting the results of the player's guess to emojis of green, yellow, or white boxes to indicate if their guess(es) was right.
        if (
            user_guess == secret
        ):  # allowing the while loop to be exited if the player has correctly guessed the secret word.
            won = True  # this line specficially makes the while loop condition False, allowing for it to be exited.
            print(f"You won in {X}/6 turns!")
        else:  # allows player to advance to their next turn.
            X += 1
    if (X > 6) and (
        won == False
    ):  # this is if player could not guess the word in six turns, they are notified of their loss and told to play again tomorrow.
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
