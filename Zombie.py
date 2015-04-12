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
                            "When opening the door to the E.R. you are faced with a zombie that tackles you to the ground.")
        ER()

    elif (choice == 2):
        
        
        Doc()
    else:
        Hospital()

def ER():
    
    messagebox.showinfo("ER" , "While on the ground you notice a hammer to your right. You can easily push the zombie off but you might be able to kill it.You have two options. 1 to push the zombie off(Likley) or 2 go for the kill(Risky)!  ")

    choice = simpledialog.askinteger("" , "Type 1 to push. Type 2 to go for the kill.")

    if (choice == 1):
        
        messagebox.showinfo("Push" , "You push the zombie off and run into a side room. As you shut the door you hear a zombie groan and are bit on the sholder.")
        Push()

    elif (choice == 2):
        
        messagebox.showinfo("" , " When trying to grab the hammer the zombie overpowers you. Right when the zombie is about to bite you a group of three people pulls the zombie off of you. The Group asked you if you want to join them.")
        Hammer()
    else:
        ER()
    

def Push():

     messagebox.showinfo("Dead" , "You have been bitten. You are DEAD!")

     

def Hammer():
    
    messagebox.showinfo("What to do?" , " They said the need another member in there team.")

    choice = simpledialog.askinteger("" , "Type 1 to go with them. Type 2 to go back home.")

    if (choice == 1):
        
        messagebox.showinfo("Team" , "You chose to go with the group of three they bring you back to the military base they came from.")
        Winner()

    elif (choice == 2):
        
        messagebox.showinfo("" , " You chose to go home and not go with the group of three.")
        Dead()
    

    else:
        Hammer()


def Winner():
    messagebox.showinfo("Winner" , " You live in the military base for the rest of your life. Winner!!")
def Dead():
    messagebox.showinfo("Dead" , " When leaving the hospital there is a zombie horde and you get swarmed by 7 zombies and die.")





def Doc():
    messagebox.showinfo("Doc Office" , " While walking into the Doctors Office a zombie jumps out and bites you. You should have gone in the ER. Your Dead!")


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



def Hospital():

    messagebox.showinfo("Hospital" , " After entering the hospital you see two doors. One says E.R. the other says Doctors Office.")
    
    choice = simpledialog.askinteger("",
                                     "You have two options: 1 for ER or 2 for Doctors Office. ")
    if (choice == 1):
        messagebox.showinfo("E.R.",
                            "When opening the door to the E.R. you are faced with a zombie that tackles you to the ground.")
        ER()

    elif (choice == 2):
        
        
        Doc()
    else:
        Hospital()



def Hospital():

    messagebox.showinfo("Hospital" , " After entering the hospital you see two doors. One says E.R. the other says Doctors Office.")
    
    choice = simpledialog.askinteger("",
                                     "You have two options: 1 for ER or 2 for Doctors Office. ")
    if (choice == 1):
        messagebox.showinfo("E.R.",
                            "When opening the door to the E.R. you are faced with a zombie that tackles you to the ground.")
        ER()

    elif (choice == 2):
        
        
        Doc()
    else:
        Hospital()

def Hospital():

    messagebox.showinfo("Hospital" , " After entering the hospital you see two doors. One says E.R. the other says Doctors Office.")
    
    choice = simpledialog.askinteger("",
                                     "You have two options: 1 for ER or 2 for Doctors Office. ")
    if (choice == 1):
        messagebox.showinfo("E.R.",
                            "When opening the door to the E.R. you are faced with a zombie that tackles you to the ground.")
        ER()

    elif (choice == 2):
        
        
        Doc()
    else:
        Hospital()




def Hospital():

    messagebox.showinfo("Hospital" , " After entering the hospital you see two doors. One says E.R. the other says Doctors Office.")
    
    choice = simpledialog.askinteger("",
                                     "You have two options: 1 for ER or 2 for Doctors Office. ")
    if (choice == 1):
        messagebox.showinfo("E.R.",
                            "When opening the door to the E.R. you are faced with a zombie that tackles you to the ground.")
        ER()

    elif (choice == 2):
        
        
        Doc()
    else:
        Hospital()


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



def Hospital():

    messagebox.showinfo("Hospital" , " After entering the hospital you see two doors. One says E.R. the other says Doctors Office.")
    
    choice = simpledialog.askinteger("",
                                     "You have two options: 1 for ER or 2 for Doctors Office. ")
    if (choice == 1):
        messagebox.showinfo("E.R.",
                            "When opening the door to the E.R. you are faced with a zombie that tackles you to the ground.")
        ER()

    elif (choice == 2):
        
        
        Doc()
    else:
        Hospital()


def Hospital():

    messagebox.showinfo("Hospital" , " After entering the hospital you see two doors. One says E.R. the other says Doctors Office.")
    
    choice = simpledialog.askinteger("",
                                     "You have two options: 1 for ER or 2 for Doctors Office. ")
    if (choice == 1):
        messagebox.showinfo("E.R.",
                            "When opening the door to the E.R. you are faced with a zombie that tackles you to the ground.")
        ER()

    elif (choice == 2):
        
        
        Doc()
    else:
        Hospital()



def Hospital():

    messagebox.showinfo("Hospital" , " After entering the hospital you see two doors. One says E.R. the other says Doctors Office.")
    
    choice = simpledialog.askinteger("",
                                     "You have two options: 1 for ER or 2 for Doctors Office. ")
    if (choice == 1):
        messagebox.showinfo("E.R.",
                            "When opening the door to the E.R. you are faced with a zombie that tackles you to the ground.")
        ER()

    elif (choice == 2):
        
        
        Doc()
    else:
        Hospital()





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





def Hospital():

    messagebox.showinfo("Hospital" , " After entering the hospital you see two doors. One says E.R. the other says Doctors Office.")
    
    choice = simpledialog.askinteger("",
                                     "You have two options: 1 for ER or 2 for Doctors Office. ")
    if (choice == 1):
        messagebox.showinfo("E.R.",
                            "When opening the door to the E.R. you are faced with a zombie that tackles you to the ground.")
        ER()

    elif (choice == 2):
        
        
        Doc()
    else:
        Hospital()




def Hospital():

    messagebox.showinfo("Hospital" , " After entering the hospital you see two doors. One says E.R. the other says Doctors Office.")
    
    choice = simpledialog.askinteger("",
                                     "You have two options: 1 for ER or 2 for Doctors Office. ")
    if (choice == 1):
        messagebox.showinfo("E.R.",
                            "When opening the door to the E.R. you are faced with a zombie that tackles you to the ground.")
        ER()

    elif (choice == 2):
        
        
        Doc()
    else:
        Hospital()





def Hospital():

    messagebox.showinfo("Hospital" , " After entering the hospital you see two doors. One says E.R. the other says Doctors Office.")
    
    choice = simpledialog.askinteger("",
                                     "You have two options: 1 for ER or 2 for Doctors Office. ")
    if (choice == 1):
        messagebox.showinfo("E.R.",
                            "When opening the door to the E.R. you are faced with a zombie that tackles you to the ground.")
        ER()

    elif (choice == 2):
        
        
        Doc()
    else:
        Hospital()












################ Main #####################
        
intro()

root.destroy()
