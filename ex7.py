def print_word(word, number):
    for i in range(number):
        print(word[i].upper(), end="")
    for i in range(number, len(word)):
        print(word[i].lower(), end="")
    print()