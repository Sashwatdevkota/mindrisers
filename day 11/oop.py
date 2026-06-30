# oop: object oriented programming
# class : structures, blueprint
# object : data created using class


# syntax:
class class_name:
    # variables are called attributes
    # functions are called methods
    var = 1


class Person:
    name = "Ram"
    age = 35
    address = "KTM"
    gender = "male"


r1 = Person()  # r1 is object, Person() is class call

print(r1.name)


sita = Person()

sita.name = "Sita"
sita.age = "30"
sita.address = "BKT"
sita.gender = "female"

# sita.abc = "ABC" #adding separate attribute to the object sita

print(sita.name)
print(sita.age)
print(sita.address)
print(sita.gender)
print(sita.abc)
