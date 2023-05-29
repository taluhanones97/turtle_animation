import turtle
from turtle import Turtle,Screen
import random
tim=Turtle()
tim.shape("turtle")
tim.color("red")

turtle.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    random_color=(r,g,b)
    return random_color


colours=["dark slate gray","pale turquoise","IndianRed","light yellow","gold"]
"""for x in range(8):
    shape=x+3
    angle=360/shape
    tim.color(random.choice(colours))
    for z in range(shape):

        tim.right(angle)
        tim.forward(100)




tim.forward(10)

tim.right(130)

"""
"""
tim.pen(speed=10,pensize=15)
for _ in range(100):
    x=random.randint(0,3)
    tim.color(random_color())
    if x==0:
        tim.forward(30)
    elif x==1:
        tim.left(90)
        tim.forward(30)
    elif x==2:
        tim.right(90)
        tim.forward(30)
    else:
        tim.right(180)
        tim.forward(30)
"""
"""








"""
turtle.speed(1000)
for i in range(37):
    turtle.circle(100)
    turtle.color(random_color())
    turtle.left(10)
tim.speed(1000)
for i in range(37):
    tim.circle(100)
    tim.color(random_color())
    tim.left(10)


tim.circle(50)

screen=Screen()
screen.exitonclick()