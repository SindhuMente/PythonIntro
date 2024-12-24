
# this is a print statement
# print("hi") 

'''this
is a multiline
comment'''

# Variables

var = 1 # this is an integer
# print(var) # the value of var is 1
# print("the value of var is " + str(var)) # the + sign in python is used only for concatenating strings
# print("the value of var is", var)
var1 = 3
# print("var =", var, "var1 =", var1) # example of chaining variables in a print statement

my_string = "this is a python string" # this is a string
my_string1 = "this is another string"

# print the value of both strings on one line
# print(my_string, my_string1)
# print the value of both string on separate lines
# print(my_string)
# print(my_string1)

# print the value of both strings on separate lines using one print statement
# print(my_string, "\n", my_string1)
# print out the first character of one of the strings
# print(my_string[0])
# print out a substring of length 3 from one of the strings
# print(my_string[0:3])
# print(my_string[2:])
# print("\"e\"")
a,b,c = 1,"hi",2.5
# print(a,b,c)

#types of variables
# print(type(a))
# print(type(b))
# print(type(c))

#random numbers
import random

# print(random.randrange(1,10))

#for loops
languages = ["python", "c++", "java"]
# for i in languages:
#     print(i)

#while loops
i=0
while i<10:
    # print(i)
    i+=1

#functions
def randomNum(x,y):
    return random.randrange(x,y)

# print(randomNum(1,10))


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
# print(int(my_string))

# convert my_string1 to a float
my_string1 = float(my_string1)
# convert my_int to a string
my_int = str(my_int)
# convert my_float to an int
# my_float = int(my_float)
# print(my_float)

# print(round(my_float))

# Strings

multi_word_str = "hey, hello, hi, how's it going?"

# for x in range(5):
#     print(x)

n = len(multi_word_str)
# print(n)
# split the string up into 2 at one of the commas
newString1 = None
newString2 = None
for i in range(len(multi_word_str)):
    if multi_word_str[i] == ",":
        newString1 = multi_word_str[:i]
        newString2 = multi_word_str[i+1:]
        break
# print(newString1,"\n", newString2)
        
# split the string up into multiple strings by using a built in string method
y = multi_word_str.split(", ")
# for i in y:
#     print(i)
'''write a function to print out every character in the string "hello" in the following 
format: "the ith character in the string is: _", using a format string'''
def printString(z):
    for i in range(len(z)):
        print(f"the {i}th character in the string is {z[i]}")
# printString("testing function")
# print out the middle 2 characters in "hello" using negative indexing
my_string = "hello"
# print(my_string[-2], my_string[-3])
# replace the word hola with adios in the following string: "to say bye in spanish, we say hola"
z = "to say bye in spanish, we say hola"
# print(z.replace("hola","adios"))
# remove the extra spaces in the following string: " he l l o o o    "
z = " he l l o o o    "
newString = ""
for i in range(len(z)):
    if z[i] == " ":
        continue
    newString += z[i]
# print(newString)
# concatenate the following strings: "hi my name is ", & "shannu "
# print("hi my name is " + "Shannu")


# write a function that takes in 1 number (n) and returns the nth number in the fibbonaci sequence
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
# print(fibonacci(6))


my_string = "hi this is a string"
my_string = my_string[0:3] + my_string[3:7].upper() + my_string[7:]
# print(my_string)


# these are all equivalent
# print(not(5 == 4))
# print(5 != 4)
# print (5 is not 4)
# print(not(5 is 4))

# bool evaluation
# anything that is a "non-zero" value is True
# the default value of that variable is False
# print(bool(1))
# print(bool(0))
# print(bool("text"))
# print(bool(""))
# print(bool(-1.0))
# print(bool(0.0))


# Operators
# operators are essentially +, -, *, /
# or, and, not, xor
# ==, <, <=, >, >=, !=

x = 8
y = 8
# print(x is y) # TODO: revisit when learning about inheritance
x = "123"
y = "123"
# print(x is y)
x = ["apple", "banana"]
y = ["apple", "banana"]
# print(x is y)


class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        for i in range(len(x)):
            if x[i] != x[-i-1]:
                return False
        return True
        
# Lists

