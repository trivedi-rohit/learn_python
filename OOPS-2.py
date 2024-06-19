# # "del" Keyword 
# # del is use to delete object properties or object itself.
# class Student:
#     def __init__ (self, name):
#         self.name = name

# s1 = Student("Rohit")
# print(s1.name)
# del s1.name
# print (s1.name)


#! To make private attribute and method:
# Private attribute & methods are meant to be used only withinn the class and are not accessible from outside the class.
class Account:
    def __init__ (self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass #! to make attribute private use __acc_pass (2 underscore )

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345", "abcde")

print(acc1.acc_no)
print(acc1.reset_pass())


#! Private attribute and method
class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello person!")

    def welcome (self):
        self.__hello()

p1 = Person()

print(p1.welcome())

#! Inheritance - 
#? When one class(child/derived) derives the properties and methods of another class(parent/base).
'''
Types of Inheritance: 1. Single Inheritance  2. Multi-level Inheritance  3. Multiple Inheritance'''

#Single inheritance
class Car: #! Parent class
    color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("Car stopped")

class Toyota_car(Car): #! Child class (inheriting properties of parent)
    def __init__ (self, name):
        self.name = name

car1 = Toyota_car("Fortuner")
car2 = Toyota_car("pirus")

print(car1.name)
print(car1.color)
print(car1.start())

#! Multi Inheritance
class car:
    @staticmethod
    def start():
        print("Car Started..")

    @staticmethod
    def stop():
        print("Car Stopped.")

class Toyotacar(car):
    def __init__ (self, brand):
        self.brand = brand

class Fortuner(Toyota_car):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("EV")
car1.start()

#! Multiple Inheritance
class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A, B):
    varC = "Welcome to class C"

c1 = C() #Object

print(c1.varC)
print(c1.varB)
print(c1.varA)

#! Super Method - Use to access methods of parent class.
class Car:
    def __init__ (self, type): # define type in constructor
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stop")

class Toyotacar(Car):
    def __init__(self, name, type): # define name in this constructor.
        self.name = name
        super().__init__(type) # super() use to inherit the feature of parent class and define type here.
        self.name = name
        super().start()

car1 = Toyotacar("Pirus", "EV")
print(car1.type)

#! Class Method : A class method is bound to class & receives the class as an implicit first argument.
# Note: Static method can't access or modify class & generally for utlity.

class Person:
    name = "anonymous"

    def changeName (self, name):
        #self.name = name
        #Person.name = name
        self.__class__.name = "Rahul"

p1 = Person()
p1.changeName("Rohit Trivedi")
print(p1.name)
print(Person.name)

#! Property Decorator - we use @property decorator on any method in the class to use the method as property.
class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths

    @property
    def percentage (self):
        return str((self.phy + self.chem + self.maths) / 3) + "%"
    
stu1 = Student(98, 97, 99)
print(stu1.percentage)

stu1.maths = 50
print(stu1.percentage)

# Polymorphism (Operatot Overloading) - when the same operatior is allowed to have different meaninig according to the context. 

class complex:
    def __init__ (self, real, img):
        self.real = real
        self.img = img

    def showNum(self):
        print(self.real, "+", self.img,"i")

    # def add(self, num2):
    #     addreal = self.real + num2.real
    #     addimg = self.img + num2.img
    #     return complex(addreal, addimg)

    def __add__(self, num2):  #! Dunder function    
        newReal = self.real + num2.real
        newimg = self.img + num2.img
        return complex(newReal, newimg)

num1 = complex(3, 2)
num1.showNum()
num2 = complex(5, 3)
num2.showNum()
# res = num1.add(num2)
# res.showNum()
Res = num1 + num2
Res.showNum()

#Que #! Define a Circle class to create a circle with radius r using the constructor.
#! Define an Area() method of the class which calculates the area of the circle.
#! Define a Perimeter() of the class which allows you to calculate the perimeter of thec circle.
class Circle:

    def __init__(self, rad):
        self.rad = rad

    def area(self):
        print("Area = ", 22/7 * self.rad ** 2)
    
    def Peri(self):
        print("Perimeter = ", 2*(22/7)* self.rad)

radi = Circle(7)
radi.area()
radi.Peri()

#Que #! Define a Employee class with attributes role, department & salary. This class also has showDetails() method.
#! Create an Engineer class that inherits properties from Employee & has additional attributes: name and age.
class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("Role = ", self.role)
        print("Dept = ", self.department)
        print("Salary = ", self.salary)

class Engineer(Employee):
    def __init__(self, name, age): #! Again create constructor
        self.name = name
        self.age = age
        print("Name = ", self.name)
        print("Age = ", self.age)
        super().__init__("Engineer", "IT", "23,937") #! use super() to inherit properties of employee.

e1 = Employee("Accountant", "Finance", "60,000")
e1.showDetails()
Eng1 = Engineer("DJ Rajesh", 26)
Eng1.showDetails()

#Ques #! Create a class called Order which stores item & its price.
#! use Dunder function __gt__()to convey that:
# order1>order2 if price of order1>price of order 2.
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def showPrice(self):
        print("price of item is", self.price)

    def __gt__(self, itm2):
        return self.price > itm2.price

itm1 = Order("Tea", 45)
itm1.showPrice()
itm2 = Order("Cookies", 30) 
itm2.showPrice()
print(itm1 > itm2)
        