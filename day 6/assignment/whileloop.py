# todo: implementing while loop
# get two numbers from user(a,b)
# check the greater number and print it out
# if a is greate than b print a statement {a} is greater than {b}
# if a is less than b
# if a and b are equal
# ask if they want to continue: yes: interate the code, no: terminate the loop


# while (True):
#   num1=input("Enter first number")
#   num2=input("Enter second number")
#   if num1>num2:
#     print(f"{num1} is greater than {num2}: ")
#   elif num1==num2:
#     print(f"both numbers {num1}, {num2} are equal: ")
#   else:
#     print(f"{num2} is greater than {num1}: ")

#   choice=input("Do you want to continue again (y/n): ")
#   if choice == "n": break


# simple calculator
# get two numbers from user and a operator(+,-,*,/)
# if the operator is +, print the sum of two number
# if the operator is -, print the subtraction of two number
# if the operator is *, print the multiple of two number
# if the operator is /, print the division of two number

# while True:

#     num1 = int(input("Enter your first number: "))
#     operator = input("Enter an operator(+,*,/,-)")
#     num2 = int(input("Enter your second number: "))

#     if operator == "+":
#         print(num1 + num2)
#     elif operator == "-":
#         print(num1 - num2)
#     elif operator == "*":
#         print(num1 * num2)
#     elif operator == "/":
#         print(num1 / num2)
#     else:
#         print("Please use the selected operator only")

#     choice = input("Do you want to continue again (y/n): ")
#     if choice == "n":
#         break


# get user's exam marks
# if the mark is greater than 100 and less than 0, print a statment
# if the mark is greater than 90 and less then 100, print a statment("Excekllent")
# if the mark is greater than 80 and less than 90 , print a statement
# if the mark is greater than 70 and less than 80 , print a statement
# if the mark is greater than 60 and less than 70 , print a statement
# if the mark is greater than 50 and less than 60 , print a statement
# if the mark is greater than 40 and less than 50 , print a statement
# if the mark is less than 40, print a statment
# ask if they want to continue: yes: interate the code, no: terminate the loop

while True:

    marks = float(input("Enter your grade"))
    if marks > 100 or marks < 0:
        print("Please enter a valid mark")
    elif marks > 90 and marks < 100:
        print("you got A+")
    elif marks > 80 and marks <= 90:
        print("you got A")
    elif marks > 70 and marks <= 80:
        print("you got B+")
    elif marks > 60 and marks <= 70:
        print("you got B")
    elif marks > 50 and marks <= 60:
        print("you got C+")
    elif marks > 40 and marks < 50:
        print("you got C")
    else:
        print("failed")

    choice = input("Do you want to continue again (y/n): ")
    if choice == "n":
        break


# define a dictionary username as key and password as value
# get the username and password from the user
# check if the username exists in the dictioney
# if yes: check if the password is correct(if yes: print Valid or Verified user, if no: print password incorrect)
# if no: print the statement(eg: Invalid username)
# ask if they want to continue: yes: interate the code, no: terminate the loop
