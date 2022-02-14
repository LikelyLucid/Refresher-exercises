def check_factor(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if check_factor(num1, num2):
    print("The second number is a factor of the first.")
else:
    print("The second number is not a factor of the first.")
