import quiz
import scores

# Menu principale
df_score = scores.charger_scores()
continuer = True  # Initialise une variable à True pour permettre au menu de s'exécuter

while continuer:  # Répète le menu tant que la variable continuer vaut True

    # Affiche du menu et des options
    print("\nBienvenue dans GéoQUIZZZ")  
    print("\n1. Nouvelle partie")
    print("2. Tableau des scores")
    print("3. Quitter\n")

    # Demande un choix et convertit la réponse en entier
    choix = input("Choisis entre 1, 2 ou 3 : ")

    # Permet au joueur de commencer la partie
    if choix == "1":  
        nom, total = quiz.quiz()

        # Enregistrer le score après la fin de la partie
        df_score = scores.ajouter_score(df_score, nom, total)

    # Permet au joueur de consulter les résultats des parties
    elif choix == "2":
        print(scores.afficher_scores(df_score))


    # Permet au joueur de quitter le jeu
    elif choix == "3":
        continuer = False  # Met fin à la boucle while
        print("n\ À bientôt sur GéoQUIZZZ !!!")

    # Gestion des erreurs d'entrées de l'utilisateur
    else:  
        print("\nChoix invalide, tu dois répondre 1, 2 ou 3")
