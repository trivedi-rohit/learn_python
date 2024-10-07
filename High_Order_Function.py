# High Order Function:
# def greet_louder(name):
#     print(f"Hello! {name.upper()}")
# def greet_softer(name):
#     print(f"Hello! {name.lower()}")
# #! Display function is here a Higher Order Function. ----(Here, Function is accepting other function as argument)
# def display(other_def_func,name1):
#     print("This is display() function")
#     other_def_func(name1)
# display(greet_louder,"ROhit")
# display(greet_softer,"ROhit")

##! hellow is higher order function --- (Here, function is returning a function)
# def hello(name):
#     print("Hello has been executed")
#     def greet():
#         print("Om Namaha Shivaay")
#     def welcome():
#         print("Hare Krishna")
#     if name=="Rohit":
#         return greet
#     else:
#         return welcome

# new_func=hello("Rohit T")
# new_func()
# print(new_func)

#! Passing function as argument:
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

def cal(num,x,y):
    print(num(x,y))

cal(add,3,5)
cal(div,15,3)