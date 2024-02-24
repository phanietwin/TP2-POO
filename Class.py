from random import randint
import random


#Class Joueur, prend en argument le nom du joueur
class Joueur(object):
    #tous les attributs sont privés
    def __init__(self, nom):
        self.__nom = nom
        self.__score = 0
        self.__cartes = []
        self.__defausse = []

    #Les get pour chaque atttribut
    def get_carte(self):
        return self.__cartes
    def get_carte_indice(self, indice):
        return self.__cartes[indice]
    def get_defausse(self):
        return self.__defausse
    def get_nom(self):
        return self.__nom
    def get_score(self):
        return self.__score
    #Les set pour les attributs en requièrant
    def set_score(self, score):
        self.__score = score
   
    
    # Ajouter des cartes dans le paquet principal  (prenant en argument la carte de type Carte à ajouter)  
    def Ajouter_carte(self, carte2):
        self.__cartes.append(carte2) 

    # Ajouter des cartes dans la défausse (prenant en argument la carte de type Carte à ajouter)  
    def Ajouter_carte_defausse(self, carte2):
        self.__defausse.append(carte2)

    # retirer des cartes du paquet principal(prenant en argument la carte de type Carte à ajouter)  
    def retirer_cartes(self, carte2):
        self.__cartes.remove(carte2)

    #transferer tout la défausse dans le paquet principal
    def transfert_defausse_vers_cartes(self):
        random.shuffle(self.__defausse)
        self.__cartes.extend(self.__defausse)
        self.__defausse = []

    # Afficher le nom du joueur, son score et ses cartes
    def Afficher_joueur(self):
        print ("le joueur", self.__nom, "de score", self.__score)
        print("ses cartes :")
        for carte in self.__cartes:
            carte.afficher_carte()
        print("sa defausse")
        for carte in self.__defausse:
            carte.afficher_carte()
    


#Classe carte, ne prenant rien en argument
class Carte(object):
    def __init__(self):
        self.__numero = 0
        self.__symbole = "0"

    #Les get pour chaque atttribut
    def get_numero(self):
        return self.__numero
    def get_symbole(self):
        return self.__symbole

    #Les set pour chaque atttribut
    def set_numero(self):
        self.__numero = randint(2, 14)
    def set_symbole(self):
        list = ["pique", "trefle", "carreau", "coeur"]
        self.__symbole = random.choice(list)

    # Afficher les cartes et convertir le numero en nom (dame, valet, roi,as)
    def afficher_carte(self):
        numero = "vide"
        symbole = "vide"
        if self.__numero < 11 and self.__numero > 1:
            numero = str(self.__numero)
        elif self.__numero == 11:
            numero = "valet"
        elif self.__numero == 12:
            numero = "Dame"
        elif self.__numero == 13:
            numero = "Roi"
        elif self.__numero == 14:
            numero = "As"
        if self.__symbole != "0":
            symbole = self.__symbole
        print(numero,"de",symbole, end =' ')


