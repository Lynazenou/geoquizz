    # Quelle langue parle t'on dans ce pays ?

import random
import donnees

df = donnees.nettoyage_donnees()

def q_langue(vies, total):
        i = random.randint(0, len(df) - 1)

        pays = df.iloc[i]["name"]
        bonne_reponse = df.iloc[i]["languages"]

        # On récupère les langues disponibles, sans les doublons ni les valeurs vides
        langues = df["languages"].dropna().unique().tolist()

        # On retire la bonne réponse des mauvaises propositions
        mauvaises_reponses = [
                langue for langue in langues
                if langue != bonne_reponse
        ]

        # On sélectionne 3 mauvaises réponses différentes
        propositions = random.sample(mauvaises_reponses, 3)

        # On ajoute la bonne réponse
        propositions.append(bonne_reponse)

        # On mélange les 4 propositions
        random.shuffle(propositions)

        # On affiche le quiz
        print(f"⚪ Quelle langue parle-t-on dans ce pays : {pays} ?\n")

        for numero, langue in enumerate(propositions, start=1):
                print(f"{numero}. {langue}")

        # On conserve la bonne réponse pour vérifier le choix du joueur
        bonne_reponse_quiz = propositions.index(bonne_reponse) + 1
        
        # On redemande tant que la saisie n'est pas 1, 2, 3 ou 4
        reponse_joueur = input("\nEntrez le numéro de votre réponse (1 à 4) : ").strip()

        while reponse_joueur not in ["1", "2", "3", "4"]:
                reponse_joueur = input("\nDonne une réponse comprise entre 1 et 4 : ").strip()

        reponse_joueur = int(reponse_joueur)

        # On vérifie la réponse
        if reponse_joueur == bonne_reponse_quiz:
                total += 100
                print(f"\nBravo, tu as {total} points")
        else :
                vies -= 1
                print(f"\nFaux la bonne réponse est : {bonne_reponse}")


        return vies,total

# Quelle est la capitale dans ce pays ?

def q_capitale(vies, total):
        i = random.randint(0, len(df) - 1)

        pays = df.iloc[i]["name"]
        bonne_reponse = df.iloc[i]["capital"]

        # On récupère les langues disponibles, sans les doublons ni les valeurs vides
        capitales = df["capital"].dropna().unique().tolist()

        # On retire la bonne réponse des mauvaises propositions
        mauvaises_reponses = [
                capitale for capitale in capitales
                if capitale != bonne_reponse
        ]

        # On sélectionne 3 mauvaises réponses différentes
        propositions = random.sample(mauvaises_reponses, 3)

        # On ajoute la bonne réponse
        propositions.append(bonne_reponse)

        # On mélange les 4 propositions
        random.shuffle(propositions)

        # On affiche le quiz
        print(f"⚪ Quelle est la capitale dans ce pays : {pays} ?\n")

        for numero, capitale in enumerate(propositions, start=1):
                print(f"{numero}. {capitale}")

        # On conserve la bonne réponse pour vérifier le choix du joueur
        bonne_reponse_quiz = propositions.index(bonne_reponse) + 1

        # On redemande tant que la saisie n'est pas 1, 2, 3 ou 4
        reponse_joueur = input("\nEntrez le numéro de votre réponse (1 à 4) : ").strip()

        while reponse_joueur not in ["1", "2", "3", "4"]:
                reponse_joueur = input("\nDonne une réponse comprise entre 1 et 4 : ").strip()

        reponse_joueur = int(reponse_joueur)

        # On vérifie la réponse
        if reponse_joueur == bonne_reponse_quiz:
                total += 100
                print(f"\nBravo, tu as {total} points")
        else :
                vies -= 1
                print(f"\nFaux la bonne réponse est : {bonne_reponse}")

        return vies,total

# A Quel Pays correspond cette capitale : ?

