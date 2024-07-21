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

#! Practice (Functions)-9:
def greet(name):
    print(f"Hi, {name}")
greet("Ram")