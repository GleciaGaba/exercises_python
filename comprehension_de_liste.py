"""Les listes en compréhension sont une fonctionnalité puissante et concise de Python qui permet
 de créer de nouvelles listes en appliquant une expression à chaque élément d'une séquence ou d'un
 itérable. Elles sont souvent plus lisibles et plus rapides que les boucles for traditionnelles.
 Voici un guide détaillé sur leur utilisation :"""

liste = [-5, -4, -2, -1, 0, 1, 2, 3, 4, 5]

nombres_positifs = [i for i in liste if i > 0]
print(nombres_positifs)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

liste = [-5, -4, -2, -1, 0, 1, 2, 3, 4, 5]

nombres_positifs_fois_deux = [i * 2 for i in liste if i > 0]
print(nombres_positifs_fois_deux)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

# Créer une liste de nombres carrés :
carres = [x ** 2 for x in range(10)]
print(carres)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

# Transformer une liste de chaînes en majuscules :

mots = ["bonjour", "le", "monde"]
majuscules = [mot.upper() for mot in mots]
majuscules = " ".join(majuscules)
print(majuscules)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

# Filtrer les nombres pairs:

pairs = [x for x in range(20) if x % 2 == 0]
print(pairs)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

# Filtrer et transformer en m^me temps:

carres_pairs = [x ** 2 for x in range(10) if x % 2 == 0]
print(carres_pairs)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

# Listes imbriquées

# Les listes en compréhension peuvent également être utilisées avec des listes imbriquées:

liste_de_listes = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
aplatir = [element for sous_liste in liste_de_listes for element in sous_liste]
print(aplatir)


# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

# Utilisation avancé

# On peut également incluire des expressions plus complexes ou des appels de fonctions:

# Appliquer une fonction à chaque élément:

def double(x):
    return x * 2


doubles = [double(x) for x in range(10)]
print(doubles)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

# Avantages des listes en compréhension

"""
Lisibilité: Elles rendent le code plus compact et souvent plus lisible.

Performance: Elles peuvent être plus rapides que l'utilisation de boucles for d'appels à 'append' pour créer des listes.

Concision : Réduisent le nombre de lignes de code nécessaires por générer une liste.
"""

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

"""
Énoncé :

Créez une liste en compréhension qui contient les carrés des nombres pairs de 0 à 20 (inclus).

Solution attendue
Votre solution devrait utiliser une liste en compréhension pour générer une liste contenant 
les carrés des nombres pairs de 0 à 20.

Voici un exemple de ce à quoi la sortie devrait ressembler :

[0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

"""

carres = [x ** 2 for x in range(21) if x % 2 == 0]
print(carres)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

"""
Exercice
Énoncé :

Créez une liste en compréhension qui contient les longueurs de chaque mot dans une liste de chaînes donnée.
 Par exemple, pour la liste ["Python", "est", "génial"], la sortie devrait être [6, 3, 7].

Solution attendue:
Votre solution devrait utiliser une liste en compréhension pour générer une liste contenant 
les longueurs des mots de la liste donnée.

Voici un exemple de ce à quoi la sortie devrait ressembler pour la liste ["Python", "est", "génial"] :

"""

liste = ["Python", "est", "génial"]

liste_len = [len(mot) for mot in liste]

print(liste_len)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

"""
Énoncé :

Créez une liste en compréhension qui contient uniquement les mots qui commencent par une
voyelle (a, e, i, o, u) à partir d'une liste de mots donnée. Par exemple, pour la 
liste ["apple", "banana", "orange", "umbrella", "kiwi"], la sortie devrait être ["apple", "orange", "umbrella"].

Solution attendue
Votre solution devrait utiliser une liste en compréhension pour générer une liste contenant uniquement
les mots qui commencent par une voyelle.

Voici un exemple de ce à quoi la sortie devrait ressembler pour la 
liste ["apple", "banana", "orange", "umbrella", "kiwi"] :
"""
voyelle = ("a", "e", "i", "o", "u")
liste = ["apple", "banana", "orange", "umbrella", "kiwi"]

liste_voyelle = [mot for mot in liste if mot[0] in voyelle]

print(liste_voyelle)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

"""
Exercice
Énoncé :

Créez une liste en compréhension qui contient les paires (tuple) de nombres (x, y)
pour x allant de 0 à 4 et y allant de 0 à 4, mais uniquement pour les paires où la somme de x et y est un nombre impair.

Solution attendue
Votre solution devrait utiliser une liste en compréhension pour générer une liste contenant 
les paires (x, y) où la somme de x et y est impaire.

Voici un exemple de ce à quoi la sortie devrait ressembler :

python
Copier le code
[(0, 1), (0, 3), (1, 0), (1, 2), (1, 4), (2, 1), (2, 3), (3, 0), (3, 2), (3, 4), (4, 1), (4, 3)]
"""

liste_de_nombres_pairs = [(x, y) for x in range(5) for y in range(5) if (x + y) % 2 != 0]
print(liste_de_nombres_pairs)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


"""
Exercice
Énoncé :

Créez une liste en compréhension qui contient les paires (x, y) pour x allant de 0 à 3 et y allant de 0 à 3, mais uniquement pour les paires où le produit de x et y est inférieur à 4.

Solution attendue
Votre solution devrait utiliser une liste en compréhension pour générer une liste contenant les paires (x, y) où le produit de x et y est inférieur à 4.

Voici un exemple de ce à quoi la sortie devrait ressembler :

python
Copier le code
[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (3, 0)]

"""

nombres_pairs = [(x, y) for x in range(4) for y in range(4) if (x + y) < 4]
print(nombres_pairs)

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

"""
Créez une liste en compréhension qui contient les mots de longueur paire d'une liste de mots donnée.
Par exemple, pour la liste ["python", "is", "fun", "and", "educational"],
la sortie devrait être ["python", "fun", "and"].
"""
liste = ["python", "is", "fun", "and", "educational"]

liste_pairs = [mot for mot in liste if len(mot) % 2 == 0]
print(liste_pairs)