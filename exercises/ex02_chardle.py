"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730767271"


def input_word() -> str:
    """Asks user for a 5 character word & validates if the length of input is 5."""
    user_word: str = str(
        input("Enter a 5-character word:")
    )  # This line is asking the user for a 5 character word and storing it as the local variable five_character_word.
    if len(user_word) == 5:  # Remember to use == as this is the relational operator.
        return user_word  # Return should be used instead of print as we clearly stated a return type in the signature above.
    else:
        print("Error: Word must contain 5 characters.")
        exit()  # This built in function tells the program to quit at this point. If it is not a 5 letter word, there is no need for us to be printing it again.
        return user_word  # Return should be used instead of print as we clearly stated a return type in the signature above.


def input_letter() -> str:
    """Asks user for a single chracter & validates if the length of input is 1."""
    single_character: str = input("Enter a single character:")
    if len(single_character) == 1:
        return single_character  # Return should be used instead of print as we clearly stated a return type in the signature above.
    else:
        print("Error: Character must be a single character.")
        exit()  # This built in function tells the program to quit at this point. If it is not 1 character, there is no need for us to be printing it again.
        return single_character  # Return should be used instead of print as we clearly stated a return type in the signature above.


def contains_char(
    word: str, letter: str
) -> (
    None
):  # new variables have to created here, it will keep looping if input_word and input_letter are used as the parameters.
    """Checks if the input character matches characters within the input word."""
    print(
        "Searching for " + letter + " in " + word
    )  # The spaces after the for and before and after the in are important as otherwise, it will print without the spaces.
    count: int = (
        0  # This is establishing a variable to keep track of how instances of the letter are found in the word. It starts with zero as increase if it finds any instances of the letter later on.
    )
    if word[0] == letter:
        print(letter + " found at index 0")
        count = (
            count + 1
        )  # Count is increased since an additional instance of letter is found in word.
    if word[1] == letter:
        print(letter + " found at index 1")
        count = (
            count + 1
        )  # Count is increased since an additional instance of letter is found in word.
    if word[2] == letter:
        print(letter + " found at index 2")
        count = (
            count + 1
        )  # Count is increased since an additional instance of letter is found in word.
    if word[3] == letter:
        print(letter + " found at index 3")
        count = (
            count + 1
        )  # Count is increased since an additional instance of letter is found in word.
    if (
        word[4] == letter
    ):  # Stop at index 4 since we started with index 0 and this covered the 5 letters in the word.
        print(letter + " found at index 4")
        count = (
            count + 1
        )  # Count is increased since an additional instance of letter is found in word.
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif (
        count == 1
    ):  # This conditional needed to be added because without it, it would have printed out 1 instances which is gramatically incorrect.
        print("1 instance of " + letter + " found in " + word)
    else:
        print(
            str(count) + " instances of " + letter + " found in " + word
        )  # This statement needs to be added here as we want the count of the instances of letter in words AFTER all the indexes have been checked.


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
