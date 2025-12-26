from turtle import Turtle

import pandas as pd
from turtle import Turtle, Screen

screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

map = Turtle()
map.shape(image)
screen.tracer(0)

writer = Turtle()
writer.penup()
writer.hideturtle()

data = pd.read_csv("50_states.csv")

more_states = True
score = 0
guessed_states = []

while more_states:
    screen.update()
    answer_state = screen.textinput(title=f"Guess the state ({score}/50)", prompt="Enter a state: ").title()

    for state in data["state"]:
        if answer_state == state and answer_state not in guessed_states:
            guessed_states.append(answer_state)
            row = data[data.state == answer_state]
            writer.goto(float(row["x"]), float(row["y"]))
            writer.write(arg=state, align="center", font=("Courier", 10, "normal"))
            score += 1

        if score == 50:
            more_states = False



screen.mainloop()