from platform import release
import time

from tkinter.scrolledtext import ScrolledText

presses = [] 
releases = []
time_to_press = []
times_between_keys = []

def show_p(event):

    presses.append((event.char, time.time_ns()))
    print("Pressed Key", event.char, time.time_ns())

def show_r(event):

    releases.append((event.char,time.time_ns()))
    print("Released Key", event.char, time.time_ns())

def hello(event):

    print("Current State of Data:")
    for i in range(len(presses)):
        j = i
        found = False
        while j < len(releases) and not found:
            if presses[i][0] == releases[j][0]:
                time_to_press.append((presses[i][0],releases[j][1] - presses[i][1]))
                found = True
            j = j + 1
    print("The times key was held down for in nanoseconds: \n", time_to_press)    
    for i in range(1,len(presses)):
        j = i
        found = False
        while j < len(releases) and not found:
            if presses[i][0] == releases[j][0]:
                times_between_keys.append((presses[i][0],presses[j][1] - releases[i-1][1]))
                found = True
            j = j + 1
    print("The time between two keypresses: \n", times_between_keys)
    print("Single Click, Button-l")

def quit(event):

    print("Double Click, so let's stop")

    import sys; sys.exit()

widget = ScrolledText(None)

widget.pack()

widget.bind('<Key>', show_p)

widget.bind('<KeyRelease>', show_r)

widget.bind('<Button-1>', hello)

widget.bind('<Double-1>', quit)

widget.focus()

widget.mainloop()