# local and global variables
# global variables can be used or accessed anywhere in the program here a,b are global variable


global_variable = "THIS IS GLOBAL VARIABLE"


# def addition(num1, num2):  # function define
#     print(
#         num1 + num2
#     )  # here num1 and num2 are local variable they only exists with in the scope of the function addition()
#     print(global_variable)


# a = int(input("Enter a number"))
# b = int(input("Enter a number"))
# addition(a, b)


# all though we can access global variable anywhere in the program we can change it inside a method only using global ahead of the variable

a = 15  # global variable
print("before changing")
print(a)


def functiontest():
    global a
    a += 5
    print("Local")
    print(a)


functiontest()
print("global")
print(a)
