import math
import turtle 
#! Square
# for i in range(4):
#     turtle.fd(100)
#     turtle.lt(90)
# turtle.lt(45)
# a = math.sqrt(2)*100
# turtle.fd(a)
# turtle.exitonclick()

#! Triangle
# for i in range(3):
#     turtle.fd(200)
#     turtle.lt(120)
# turtle.exitonclick()

#! # Rectangle
# turtle.getscreen()
# turtle.fd(100)
# turtle.lt(90)
# turtle.fd(50)
# turtle.lt(90)
# turtle.fd(100)
# turtle.lt(90)
# turtle.fd(50)
# turtle.exitonclick()

#! # Pentagon
# turtle.getscreen()
# turtle.fd(100)
# turtle.lt(72)
# turtle.fd(100)
# turtle.lt(72)
# turtle.fd(100)
# turtle.lt(72)
# turtle.fd(100)
# turtle.lt(72)
# turtle.fd(100)
# turtle.exitonclick()
''' or'''
# for i in range(5):
#     turtle.fd(100)
#     turtle.lt(72)
# turtle.exitonclick()

#! # Hexagon:
# pen = turtle.Turtle()
# pen.speed(1)
# for i in range(6):
#     pen.fd(100)
#     pen.lt(60)
# turtle.exitonclick()

# def star_pattern():
#     pen = turtle.Turtle()
#     pen.speed(0)
#     turtle.bgcolor("black")
#     pen.color("yellow")
    
#     for i in range(36):  # Draw 36 stars
#         for _ in range(5):
#             pen.forward(100)
#             pen.right(144)
#         pen.right(10)  # Rotate the star for the next one
    
#     turtle.done()

#! Grid Pattern
def grid_pattern():
    pen = turtle.Turtle()
    pen.speed(3)
    turtle.bgcolor("lightblue")
    
    for i in range(-200, 201, 50):  # Vertical lines
        pen.penup()
        pen.goto(i, -200)
        pen.pendown()
        pen.goto(i, 200)
    
    for i in range(-200, 201, 50):  # Horizontal lines
        pen.penup()
        pen.goto(-200, i)
        pen.pendown()
        pen.goto(200, i)
    
    turtle.mainloop()

grid_pattern()





