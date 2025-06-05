# This is the Mile to Kilometer Project
# You can just simply run this file and have some fun calculating distances!

from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Labels

def print_result(value_km):
    label_value.config(text=f"{value_km}")

label_one = Label(text="Miles", font=("Arial", 14))
label_one.grid(column=2, row=0)

label_two = Label(text="is equal to", font=("Arial", 14))
label_two.grid(column=0, row=1)

label_three = Label(text="Km", font=("Arial", 14))
label_three.grid(column=2, row=1)

label_value = Label(text="0", font=("Arial", 14))
label_value.grid(column=1, row=1)

# Entry

entry = Entry(width=10)
entry.grid(column=1, row=0)
entry.insert(END, string="0")

# Button

def calculator():
    value_miles = int(entry.get())
    if value_miles < 0:
        print_result(0)
        return 0
    value_km = round(value_miles * 1.609, 2)
    print_result(value_km)

button = Button(text="Calculate", command=calculator)
button.grid(column=1, row=2)

window.mainloop()