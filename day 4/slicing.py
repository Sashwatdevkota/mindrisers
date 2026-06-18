# Slicing # acess a subset od data from a sequence

# start_index: inclusive -> read
# end_index: exclusive -> is not read ( yo value vanda sano)
# syntax: variable[start_index: end_index+1]
# syntax: variable[start_index: end_index+1:step]

# print out learn
a = "I am ( learning Python Basic"
a[7]  # reading from the letter l it is inclusive meaning it will read from l

print(a[7:12])


# print out learning
print(a[7:15])

# print I am
print(a[0:4])

# print Python
print(a[16:22])


# print Python Basic
print(a[16:28])

fruits = [
    "Apple",
    "Banana",
    "Mango",
    "Orange",
    "Grapes",
    "Pineapple",
    "Papaya",
    "Watermelon",
    "Strawberry",
    "Kiwi",
]

# print out "Grapes","Pineapple","Papaya","Watermelon","Strawberry"

print(fruits[4:9])

# print all except last 3
print(fruits[0:7])

# print out all fruits except first 4
print(fruits[4:10])

# print any 5 datas
print(fruits[2:7])


a = "I am ( learning python basic"
print(a[7:])


print("\n" * 30)


fruits = [
    "Apple",
    "Banana",
    "Mango",
    "Orange",
    "Grapes",
    "Pineapple",
    "Papaya",
    "Watermelon",
    "Strawberry",
    "Kiwi",
]


# print only even indexing
print(fruits[-4:-2:])
# print only odd indexing
print(fruits[1::2])

