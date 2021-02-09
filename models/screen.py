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


def screen(chances, word_to_show, already_chosen, won=False):

    guess_word = True

    clear()
    print(LOGO + "\n\n")
    
    print(STAGES[chances], end="\n\n")

    if chances > 0:
        print(f"Number of chances: {chances}")
    else:
        guess_word = False
        print("You are dead.")

    message = f"""\nGuess a character for the word: {word_to_show}
        Already chosen characters: {already_chosen}
        """
    if guess_word and not won:

        char_guess = input(message + "Choose: ")
        char_guess = char_guess.lower()[0]

        while char_guess in already_chosen:
            char_guess = screen(chances, word_to_show, already_chosen)

        return char_guess

    elif won:

        print(message + "\n")

    return False
