# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------

"""
COMMENT UTILISER LA BOUCLE FOR ?

Avec Python, on utilise la boucle for pour parcourir des objets itérables comme les listes,
les tuples ou encore les chaînes de caractères.

C'est une boucle commune à presque tous les langages de programmation.

Syntaxe de la boucle for
Une boucle for s'écrit de la manière suivante :

for value in object:
    code
    ....
    
En pratique, cela donne :

fruits = ['🍊', '🍋', '🍏', '🍒', '🥭']

for fruit in fruits:
    print(fruit)    



for ... else

Comme pour les structures conditionnelles if..else, 
vous pouvez définir un comportement par défaut pour votre boucle for grâce au mot-clé else.

Ce mot clé est optionnel, mais cela vous permet d'exécuter du code lorsque la boucle for est terminée :

"""
fruits = ['🍊', '🍋', '🍏', '🍒', '🥭']

for fruit in fruits:
    print(fruit)
else:
    print('Plus de fruits dans le panier')





# Exemples

for i in range(3):
    print(i)

prenom = "John"
for lettre in prenom:
    print(lettre)

for (pk, name) in [(1, "Patrick"), (2, "John"), (3, "Marie")]:
    print(pk, name)


