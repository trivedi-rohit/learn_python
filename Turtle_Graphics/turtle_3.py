import turtle
# drawing a circle
t1=turtle.Turtle()
t1.shape("turtle")
t1.pensize(4)
t1.color("yellow")
t1.penup()
t1.goto(-250,0)
t1.pendown()
t1.circle(100)
t1.hideturtle()

# drawing a square
t2=turtle.Turtle()
t2.shape("turtle")
t2.color("red")
t2.penup()
t2.forward(200)
t2.pendown()
t2.pensize(4)
t2.forward(100)
t2.left(90)
t2.forward(100)
t2.left(90)
t2.forward(100)
t2.left(90)
t2.forward(100)
t2.hideturtle()

# drawing a triangle
t3=turtle.Turtle()
t3.shape("turtle")
t3.penup()
t3.goto(-300,-200)
t3.pendown()
t3.pensize(4)
t3.color("green")
t3.forward(100)
t3.left(120)
t3.forward(100)
t3.left(120)
t3.forward(100)
t3.hideturtle()

# drawing a pentagon
t4=turtle.Turtle()
t4.shape("turtle")
t4.penup()
t4.goto(200,-200)
t4.pendown()
t4.shape("turtle")
t4.pensize(4)
t4.color("skyblue")
t4.forward(100)
t4.left(72)
t4.forward(100)
t4.left(72)
t4.forward(100)
t4.left(72)
t4.forward(100)
t4.left(72)
t4.forward(100)
t4.hideturtle()
turtle.done()  # keep the turtle window open