import os
import tkinter as tk
from os.path import normpath
from tkinter.filedialog import askopenfilenames, askopenfilename

from PIL import Image

deplacement = False
_ROOT = os.path.abspath(os.path.dirname(__file__))


class Image:
    mur = os.path.join(_ROOT, 'images/mur.gif')
    trou = os.path.join(_ROOT, 'images/objectif.gif')
    caisseOk = os.path.join(_ROOT, 'images/caisse_ok.gif')
    caisse = os.path.join(_ROOT, 'images/caisse.gif')
    joueur = os.path.join(_ROOT, 'images/mario_bas.gif')
    air = os.path.join(_ROOT, 'images/air2.gif')
    joueurOk = os.path.join(_ROOT, 'images/marioOk.gif')

class Niveau:

    def __init__(self):
        self.fenetre = tk.Tk()
        #fichier = self.ouvrirFichier()
        self.charger()#fichier)

    def ouvrirFichier(self):
        self.chemin = askopenfilename(initialdir=os.path.join(_ROOT, 'niveaux'))
        return self.chemin


    def charger(self) :# ,fichier):
        #self.fenetre = tk.Tk()
        #leChemin = self.OpenFile()
        #print(leChemin)
        self.tableau = []
        #self.fichier = open(leChemin)
        self.fichier = open("niveaux/level1.sok.txt")
        self.listeMurs = []
        self.listeCaisses = []
        self.listeTrou = []
        self.dimensions = self.fichier.readline()
        self.dimensions = self.dimensions.split(" ")
        self.largeur = int(self.dimensions[0])
        self.hauteur = int(self.dimensions[1])
        for c in range(self.hauteur):
            liste = list(self.fichier.readline())
            self.tableau.append(liste)

        for x in range(self.hauteur):
            for y in range(self.largeur):
                while len(self.tableau[x]) <= self.largeur + 1:
                    self.tableau[x] += " "
                if self.tableau[x][y] == "#":
                    self.nouveauMur = Mur(y, x)
                    self.listeMurs.append(self.nouveauMur)
                    mur = tk.PhotoImage(file=Image.mur)
                    self.mur = tk.Label(self.fenetre, image=mur)
                    self.mur.image = mur  # keep a reference!
                    self.mur.grid(row=x, column=y)
                elif self.tableau[x][y] == "@":
                    self.Mario = Personnage(y, x)
                    joueur = tk.PhotoImage(file=Image.joueur)
                    self.perso = tk.Label(self.fenetre, image=joueur)
                    self.perso.image = joueur  # keep a reference!
                    self.perso.grid(row=x, column=y)

                elif self.tableau[x][y] == ".":
                    self.nouveauTrou = Trou(y,x)
                    self.listeTrou.append(self.nouveauTrou)
                    trou = tk.PhotoImage(file=Image.trou)
                    self.rangement = tk.Label(self.fenetre, image=trou)
                    self.rangement.image = trou  # keep a reference!
                    self.rangement.grid(row=x, column=y)
                elif self.tableau[x][y] == "$":
                    self.nouvelleCaisse = Caisse(y, x, False)
                    self.listeCaisses.append(self.nouvelleCaisse)
                    caisse = tk.PhotoImage(file=Image.caisse)
                    self.caisse = tk.Label(self.fenetre, image=caisse)
                    self.caisse.image = caisse  # keep a reference!
                    self.caisse.grid(row=x, column=y)
                elif self.tableau[x][y] == " ":
                    air = tk.PhotoImage(file=Image.air)
                    self.espace = tk.Label(self.fenetre, image=air)
                    self.espace.image = air
                    self.espace.grid(row=x, column=y)
                elif self.tableau[x][y] == "+":
                    self.Mario = Personnage(y, x)
                    joueurOk = tk.PhotoImage(file=Image.joueurOk)
                    self.nouveauTrou = Trou(y,x)
                    self.listeTrou.append(self.nouveauTrou)
                    self.persorangement = tk.Label(self.fenetre, image=joueurOk)
                    self.persorangement.image = joueurOk
                    self.persorangement.grid(row=x, column=y)
                elif self.tableau[x][y] == "*":
                    self.nouvelleCaisse = Caisse(y, x, True)
                    self.listeCaisses.append(self.nouvelleCaisse)
                    self.nouveauTrou = Trou(y,x)
                    self.listeTrou.append(self.nouveauTrou)
                    caisseOk = tk.PhotoImage(file=Image.caisseOk)
                    self.caisserangement = tk.Label(self.fenetre, image=caisseOk)
                    self.caisserangement.image = caisseOk
                    self.caisserangement.grid(row=x, column=y)

    def effaceMemoire(self):
        del self.tableau
        del self.listeMurs
        del self.listeCaisses
        del self.listeTrou
        del self.dimensions
        del self.largeur
        del self.hauteur

    def redemmarer(self):
        self.effaceMemoire()
        self.charger()


    def victoire(self):
        for i in range(len(self.listeCaisses)):
            if self.listeCaisses[i].valeur == False:
                return False
        return True

    def ecranVictoire(self):
        self.ecranFin = tk.Tk()
        felicitations = tk.Label(self.ecranFin, text="Félicitations, vous avez terminé le niveau !")
        felicitations.pack()
        quitter = tk.Button(self.ecranFin,text="Quitter", command = lambda self=self: self.quitter())
        quitter.pack()
        rejouer = tk.Button(self.ecranFin,text="Rejouer", command = lambda self=self: self.rejouer())
        rejouer.pack()

    def rejouer (self):
        self.ecranFin.destroy()
        self.redemmarer() 

    def quitter (self):
        self.fenetre.destroy()
        self.ecranFin.destroy() 


    def ajouteCaisse(self,caisseBouge):
        if niveau.tableau[self.listeCaisses[caisseBouge].yCaisse][self.listeCaisses[caisseBouge].xCaisse] == ".":
            niveau.tableau[self.listeCaisses[caisseBouge].yCaisse][self.listeCaisses[caisseBouge].xCaisse] = "*"
            self.listeCaisses[caisseBouge].valeur = True
            caisseOk = tk.PhotoImage(file=Image.caisseOk)
            self.caisserangement = tk.Label(self.fenetre, image=caisseOk)
            self.caisserangement.image = caisseOk
            self.caisserangement.grid(row=self.listeCaisses[caisseBouge].yCaisse, column=self.listeCaisses[caisseBouge].xCaisse)
        else:
            niveau.tableau[self.listeCaisses[caisseBouge].yCaisse][self.listeCaisses[caisseBouge].xCaisse] = "$"
            self.listeCaisses[caisseBouge].valeur = False
            caisse = tk.PhotoImage(file=Image.caisse)
            self.perso = tk.Label(self.fenetre, image=caisse)
            self.perso.image = caisse  # keep a reference!
            self.perso.grid(row=self.listeCaisses[caisseBouge].yCaisse, column=self.listeCaisses[caisseBouge].xCaisse)

    def retireCaisse(self,caisseBouge):
        if niveau.tableau[self.listeCaisses[caisseBouge].yCaisse][self.listeCaisses[caisseBouge].xCaisse] == "*":
            self.listeCaisses[caisseBouge].valeur = False
            niveau.tableau[self.listeCaisses[caisseBouge].yCaisse][self.listeCaisses[caisseBouge].xCaisse] = "."
            trou = tk.PhotoImage(file=Image.trou)
            self.rangement = tk.Label(self.fenetre, image=trou)
            self.rangement.image = trou
            self.rangement.grid(row=self.listeCaisses[caisseBouge].yCaisse,column=self.listeCaisses[caisseBouge].xCaisse)
        else :
            niveau.tableau[self.listeCaisses[caisseBouge].yCaisse][self.listeCaisses[caisseBouge].xCaisse] = " "
            air = tk.PhotoImage(file=Image.air)
            self.espace = tk.Label(self.fenetre, image=air)
            self.espace.image = air
            self.espace.grid(row =self.listeCaisses[caisseBouge].yCaisse,column=self.listeCaisses[caisseBouge].xCaisse)

    def ajouteJoueur(self):
        if niveau.tableau[self.Mario.yPers][self.Mario.xPers] == ".":
            niveau.tableau[self.Mario.yPers][self.Mario.xPers] = "+"
            joueurOk = tk.PhotoImage(file=Image.joueurOk)
            self.persorangement = tk.Label(self.fenetre, image=joueurOk)
            self.persorangement.image = joueurOk
            self.persorangement.grid(row=self.Mario.yPers, column=self.Mario.xPers)
        else:
            niveau.tableau[self.Mario.yPers][self.Mario.xPers] = "@"
            joueur = tk.PhotoImage(file=Image.joueur)
            self.perso = tk.Label(self.fenetre, image=joueur)
            self.perso.image = joueur  # keep a reference!
            self.perso.grid(row=self.Mario.yPers, column=self.Mario.xPers)

    def retireJoueur(self):
        if niveau.tableau[self.Mario.yPers][self.Mario.xPers] == "+":
            niveau.tableau[self.Mario.yPers][self.Mario.xPers] = "."
            trou = tk.PhotoImage(file=Image.trou)
            self.rangement = tk.Label(self.fenetre, image=trou)
            self.rangement.image = trou  # keep a reference!
            self.rangement.grid(row=self.Mario.yPers, column=self.Mario.xPers)
        else:
            niveau.tableau[self.Mario.yPers][self.Mario.xPers] = " "
            air = tk.PhotoImage(file=Image.air)
            self.espace = tk.Label(self.fenetre, image=air)
            self.espace.image = air
            self.espace.grid(row=self.Mario.yPers, column=self.Mario.xPers)

