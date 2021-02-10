"""This module contains the checks the game have to perform during execution."""


def letter_in(letter: str, /, *, word: str):
    """This function checks if a letter occurs in a word, and return a list with the positions.


    Receives the parameters:
      Positional:
        - letter: str -> the letter to be checked if is in a word.
      Keyword:
        - word: str -> the word to be searched.


    Returns:
        - letter_positions: list[int] -> a list containing the letter positions, empty if the \
letter don't occur in the word.
"""

    letter, word = letter.lower(), word.lower()
    letter_positions = []

    for position in range(len(word)):
        if word[position] == letter:
            letter_positions.append(position)

    return letter_positions


def spaced_string(wordlist) -> str:
    """This function receives a list with strings within the format [A, _, r, p, l, a, _] \
and returns a string within the format 'A _ r p l a _'"""

    if wordlist[0] != '_':
        # Set the first letter to upper case if already discovered
        wordlist[0] = wordlist[0].upper()

    # Mount a string with the shape: A _ r _ l a n _
    string_with_spaces = ""
    for character in wordlist:
        string_with_spaces += character
        string_with_spaces += " "
    # removing last space
    string_with_spaces = string_with_spaces[:-1:]

    return string_with_spaces
