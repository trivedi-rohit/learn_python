import turtle
import random
t1=turtle.Turtle()
turtle.bgcolor("black")
t1.speed(0)
turtle.colormode(255)
print(t1.heading())
while True:
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    t1.pencolor(r,g,b)
    t1.circle(100)
    t1.lt(6)
    if t1.heading()==0:
        break
turtle.exitonclick()