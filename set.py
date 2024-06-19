#! Sets
""" 
Sets is a collection of the unordered items. 
#! Set is mutable. But, Each element in sets must be unique and immutable. 
So, string, tuple (1,), Boolean can be stored in list, but list & dict can not be stored in set b'cos they are immutable.
nums = {1, 2, 3, 4}
Set2 = {1, 2, 1, 2} 
{1, 2} # Repeated elements sorted only once. so it resolved.
null_set = set() #! empty set syntax
 """
collection = set()
print(type(collection))
collection.add("Name",) # set.add() takes only 1 argument.
collection.add(6)
collection.add((4, 6, 5))
collection.add(("Quarter"))
print(collection)
collection.remove("Name")
print(collection)

set1 = {1, 2, 3, "hello", 96.8, 4, 5, "World"}
set2 = {4, 5, 'world', 1, "santa", "Banta"}
print(set1.union(set2))        # Union of set1 & set2
print(set2.intersection(set1)) # intersection of set1 and set2

