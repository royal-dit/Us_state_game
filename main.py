import turtle
import pandas
screen = turtle.Screen()
screen.title("Us States games")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x,y):
#print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_state = []
while len(guessed_state) < 50 :
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50",prompt="What another state name").title()
    print(answer_state )

    if answer_state =="Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("States to learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.state.item())


# new_csv=pandas.DataFrame(guessed_state)
# new_csv.to_csv("guessed_states")


screen.exitonclick()