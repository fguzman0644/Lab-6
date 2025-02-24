#Fernando Guzman
#02/23/25

#Problem 5-Create a function that converts radian to degrees based on the user's input.
#Also show the calculated value using the degrees funtion in the math module.

import math


radians = float(input("Please enter your value for radians: "))

degrees = radians * (180 / math.pi)
#Based on this equation, we can see that 3.14 radians will equal 180
#This is what we will use for our base test to make sure that the equation matches the function

print(degrees)
print(math.degrees(radians))
