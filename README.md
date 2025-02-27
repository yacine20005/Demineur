# Démineur

L'objectif de ce problème est de réaliser à l'aide de la bibliothèque fltk votre propre version du classique jeu vidéo "Démineur", distribué avec divers systèmes d'exploitations bien connus depuis des décennies.

## Principe du jeu

Le jeu de démineur consiste en une grille rectangulaire, dont toutes les cases sont initialement couvertes (cachées). Un certain nombre de cases, déterminées de manière aléatoire au démarrage, contiennent une mine explosive. Le but du jeu est de découvrir le plus rapidement possible toutes les cases ne contenant pas de mine.

Le joueur peut agir de différentes manières sur le plateau de jeu :

- Découvrir une case par un clic gauche sur celle-ci. Dans ce cas, si la case contient une mine, la partie est perdue. Sinon, la case est découverte ;
- Indiquer par un clic droit qu'il pense qu'une mine se trouve sur une certaine case. La case est alors marquée pour éviter un clic malencontreux.

Lorsqu'une case ne contenant pas de mine est découverte, deux cas de figure se présentent. 

- Si la case est voisine d'au moins une mine, un nombre entier compris entre 1 et 8, indiquant le nombre total de mines sur les huit cases voisines, est affiché dans la case. Aucune autre case n'est alors découverte.
- Si la case n'est voisine d'aucune mine, toutes les cases adjacentes à cette case doivent être (récursivement !) découvertes. 

## Travail demandé

Vous devez réaliser un jeu parfaitement fonctionnel, permettant de faire des parties complètes. On favorisera la jouabilité et la stabilité plutôt que l'esthétique. Chaque partie doit être chronométrée et le temps total affiché en fin de partie.

## Paramétrage

Le programme doit permettre au moins le réglage des aspects suivants du jeu :

- nombre de lignes et de colonnes de la grille ;
- nombre de mines présentes ;
- ouverture initiale d'une case (ou non) ;
- taille de la fenêtre ;
- variantes...

## Suggestion d'améliorations

On pourra modifier le jeu afin de réduire la part de hasard nécessaire pour gagner : chaque fois que l'utilisateur a besoin de deviner une case sans être certain qu'elle ne contient pas de mine, le jeu peut par exemple jouer pour lui ou colorer une case "sûre".

Une autre amélioration possible est de maintenir un tableau des meilleurs scores pour chaque niveau de difficulté, sauvegardé même à la fermeture du programme.

## Instructions d'installation

Pour installer et configurer le jeu, suivez ces étapes :

1. Clonez le dépôt :
   ```sh
   git clone https://github.com/yacine20005/Demineur.git
   cd Demineur
   ```

2. Installez les dépendances requises :
   ```sh
   pip install -r requirements.txt
   ```

3. Exécutez le jeu :
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

## Directives de contribution

Nous accueillons les contributions pour améliorer le jeu. Pour contribuer, suivez ces étapes :

1. Forkez le dépôt.
2. Créez une nouvelle branche pour votre fonctionnalité ou correction de bug :
   ```sh
   git checkout -b feature-name
   ```
3. Validez vos modifications :
   ```sh
   git commit -m "Description de vos modifications"
   ```
4. Poussez vers la branche :
   ```sh
   git push origin feature-name
   ```
5. Créez une pull request.

Pour signaler des problèmes, veuillez utiliser le traqueur de problèmes GitHub.

## Structure du code

Le dépôt contient les fichiers suivants :

- `main.py` : Le point d'entrée principal du jeu.
- `affichage.py` : Contient des fonctions pour afficher le jeu dans le terminal et graphiquement.
- `fltk.py` : Une bibliothèque pour créer des interfaces utilisateur graphiques.
- `interne.py` : Contient la logique interne du jeu et les fonctions.
- `menu.py` : Contient des fonctions pour afficher et gérer le menu du jeu.
- `README.md` : Ce fichier, contenant la description du jeu et les instructions.

## Informations de contact

Pour toute question ou demande, veuillez nous contacter à [email@example.com](mailto:email@example.com).

## Ressources connexes

- [Documentation FLTK](https://www.fltk.org/documents.php)
- [Documentation Python](https://docs.python.org/3/)
