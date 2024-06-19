"""
#Agenda 
1. Python keywords & Identifiers
2. Comments, Induntation and Statements.
3.Variable and data types in Python.
4. Standard Input and Output
5. Operators
6. Control flow: If, else, elif
7. Control flow: while loop
8. Control flow: for loop
9. Control flow: break and continue
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it

# Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

#Variable
# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# You can also use the + operator to output multiple variables:
# Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# To take output of string & integer use comma (,) not plus (+)
x = 5
y = "John"
print(x, y)

# Global Variables
""" 
Variables that are created outside of a function (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.
 """
# 
x = "awesome"

def myfunc():
  print("Python is " + x)
myfunc()

"""  
If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 
The global variable with the same name will remain as it was, global and with the original value.
Example below
"""
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

# To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

# Refer Data_types.py(for data types)

# pip install keyword
import keyword
print (keyword.kwlist)

import math
result = math.sqrt(25)
print(result)

from math import sqrt
result = sqrt(99)
print (result)

_age = 21
print(_age)

age = 22
print(age)

Age = 23
print(Age)

AGE = 24
print(AGE)

_age123 = 25
print(_age123)

_Age = 26
print(_Age)


MARKS = 10
marks = 20
print ("Hello you got", MARKS, "out of", marks) # Anything written in Quotes "" is a string.

a = 3 # value a 
b = 52 # value b
c = b/a # division
print(c)

# Indendation:-
def add_No(a,b):
    """
    This function will add numbers
    Parameters:
    a(int): The first variable
    b(int): The second variable

    Return:
    int: which is the sum of a and b
    """
    return a + b
    print(add_No.__doc__)


if True:
    print("This is true") # Error: if it is not indentated (1tab or 4 spaces before print)

# Incorrect use of Indendation
if True:
    print("This will be True")

for i in range(3):
    print(i)

if False:
    print("This won't print")

# Conditional Statements, Positive-Negative Number Program
x = -56
if x > 0:
    print("This is a positive Number")
else :
    print("This is a Negative Number")

# Conditional Statement for Even - Odd program
y = int(input("Enter a Number:"))
if (y % 2) == 0:
    print("Even Number")
else:
    print("Odd Number")

# To get the type of integer, float strig
print(type(49))
print(type(3.14))
a = 2
b = 3.14
c = "abc"
print(type(c))

# Multiline Statemets
s = 1+2+3+4+5+6\
    +1*2*3*4\
    -3+5-91
print(s)

s = {1+2+3+4+5+6.01
    +1*2*3*4}
print(s)

# 
"""
# Python has Dynamic Typing 
so no need to define variable type like (int, char, float etc)
int percentage
percentage = 80
"""
percentage = 80.04
print(percentage)

# Multiple way of making list and elemnts of list are in square brackets []
# List is Mutable i.e it can be modified, added or deleted etc. after they are created.

"""
Fruits = "Apple","Grapes","Mango","Pineapple"
Fruits = "Apple, Grapes, Mango, Pineapple"
Fruits = ["Apple","Grapes","Mango","Pineapple"]
"""
Fruits = ["Apple","Grapes","Mango","Pineapple"]
print(Fruits)

# List can contain "Hetrogeneous element" i.e (integer, floats, strings and even other lists or tuples).
# List is declared in Square Brackets [].
Fruit = [24, "Apple", 89, 84.16546, "Mango"] # Here are 5 elements in the stack (0-5).
print(Fruit)

# Indexing & Slicing (will teach later in 3rd class)

# Tuple is similar to list but, Tuple is immutable i.e its elements can not be altered once they are declared.
# Both are hetrogeneous. Tuple contain ordered elements.
# Elements of Tuple are presented in parentheses (), seperated by commas.
my_tuple = (1, 2, 3, 4)
print(my_tuple)

color = ("Indigo", "Green", "Blue")
print(color)

# Dictionaries:-
"""
1. It contains unordered collection of elements; each item stored in dicitioary has key & value, making it a key-value pair.
2. Dictionary is mutable i.e modify its elements once created.
3. Dictionary is created by placing items (key value pair) inside curly braces {}, seprated by commas.
4. Each item is a pair made up of a key & a value seprated by colon:.
 """
person = {"name": "Tom", "Roll No.": 896054, "number": 46, "whole numbers": (0,1,2,3,4,...), (1,2): [4,5,6,7,8]}
print(person)


# Important Program
name = input ("Enter your name ")
print(f"Hello! Welcome to our community, {name}") 

# Sets
""" 
! Sets contain unordered elements, but they don't have key values as dicitionary.
* SETs & Dictionary have unordered elements. Also Hetrogeneous.
* List & Tuple have ordered elements. Also Hetrogeneous.
"""
fruits = {"Cherry","Bananas","Apples","Grapes"}
S1 = {1,2,3,4,5}
S2 = {1,2,3,4,5,6,7,8}

S1 = {1, 2, 3, "Bananas"}
print(S1)

#! List is mutable that its elements can be updated:-
my_list = [1, 2, 3, 4]
my_list[3] = 552828
my_list.append("Apple")
print(my_list)
type(my_list)

# Dictionary
my_Dict = {"Car": "Bently", (1,2): (3, 9)}
print(my_Dict)
type(my_Dict)

#Sets
my_tuple = (1, "Apple", 3, "Car")
print(my_tuple)
type(my_tuple)

#! Tuple is Immutable
# my_tuple = (1, "Apple", 3, "Car")
# my_tuple[0] = 2828 #! Error : 'tuple' object does not support item assignment
# print(my_tuple)
# type(my_tuple)

thistuple = ("apple",)
print(type(thistuple))

#! NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

""" 
There are four collection data types in the Python programming language:
1. List is a collection which is ordered and changeable. Allows duplicate members.
2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
3. Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
4. Dictionary is a collection which is ordered** and changeable. No duplicate members.

*Set items are unchangeable, but you can remove and/or add items whenever you like.
**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
"""
