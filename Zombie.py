#Choose.py
# by [Taylor Hoyt]{Carlos Pliego}(Bradley McMahan), Andy Ramirez
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
    messagebox.showinfo("Title", "Your name is Taylor. "" You're at your house when you hear a loud explosion." "You run outside and you're met with chaos, it's the start of the Apocalypse!!")
    messagebox.showinfo("Start", "You're home alone and running out of food and medicine. You have two options, go to the hospital or go to the supermarket. ")
    choice = simpledialog.askinteger("Choose wisely",
                                   "Choose 1 if you want to go to the supermarket. Choose 2 if you want some medicine: Type 1 or 2.")
    if choice == 1:
        SuperMarket()
    elif choice == 2:
        Hospital()
    else:
        intro()

################  Taylor Functions #####################
def SuperMarket():
    choice = simpledialog.askinteger("",
                                     "You find a group, Do you trust them or keep moving.  Now you must choose 1 to go with them or 2 to stay in the store.")
    if (choice == 1):
        messagebox.showinfo("The End",
                            " The group are cannibals!! There is no escape. You did not survive the Apocalypse!")

    elif (choice == 2):
        messagebox.showinfo("",
                            " You chose to continue looking in the store. You find a food truck")
    else:
        SuperMarket()

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
        
################ Andy Functions ############
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
