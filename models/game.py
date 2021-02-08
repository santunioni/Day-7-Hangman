
import models.checks as check
from models.screen import screen
from models.words import word_list
from random import choice
from models.arts import chances


def play(*, word=choice(word_list), chances=chances):
    
    word = word.title()

    current_word_list = ('_ ' * len(word)).split()
    current_word, word_to_show = check.compile(current_word_list)

    already_chosen = ""

    while chances >= 0:

        if current_word == word:
            print(f"\nYou guessed the word '{current_word}' with {chances} chances remaining!")
            break

        guess = screen(chances, word_to_show, already_chosen)

        if not guess:
            break

        already_chosen += guess
          
        char_positions = check.letter_in(guess, word=word)
        if char_positions:
            for position in char_positions:
                current_word_list[position] = guess.lower()
            current_word, word_to_show = check.compile(current_word_list)
        else:
            chances -= 1
