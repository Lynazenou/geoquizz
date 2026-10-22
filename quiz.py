#Quiz

import questions
import random

def quiz():
    global total, vies  # On utilise les mêmes variables que les fonctions de questions
    vies = 3
    total = 0
    NbQuestions = 10
    nom = str(input("Pour commencer donne-moi ton prénom : "))

    print("Tu as 3 vies et tu vas répondre à 10 questions.")
    print("Chaque bonne réponse rapporte 100 points.")

    while vies > 0 and NbQuestions > 0:
        question = random.choice(questions.liste_question)

        vies, total = question(vies, total) # On récupère les valeurs de vies et total MàJ
        NbQuestions -= 1     # On retire une question au compteur

        print(f"\nVies restantes : {vies}")
        print(f"Questions restantes : {NbQuestions}")
        print(f"Score : {total}")

    if vies == 0:
        print("\nTu as perdu toutes tes vies !\n")
        
    elif NbQuestions == 0:
        print("\nBravo, tu as terminé les 10 questions !\n")

    print(f"Score final : {total}")
    return nom,total