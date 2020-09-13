import turtle

wn = turtle.Screen()
t = turtle.Turtle()

t.up()
t.goto(-50, 100)
t.color('yellow')
for _ in range(5):
    t.forward(50)
    t.left(90)
    t.down()

wn.exitonclick()
