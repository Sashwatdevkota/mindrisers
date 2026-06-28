# 7. Suppose we have a pair of dice.
# First, use the random module to “roll” the two dice.
# Each die (named die1 and die2) should have an integer value from 1 to 6.
# Store the sum of the two random values in variable named total.
# Using a while loop, check if total is 2. If it isn't, print the string 'Nope' and keep "rerolling" the dice.
# Let the loop run until the total is 2, then print 'Snake eyes!

import random

while True:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print("Value of dice 1 is", dice1)
    print("Value of dice 2 is", dice2)

    if dice1 + dice2 == 2:
        print("Snake Eyes")
        break
    else:
        print("Nope")
