from random import seed
from  Class import *
import unittest

class Test(unittest.TestCase) :

    # Test de la classe Joueur
    def test_joueur(self):

        # test du joueur
        joueur = Joueur("fifi")
        nom = joueur.get_nom()
        score = joueur.get_score()
        self.assertEqual(nom,"fifi")
        self.assertEqual(score,0)

        # Test du set_scori
        joueur2 = Joueur("Loulou")
        joueur2.set_score(10)
        score2 = joueur2.get_score()
        self.assertEqual(score2,10)

        # test de ajouter carte
        carte1 = Carte()
        carte1.set_numero()
        carte1.set_symbole()
        joueur.Ajouter_carte(carte1)
        carte_test = joueur.get_carte()
        self.assertEqual(carte_test,[carte1])

        #test_remove
        joueur.retirer_cartes(carte1)
        carte_test2 = joueur.get_carte()
        self.assertEqual(carte_test,[])

        # Test jouter carte défausse
        joueur.Ajouter_carte_defausse(carte1)
        carte_test3= joueur.get_defausse()
        self.assertEqual(carte_test3,[carte1])

        #test transfert cartes <--défausse
        joueur.transfert_defausse_vers_cartes()
        carte_test4 = joueur.get_carte()
        self.assertEqual(carte_test4,[carte1])
    

    # Test de la classe Carte
    def test_carte(self):
        # Test des fonctions set, numero et symbole
        random.seed(12)
        carte2 = Carte()
        carte2.set_symbole()
        carte2.set_numero()
        symbole_attendu = "coeur"  # grace au seed
        numero_attendu = 6
        carte2.afficher_carte()
        symbole_obtenu = carte2.get_symbole()
        numero_obtenu = carte2.get_numero()
        self.assertEqual(symbole_obtenu, symbole_attendu)
        self.assertEqual(numero_obtenu, numero_attendu)

    
    # Test des fonctions de la classe Jeu
    def test_jeu(self):
        # Initialisation des joueurs
        joueur1 = Joueur("riri")
        joueur2 = Joueur("donald")

        # Initialisation du jeu
        jeu = Jeu(joueur1, joueur2)

        # Test de la fonction remplir_le_jeu_de_cartes
        jeu.remplir_le_jeu_de_cartes()
        self.assertEqual(len(jeu.get_jeu_de_carte()), 52)
        

        # Test de la fonction initialiser le jeu
        joueur3= Joueur("l")
        joueur4 = Joueur("m")
        jeu2 = Jeu(joueur3, joueur4)
        random.seed(2)#pour garder un jeu constant
        
        jeu2.initialiser_le_jeu()

        self.assertEqual(joueur3.get_score(), 26)
        self.assertEqual(joueur4.get_score(), 26)

    #test de la fonction duel
        jeu2.duel()
        self.assertEqual(joueur3.get_score(), 25)
        self.assertEqual(joueur4.get_score(), 27)
        


# Exécution des tests
if __name__=='__main__':
    unittest.main(argv=[''],verbosity =0, exit =False)