class Mur:
    def __init__(self, xMur, yMur):
        self.xMur = xMur
        self.yMur = yMur


class Caisse:
    def __init__(self, xCaisse, yCaisse, valeur):  # True si la caisse est sur un rangement False sinon
        self.xCaisse = xCaisse
        self.yCaisse = yCaisse
        self.valeur = valeur


class Trou:
    def __init__(self, xTrou, yTrou):
        self.xTrou = xTrou
        self.yTrou = yTrou


class Personnage:

    def __init__(self, xPers, yPers):  # , #valeur):
        self.xPers = xPers
        self.yPers = yPers
        # self.valeur = valeur

    def deplacement(self, event):
        touche = event.keysym
        # Niveau = graphique.tableau[]

        if touche == "Up":
            collision = False
            for i in range(len(niveau.listeMurs)):
                if self.yPers - 1 == niveau.listeMurs[i].yMur and self.xPers == niveau.listeMurs[i].xMur:
                    collision = True

            pousser = None
            for i in range(len(niveau.listeCaisses)):
                if self.yPers - 1 == niveau.listeCaisses[i].yCaisse and self.xPers == niveau.listeCaisses[i].xCaisse:
                    pousser = True
                    caisseBouge = i
                    for j in range(len(niveau.listeMurs)):
                        if niveau.listeCaisses[i].yCaisse - 1 == niveau.listeMurs[j].yMur and niveau.listeCaisses[i].xCaisse == niveau.listeMurs[j].xMur:
                            pousser = False
                    for k in range(len(niveau.listeCaisses)):
                        if niveau.listeCaisses[i].yCaisse - 1 == niveau.listeCaisses[k].yCaisse and niveau.listeCaisses[i].xCaisse == niveau.listeCaisses[k].xCaisse:
                            pousser = False

            if collision or pousser == False:
                pass
            elif pousser:
                niveau.retireCaisse(caisseBouge)
                niveau.listeCaisses[caisseBouge].yCaisse -=1
                niveau.ajouteCaisse(caisseBouge)
                niveau.retireJoueur()
                self.yPers -= 1
                niveau.ajouteJoueur()
                if niveau.victoire():
                    niveau.ecranVictoire()
            else:
                niveau.retireJoueur()
                self.yPers -= 1
                niveau.ajouteJoueur()


        if touche == "Down":
            collision = False
            for i in range(len(niveau.listeMurs)):
                if self.yPers + 1 == niveau.listeMurs[i].yMur and self.xPers == niveau.listeMurs[i].xMur:
                    collision = True

            pousser = None
            for i in range(len(niveau.listeCaisses)):
                if self.yPers + 1 == niveau.listeCaisses[i].yCaisse and self.xPers == niveau.listeCaisses[i].xCaisse:
                    pousser = True
                    caisseBouge = i
                    for j in range(len(niveau.listeMurs)):
                        if niveau.listeCaisses[i].yCaisse + 1 == niveau.listeMurs[j].yMur and niveau.listeCaisses[i].xCaisse == niveau.listeMurs[j].xMur:
                            pousser = False
                    for k in range(len(niveau.listeCaisses)):
                        if niveau.listeCaisses[i].yCaisse + 1 == niveau.listeCaisses[k].yCaisse and niveau.listeCaisses[i].xCaisse == niveau.listeCaisses[k].xCaisse:
                            pousser = False

            if collision or pousser == False:
                pass
            elif pousser:
                niveau.retireCaisse(caisseBouge)
                niveau.listeCaisses[caisseBouge].yCaisse += 1
                niveau.ajouteCaisse(caisseBouge)
                niveau.retireJoueur()
                self.yPers += 1
                niveau.ajouteJoueur()
                if niveau.victoire():
                    niveau.ecranVictoire()
            else:
                niveau.retireJoueur()
                self.yPers += 1
                niveau.ajouteJoueur()

        if touche == "Left":
            collision = False
            for i in range(len(niveau.listeMurs)):
                if self.yPers == niveau.listeMurs[i].yMur and self.xPers - 1 == niveau.listeMurs[i].xMur:
                    collision = True

            pousser = None
            for i in range(len(niveau.listeCaisses)):
                if self.yPers == niveau.listeCaisses[i].yCaisse and self.xPers - 1 == niveau.listeCaisses[i].xCaisse:
                    pousser = True
                    caisseBouge = i
                    for j in range(len(niveau.listeMurs)):
                        if niveau.listeCaisses[i].yCaisse == niveau.listeMurs[j].yMur and niveau.listeCaisses[i].xCaisse - 1 == niveau.listeMurs[j].xMur:
                            pousser = False
                    for k in range(len(niveau.listeCaisses)):
                        if niveau.listeCaisses[i].yCaisse == niveau.listeCaisses[k].yCaisse and niveau.listeCaisses[i].xCaisse - 1 == niveau.listeCaisses[k].xCaisse:
                            pousser = False

            if collision or pousser == False:
                pass
            elif pousser:
                niveau.retireCaisse(caisseBouge)
                niveau.listeCaisses[caisseBouge].xCaisse -= 1
                niveau.ajouteCaisse(caisseBouge)
                niveau.retireJoueur()
                self.xPers -= 1
                niveau.ajouteJoueur()
                if niveau.victoire():
                    niveau.ecranVictoire()
            else:
                niveau.retireJoueur()
                self.xPers -= 1
                niveau.ajouteJoueur()

        if touche == "Right":
            collision = False
            for i in range(len(niveau.listeMurs)):
                if self.yPers == niveau.listeMurs[i].yMur and self.xPers + 1 == niveau.listeMurs[i].xMur:
                    collision = True

            pousser = None
            for i in range(len(niveau.listeCaisses)):
                if self.yPers == niveau.listeCaisses[i].yCaisse and self.xPers + 1 == niveau.listeCaisses[i].xCaisse:
                    pousser = True
                    caisseBouge = i
                    for j in range(len(niveau.listeMurs)):
                        if niveau.listeCaisses[i].yCaisse == niveau.listeMurs[j].yMur and niveau.listeCaisses[i].xCaisse + 1 == niveau.listeMurs[j].xMur:
                            pousser = False
                    for k in range(len(niveau.listeCaisses)):
                        if niveau.listeCaisses[i].yCaisse == niveau.listeCaisses[k].yCaisse and niveau.listeCaisses[i].xCaisse + 1 == niveau.listeCaisses[k].xCaisse:
                            pousser = False

            if collision or pousser == False:
                pass
            elif pousser:
                niveau.retireCaisse(caisseBouge)
                niveau.listeCaisses[caisseBouge].xCaisse += 1
                niveau.ajouteCaisse(caisseBouge)
                niveau.retireJoueur()
                self.xPers += 1
                niveau.ajouteJoueur()
                if niveau.victoire():
                    niveau.ecranVictoire()

            else:
                niveau.retireJoueur()
                self.xPers += 1
                niveau.ajouteJoueur()
        if touche == "r":
            niveau.redemmarer()


niveau = Niveau()
niveau.fenetre.bind("<KeyPress>", lambda event: niveau.Mario.deplacement(event))
niveau.fenetre.mainloop()

