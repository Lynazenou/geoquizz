import pandas as pd
from pathlib import Path

# Le CSV est placé à côté du fichier scores.py, quel que soit le dossier d'où tu lances le jeu
fichier_scores = Path(__file__).parent / "scores.csv"


def charger_scores():
    if fichier_scores.exists():
        return pd.read_csv(fichier_scores)

    return pd.DataFrame({"Nom": [], "Score": []})


def ajouter_score(df, nom, score):
    nouveau_score = pd.DataFrame({"Nom": [nom], "Score": [score]})

    # ignore_index=True renumérote proprement les lignes de 0 à n-1
    df = pd.concat([df, nouveau_score], ignore_index=True)
    df["Score"] = df["Score"].astype(int)

    # Tri du meilleur score au plus faible
    df = df.sort_values("Score", ascending=False).reset_index(drop=True)

    # Sauvegarde dans le fichier CSV
    df.to_csv(fichier_scores, index=False)

    return df


def afficher_scores(df):
    if df.empty:
        return "Aucun score pour le moment."

    top = df.head(10).copy()

    # Le classement est calculé à l'affichage : les égalités ont le même rang
    top.insert(0, "Classement", top["Score"].rank(ascending=False, method="min").astype(int))

    return f"Voici le tableau des scores !\n\n{top.to_string(index=False)}"
