# 'Scrollbar' with Tkinter module
# Author: Valeriy B.
# Language: Python 3.8.5


# importing the module
from tkinter import *


# creating the main window
root = Tk()
root.title("Scrollbar")


# creating a scrollbar
scb = Scrollbar(root)
scb.pack(side = RIGHT, fill = Y)


# creating a text box
txt = Text(root,width=40,height=3,font='12', yscrollcommand = scb.set)


txt.pack()
scb.config(command = txt.yview)


root.mainloop()