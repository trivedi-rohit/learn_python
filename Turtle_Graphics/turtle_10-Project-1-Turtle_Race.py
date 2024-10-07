# Turtle Race Project:
import random
import turtle
width, height = 600,600
colorList=['orange','yellow','green','cyan','blue','red','blue4','purple','green3','brown','indigo']
# Taking user input (no. of turtles) for turtle race
def usrInput():
    turtleCount = 0
    while True:
        turtleCount=(input("How many turtles you want to race (2 - 10) : "))
        if turtleCount.isdigit():
            turtleCount = int(turtleCount)
        else:
            print("Please enter numeric value only (2 to 10).")
            continue
        if 2<=turtleCount<=10:
            return turtleCount
        else:
            print("Provide valid number of turtles (2 to 10)..........Try Again!!")
turtles = usrInput()
print(turtles)

# Setting up screen size
s1 =turtle.Screen()
s1.setup(width=600,height=600)

# Making equal spacing for each turtle
x_spacing = width//(turtles+1)
turtle_list=[]
for i in range(1, turtles+1):
    newTurtles=turtle.Turtle()
    newTurtles.shape("turtle")
    newTurtles.lt(90)
    newTurtles.color(colorList[i])
    newTurtles.penup()
    newTurtles.goto(-width//2+(i*x_spacing),-height//2+10)
    turtle_list.append(newTurtles)

# Race logic to run all turtle and declare winner also.
def raceLogic():    
    is_race_on=True
    while is_race_on:
        for turtleJEE in turtle_list:
            distance=random.randrange(1,20)
            turtleJEE.fd(distance)
            x,y=turtleJEE.pos()
            if y>=height//2-27:
                print(f"The winner is {turtleJEE.fillcolor()} turtle.")     # tuttle.color(pencolor,fillcolor)
                is_race_on=False
raceLogic()
s1.exitonclick()