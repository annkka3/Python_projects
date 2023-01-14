from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_dict)
    canvas.itemconfig(card_title, text= "French", fill ='black')
    canvas.itemconfig(card_word, text= current_card["French"], fill= 'black')
    canvas.itemconfig(canvas_image, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=current_card["English"], fill='white')
    canvas.itemconfig(canvas_image, image=card_back_image)

def right():
    global current_card
    words_dict.remove(current_card)
    data = pd.DataFrame(words_dict)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()

def wrong():
    next_card()



try:
    words = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    words = pd.read_csv("data/french_words.csv")

words_dict = words.to_dict(orient='records')



window = Tk()
window.title('Flash cards')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func = flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0 )
card_front_image = PhotoImage(file ="images/card_front.png")
card_back_image = PhotoImage(file ="images/card_back.png")
canvas_image = canvas.create_image(400, 260, image = card_front_image)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text = "", font =('Arial', 40, "italic"))
card_word = canvas.create_text(400,263,  text = "", font =('Arial', 60, "bold"))


#Buttons
right_image = PhotoImage(file = 'images/right.png')
button_ok = Button(imag=right_image, command=right, highlightthickness=0)
button_ok.grid(column=1, row=1)
wrong_image = PhotoImage(file = 'images/wrong.png')
button_no = Button(image=wrong_image, command=wrong, highlightthickness=0)
button_no.grid(column=0, row=1)

next_card()




window.mainloop()