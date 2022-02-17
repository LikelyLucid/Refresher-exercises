"""
You will be given a series of integer numbers that you must add together. Each line will contain one number
between 1 and 100 and the series will be terminated with a #.
Your program must output the sum of all the numbers.
"""
input_list = input("enter your inputs").split()
sum = 0
print
for i in range(len(input_list)):
    if input_list[i] == "#":
        break
    else:
        sum += int(input_list[i])
print(sum)

