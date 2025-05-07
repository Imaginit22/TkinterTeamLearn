from tkinter import *
from ctypes import windll

#this is a py file
print("Hello guys whats up it is I Noah")
print("Hello guys whats up it is I Noah")

#I'm just making sure I remeber how to use github desktop
#i purposely spelled remeber remeber

def test1():
    # create root window
    root = Tk()
    # root window title and dimension
    root.title("Thomas might be the gote")
    # Set geometry (widthxheight)
    root.geometry('100x100+65+400')
    hi = Label(root, text="He")
    hi.pack()
    # all widgets will be here
    # Execute Tkinter
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        root.mainloop()
test1()
