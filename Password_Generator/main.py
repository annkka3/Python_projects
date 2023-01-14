from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pd_letters = [choice(letters) for _ in range(randint(8, 10))]
    pd_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pd_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pd_letters + pd_numbers + pd_symbols

    shuffle(password_list)

    password = ''.join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()
    new_data = {
        website: {
            "e-mail": username,
            "password": password,
        }
    }
    if len(username) == 0 or len(password) == 0 or len(website) == 0:
        messagebox.showwarning(title="Warning", message="Hey, you've left some fields empty...")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These details are entered: \n username:{username} \n password: {password} \n Is it ok to save?")
        if is_ok:
            try:
                with open('data.json', 'r') as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open('data.json', "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                if (website in data) and (username == data[website]["e-mail"]):
                    is_update = messagebox.askokcancel(title="Warning",
                                                       message="It seems that you already have a password for such user on this website. Do you want to update it?")
                    if is_update:
                        data[website]['e-mail'] = username
                        data[website]['password'] = password
                        with open('data.json', "w") as data_file:
                            json.dump(data, data_file, indent=4)
                else:
                    data.update(new_data)
                    with open('data.json', "w") as data_file:
                        json.dump(data, data_file, indent=4)
                    messagebox.showinfo(title="Success", message=f"Added {website} to the data store.")
            finally:
                entry_website.delete(0, END)
                entry_password.delete(0, END)
                entry_website.focus()

# ---------------------------- FIND PASSWORD ------------------------------- #


def search():
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Warning", message="Sorry, there is no Data File")
    else:
        website_search = entry_website.get()
        if website_search in data:
            pass_search = data[entry_website.get()]['password']
            user_search = data[entry_website.get()]['e-mail']
            messagebox.showinfo(title=f"{entry_website.get}",
                                message=f'Username: {user_search} \n Password: {pass_search}')
        else:
            messagebox.showwarning(title="No such site", message="Sorry, there is no details for such website")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:", font=('Arial', 16, "bold"))
label_website.grid(column=0, row=1)

label_username = Label(text="Email/Username:", font=('Arial', 16, "bold"))
label_username.grid(column=0, row=2)

label_password = Label(text="Password:", font=('Arial', 16, "bold"))
label_password.grid(column=0, row=3)

entry_website = Entry(width=20)
entry_website.grid(column=1, row=1)
entry_website.focus()

entry_username = Entry(width=33)
entry_username.grid(column=1, row=2, columnspan=2)
entry_username.insert(0, "annkka3@yandex.ru")

entry_password = Entry(width=20)
entry_password.grid(column=1, row=3)

button_generate = Button(text="Generate", width=11, command=generate, font=('Arial', 12, "bold"))
button_generate.grid(column=2, row=3)

button_save = Button(text="Add", width=40, command=save, font=('Arial', 12, "bold"))
button_save.grid(column=1, row=4, columnspan=2)

button_generate = Button(text="Search", width=11, command=search, font=('Arial', 12, "bold"))
button_generate.grid(column=2, row=1)

window.mainloop()
