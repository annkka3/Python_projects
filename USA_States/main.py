import turtle
import pandas as pd
from print_state_name import State

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

guessed_states_num = 0
guessed_states = []
states = pd.read_csv('50_states.csv')
all_states = states.state.to_list()

while guessed_states_num < 50:
    answer_state = screen.textinput(title=f"{guessed_states_num}/50 Guess the State",
                                    prompt="What's another state do you know?").title()
    if answer_state == 'Exit':
        states_to_learn = [state for state in all_states if state not in guessed_states]
        data_to_learn = pd.DataFrame(states_to_learn)
        data_to_learn.to_csv('states_to_learn.csv')
        break

    if answer_state in all_states:
        x_cor = states['x'][all_states.index(answer_state)]
        y_cor = states['y'][all_states.index(answer_state)]
        print_state = State(answer_state, x_cor, y_cor)
        guessed_states_num += 1
        guessed_states.append(answer_state)

# function that helps to find x, y coordinates for th states on th picture
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
