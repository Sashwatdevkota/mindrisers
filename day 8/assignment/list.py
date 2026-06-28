# 11.  create a list of numbers. Find sum of all numbers in the list

sum = 0
number = [1, 4, 7, 5, 9, 11, 20, 5, 34]
for i in number:
    sum += i
print("Sum:", sum)

# 12. define a word and print out each character


# 13.  create a list of numbers. find the largest number
greatest = 0
number = [1, 4, 7, 5, 9, 11, 20, 5, 34]
for i in number:
    if i > greatest:
        greatest = i
print("Greatest:", greatest)


# 14. create a list of numbers and count how many even numbers exist
count = 0
number = [1, 4, 7, 5, 9, 11, 20, 5, 34]
for i in number:
    if i % 2 == 0:
        count += 1
print("count:", count)
