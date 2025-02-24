#Fernando Guzman
#02/23/25

#Problem 3- Use random.choice to select a day of the week from a list and print the day.

import random
#Imports the random module

days_of_week = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
    ]
#We can use days_of_week to provide our random.choice function a list of option to choose from.

random_day = random.choice(days_of_week)
print(random_day)
