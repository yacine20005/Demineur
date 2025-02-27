# Démineur
## Principe du jeu

Le jeu de démineur consiste en une grille rectangulaire, dont toutes les cases sont initialement couvertes (cachées). Un certain nombre de cases, déterminées de manière aléatoire au démarrage, contiennent une mine explosive. Le but du jeu est de découvrir le plus rapidement possible toutes les cases ne contenant pas de mine.

Le joueur peut agir de différentes manières sur le plateau de jeu :

- Découvrir une case par un clic gauche sur celle-ci. Dans ce cas, si la case contient une mine, la partie est perdue. Sinon, la case est découverte ;
- Indiquer par un clic droit qu'il pense qu'une mine se trouve sur une certaine case. La case est alors marquée pour éviter un clic malencontreux.

Lorsqu'une case ne contenant pas de mine est découverte, deux cas de figure se présentent. 

- Si la case est voisine d'au moins une mine, un nombre entier compris entre 1 et 8, indiquant le nombre total de mines sur les huit cases voisines, est affiché dans la case. Aucune autre case n'est alors découverte.
- Si la case n'est voisine d'aucune mine, toutes les cases adjacentes à cette case doivent être (récursivement !) découvertes. 

## Paramétrage

Le programme permet le réglage des aspects suivants du jeu :

- nombre de lignes et de colonnes de la grille ;
- nombre de mines présentes ;
- ouverture initiale d'une case (ou non) ;
- taille de la fenêtre ;
- variantes...

## Instructions d'installation

Pour installer et configurer le jeu, suivez ces étapes :

1. Clonez le dépôt :
   ```sh
   git clone https://github.com/yacine20005/Demineur.git
   cd Demineur
   ```

2. Exécutez le jeu :
   ```sh
   python main.py
   ```

## Exemples d'utilisation

Pour démarrer une partie, exécutez la commande suivante :
```sh
python main.py
```

Contrôles de base :
- Clic gauche pour découvrir une case.
- Clic droit pour marquer une case comme contenant une mine.

## Structure du code

Le dépôt contient les fichiers suivants :

- `main.py` : Le point d'entrée principal du jeu.
- `affichage.py` : Contient des fonctions pour afficher le jeu dans le terminal et graphiquement.
- `fltk.py` : Une bibliothèque pour créer des interfaces utilisateur graphiques.
- `interne.py` : Contient la logique interne du jeu et les fonctions.
- `menu.py` : Contient des fonctions pour afficher et gérer le menu du jeu.
- `README.md` : Ce fichier, contenant la description du jeu et les instructions.

## Ressources connexes

- [Documentation FLTK](https://www.fltk.org/documents.php)
- [Documentation Python](https://docs.python.org/3/)
