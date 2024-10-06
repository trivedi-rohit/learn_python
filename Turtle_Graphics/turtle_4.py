import turtle
turtle.bgcolor("black")
t1=turtle.Turtle()
t1.pensize(2)
# for i in range(10):
#     t1.pencolor("red")
#     t1.fd(10)
#     t1.penup()
#     t1.fd(10)
#     t1.pendown()
#     t1.pencolor("cyan")
#     t1.fd(10)
# # turtle.exitonclick()
# turtle.done()

def Dash():
    t1.forward(10)
    t1.penup()
    t1.forward(10)
    t1.pendown()

for _ in range(5):
    t1.pencolor("red")
    Dash()
    t1.pencolor("cyan")
    Dash()
turtle.exitonclick()