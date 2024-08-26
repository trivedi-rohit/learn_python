class Human (object):
    def __init__(self,name,age): # instance method (__init__), taking 2 argument name & age.
        print("calling __init__ from Human class.")
        self.name = name # attributes/parameter
        self.age = age # attributes

    def showDetails (self):
        print(f"Name : {self.name}, Age : {self.age}")

    def eat(self):
        print("I can eat.")

class Male (Human):
    def __init__(self,M_name,M_age,location): # defined new argument location in Male class.
        print("calling __init__ from Male class.")
        Human.__init__(self,M_name,M_age) # used the argument of Human class
        self.location=location

    def sleep (self):
        print("I can sleep whole day.")
'''
Since there is no relation or interdependenc of male class or female class on each other, therefore attributes & methods can not be accesso of each other.
But, both can access properties of Human class.
'''
class Female (Human):  
    def __init__(self,F_name,F_age,can_dance):
        print("Calling __init__ from Female class.")
        super().__init__(F_name,F_age)
        self.know_dance = can_dance
    def showDetails(self):
        print(f"Know Dancing : {self.know_dance}")
        return super().showDetails()    
        
    def work (self):
        print("I can code.")

female_1 = Female("Rachna", 30, True)
female_1.eat()
print(female_1.name)
female_1.showDetails()
print(female_1.age)

# male_1 = Male("Jagdeep",30,"Haryana")
# print(Male.mro())
# male_1.sleep()
