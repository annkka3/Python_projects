from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.3
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset():
    global reps, label_timer
    label_timer.config(text="Timer")
    check_mark.config(text='')
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="25:00")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start():
    global reps, label_timer
    reps += 1
    work_sec = WORK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60
    if reps % 2 == 1:
        count_down(work_sec)
        label_timer.config(text="Work", fg=RED, bg=YELLOW, font=(FONT_NAME, 32, "bold"))

    elif reps % 8 == 0:
       count_down(long_break)
       label_timer.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 32, "bold"))
    else:
       count_down(short_break)
       label_timer.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 32, "bold"))
       count_check = 1
       check_mark.config(text='✅' * count_check)
       count_check += 1
       if count_check == 5:
           count_check -= 4









# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
   global timer
   count_min  = math.floor(count/60)
   count_sec = count % 60
   if count_sec < 10:
      count_sec = f"0{count_sec}"
   canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
   if count > 0:
      timer = window.after(1000, count_down, count -1)
   else:
      start()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg = YELLOW)

label_timer = Label(text="Timer",fg = RED, bg = YELLOW, font=(FONT_NAME, 32, "bold"))
label_timer.grid(column=1, row=0)

check_mark = Label(text = '',bg = YELLOW,font=(FONT_NAME, 20, "bold"))
check_mark.grid(column=1, row=4)

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100,130, text= '25:00', fill = 'white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

button_start = Button(text="Start",fg = RED, command=start, highlightthickness=0, font=(FONT_NAME, 20, "bold"))
button_start.grid(column=0, row=3)
button_reset = Button(text="Reset",fg = RED, command=reset,font=(FONT_NAME, 20, "bold"))
button_reset.grid(column=2, row=3)



window.mainloop()