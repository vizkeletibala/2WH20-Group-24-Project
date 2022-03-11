from platform import release
import time

from tkinter.scrolledtext import ScrolledText

presses = []
releases = []
time_to_press = []
times_between_keys = []

def show_p(event):

    presses.append(time.time_ns())
    print("Pressed Key", event.char, time.time_ns())

def show_r(event):

    releases.append(time.time_ns())
    print("Released Key", event.char, time.time_ns())

def hello(event):

    print("Current State of Data:")
    for i in range(len(presses)):
        time_to_press.append(releases[i] - presses[i])
        print("The times a key was held down for in nanoseconds: {0} \n", time_to_press[i])
    for i in range(1,len(presses)):
        times_between_keys.append(presses[i] - releases[i-1])
        print("The times between key presses in nanoseconds: {0} \n", times_between_keys[i-1])
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