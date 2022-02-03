"""Write a program which gets the user to input two numbers.
If the numbers have different values, output the higher value otherwise output a message saying they are equal.
The program must repeatedly ask for two numbers until a rogue number of 0 is entered. """
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

if number1 == 0 or number2 == 0:
    print("You have entered 0, exiting program.")
elif number1 > number2:
    print(f"{number1} is greater than {number2}")
elif number1 < number2:
    print(f"{number2} is greater than {number1}")
else:
    print(f"{number1} and {number2} are equal")
