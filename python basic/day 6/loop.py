# Loop

# while loop: conditional(True/False)
# while block is executed until the condition is met
# if condition is True, while block is executed
# if condition is False then only program teminate

# condition=True

# while condition:
#   #statements

a = 5
b = 0

while a > b:
    b += 1
    print("A is greater than b.")
    if b == 3:
        break
    b += 1
print("Whileloop end.")


a = 5
b = 0
while a > b:
    b += 1
    if b == 3:
        continue
        print("A is greater than b.", b)
print("Whileloop end.")



# for loop
