# a = input("what is your name")
# print("Hello",a)

# f = open("detmo.txt", "x")
# data = f.write("I want lean java\n This is a Python file.")
# print(data)
# f.close()

#! Moddule
# WAP to create a "practice.txt" file and print data in it.
f = open("practice.txt", "x")
data = f.write("Hi everyone\nWe are learning File I/O\n")
data = f.write("using Java.\nI like programing in Java.")
print(data)
f.close()

#! Module
# import os
# os.remove("practice.txt")

#! Module 
# WAP a program and replace "Java" with "python" in previously created file.

with open ("practice.txt", "r") as f:
    data = f.read()
    
new_data = data.replace("Java", "Python")
print(new_data)

with open ("practice.txt", "w") as f:
    data = f.write(new_data)

# WAP to find the location of word in the previously created file:

with open("practice.txt", "r") as f:
    data = f.read()

few_data = data.find("everyone")
print(few_data)

#! Find the word if "learning" exist in the previously created file.
word = "learning"
with open("practice.txt", "r") as f:
    data =  f.read()
    if (data.find(word) != -1):
        print("Found")
    else:
        print("Notfound")

# WAP to creat above check as function:
def Check_for_words():
    word = "Javascript"
    with open("practice.txt", "r") as f:
        data =  f.read()
        if (data.find(word) != -1):
            print("Found")
        else:
            print("Notfound")

Check_for_words ()

#! WAP to find in which line of the file does the word "learninng" occurs first
# Print -1 if word not found

def check_for_line():
    word = "learning" 
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print(line_no)
                return
            line_no += 1
    return -1

print(check_for_line())

# From a file containing numbers separated by comma(,); print the count of even numbers.
count = 0
with open("practice.txt", "r") as f:
    data = f.read()
    # print(type(data))
    # print(data)
'''
    num = ""                   # number is intialized with empty string.
    for i in range(len(data)): # run a loop till the length of data.
        if (data[i] == ","):
            print(int(num))     # convert to integer and print the number.
            num = ""            # Again, empty the string.
        else:
            num += data[i]      # increase the number with data having in range as i moves.  
'''
nums = data.split(",")
# print((nums))
for val in nums:
    if (int(val) % 2 == 0):
        print(val)
        count += 1

print(count)
