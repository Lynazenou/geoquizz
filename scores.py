import pandas as pd

# Création d'un dictionnaire contenant les noms et les scores des joueurs
data_score = {
    "Nom": ["Lyna", "Antonio"],                                 # Liste des noms des joueurs
    "Score": [0, 1337]                                          # Liste des scores associés à chaque joueur
}

# Convertit le dictionnaire en DataFrame Pandas
df_score = pd.DataFrame(data_score)                             

# Crée une fonction pour ajouter un joueur et son score
def ajouter_score(df, nom, score):                              
    # Création d'un DataFrame contenant le nouveau joueur
    nouveau_score = pd.DataFrame({
        "Nom": [nom],                                           # Ajoute le nom du nouveau joueur
        "Score": [score]                                        # Ajoute le score du nouveau joueur
    })

    # Ajoute le nouveau joueur et réinitialise temporairement l'index de 0 à n-1
    df = pd.concat([df, nouveau_score])      

    # Attribution du rang : les joueurs à égalité ont le même rang
    df["Classement"] = df["Score"].rank(
        ascending=False,
        method="min"
    ).astype(int)

    # Trie les joueurs du score le plus élevé au plus faible
    df = df.sort_values("Score", ascending=False)               

    # Utilisation du classement comme index
    df = df.set_index("Classement")

    return df


def afficher_scores():
    return f"Voici le tableau des scores !\n\n{df_score.head(10)}"

df_score = ajouter_score(df_score,"Dylan",800)
df_score = ajouter_score(df_score,"François",800)
df_score = ajouter_score(df_score,"Paul",69)