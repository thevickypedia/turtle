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

# extend to top
for distance in [400, 300, 400, 300]:
    jan.forward(distance)
    jan.left(90)

# start drawing lines inside with spacing of 10 units
for _ in range(20):
    '''using range 20 because we are doing two tasks within the main loop each with a distance of 10 units so
    range(20)*2(tasks)*10(units)'''
    for distance in [10, 100]:
        jan.forward(distance)
        jan.left(90)

    jan.right(180)

    for distance in [10, 100]:
        jan.forward(distance)
        jan.right(90)

    jan.right(180)

wn.exitonclick()
