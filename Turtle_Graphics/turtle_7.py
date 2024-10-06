import turtle
t1=turtle.Turtle()
turtle.bgcolor("black")
t1.speed(0)
t1.color("red", "yellow")
print(t1.heading())
t1.begin_fill()
while True:
    t1.fd(400)
    t1.lt(170)
    if t1.heading()==0:
        break
t1.end_fill()
turtle.exitonclick()