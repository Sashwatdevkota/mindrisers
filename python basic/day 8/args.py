# args:
# a parameter accepts multiple data, accepts data in tuple former
# add the data send to the function


def addition(*abc):
    total = 0
    for i in abc:
        total += i
    print(total)


addition(1, 2, 3, 4)

# create a function that prints out the introduction of the user name send to it 

def intro(*names):
  for name in names:
    print(f"I am {name}")
    
intro("Ram","Shyam","Gita","Sita")


