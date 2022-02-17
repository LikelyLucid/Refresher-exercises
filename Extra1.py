input_list = input("enter your inputs").split()
sum = 0
print(input_list)
for i in range(len(input_list)):
    if input_list[i] == "#":
        break
    else:
        sum += int(input_list[i])
print(sum)

