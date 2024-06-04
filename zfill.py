# Exemple 1: Ajouter des zéros devant un nombre
numero = "50"
numero_zfill = numero.zfill(5)
print(numero_zfill)  # Résultat : 00050

# Exemple 2: Utilisation avec une chaîne qui a déjà des zéros
texte = "007"
texte_zfill = texte.zfill(5)
print(texte_zfill)  # Résultat : 00007

# Exemple 3: Chaîne plus longue que la largeur spécifiée
texte_long = "Python"
texte_long_zfill = texte_long.zfill(10)
print(texte_long_zfill)  # Résultat : Python (pas de changement car la chaîne est déjà plus longue que 3)

"""Exercice : Formatage de numéros de série

Imaginez que vous travaillez dans une entreprise qui fabrique des appareils électroniques. 
Chaque appareil est attribué un numéro de série unique lors de sa fabrication. 
Le format du numéro de série est le suivant : Axxxx, 
où A est une lettre qui représente l'année de fabrication (par exemple, A pour 2020,B pour 2021, etc.),
et xxxx est un numéro séquentiel qui commence à 1 et est formaté pour avoir toujours quatre chiffres
 en incluant des zéros au début si nécessaire.

Votre tâche est d'écrire une fonction en Python qui prend en entrée une lettre représentant l'année et un numéro
séquentiel, puis retourne le numéro de série formaté correctement.

Par exemple :

Si l'entrée est ('A', 3), la sortie devrait être 'A0003'.
Si l'entrée est ('B', 123), la sortie devrait être 'B0123'.
Vous pouvez assumer que le numéro séquentiel est toujours un nombre positif et que la lettre est toujours
 une chaîne de caractère de longueur 1.

Une fois que vous avez écrit votre fonction, testez-la avec quelques entrées pour vérifier qu'elle 
fonctionne comme prévu.
"""


# Chaque appareil est attribué un numéro de série unique lors de sa fabrication
# A est une lettre qui représente l'année de fabrication
# xxxx est un numéro séquentiel qui commence à 1 et est formaté pour avoir toujours quatre chiffres
# en incluant des zéros au début si nécessaire


def letter_represented(year, number):
    years = year
    numbers = str(number).zfill(4)

    years_numbers = years + numbers

    return years_numbers


print(letter_represented('A', 5))

"""Exercice : Vérification de code IBAN

L'IBAN (International Bank Account Number) est un système international conçu pour identifier les 
comptes bancaires à travers le monde. Il réduit les erreurs dans les transferts d'argent. 
Un IBAN se compose de lettres et de chiffres, et sa longueur varie d'un pays à l'autre, 
allant jusqu'à 34 caractères.

Votre tâche est de créer une fonction en Python qui vérifie si un IBAN donné respecte les critères de base suivants :

La longueur de l'IBAN est correcte selon le pays. (Pour simplifier, utilisons 22 caractères comme
longueur correcte pour cet exercice, bien que dans la réalité, chaque pays ait sa propre longueur spécifique.)
L'IBAN ne contient que des chiffres et des lettres majuscules.
La fonction doit prendre un IBAN comme argument (une chaîne de caractères) et retourner 
True si les deux critères ci-dessus sont remplis, ou False sinon.

Exemple de critères à vérifier dans votre fonction :

FR7612345987650123456789014 devrait retourner True (pour cet exercice, on suppose que c'est la longueur
correcte et qu'il contient uniquement des chiffres et des lettres majuscules).
FR76 1234 5987 6501 2345 6789 014 devrait retourner False (contient des espaces).
fr7612345987650123456789014 devrait retourner False (contient des lettres minuscules).
FR7612345987650123456789 devrait retourner False (longueur incorrecte pour cet exercice).
N'hésitez pas à vous lancer, et si vous avez besoin d'aide ou voulez que je vérifie votre solution, je suis là !"""


# fonction en Python qui vérifie si un IBAN donné respecte les critères
# Un IBAN se compose de lettres et de chiffres
# allant jusqu'à 22  caractères

def iban_verifier(iban):
    iban_string = iban.zfill(22).upper().replace(" ", "")
    if iban == iban_string:
        return True
    else:
        return False


print(iban_verifier('FR7612345987650123456789014'))
print(iban_verifier('FR76 1234 5987 6501 2345 6789 014'))
print(iban_verifier('fr7612345987650123456789014'))
print(iban_verifier('FR7612345987650123'))
