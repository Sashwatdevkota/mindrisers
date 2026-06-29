# # file handling:process of manipulating file programmatically

# # open the file
# f = open(file_path, mode)

# close
# f.close()

# # read mode r read the contexts of the files, files must exist
# f = open("day 1\\dat1.txt", "r")
# a = f.read()
# f.close()
# print(a)

# write(w) if files does not exist and a new file is created
f = open("test.txt", "w")
f.write("Hello this is statement in write mode")
f.close()

# append(a):new lines are added to the files at the end, if file does not exist a new file is created
f = open("test.txt", "a")
f.write("Hello this is statement in append mode")
f.close()

# todo:
# login/register ask user
# if register: get username and store in a file
# if login: get username and check if the username exists in the file

print("Press 1 for login")
print("Press 2 for register")
choice = int(input("Choice: "))
if choice == 1:
    username = input("Please enter your existing username:")
    f = open("day 10\\username.txt", "r")
    a = f.read()
    if username in a:
        print("Your account exists")
    else:
        print("Your username does not exists try to register")
    f.close()
if choice == 2:
    username = input("Enter your new username: ")
    f = open("day 10\\username.txt", "a")
    f.write(username)
    f.close()
