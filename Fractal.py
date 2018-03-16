import turtle
import math

my_turtle = turtle.Turtle()
my_turtle.showturtle()
my_turtle.shape("turtle")
my_turtle.speed(0)
my_screen = turtle.Screen()
my_screen.bgcolor('black')
my_turtle.width(1)
my_turtle.pencolor("white")

#------------------------

def recursive_snowflake(x, y, size, depth):
    m = 3.5
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x + size, y)
        my_turtle.goto(x - size, y)
        my_turtle.goto(x, y)
        my_turtle.goto(x + math.cos(math.radians(60)) * size, y + math.sin(math.radians(60)) * size)
        my_turtle.goto(x + math.cos(math.radians(60)) * size * -1, y + math.sin(math.radians(60)) * size * -1)
        my_turtle.goto(x, y)
        my_turtle.goto(x + math.cos(math.radians(120)) * size, y + math.sin(math.radians(120)) * size)
        my_turtle.goto(x + math.cos(math.radians(120)) * size * -1, y + math.sin(math.radians(120)) * size * -1)
        my_turtle.up()
        recursive_snowflake(x + size, y, size / m,  depth - 1)
        recursive_snowflake(x - size, y, size / m, depth - 1)
        recursive_snowflake(x + math.cos(math.radians(60)) * size, y + math.sin(math.radians(60)) * size, size / m, depth - 1)
        recursive_snowflake(x + math.cos(math.radians(60)) * size * -1, y + math.sin(math.radians(60)) * size * -1, size / m, depth - 1)
        recursive_snowflake(x + math.cos(math.radians(120)) * size, y + math.sin(math.radians(120)) * size, size / m,  depth - 1)
        recursive_snowflake(x + math.cos(math.radians(120)) * size * -1, y + math.sin(math.radians(120)) * size * -1, size / m,  depth - 1)

recursive_snowflake(0, 0, 200, 4)


my_screen.exitonclick() # end of program