#Fernando Guzman
#02/23/25

#Problem 1- Use for statement and random.randrange to print 10 random intergers
#between 25-25

import random
#Importing random module because random.randrange function is available in this module

for _ in range(10):
#"_" is used a placeholder variable because its value is only needed for syntax requirements. 
    random_number = random.randrange(25,36)
    #use 36 because this reads the second number as exclusive. Gives you range of 25-35.
    print(random_number)
