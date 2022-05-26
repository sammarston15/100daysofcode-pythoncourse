import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# create label in window
label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# the packer is what allows the label to show on the screen in the window
label.pack(side="left")










window.mainloop()

