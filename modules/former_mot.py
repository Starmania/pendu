def normaliser(chaine):
    c = 0
    chaine = chaine.lower()
    for i in chaine:
        if i == 'é' or i == 'è' or i == 'ê' or i == 'ë':
            chaine = list(chaine)
            chaine[c] = 'e'
            chaine = "".join(chaine)
        if i == 'à' or i == 'â' or i == 'ä':
            chaine = list(chaine)
            chaine[c] = 'a'
            chaine = "".join(chaine)
        if i == 'ç':
            chaine = list(chaine)
            chaine[c] = 'c'
            chaine = "".join(chaine)
        if i == 'ö' or i == 'ô':
            chaine = list(chaine)
            chaine[c] = 'o'
            chaine = "".join(chaine)
        if i == 'û' or i == 'ù':
            chaine = list(chaine)
            chaine[c] = 'u'd
            chaine = "".join(chaine)
        c += 1
    return chaine

def etoile(mot_random):
    mot_etoile = list()
    for i in mot_random:
        mot_etoile.append('*')
    mot_etoile = ''.join(mot_etoile)
    return mot_etoile