import random

dico = {'mine': False, 'drapeau': False, "decouvert": False, "adjacent": 0}


def init(x, y):
    """Fonction qui initialise un plateau de jeu

    Args:
        x (int): nombre de colonnes
        y (int): nombre de lignes

    Returns:
        list: liste de liste de dictionnaire
    """
    lst = []
    for _ in range(y):
        lst_x = []
        for _ in range(x):
            lst_x.append({'mine': False, 'drapeau': False, "decouvert": False, "adjacent": 0})
        lst.append(lst_x)
    return lst

def affichage_list(liste):
    """Fonction qui affiche une liste de liste ligne par ligne

    Args:
        liste (list): liste de liste à afficher
    """
    for x in liste:
        print(x)

def minage(plateau, x, y):
    """Fonction qui place une mine sur une case

    Args:
        plateau (list): liste de liste de dictionnaire
        x (int): coordonnée x
        y (int): coordonnée y
    """
    plateau[x][y]['mine'] = True

def incrementation_adjacent(plateau, x, y):
    """fontion qui incrémente le nombre de mines adjacentes à une case

    Args:
        plateau (list): liste de liste de dictionnaire
        x (int): coordonnée x
        y (int): coordonnée y
    """
    plateau[x][y]["adjacent"] += 1

def drapeau(plateau, x, y):
    """Fonction qui place un drapeau sur une case

    Args:
        plateau (list): liste de liste de dictionnaire
        x (int): coordonnée x
        y (int): coordonnée y
    """
    plateau[x][y]['drapeau'] = True

def decouvert(plateau, x, y):
    """Fonction qui découvre une case

    Args:
        plateau (list): liste de liste de dictionnaire
        x (int): coordonnée x
        y (int): coordonnée y
    """
    plateau[x][y]['decouvert'] = True

def compteur_proximite(plateau, ligne, colonne):
    """Fonction qui retourne le nombre de mines adjacentes à une case

    Args:
        plateau (list): liste de liste de dictionnaire
        ligne (int): coordonnée x
        colonne (int): coordonnée y

    Returns:
        int: le nombre de mines adjacentes
    """
    return plateau[ligne][colonne]["adjacent"]

def minage_aleatoire(plateau, nb_mine):
    """Fonction qui place un nombre aléatoire de mines sur le plateau

    Args:
        plateau (list): liste de liste de dictionnaire
        nb_mine (int): nomnbre de mines à placer
    """
    liste_coord = []
    for a in range(len(plateau)):
        for b in range(len(plateau[a])):
            liste_coord.append((a, b))
    liste_coord_aleatoire = random.sample(liste_coord, nb_mine)
    for coord in liste_coord_aleatoire:
        minage(plateau, coord[0], coord[1])
        liste_adjacent = adjacent(plateau, coord[0], coord[1], True)
        for i in liste_adjacent:
            incrementation_adjacent(plateau, i[0], i[1])

def adjacent(plateau:list, ligne:int, colonne:int, diagonale:bool):
    """Fonction qui retourne les coordonnées des cases adjacentes à une case

    Args:
        plateau (list): liste de liste de dictionnaire
        ligne (int): coordonnée x
        colonne (int): coordonnée y
        diagonale (bool): booléen pour savoir si on vérifie les diagonales

    Returns:
        list: liste de tuples contenant les coordonnées des cases adjacentes

    >>> plateau = [["" for i in range(3)] for i in range(3)]
    >>> adjacent(pp, 3, 0)
    >>> adjacent(plateau, 0, 0, True)
    [(0, 1), (1, 0), (1, 1)]
    >>> adjacent(plateau, 2, 2, True)
    [(1, 2), (2, 1), (1, 1)]
    >>> adjacent(plateau, 0, 2, True)
    [(1, 2), (0, 1), (1, 1)]
    >>> adjacent(plateau, 2, 0, True)
    [(1, 0), (2, 1), (1, 1)]
    >>> adjacent(plateau, 1, 1, True)
    [(0, 1), (1, 2), (2, 1), (1, 0), (0, 0), (0, 2), (2, 2), (2, 0)]
    """
    adjacent = []
    bord_colonne_droite = bord_colonne_gauche = True
    bord_ligne_haut = bord_ligne_bas = True
    if ligne > 0: #on n'est pas a la premiere ligne
        adjacent.append((ligne - 1, colonne))
        bord_ligne_haut = False
    if colonne < len(plateau[ligne]) - 1: #on n'est pas a la derniere colonne
        adjacent.append((ligne, colonne + 1))
        bord_colonne_droite = False
    if ligne < len(plateau) - 1: #on n'est pas a la derniere ligne
        adjacent.append((ligne + 1, colonne))
        bord_ligne_bas = False
    if colonne > 0: #on n'est pas a la premiere colonne
        bord_colonne_gauche = False
        adjacent.append((ligne, colonne - 1))
    if diagonale:
        if (not bord_colonne_gauche) and (not bord_ligne_haut):
            adjacent.append((ligne - 1, colonne - 1))
        if (not bord_colonne_droite) and (not bord_ligne_haut):
            adjacent.append((ligne - 1, colonne + 1))
        if (not bord_colonne_droite) and (not bord_ligne_bas):
            adjacent.append((ligne + 1, colonne + 1))
        if (not bord_colonne_gauche) and (not bord_ligne_bas):
            adjacent.append((ligne + 1, colonne - 1))
    return adjacent

