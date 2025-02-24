#Fernando Guzman
#02/23/25

#Problem 6-Use a for statement to calculatet he factorial of a user input value.

import math

def calc_factorial(num): #This defines our function we made to calculate factorials
    factorial = 1
    for i in range(1, num + 1): #This makes it loop from 1 to the user input value inclusively
        factorial *= i
    return factorial #Once loop is completed, this returns the calculated factorial

user_value = int(input("Please enter the number you'd like to calculate its factorial for: "))
calculated_factorial = calc_factorial(user_value)

print(calculated_factorial)
print(math.factorial(user_value))
