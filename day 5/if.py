# if else : condtonal statments

# condition must be True to execute the if block
# else block is executed iif the condiiitions in upper blockks are False

#if and elif block takes condition but else block does not take condition
#multiple elif block can be dined but if and else only one
#else block is executed if the conditions in upper blocks are false

# #Syntax
# condition='raining'
# if condition:
#   print("statement")
# elif condition:
#   print("statement")
# else:
#   print("statement")


a = 10
b = 5

# if values if a is greater than the value of b then print A is greater
if a > b:
    print("a is greater than b.")
elif a == b:
    print("a and b are equal")
else:
    print("b is greater than a")


print("This is outside the if block")

#to do
# get two numbers from user and check which one is greater and print it

# num1=int(input("Enter your first number: "))
# num2=int(input("Enter your second number: "))
# if num1>num2:
#   print(f"{num1} is greater than {num2}")
# elif num2>num1:
#   print(f"{num2} is greater than {num1}")
# else:
#   print("Both numbers are equal")
  
  
#simple calculator
#get two numbers from user and a operator(+,*,-,/)
#print output of the slected operation


num1=int(input("Enter your first number: "))
operator=input("Enter an operator(+,*,/,-)")
num2=int(input("Enter your second number: "))

if operator == "+" :
  print(num1+num2)
elif operator == "-" :
  print(num1-num2)
elif operator == "*" :
  print(num1*num2)
elif operator == "/" :
  print(num1/num2)
else:
  print("Please use the selected operator only")
  
  


#get user exam marks
# if greater than 100 and less than 0 print error
# 90 - 100 
#80 - 89 
#.....

marks=float(input("Enter your grade"))
if (marks > 100 or marks <0):
  print("Please enter a valid mark")
elif (marks > 90 and marks < 100):
  print()
elif (marks > 90 and marks < 100):
  print()
elif (marks > 90 and marks < 100):
  print()
elif (marks > 90 and marks < 100):
  print()
elif (marks > 90 and marks < 100):
  print()
elif (marks > 90 and marks < 100):
  print()
  
  # simple calculator
# get two numbers from user and a operator(+,-,*,/)
# if the operator is +, print the sum of two number
# if the operator is -, print the subtraction of two number
# if the operator is *, print the multiple of two number
# if the operator is /, print the division of two number

# get user's exam marks
# if the mark is greater than 100 and less than 0, print a statment
# if the mark is greater than 90 and less then 100, print a statment("Excekllent")
# if the mark is greater than 80 and less than 90 , print a statement
# if the mark is greater than 70 and less than 80 , print a statement
# if the mark is greater than 60 and less than 70 , print a statement
# if the mark is greater than 50 and less than 60 , print a statement
# if the mark is greater than 40 and less than 50 , print a statement
# if the mark is less than 40, print a statment

# define a dictionary username as key and password as value
# get the username and password from the user
# check if the username exists in the dictioney
# if yes: check if the password is correct(if yes: print Valid or Verified user, if no: print password incorrect)
# if no: print the statement(eg: Invalid username)