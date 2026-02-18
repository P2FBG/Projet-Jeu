from microbit import *
import random

def deviner_un_nombre():
    score = 0  # score des parties
    nb_parties = 0  # Le nombre de partie
    display.scroll("Bienvenue")

    while True:
        nombre_a_deviner = random.randint(0, 9) # nombre aléatoire entre 0 et 9
        affichage = 5  # valeur affiché au début
        essais_restants = 3  # nombre de coup pour trouver
        display.show(str(affichage)) # Afficher la valeur choisie

        while essais_restants > 0:
            if button_a.is_pressed():  # si le bouton A est pressé
                affichage -= 1 # le nombre diminue
                display.show(str(affichage))  # le nombre est affiché
                sleep(300)  # pause sinon l'affichage est trop rapide

            if button_b.is_pressed():  # si le bouton A est pressé
                affichage += 1 # le nombre augmente
                display.show(str(affichage))  # le nombre est affiché
                sleep(300)   # pause sinon l'affichage est trop rapide
			
            if pin_logo.is_touched():  # si le logo est pressé
                if affichage == nombre_a_deviner: #si le nombre correspond au nombre aléatoire 
                    display.scroll("Bravo")
                    partie_gagne = 1  # la partie est gagnée
                    break  # fin de cette partie en arretant la boucle while
                elif affichage < nombre_a_deviner: # sinon proposer un autre nombre
                    display.scroll("+")
                else:
                    display.scroll("-")

                essais_restants -= 1 # un coup en moins sur les 3 possibles

                if essais_restants > 0: # si il reste des coups à jouer on recommence
                    display.show(str(affichage))

        if affichage != nombre_a_deviner: # si on ne trouve pas le bon nombre apres tout les coups
            display.scroll("Perdu, le nombre etait " + str(nombre_a_deviner))
            partie_gagne = 0 # la partie est perdue

        if partie_gagne == 1: 
           score += 1 # si la partie est gagnée on gagne un point à notre score

        nb_parties += 1 # on ajoute 1 au nombre de parties jouées

        display.scroll("Score: " + str(score) + "/" + str(nb_parties)) # affichage du score total
        display.scroll("Rejouer? Oui(a) /Non(b)")  # continue ou arrête le jeu

        while True: 
            if button_a.is_pressed():  # si bouton A est pressé alors ca recommence
                break # relance le jeu
            elif button_b.is_pressed():  # si c'est les bouton B alors c'est fini
                display.scroll("Merci d'avoir joue")

deviner_un_nombre() # lance la fonction deviner_un_nombre