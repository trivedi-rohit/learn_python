# Python Event Listeners:
from turtle import Turtle,Screen
screen=Screen()
tom=Turtle()

def forwrd():
    tom.fd(20)
def up():
    tom.setheading(90)
    # tom.fd(20)
def down():
    tom.setheading(270)
    # tom.fd(20)
def left():
    tom.setheading(180)
    # tom.fd(20)
def right():
    tom.setheading(360)

def clearScreen():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()

screen.listen()
screen.onkey(fun=up,key="Up")
screen.onkey(fun=down,key="Down")
screen.onkey(fun=left,key="Left")
screen.onkey(fun=right,key="Right")
screen.onkey(fun=clearScreen,key="c")
screen.onkey(fun=forwrd,key="space")

screen.exitonclick()