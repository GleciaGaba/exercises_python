i = 0
while i < 10:
    print('Salut')
    i += 1
else:
    print('Au revoir')

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

continuer ="y"
while continuer == "y":
    print("On continue")
    continuer = input("Voulez-vous continuer ? y/n\n")

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

fruits = ['🍊', '🍋', '🍏', '🍒', '🥭']

for fruit in fruits:
    if fruit == '🍒':
        print('Pas fan des cerises')
        continue

    print(fruit)

print('On passe à la suite')


# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

prenoms = ["Pierre", "Patrick", "Jean", "Marc"]

for prenom in prenoms:
    if prenom == "Patrick":
        print("Patrick a été trouvé !")
        break
else:
    print("Patrick est introuvable...")