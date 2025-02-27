import time
import fltk


def chrono(begining, l, h):
    """Fonction qui affiche le temps écoulé depuis le début de la partie

    Args:
        begining (int): temps de début de la partie
        l (int): lagrgeur de la fenêtre
        h (int): hauteure de la fenêtre
    """
    timer = time.time() - begining
    minutes, secondes = divmod(int(timer), 60)
    fltk.efface("t")
    fltk.texte(l*41/48, h*1/4+min(l*7/240, h*7/160), f"{minutes} : {secondes}",
               "black", "center", "Arial", min(l//60, h//40), "t")
    fltk.ligne(l*41/48, h*1/4, l*41/48, h*1/4 -
               min(h*1/80, l*1/120), "black", 1, tag="t")
    fltk.ligne(l*41/48, h*1/4, l*41/48+min(h*1/80, l*1/120),
               h*1/4, "black", 1, tag="t")
    fltk.cercle(l * (41 / 48), h / 4, min(l // 60, h // 40), "black", tag="t")
    fltk.mise_a_jour()


def dessin_drapeau(tag, l_, h_, coord=[0, 0]):
    """Fonction qui affiche un drapeau

    Args:
        tag (string): string associé au drapeau dessiné
        l_ (_type_): largeur de la fenêtre
        h_ (_type_): hauteur de la fenêtre
        coord (list, optional): coordonée où dessiner le drapeau. Defaults to [0, 0].
    """
    fltk.polygone([((l_*41/48) - coord[0], (h_*1/4-min(l_*1/12, h_*1/8)) + coord[1]),
                   ((l_*41/48) - coord[0], (h_*1/4 -
                                            min(l_*1/10, h_*3/20)) + coord[1]),
                   ((l_*13/15) - coord[0], (h_*1/4-min(l_*11/120, h_*11/80)) + coord[1])],
                  "black", "black", tag=tag)
    fltk.ligne((l_*41/48) - coord[0], (h_*1/4-min(l_*7/120, h_*7/80) + coord[1]),
               (l_*41/48) - coord[0], (h_*1/4 -
                                       min(l_*1/10, h_*3/20) + coord[1]),
               "black", 1, tag=tag)


def drapeau(v1, v2, l, h):
    """Fonction qui affiche un drapeau

    Args:
        v1 (int): nombre de drapeu posé
        v2 (int): nombre de drapeau à posé
        l (int): largeur de la fenêtre
        h (int): hauteur de la fenêtre
    """
    fltk.efface("drapeau")
    dessin_drapeau("drapeau", l, h)
    fltk.texte(l*41/48, h*1/4-min(h*11/160, l*11/240),
               f"{v1}/{v2}", "black", "center", "Arial", min(l//60, h//40), tag="drapeau")


def afficher_menu(l, h):
    """Fonction qui affiche le menu

    Args:
        l (int): largeur de la fenêtre
        h (int): hauteur de la fenêtre
    """
    a = ["Start Over", "Change Difficulty", "Pause"]
    fltk.rectangle(0, 0, l, h, "white", "white")
    #fltk.rectangle(l*1/24, h*1/8, l*2/3, h*7/8)
    for i in range(3):
        fltk.rectangle(l*(3/4), h/2+i*h/8, l*(23/24),
                       h*(19/32)+i*h/8, couleur="grey")
        fltk.texte(l*(41/48), h*(432.5/800)+i*h/8,
                   a[i], "black", "center", "Arial", min(l//60, h//40))


def change_difficulty(l, h):
    """Fonction qui affiche le menu de changement de difficulté

    Args:
        l (int): largeur de la fenêtre
        h (int): hauteur de la fenêtre

    Returns:
        int, int: nombre de bombes à poser aléatoirement et la taille du plateau à affiché en fonction de la difficulté
    """
    nb_bombe = 0
    quitter = False
    while not quitter:
        fltk.efface("difficulter")
        fltk.rectangle(0, 0, l, h, "white", "white", tag="difficulter")
        a, j, b = ["8*8 (10 mines)", "16*16 (40 mines)",
                   "30*30 (90mines)", "? (Personnalisée)"], 0, 0
        for _ in range(4):
            fltk.rectangle(l*1/6+j, h*1/16+b, l*11/24+j,
                           h*13/32+b, tag="difficulter")
            fltk.texte(l*5/16+j, h*137.5/800+b,
                       a[_], "black", "center", "Arial", min(l//60, h//40), tag="difficulter")
            j = l*1/3
            if _ == 1:
                j, b = 0, h*15/32
        fltk.mise_a_jour()
        ev = fltk.attend_ev()
        tev = fltk.type_ev(ev)
        if tev == "Quitte":
            fltk.ferme_fenetre()
            break
        x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
        if tev == "ClicGauche":
            if l*1/6 <= x <= l*11/24 and h*1/16 <= y <= h*13/32:
                taille_plateau = 8
                nb_bombe = int((taille_plateau**2)//6.4)
                quitter = not quitter
            if l*1/2 <= x <= l*19/24 and h*1/16 <= y <= h*13/32:
                taille_plateau =  16
                nb_bombe = int((taille_plateau**2)//6.4)
                quitter = not quitter
            if l*1/6 <= x <= l*11/24 and h*17/32 <= y <= h*7/8:
                taille_plateau = 30
                nb_bombe = int((taille_plateau**2)//6.4)
                quitter = not quitter
            if l*1/2 <= x <= l*19/24 and h*17/32 <= y <= h*7/8:
                taille_plateau = 50
                nb_bombe = int((taille_plateau**2)//6.4)
                quitter = not quitter
                personnalisation(l, h)
    fltk.efface("difficulter")
    return nb_bombe, taille_plateau


def personnalisation(l, h):
    
    nb_bombe = 0
    quitter = False
    while not quitter:
        fltk.rectangle(0, 0, l, h, "white", "white", tag="difficulter")
        for i in range(2):
            fltk.rectangle(l*1/6, h*1/4, l*1/3, h*1/2)
            fltk.rectangle(l*2/3, h*1/4, l*5/6, h*1/2)
        fltk.mise_a_jour()
        ev = fltk.attend_ev()
        tev = fltk.type_ev(ev)
        if tev == "Quitte":
            fltk.ferme_fenetre()
            break
        x, y = fltk.abscisse(ev), fltk.ordonnee(ev)
        if tev == "ClicGauche":
            if l*1/6 <= x <= l*11/24 and h*1/16 <= y <= h*13/32:
                taille_plateau = 8
                nb_bombe = (taille_plateau**2)//6.4
                quitter = not quitter
            if l*1/2 <= x <= l*19/24 and h*1/16 <= y <= h*13/32:
                taille_plateau =  16
                nb_bombe = (taille_plateau**2)//6.4
                quitter = not quitter
            if l*1/6 <= x <= l*11/24 and h*17/32 <= y <= h*7/8:
                taille_plateau = 30
                nb_bombe = (taille_plateau**2)//6.4
                quitter = not quitter
            if l*1/2 <= x <= l*19/24 and h*17/32 <= y <= h*7/8:
                taille_plateau = 50
                nb_bombe = (taille_plateau**2)//6.4
                personnalisation(l, h)
                #quitter = not quitter
    return nb_bombe, taille_plateau
