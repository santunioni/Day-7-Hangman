from models.arts import CHANCES as NUMBER_OF_CHANCES
from models.screen import screen
import models.checks as check


def run_game(*, word: str, chances: int = NUMBER_OF_CHANCES) -> None:
    word = word.title()

    current_word_list = ('_ ' * len(word)).split()
    word_to_display = check.spaced_string(current_word_list)

    already_chosen = ""

    while chances >= 0:

        guess = ''
        if '_' not in current_word_list:
            screen(chances, word_to_display, already_chosen, won=True)
            break

        elif chances > 0:
            guess = screen(chances, word_to_display, already_chosen)
            already_chosen += guess

        char_positions = check.letter_in(guess, word=word)
        if char_positions:
            for position in char_positions:
                current_word_list[position] = guess.lower()
            word_to_display = check.spaced_string(current_word_list)
        else:
            chances -= 1
