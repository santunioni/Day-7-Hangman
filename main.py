"""This is the main module of the Hangman game.
Use the command to run the game:
`python3.8 main.py`
"""

from models.words import WORD_LIST
from models.game import run_game
import random
# the time module is imported for improving user experience with the sleep() function
import time


def main() -> None:
    """This is the function which initializes the Hangman game."""

    while True:
        run_game(word=random.choice(WORD_LIST))

        play_again = input('\nDo you wanna play again (y/n)? ')
        if play_again.lower()[0] == 'y':
            print("\n\nStarting again ...\n")
            time.sleep(1)
        else:
            print("\n\nLeaving ...\n")
            time.sleep(1)
            return None

        del play_again


if __name__ == '__main__':
    main()
