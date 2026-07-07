# # Exception handling. exception that raise during the execution of program
# # try: block of code that raise exception are placed in try block
# # expect: block of code that is to be executed when exception raises in try block
# # finally: block of code that is to be executed either exception raises or not
# # only one catch block is executed for one try block. if multiple catch blocks are present
# # then the first catch block that matches the exception is executed and rest of the catch blocks are ignored

# # try-except blocks


# try:
#     a = int(input("Enter a number: "))
#     print(a + 5)
# except ValueError:
#     print("Value Error")
# except NameError:
#     print("Name Error")
# except:
#     print("Catch all error")
# finally:
#     print("FINAL BLOCK")

# # try:
# #     print(a + 5)
# # except:
# #     print("A is not defined")


while True:

    try:
        num1 = int(input("Enter your first number: "))
        operator = input("Enter an operator(+,*,/,-): ")
        num2 = int(input("Enter your second number: "))

        if operator == "+":
            print(num1 + num2)
        elif operator == "-":
            print(num1 - num2)
        elif operator == "*":
            print(num1 * num2)
        elif operator == "/":
            print(num1 / num2)
        else:
            print("Please use the selected operator only")
    except:
        print("Exception handling")

    choice = input("Do you want to continue again (y/n): ")
    if choice == "n":
        break


