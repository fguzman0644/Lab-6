#Fernando Guzman
#02/23/25

#Problem 4-Calculate pi and also print out the pi from the math function

import math
#Import math module

#Defined our function to approximate pi, our non-math module equation is using
#the Leibniz formula which uses a series to approach the value of pi
def approximate_pi(terms):
    
    pi_approx = 0
    for i in range(terms):
        pi_approx += ((-1)**i) / (2*i + 1) #Leibniz's formula 
    return 4 * pi_approx
    
n_terms = 1000000

pi_approximation = approximate_pi(n_terms)

print(f"{pi_approximation:.4f}")
#f-strings to format the output to show four decimal places
print(math.pi)
#using the pi function in the math module
