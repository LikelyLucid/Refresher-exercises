
concrete_thickness = 0.5  # meters


def integer_checker(question):
    """This function checks if an input is an integer"""
    while True:
        try:
            number = float(input(question))
            return number
        except ValueError:

            if number == "X": exit()
            print("Please enter a valid integer")


def float_checker(question):
    """This function checks if an input is a float"""
    while True:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print("Please enter a valid float")


building_type = integer_checker("Enter the building type: \n1 = Resdential\n2 = Commercial\n")
length = float_checker("Enter the length of the building in meters: ")
width = float_checker("Enter the width of the building in meters: ")
depth = float_checker("Enter the depth of the building in meters: ")
volume = length * width * depth
print(
    "The volume of concrete required for a slab with a length of {length} and width of {width} and a depth of {depth} is {volume} cubic metres.".format(
        length=length, width=width, depth=depth, volume=volume))
