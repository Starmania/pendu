def organiser(dico):
    compteur = 0
    taille_dico = len(dico)
    bigger_one_nb = -1
    dico_reorganise = {}
    while compteur != taille_dico:
        for key, value in dico.items():
            if value > bigger_one_nb:
                bigger_one_nb = value
                bigger_one_key = key
                bigger_one_value = value
        dico_reorganise[bigger_one_key]=bigger_one_value
        del(dico[bigger_one_key])
        compteur +=1
        print("Le joueur N°{0}, pseudo : '{1}' score : {2} points".format(compteur, bigger_one_key, bigger_one_value))
        bigger_one_nb = -1
        bigger_one_value = 0
    return dico_reorganise