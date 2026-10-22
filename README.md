# 🌍 GéoQuizz

Quiz sur les pays du monde, jouable dans le terminal, écrit en Python.
Les questions et les réponses sont tirées au hasard à partir d'un dataset réel de pays, chargé et nettoyé par le programme.

## 🎮 Le jeu

### Principe

- Tu commences avec **3 vies**.
- Tu réponds à **10 questions** à choix multiples (4 propositions, une seule bonne réponse).
- Chaque **bonne réponse** rapporte **100 points**.
- Chaque **mauvaise réponse** te fait perdre **1 vie**.
- La partie s'arrête après les 10 questions **ou** quand tu n'as plus de vie.
- Ton score est enregistré et tu peux consulter le **tableau des scores** depuis le menu.

### Thèmes de questions

| Thème | Exemple |
|---|---|
| Capitales | Quelle est la capitale de ce pays : France ? |
| Pays d'une capitale | À quel pays correspond cette capitale : Lima ? |
| Régions / continents | Dans quel continent se trouve ce pays : Kenya ? |
| Langues | Quelle langue parle-t-on dans ce pays : Brésil ? |
| Monnaies | Quelle est la monnaie utilisée dans ce pays : Japon ? |

### Déroulement d'une partie

1. **Menu principal** : nouvelle partie, tableau des scores ou quitter.
2. **Nouvelle partie** : le joueur saisit son prénom.
3. **Questions** : après chaque question, le jeu affiche les vies restantes, le nombre de questions restantes et le score.
4. **Fin de partie** : message de victoire (10 questions terminées) ou de défaite (plus de vies), puis affichage du score final. Le score est ajouté au tableau des scores et sauvegardé.
5. Retour au menu pour rejouer ou quitter.

## 📦 Installation

### Prérequis

- **Python 3.9 ou supérieur**
- **pip**
- Une connexion internet (le dataset des pays est téléchargé au lancement)

### Bibliothèques à installer

| Bibliothèque | Utilité |
|---|---|
| `pandas` | Chargement et nettoyage du dataset, gestion du tableau des scores |
| `pytest` | Exécution des tests (uniquement pour le développement) |

Les modules `random` et `pathlib` font partie de la bibliothèque standard de Python : il n'y a rien à installer pour eux.

```bash
pip install pandas pytest
```

Ou, avec un fichier `requirements.txt` à la racine du projet :

```
pandas
pytest
```

```bash
pip install -r requirements.txt
```

### Récupérer le projet

```bash
git clone https://github.com/<ton-pseudo>/<nom-du-depot>.git
cd <nom-du-depot>
```

## ▶️ Lancer le jeu

```bash
python main.py
```

## 🗂️ Structure du projet

```
GeoQuizz/
├── main.py         # Point d'entrée : menu principal
├── quiz.py         # Déroulement d'une partie
├── questions.py    # Les questions et leur logique
├── donnees.py      # Chargement et nettoyage du dataset
├── scores.py       # Gestion et sauvegarde des scores
├── scores.csv      # Créé automatiquement au premier score
└── README.md
```

## 📄 Rôle de chaque fichier

### `main.py` : le menu principal

C'est le fichier à exécuter. Il charge les scores existants, puis affiche le menu dans une boucle :

1. **Nouvelle partie** : lance `quiz.quiz()`, récupère le prénom et le score, puis enregistre le résultat.
2. **Tableau des scores** : affiche le top 10.
3. **Quitter** : arrête le programme.

Toute saisie différente de 1, 2 ou 3 affiche un message d'erreur et le menu est proposé à nouveau.

### `quiz.py` : la partie

Contient la fonction `quiz()` qui gère une partie complète :

- initialise les **3 vies**, le **score à 0** et le **compteur de 10 questions** ;
- demande le prénom du joueur ;
- choisit une question au hasard parmi les 5 types disponibles ;
- met à jour et affiche les vies, la progression et le score après chaque question ;
- détecte la fin de partie (plus de vies ou 10 questions posées) ;
- renvoie le **prénom** et le **score final** à `main.py`.

### `questions.py` : les questions

Contient une fonction par type de question (`q_capitale`, `q_pays_capitale`, `q_continent`, `q_langue`, `q_monnaie`) ainsi que la liste `liste_question` utilisée par `quiz.py` pour tirer une question au hasard.

Chaque fonction suit la même logique :

1. tire un pays au hasard dans le dataset ;
2. récupère la bonne réponse ;
3. choisit 3 mauvaises réponses différentes parmi les autres valeurs du dataset ;
4. mélange les 4 propositions et les affiche numérotées ;
5. lit le choix du joueur, vérifie la réponse, ajoute 100 points ou retire 1 vie ;
6. renvoie les vies et le score mis à jour.

### `donnees.py` : le dataset

La fonction `nettoyage_donnees()` :

- télécharge le dataset public [mledoze/countries](https://github.com/mledoze/countries) au format JSON ;
- ne garde que les colonnes utiles : nom, monnaie, capitale, région et langue ;
- extrait le nom commun du pays, le nom de la monnaie, la première capitale et la première langue ;
- renvoie un DataFrame pandas prêt à être utilisé par `questions.py`.

### `scores.py` : les scores

- `charger_scores()` : lit `scores.csv` s'il existe, sinon crée un tableau vide.
- `ajouter_score(df, nom, score)` : ajoute un joueur, trie du meilleur au plus faible et sauvegarde dans `scores.csv`.
- `afficher_scores(df)` : affiche le top 10 avec le classement. Les joueurs à égalité ont le même rang.

## 🧪 Tests

```bash
pytest
```

> Les tests sont à placer dans un dossier `tests/` (par exemple `tests/test_scores.py`).

## 🛠️ Technologies

- Python 3
- pandas

## 👤 Auteur

Projet réalisé par **<ton nom>** dans le cadre de ma formation.