#Class Jeu, ne prenant rien en argument
class Jeu(object):
    def __init__(self, joueur1, joueur2):
        self.__joueur1 = joueur1
        self.__joueur2 = joueur2
        self.__jeu_de_cartes = []

 #Les get pour chaque atttribut le requièrant
    def get_jeu_de_carte(self):
        return self.__jeu_de_cartes
    

    #Remplir le jeu de carte de ses 52 cartes
    def remplir_le_jeu_de_cartes(self):
        jeu = 1
        cartes = Carte()
        cartes.set_numero()
        cartes.set_symbole()
        self.__jeu_de_cartes.append(cartes)
        while(jeu != 52):
            cartes = Carte()
            cartes.set_numero()
            cartes.set_symbole()
            red = 0

            # Éviter la redondance d'une carte
            for carte in self.__jeu_de_cartes:
                if carte.get_numero() == cartes.get_numero() and carte.get_symbole() == cartes.get_symbole():
                    red = 1
            if red == 0:
                self.__jeu_de_cartes.append(cartes)
                jeu = jeu + 1

    #Initialiser le jeu en distribuant 26 cartes et 26 points à chaque joueur
    def initialiser_le_jeu(self):
        self.remplir_le_jeu_de_cartes()
        
        for joueur in range(26):
            self.__joueur1.Ajouter_carte(self.__jeu_de_cartes[2 * joueur])
            self.__joueur2.Ajouter_carte(self.__jeu_de_cartes[2 * joueur + 1])
        
        self.__joueur1.Afficher_joueur()
        self.__joueur2.Afficher_joueur()
        self.__joueur1.set_score(26)
        self.__joueur2.set_score(26)

    #Mettre en oeuvre un duel qui mettra à jour les scores et les paquets de cartes des joueurs en fonction du gagnant et du perdant
    def duel(self):
        
        if len(self.__joueur1.get_carte())<=1 :
            self.__joueur1.transfert_defausse_vers_cartes()
       
        if len(self.__joueur2.get_carte())<=1:
            self.__joueur2.transfert_defausse_vers_cartes()

       
        print("j1 :",self.__joueur1.get_score())
        print("j2 :",self.__joueur2.get_score())

        #Cas de la bataille :
        if self.__joueur1.get_carte_indice(0).get_numero()== self.__joueur2.get_carte_indice(0).get_numero() :
           
            i=0
            #La boucle permet de compter combien de bataille à la suite, on aurait
            while(self.__joueur1.get_carte_indice(2*i).get_numero()== self.__joueur2.get_carte_indice(2*i).get_numero()):
                
                print("bataille !!")
                
                self.__joueur1.get_carte_indice(2*i).afficher_carte()
                print("vs", end=' ')
                self.__joueur2.get_carte_indice(2*i).afficher_carte()
               

                print("\n[face cachée:", end = ' ')
                self.__joueur1.get_carte_indice(2*i-1).afficher_carte()
                print("&", end=' ')
                self.__joueur2.get_carte_indice(2*i-1).afficher_carte()
                print("]")
                i =i+1
                if len(self.__joueur1.get_carte())<2*i+1  or len(self.__joueur2.get_carte())<2*i+1 :
                    break

            #reprise de la défausse si le nombre de cartes dans le paquet est insuffisant pour mener à bien la bataille
            if len(self.__joueur1.get_carte())<2*i+1:
                self.__joueur1.transfert_defausse_vers_cartes()
            if len(self.__joueur2.get_carte())<2*i+1 :
                self.__joueur2.transfert_defausse_vers_cartes()

            #Cas ordinaire : les deux joueurs ont suffissament de cartes pour faire bataille
            if len(self.__joueur1.get_carte())>2*i and len(self.__joueur2.get_carte())> 2*i: 
                self.comparaison(self.__joueur1, self.__joueur2, 2*i)
                
            else :
                #Il manque une carte au joueur pour faire la bataille --> il prend celle face cachée
                if len(self.__joueur1.get_carte())==2*i or len(self.__joueur2.get_carte())==2*i :
                   
                    self.comparaison(self.__joueur1, self.__joueur2,2*i-1)

                #La carte bataille est la dernière du joueur ---> le joueur a perdu (choix arbitraire pour ne pas rester bloqué)
                if len(self.__joueur1.get_carte())==1:
                    print("\nle joueur 2 a gagné")
                    self.gagnant_perdant(self.__joueur2, self.__joueur1, 1)
                if len(self.__joueur2.get_carte())==1 :
                    print("\nle joueur 1 a gagné")
                    self.gagnant_perdant(self.__joueur1, self.__joueur2, 1)

                else :
                    if len(self.__joueur1.get_carte())!=0 and len(self.__joueur2.get_carte())!=0:
                        self.comparaison(self.__joueur1, self.__joueur2, min(len(self.__joueur1.get_carte())-1, len(self.__joueur2.get_carte())-1))


    #En cas de non bataille
        else :
            self.comparaison(self.__joueur1, self.__joueur2,0)
            


#Pour comparer deux cartes et changer les scores en fonction 
    def comparaison (self, joueur1, joueur2, numero):

        self.__joueur1.get_carte_indice(numero).afficher_carte()
        print("vs", end=' ')
        self.__joueur2.get_carte_indice(numero).afficher_carte()
        

        if(joueur1.get_carte_indice(numero).get_numero()>joueur2.get_carte_indice(numero).get_numero()) :
            print("\nle joueur 1 a gagné")
            self.gagnant_perdant(self.__joueur1, self.__joueur2, numero+1)

        elif(joueur1.get_carte_indice(numero).get_numero()<joueur2.get_carte_indice(numero).get_numero()):
            print("\nle joueur 2 a gagné")
            self.gagnant_perdant(self.__joueur2, self.__joueur1, numero+1)
        else :
            joueur1.Ajouter_carte_defausse(joueur1.get_carte_indice(numero))
            joueur2.Ajouter_carte_defausse(joueur2.get_carte_indice(numero))
            joueur1.retirer_cartes(joueur1.get_carte_indice(numero))
            joueur2.retirer_cartes(joueur2.get_carte_indice(numero))
            
                               
#Incrémenter/ décrémenter les scores et mettre à jour les paquets de cartes
    def gagnant_perdant(self, gagnant, perdant, i):
        gagnant.set_score(gagnant.get_score() + i)
        perdant.set_score(perdant.get_score() - i)
        
        for j in range(i, 0, -1):
            gagnant.Ajouter_carte_defausse(gagnant.get_carte_indice(j-1))
            gagnant.Ajouter_carte_defausse(perdant.get_carte_indice(j-1))
            perdant.retirer_cartes(perdant.get_carte_indice(j-1))
            gagnant.retirer_cartes(gagnant.get_carte_indice(j-1))
   