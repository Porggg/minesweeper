from tkinter import *
import random
import time

class Plateau:
    def __init__(self, parent, grey, disabled, i1, i2, i3, i4, i5,i6, dead, difficlt, perdu, flag, no_flag, time_start):

        # initialisation et creation du plateau :
        self.parent = parent
        self.disabled = disabled
        self.image = [disabled,i1, i2, i3, i4, i5,i6]
        self.i1, self.i2, self.i3, self.i4, self.i5,self.i6 = i1, i2, i3, i4, i5,i6
        self.grey = grey
        self.flag = flag
        self.no_flag = no_flag
        self.difficlt = difficlt
        self.dead = dead
        self.time_start = time_start
        self.mode = 0 # le mode 0 = mode pour déminer
                      # le mode 1 = le mode qui pose des drapeaux

        # creation d'un dictionnaire de 10 frames...
        self.dicf = dict()
        for i in range(10*self.difficlt):
            self.dicf[i] = Frame(parent,bg = 'white')
            self.dicf[i].pack()

        # ... et dans chaque frame sont crées 10 boutons automatiquement...
        self.dicb = dict() # dictionnaires avec tout les boutons
        for i in range(100*self.difficlt):

            for j in range(100*self.difficlt):
                if i>=j*10*self.difficlt and  i<(j+1)*10*self.difficlt:

                    self.dicb[i] = Button(self.dicf[j], image = grey, justify = 'left') # l'argument justify est utilisé pour désigner le présence d'une bombe. 'left' = pas de bombe
                    # les boutons sont pack :                                                                                                                #  'right' = bombe
                    self.dicb[i].pack(side = LEFT)                                                                                                           #  'center' = case déjà cliquer

        # ici, ont rajoute aux boutons leurs commande (voir la méthode démine)
        for k in range(0,(100*self.difficlt)):
            self.dicb[k].config(command = lambda z = k: Plateau.demine(self,z,0))

        # bouton pour le mode drapeau
        self.drapeau_bouton = Button(parent, image = flag, command= lambda x = j: Plateau.change_mode(self))
        self.drapeau_bouton.pack()

    def change_mode(self):
        # commande du bouton qui change le mode du
        if self.mode == 0:
            self.drapeau_bouton["image"] = self.no_flag
            self.mode = 1
        else:
            self.drapeau_bouton["image"] = self.flag
            self.mode = 0

    def verif_fin(self,place_holder,perdu,nb): # ne pas ce préocupper de place_holder, il est juste la pour récuperer un argument mais on ne l'utilise pas
        case_sans_mine_sur=1
        # On compte le nombre de case déminée
        for i in range(100*self.difficlt):
            if self.dicb[i]["relief"]==SUNKEN:
                case_sans_mine_sur=case_sans_mine_sur+1
        # si pas perdu et que toute les cases sans bombe on été déminées --> c'est gagné
        if case_sans_mine_sur==(100*self.difficlt)-(10*self.difficlt) and perdu!=1:
            # calcul du temps que le joueur a mis pour finir
            final_time = time.strftime("%H:%M:%S")
            print(final_time, self.time_start)
            final_time2 = final_time.split(":")
            final_timeH = int(final_time2[0])-int(self.time_start[0])
            final_timeM = int(final_time2[1])-int(self.time_start[1])
            final_timeS = int(final_time2[2])-int(self.time_start[2])
            if final_timeS<0:
                final_timeS += 60
                final_timeM -= 1
            final_time3 = str(final_timeH)+":"+str(final_timeM)+":"+str(final_timeS)
            # gagné !
            gagne_msg = Message(self.parent,text=f"tu a gagné en {final_time3}")
            gagne_msg.pack()

        # si il reste des cases vides à deminer
        elif (100*self.difficlt)-(10*self.difficlt)-case_sans_mine_sur>0:
            print("Il reste encore",(100*self.difficlt)-(10*self.difficlt)-case_sans_mine_sur,"case sans mine")

        else:
            perdu_msg = Message(self.parent,text="Tu as perdu")
            perdu_msg.pack()

    def create_mine(self):
        # toutes les cases ont été crées avec 'left' (pas de bombe), donc on met 'right' sur des cases aléatoirement
        # le 10 ici -->   correspond au nombre de bombe voulut
        for j in range(10*self.difficlt):
            a = random.randint(0,(100*self.difficlt-1))
            # vérification que la case choisie n'est pas déjà une bombe
            while self.dicb[a]['justify'] == 'right':
                a = random.randint(0,(100*self.difficlt-1))
            # et on remplace enfin l'argument justify
            self.dicb[a]['justify'] = 'right'

    def case_autours(self,place_holder,nb): # ne pas ce préocupper de place_holder, il est juste la pour récuperer un argument que l'on utilise pas
        # liste des cases autours de la case "nb"
        liste = [nb-(10*self.difficlt)+1, nb+1, nb+(10*self.difficlt)+1, nb-(10*self.difficlt), nb+(10*self.difficlt), nb-(10*self.difficlt)-1, nb-1, nb+(10*self.difficlt)-1]

        # lorsque la case "nb" est sur un bord, le bord droit par exemple,  il faut supprimer de la liste les cases qui "n'existe pas" (en haut à droite, au milieu droit, et en en bas à droite dans notre exemple)
        if (nb+1) % (10*self.difficlt) == 0:
            del liste[:3]
        if (nb) % (10*self.difficlt) == 0:
            del liste[5:]
        return liste

    def detect_bomb(self,nb):
        # utilise la fonction case_autours pour detecter toutes les bombes autour de la case "nb"
        nb_bomb = 0
        liste = self.case_autours(self,nb)
        for case in liste:
            if case > -1 and case < 100*self.difficlt:
                # si la case à l'argument justify à "right", c'est une bombe
                if self.dicb[case]['justify'] == 'right':
                    nb_bomb += 1
        return nb_bomb

    def demine(self,nb,perdu):

        if self.mode == 0:  # si le mode drapeau n'est pas enclenché

            if self.dicb[nb]['justify'] == 'center' or nb<0 or nb > 100*self.difficlt or self.dicb[nb]['image'] == 'pyimage2': # je rappelle, quand justify est à "center", la case est déjà cliquer donc la méthode demine ne fait rien
                pass
            else:
                if self.dicb[nb]['justify'] == 'right':
                    self.dicb[nb]["image"] = self.dead
                    # si c'est perdu , alors il faut révéller toutes les cases du plateau
                    if perdu!=1:
                        for i in range(100*self.difficlt):
                            perdu=1
                            self.demine(i,perdu)
                else:
                    self.verif_fin(self,perdu,nb)
                    self.dicb[nb]["relief"] = SUNKEN
                    x = Plateau.detect_bomb(self,nb)
                    self.dicb[nb]["image"] = self.image[x]
                    self.dicb[nb]['justify'] = 'center'
                    if x==0:
                        liste=self.case_autours(self,nb)
                        for i in liste:
                            if i > -1 and i < 100*self.difficlt:
                                self.demine(i,perdu)

        elif self.mode == 1: # si le mode drapeau est enclenché

            if self.dicb[nb]['justify'] == 'center' or nb<0 or nb > 100*self.difficlt: # je rappelle, quand justify est à "center", la case est déjà cliquer donc la méthode demine ne fait rien
                pass

            elif self.dicb[nb]["image"] == 'pyimage2':
                self.dicb[nb]["image"] = self.grey
                print(self.dicb[nb]["image"])

            else:
                self.dicb[nb]["image"] = self.flag
                print(self.dicb[nb]["image"])




