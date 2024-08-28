from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)  # When adding a function in a function, don't add parenthesis as the
# parenthesis triggers function to happen there and then
screen.exitonclick()

# A higher order function is a function that can work with other functions. In this case, onkey()
