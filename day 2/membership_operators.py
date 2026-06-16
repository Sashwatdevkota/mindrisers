#Membership operators are used to check if a 'member' exists in a sqeunce of data (list,tuple,set,string,etc)

#in , not in

list_numbers=[10,20,30,40]
tuple_numbers=(10,20,30,40)
set_numbers={10,20,30,40}

print(10 in list_numbers)
print(20 in tuple_numbers)
print(20 not in set_numbers)

text = "Python"

print("Py" in text)      
print("Java" in text)   