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

# extend to bottom
for distance in [400, -200, 400, -200]:
    jan.forward(distance)
    jan.left(90)

# extent to top
for distance in [400, 300, 400, 300]:
    jan.forward(distance)
    jan.left(90)

wn.exitonclick()
