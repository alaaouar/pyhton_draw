import turtle

def draw_leaf(t, size):
    t.begin_fill()  # Start filling the shape with color
    t.circle(size, 60)
    t.left(120)
    t.circle(size, 60)
    t.left(120)
    t.circle(size, 60)
    t.end_fill()  # End filling the shape

def draw_rectangle(t, width, height):
    t.begin_fill()  # Start filling the rectangle
    t.forward(width / 2)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width / 2)
    t.end_fill()  # End filling the rectangle

# Set up the turtle
t = turtle.Turtle()
t.color("green")
t.speed(0)

# Draw the first leaf standing vertically
t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(60)  # Adjust the heading to 60 degrees
draw_leaf(t, 170)  # Increase the size parameter to make the leaf bigger

# Draw additional leaves at different angles
t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(100)
draw_leaf(t, 130)

t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(20)
draw_leaf(t, 130)

t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(140)
draw_leaf(t, 150)

t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(-20)
draw_leaf(t, 150)

t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(-60)
draw_leaf(t, 70)

t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(180)
draw_leaf(t, 70)

# Draw the stem
t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(0)
draw_rectangle(t, 16, 50)

# Hide the turtle and finish drawing
t.hideturtle()
turtle.done()
