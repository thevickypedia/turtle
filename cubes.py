import turtle
import random

wn = turtle.Screen()
t = turtle.Turtle()

colors = ['red', 'yellow', 'green', 'blue', 'hotpink']

t.up()
t.goto(random.randrange(-50, 100), random.randrange(-50, 100))
t.color(random.choice(colors))
for _ in range(5):
    t.forward(50)
    t.left(90)
    t.down()

wn.exitonclick()
