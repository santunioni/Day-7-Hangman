def letter_in(letter: str, /, *, word: str):
    letter, word = letter.lower(), word.lower()
    letter_positions = []
    start = 0

    while start <= len(word):
        if letter.lower() in word.lower()[start::]:

            position = word.lower().index(letter, start)
            letter_positions.append(position)

            start = position + 1
            del position
        else:
            break

    return letter_positions


def sum_to_string(wordlist) -> str:
    string = ""
    string_with_spaces = ""
    for character in wordlist:
        string_with_spaces += " "
        string_with_spaces += character
        string += character

    return string, string_with_spaces


def compile(wordlist):
    if wordlist[0] != '_':
        wordlist[0] = wordlist[0].title()
    return sum_to_string(wordlist)
