from tkinter import *
from classes import *
import os
import time

# initialisation de la fenetre
fenetre = Tk()
fenetre.title("Menus principal")
fenetre.geometry("250x400")

perdu=0
diff = 1
def start():
    # commande du bouton START
    game = Toplevel(fenetre)
    game.title("démineur")

    # mise en place d'un timer
    time_start = time.strftime("%H:%M:%S")
    time_start2 = time_start.split(":")
    # creation du plateau, mais aucune bombe
    plateau = Plateau(game,grey,disabled,i1,i2,i3,i4,i5,i6,dead,diff,perdu,flag,no_flag,time_start2)
    # les bombes sont placées
    plateau.create_mine()
    game.mainloop()


def change_difficult():
    # commande du bouton de difficultée
    global diff
    if diff==3:
        diff=1
    else:
        diff+=1
    difficult_variable.set(str(diff))

def fenetre_des_options():
    # commande du bouton OPTION
    fenetre_option = Toplevel(fenetre)
    fenetre_option.title("fenetre des options")
    fenetre_option.geometry("300x450")
    fenetre_option.mainloop()

def regles():
    # commande du bouton REGLES
    fenetre_regle = Toplevel(fenetre)
    fenetre_regle.title("fenetre des regles")
    fenetre_regle.geometry("300x450")
    fenetre_regle.mainloop()

# bouton START
start=Button(fenetre, text="START",command = start, width=20)
start.place(x=50, y=70)

# changer le difficulté
difficult_variable=StringVar(value="1")
difficult_button=Button(fenetre, text="Difficulter",command = change_difficult)
difficult_button.place(x=20, y=130)
difficult_label= Label(fenetre, text='0', textvariable =difficult_variable)
difficult_label.place(x=5,y=130)

# bouton OPTIONS
option_button=Button(fenetre, text="Options",command = fenetre_des_options)
option_button.place(x=20, y=160)

# bouton REGLES
regle_button=Button(fenetre, text="Règles du jeu",command = regles)
regle_button.place(x=20, y=190)

# utilisation du module os pour que les ressources soient chargés automatiquement
rep = os.getcwd()

# chargement des ressources
bomb=PhotoImage(file=rep + r"/ressources/bomb.PNG")
flag=PhotoImage(file=rep + r"/ressources/flag.PNG")
dead=PhotoImage(file=rep + r"/ressources/dead.PNG")
grey=PhotoImage(file=rep + r"/ressources/grey.PNG")
disabled=PhotoImage(file=rep + r"/ressources/disabled.PNG")
i1=PhotoImage(file=rep + r"/ressources/i1.PNG")
i2=PhotoImage(file=rep + r"/ressources/i2.PNG")
i3=PhotoImage(file=rep + r"/ressources/i3.PNG")
i4=PhotoImage(file=rep + r"/ressources/i4.png")
i5=PhotoImage(file=rep + r"/ressources/i5.png")
i6=PhotoImage(file=rep + r"/ressources/i6.PNG")
no_flag=PhotoImage(file=rep + r"/ressources/no_flag.png")
#i7=PhotoImage(file=rep + r"\ressources\i7.png")
#i8=PhotoImage(file=rep + r"\ressources\i8.png")

fenetre.mainloop()


