import time

from tkinter.scrolledtext import ScrolledText

def show_p(event) -> int:

    print("Pressed Key", event.char, time.time_ns())
    return time.time_ns()

def show_r(event, _pressTime: int) -> int:

    btwPress_and_Rls = time_between()
    print("Released Key", event.char, time.time_ns())

def hello(event):

    print("Single Click, Button-l")

def quit(event):

    print("Double Click, so let's stop")

    import sys; sys.exit()

def time_between(time1: int, time2: int) -> int:
    print("Time between press and release: {0}", time2 - time1)
    return time2 - time1
 

widget = ScrolledText(None)

widget.pack()

pressTime = widget.bind('<Key>', show_p)

widget.bind('<KeyRelease>', show_r)

widget.bind('<Button-1>', hello)

widget.bind('<Double-1>', quit)

widget.focus()

widget.mainloop()