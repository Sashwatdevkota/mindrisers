try:
    x = 10 / 0
except:
    print("Error")
# else:
# print("Success") #this print when there is no error
finally:
    print("Program ended")  # this print regardless if there is an error or not
