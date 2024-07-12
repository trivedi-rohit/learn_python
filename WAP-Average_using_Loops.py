# WAP to find average using for loop (without sum & len function) & take input from user.
#! Method - 1
# height = input('Enter all heights seprated by space:')
# list_height = height.split()
# # print(list_height)
# count = 0
# for k in list_height:
#     count = count+1
# # print(count)
# for i in range (0,count):
#     list_height[i] = float(list_height[i])
# sum = 0
# for person in list_height:
#     sum = sum + person
# avg = sum/count
# print(avg)
# print(round(avg))

#! Method - 2
# print("Enter height seprated by space:")
# a = (input()).split()
# sum = 0
# count = 0
# for i in a:
#     sum += float(i)
# for i in a:
#     count = count+1
# print(sum/count)
# print(f" The average height is  {round(sum/count)}") 

#! Method - 3
# heights = input("Enter height (in floating point) seprated by space: ").split(" ")
# sum = 0
# count = 0
# for i in heights:
#     count += 1
# for i in heights:
#     sum += float(i)
# # print(sum // count)
# print(f"The average height of students = {round(sum/count)}")

#! Method - 4
# height = input("Enter heights separated by space:").split()
# sum = 0
# count = 0
# for i in height:
#     i = float(i)
#     sum += i
#     count = count+1
# print(round(sum/count))

#! Method - 5
height = input("Enter the heights separate with comma(,) : ")
height = height.split(',')
# count = height.count(',')+1
count = height.count(',')+1
total = 0
for i in height :
    total += float(i)
print(round(total/count))