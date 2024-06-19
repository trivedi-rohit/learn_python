x = ('apple', 'banana', 'Cherry')
y = list(x)
y.append('papaya')
y[0] = 'king'
x = tuple(y)
print(x)


t1 = ('Orange', 'apple', 'Papaya', 'Coconut')
t2 = ('laughing Buddha',)
t1 += t2
print (t1)

# when variable are less than the number of items in the list,then use * before that varibale.

fruits = ("apple", "banana", "cherry",\
     "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

t = ('apple', 'Orange', 'Grapes')
for x in t:
    print(x)

s = {'apple', 'kiwi', 'banana', 'apple'}
s = {'apple', 'kiwi', 'apple', 'banana'}
print(s, t)

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

# Dictionary
dictn = {
    'brand': 'Ford',
    "Model": "Mustang",
    "Year": 1964
}
print(dictn)


#Dictionary contructor
f = dict(Name = 'Rahul', Age = 24, Nationality = 'India')
print(f)
x = f.keys()
print(x)

# Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

num1 = 5
num2 = 10
if num1>3 and num2 == 10:
  print("both are correct")
else:
  print ("one is wrong")


String1 = "GeeksForGeeks"
print("Initial String: ") 
print(String1) 
print("\nFirst character of String is: ") 
print(String1[11]) 
print("\nLast character of String is: ") 
print(String1[-8])

Tuple1 = tuple('Geeks') 
print("\nTuple with the use of function: ") 
print(type(Tuple1))
print((Tuple1))

coordinates = (3, 5) 
print(coordinates) 
print("X-coordinate:", coordinates[0]) 
print("Y-coordinate:", coordinates[1])

name = "Alice"
age = 30
print("My name is", name, "and I am", age, "years old.", end=" ")
print("Nice to meet you!")



print('G','F', sep='', end='')
print('G')
#\n provides new line after printing the year
print('09','12','2016', sep='-', end='\n')
  
print('Red','Green','Blue', sep=',', end='@')
print('geeksforgeeks')


# Python program to illustrate
# Finding common member in list
# using 'in' operator
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
for item in list1:
    if item in list2:
        print("overlapping")
    else:
        print("not overlapping")



def overlapping(list1, list2):
    c = 0
    d = 0
    for i in list1:
        c += 1
    for i in list2:
        d += 1
    for i in range(0, c):
        for j in range(0, d):
            if(list1[i] == list2[j]):
                return 1
    return 0
 
list1 = [1, 2, 7, 4, 5]
list2 = [6, 7, 8, 9]
if(overlapping(list1, list2)):
    print("overlapping")
else:
    print("not overlapping")

# Print None if key is not found in dictionary
my_dict = {"one": 1, "two": 2, "three": 3}

result4 = my_dict.get("three", None)
print(result4)

# Calculate the sum of the two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum_of_numbers = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_of_numbers}.") # Print the result

# Calculate the sum of the two numbers
a = input("Enter value of a:")
b = input("Enter value of b:")
add = float(a) + float(b)
print("The sum of a and b is ", add)

# Check eligibility to be a voter
age = float(input("Enter a number"))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Grading system
score = float(input("Enter your marks"))
if score >= 90:
    print('You got grade - A')
elif score >= 80:
    print("You got grade - B")
elif score >= 70:
    print("You got grade - C")
else:
    print("You got grade - D")

# Find the largest Number:
a = float(input("Enter value of a:"))
b = float(input("Enter value of b:"))
c = float(input("Enter value of c:"))
if a>=b and a>=c:
    score = a
elif b>=a and b>=c:
    score = b
else:
    score = c
print('The largest number is', score)

# Find the smallest Number:
a = float(input("Enter value of a:"))
b = float(input("Enter value of b:"))
c = float(input("Enter value of c:"))
if a<=b and a<=c:
    score = a
elif b<=a and b<=c:
    score = b
else:
    score = c
print('The smallest number is', score)

# Python program to find largest number in a list
# List of numbers
list1 = [10, 20, 20, 4, 45, 45, 45, 99, 99]
# Removing duplicates from the list
list2 = list(set(list1))
# Sorting the  list
list2.sort()
print(list2)
# Printing the second last element
print("largest element is:", list2[-1])

#! Pyhthon program to find second largest Number from the inputs:
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
if a >= b and a >= c:
    if b >= c:
        score = b
    else:
        score = c
elif b >= a and b >= c:
    if a >= c:
        score = a
    else:
            score = c
else : 
    if b >= a:
        score = b
    else: 
        score = a
    
print ("Second largest no. is", score)

# Make a calculator by taking input of 2 numbers and can perform operations of their choice
a = float(input("Enter a number for a : "))
b = float(input("Enter a number for b : "))
choice = input("chose type of operation : \n" 
                "1. Add \n"
                "2. Sub \n"
                "3. Div\n"
                "4. Mul\n")
if choice == "1":
    print(" The sum of digits is : ", (a+b) )
elif choice == "2":
    print(" The difference of digits is : ", (a-b))
elif choice == "3":
    if (b == 0):
        print ("The result is not defined")
    else:
        print(" The division of number is : ", (a/b))
elif choice == "4": 
    print(" The multiplication of digits is : ", (a*b))
else:
    print("Chose a correct operation")
#! GUI Calculator
# pip install tkinter
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

window = tk.Tk()
window.title('Calculator-GeeksForGeeks')
frame = tk.Frame(master=window, bg="skyblue", padx=10)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)


def myclick(number):
	entry.insert(tk.END, number)


def equal():
	try:
		y = str(eval(entry.get()))
		entry.delete(0, tk.END)
		entry.insert(0, y)
	except:
		tkinter.messagebox.showinfo("Error", "Syntax Error")


