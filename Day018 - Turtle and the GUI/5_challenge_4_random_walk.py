import random
from turtle import Turtle, Screen

timmy = Turtle()
timmy.pensize(10)
colors = ["red", "olive drab", "blue", "medium violet red", "orange", "medium purple", "deep pink", "gold"]
timmy.speed("fast")

for move in range(200):
    timmy.color(random.choice(colors))
    random.choice([timmy.left, timmy.right])(90)
    timmy.forward(30)

screen = Screen()
screen.exitonclick()
