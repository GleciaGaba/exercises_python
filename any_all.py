""" 'any' et 'all' en Python sont très utiles pour vérifier des conditions sur des itérables
(comme des listes, des tuples, des ensembles, etc.).
Voici une explication détaillée de ces fonctions avec des exemples.

Fonction any
La fonction any retourne True si au moins un élément de l'itérable est True. Sinon, elle retourne False.

Syntaxe : any(iterable)

"""

# Fonction any

bool_list = [False, False, True, False]

print(any(bool_list))

# Avec une liste de nombres :

numbers = [0, 0, 0, 1]
print(any(numbers))

# Avec une liste de chaînes :

string = ["", "Hello", ""]
print(any(string))

"""
Fonction all:

La fonction all retourne True si tous les éléments de l'itérable sont True. Sinon, elle retourne False.

all(iterable)

"""

# Avec une liste de valeurs booléennes :

bool_list = [True, True, True, True]
print(all(bool_list))

bool_list = [True, False, True, True]
print(all(bool_list))

# Avec une liste de nombres:

numbers = [1, 2, 3, 4]
print(all(numbers))

numbers = [1, 0, 3, 4]
print(all(numbers))

# Avec une liste de chaînes :

string = ["Hello", "Word", "Python"]
print(all(string))

string = ["Hello", "", "Python"]
print(all(string))


# Utilisation avec des conpréhensions de liste

# Vérifier si au moins un élément dans une liste de nombres est pair:

numbers = [1, 3, 5, 7, 8]
print(any(n % 2 == 0 for n in numbers))

# Vérifier si tous les éléments dans une liste de nombres sont positifs:

numbers = [1, 2, 3, 4, 5]
print(all(n > 0 for n in numbers))

numbers = [1, 2, -3, 4, 5]
print(all(n > 0 for n in numbers))

















