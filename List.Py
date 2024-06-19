# List is mutable & allow duplicate. Also, ordered (i.e. order will not chamge)
# List is indexed, can have items with same value
# If you add new items to a list, the new items will be placed at the end of the list.

points = [9, 1, 4, 2, 9, 7, 8, 9, 3, 1, 9, 3, 7, 9, 1, 2]
x = points.count(9)
print(x)

fruits = ["cherry", "apple", "banana", "cherry", "banana", "banana", "banana", "cherry", "cherry"]
x = fruits.count("cherry")
print(x)


fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)