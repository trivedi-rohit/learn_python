num = input("Enter list of numbers : ")
split_num = num.split()
count = 0
for i in split_num:
    count += 1
for i in range(0,count):
    split_num[i] = int(split_num[i])
max_numbr = split_num[0]
for number in split_num:
    if number > max_numbr:
        max_numbr = number
print(f"The maximum number is : {max_numbr}")

#! Method -2
num = input("Enter list of numbers : ")
split_num = num.split()
split_num.sort()
print(f"The maximum number is = {split_num[-1]}")