class Human:
    lang_name = 'Python'  # class attributes
    def eat(self):
        print("I can eat.")
    def work(self):
        print("I can work.")
class Male(Human):
    pass

male_1 = Male()
male_1.work()
male_1.eat()
#******************************************
class Human:
    def __init__(self,num_heart): # num_heart is argument & self is a keyword.
        self.num_eyes = 2         #access class attributes with self keyword.
        self.num_nose = 1
        self.num_heart = num_heart
    def eat (self):
        print("I can eat.")
    def play(self):
        print("I can play.")
    def work(self):
        print("I can work.")
class female(Human):
    def __init__(self,name,heart): # Defined own init function here, so to access attributes (num_eyes, num_nose), we have to use 'super' function.
        super().__init__(heart)
        self.name = name
    def work(self):
        super().work() # TO add something extra and use defination form base class, so a function (super) can be used.
        print("I can code.") # (Overridden 'work' method)
    def flirt(self):
        print("I can flirt.")
    def display (self):
        print(f"I'm {self.name} and I have {self.num_heart} heart.")

female_1 = female('Riya',1)
female_1.eat()
female_1.work()
female_1.flirt()
print(female_1.num_eyes)
print(female_1.name)
print(female_1.num_heart)
female_1.display()
