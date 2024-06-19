# Python Built-in Data Types:
""" 
Python has the following data types built-in by default, in these categories:

Text Type:	    str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	    set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	    NoneType
"""
# You can get the data type of any object by using the type() function:
x = 5
print(type(x))

"""
Example	                                           Data Type	
x = "Hello World"	                                str	
x = 20	                                            int	
x = 20.5	                                        float	
x = 1j	                                            complex	
x = ["apple", "banana", "cherry"]	                list	
x = ("apple", "banana", "cherry")	                tuple	
x = range(6)	                                    range	
x = {"name" : "John", "age" : 36}	                dict	
x = {"apple", "banana", "cherry"}	                set	
x = frozenset({"apple", "banana", "cherry"})	    frozenset	
x = True	                                        bool (True/False)	
x = b"Hello"	                                    bytes	
x = bytearray(5)	                                bytearray	
x = memoryview(bytes(5))	                        memoryview	
x = None	                                        NoneType	

"""
# Setting the Specific Data Type
"""
Example	                                       Data Type	
x = str("Hello World")	                         str	
x = int(20)	                                     int	
x = float(20.5)	                                 float	
x = complex(1j)	                                 complex	
x = list(("apple", "banana", "cherry"))	         list	
x = tuple(("apple", "banana", "cherry"))	     tuple	
x = range(6)	                                 range	
x = dict(name="John", age=36)	                 dict	
x = set(("apple", "banana", "cherry"))	         set	
x = frozenset(("apple", "banana", "cherry"))	 frozenset	
x = bool(5)	                                     bool	
x = bytes(5)	                                 bytes	
x = bytearray(5)	                             bytearray	
x = memoryview(bytes(5))	                     memoryview

# Note: You cannot convert complex numbers into another number type.
"""
# Random Number
"""
Python does not have a random() function to make a random number, 
but Python has a built-in module called random that can be used to make random numbers:
"""
# Import the random module, and display a random number between 1 and 9:
import random
print(random.randrange(1, 10))

# Get the first character of the string txt.
txt = "Hello World"
x = txt[0]

# Get the characters from index 2 to index 4 (llo).
txt = "Hello World"
x = txt[2:5]

# Return the string without any whitespace at the beginning or the end.
txt = " Hello World "
x = txt.strip()

# Replace the character H with a J.
txt = "Hello World"
txt = txt.replace("H", "J")

# Insert the correct syntax to add a placeholder for the age parameter.
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# Use the correct membership operator to check if "apple" is present in the fruits object.
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit!")

# You can assign a multiline string to a variable by using three quotes:
a = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings are Arrays
'''
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.

Get the character at position 1 (remember that the first character has the position 0):
'''
a = "Hello, World!"
print(a[7])
print(len(a)) # string length of 'a'

# Looping Through a String
# (Since strings are arrays, we can loop through the characters in a string, with a for loop.)
# Loop through the letters in the word "banana":
for x in "banana":
  print(x)

# Check String
''' To check if a certain phrase or character is present in a string, we can use the keyword in.'''
# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)

# Use it in an if statement:
# Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# Check if NOT
'''To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.'''
# Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)

# print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# Python - Slicing Strings
'''
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

Note: The first character has index 0
'''
# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

# Slice From the Start
# By leaving out the start index, the range will start at the first character:
# Ex. - Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:8])

# Get the first character of the string txt.
txt = "Hello World"
x = txt[0]

# Slice To the End
# By leaving out the end index, the range will go to the end:
# Ex. Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])

list_of_marks = [2, 3, 4, 1]
list_of_marks.reverse() #! It will reverse the original list.
print(list_of_marks)
list_of_marks.append(5)
print(list_of_marks)
print(list_of_marks.sort()) #! List_of_marks.sort() = will sort the list in accending order and it return """ none """ value. (sorting will be applicable for character also)
print(list_of_marks)
list_of_marks.sort(reverse=True) #! Here this '''reverse =True''' so it will arrange in decending order & we did not print so '''none ''' will not display here.
print(list_of_marks)

