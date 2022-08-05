from tkinter import *


# ------------------------------------------------ CONSTANTS -------------------------------------------------------
ash = '#4B5D67'

# ------------------------------------------------ UI SETUP -------------------------------------------------------

app = Tk()
app.title("Handy Timer")
app.config(padx=50 ,pady=20, bg=ash)
app.resizable(False, False)


# title label
title = Label(text="TIMER", bg=ash, font=("MONTSERRAT", 70, "bold"))
title.grid(row=0, column=1)


# Start and stop button
start = Button(text="START", bg=ash, highlightthickness=0, font=("MONTSERRAT", 30, "bold") )
start.grid(row=2, column=0)

stop = Button(text="STOP", bg=ash, highlightthickness=0, font=("MONTSERRAT", 30, "bold") )
stop.grid(row=2, column=2)



# creating the canvas
canvas = Canvas(width=600, height=340, bg=ash, highlightthickness=0)

# adding an image to the canvas
background_img = PhotoImage(file="./pck.png")
canvas.create_image(150, 170, image=background_img)

# adding text to the canvas
canvas.create_text(460, 170, text="00:00", font=("COURIER", 80, "bold"))
canvas.grid(row=1, column=1)





app.mainloop()