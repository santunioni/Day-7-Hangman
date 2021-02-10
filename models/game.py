"""This module is responsible for running the Hangman game. It's main function is the run_game function."""

from models.arts import CHANCES as NUMBER_OF_CHANCES
from models.screen import screen
from models import check


def run_game(*, word: str, chances: int = NUMBER_OF_CHANCES) -> None:
    """This function runs the Hangman game.


    The function receives the parameters:
      Keyword:
        word: str -> the word to be guessed by the player.
        chances: int = NUMBER_OF_CHANCES -> the number of chances the player have to guess the word. \
It's default value is the NUMBER_OF_CHANCES global constant.
"""

    word = word.lower()
    current_word_list = ('_ ' * len(word)).split()
    word_to_display = check.spaced_string(current_word_list)

    # Start an empty string which contains already chosen letters
    already_chosen = ""

    while chances >= 0:

        if '_' not in current_word_list:
            # The player won!
            screen(chances, word_to_display, already_chosen, won=True)
            break

        elif chances > 0:
            # The player didn't win or lose yet!
            guess = screen(chances, word_to_display, already_chosen)
            already_chosen += guess

            char_positions = check.letter_in(guess, word=word)
            if char_positions:
                for position in char_positions:
                    current_word_list[position] = guess.lower()
                word_to_display = check.spaced_string(current_word_list)
            else:
                chances -= 1

        else:
            # The player lost!
            screen(chances, word_to_display, already_chosen)
            break
