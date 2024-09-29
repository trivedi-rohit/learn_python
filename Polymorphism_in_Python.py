""" 
Polymorphism => one of the core concepts of OOPs that describes situations in which something occurs in several different forms.
{i.e. you can access objects of different types through the same interface.}
Polymorphism can be achieved by-
1. Duck Typing
2. Operator Overloading 
3. Method Overloading
4. Method Overriding
"""
#! Duck Typing
class Duck:
    def swim(self):
        print("I'm a duck and I can swim.")
    def speak (self):
        print("Quak Quak")
class Dog:
    def swim(self):
        print("I'm a dog & can swim.")
    def speak(self):
        print("Woof Woof")
class person:
    def speak(self):
        print("Bla Bla")

def display(duck):
    duck.swim()
    duck.speak()
    print("=================================")

d = Duck()
dg = Dog()
per = person()
display(d)
display (dg)
# display(per)
# **********************************************************************************************************
##! Operator Overloading
# print(int.__add__(1,2))
# print(str.__add__('3','5'))
class complexNumber:
    def __init__(self, real, img):
        self.real=real
        self.img=img
    def __add__(self,other):          # Dunder Method __add__
        return(f"{self.real+other.real}+{self.img+other.img}i")


c1 = complexNumber(1,3)              # Object of class complexNumber
c2 = complexNumber(5,2)              # Object of class complexNumber   
print(c1 + c2)
#***********************************************************************************************************
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
# __gt__ method (for greater than)
    def __gt__(self,other):
        if self.age>other.age:
            return True
        else:
            return False
        
p1= Person('Rajdeep',23)
p2= Person('Jyoti',40)
if p1>p2:
    print(f"{p1.name} will pay the bill")
else:
    print(f"{p2.name} will pay the bill")
print("=================================================================================================")

# Method Overloading & Method Overridding:
#? (By default Python does not support method overloading)
# Method Overloading
class Demo:
    def add (self,*args):
        total =0
        for i in args:
            total +=i
        return total
    # def add(self,a,b,c=0):
    #     return a+b+c
d=Demo()
print(d.add(2,3))
print(d.add(3,4,5))
print(d.add(3,5,9,2,8,5,2,6))

# Method Overridding
class Father:
    def sleep(self):
        print("Sleep from 10:00 PM to 5:00 AM")
    def eat(self):
        print("Eating")
class Son(Father):
    def sleep(self):
        print("Sleep from 12:00 AM to 6:00 AM")

ram=Son()
ram.sleep()
ram.eat()