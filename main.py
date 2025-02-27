import time
import affichage
import fltk
import interne
import menu

l = 700
h = 700
fltk.cree_fenetre(l, h, redimension=True)
NB_BOMBE = 10 #nombre de bombe au debut du jeu
TAILLE_PLATEAU = 8 #nombre de ligne et de colonne
NB_DRAPEAU = 0
DEBUT_X = l*1/24 #coordonner du point en haut a gauche du plateau
DEBUT_Y = h*1/8 #coordonner du point en bas a droite du plateau
plateau = interne.init(TAILLE_PLATEAU, TAILLE_PLATEAU) #creation du plateau
interne.minage_aleatoire(plateau, NB_BOMBE) #placement des bombes
BEGINING = False #represente le temps au moment de l'affichage de l'horloge
RE_AFFICHAGE = False #option pour reafficher le plateau apres des changement
pause = False
menu.afficher_menu(fltk.largeur_fenetre(), fltk.hauteur_fenetre())
taille_case_x, taille_case_y, NB_DRAPEAU = affichage.affichage(plateau, DEBUT_X, DEBUT_Y, l*2/3, h*7/8)
jeu = True
fin = False

while jeu:
    ev = fltk.donne_ev()
    tev = fltk.type_ev(ev)
    menu.drapeau(NB_DRAPEAU, NB_BOMBE, fltk.largeur_fenetre(), fltk.hauteur_fenetre())
    if isinstance(BEGINING, float) and not pause:
        menu.chrono(BEGINING, fltk.largeur_fenetre(), fltk.hauteur_fenetre())

    if tev == "Redimension" or RE_AFFICHAGE:
        RE_AFFICHAGE = False
        l = fltk.largeur_fenetre()
        h = fltk.hauteur_fenetre()
        DEBUT_X = l*1/24
        DEBUT_Y = h*1/8
        fltk.efface_tout()
        menu.afficher_menu(fltk.largeur_fenetre(), fltk.hauteur_fenetre())
        taille_case_x, taille_case_y, NB_DRAPEAU = affichage.affichage(plateau, DEBUT_X, DEBUT_Y, l*2/3, h*7/8)
    x, y = fltk.abscisse_souris(), fltk.ordonnee_souris()

    if tev == "ClicGauche":
        if l*(3/4) <= x <= l*(23/24) and h/2 <= y <= h*(19/32):
            BEGINING = time.time()
            pause = False
        elif l*(3/4) <= x <= l*(23/24) and h*(5/8) <= y <= h*(23/32):
            NB_BOMBE, TAILLE_PLATEAU = menu.change_difficulty(fltk.largeur_fenetre(), fltk.hauteur_fenetre())
            plateau = interne.init(TAILLE_PLATEAU, TAILLE_PLATEAU)
            interne.minage_aleatoire(plateau, NB_BOMBE)
            RE_AFFICHAGE = True
        elif l*(3/4) <= x <= l*(23/24) and h*(3/4) <= y <= h*(27/32):
            pause = not(pause)
        else:
            colonne_case = (x - DEBUT_X) / taille_case_x
            ligne_case = (y - DEBUT_Y) / taille_case_y
            if  0 <= ligne_case <= len(plateau) and 0 <= colonne_case <= len(plateau[0]):
                interne.decouvrir_case(plateau, int(ligne_case), int(colonne_case))
                fin, message = interne.defaite(plateau)
                if not fin:
                    fin, message = interne.victoire(plateau, NB_BOMBE)
                RE_AFFICHAGE = True

    if tev == "ClicDroit":
        colonne_case = (x - DEBUT_X) / taille_case_x
        ligne_case = (y - DEBUT_Y) / taille_case_y
        if 0 <= ligne_case <= len(plateau) and 0 <= colonne_case <= len(plateau[0]):
            if plateau[int(ligne_case)][int(colonne_case)]["drapeau"] is True:
                plateau[int(ligne_case)][int(colonne_case)]["drapeau"] = False
            else:
                interne.drapeau(plateau, int(ligne_case), int(colonne_case))
            RE_AFFICHAGE = True
    
    fltk.mise_a_jour()
    if fin:
        affichage.affichage_fin(message, (DEBUT_X, DEBUT_Y, l*2/3, h*7/8))
        ev = fltk.attend_ev()
        tev = fltk.type_ev(ev)
        if tev != "Quitte":
            plateau = interne.init(TAILLE_PLATEAU, TAILLE_PLATEAU)
            interne.minage_aleatoire(plateau, NB_BOMBE)
            RE_AFFICHAGE = True
            fin = False

    if tev == "Quitte":
        fltk.ferme_fenetre()
        jeu = False
