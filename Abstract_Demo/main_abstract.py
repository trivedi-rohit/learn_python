from main import *
bike = Bike (2,"Blue")
bike.start()
bike.display()

scotty = Scotty (2)
scotty.start()
scotty.display()

car = Car(4,6)
car.start()


""" Abstract class = a class having one or more abstracrmethod & abstract class can not be instantiated (No Object can be created) from abstact class; 
Also abstract class can have abstractmethod & concret method.
Abstract class has only declaration but no implemenataion i.e is abstract method"""