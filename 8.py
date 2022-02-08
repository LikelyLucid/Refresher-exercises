pi = 3.14159265359
impo
radius = float(input("Enter the radius of the sphere: "))

area = round(4 * pi * radius ** 2, 2)
volume = round(4 / 3 * pi * radius ** 3, 2)

print("Area =", area, "square centimetres")
print("Volume =", volume, "cubic centimetres")

# alternatively