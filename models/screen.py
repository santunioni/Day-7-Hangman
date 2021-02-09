from models.arts import STAGES, LOGO
from os import system, name


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def screen(chances, word_to_display, already_chosen,/ , *, won=False):

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

        if not char_guess:
            char_guess = screen(chances, word_to_display, already_chosen)

        char_guess = char_guess.lower()[0]

        if char_guess in already_chosen:
            char_guess = screen(chances, word_to_display, already_chosen)

        return char_guess

    # Message to print if have zero chances and didn't won
    print("You are dead.")

    return None
