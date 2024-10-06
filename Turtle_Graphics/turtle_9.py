import turtle
import random
turtle.bgcolor("black")
t=turtle.Turtle()
turtle.colormode()
s1=turtle.Screen()
s1.screensize(400,400)
turtle.speed(10)
print(s1.screensize())
list_1=['red','yellow','green','cyan','blue','orange','blue4','purple','green3']
for i in range(300):
    t.pencolor(random.choice(list_1))
    t.penup()
    t.goto(random.randint(-400,400),random.randint(-400,400))
    t.pendown()
    t.dot(20)
s1.exitonclick()