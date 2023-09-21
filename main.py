file = 'book/frankenstein.txt'

with open(file) as f:
    words = f.read()  # list of words
    print(f"-- Begin report of {file} --")
    print(len(words.split()), "words found in the document\n")
    lettersCounted = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0,
            'e': 0,
            'f': 0,
            'g': 0,
            'h': 0,
            'i': 0,
            'j': 0,
            'k': 0,
            'l': 0,
            'm': 0,
            'n': 0,
            'o': 0,
            'p': 0,
            'q': 0,
            'r': 0,
            's': 0,
            't': 0,
            'u': 0,
            'v': 0,
            'w': 0,
            'x': 0,
            'y': 0,
            'z': 0,
    }
    for letter in words:
        if letter.lower() in lettersCounted:
            lettersCounted[letter.lower()] += 1
    for letter in lettersCounted:
        if lettersCounted[letter] > 0:
            print(f"The '{letter}' character was found {lettersCounted[letter]} times.")
    print("-- End report --")
