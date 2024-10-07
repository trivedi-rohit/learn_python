#! Coding Excercise on Event Listeners in python (Free Hand Drawing):
from turtle import Turtle,Screen
screen=Screen()
tom=Turtle()

def moveFWD():
    tom.fd(20)
def moveBKD():
    tom.bk(20)
def turnLeft():
    newHeading=tom.heading()+20
    tom.setheading(newHeading)
    tom.forward(20)
def turnRight():
    newHeading=tom.heading()-20
    tom.setheading(newHeading)
    tom.forward(20)

def clearScreen():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()

screen.listen()
screen.onkey(fun=moveFWD,key="f")
screen.onkey(fun=moveBKD,key="b")
screen.onkey(fun=turnLeft,key="l")
screen.onkey(fun=turnRight,key="r")
screen.onkey(fun=clearScreen,key="c")

screen.exitonclick()