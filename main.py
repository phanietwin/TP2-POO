from Class import*

joueur = Joueur("joueur1")
joueur2 = Joueur("joueur2")

jeu = Jeu(joueur, joueur2)
jeu.initialiser_le_jeu()

carte = joueur.get_carte()

while(joueur.get_score()!= 0 and joueur2.get_score()!=0):
    jeu.duel()

print("*******************************fin du jeu **********************************")
print("joueur1 :",joueur.get_score())
print("joueur2 :",joueur2.get_score())
if (joueur.get_score()== 52):
    print("le gagnant est", joueur.get_nom())
else :
    print("le gagnant est", joueur2.get_nom())
    

