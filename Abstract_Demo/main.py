from abstract_class import Vehicle
class Bike(Vehicle):
    def __init__(self,n,color):
        super().__init__(n)
        self.color = color
    def start(self):
        print("Start with kick")

#! Method Overridding
    def display(self):
        print (f"My color is {self.color}")

class Scotty(Vehicle):
    def __init__(self,n):
        super().__init__(n)
    def start(self):
        print("Self Start")

class Car(Vehicle):
    def __init__(self,n,x):
        super().__init__(n)
        self.gear=6
    def start(self):
        print("Start with key")

