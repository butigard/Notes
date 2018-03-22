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
colors = ["pink", "purple", "blue", "yellow", "green", "orange", "red"]

#------------------------

def recursive_square(x, y, size, depth):
    m = 2
    if depth > 0:
        my_turtle.fillcolor(colors[random.randrange(len(colors))])
        my_turtle.begin_fill()
        my_turtle.up()
        my_turtle.goto(x - size, y + size)
        my_turtle.down()
        my_turtle.goto(x + size, y + size)
        my_turtle.goto(x + size, y - size)
        my_turtle.goto(x - size, y - size)
        my_turtle.goto(x - size, y + size)
        my_turtle.end_fill()
        recursive_square(x - size, y + size, size / m,  depth - 1)
        recursive_square(x + size, y + size, size / m, depth - 1)
        recursive_square(x + size, y - size, size / m, depth - 1)
        recursive_square(x - size, y - size, size / m, depth - 1)


recursive_square(0, 0, 150, 7)


my_screen.exitonclick() # end of program