# While loop
i = 0                       # initionalize the counter.
while i <= 9:
    print("hello", i)       # print hellow and no. of times loop worked. 
    i +=  1                 # increase the counter by 1.
print(i)                    # Print total no. of count.

# WAP to print number 1 to 5.
i = 1
while i <= 5:
    print(i)
    i += 1
print("Loopend")

# WAP to print 10 to 1 in reverse.
i = 10
while i >= 1:
    print(i)
    i -= 1

# Q1. WAP to print number from 1 to 100.
i = 1
while i <= 100:
    print(i)
    i += 1
print("Loop End")

# Q2. WAP to print number from 100 to 1.
i = 100
while i >= 1:
    print(i)
    i -= 1 
print("Loop End")

# Q3. WAP to print a table of number n:
i = int(input("Enter a number to get its table: "))
v = 1
while v <= 10:
    print(i*v)
    v += 1

#! Q4. WAP the elements of following list using a loop:
ilist = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

indexx = 0                               # initialize the index of the list
while indexx < len(ilist):               # running a loop value less than length of list. Length of list = 10 & indexes are from 0 to 9.
    print(ilist[indexx])
    indexx += 1

# Q5. WAP to search for a number x in this tuple using loop:

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 49     # search the number x in tuple
idx = 0   # initialize the index.
while idx < len(tup):        # index value will increase till less than len(tup)[lenth of tuple].
    if (tup[idx] == x):      # tuple index equal to number, then print the number found at particular index.
        print("the number found at index :", idx)
    else:
        print("finding... Please wait")
    idx += 1


# print till i == 3 then """ break """.

i = 1
while i <= 5:
    print(i)
    if (i == 3):
        break
    i += 1

# Use of """ continue """ in loops:
i = 0
while i <= 5:
    if (i == 3):
        i += 1
        continue
    print(i)
    i += 1

# Check at odd place 
i = 0
while i <= 10:
    if (i % 2 == 0):
        i += 1
        continue
    print(i)
    i += 1

# Use of for loop:
list = ["Hello", 2, 3, 4, 5]
for x in list:
    print(x)

# Print character of string:
list = "Hello Mr. Lobo" # String 
for i in list:
    print(i)

#! Use for & else; find character "o" in a string and the print "found"

I = "Mango is tasty"
for char in I:
    if (char == "o"):
        print ("Found")
        break
    print(char)
else:
    print("end")

# WAP to print the elements of the following list using loops: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
lil = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36]
for x in lil:
    print(x)

#!0 WAP to search a number x in this tuple using loop:
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)
x = 36
idx = 0
for i in tup:
    if (i == x):
        print("Number found at index :                              ", idx) 
        # break    # if u want to break an operation after 1st result found.
    idx += 1  
else:
    ("Not found")

# Range()
""" 
Range function returns a sequence of numbers, starting from 0 by default, and increments by 1(by default), and stop before a specified number.
range(start, stop, step)
eg print(range(5))-----> Ans = range(0, 5)
here, start = 0, stop = 5, step = 1. #{Star & step values are optional}
 """
print(range(5))
rag = range(10)
for i in rag:
    print(i)

# code
for i in range(2, 10): #! start value will be included but ending value will be excluded in result.
    print(i)

# code (Print even number in series):
for i in range(2, 10, 2):               # (start, stop, step)
    print(i) 

# code (Print odd number in series):
for i in range(1, 10, 2):
    print(i)
# Code (Print number 100 to 0)
for i in range(100, 0, -1):
    print(i)

# WAP to print multiple of any number(n) using range:
n = int(input("Enter a number : "))
for i in range(1, 11):
    print(i*n)

# pass statements
# pass is a null statement that does nothing. It is used as a placeholder for future code.
""" 
for el in range(10):
    pass
print("some useful works") """

# WAP to find the sum of first n numbers. (using while loop).
n = int(input("Enter the number : "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print('Total Sum = ', sum) 

# WAP to find the sum of first n numbers. (using for loop).

n = int(input("Enter the value of n : "))
sum = 0
for i in range (1, n+1):
    sum += i
print("Total sum =", sum)

# WAP to find the factorial of first n number (using for loop):
n = int(input("Enter a number"))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial of given number  is : ", fact)

# WAP to find the factorial of first n number (using while loop):
n = int(input("Enter the number : "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print('Factorial of number = ', fact) 

