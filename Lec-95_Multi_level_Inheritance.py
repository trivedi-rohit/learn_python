class Human:
    can_breath = True
    def __init__(self,num_heart):
        self.eyes = 2
        self.num_heart = num_heart

    def eat(self):
        print("I can eat.")

    def work(self):
        print("I can work.")

class Male(Human):
    def __init__(self,name):
        print("calling from male class")
        self.name = name
    def sleep (self):
        print("I can sleep whole day.")

class Boy(Male):
    def __init__(self,heart,name,can_dance):
        Human.__init__(self,heart)
        Male.__init__(self,name)
        self.know_dance = can_dance
    def work(self):
        # Human.work(self)                # To use the attribute of Human class & Boy class both.
        super().work()              # To use attribute of parent class, we can super() or above statement.
        print("I can code.")

boy_1 = Boy(1,"Rahul",False)
print(boy_1.name)
# boy_1.work()    
# print(boy_1.num_heart)
print(boy_1.know_dance)
print(boy_1.can_breath)
print(Boy.mro())
