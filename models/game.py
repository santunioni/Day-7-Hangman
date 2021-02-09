from models.arts import CHANCES as NUMBER_OF_CHANCES
from models.screen import screen
import models.checks as check


def run_game(*, word: str, chances: int = NUMBER_OF_CHANCES) -> None:
    word = word.title()

    current_word_list = ('_ ' * len(word)).split()
    word_to_display = check.spaced_string(current_word_list)

    already_chosen = ""

    while chances >= 0:

        if '_' not in current_word_list:
            screen(chances, word_to_display, already_chosen, won=True)

            if chances == 1:
                number_of_chances = f"{chances} chance"
            else:
                number_of_chances = f"{chances} chances"

            print(f"You guessed the word '{word_to_display.replace(' ', '')} with {number_of_chances} remaining!")
            break

        guess = screen(chances, word_to_display, already_chosen)
        if not guess:
            break

        already_chosen += guess

        char_positions = check.letter_in(guess, word=word)
        if char_positions:
            for position in char_positions:
                current_word_list[position] = guess.lower()
            word_to_display = check.spaced_string(current_word_list)
        else:
            chances -= 1
