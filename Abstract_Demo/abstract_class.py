# Make Vehicle class abstract class, to avoid/restrict anyone from creating object of a particular class.
# In order to have abstract class then that class must have 1 abstract method using decorator.
from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,n):
        self.no_of_types = n
    @abstractmethod
    def start (self):
        pass
    def display(self):
        print ("Hi, I from Vehicle class")
