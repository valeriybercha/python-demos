# 'Hello, World' application with Tkinter module
# Author: Valeriy B.
# Language: Python 3.8.5


# importing the module
from tkinter import *


# creating 'hello world' function
def hello_world(event):
    print("Hello, World! First app with Tkinter")


# creating the main window
window = Tk()


# setting window size
window.geometry('150x150')


# Button settings
but = Button(window)
but['text'] = "Print"
but.bind("<Button-1>", hello_world)
but.pack()


# mainloop
window.mainloop()
