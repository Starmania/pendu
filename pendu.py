# -*- coding: utf-8 -*-

import codecs
import pickle
import time # Imports de modules
import os
import random

try:
    from modules.afficher import * # Verifications de la présence des modules susceptibles de ne pas être présents, car ils ne sont pas sur Python par défaut vu que ce sont MES modules
except ImportError:
    print("ERREUR : Impossible de trouver un module nécessaire au bon fonctionnement du programme 'afficher.py'")
    print("Veuillez installer ce module à l'aide du lien ci-joint : https://drive.google.com/drive/folders/1qqgdcED7iRTbQLzQN5xmFI6rV7CamF8R?usp=sharing \net le positionnez dans le même dossier que 'pendu.py'")
    print("Cela peut aussi être causé par l'absence du fichier '__init__.py', veuillez dans ce cas retélécharger l'ensemble du dossier 'modules'")
    os.system("pause")
    os.exit()
try:
    from modules.orga_scores import *
except ImportError:
    print("ERREUR : Impossible de trouver un module nécessaire au bon fonctionnement du programme 'orga_scores.py'")
    print("Veuillez installer ce module à l'aide du lien ci-joint : https://drive.google.com/drive/folders/1qqgdcED7iRTbQLzQN5xmFI6rV7CamF8R?usp=sharing \net le positionnez dans le même dossier que 'pendu.py'")
    print("Cela peut aussi être causé par l'absence du fichier '__init__.py', veuillez dans ce cas retélécharger l'ensemble du dossier 'modules'")
    os.system("pause")
    os.exit()
try:
    from modules.former_mot import *
except ImportError:
    print("ERREUR : Impossible de trouver un module nécessaire au bon fonctionnement du programme 'former_mot.py'")
    print("Veuillez installer ce module à l'aide du lien ci-joint : https://drive.google.com/drive/folders/1qqgdcED7iRTbQLzQN5xmFI6rV7CamF8R?usp=sharing \net le positionnez dans le même dossier que 'pendu.py'")
    print("Cela peut aussi être causé par l'absence du fichier '__init__.py', veuillez dans ce cas retélécharger l'ensemble du dossier 'modules'")
    os.system("pause")
    os.exit()


start = time.monotonic()

print("\nBienvenue dans ce programme vous permettant de faire un pendu !") # C'est ici que tout commence !
os.system("pause")
while True:
    pseudo_joueur = input("\nTout d'abord, comment vous appellez-vous ? : ")
    try:
        pseudo_joueur=str(pseudo_joueur) # On demande à l'utilisateur son pseudo qu'on va stocker précieusement
    except ValueError:
        print("Oh non, le type de votre pseudo n'a pas été accepté, veuillez réessayer !\n") # Je ne sais même pas si cette ligne de code pourra s'éxécuter un jour en faite xD
        continue
    break

mot_mystere = ""
coups = 10 # Déclarations de variables devant se faire hros boucle
score_joueur = 0
jveux_continuer = True

