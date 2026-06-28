# 4. Create a weight conversion program that:
# Asks the user what their Earth weight is (as a float).
# Asks the user for a planet number (as an int).
# Then, use an if/elif/else statement to calculate the user's weight on the destination planet.
# To calculate the user's weight:
# destination weight=Earth weight × relative gravity
# Number	Planet	Relative Gravity
# 1	Mercury	0.38
# 2	Venus	0.91
# 3	Mars	0.38
# 4	Jupiter	2.53
# 5	Saturn	1.07
# 6	Uranus	0.89
# 7	Neptune	1.14
# If the user enters a planet number outside of 1 - 7, print a message that says 'Invalid planet number'.

weight = float(input("Enter your weight"))
print("1. Mercury")
print("2. Venus")
print("3. Mars")
print("4. Jupiter")
print("5. Saturn")
print("6. Uranus")
print("7. Neptune")

planet = int(input("Enter the planet you want to see your relative weight at:"))
if planet == 1:
    relative_weight = weight * 0.38
elif planet == 2:
    relative_weight = weight * 0.91
elif planet == 3:
    relative_weight = weight * 0.38
elif planet == 4:
    relative_weight = weight * 2.53
elif planet == 5:
    relative_weight = weight * 1.07
elif planet == 6:
    relative_weight = weight * 0.89
elif planet == 7:
    relative_weight = weight * 1.14
else:
    relative_weight = None

if relative_weight:
    print("Relative weight is:", relative_weight)
else:
    print("Invalid planet number")
