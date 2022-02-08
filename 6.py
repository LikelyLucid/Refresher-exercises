
biking_cal = 200
jogging_cal = 475
swimming_cal = 275
# all hours
weight_lost = 454 / 3500 # mg / calories

bike_hours = int(input("How many hours did you bike? "))
jogging_hours = int(input("How many hours did you jog? "))
swimming_hours = int(input("How many hours did you swim? "))

total_calories = bike_hours * biking_cal + jogging_hours * jogging_cal + swimming_hours * swimming_cal # add them all together

print("you lost", round(total_calories * weight_lost / 1000, 3), "kg") #divide by 1000 to get kg


