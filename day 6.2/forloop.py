# # for loop:
# # iterable: sequential data(group data and string data)
# # iteration: process of moving from first index of data to last index in the interable
# # iterator: variable using to perform iteraation in iterable

# # Syntax:

# # for iterator in iterable:
# # statment1
# # statment2

# a = [1, 2, 3, 4, 5]

# for i in a:
#     print("For loop", i)

# print("\n" * 5)


# # to do:
# # create a list of hobbies
# # print out a statement using each hobbies

# hobbies = ["Coding", "Gym", "Guitar", "Chess", "Football"]
# for hobbie in hobbies:
#     print(hobbie)


# # create a list of dictionary with name,age,contact
# infos = [
#     {"name": "ram", "age": 20, "contact": 1},
#     {"name": "ram", "age": 21, "contact": 4},
#     {"name": "sita", "age": 22, "contact": 3},
# ]

# for info in infos:
#     print(
#         f"Hello my name is {info["name"]}, my age is {info["age"]}, my contact no is {info["contact"]}"
#     )

# string = "Python Basics"
# # print out each characters

# for c in string:
#     print(c)


# # print the sum of data present in variable a

# a = [1, 2, 3, 4, 5, 6, 7]
# sum = 0
# for num in a:
#     sum += num
# print("Total sum is", sum)


z = ["apple", "mango", "watermelon", "cat", "dog", "mouse", "butterfly", "table"]
# print the number of times the loop is executed using iterable z

i = 0
for fruit in z:
    i += 1

print("The loop runs for", i, "times")


x = ("1", "15", "6", "13", "18", "9")

max = int(x[0])
min = int(x[0])
# find the greatest number and print

for num in x:
    num = int(num)
    if num < min:
        min = num
    if num > max:
        max = num

print("greatest is", max)
print("smallest is", min)
# find the smallest number and print


for i in range(2,10,2):
    print (i)