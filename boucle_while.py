"""COMMENT UTILISER LA BOUCLE WHILE ?

La boucle while est utilisée pour exécuter du code tant qu'une certaine condition est vérifiée.

Cette boucle est très utile lorsqu'on ne sait pas combien de fois nous devons itérer.

Syntaxe de la boucle while
Une boucle while s'écrit de cette manière :

while condition:
    code
    ....
"""


i = 0
while i < 10:
    print('Salut')
    i += 1
else:
    print('Au revoir')

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

continuer = "o"
while continuer == "o":
    print("On continue !")
    continuer = input("Voulez-vous continuer ? o/n\n")
    if continuer != "o":
        break


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