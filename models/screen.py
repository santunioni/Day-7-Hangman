from models.arts import stages, logo
from os import system, name


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def screen(chances, word_to_show, already_chosen):

    guess_word = True

    clear()
    print(logo + "\n\n")
    
    print(stages[chances], end="\n\n")

    if chances > 0:
        print(f"Number of chances: {chances}")
    else:
        guess_word = False
        print("You are dead.")

    if guess_word:

        char_guess = input(f"""\nGuess a character for the word: {word_to_show}
        Already chosen characters: {already_chosen}
        Choose: """)
        char_guess = char_guess.lower()

        while char_guess in already_chosen:
            char_guess = screen(chances, word_to_show, already_chosen)

        return char_guess

    return False
