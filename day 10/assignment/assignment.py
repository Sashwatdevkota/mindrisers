# Accounting(.txt, .json)
# login/register ask user
# if register: get username, password(optional) from user and store it in a file
# if login: get username, password(optional) from the user and check if the username exists in the file
#     show 2  options: read balance, add balance
#     if add: get the amount to add store it in a file in dict format({username: amount})
#     if read: print out the balance of that user

print("Press 1 for login")
print("Press 2 for register")
choice = int(input("Choice: "))

if choice == 1:
    username = input("Please enter your existing username: ")

    f = open("day 10\\username.txt", "r")
    a = f.read()

    if username in a:
        print("Your account exists")

        print("Press 1 to read balance")
        print("Press 2 to add balance")
        option = int(input("Choice: "))

        if option == 1:
            f = open("day 10\\balance.txt", "r")
            b = f.read()
            print(b)
            f.close()

        if option == 2:
            amount = input("Enter amount to add: ")

            f = open("day 10\\balance.txt", "a")
            f.write(username + " : " + amount + "\n")
            f.close()

            print("Balance added.")

    else:
        print("Your username does not exist. Try to register.")

    f.close()

if choice == 2:
    username = input("Enter your new username: ")

    f = open("day 10\\username.txt", "a")
    f.write(username + "\n")
    f.close()
