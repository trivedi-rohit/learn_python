import turtle
import random
turtle.bgcolor('black')
tom=turtle.Turtle()
tom.speed(10)
tom.width(15)
tom.pensize(8)
# list_1=['red','yellow','green','cyan','blue','orange','blue4','purple','green3']
turtle.colormode(255)
for i in range(100):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    tom.setheading(random.randrange(0,360,90))
    tom.pencolor(r,g,b)
    # tom.pencolor(random.choice(list_1))
    tom.fd(40)
tom.screen.mainloop()
