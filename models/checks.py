def letter_in(letter: str, /, *, word: str):
    letter, word = letter.lower(), word.lower()
    letter_positions = []

    for position in range(len(word)):
        if word[position] == letter:
            letter_positions.append(position)

    return letter_positions


def spaced_string(wordlist) -> str:

    if wordlist[0] != '_':
        wordlist[0] = wordlist[0].title()

    string_with_spaces = ""
    for character in wordlist:
        string_with_spaces += character
        string_with_spaces += " "

    # removing last space
    string_with_spaces = string_with_spaces[:-1:]

    return string_with_spaces
