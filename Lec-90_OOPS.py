# **** Learn : How add attributes in class. (what object has)****
# Class -> Instructor & oject ->Instructor_1; 
'''
class Instructor:
    #pass
    print("Hello!")

instructor_1 = Instructor()
instructor_1.name = 'Raja'
instructor_1.city = 'Delhi'
print(type(instructor_1))
print(instructor_1.name)

instructor_2 = Instructor()
instructor_2.name = 'Kanupriya'
instructor_2.city = 'Chennai'
print(type(instructor_2.city))
print((instructor_2.name))
'''

#! To avoid writing multiple object for multiple instructor, 
'''
Then class comes in pricture, we use 'constructor'; - 
Constructor is use to initialise the data members (attributes of that particular object) to assign values to the data members of a class when an object is created.
In other words, constructor will allow us to specify what would happen when we creat a object.
#? __init__(self) function will be called every time for every newly created objectw.
'''
class Instructor:
    #followers = 0 #? if all insttructor has zero followers.
    def __init__(self,name, city,ins_followers):
        # print("Hello!")
        self.ins_name=name
        self.ins_city=city
        self.insta_follower = ins_followers

instructor_1 = Instructor('Rohit','Lucknow',53)
print(instructor_1.ins_name)
#print(instructor_1.followers)
print(instructor_1.insta_follower)

instructor_2 = Instructor('Ashok','Delhi',0) # can't be left emptied
print((instructor_2.ins_name))
print(instructor_2.ins_city)
print(instructor_2.insta_follower)