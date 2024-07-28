# Add without using sum 1 to 100.
count = 0
for i in range(1,101):
    count += i
print(count)

# Find sum of even numbers from 1 to 100 (including 1 to 100).
sum = 0
for i in range (0,101,2):
    sum += i
print(sum)

# FizzBuzz Job Interview question:
''' 
Rule:
For numbers 1 to 100,  
1. The number divisible by 3 print Fizz.
2. The number divisible by 5 print Buzz.
3. The number divisible by 3 & 5 print FizzBuzz.
'''
for i in range(1,101):
    if (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif (i % 5 == 0):
        print("Buzz")
    else:
        print(i)

## count = 1
# while count <= 5:
#     print(count)
#     count += 1
#     if count == 3:
#         break
# else:
#     print("In Else Block")

# Practice - 1: 
count =1
while count < 1:
    print(count)
    count += 1
else:
    ("In else statement")
print("Out from loop")

#! Practice - 2:
count =1
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break
else:
    ("In else statement")
print("Out from loop")

#! Practice - 3:
number = int(input("Enter number (-1 to Quit)"))
while number != -1:
    print(number)
    number = int(input("Enter number (-1 to Quit)"))
else:
    print("In else loop")
print("Out for loop")

#! Practice - 4:
count = 0
while True:
    print(count)
    count += 1
    if count == 5:
        break
else:
    print("In else loop")
print("Out from loop")

#! Practice - 5:
total = 0
num = int(input("Enter a number (0 to Quit) : "))
while num != 0:
    total += num
    num = int(input("Enter a number : "))
print(f"Total is {total}")

#! Practice - 6: 
count  = 1
while count <= 10:
    print(count)
    count += 1
    if count == 7:
        break
    print("Hi")
print("Out form loop")

#! Practice - 7:
list1 = ["Hi", "Hello", "Hi!"]
name = ["Ram", "Shayam", "Rohit"]
for i in list1:
    for j in name:
        print(i,j)
        if (i == "Hi" and j == "Shayam"):
            break
    print("out from internal loop")
print("Quit") 

#! Practice - 8:
count = 0    
while count <= 5:
    print(count)
    count+=1   
    if count == 4:
        continue
    print("Hello")
print("Quit")

#! Practice (Functions)-1:
def greet(name):
    print(f"Hi, {name}")
greet("Ram")

#! Functions - 2
def greet (name,dept, college = "BBDNIIT"):
    print(f"Hi Mr.{name}, you are alloted to {dept} department in college {college}.")
greet('Raj', 'ECE')
greet(name ='Mohak', dept ="CS")
greet('Ankita', dept = 'IT')
greet("Rajhanse", "EE", college = "IIT-Patna")

#! Function (*arg) (Arbitary argument):
def sum(*numbers):
    c = 0
    for i in numbers:
        c += i
    print(f"The sum is {c}")
sum(5,7,9.10,11,12.5,13.2)

#! *Args multiplication:
def mul(*args):
    c=1
    for i in args:
        c *= i
    print(f"sum is = {c}")
mul(2,3,-6,8)
mul(2,5,8,9,0,6)

#! Functions (**Kwarg- Keyword Argument): 
def persons_info(**information):
    for key,value in information.items():
        print(key,value)
persons_info(name = "Ram", age=30, dept = "CSE")
persons_info(name = "Shyam", dept = "ECE")

#! Use of arg befor kwarg, otherwise give error:
def persons_info(*args, **information):
    c=0
    for i in args:
        c+= i
    print(f"sum is = {c}")
    for key,value in information.items():
        print(key,value)

persons_info(74,2,9,5,Name = "Ram", Age = 30, Dept = "CSE")
persons_info(5,7,2, Name = "Shyam", Dept = "ECE")

#! Find Factorial
def factorial(num):
    if num < 0:
        print(f"Factorial of {num} can't be determined.")
    elif (num ==1 or num == 0):
        return 1
    else:
        return num*factorial(num-1)
number = int(input("Enter a number : "))
# print("Factorial of", number, "is", factorial(number))
print(f"Factorial of {number} is {factorial(number)}")

# Find if number is prime number or not.
#! Method -1 
import math
def prime (n):
    if n>1:
        my_prime = True
        # for i in range(2, n):
        for i in range(2, math.ceil(n/2)+1):
            if n % i == 0: 
                my_prime = False
        if my_prime == True:
            print("Given number is a Prime Number")   
        else:
            print("Not a prime number") 
    else:
        print("Not a prime number")    
num = int(input("Enter a number : "))
prime(num)

#! Title case:
def format_name(f_name, l_name):
    first=f_name.title()
    last=l_name.title()
    print(f"{first} {last}")
    return (f"{first} {last}")
format_name("rohit","TRIVEDI") #Rohit Trivedi # (print)
print(format_name("rohit","TRIVEDI")) # (print)
formatted=format_name("rohit","TRIVEDI") #!
print(formatted) #!

#! stats function use & return value
import statistics
def list(list1):
    return statistics.mean(list1), statistics.median(list1), statistics.mode(list1)
mean, median, mode = list([3,5,45,3,2,1,89])
print(f"The value of mean, median, mode are {mean}, {median}, {mode} respectively.")

#! Method -1:
def format_name(fname, lname):
    if fname=="" and lname=="":
        return "Enter valid name"
    else:
        return (f"{fname.title()} {lname.title()}")
    
print(format_name ("rohit","Trivedi"))

#! Method -2:
def format_name(fname,lname):
    if fname=="" and lname=="":
        return "Enter a valid name"
    else:
        return fname.title(),lname.title()
        
fname=input("Enter first name : ")
lname=input("Enter last name : ")
result=format_name(fname,lname)
print(result)