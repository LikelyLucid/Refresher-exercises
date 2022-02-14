"""Write a function numbers_in_list(list, multiple) that takes a list and a number and prints a new list of all
numbers in the given list that are a multiple of that number. See the examples below to understand what is
needed :
"""
def numbers_in_list(list, multiple):
    new_list = []
    for num in list:
        if num % multiple == 0:
            new_list.append(num)
    return new_list
pr