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
                                   "Choose wisley: 1 to go to the Hospital, 2 for the store, 3 to go Downtown, 4 to stay home.")
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
def Store():
    choice = simpledialog.askinteger("Store",
                                     "When you're at the store you run into another group, do you 1 go with them or 2 continue looking for food?  ")
    if (choice == 1):
        messagebox.showinfo("Leave with group",
                            "The group are cannibals!You must escape quickly")
        Leavewithgroup()

    elif (choice == 2):
        messagebox.showinfo("Continue at store",
                            "You need to find food")
        Continueatstore()
    else:
        Store()



def Leavewithgroup():

    messagebox.showinfo("With Group" , " You find out they are cannibals. Are you next?")
    
    choice = simpledialog.askinteger("",
                                     "You have two options: 1 try to escape or 2 stay with the group. ")
    if (choice == 1):
        messagebox.showinfo("",
                            " You try to escape, you run down an alley and manage to lose them!")
        ER()

    elif (choice == 2):
        messagebox.showinfo("",
                            "You stay with the gruop and go to thier base")
        
        
        Staywithgroup()
    else:
        Hospital()



def Continueatstore():

    messagebox.showinfo("Store" , " You see a food truck. You check and see its full of food!") 
    
    choice = simpledialog.askinteger("",
                                     "You have two options: 1 take the truck or 2 continue looking in the store. ")
    if (choice == 1):
        messagebox.showinfo("",
                            "You can't pass this up you need the food.")
        TakeTruck()

    elif (choice == 2):("",
                        "It's to risky you'll never make it back, you go back inside.")
   
    
    else:
        Continueatstore()

def TakeTruck():

    messagebox.showinfo("You took the truck" , "You have to get home as fast as you can!")
    
    choice = simpledialog.askinteger("",
                                     " You can take the 1 main road and save time or take the 2 backroads and take longer.")
    if (choice == 1):
        messagebox.showinfo("",
                            "You take the main road and you're overun! You are dead.")
        

    elif (choice == 2):("",
                        "You take the backroads and make it to your house. You have saved yourself and your family.")
  
    else:
        TakeTruck()





def ContinueLooking():

    messagebox.showinfo("" , " The store is overun you have to find an exit.")
    
    choice = simpledialog.askinteger("",
                                     "You have two options: 1 fight off the zombies or 2 try to find an exit.")
    if (choice == 1):
        messagebox.showinfo("",
                            "There's to many off them you get overun! You are dead")
        ER()

    elif (choice == 2):
        messagebox.showinfo("",
                            "You spot the exit and make a run for it, you suddenly hear gunfire! You are saved by the army. You have Survived!")
        
        
        Doc()
    else:
        Hospital()
        
################ Andy Functions ############
def DownTown():

    messagebox.showinfo("DownTown" , " You have arrived Downtown and see that most of the city is overrun with Zombies already.")
    
    choice = simpledialog.askinteger("",
                                     "You have two choices: 1 to run into to mall and gather supplies.  2 to steal a bus and try and escape from the city.")
    if (choice == 1):
        messagebox.showinfo("Mall",
                            "You walk into the mall and forget to close the doors at the entrance. A horde of zombies follow you into the mall and start running towards you. You are cornered.")
        Mall()

    elif (choice == 2):
        
        
        Bus()
    else:
        DownTown()

def Mall():
    
    messagebox.showinfo("Mall" , "You have 2 choices")

    choice = simpledialog.askinteger("" , "Type 1 to Give Up and let the zombies kill you. Type 2 to try and fight off the zombies.")

    if (choice == 1):
        
        GiveUp()

    elif (choice == 2):
        
        Fight()

    else:
        Mall()
    

def GiveUp():

     messagebox.showinfo("Dead" , "")
     Dead()

     

def Fight():
    
    messagebox.showinfo("" , " You look behind you and see a baseball bat and a crow bar. ")

    choice = simpledialog.askinteger("" , "Choose 1 for the Baseball Bat, Choose 2 for the Crow Bar.")

    if (choice == 1):
        
        messagebox.showinfo("Bat" , "The baseball bat breaks when you hit the first Zombie and the rest of them rush at you, leaving you no time to reach for the crow bar.")
        Dead()

    elif (choice == 2):
        
        messagebox.showinfo("" , " You grabbed the crow bar and started fighting off the zombies but more and more keep coming. There is now too many zombies for you to fight off. ")
        Dead()
    

    else:
        Fight()


def Winner():
    messagebox.showinfo("Winner" , "Congratulations, You and your bus full of survivors, survived the Apocalypse ")
def Dead():
    messagebox.showinfo("Dead" , "The zombies killed you")





def Bus():
    messagebox.showinfo("Bus" , "You find a working bus and spend the rest of your life recruiting survivors to join you on the bus and help gather supplies.")

    Winner()



############ Brad's Functions ##############
def StayHome():
    choice = simpledialog.askinteger("StayHome",
                                     "If you decide to stay home, Choose 1, if you want to leave, Choose 2")
    if (choice == 1):
        messagebox.showinfo("StayHome",
                            "You choose to stay home, and hear people outside.")
        PeopleOutside()

    elif (choice == 2):
        messagebox.showinfo("Leave",
                       "You choose to leave your house. You see a group of people in the distance.")
        PeopleinDistance()
    else:
        StayHome()





def PeopleOutside():

    messagebox.showinfo("PeopleOutside" , "You see 5 people through the blinds, they are coming right to your house, choose 1 to run out the back door, choose 2 if you want to open the door to let them in")
    
    choice = simpledialog.askinteger("PeopleOutside",
                                     "You have two options: 1 is to run out the back door, 2 is to let them in.")
    if (choice == 1):
        messagebox.showinfo("RunOutBack",
                            "You run out the back door into the forest behind your house, but trip and fall on a branch and a zombie kills eats you.")
        dead()

    elif (choice == 2):
        messagebox.showinfo("LetThemIn" , "You let them in and they tie you up and take you hostage and kill you")
        dead()
        

    else:
        PeopleOutside()



def PeopleinDistance():

    messagebox.showinfo("PeopleinDistance" , "The people in the distance are holding guns and food.")
    
    choice = simpledialog.askinteger("PeopleinDistance",
                                     "You have two options: 1 try and talk to them, 2 to hide behind a mailbox and let them pass.")
    if (choice == 1):
        messagebox.showinfo("",
                            "You approach them and they are cannibals and kill you. The End")
        dead() 

    elif (choice == 2):
        messagebox.showinfo("", "You hide behind the mailbox, but while hiding a zombie tackles you and brings you to the ground, you hear a loud bang and the zombie is dead. They group of people Shot the zombie and help you up.")
        
    
        Help()
    else:
        PeopleinDistance()





def Help():

    messagebox.showinfo("Help" , "After you get up, they ask you if you want to join their group or go back home.")
    
    choice = simpledialog.askinteger("",
                                     "You have two options: 1 to go with group, 2 for going back home. ")
    if (choice == 1):
        messagebox.showinfo("",
                            "You go back with the group and live safely at their barricaded town.")
        winner()

    elif (choice == 2):
        messagebox.showinfo("", "The group gets angry you won't go with them, so they take you hostage and feed you to the zombies.")
        
        
        dead()
    else:
        Help()

def winner():

    messagebox.showinfo("" , "YOU SURVIVED!")
    
    

def dead():

    messagebox.showinfo("" , "SORRY YOU DIED!")







################ Main #####################
        
intro()

root.destroy()
