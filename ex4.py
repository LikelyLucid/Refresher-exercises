#Write a function check_factor(numl, num2) that takes two numbers and prints if the second number is a factor ot the first.
def check_factor(num1, num2):
    return num1 % num2 == 0
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if check_factor(num1, num2):
    print("The second number is a factor of the first.")
else:
    print("The second number is not a factor of the first.")
