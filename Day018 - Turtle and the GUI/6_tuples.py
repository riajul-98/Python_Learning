import random
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
timmy.pensize(10)
timmy.speed("fast")
turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)       # This is a tuple which is immutable.
    return color

for move in range(200):
    color = random_color()
    timmy.color(color)
    random.choice([timmy.left, timmy.right])(90)
    timmy.forward(30)

screen = Screen()
screen.exitonclick()
