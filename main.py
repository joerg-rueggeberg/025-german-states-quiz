from turtle import Screen, Turtle
import pandas

data = pandas.read_csv("data.csv")
states = data.state.to_list()
print(states)
screen = Screen()
screen.title("Deutschland Bundesländer Quiz - Jörg")
image = "deutschland.gif"
screen.addshape(image)
screen.setup(640, 640)

game_map = Turtle()
game_map.shape(image)
show_name = Turtle()
show_name.hideturtle()
show_name.color("black")
show_name.pu()
FONT_OVER = ("Verdana", 18, "bold")

game_over = False
guessed_right = 0
guessed = []

while len(guessed) != len(data):
    guess = screen.textinput(f"Bundesländer erraten: {guessed_right}/{len(data)}",
                             "Wie lautet ein weiteres deutsches Bundesland?\n\n"
                             "Tippe 'exit' zum beenden.").title()
    if guess == "Exit":
        break
    if guess in states and guess not in guessed:
        guessed_right += 1
        guess_data = data[data.state == guess]
        x_coord = int(guess_data.x)
        y_coord = int(guess_data.y)
        show_name.setpos(x_coord, y_coord)
        show_name.write(guess, align="center", font=("Verdana", 8, "bold"))
        guessed.append(guess)

if guessed_right == 16:
    show_name.goto(0, 0)
    show_name.pd()
    show_name.write(f"Du hast alle {len(data)} Bundesländer gefunden!\n 🥳🥳 Glückwunsch! 🥳🥳",
                    align="center", font=FONT_OVER)

states_left = [state for state in states if state not in guessed]

states_to_learn = pandas.DataFrame(states_left)
states_to_learn.to_csv("states_to_learn.csv")

screen.exitonclick()
