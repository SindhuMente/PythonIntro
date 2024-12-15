
# this is a print statement
print("hi") 

'''this
is a multiline
comment'''

# Variables

var = 1 # this is an integer
print(var) # the value of var is 1
print("the value of var is " + str(var)) # the + sign in python is used only for concatenating strings
print("the value of var is", var)
var1 = 3
print("var =", var, "var1 =", var1) # example of chaining variables in a print statement

my_string = "this is a python string" # this is a string
my_string1 = "this is another string"

# print the value of both strings on one line
print(my_string, my_string1)
# print the value of both string on separate lines
print(my_string)
print(my_string1)

# print the value of both strings on separate lines using one print statement
print(my_string, "\n", my_string1)
# print out the first character of one of the strings
print(my_string[0])
# print out a substring of length 3 from one of the strings
print(my_string[0:3])
print(my_string[2:])
print("\"e\"")
a,b,c = 1,"hi",2.5
print(a,b,c)

#types of variables
print(type(a))
print(type(b))
print(type(c))

#random numbers
import random

print(random.randrange(1,10))

#for loops
languages = ["python", "c++", "java"]
for i in languages:
    print(i)

#while loops
i=0
while i<10:
    print(i)
    i+=1

#functions
def randomNum(x,y):
    return random.randrange(x,y)

print(randomNum(1,10))


# Numbers & type conversions (Casting)

num0 = 12345
num1 = 4.9
num2 = 2e2

# convert num0 to a float
num0 = float(num0)
# convert num1 to an int
num1 = int(num1)
# convert num2 to an int
num2 = int(num2)

my_string = "12345 is a great number"
my_string1 = "123"
my_int = 1
my_float = 2.6

# convert my_string to an int
my_string = my_string[:5]
print(int(my_string))

# convert my_string1 to a float
my_string1 = float(my_string1)
# convert my_int to a string
my_int = str(my_int)
# convert my_float to an int
# my_float = int(my_float)
# print(my_float)

print(round(my_float))