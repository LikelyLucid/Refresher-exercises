pi = 3.1
radius = float(input("Enter the radius of the sphere: "))

area = round(4 * math.pi * radius ** 2, 2)
volume = round(4 / 3 * math.pi * radius ** 3, 2)

print("Area =", area, "square centimetres")
print("Volume =", volume, "cubic centimetres")