
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

if number1 == 0 or number2 == 0:
    print("You have entered 0, exiting program.")
else:
    print("The higher number is: ", max(number1, number2))
