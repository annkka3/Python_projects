from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Mile to km converter")
window.config(padx=30, pady=30)




#labels
label_is_equal= Label(text="is equal to", font=("Arial", 16, "bold"))
label_is_equal.grid(column=0, row=1)
label_miles= Label(text="Mlies", font=("Arial", 16, "bold"))
label_miles.grid(column=2, row=0)
label_km= Label(text="km", font=("Arial", 16, "bold"))
label_km.grid(column=2, row=1)
label_km_amount= Label(text="0", font=("Arial", 16, "bold"))
label_km_amount.grid(column=1, row=1)

#Button
#calls action() when pressed

def calculation():
    km_calc = float(input.get())*1.609344
    label_km_amount.config(text=f"{km_calc}")
button = Button(text="Calculate", command=calculation,font=("Arial", 16, "bold"))
button.grid(column=1, row=2)

#Entry
input = Entry(width=10)
input.grid(column=1, row=0)


window.mainloop()


