"""
Vous vous rappelez de la calculatrice ?

On va améliorer le script que l'on avait fait dans la première partie de ce
projet en y ajoutant la gestion des erreurs.

En effet, en programmation, il ne faut jamais faire confiance à l'utilisateur.

C'est d'ailleurs bien souvent à ça que sert la moitié du code qu'on écrit :
 prévenir les risques d'erreurs, de sécurité et autres.

👉 Dans la deuxième version de ce projet, vous allez devoir créer une calculatrice
en ligne de commande qui demande à l'utilisateur de saisir deux nombres et qui affiche
 ensuite le résultat de l'addition de ces deux nombres.

On va donc également gérer le cas de figure dans lequel l'utilisateur ne rentre pas de données valides.


"""

premier_nombre = (input("Entrez un premier nombre:  "))

deuxieme_nombre = (input("Entrez un deuxième nombre:  "))

verifier_premier_nombre = premier_nombre.isdigit()
verifier_deuxieme_nombre = deuxieme_nombre.isdigit()

if verifier_premier_nombre and verifier_deuxieme_nombre:
    premier_nombre_int = int(premier_nombre)
    deuxieme_nombre_int = int(deuxieme_nombre)

    result = premier_nombre_int + deuxieme_nombre_int
    print(f" Le résultat de l'addition de {premier_nombre} avec {deuxieme_nombre} est égal à {result} ")
else:
    print("Veuillez entrer deux nombres valides")

# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------


a = b = ""

while not (a.isdigit() and b.isdigit()):
    a = input("Entrez un premier nombre : ")
    b = input("Entrez un deuxième nombre : ")
    if not (a.isdigit() and b.isdigit()):
        print("Veuillez entrer deux nombres valides")
print(f"Le résultat de l'addition de {a} avec {b} est égal à {int(a) + int(b)}" )

