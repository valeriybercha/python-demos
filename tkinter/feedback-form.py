# Feedback form with Tkinter module
# Author: Valeriy B.
# Language: Python 3.8.5

# importing the module
from tkinter import *


# creating 'print' information function
def print_info():
    user_email = email_input_field.get()
    user_message = message_text_field.get('1.0', END) # for text fields you have to specify the begin and the end of a text to print
    print(f"{user_email}: {user_message}")


# creating the main window
window = Tk()
window.title("Feedback Form")


# setting window size
window.geometry('400x400')


# creating a label for 'email' input field
email_label = Label(window, text="Your email:", bg='lemon chiffon')


# entry input field settings
email_input_field = Entry(window, width=20, bd=3, bg='lemon chiffon')


# 'comments' label settings
message_label = Label(window, text='Your message:')


# 'input field' settings
message_text_field = Text(window, width=25, height='5', wrap=WORD)


# button settings
submit = Button(window, text='Send', width=20, bg='sky blue', command=print_info)


# declaring widgets position
email_label.pack()
email_input_field.pack()
message_label.pack()
message_text_field.pack()
submit.pack()


# mainloop
window.mainloop()