# for loop:
# iterable: sequential data(group data and string data)
# iteration: process of moving from first index of data to last index in the interable
# iterator: variable using to perform iteraation in iterable

# Syntax:

# for iterator in iterable:
# statment1
# statment2

a = [1, 2, 3, 4, 5]

for i in a:
    print("For loop", i)

print("\n" * 5)


# to do:
# create a list of hobbies
# print out a statement using each hobbies

hobbies = ["Coding", "Gym", "Guitar", "Chess", "Football"]
for hobbie in hobbies:
    print(hobbie)


# create a list of dictionary with name,age,contact
infos=[{"name":"ram","age":20,"contact":1},{"name":"ram","age":21,"contact":4},{"name":"sita","age":22,"contact":3}]

for info in infos:
  print(f"Hello my name is {info["name"]}, my age is {info["age"]}, my contact no is {info["contact"]}")
