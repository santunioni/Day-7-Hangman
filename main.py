from models.game import play


if __name__ == '__main__':

    play_again = True
    while play_again:

        play()

        pa = input('\n\nDo you wanna play again (y/n)? ')

        if pa.lower()[0] == 'y':
            play_again = True
        else:
            play_again = False
