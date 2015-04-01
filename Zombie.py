# Choose.py
# by [Taylor Hoyt]{Carlos Pliego}(Bradley McMahan)
# Description: starter code for the Choose Your
# Own Adventure Project

# Import Statements
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox

root = Tk()
w = Label(root, text="Choose Your Own Adventure")
w.pack()

def intro():
    """ Introductory Function -> starts the story going """
    messagebox.showinfo("Title", "You're name is Tom. "" Your at your house when you hear a loud expolsion." "You run outside and your're met with choas, it's the start of the Apocalypse!!")
    messagebox.showinfo("Start", "You're home alone and running out of food and medicine. You have two options go to the hospital or go to the super market. ")
    choice = simpledialog.askinteger("Choose wisely",
                                   "Choose 1 if you want to go to the super market. Choose 2 if you want some medicine: Type 1 or 2.")
    if choice == 1:
        choice1()
    elif choice == 2:
        choice2()
    else:
        intro()

################ Student A Functions #####################
def choice1():
    choice = simpledialog.askinteger("Choose wisely",
                                     "This is the next part of the story.  Now you must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("The End",
                            "You chose right.  THE END")

    elif (choice == 2):
        messagebox.showinfo("The End",
                            "You chose ok.  THE END")
    else:
        choice1()

################ Student B Functions #####################
def choice2():
    choice = simpledialog.askinteger("Choose wisely",
                                     "This is the next part of the story.  Now you must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("The End",
                            "You chose right.  THE END")

    elif (choice == 2):
        messagebox.showinfo("The End",
                            "You chose ok.  THE END")
    else:
        choice2()

################ Main #####################
intro()

root.destroy()
