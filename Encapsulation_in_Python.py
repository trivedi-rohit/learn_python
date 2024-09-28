#Encapsulation (getter & setter method)
# Getter Method - to get private data & Setter Method - Is to set/modify the values.
class Student:
    def __init__(self,name,rollNo,age):
        self.name = name            # Public Instance Variable
        self._rollNo = rollNo       # Protected Instance Variable (Use within class & drived class)
        self.__age = age            # Private instance variable
    
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>35:
            print("Invalid Age; it should be less than 35.")
        else:
            self.__age = age
    
    # def __display(self):
    #     print(f"Hi I'm {self.name}, age is {self.__age} and having roll no. {self._rollNo} from Student class")
    # def displayPrivateData(self):
    #     self.__display()

# Derived Class: It can access to protected data      
# class Branch(Student):
#     def show(self):
#         print(f"My roll no. is {self._rollNo}")

# b1=Branch("Nish",23,22)
# b1.show()
# def show_Details():
#     b1 =Branch("Rohit",26)
#     print(b1.name)
# show_Details()

s1 = Student("Rahul",21,20)
print(s1.get_age())
s1.set_age(36)
print(s1.get_age())
# s1._Student__age = 45
# print(s1._Student__age) 

