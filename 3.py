concrete_thickness = 0.5  # meters
res_concrete_thickness = concrete_thickness / 2


def integer_checker(question):
    """This function checks if an input is an integer"""
    while True:
        try:
            number = input(question)
            if number == "X" or "x":
                exit()
            else:
                number = int(number)
                return number
        except ValueError:
            print("Please enter a valid integer")


def float_checker(question):
    """This function checks if an input is a float"""
    while True:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print("Please enter a valid float")


while True:
    building_type = integer_checker("Enter the building type: \n1 = Resdential\n2 = Commercial\n")
    length = float_checker("Enter the length of the building in meters: ")
    width = float_checker("Enter the width of the building in meters: ")
    if building_type == 1:
        depth = res_concrete_thickness
    else:
        depth = concrete_thickness
    volume = length * width * depth
    print(
        "The volume of concrete required for a slab with a length of {length} and width of {width} and a depth of {depth} is {volume} cubic metres.".format(
            length=length, width=width, depth=depth, volume=volume))
