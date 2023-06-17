import turtle
from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

def draw_circle(size, angle, shift):
    turtle.bgcolor(next(colors))
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)

turtle.speed('fast')

# First circle
draw_circle(30, 0, 1)

# Reset turtle's position
turtle.penup()
turtle.home()
turtle.pendown()

turtle.bgcolor('black')
turtle.pensize(40)

# Second circle
draw_circle(35, 0, 1)

turtle.done()

