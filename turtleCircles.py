import turtle

speed = 10
circles = 20
radius = 75
Angle = 15

turtle.speed(speed)

for x in range(circles):
    turtle.circle(radius)
    turtle.right(Angle)
