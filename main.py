from models.words import WORD_LIST
from models.game import run_game
from datetime import datetime
import random
import time


def main() -> None:
    play_again: bool = True
    while play_again:

        random.seed(datetime.now().microsecond)
        run_game(word=random.choice(WORD_LIST))

        play_again_str = input('\n\nDo you wanna play again (y/n)? ')
        if play_again_str.lower()[0] == 'y':
            play_again = True
            print("\n\nStarting again ...\n")
            time.sleep(1)
        else:
            play_again = False
            print("\n\nLeaving ...\n")
            time.sleep(1)
        del play_again_str


if __name__ == '__main__':
    main()