# add elements to a list
lst1 = ["1", "2", "3"]
lst1 = [1.0, "2", 3]
lst1.append(4)
# print(lst1)
lst1 = lst1 + [4]
# print(lst1)
lst2 = list()
lst2 = []
lst2.append(1) # will always add the element to the end of the list
# print(lst2)
# print(lst1[2])
'''Key thing to note below:'''
my_string = "helloooo"
# can't do this -> my_string[4] = "l"
lst1[1] = 4
# print(lst1)
lst1[0:2] = [1, 2, 3]
# print(lst1)
# insert element into list
lst = [1, 2, 3, 4, 5] 
lst1 = lst[0:3] + [6] + lst[3:] # 1
# print(lst1)
lst.insert(3, 6) # insert works in-place similar to append
# print(lst)
lst = [1, 2, 3]
lst1 = [4, 5]
# lst.append(lst1) # we can have a list of lists
# lst.append(lst1[0:]) # we can have a list of lists
lst += lst1 # one valid way to concatenate lists
lst.extend(lst1)
# print(lst)

# removing elements from a list
lst = [1, 2, 1, 3, 5, 8]
# lst.remove(1) # remove accepts the element you want to remove as an argument
# lst.pop() # pop with no argument will remove the last element in the list
# lst.pop(3) # pop with argument removes element at specified index
# del lst[3] del also removes the element it's given from the lst specified
# del lst # this deletes the list itself if we no longer want that variable

# clearing out a list
# for i in range(len(lst)):
#     lst.pop()
# lst = []
# lst.clear()
# print(lst)

# [print(x) for x in lst] # list comprehension

# for x in lst: # for loop / iteration
#     print(x)


# sorting lists
lst = ["milky_way", "caramel", "lindor"]
# lst.sort(reverse=True)

def my_func(x):
    if "caramel" == x:
        return 0
    if "milk" in x:
        return 1
    if "lindor" == x:
        return 100
    else:
        return 0.5
    
lst = ["hersheys", "cadbury milk", "lindor", "milky_way", "caramel", "almond joy", "twix"]
# the order should be: [caramel, almond joy, hersheys, twix, cadbury milk, milky way, lindor]
lst.sort(key = my_func) # sort function breaks ties based on what element it processes first
# print(lst)

lst = [1, 2, 3]
lst1 = lst # this is a reference to lst, not a copy of it
#lst[1] = 5
#print(lst, lst1)

lst1 = lst[0:] # this is now a copy of list 
# lst[1] = 5
# print(lst1)
lst1 = lst.copy() # one way to make a copy
lst1 = list(lst) # making a copy using a constructor
lst[1] = 5
# print(lst1)

'''Tuples'''
my_tuple = (1.0, "2")
my_tuple = tuple((0, 1, 1, 2))
# my_tuple[0] = 1 we can't modify this
# print(my_tuple[0:2]) # we can splice tuples just like strings & lists
# use len to get length of tuple
pi_tuple = (3.14,)
# print(type(pi_tuple))
# modifying a tuple
my_fav_chocos = ("lindor", "caramel")
# my_fav_chocos = ("lindor", "caramel", "milky way") # method 1
# my_lst = list(my_fav_chocos)
# my_lst.append("milky way")
# my_fav_chocos = tuple(my_lst)
# my_fav_chocos += ("milky way",)
# print(my_fav_chocos)
my_pt = (3, 6, 4) # this is called packing a tuple
x, y, z = my_pt # this is called unpacking the tuple
# print(x, y, z)
my_pt = (3, 6, 4, 5, 7, 9)
x, y, *z = my_pt
x, *y, z = my_pt
# print(x, y, z)

my_tup = (1, 2, 3) * 2 # my_tup += my_tup
# print(my_tup)

my_lst = [1, 2, 3] * 2
# print(my_lst)

# print(my_tup.count(1))


'''Sets'''
my_set = {1, 2, 3, 4, 1}
my_set.add(5)
# print(my_set)
my_set = set((1, 2, 3))
other_set = set((4, 5, 6))
# my_set.update(other_set)
# my_set.update([3, 8, 9])
# print(my_set)
my_set.remove(1)
my_set.discard("1")
my_set.pop()
# print(my_set)
new_set = my_set | other_set
# print(new_set)


# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         strs.sort(key = lambda x: len(x))
#         print(strs)
#         prefix = strs[0][0]
#         i = 0
#         while all(prefix in x for x in strs):
#             if len(prefix) == len(strs[0]):
#                 return prefix
#             prefix = strs[0][:i+1]
#         return prefix[:-1]


'''Dictionaries'''
thisdict = {
  "brand": "Ford",
  "model": 2020,
  "year": 1964,
  "year": 2020
}
my_dict = dict({"year": {"this_year": 2024, "next_year": 2025}, 
                "day": ["saturday", "today is great", "random stuff"], 6: "6:00"})
# print((my_dict["year"])["this_year"]) # accessing a key that doesn't exist with [] will throw an error
# print(my_dict.get("dne", 0)) # get() allows you to specify a default value for any key
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# if "day" in my_dict:
#     print("yes")
# Changing/Updating a dictionary
my_dict["day"][0] = "sunday"
my_dict.update({"day": ["saturday", "today is great", "random stuff"]})
my_dict["month"] = "december"
# my_dict.pop("month") # pop always requires an input for DICTIONARIES
# my_dict.popitem()
# del my_dict["month"]
# print(my_dict)

