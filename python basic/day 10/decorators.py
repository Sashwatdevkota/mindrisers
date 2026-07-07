# # decorators:


# def func2():
#     print("This is second function")


# def func():
#     print("This is a first function")
#     func2()


# func()


def into(a):
    print("Performing Arithmetic operations")
    a()


@into  #decorator
def add():
    print("Sum:", 5 + 10)
