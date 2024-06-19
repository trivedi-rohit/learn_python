# ! Dictionary:
# They are unordered, mutable and don't allow duplicates.

info ={
    "Name" : "Rohit Trivedi", "Age" : 31,
    "Qualification" : (12, 'B.Tech', "M.B.A"),
    "Company" : ["HCL Technologies", "Infosys"],
    "Is Adult" : True,
    "Language" : {"Jave", "Python", "Data Science"}
}
info['Name'] = "Mohit"
info['Surname'] = "Trivedi"
print(info)
print(info["Name"])                   # print infomation from dictionary using its keys
print(info["Is Adult"])               # print infomation from dictionary using its keys

# Modify a blank dictionary:
dict = {}                             # Created a blank dictionary
print(dict)
dict['name'] = 'Rohit'                # Add 2 keys 'name' & 'surname'
dict['Surname'] = 'Trivedi'
print(dict)

#! Nested Dictionaries
Student = {
    "Name" : "Rohit",
    "Score" : {
        "Phy" : 98,
        "Chem" : 94,
        "Math" : 100,
    }
}
print(Student["Score"]["Phy"])         #! Imp: To print marks of phy.

# #! Methods in Dictionaries:
# 1. myDict.keys() # return all keys
myDict = {
    "Name" : "Rohit",
     "Marks" :{
        "Math" : 98,
        "English" : 92,
        "Chem" : 99,
        "Phy" : 100,
    }
}
print(myDict.keys())
print(list(myDict.keys()))     #! Typecast dictionaries "keys" in list

# 2. myDict.values() # returns all values
print(myDict.values())
print(list(myDict.values()))  #! Typecast dictionaries "values" in list

# 3. myDict.items()  # returns all (key, val) pairs as tuples
print(myDict.items())
pairs = list(myDict.items())  #! Typecase dictionaries to list
print(pairs[0])               #! Print pair first having index 0.

# 4. myDict.get("key") # returns the key according to value

print(myDict['Name'])
print(myDict.get('Name'))

#! SO, If we put any key not present in dictionary the 1st one will generate error but 2nd one will give 'None'.
# 1.   print(myDict['Name2'])
# 2.   print(myDict.get("Name2"))

# 5. myDict.update(newDict) # insert the specified items of the dictionary
""" myDict.update({"City" : "Delhi", "Age" : 16})
    print(myDict) """  # Also (Method -2)

newDict = {"City" : "Delhi", "Age" : 16}
myDict.update(newDict)
print(myDict)

# WAP to store the following word meaning in a python dictionary
""" 
table : "a piece of furniture", "list of facts & figures"
cat : "a small animal"
 """
dicto = {"table" : ("a piece of furniture", "list of facts & figure"),   #! To print 2 value of 1 key, we can use list or tuple
         "cat" : "a small animal"}
print(dicto)

# WAP to enter marks of 3 subjects from user and store them in an empty dictionary one by one, using their subjects as key & marks as value.

dictn = {}
a = float(input("Enter Maths marks : "))
dictn.update({"Maths" : a})
b = float(input("Enter Maths Phy : "))
dictn.update({"Phy" : b})
c = float(input("Enter Maths Chem : "))
dictn.update({"Chem" : c})
print(dictn)

# Figure out ways to store 9 & 9.0 as seprate values in the set. 
store = set()
x = 9
y = "9.0"
store.add(x)
store.add(y)
print(store)
