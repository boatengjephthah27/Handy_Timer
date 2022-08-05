from tkinter import *


# ------------------------------------------------ CONSTANTS -------------------------------------------------------
ash = '#4B5D67'
green = '#3CCF4E'
red = '#FF1E00'

# ------------------------------------------------ UI SETUP -------------------------------------------------------

app = Tk()
app.title("Handy Timer")
app.config(padx=50 ,pady=20, bg=ash)
app.resizable(False, False)


# title label
title = Label(text="TIMER", bg=ash, font=("MONTSERRAT", 50, "bold"))
title.grid(row=0, column=1)


# Start and stop button
start = Button(text="START", bg=ash, fg=green, highlightthickness=0, padx=5, pady=5, font=("MONTSERRAT", 20, "bold") )
start.grid(row=2, column=0)

reset = Button(text="RESET", fg=red, padx=5, pady=5,  highlightthickness=0, font=("MONTSERRAT", 20, "bold") )
reset.grid(row=2, column=2)

# CHECK mark

checkMark = Label(text="✅", bg=ash, fg="BLACK", font=("MONTSERRAT", 30, "bold"))
checkMark.grid(row=3, column=1)

# creating the canvas
canvas = Canvas(width=450, height=300, bg=ash, highlightthickness=0)

# adding an image to the canvas
background_img = PhotoImage(file="./pck.png")
canvas.create_image(140, 150, image=background_img)

# adding text to the canvas
canvas.create_text(370, 150, text="00:00", font=("COURIER", 50, "bold"))
canvas.grid(row=1, column=1)





app.mainloop()