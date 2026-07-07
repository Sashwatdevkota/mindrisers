# # functions: like variables, block of code is assigned to a function
# # specific task


# def function_name(var1, var2):
#     print("hello")
#     return None


# def addition():  # function define
#     a = int(input("Enter a number"))
#     b = int(input("Enter a number"))
#     print(a + b)


# addition()  # function call

# # do assignments


# def intro():
#     name = "Ram"
#     age = 35
#     print(f"My name is {name} and my age is {age}")


# intro()


# parameter: variables defend inside the parenthesis in function definition
# argument: variables defined inside the parenthesis iin function cell


# def intro(name, age, add):  # this is parameter
#     print(f"My name is {name} and my age is {age}")


# n = "Ram"
# a = 35
# add = "KTM"
# intro(n, a, add)  # this is argument


# def addition(num1, num2):  # function define
#     print(num1 + num2)


# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))

# addition(a, b)


# def addition(num1, num2):  # function define
#     sum = num1 + num2
#     return sum


# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))

# sum = addition(a, b)
# print(sum)


# Types of Argument

# Positional Argument: The sequence of argument is same as the same the sequence of parameters


# def intro(name, age, add):  # this is parameter
#     print(f"My name is {name} and my age is {age}. I live in {add}")


# n = "Ram"
# a = 35
# add = "KTM"
# intro(n, a, add)  # this is argument
# intro(n, add, a)  # this is argument

# Keyword argument:


# def intro(name, age, add):  # this is parameter
#     print(f"My name is {name} and my age is {age}. I live in {add}"")


# n = "Ram"
# a = 35
# address = "KTM"

# intro(name=n, age=a, add=address)
# intro(name=n, add=address, age=a)


# Default arguments: If argument
def intro(
    age, address, name="Default"
):  # default parameters must be at the end of the function bracket
    print(f"My name is {name} and my age is {age}. I live in {address}")


intro(age=30, address="KTM")


# Types of Argument:

#positional arguments
#keyword arguments
#default arguments