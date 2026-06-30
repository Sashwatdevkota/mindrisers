# # oop: object oriented programming
# # class : structures, blueprint
# # object : data created using class


# # syntax:
# class class_name:
#     # variables are called attributes
#     # functions are called methods
#     var = 1


class Person:
    name = "Ram"
    age = 35
    address = "KTM"
    gender = "male"

    def intro(self):

        print(f"""
            Name: {self.name}
            Age: {self.age}
            Address: {self.address}
            Gender: {self.gender}
            """)


r1 = Person()  # r1 is object, Person() is class call

print(r1.name)


sita = Person()

sita.name = "Sita"
sita.age = "30"
sita.address = "BKT"
sita.gender = "female"

sita.abc = "ABC"  # adding separate attribute to the object sita

print(sita.name)
print(sita.age)
print(sita.address)
print(sita.gender)
print(sita.abc)

sita.intro()
# todo
# create a class car
# attribute: brand, model, color, release_date

# create  2 objects


# class Car:
#     brand = None
#     model = None
#     color = None
#     release_date = None


# car1 = Car()
# car1.brand = "brand1"
# car1.model = "model1"
# car1.color = "color1"
# car1.release_date = "date1"

# print(car1.brand)
# print(car1.model)
# print(car1.color)
# print(car1.release_date)

# car2 = Car()
# car2.brand = "brand2"
# car2.model = "model2"
# car2.color = "color2"
# car2.release_date = "date2"

# print(car2.brand)
# print(car2.model)
# print(car2.color)
# print(car2.release_date)
