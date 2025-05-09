# Hello! Welcome to the U.S. States Game!
# In this game, you'll try to guess all the U.S. States
# If you want to stop guessing, just write "exit" in the writing tab

# In this project, I learned a lot of data and csv management skills using pandas.

# P.S: If you have any questions or suggestions about this code, feel free to reach out to me!

import turtle
import pandas as pd
from map import MapNames

# Setting the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(height=491, width=725)

# Getting all data and countries from the csv using pandas
data = pd.read_csv("50_states.csv")
all_states = data["state"].tolist()

# Setting important variables
game_is_on = 1
score = 0
guessed_states = []
title="Guess the State"

# Game start
while score < 50:
    if score > 0:
        title = f"{score}/50 States Correct"

    # Setting the answer tab
    answer_state = screen.textinput(title=title, prompt="What's another state's name?").title()

    # Verifying the keyword "Exit" used to stop guessing
    if answer_state == "Exit":
        break

    # Verifying the existence of the state guessed
    if answer_state in all_states:
        state_row = data[data["state"] == answer_state]
        x = state_row.x.item()
        y = state_row.y.item()
        state_name = MapNames()
        state_name.add(x,y, answer_state)
        guessed_states.append(answer_state)
        score += 1

# Putting all missed States in a list
missed_states = []
for state in all_states:
    if state not in guessed_states:
        missed_states.append(state)

# Creating a new DataFrame with all missing states
data_dict = {
    "States to learn": missed_states,
}
df = pd.DataFrame(data_dict)
df.to_csv("states_to_learn")

print(df)