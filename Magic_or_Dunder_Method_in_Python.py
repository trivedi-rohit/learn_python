# Dunder/Magic method in python allow us to use built-in operations with our user created Objects.
# list1=[-1,2,3]
# print(len(list1))

# class Demo:
#     name="Indardeep"
# d=Demo()
# print(len(d.name))
# print(d.name)

class Author:
    def __init__(self,name,bookName,pages):
        self.name=name
        self.bookName=bookName
        self.pages=pages
    def __len__ (self):
        return  self.pages
    def __str__(self):
        return f"{self.bookName} by {self.name}"
    def __call__ (self, *args, **kwargs):
        print("Hi all",)

d=Author("Rohit Trivedi","Python-O-Mania",450)
print(str(d))
print(len(d))
d()