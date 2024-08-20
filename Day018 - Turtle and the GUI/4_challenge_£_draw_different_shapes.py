import random
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
no_of_angles = 3
side_length = 100
colors = ["red", "olive drab", "blue", "medium violet red", "yellow", "medium purple", "deep pink", "gold"]

while no_of_angles < 11:
    angle_size = 360 // no_of_angles
    for side in range(no_of_angles):
        timmy.forward(side_length)
        timmy.right(angle_size)
    no_of_angles += 1
    timmy.color(random.choice(colors))

screen.exitonclick()