# child/derived class inherit properties from more than 1 partnet class.
class Human:
    def __init__(self,num_heart):
        self.num_eyes = 2
        self.num_nose = 1
        self.num_heart = num_heart
    def eat (self): #Method-1
        print("I can eat.")
    def win (self):
        print("I can win.")
    def work(self):
        print("I can work.")

class Male:
    def __init__(self,name):
        self.name = name
    def win (self):
        print("I can win.")
    def work(self): #Method -2
        print("I can code.")

class Boy(Human,Male):
    def __init__(self,name,heart,langugae):
        Human.__init__(self,heart)
        Male.__init__(self,name)
        self.language=langugae
    def sleep(self):
        print("I can sleep.")
    def work(self):
        print("I can test.")
    def display(self):
        print(f"I'm {self.name}, and currently learning {self.language}.")

boy_1 = Boy('Rajesh',1,"Python")
boy_1.win()
boy_1.work()
'''
For above => If same method available in both parent & child class, then it is first access from child, after that from order mentioned at 'boy class' (class Boy(Human,Male):); 
This is also called as MRO (Method Resolution Order).
### when we call any function we have to print
'''
print(Boy.mro())
Male.work(boy_1) # accessing method from Male class, which boy inherit.
print(boy_1.num_eyes)
print(boy_1.name)
print(boy_1.num_heart)
print(boy_1.language)
boy_1.display()
