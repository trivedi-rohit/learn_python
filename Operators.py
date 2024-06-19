# Arithmetic Operator
a = 7
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a ** b) # Exponential Operator
print(a / b)
print(a // b) # Floor Division (Quotient)
print(a % b) # Modulo (Remainder)

#Comparision Operator
print(a == b) # a equal to b
print(a != b) # a not equal to b
print(a > b) # a greater than b
print(a < b) # a less than b
print(a >= b)
print(a <= b)

#Logical Operator/boolean Operator
""" 1. and 2. or 3. not """
t = 8
print(t>3 and t<10) # Incase of AND, compiler will check for both statement true or not.
print(t>9 or t<6) # Incase of OR, compiler will check for both statemetns if either of the statements are true then result will be true.
print (not(t>9 or t<6))

# Bitwise Operator(Binary No.)


# Identity Operators
""" 
1. is    2. is not
1. is => x is y # Returns True if both variables are the same object
2. is not => x is not y # Returns True if both variables are not the same objec
 """
 
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have the same content

print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

print(x is not z)
# returns False because z is the same object as x

print(x is not y)
# returns True because x is not the same object as y, even if they have the same content

print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

