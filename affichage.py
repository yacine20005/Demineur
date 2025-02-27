import fltk
import interne

TAILLE_BLOC = 100


def affichage_jeu_terminal(matrix, admin):
    """Fonction qui affiche le jeu dans le terminal

    Args:
        matrix (list): plateau de jeu
        admin(bool): affiche les mines
    """
    for ligne in matrix:
        for val in ligne:
            if val["decouvert"] or admin:
                if val["mine"]:
                    print(" X ", end="")
                else:
                    print(f' {val["adjacent"]} ', end="")
            else:
                print(" / ", end="")
        print("")
    print()


def affichage(plateau, ax, ay, bx, by):
    """Fonction qui affiche le plateau de jeu de facon graphique

    Args:
        plateau (list): liste de liste de dictionnaire
        ax (int): coordonnée x du coin supérieur gauche
        ay (int): coordonnée y du coin supérieur gauche
        bx (int): coordonnée x du coin inférieur droit
        by (int): coordonnée y du coin inférieur droit

    Returns:
        int, int, int: taille_case_x, taille_case_y, nb_drapeau
    """
    taille_case_x = int((bx - ax) / len(plateau[0]))
    taille_case_y = int((by - ay) / len(plateau))
    nb_drapeau = 0
    for y in range(len(plateau)):
        for x in range(len(plateau[0])):
            compteur = interne.compteur_proximite(plateau, y, x)
            coord_x = round(x * taille_case_x + ax, 3)
            coord_y = round(y * taille_case_y + ay, 3)
            if not plateau[y][x]["decouvert"] :
                fltk.image(coord_x, coord_y, "img/case.png", taille_case_x, taille_case_y, "nw", "case")
                if plateau[y][x]["drapeau"]:
                    nb_drapeau += 1
                    fltk.image(coord_x, coord_y, "img/drapeau.png", taille_case_x, taille_case_y, "nw", "case")
            else:
                if compteur >= 0:
                    fltk.image(coord_x, coord_y, f"img/{compteur}.png", taille_case_x, taille_case_y, "nw", "case")
                if plateau[y][x]["mine"]:
                    fltk.image(coord_x, coord_y, "img/mine.png", taille_case_x, taille_case_y, "nw", "case")
    return taille_case_x, taille_case_y, nb_drapeau


def affichage_list(liste):
    """Fonction qui affiche une liste de liste ligne par ligne

    Args:
        liste (list): liste de liste à afficher
    """
    for x in liste:
        print(x)

def get_police(texte, longueur_x, largeur_y, police: str = "Helvetica"):
    """Fonction qui retourne la taille de police maximale possible pour un texte

    Args:
        texte (string): texte à afficher
        longueur_x (int): longueur de la boite dans laquelle affiché le texte
        largeur_y (int): largeur de la boite dans laquelle affiché le texte
        police (str, optional): police à utiliser. Defaults to "Helvetica".

    Returns:
        int: taille de police maximale possible
    """
    taille_x, taille_y = fltk.taille_texte(texte, police, 1)
    taille_posible = 0
    while taille_x < longueur_x - (0.03 * longueur_x) and taille_y < largeur_y - (0.03 * largeur_y):
        taille_posible += 1
        taille_x, taille_y = fltk.taille_texte(texte, police, taille_posible+1)
    return taille_posible

def affichage_fin(message, coord_plateau):
    """Fonction qui affiche un message de fin de partie avec la bonne taille de police

    Args:
        message (string): message à afficher
        coord_plateau (list): liste des coordonnées du plateau
    """
    fltk.rectangle(coord_plateau[0], coord_plateau[1], coord_plateau[2],
                   coord_plateau[3], "black", "white")
    longueur_x = coord_plateau[2] - coord_plateau[0]
    largeur_y = coord_plateau[3] - coord_plateau[1]
    plus_message = "\nClick n'importe ou pour continuer."
    if message >= plus_message:
        taille = get_police(message, longueur_x, largeur_y)
    else:
        taille = get_police(plus_message, longueur_x, largeur_y)
    x = coord_plateau[0] + (longueur_x / 2)
    y = coord_plateau[1] + (largeur_y / 2)
    message += plus_message
    fltk.texte(x, y, message, ancrage="center", taille=taille)