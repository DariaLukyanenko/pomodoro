# TODO import tkinter
from time import sleep
from tkinter import IntVar, StringVar, Tk, Canvas, PhotoImage, Button, Label
from tkinter import ttk
import datetime


# ---------------------------- CONSTANTS ------------------------------- #
# TODO 1 
# Put all constants of the project below
# For example
# WORK_TIME = 60*20
WORK_TIME = 60 * 25 
LONG_BREAK = 60 * 20 
SHORT_BREAK = 60 * 5 
reps = 0
GREEN = "#DCFFB7"
ORANGE = "#FFBB64"
YELLOW= '#FFEAA7'
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    
    # TODO reset all interface and labels

# TODO 2 
# If it's work time, change top label to Work
# If it's long&short break time, change top label to Break


# ---------------------------- TIMER MECHANISM ------------------------------- #
def stop_timer(stop):
    minute = stop // 60 # HINT // 
    second = stop % 60 # HINT % 
    if stop>=0:
        if second < 10:
            canvas.itemconfig(timer_text, text=f'{minute}:0{second}')
        else:
            canvas.itemconfig(timer_text, text=f'{minute}:{second}')
        global timer
        timer = window.after(2, stop_timer, stop-1)
    else:
        start_timer()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_timer():
    # 25 - > 5
    global WORK_TIME
    global LONG_BREAK
    global SHORT_BREAK
    # TODO If it's 

    global reps
    reps+=1
    mark = reps//2*'+'


    if reps%2==0:
        top_label.config(text=f'Short Break {mark}')
        stop_timer(SHORT_BREAK)
    
    if reps%2!=0:
        top_label.config(text=f'Work {mark}')
        stop_timer(WORK_TIME)

    if reps%2==0 and reps==8:
        top_label.config(text=f'Long Break'+'++++')
        stop_timer(LONG_BREAK)

    
    
    
# ---------------------------- UI SETUP ------------------------------- #
# TODO Set bg to a color
# TODO Improve size of the text
# TODO Set color of text
window = Tk()
window.configure(bg=GREEN,padx=50)
window.minsize(500, 500)
canvas = Canvas(bg=GREEN, highlightthickness=0)
timer = StringVar()
img = PhotoImage(file='1.png')
canvas.create_image(220,125,image=img)
timer_text = canvas.create_text(220,125, text='00:00',font=('Helvetica', 36))
canvas.grid(column=2, row=1)
start = Button(window, text='START', command= start_timer, bg=YELLOW).grid(column=1,row=3)
reset = Button(window, text='RESET', command=reset, bg=YELLOW).grid(column=3,row=3)
label = Label(window, text='TIMER', bg=GREEN, fg=ORANGE, font=('Helvetica', 20)).grid(column=2,row=0)
top_label = Label(window, text='Time', font=('Helvetica', 16), bg=GREEN, fg=ORANGE)
top_label.grid(column=2, row=3)
window.mainloop()
