#Identity operators checks where two variables refers to the same memory allocation

#is, is not

a=[1,2,3]
b=a
c=[1,2,3]

print(a is b)

print(a is not c)
print(a == c)

#Here is check if two variables refer to the same memory alloaction while == check values

b[1]=4

print(a is b)
print(a)
print(b)