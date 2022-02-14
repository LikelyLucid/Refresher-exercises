#Write a function check_factor(numl, num2) that takes two numbers and prints if the second number is a factor ot the first.
def check_factor(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False
