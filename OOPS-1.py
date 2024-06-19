# class Student:
#     name = "karan"

# s1 = Student()
# print(s1)
# print(s1.name)

#! Constructor (__init__ Function)
# All classes have function called __init__() which is always executed when object is being initiated.
""" The "self" parameter is a reference to the current instance of the class and is used to access variables that belongs to the class."""

class Student:
    College_name = "ABC College"
    name = "NoName" # Class attribute

    # default constructor
    def __init__(self): # No need to write  this. It will be automatically created.
        pass
    
    # Parameterized constructor    
    def __init__(self, name, marks):    # contructor always takes a parameter(self) & self is pointing towards 1st object "s1"
        self.name = name        #! {Object Attribute and presidence of object attribute is higher than class attributes}  "self.name" will be created in object. "name" after self in above statemnt is same name.
        self.marks = marks
        print("adding new student in DB..")

    def welcome(self):
        print("welcome student", self.name)

    def get_marks(self):
        return self.marks


s1 = Student("karan", 98)    # After writing class name parantheses() is used to call constructor.
print(s1.name, s1.marks)
print (Student.College_name)
print(s1.marks) 
print(s1.get_marks())

s2 = Student("Praveen", 91)  # After writing class name parantheses() is used to call constructor.
print(s2.name, s2.marks)

#! WAP & create studentclass that take name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.
# Method-1
class Student:
    def __init__(self, name, phy, chem, maths):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.maths = maths
        
    def avgn(self): 
            avg_mks = ((self.phy + self.chem + self.maths) / 3)
            return avg_mks


s1 = Student ("Karan", 78, 90, 93)
print("Hi,", s1.name, "your average score is", s1.avgn())
print("Student Name: ", s1.name)
print("Average Marks:", s1.avgn())
s1.name = "Tony" # name can be changed.
print("Hi,", s1.name, "your average score is", s1.avgn())


# Method-2
class Student:
    def __init__(self, name, phy, chem, maths):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.maths = maths

    def avgn(self):
        sum_mks = self.phy + self.chem + self.maths
        avg_mks = sum_mks / 3
        return avg_mks

    def display_info(self):
        print("Average Marks:", self.avgn())

student1 = Student("John", 80, 75, 90)
student1.display_info()


# Method-3
class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod # Decorator- '''Decorator allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.'''
    def hello():
        print("hello")


    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "your average score is", sum/3)

s1 = Students ("Jack Sparrow", [98,99,100])
s1.get_avg()
s1.hello()

# The 4 main pillars of OOP's are:

# a. Abstraction
# b. Encapsulation
# c. Inheritance
# d. Polymorphism

#! a. Abstraction - Hiding the implementation details of a class and only showing the essential features to the user.

class Cars:
    
    def __init__(self):
        self.acc = False
        self.clutch = False
        self.brk = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car Started..")

car = Cars()
car.start()

#! b. Encapsulation - wrapping data and functions into a single unit (object).
# Create "Account" class with 2 attributes - balance and account no. 
# Create method for debit, credit & printing the balance.
#! Method -1
class Account:

    def __init__ (self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # debit method
    def debit(self, amt):
        self.balance -= amt
        print("Rs.", amt, "was debited")
        print("Total balance = ", self.final_bal())
    
    # Credit Method
    def credit(self, amt):
        self.balance += amt
        print("Rs.", amt, "was credited")
        print("Total balance = ", self.final_bal())
    
    def final_bal(self):
        return self.balance


acc1 = Account(10000, 7560)
print(acc1.balance)
acc1.debit(5000)
acc1.credit(15937)

# Method-2
class Account:

    def __init__ (self, name, acc_no, balance, credit, debit):
        self.name = name
        self.balance = balance
        self.acc_no = acc_no
        self.debit = debit
        self.credit = credit

    def bank_fun(self):
            bank_remain = (self.balance + self.credit - self.debit)
            print("Hi,", self.name, "remaining balance in your account number", self.acc_no, "is", bank_remain)



my_acc = Account("Raju", 756000102033693, 1000000, 500, 250)
my_acc.bank_fun()
print(my_acc.balance)

my_acc1 = Account("Raja", 756000102033683, 1000, 500, 250)
my_acc1.bank_fun()
print(my_acc1.balance)