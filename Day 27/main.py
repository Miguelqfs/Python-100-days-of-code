# These are my first impressions about tkinter module
# The final project is in the file: mile_to_km_converter.py

from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200) # Padding (space)

# Label

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))

my_label["text"] = "New Text"
# OR
my_label.config(text="New Text")

my_label.config(padx=50, pady=50)

# Layout managers:
# my_label.pack() # Pack things next to each other
# my_label.place(x=0,y=0) # Specify the exact coordinate of the label
my_label.grid(column=0, row=0)

# Button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

# Entry

input = Entry(width=10)
input.grid(column=3, row=2)

# New button

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

window.mainloop()
