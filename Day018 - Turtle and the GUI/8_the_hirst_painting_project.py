# Recreating the Spot Painting by Damien Hirst using Turtle
import random
import turtle
# pip install colorgram.py

# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

from turtle import Turtle, Screen

turtle.colormode(255)

color_list = [(207, 159, 82), (54, 89, 130), (146, 91, 39),
              (140, 26, 48), (222, 207, 104), (132, 177, 203), (158, 46, 83), (45, 55, 104), (170, 160, 39),
              (129, 189, 143),
              (83, 20, 44), (36, 43, 69), (186, 94, 106), (186, 140, 172), (84, 120, 180), (60, 39, 31), (88, 157, 92),
              (78, 153, 164), (195, 78, 72), (45, 74, 78), (80, 74, 44), (162, 201, 218), (58, 126, 122),
              (218, 176, 187),
              (169, 207, 170), (220, 181, 168)]

tim = Turtle()
tim.penup()
tim.speed("fast")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
turtle.pendown()

for column in range(10):
    for row in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.left(180)
    tim.pendown()

tim.hideturtle()
screen = Screen()
screen.exitonclick()
