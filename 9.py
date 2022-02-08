# function that only allows numbers to be entered
def numbers_only(string):
    return bool(string.isdigit())
numbers_only('123')