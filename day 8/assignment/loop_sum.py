# For loop
# 8. Find the sum of numbers from 1 to 100

sum = 0

for i in range(1, 101):
    sum += i

print("Sum from 1 to 100 is", sum)

# 9. Find the sum of even numbers from 1 to 50

sum = 0

for i in range(1, 51):
    if i % 2 == 0:
        sum += i

print("Sum from 1 to 50 even numbers is", sum)

# 10. Find the sum of odd numbers from 1 to 50
sum = 0

for i in range(1, 51):
    if i % 2 != 0:
        sum += i

print("Sum from 1 to 50 odd numbers is", sum)
