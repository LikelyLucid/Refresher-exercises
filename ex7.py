"""Write a function print_word(word, number) that prints the given number of letters in uppercase and the rest in lowercase.
"""
def print_word(word, number):
    for i in range(number):
        print(word[i].upper(), end="")
    for i in range(number, len(word)-1):
        print(word[i].lower(), end="")

print(print_word("Hello", 3))
