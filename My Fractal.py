import turtle
import random
import math

my_turtle = turtle.Turtle()
my_turtle.showturtle()
my_turtle.shape("turtle")
my_turtle.speed(0)
my_screen = turtle.Screen()
my_screen.bgcolor('white')
my_turtle.width(1)
my_turtle.fillcolor("grey")
colors = ["pink", "purple", "blue", "yellow", "green", "orange", "red"]

#------------------------

def recursive_frac(x, y, size, depth, angle):
    m = 2
    if depth > 0:
        my_turtle.pencolor(colors[random.randrange(len(colors))])
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.right(angle)
        my_turtle.forward(size)
        recursive_frac(x, y, size / 1.003, depth - 1, angle)


recursive_frac(0, 0, 300, 900, 1)


my_screen.exitonclick() # end of program