def q_pays_capitale(vies, total):
        i = random.randint(0, len(df) - 1)

        capitale = df.iloc[i]["capital"]
        bonne_reponse = df.iloc[i]["name"]

        # On récupère les langues disponibles, sans les doublons ni les valeurs vides
        liste_pays = df["name"].dropna().unique().tolist()

        # On retire la bonne réponse des mauvaises propositions
        mauvaises_reponses = [
                pays for pays in liste_pays
                if pays != bonne_reponse
        ]

        # On sélectionne 3 mauvaises réponses différentes
        propositions = random.sample(mauvaises_reponses, 3)

        # On ajoute la bonne réponse
        propositions.append(bonne_reponse)

        # On mélange les 4 propositions
        random.shuffle(propositions)

        # On affiche le quiz
        print(f"⚪ A Quel Pays correspond cette capitale : {capitale} ?\n")

        for numero, pays in enumerate(propositions, start=1):
                print(f"{numero}. {pays}")

        # On conserve la bonne réponse pour vérifier le choix du joueur
        bonne_reponse_quiz = propositions.index(bonne_reponse) + 1

        # On redemande tant que la saisie n'est pas 1, 2, 3 ou 4
        reponse_joueur = input("\nEntrez le numéro de votre réponse (1 à 4) : ").strip()

        while reponse_joueur not in ["1", "2", "3", "4"]:
                reponse_joueur = input("\nDonne une réponse comprise entre 1 et 4 : ").strip()

        reponse_joueur = int(reponse_joueur)

        # On vérifie la réponse
        if reponse_joueur == bonne_reponse_quiz:
                total += 100
                print(f"\nBravo, tu as {total} points")
        else :
                vies -= 1
                print(f"\nFaux la bonne réponse est : {bonne_reponse}")


        return vies,total

# Dans quel continent se trouve ce pays ?

def q_continent(vies, total):
        i = random.randint(0, len(df) - 1)

        pays = df.iloc[i]["name"]
        bonne_reponse = df.iloc[i]["region"]

        # On récupère les regions disponibles, sans les doublons ni les valeurs vides
        regions = df["region"].dropna().unique().tolist()

        # On retire la bonne réponse des mauvaises propositions
        mauvaises_reponses = [
                region for region in regions
                if region != bonne_reponse
        ]

        # On sélectionne 3 mauvaises réponses différentes
        propositions = random.sample(mauvaises_reponses, 3)

        # On ajoute la bonne réponse
        propositions.append(bonne_reponse)

        # On mélange les 4 propositions
        random.shuffle(propositions)

        # On affiche le quiz
        print(f"⚪ Dans quel continent se trouve ce pays : {pays} ?\n")

        for numero, region in enumerate(propositions, start=1):
                print(f"{numero}. {region}")

        # On conserve la bonne réponse pour vérifier le choix du joueur
        bonne_reponse_quiz = propositions.index(bonne_reponse) + 1

        # On redemande tant que la saisie n'est pas 1, 2, 3 ou 4
        reponse_joueur = input("\nEntrez le numéro de votre réponse (1 à 4) : ").strip()

        while reponse_joueur not in ["1", "2", "3", "4"]:
                reponse_joueur = input("\nDonne une réponse comprise entre 1 et 4 : ").strip()

        reponse_joueur = int(reponse_joueur)

        # On vérifie la réponse
        if reponse_joueur == bonne_reponse_quiz:
                total += 100
                print(f"\nBravo, tu as {total} points")
        else :
                vies -= 1
                print(f"\nFaux la bonne réponse est : {bonne_reponse}")


        return vies,total

#Quelle est la monnaie utilisée dans ce pays ?

def q_monnaie(vies, total):
        i = random.randint(0, len(df) - 1)

        pays = df.iloc[i]["name"]
        bonne_reponse = df.iloc[i]["currencies"]

        # On récupère les monnaies disponibles, sans les doublons ni les valeurs vides
        monnaies = df["currencies"].dropna().unique().tolist()

        # On retire la bonne réponse des mauvaises propositions
        mauvaises_reponses = [
                monnaie for monnaie in monnaies
                if monnaie != bonne_reponse
        ]

        # On sélectionne 3 mauvaises réponses différentes
        propositions = random.sample(mauvaises_reponses, 3)

        # On ajoute la bonne réponse
        propositions.append(bonne_reponse)

        # On mélange les 4 propositions
        random.shuffle(propositions)

        # On affiche le quiz
        print(f"⚪ Quelle est la monnaie utilisée dans ce pays : {pays} ?\n")

        for numero, monnaie in enumerate(propositions, start=1):
                print(f"{numero}. {monnaie}")

        # On conserve la bonne réponse pour vérifier le choix du joueur
        bonne_reponse_quiz = propositions.index(bonne_reponse) + 1

        # On redemande tant que la saisie n'est pas 1, 2, 3 ou 4
        reponse_joueur = input("\nEntrez le numéro de votre réponse (1 à 4) : ").strip()

        while reponse_joueur not in ["1", "2", "3", "4"]:
                reponse_joueur = input("\nDonne une réponse comprise entre 1 et 4 : ").strip()

        reponse_joueur = int(reponse_joueur)

        # On vérifie la réponse
        if reponse_joueur == bonne_reponse_quiz:
                total += 100
                print(f"\nBravo, tu as {total} points")
        else :
                vies -= 1
                print(f"\nFaux la bonne réponse est : {bonne_reponse}")


        return vies,total

liste_question = [q_capitale,q_pays_capitale,q_monnaie,q_continent,q_langue]
