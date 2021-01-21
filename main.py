import turtle
import random
import pandas

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    return new_color


screen = turtle.Screen()
screen.title("INDIAN STATE GAME")
screen.bgcolor(random_color())
image = "blank_indian_state.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("States_of_India.csv")
all_states = data.states.to_list()

guessed_state = []
while len(guessed_state) < 50:

    answer_state = screen.textinput(
        title=f"{len(guessed_state)} / 30 States Correct", prompt="What's the another state name?").title()

    if answer_state == "Exit":
        missing_state = [
            state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("States_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.states == answer_state]
        t.goto(x=int(state_data.x), y=int(state_data.y))
        t.write(arg=answer_state, align="center",
                font=("Courier", 8, "bold"))
