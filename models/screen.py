"""This module contains all functions related to printing the game in the terminal."""
from models.arts import STAGES, LOGO
from os import system, name


# define our clear function
def clear():
    """This function clear the terminal screen, either for Linux, Mac or Windows."""
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def screen(chances, word_to_display, already_chosen, /, *, won=False):
    """This function prints the game in the terminal.


    The function receives the parameters:
      Positional:
        chances: int -> number of chances the user still have
        word_to_display: str -> the current status of the word being guessed, \
in the underscore style
        already_chosen: str -> a string with the already chosen letters
      Keyword:
        won: bool = False -> a variable which is passed True if the user already \
won. Otherwise it is false


    The function does:
        Case the player has already won (won == True):
            - Prints the winning screen
            - Return None
        Case the player has already lost (chances == 0):
            - Prints the lost screen
            - Return None
        Case the player didn't win or lost yet (chances > 0):
            - Prints the player chances, current word status and ask for the user guess
            - Checks for the user input, forbidding numbers and repeated letters
            - Returns the user guess"""

    # Clean the screen
    clear()
    # Make head
    print(LOGO + "\n\n")
    print(STAGES[chances], end="\n\n")

    # Setup the initial message
    message = f"""\nGuess a character for the word: {word_to_display}
Already chosen characters: {already_chosen}
"""

    if won:
        # Message to print if already won 
        print(f"Number of chances: {chances}")
        print(message)

        if chances == 1:
            number_of_chances = f"{chances} chance"
        else:
            number_of_chances = f"{chances} chances"

        print(f"You guessed the word '{word_to_display.replace(' ', '')}' with {number_of_chances} remaining!")

        # End the function
        return None

    elif chances > 0:
        # Message to print in case there are chances to wast
        print(f"Number of chances: {chances}")

        char_guess = input(message + "Choose: ")

        # Ask the letter again if the user pressed enter without any letter
        if not char_guess:
            char_guess = screen(chances, word_to_display, already_chosen)

        # Set's the guess to only first letter in case the user typed a long string
        char_guess = char_guess.lower()[0]

        # Ask the letter again in case the user guess is a
        # number, or the guess was already chosen:
        if char_guess in already_chosen + '0123456789':
            char_guess = screen(chances, word_to_display, already_chosen)

        return char_guess

    # Message to print if have zero chances and didn't won
    print("You are dead.")

    return None