while jveux_continuer:
    try:
        with codecs.open("data\Base de donnees mots francais.txt",  "r", encoding='utf-8') as mots:
            mot_random = mots.readlines()[random.randint(0,22740)] # On choisit un mot au hasard dans la base de données
    except FileNotFoundError: # On vérifie que le fichier en question est bien présent, si ce n'est pas le cas, on le redirige vers ce dernier par l'intermédiaire du lien ci-joint
        print("Le fichier 'Base de donnees mot francais.txt' est introuvable, veuillez le télécharger à l'adresse suivante : https://drive.google.com/file/d/100A0urc2MguP5uJTYKOvvAd8hV95SXpt/view?usp=sharing \net le positionnez dans le dossier 'data'")
        os.system("pause")
        os.exit()
    mot_random = mot_random.strip()
    mot_mystere = etoile(mot_random)
    print("\nTrès bien {0}, voici le mot mystère : '{1}' ".format(pseudo_joueur, mot_mystere), "\nEssaye de le retrouver !")
    os.system("pause")
    lettres_rentrees = []
    mot_random = normaliser(mot_random) # Il faut s'assurer que le mot pris au hasard ne contiennent ni majuscules, ni caractères spéciaux
    while mot_mystere != mot_random:
        bete = False
        if coups == 0:
            pendu_haut_et_court()
            print("Oh non vous avez perdu, vous voilà pendu !")
            print("Le mot mystère était : ", mot_random)
            os.system("pause")
            break
        touche = input("\n\nVeuillez saisir une lettre : ")
        for i in lettres_rentrees:
            if touche == i:
                print("Vous avez déjà rentré cette lettre, ne soyez pas idiot !") # On vérifie que le joueur ne soit pas né de la dernière pluie
                bete = True
                break
        if bete == True:
            continue # Si le joueur a déjà rentré cette lettre, c'est reparti pour un tour ! (de boucle)
        lettres_rentrees.append(touche)
        compteur = 0
        lettres_trouvees = 0
        for i in mot_random:
            if touche == i: # On vérifie si le joueur a trouvé des lettres parmi le mot tiré au hasard
                mot_mystere = list(mot_mystere)
                mot_mystere[compteur] = touche
                mot_mystere = "".join(mot_mystere)
                lettres_trouvees += 1
                score_joueur += 10
            compteur += 1
        if lettres_trouvees > 0: # S'il en a effectivement trouvé, tant mieux pour lui
            thick()
            print("Bien joué, vous avez trouvé {0} lettres ! voici le mot mystère désormais : '{1}'\n".format(lettres_trouvees, mot_mystere))
            print("voici les lettres que vous avez déjà rentré jusqu'à maintenant : ", lettres_rentrees, "\n")
        else:
            coups -= 1 # Sinon, attention à son cou délicat !
            pendaison_en_cours_veuillez_patienter(coups)
            print("Oh non vous n'avez trouvé aucune lettre du mot... Il ne vous reste plus que {0} coups !\n".format(coups))
            print("Voici le mot mystère : ", mot_mystere, "\n")
            print("voici les lettres que vous avez déjà rentré jusqu'à maintenant : ", lettres_rentrees, "\n")
    score_joueur = score_joueur + coups * 5 # Pour les petits malins, voilà comment est calculé le score, DON'T TOUCH AT THIS VALUE, CAPICHE ? (Sinon c'est de la triche)
    if mot_mystere == mot_random: # Si l'utilisateur a finit par trouver le mot
        gagne = True
        print("Félicitations ! ^o^ Le mot mystère était bien '{0}' !\nEn plus vous avez remporté cette partie alors qu'il ne vous restait que {1} coups, ce qui vous fait un score de {2} points au total !".format(mot_mystere, coups, score_joueur))
    else:
        gagne = False # Sinon, ben on fait un peu de social, histoire de fidéliser un peu le cli.. euh le joueur pardon.
        print("Mais vous avez tout de même fait un score de {0} points, c'est pas mal !".format(score_joueur))
        jveux_continuer = False # Et oui, pas de second tour de manège pour les perdants !
    
    if gagne:
        while True:
            ok = input("Souhaitez-vous refaire une partie pour tenter d'améliorer votre score ? (O/N) : ") # Je n'ai pas besoin d'expliquer ici je pense
            ok = ok.upper()
            if ok == "O":
                break
            elif ok == "N":
                break
            else:
                print("Vous n'avez pas saisi 'o' ou 'n'")
        if ok == "O":
            jveux_continuer = True
            mot_mystere = ""
        else:
            jveux_continuer = False

while True:
    alors = input("\n Souhaitez vous enregistrer votre score actuel ? (O/N) : ") # L'utilisateur préfère-t-il se couvrir de gloire, ou se préserver dans l'humilité ? (Ou la honte, surtout s'il a fait 0 ce nulos)
    alors = alors.upper()
    if alors == "O":
        break
    elif alors == "N":
        break
    else:
        print("Vous n'avez pas saisi 'o' ou 'n'")
if alors == "O":
    enregistrer = True # Cette variable aura son importance plus tard
    try:
        with open("data\scores.txt",  "rb") as fichier_scores:
            scores_totaux = pickle.load(fichier_scores)
    except FileNotFoundError: # On vérifie si le fichier est présent, du bon boulot en somme
        with open("data\scores.txt", "xb") as fichier_scores: # Si le fichier n'est pas présent, et ben on le crée évidemment
           PP = False # Celui qui arrivera à trouver l'utilité de cette variable remportera une Nintendo Switch !
        with open("data\scores.txt", "wb") as fichier_scores:
            scores_totaux = {} # On est obligé de faire ça si on ne veut pas créer de problèmes lors de la future lecture du dico par le module pickle
            pickle.dump(scores_totaux, fichier_scores)
    with  open("data\scores.txt", "r+b") as fichier_scores:
        scores_totaux = pickle.load(fichier_scores)
        try:
            if scores_totaux[pseudo_joueur] < score_joueur: # On vérifie ici si le joueur n'a pas déjà un score établi sous le même pseudo, car un dico ne peut contenir qu'une seule valeur par clé
                del(scores_totaux[pseudo_joueur]) # Si c'est le cas, on supprime ce score et on le remplace par l'actuel, s'il est supérieur à l'ancien bien sûr, car quitte à ne garder qu'une valeur, autant garder la plus grosse
                scores_totaux[pseudo_joueur]=score_joueur
                print("\nVoici les scores : ")
                scores_totaux = organiser(scores_totaux) # La fonction 'organiser()' s'occupe également d'afficher les scores, pars beau la technologie ?
                pickle.dump(scores_totaux, fichier_scores)
            else:
                print("\nVoici les scores : ")
                organiser(scores_totaux)
                print("\nMalheureusement {0}, vous n'avez pas battu votre record personel, celui-ci n'a donc pas été mis à jour dans le tableau des scores".format(pseudo_joueur))
                enregistrer = False # Si l'utilisateur n'a pas dépassé son record personel, inutile de l'enregistrer
        except KeyError:
            scores_totaux[pseudo_joueur]=score_joueur
            print("\nVoici les scores : ")
            scores_totaux = organiser(scores_totaux)
    if enregistrer:
        with open("data\scores.txt", "wb") as fichier_scores: # On enregistre les scores qu'en cas de besoin
            pickle.dump(scores_totaux, fichier_scores)
end = time.monotonic()
print("Temps d'éxécution : ", end - start, "s")
os.system("pause")
