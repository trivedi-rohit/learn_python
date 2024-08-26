class A:
    def  display(self):
        print("Display form A class.")

class B (A):
    def display(self):
        print("Display from B class.")

class C:
    def show (self):
        print("This is 'C' class.")
    
class D (B,C):
    def display (self):
        print("Display form 'D' class.")
    
d1 = D()
d1.display()
print(D.mro())

