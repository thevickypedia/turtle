import turtle

wn = turtle.Screen()
jan = turtle.Turtle()

jan.up()
jan.goto(-200, -50)
jan.down()

# draw a rectangle
for distance in [400, 100, 400, 100]:
    jan.forward(distance)
    jan.left(90)

wn.exitonclick()
