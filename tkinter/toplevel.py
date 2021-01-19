# 'Toplevel' window with Tkinter module
# Author: Valeriy B.
# Language: Python 3.8.5


# importing the module
from tkinter import *


# creating the main window
root = Tk()
root.title("Toplevel")


# creating the first toplevel window
win1 = Toplevel(root, relief = SUNKEN, bd = 10, bg = "lightblue")
win1.title("First toplevel window")
win1.minsize(width=400, height=200)


# creating the second toplevel window
win1 = Toplevel(root, relief = SUNKEN, bd = 10, bg = "lightyellow")
win1.title("Second toplevel window")
win1.minsize(width=600, height=400)


root.mainloop()