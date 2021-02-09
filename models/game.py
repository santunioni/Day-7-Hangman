import models.checks as check
from models.screen import screen
from models.words import word_list
from random import choice
from models.arts import chances

random_word = choice(word_list)


def run_game(*, word=random_word, chances=chances):
    word = word.title()

    current_word_list = ('_ ' * len(word)).split()
    current_word, word_to_show = check.compile(current_word_list)

    already_chosen = ""

    while chances >= 0:

        if current_word == word:
            screen(chances, word_to_show, already_chosen, won=True)

            if chances == 1:
                number_of_chances = f"{chances} chance"
            else:
                number_of_chances = f"{chances} chances"

            print(f"You guessed the word '{current_word}' with {number_of_chances} remaining!")
            break

        guess = screen(chances, word_to_show, already_chosen)
        if not guess:
            break
        else:
            # Take only the first word from the input
            guess = guess[0]

        already_chosen += guess

        char_positions = check.letter_in(guess, word=word)
        if char_positions:
            for position in char_positions:
                current_word_list[position] = guess.lower()
            current_word, word_to_show = check.compile(current_word_list)
        else:
            chances -= 1
