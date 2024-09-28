""" 
Access Specifiers are of 2 Types:
1. Public 2. Private 3. Protected
No symbol to define Public attribute/methods
for Potected attribute use single Underscore (_).
"""
class Student:
    def __init__(self,name,rollNo,age):
        self.name = name            # Public Instance Variable
        self._rollNo = rollNo       # Protected Instance Variable (Use within class & drived class)
        self.__age = age            # Private instance variable
    def __display(self):
        print(f"Hi I'm {self.name}, age is {self.__age} and having roll no. {self._rollNo} from Student class")
    def displayPrivateData(self):
        self.__display()
class Branch(Student):
    def show(self):
        print(f"My roll no. is {self._rollNo}")

# b1=Branch("Nish",23,22)
# b1.show()
# def show_Details():
#     b1 =Branch("Rohit",26)
#     print(b1.name)
# show_Details()

s1 = Student("Rahul",21,20)
# s1.name="Jaideep"
# s1._rollNo=42
# s1.displayPrivateData()
print(s1._Student__age)
s1._Student__display()
# print(s1.name)
# s1.display()