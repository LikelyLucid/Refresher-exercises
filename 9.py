# function that only allows numbers to be entered
def numbers_only(string):
    if string.isdigit():
        return True
    else:
        return False