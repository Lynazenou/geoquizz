#import quiz
#import donnees
#import scores

# Menu principale

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
        print("def quiz.Quizz() à creer")

    # Permet au joueur de consulter les résultats des parties
    elif choix == "2":  
        print("afficher_scores()")


    # Permet au joueur de quitter le jeu
    elif choix == "3":
        continuer = False  # Met fin à la boucle while
        print("À bientôt sur GéoQUIZZZ !!!")

    # Gestion des erreurs d'entrées de l'utilisateur
    else:  
        print("Choix invalide, tu dois répondre 1, 2 ou 3")
