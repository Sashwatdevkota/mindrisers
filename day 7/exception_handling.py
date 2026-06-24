# Exception handling. exception that raise during the execution of program
# try: block of code that raise exception are placed in try block
# expect: block of code that is to be executed when exception raises in try block
# finally: block of code that is to be executed either exception raises or not

# try-except blocks


try:
    a = int(input("Enter a number: "))
    print(a + 5)
except ValueError:
    print("Value Error")
except NameError:
    print("Name Error")
except:
    print("Catch all error")
finally:
    print("FINAL BLOCK")

# try:
#     print(a + 5)
# except:
#     print("A is not defined")
