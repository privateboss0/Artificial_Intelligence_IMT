import turtle
from turtle import *

def draw_heart(color):
    t.color(color)
    t.begin_fill()
    t.pensize(3)
    t.left(50)
    t.forward(133)
    t.circle(50, 200)
    t.right(140)
    t.circle(50, 200)
    t.forward(133)
    t.end_fill()

t = turtle.Turtle()
t.speed(0)

# Draw the Brown heart
draw_heart("Brown")

# Move the turtle to the position for the red heart
t.penup()
t.setheading(0)
t.goto(-270, 0)
t.pendown()

# Draw the Pink heart
draw_heart("Pink")

# Move the turtle to the position for the blue heart
t.penup()
t.setheading(0)
t.goto(270, 0)
t.pendown()

# Draw the Green heart
draw_heart("Green")

turtle.Screen().mainloop()