def clear():
	entry.delete(0, tk.END)


button_1 = tk.Button(master=frame, text='1', padx=15,
					pady=5, width=3, command=lambda: myclick(1))
button_1.grid(row=1, column=0, pady=2)
button_2 = tk.Button(master=frame, text='2', padx=15,
					pady=5, width=3, command=lambda: myclick(2))
button_2.grid(row=1, column=1, pady=2)
button_3 = tk.Button(master=frame, text='3', padx=15,
					pady=5, width=3, command=lambda: myclick(3))
button_3.grid(row=1, column=2, pady=2)
button_4 = tk.Button(master=frame, text='4', padx=15,
					pady=5, width=3, command=lambda: myclick(4))
button_4.grid(row=2, column=0, pady=2)
button_5 = tk.Button(master=frame, text='5', padx=15,
					pady=5, width=3, command=lambda: myclick(5))
button_5.grid(row=2, column=1, pady=2)
button_6 = tk.Button(master=frame, text='6', padx=15,
					pady=5, width=3, command=lambda: myclick(6))
button_6.grid(row=2, column=2, pady=2)
button_7 = tk.Button(master=frame, text='7', padx=15,
					pady=5, width=3, command=lambda: myclick(7))
button_7.grid(row=3, column=0, pady=2)
button_8 = tk.Button(master=frame, text='8', padx=15,
					pady=5, width=3, command=lambda: myclick(8))
button_8.grid(row=3, column=1, pady=2)
button_9 = tk.Button(master=frame, text='9', padx=15,
					pady=5, width=3, command=lambda: myclick(9))
button_9.grid(row=3, column=2, pady=2)
button_0 = tk.Button(master=frame, text='0', padx=15,
					pady=5, width=3, command=lambda: myclick(0))
button_0.grid(row=4, column=1, pady=2)

button_add = tk.Button(master=frame, text="+", padx=15,
					pady=5, width=3, command=lambda: myclick('+'))
button_add.grid(row=5, column=0, pady=2)

button_subtract = tk.Button(
	master=frame, text="-", padx=15, pady=5, width=3, command=lambda: myclick('-'))
button_subtract.grid(row=5, column=1, pady=2)

button_multiply = tk.Button(
	master=frame, text="*", padx=15, pady=5, width=3, command=lambda: myclick('*'))
button_multiply.grid(row=5, column=2, pady=2)

button_div = tk.Button(master=frame, text="/", padx=15,
					pady=5, width=3, command=lambda: myclick('/'))
button_div.grid(row=6, column=0, pady=2)

button_clear = tk.Button(master=frame, text="clear",
						padx=15, pady=5, width=12, command=clear)
button_clear.grid(row=6, column=1, columnspan=2, pady=2)

button_equal = tk.Button(master=frame, text="=", padx=15,
						pady=5, width=9, command=equal)
button_equal.grid(row=7, column=0, columnspan=3, pady=2)

window.mainloop()
'''****************************************************************'''
marks = [97.5, 93.5, 93.2, 96.6, 92.5, 83.7]
print(marks)
print(type(marks))
print(marks[2])

Student = ["Mohan", 94.4, 17, "DPS"]
print(Student)
Student[2] = 24
print(Student)

# student ="hello"
# students[1] = i
# print(student)

list_of_marks = [1, 2, 3, 1, 4, 1]
list_of_marks.insert(3, 7)
print(list_of_marks)

list_of_marks.reverse() #! It will reverse the original list.
print(list_of_marks)

list_of_marks.append(0)
print(list_of_marks)

print(list_of_marks.sort()) #! list_of_marks.sort() = will sort the list in """ accending order """ and it return """ none """ value.
print(list_of_marks)

list_of_marks.sort(reverse=True) #! Here this '''reverse=True''' so it will arrange in """ decending order """ & we did not print so '''none ''' will not display here.
print(list_of_marks)

list_of_marks = [1, 2, 3, 1, 4, 1, 9]
list_of_marks.remove(1) #! remove - it remove first element of the list.
print(list_of_marks)

list_of_marks = [1, 2, 3, 1, 4, 1, 9]
list_of_marks.pop(1) #! pop - it remove value at particular index.
print(list_of_marks)

tuple = ("hello",)
print(type(tuple))
print(tuple)

#! Exercise:
#  WAP to add or input any 3 movies in a list:
# //? Method -1
movie = []
mov1 = input("Enter movie 1 ")
movie.append(mov1)
mov2 = input("Enter movie 2 ")
movie.append(mov2)
mov3 = input("Enter movie 3 ")
movie.append(mov3)
print(movie)

#//? Method -2
movie = []
movie.append(input("Enter movie 1 "))
movie.append(input("Enter movie 2 "))
movie.append(input("Enter movie 3 "))
print(movie)

# //? Method -3
mov1 = input("Enter movie 1")
mov2 = input("Enter movie 2")
mov3 = input("Enter movie 3")
a = [mov1, mov2, mov3]
print(a)
print(type(a))

# WAP to check if a list contains a palindrome of elements. (hint: use copy() method)
list1 = ["R", "A", "C", "E", "C", "A", "R"] #! Palindrome eg. = 121, 123 is not a palindrom, 77, racecar, dad, divid etc.
copy_list = list1.copy()
copy_list.reverse()
if (list1 == copy_list):
    print('Pallindrome')
else:
    print("Not a Pallindrome")

# WAP to count the numeber of students with grade 'A' in the following tuple:
grade = ("c", "D", "A", "A", "B", "B", "A")
# print(type(grade))
print(grade.count("A"))
my_list = list(grade)
my_list.sort()
print(my_list)
# print(type(my_list))
#! ****************************************************************************************************************************




 
