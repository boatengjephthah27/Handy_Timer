from tkinter import *


# ------------------------------------------------ CONSTANTS -------------------------------------------------------


# ------------------------------------------------ UI SETUP -------------------------------------------------------

app = Tk()
app.title("Handy Timer")
# app.config(padx=100, pady=60)
app.resizable(False, False)

# creating the canvas
canvas = Canvas(width=600, height=400)

# adding an image to the canvas
background_img = PhotoImage(file="./glass copy.png")
canvas.create_image(300, 200, image=background_img)
canvas.pack()





app.mainloop()