def decouvrir_case(plateau:list, ligne:int, colonne:int):
    """Fonction qui découvre une case et les cases adjacentes si la case est vide récursivement

    Args:
        plateau (list): liste de liste de dictionnaire
        ligne (int): coordonnée x
        colonne (int): coordonnée y
    """
    decouvert(plateau, ligne, colonne)
    if plateau[ligne][colonne]["mine"] or plateau[ligne][colonne]["adjacent"] > 0 :
        return
    liste_adjacant = adjacent(plateau, ligne, colonne, True)
    deja_decouvert = []
    for case in liste_adjacant:
        if plateau[case[0]][case[1]]["decouvert"]:
            deja_decouvert.append(case)
    for case in liste_adjacant:
        decouvert(plateau, case[0], case[1])
        if case not in deja_decouvert:
            if not plateau[case[0]][case[1]]["mine"] and plateau[case[0]][case[1]]["adjacent"] <= 0 :
                decouvrir_case(plateau, case[0], case[1])


def defaite(plateau):
    """Fonction qui retourne True et un message de défaite si une mine a été découverte

    Args:
        plateau (list): liste de liste de dictionnaire

    Returns:
        bool, string: True ou False et selon le booléen un message de défaite
    """
    messages_defaite = [
    "Dommage, tu as trouvé une mine. Essaie à nouveau !",
    "Oups, il semble que tu aies déclenché une mine. Tu peux réessayer !",
    "Force a toi tu es tombé sur une mine, réessaie une prochaine fois",
    "Attention, ça va péter ! Tu as trouvé la mauvaise case !",
    "Qui aurait pensé qu'un si petit clic pourrait causer autant de désordre ?",
    "Zut alors ! Ton clic a fait plus de bruit que prévu !",
    "On dirait que tu as trouvé le chemin le plus court vers l'explosion !",
    "Tu as été choisi par la mine... comme cobaye malchanceux !",
    "C'était comme chercher une aiguille dans une botte de foin, mais au lieu de l'aiguille, tu as trouvé la mine !",
    "Quand on dit que le jeu est explosif, ce n'était pas une figure de style !"
    ]

    for y in range(len(plateau)):
        for x in range(len(plateau[0])):
            if plateau[x][y]["decouvert"] and plateau[x][y]["mine"]:
                message = random.choice(messages_defaite)
                print(message)
                return True, message
    return False, messages_defaite[0]

def victoire(plateau, NB_BOMBE:int):
    """Fonction qui retourne True et un message de victoire si toutes les cases ont été découvertes sauf les mines

    Args:
        plateau (list): liste de liste de dictionnaire
        NB_BOMBE (int): nombre de bombes

    Returns:
        bool, string: True ou False et selon le booléen un message de victoire
    """
    messages_victoire = [
        "Félicitations, tu es sorti(e) indemne de ce champ de mines !",
        "Tu as réussi à déminer cette situation comme un(e) pro !",
        "Tu as navigué à travers les dangers avec brio !",
        "Ton flair pour les mines est inégalé ! Tu as triomphé sans une égratignure !",
        "Ta victoire est plus douce que le son d'une mine désamorcée !",
        "Félicitations ! Tu es officiellement qualifié pour le poste de démineur en chef !",
        "Tu as réussi là où d'autres ont échoué !",
        "Toutes les mines sont désamorcées ! Tu es le roi du désamorçage !",
        "Tu as déminé le champ de bataille comme un véritable stratège militaire !",
        "Tu as rendu le champ de mines aussi sûre qu'une pelouse bien entretenue !"
    ]
    nb_bombe_pas_activer = 0
    nb_decouvert = 0
    for y in range(len(plateau)):
        for x in range(len(plateau[0])):
            if plateau[x][y]["decouvert"]:
                nb_decouvert += 1
            if plateau[x][y]["decouvert"] is False:
                nb_bombe_pas_activer += 1
    if nb_bombe_pas_activer == NB_BOMBE and nb_decouvert == (len(plateau)**2) - NB_BOMBE:
        message = random.choice(messages_victoire)
        print(message)
        return True, message
    return False, messages_victoire[0]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
