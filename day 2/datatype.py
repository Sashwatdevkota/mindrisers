#datatypes in python
# string init float list tuple boolean  etc



#------------------------STRING-------------------------------------------#

#string: collection of characters all strings must be inside a ' ' " "

a='hello he\'s' # here \ is a escape character
b="hello \"HE\" is"
c='''This is a triple quote also used mainly
    for paragaphs'''

# print(c)


#------------------------INTEGER-------------------------------------------#

i=52 # whole numbers
print(i)
print(type(i))


#------------------------FLOAT-------------------------------------------#

f=15.535 # decimal numbers
print(f)
print(type(f))


#------------------------Boolean-------------------------------------------#

b=True
b=False
print(b)
print(type(b))


#------------------------None-------------------------------------------#

n = None # an empty variable will be declared
print(n)
print(type(n))


#------------------------Group Datatypes-------------------------------------------#
# List [] used to define list, multiple data of multiple datatypes, mutable(changeable), ordered

my_list= ['hello',50,55.5,True]
print(my_list)
my_list[2]=20
print(my_list)

#Tuple () used to define list, mutiple data of multiple datatypes, immutable(unchangebale, ordered)

my_tuple= ('hello',50,55.5,True)
print(my_tuple)
print(type(my_tuple))

#set: {} used to define set, multiple data of multiple data of multiple datatupes, unordered, does not except duplicate data, mutable

my_set={'hello',50,55.5,True,'hello'}
print(my_set)


#dictionary: {} used to define dictionary, key: value pair ( this can be different datatypes asw), key must be unique

my_dict={1:"ram", 2:"sita", "third": 12}
print(my_dict)

#keys if duplicated with overright the value 
my_dict={1:"ram", 2:"sita", "third": 12, 1:"test"}
print(my_dict)
