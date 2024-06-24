import random
import sys

print("*** Le jeu du nombre mystère ***")
nombre_mystere: int = random.randint(0, 100)

nombre_essai = 5

while True:

    essai = input("Devine le nombre : ")
    if not essai.isdigit():
        print("Veuillez entrer un nombre valide")
        continue
    essai = int(essai)
    nombre_essai -= 1
    if nombre_essai <= -1 and essai != nombre_mystere:
        print(f"Dommage ! Le nombre mystère était {nombre_mystere}")
        print("Fin de jeu.")
        sys.exit()

    if essai < nombre_mystere:
        print(f"Le nombre mystère est plus grand que {essai}")

        print(f"Il reste {nombre_essai} essais.")

    elif essai > nombre_mystere:
        print(f"Le nombre mystère est plus petit que {essai}")

        print(f"Il reste {nombre_essai} essais.")

    elif essai == nombre_mystere:
        print(f"Le nombre mystère est {nombre_mystere}, vous avez gagné !")
        print("Fin de jeu.")
        sys.exit()

    elif essai != nombre_mystere:
        print(f"Dommage ! Le nombre mystère était {nombre_mystere}")
        print("Fin de jeu.")
        sys.exit()

    else:
        print("Vous devez devez écrire un nombre entre 0 et 100")

# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------


from random import randint

number_to_find = randint(0, 100)
remaining_attempts = 5

print("*** Le jeu du nombre mystère ***")

# Boucle principale
while remaining_attempts > 0:
    print(f"Il te reste {remaining_attempts} essai{'s' if remaining_attempts > 1 else ''}")

    # Saisie de l'utilisateur
    user_choice = input("Devine le nombre : ")
    if not user_choice.isdigit():
        print("Veuillez entrer un nombre valide.")
        continue

    user_choice = int(user_choice)

    if number_to_find > user_choice:  # Plus grand
        print(f"Le nombre mystère est plus grand que {user_choice}")
    elif number_to_find < user_choice:  # Plus petit
        print(f"Le nombre mystère est plus petit que {user_choice}")
    else:  # Égal (succès)
        break

    remaining_attempts -= 1

# Gagné ou perdu
if remaining_attempts == 0:
    print(f"Dommage ! Le nombre mystère était {number_to_find}")
else:
    print(f"Bravo ! Le nombre mystère était bien {number_to_find} !")
    print(f"Tu as trouvé le nombre en {6 - remaining_attempts} essai")

print("Fin du jeu.")
