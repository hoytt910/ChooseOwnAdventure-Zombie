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
    messagebox.showinfo("Start", "You're home alone and running out of food and medicine. You have four options, go to the hospital , store , down town, or stay home. ")
    choice = simpledialog.askinteger("Choose wisely",
                                   "Choose wisley: 1 to go to the Hospital, 2 for the store, 3 for down town, 4 to stay home.")
    if choice == 1:
        Hospital()
    elif choice == 2:
        Store()
    elif choice == 3:
        DownTown()
    elif choice == 4:
        StayHome()
    else:
        intro()

################  Taylor Functions #####################
def Hospital():

    messagebox.showinfo("Hospital" , " After entering the hospital you see two doors. One says E.R. the other says Doctors Office.")
    
    choice = simpledialog.askinteger("",
                                     "You have two options: 1 for ER or 2 for Doctors Office. ")
    if (choice == 1):
        messagebox.showinfo("E.R.",
                            "When opening the door to the E.R. you are faced with a zombie that tackles you to the ground. You have to  ")

    elif (choice == 2):
        messagebox.showinfo("Hospital",
                            " You chose to continue looking in the store. You find a food truck")
    else:
        Hospital()




################ Carlos Functions #####################
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
############ Brad's Functions ##############
def choice2():
    choice = simpledialog.askinteger("",
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
