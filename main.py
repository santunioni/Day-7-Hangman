from models.game import run_game
import time


if __name__ == '__main__':

    play_again = True
    while play_again:

        run_game()

        play_again = input('\n\nDo you wanna play again (y/n)? ')
        if play_again.lower()[0] == 'y':
            play_again = True
            print("\n\nStarting again ...\n")
            time.sleep(1)
        else:
            play_again = False
            print("\n\nLeaving ...\n")
            time.sleep(1)