# Looping through a dict
for x, y in my_dict.items():
    # print(x, y)
    pass

for x in my_dict:
    if x == "day":
        for y in my_dict["day"]:
            # print(y)
            pass

# refreshing our memory of tuple unpacking
w, x, *y, z = (1, 2, 3, 4, 5, 6, 7)
# print(w, x, y, z)

# copying a dictionary
my_dict1 = my_dict.copy()
my_dict1 = dict(my_dict)


# Loops - continue statement
for i in range(10):
    if i == 8:
        continue
    # print(i)


'''Functions'''

# we want a function that can take in one or two arguments

# Method 1 - optional parameters
def my_interesting_function(first_name, last_name, middle_name = "n/a"):
    # print(first_name, middle_name, last_name)
    pass

my_interesting_function("Jane", "Doe")
my_interesting_function("Shannu", "Mente", "V")

# Method 2 - *args
def my_interesting_function_1(num, *args):
    sum = num
    for i in range(len(args)):
        sum += args[i]
    print(sum) 

my_interesting_function_1(25)
my_interesting_function_1(1, 2, 3, 4, 5)

def my_interesting_function_2(first_name, **args):
    middle_name = ""
    if "middle_name" in args:
        middle_name = args["middle_name"]
    print(first_name, middle_name, args["last_name"])

my_interesting_function_2(first_name="Shannu", last_name="Mente")

'''Hash Functions'''

my_storage = [None for i in range(10)]
def my_hash_function(key: str):
    if key[0] == "a":
        return 0
    if key[0] == "b":
        return 1
    if key[0] == "c":
        return 2
    if key[0] == "d":
        return 3
    if key[0] == "e":
        return 4
    if key[0] == "f":
        return 6
    else:
        return 5

my_data_point_1 = ("apple", "an apple a day keeps the doctor away")  #key value
my_data_point_2 = ("color", "green is the best color")
my_data_point_3 = ("orange", "a fruit")
my_data_point_4 = ("keyboard", "can't code without them")
my_data_point_5 = ("function", "functions are cool")

index = my_hash_function(my_data_point_1[0])
my_storage[index] = my_data_point_1[1]
print(my_storage)

index = my_hash_function(my_data_point_2[0])
my_storage[index] = my_data_point_2[1]
print(my_storage)

index = my_hash_function(my_data_point_3[0])
my_storage[index] = my_data_point_3[1]
print(my_storage)

index = my_hash_function(my_data_point_4[0])
# my_storage[index] = my_data_point_4[1]
print(my_storage)

index = my_hash_function(my_data_point_5[0])
my_storage[index] = my_data_point_5[1]
print(my_storage)


'''Side Quest: str.split()'''
my_str = " hell o wo rld    i"
# print(my_str.split()) # output = ['hell', 'o', 'wo', 'rld', 'i']

'''Back to Hash functions'''
'''Collison Resolution'''
# Method 1 = Open Addressing

# Linear Probing
index = my_hash_function(my_data_point_4[0])
if my_storage[index] is not None:
    i = index + 1
    if index == len(my_storage) - 1:
        i = 0
    while i != index:
        if i == len(my_storage):
            i = 0
        elif my_storage[i] != None and i < len(my_storage):
            i += 1
        else:
            my_storage[i] = my_data_point_4[1]
            break

# print(my_storage)
my_storage = ['an apple a day keeps the doctor away', None, 'green is the best color', None, None, 'a fruit', 'functions are cool', None, None, None]

# Quadratic Probing
index = my_hash_function(my_data_point_4[0])
if my_storage[index] is not None:
    i = index + 3
    if index == len(my_storage) - 3:
        i = 0
    while i != index:
        if i == len(my_storage) - 3:
            if my_storage[i] == None:
                my_storage[i] = my_data_point_4[1]
            i = 0
        elif i == len(my_storage) - 2:
            if my_storage[i] == None:
                my_storage[i] = my_data_point_4[1]
            i = 1
        elif i == len(my_storage) - 1:
            if my_storage[i] == None:
                my_storage[i] = my_data_point_4[1]
            i = 2
        elif my_storage[i] != None and i < len(my_storage) - 3:
            if my_storage[i] == None:
                my_storage[i] = my_data_point_4[1]
            i += 3
        else:
            my_storage[i] = my_data_point_4[1]
            break

print(my_storage)

# Double Hashing

# Method 2 = Chaining
