# todo: implementing while loop
# get two numbers from user(a,b)
# check the greater number and print it out
# if a is greate than b print a statement {a} is greater than {b}
# if a is less than b
# if a and b are equal
# ask if they want to continue: yes: interate the code, no: terminate the loop


while (True):
  num1=input("Enter first number")
  num2=input("Enter second number")
  if num1>num2:
    print(f"{num1} is greater than {num2}: ")
  elif num1==num2:
    print(f"both numbers {num1}, {num2} are equal: ")
  else:
    print(f"{num2} is greater than {num1}: ")
  
  choice=input("Do you want to continue again (y/n)")
  if choice == "n": break
  

# simple calculator
# get two numbers from user and a operator(+,-,*,/)
# if the operator is +, print the sum of two number
# if the operator is -, print the subtraction of two number
# if the operator is *, print the multiple of two number
# if the operator is /, print the division of two number
# ask if they want to continue: yes: interate the code, no: terminate the loop


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


# define a dictionary username as key and password as value
# get the username and password from the user
# check if the username exists in the dictioney
# if yes: check if the password is correct(if yes: print Valid or Verified user, if no: print password incorrect)
# if no: print the statement(eg: Invalid username)
# ask if they want to continue: yes: interate the code, no: terminate the loop