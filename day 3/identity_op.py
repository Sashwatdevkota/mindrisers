#Identity operator:checks if two values are equal,location

a=10
b=15
c=10

#is : if two data are identical, Output:True, else False
print (a is c)

#is not: if two data are identical, Output: False else Trye
print (a is not b)

a=10 # ---> id=1 same as c
b=15 # ---> id=2 different location
c=10 # ---> id=1 same as a

#in python if two values are the same its memory location is set as the same


print(id(a))
print(id(b))
print(id(c))
