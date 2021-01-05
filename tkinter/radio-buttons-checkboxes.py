# Feedback form with Tkinter module
# Author: Valeriy B.
# Language: Python 3.8.5


# importing the module
from tkinter import *


# logic functions
def radiobuttons():
    if var.get() == 0:
        return "0-10"
    elif var.get() == 1:
        return "11-20"
    elif var.get() == 2:
        return "21-30"
    elif var.get() == 3:
        return "31-40"


def checkboxes():
    check_list = []
    if c1.get() == 1:
        check_list.append("RED")
    if c2.get() == 1:
        check_list.append("BLUE")
    if c3.get() == 1:
        check_list.append("GREEN")
    if c4.get() == 1:
        check_list.append("YELLOW")
    return " ".join(check_list)

# printing the result
def print_result():
    r = radiobuttons()
    c = checkboxes()
    print("Result: Pieces - " + r + " , Colors - " + c)

# creating the main window
window = Tk()
window.title("Feedback Form")


# setting window size
window.geometry('400x400')


# creating radio buttons section
radio_label = Label(window, text='How many pieces?').pack()
var = IntVar()
var.set(1)
rad0 = Radiobutton(window, text='0-10', variable = var, value=0).pack()
rad1 = Radiobutton(window, text='11-20', variable = var, value=1).pack()
rad2 = Radiobutton(window, text='21-30', variable = var, value=2).pack()
rad3 = Radiobutton(window, text='31-40', variable = var, value=3).pack()


# creating checkboxes section
checkbox_label = Label(window, text='Pick a color').pack()
c1 = IntVar()
c2 = IntVar()
c3 = IntVar()
c4 = IntVar()
che1 = Checkbutton(window, text='RED', bg='red', variable=c1, onvalue=1, offvalue=0).pack()
che2 = Checkbutton(window, text='BLUE', bg='blue', variable=c2, onvalue=1, offvalue=0).pack()
che3 = Checkbutton(window, text='GREEN', bg='green', variable=c3, onvalue=1, offvalue=0).pack()
che4 = Checkbutton(window, text='YELLOW', bg='yellow', variable=c4, onvalue=1, offvalue=0).pack()

# submit button
submit = Button(window, text='Send', width=20, bg='sky blue', command=print_result).pack()


window.mainloop()