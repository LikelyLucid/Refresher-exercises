"""Write a function print_word(word, number) that prints the given number of letters in uppercase and the rest in lowercase.
"""
def print_word(word, number):
    """
    Prints the given number of letters in uppercase and the rest in lowercase.
    """
    print(word[:number].upper() + word[number:].lower())