# Strings are Arrays
'''
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.
# Get the character at position 1 (remember that the first character has the position 0):
'''
a = "Hello, World!"
print(a[1])

# Negative Indexing
''' 
Get the characters:
From: "o" in "World!" (position -5)
To, but not included: "d" in "World!" (position -2):
'''
# Use negative indexes to start the slice from the end of the string:
b = "Hello, World!"
print(b[-5:-2])

# To get the upper case of all letter
Hi = 'Hello Boss!'
print(Hi.upper()) # To print all letter of variable Hi in Upper case.
print(Hi.lower()) # To print all letter of variable Hi in lower case.

# Remove Whitespace
'''Whitespace is the space before and/or after the actual text, and very often you want to remove this space. '''
# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Replace String
# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String
'''The split() method returns a list where the text between the specified separator becomes the list items.'''
# The split() method splits the string into substrings if it finds instances of the separator:
a = "Mohan, is, a, good, boy"
print(a.split(",")) # ['Mohan', ' is', ' a', ' good', ' boy']

# To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#! The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = input("Enter the Quantity")
item_No = input("Enter the Item No.")
price = input("Enter the Price")
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, item_No, price))

# Escape Character
''' 
To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to insert.
An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
'''
txt = "We are the so-called \"Vikings\" from the north."
print(txt) 



#All String Methods:
'''
Method	             Description
capitalize()       	Converts the first character to upper case
casefold()	        Converts string into lower case
center()	          Returns a centered string
count()	            Returns the number of times a specified value occurs in a string
encode()	          Returns an encoded version of the string
endswith()	        Returns true if the string ends with the specified value
expandtabs()	      Sets the tab size of the string
find()	            Searches the string for a specified value and returns the position of where it was found
format()	          Formats specified values in a string
format_map()	      Formats specified values in a string
index()	            Searches the string for a specified value and returns the position of where it was found
isalnum()	          Returns True if all characters in the string are alphanumeric
isalpha()	          Returns True if all characters in the string are in the alphabet
isascii()	          Returns True if all characters in the string are ascii characters
isdecimal()	        Returns True if all characters in the string are decimals
isdigit()	          Returns True if all characters in the string are digits
isidentifier()	    Returns True if the string is an identifier
islower()	          Returns True if all characters in the string are lower case
isnumeric()       	Returns True if all characters in the string are numeric
isprintable()     	Returns True if all characters in the string are printable
isspace()	          Returns True if all characters in the string are whitespaces
istitle()         	Returns True if the string follows the rules of a title
isupper()         	Returns True if all characters in the string are upper case
join()	            Converts the elements of an iterable into a string
ljust()	            Returns a left justified version of the string
lower()	            Converts a string into lower case
lstrip()            Returns a left trim version of the string
maketrans()       	Returns a translation table to be used in translations
partition()       	Returns a tuple where the string is parted into three parts
replace()	          Returns a string where a specified value is replaced with a specified value
rfind()	            Searches the string for a specified value and returns the last position of where it was found
rindex()          	Searches the string for a specified value and returns the last position of where it was found
rjust()	            Returns a right justified version of the string
rpartition()	      Returns a tuple where the string is parted into three parts
rsplit()	          Splits the string at the specified separator, and returns a list
rstrip()	          Returns a right trim version of the string
split()	            Splits the string at the specified separator, and returns a list
splitlines()      	Splits the string at line breaks and returns a list
startswith()	      Returns true if the string starts with the specified value
strip()	            Returns a trimmed version of the string
swapcase()         	Swaps cases, lower case becomes upper case and vice versa
title()           	Converts the first character of each word to upper case
translate()       	Returns a translated string
upper()	            Converts a string into upper case
zfill()            	Fills the string with a specified number of 0 values at the beginning
'''
#! Escape Character
# Code	               Result	
# \'	               Single Quote	
#\\	                 Backslash	
# \n	               New Line	
# \r	               Carriage Return	
# \t	               Tab	
# \b	                Backspace	
# \f	               Form Feed	
# \ooo	             Octal value	
# \xhh	             Hex value
