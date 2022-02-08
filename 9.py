"""Sound travels at about 340 m/s, so if you multiply the number of seconds between the lightning and the
sound of the thunder by 340, you'll know how many meters away the storm is. For example, a three-second
count, would place the storm about I ,020 m away, or roughly I km.
Write a program that requests the number of secnnds between lightning and thunder and reports the
distance of the storm.
Test the program for the case where there are one and a quarter seconds between the lightning and
thunder. (Answer = 0.42 kms)
"""
seconds = float(
    input("Enter the number of seconds between lightning and thunder: "))

distance = seconds * 340
print("The distance of the storm is", distance, "meters")
