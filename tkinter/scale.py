# 'Scale' with Tkinter module
# Author: Valeriy B.
# Language: Python 3.8.5


# importing the module
from tkinter import *


# creating the main window
root = Tk()
root.title("Scale")


# creating frameworks
fra1 = Frame(root,width=700,height=200,bg="lightgreen",bd=20)
fra2 = Frame(root,width=300,height=50,bg="green",bd=20)
fra3 = Frame(root)


# creating a scale
sca1 = Scale(fra1,orient=HORIZONTAL,length=300,from_=0,to=100,tickinterval=10,resolution=5).pack()
ent1 = Entry(fra2,width=20).pack()


# packing the frames widgets
fra1.pack()
fra2.pack()


root.mainloop()