import turtle

my_turtle = turtle.Turtle()
my_turtle.showturtle()
my_turtle.shape("turtle")
my_turtle.speed(3)

my_screen = turtle.Screen()
my_screen.bgcolor('white')

# draw a shape using goto
my_turtle.fillcolor("red")
my_turtle.begin_fill() # starts a shape to fill in
my_turtle.goto(200, 0)
my_turtle.goto(200, 200)
my_turtle.goto(0, 200)
my_turtle.goto(0, 0)
my_turtle.end_fill() # end of shape

# pick up the turtle
my_turtle.up()
my_turtle.goto(200, 200)

my_turtle.down()
my_turtle.fillcolor("purple")
my_turtle.begin_fill()
my_turtle.goto(300, 300)
my_turtle.goto(300, 200)
my_turtle.goto(200, 200)
my_turtle.end_fill()

# draw using headings
my_turtle.up()
my_turtle.goto(0, 0)
my_turtle.down()
my_turtle.width(10) # width in pixels

my_turtle.fillcolor("yellow")
my_turtle.begin_fill()
my_turtle.forward(100)
my_turtle.setheading(90)
my_turtle.forward(100)
my_turtle.setheading(180)
my_turtle.forward(100)
my_turtle.setheading(270)
my_turtle.forward(100)
my_turtle.end_fill()

for i in range(6):
    my_turtle.right(60)
    my_turtle.forward(100)


my_screen.exitonclick() # end of program