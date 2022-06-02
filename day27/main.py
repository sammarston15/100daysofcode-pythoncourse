from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# create label in window
label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# the packer is what allows the label to show on the screen in the window
label.grid(column=0, row=0)
label.config(padx=50, pady=50)

# Button
def button_clicked():
    print("I got clicked")
    new_input = input.get()
    label.config(text=new_input)

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=3, row=0)

# Entry
input = Entry(width=10)
input.grid(column=4, row=3)






window.mainloop()

