# f1=open("file_1.txt","w+")
# print(f1.tell())
# f1.write("Hello")
# print(f1.tell())
# print(f1.read())
# print(f1.tell())
# # data = f1.write("Hi this is new text")
# # print(data)

#*****************************************************************************

# f1 = open("file_1.txt","w+")
# print(f1.tell())
# f1.write("Hello, welcome")
# print(f1.tell())
# f1.write("This is a python course.")
# print(f1.tell())
# f1.seek(3) # change cursor/pointer position to the begining.
# print(f1.tell())
# data = f1.read()
# print(data)
# print(f1.tell())
# f1.close()

#********************************************************************************
# # Append:
# f1 = open("file_1.txt", "a+") # " a+ " = append and read
# print(f1.tell())
# f1.seek(0)
# f1.write("Hello ALL")
# f1.read()
# print(f1.seek(0))
# print(f1.read())

#*********************************************************************************
# Handling Binaries (Images, videos ,etc)
f1 = open("D:\wbc.txt", "a+")
#print(f1.tell())
f1.seek(0)
# f1.write("Hello ALL")
# f1.read()
# print(f1.seek(0))
print(f1.read())
#***********************************************************************************
f2 = open("Schedule.jpg","rb")
f3 = open("Schedule_MBA.webp", "wb")
for i in f2:
    f3.write(i)
print(f2.read())