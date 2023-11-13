import turtle

t = turtle.Turtle()
t.speed(0)
t.left(90)

def branch(length, t):
    if length < 6:
        return

    t.forward(length)
    t.right(15)
    branch(length -10, t)
    t.left(30)
    branch(length-20, t)
    t.right(15)
    t.backward(length)

branch(100, t)

#Ensure the program remains open after construction
turtle.Screen().exitonclick()
turtle.Screen().mainloop()
