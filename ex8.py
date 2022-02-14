"""Write a function print_word(word, number) that prints the given number of letters in uppercase and the rest in lowercase.
"""
def print_word(word, number):
    for i in range(len(word)):
        if i < number:
            print(word[i].upper())
        else:
            print(word[i].lower())

print(print_word("Hello", 3))
