import turtle
import random
t=turtle.Turtle()
turtle.bgcolor("black")
t.pensize(3)
#! Method - 1: 
# # Multiple shapes using loops
# for i in range(3):
#     t.pencolor("cyan")
#     t.fd(100)
#     t.rt(120)
# for j in range(4):
#     t.pencolor("yellow")
#     t.fd(100)
#     t.rt(90)
# for k in range(5):
#     t.pencolor("red")
#     t.fd(100)
#     t.rt(72)    
# for l in range(6):
#     t.pencolor("yellow")
#     t.fd(100)
#     t.rt(60)
# for m in range(7):
#     t.pencolor("orange")
#     t.fd(100)
#     t.rt(51.42)
# for n in range(8):
#     t.pencolor("blue")
#     t.fd(100)
#     t.rt(45)
# turtle.exitonclick()
#! Method - 2:
list_1=['red','yellow','green','cyan','blue','orange','blue4','purple','green3']
for a in range(3,9):
    angle=360/a
    t.pencolor(random.choice(list_1))
    for _ in range(a):
        t.fd(100)
        t.rt(angle)
t.screen.mainloop()