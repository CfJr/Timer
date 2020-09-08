from tkinter import *
from tkinter import messagebox
import time

total = 0
exit = "play"

def store():
    if(entry_enter.get() != ""):
        button_store.configure(state=DISABLED)
        with open('Times.txt', "a") as handler:
            handler.write(entry_enter.get() + " : " + "[" + label_prev_time.cget("text") + "]" + "\n")
            entry_enter.delete(0, "end")
            label_prev_time.config(text="00:00:00")
    else:
        messagebox.showinfo(title="Timer", message="Please Enter Some Info For This Entry Before Storing!")

def pause():
    global exit
    if(total != 0):
        exit = "pause"
        button_pause.configure(state=DISABLED)
        button_start.configure(state=NORMAL)

def stop(): 
    global total
    global exit

    if(total != 0):
        label_prev_time.config(text=getTime())
        total = 0
        label_time.config(text=getTime())
        exit = "stop"
        button_start.configure(state=NORMAL)
        button_stop.configure(state=DISABLED)
        button_pause.configure(state=DISABLED)
        button_store.configure(state=NORMAL)

def getTime():

    global total

    def getSeconds():
        return ("0" + str(total%60))[-2:] #Returns seconds less than 60. -2: trims 010 and above to 10, 11, etc

    def getMinutes():
        return ("0" + str(total//60%60))[-2:]

    def getHours():
        return ("0" + str(total//60//60))[-2:]

    return getHours() + ":" + getMinutes() + ":" + getSeconds()

def counter():
    button_start.configure(state=DISABLED)
    button_stop.configure(state=NORMAL)
    button_pause.configure(state=NORMAL)
    global exit
    exit = "play"
    def count():
        global total
        global label_time
        if(exit == "play"):
            total += 1
            label_time.config(text=getTime())
            label_time.after(1000, count)
    count()


window = Tk()

window.title("Timer")

label_time = Label(window, text="00:00:00")
label_prev_time = Label(window, text="00:00:00")

entry_enter = Entry(window)

button_start = Button(window, text="     Start     ", command = counter)
button_pause = Button(window, text="     Pause     ", command = pause, state=DISABLED)
button_stop = Button(window, text= "     Stop     ", command = stop, state=DISABLED)
button_store = Button(window, text="     Store     ", command = store, state=DISABLED)

label_time.grid(row=0, columnspan=3)
label_prev_time.grid(row=4, column=2)

entry_enter.grid(row=4, column=0)

button_start.grid(row=2, column=0)
button_stop.grid(row=2, column=1)
button_pause.grid(row=2, column=2)
button_store.grid(row=6, columnspan=3)

mainloop()