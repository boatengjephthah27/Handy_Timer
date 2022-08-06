from tkinter import *
import math


# ------------------------------------------------ CONSTANTS -------------------------------------------------------
ash = '#4B5D67'
green = '#3CCF4E'
red = '#FF1E00'
lime = '#49FF00'
yellow = '#FFD93D'
work_min = 3
s_break = 1
l_break = 2
reps = 0
timer_count = None




# ------------------------------------------------ TIMER RESET -------------------------------------------------------

def reset_timer():
    canvas.after_cancel(timer_count)
    canvas.itemconfig(timer, text="00:00")
    title.config(text="TIMER", fg="#140303")
    checkMark.config(text="")
    global reps
    reps = 0
    
    
    
    
    
    
# ------------------------------------------------ TIMER MECHANISM -------------------------------------------------------

def start_timer():
    global reps
    reps += 1

    work_min_sec = work_min * 60
    s_break_sec = s_break * 60
    l_break_sec = l_break * 60
    
    w_rep = [1,3,5,7]
    sb_rep = [2,4,6]
    lb_rep = 8
    
    if reps in w_rep:
        countDown(work_min_sec)
        title.config(text="WORKING", fg=red)
    elif reps in sb_rep:
        countDown(s_break_sec)
        title.config(text="SHORT BREAK", fg=lime)
    elif reps == lb_rep:
        countDown(l_break_sec)
        title.config(text="LONG BREAK", fg=yellow)
        





# ------------------------------------------------ COUNTDOWN MECHANISM -------------------------------------------------------

def countDown(count):
    
    min = math.floor(count/60)
    sec = count % 60
    
    hand = [min,sec]
    
    if min < 10:
        min = f"0{min}"
    if sec < 10:
        sec = f"0{sec}"
    
    
    
    canvas.itemconfig(timer, text=f"{min}:{sec}")
    if count > 0:
        global timer_count
        timer_count = app.after(100, countDown, count-1)
    else:
        start_timer()
        checks = ""
        work_rounds = math.floor(reps/2)
        for i in range(work_rounds):
            checks += "✅"
        checkMark.config(text=checks)
            





# ------------------------------------------------ UI SETUP -------------------------------------------------------

app = Tk()
app.title("Handy Timer")
app.config(padx=50 ,pady=20, bg=ash)
app.resizable(False, False)


# title label
title = Label(text="TIMER", bg=ash, font=("COURIER", 50, "bold"))
title.grid(row=0, column=1)


# Start and stop button
start = Button(text="START", bg=ash, fg=green, highlightthickness=0, padx=5, pady=5, font=("MONTSERRAT", 20, "bold"), command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="RESET", fg=red, padx=5, pady=5,  highlightthickness=0, font=("MONTSERRAT", 20, "bold"), command=reset_timer )
reset.grid(row=2, column=2)

# CHECK mark

checkMark = Label(bg=ash, fg="BLACK", font=("MONTSERRAT", 30, "bold"))
checkMark.grid(row=3, column=1)

# creating the canvas
canvas = Canvas(width=465, height=300, bg=ash, highlightthickness=0)

# adding an image to the canvas
background_img = PhotoImage(file="./pck.png")
canvas.create_image(140, 150, image=background_img)

# adding text to the canvas
timer = canvas.create_text(375, 150, text="00:00", font=("COURIER", 60, "bold"))
canvas.grid(row=1, column=1)



app.mainloop()