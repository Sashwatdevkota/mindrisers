# Nesred staement: nested if

a = 5
b = 5
c = 10

# if values if a is greater than the value of b then print A is greater
# if values if b is greater than the value of a then print B is greater


# Voting Eligibility
# get user age
# if user age < 18: print statment
# if user age > 18:
# print statement
# ask if they have voting card
# if yes print a statement,
# # if no
#  ask if you want to create one
#  # if yes: print a statment
#  # if no: print a statment

age = int(input("Enter your age"))
if age > 18:
    print("You are eligible to vote")
    card = input("Do you have a voting card (y/n)")
    if card == "y":
        print("Good")
    elif card == "n":
        print("Do you want to create one? (y/n)")
        choice = input()
        if choice == "y":
            print("Go to www.createvotingcard.com")
        elif choice == "n":
            print("bad")
        else:
          print("please enter the correct choice for card")
    else:
        print("This is not a valid choice")
else:
  print("you can not vote")

# Licence
# get user age
# if user age < 18: 
#     print statment
#     ask if they can to get one(yes/no)
#     if yes: print a statement
#     if no: print a statement
#       one statement for invalid choice(optional)
# if user age >= 18:
#      print a stetement
#     ask if they have Licence:
#     if yes: print a statement:
#     if no: 
#        ask if you want to create one
#        if yes: print a statement
#        if no: print a statement
#        one statement for invalid choice(optional)
#     if not yes or no: a statement for the choice(optional)

age = int(input("Enter your age"))
if age >0 and age<100:
  print("enter a valid age")
elif age < 18:
  print("You are not eligible for license")
  print("Would you like to create one?(y/n)")
  choice=input()
  if choice=="y":
    print("Please wait until you are 18 to apply for one")
  elif choice=="n":
    print('Thank you! (Age<18 elif choice)')
  else:
    print("Invalid choice (For age less than 18)")
else:
      print("You are to create a license would you like to create one?")
      choice=input()
      if choice =="y":
        print("go to www.license.com")
      elif choice=="n":
        print("please consider creating one")
      else:
        print("invalid choice")