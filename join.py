lignes = ['Première ligne', 'Deuxième ligne', 'Troisième ligne']
texte = '\n'.join(lignes)
print(texte)

elements = ['Ceci', 'est', 'un', 'exemple', 'de', 'concaténation', 'de', 'chaînes.']
resultat = " ".join(elements)  # Beaucoup plus efficace

print(resultat)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

"""Imaginons que vous travaillez sur un script Python qui génère un fichier CSV 
(valeurs séparées par des virgules) à partir de données stockées dans une liste de listes.
 Chaque sous-liste contient des éléments qui représentent une ligne dans le fichier CSV. 
 Vous pouvez utiliser la méthode join() pour convertir chaque sous-liste en une chaîne de caractères,
  avec chaque élément séparé par une virgule. Ensuite, vous pouvez joindre toutes ces chaînes avec
un saut de ligne (\n) pour former le contenu complet du fichier CSV."""

# Données à écrire dans un fichier CSV
donnees = [
    ['Nom', 'Âge', 'Ville'],
    ['Alice', '24', 'Paris'],
    ['Bob', '30', 'Lyon'],
    ['Charlie', '28', 'Marseille']
]

# Convertir chaque sous-liste en une chaîne de caractères, en séparant les éléments par une virgule
lignes = [','.join(ligne) for ligne in donnees]

# Joindre toutes les chaînes de caractères avec un saut de ligne pour former le contenu du fichier CSV
contenu_csv = '\n'.join(lignes)

# Afficher le contenu du fichier CSV
print(contenu_csv)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

"""
Si vous avez une liste contenant des nombres et que vous souhaitez les joindre en une seule chaîne de caractères,
 avec, par exemple, des virgules comme séparateurs, vous devez d'abord convertir ces nombres en chaînes. 
 Voici deux façons de le faire :

1. Utilisation d'une compréhension de liste
La compréhension de liste est une méthode concise pour créer des listes. Vous pouvez l'utiliser pour parcourir tous 
les éléments de la liste originale, convertir chaque élément en chaîne et générer une nouvelle liste de chaînes."""

nombres = [1, 2, 3, 4, 5]

# Convertir chaque nombre en chaîne de caractères
chaines = [str(nombre) for nombre in nombres]

# Joindre les chaînes avec des virgules comme séparateurs
resultat = ','.join(chaines)

print(resultat)  # 1,2,3,4,5

# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------

"""2. Utilisation de la fonction map()
La fonction map() applique une fonction à tous les éléments d'un itérable et retourne un nouvel itérable.
 Vous pouvez l'utiliser pour appliquer la fonction str à chaque élément de la liste originale,
convertissant ainsi tous les nombres en chaînes."""

nombres = [1, 2, 3, 4, 5]

# Utiliser map pour convertir chaque nombre en chaîne de caractères
chaînes = map(str, nombres)

# Joindre les chaînes avec des virgules comme séparateurs
resultat = ','.join(chaînes)

print(resultat)  # 1,2,3,4,5

# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------

"""Concaténer des chaînes de caractères en utilisant l'opérateur + dans une boucle peut être coûteux en termes de 
performance, surtout pour de grandes quantités de chaînes. Cela est dû au fait que les chaînes en Python sont 
immuables, ce qui signifie que chaque fois que vous concaténez des chaînes avec +, Python doit créer une nouvelle 
chaîne et copier les anciennes données dans cette nouvelle chaîne. Cela entraîne une utilisation élevée de la mémoire
 et une baisse de performance avec un grand nombre de chaînes.

À l'inverse, join() est conçu pour être efficace pour de telles opérations, car il calcule la taille 
totale nécessaire pour la nouvelle chaîne une seule fois, alloue cet espace, et copie ensuite les éléments,
 ce qui réduit considérablement le nombre d'opérations d'allocation et de copie.

Exemple avec l'opérateur + dans une boucle :"""

elements = ['Ceci ', 'est ', 'un ', 'exemple ', 'de ', 'concaténation ', 'de ', 'chaînes.']
resultat = ""
for element in elements:
    resultat += element  # Concaténation inefficace pour un grand nombre d'éléments

print(resultat)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

"""Exemple avec join() :"""

elements = ['Ceci ', 'est ', 'un ', 'exemple ', 'de ', 'concaténation ', 'de ', 'chaînes.']
resultat = "".join(elements)  # Beaucoup plus efficace

print(resultat)
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------

'''Exercice : Création d'une Adresse URL
Vous travaillez sur une application web qui génère des URLs dynamiques en fonction des choix de 
l'utilisateur. Les utilisateurs peuvent sélectionner différentes catégories, et vous devez générer
 une URL correspondante. Les catégories sont stockées dans une liste, et vous devez les joindre en 
 utilisant des tirets (-) comme séparateurs. De plus, vous devez ajouter https://monsite.com/categories/ 
 au début de l'URL générée.

Objectif : Écrivez une fonction creer_url qui prend une liste de catégories et retourne l'URL complète.

Exemple d'entrée :'''


# application web qui génère des URLs dynamiques en fonction des choix
# Les utilisateurs peuvent sélectionner différentes catégories
# vous devez générer une URL correspondante
# Les catégories sont stockées dans une liste
# vous devez les joindre en utilisant des tirets (-)
# https://monsite.com/categories/ au début de l'URL générée.
# Écrivez une fonction creer_url qui prend une liste de catégories et retourne l'URL complète

def create_url(choices):
    add_hyphen = "-".join(choises)

    creating_url = f"https://monsite.com/categories/{add_hyphen}"

    return creating_url


choises = ["technologie", "blogs", "tutoriels"]
print(create_url(choises))

# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------

"""Exercice : Générer une Liste de Courses Formatée
Imaginez que vous développez une application pour aider les utilisateurs à organiser leurs courses.
 L'application permet à l'utilisateur d'entrer une liste d'articles à acheter,
mais pour faciliter la lecture, vous souhaitez formater cette liste en une seule chaîne de caractères,
avec chaque article séparé par une virgule et un espace. De plus, 
chaque article doit commencer par une majuscule, indépendamment de comment l'utilisateur l'a saisi.
Enfin, ajoutez "Votre liste de courses : " au début de la chaîne formatée.

Objectif : Écrivez une fonction formater_liste_courses qui prend une liste d'articles de courses
(comme une liste de chaînes de caractères) et retourne la liste formatée comme une chaîne de caractères."""


# application pour aider les utilisateurs à organiser leurs courses
# l'utilisateur d'entrer une liste d'articles à acheter
# vous souhaitez formater cette liste en une seule chaîne de caractères, avec chaque article séparé par une virgule et un espace
# chaque article doit commencer par une majuscule
# ajoutez "Votre liste de courses : " au début de la chaîne formatée

def list_organiser(grocery_list):
    creating_list = ", ".join(grocery_list)
    title_list = creating_list.title()
    your_list = f"Votre liste de courses : {title_list}"
    return your_list


grocery_list = ["pommes", "bananes", "lait", "pain"]

print(list_organiser(grocery_list))

# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------

"""Exercice : Formatage d'Adresses Email
Vous travaillez sur un système qui gère les informations de contact. Une fonctionnalité requise est de 
pouvoir générer une adresse email basée sur le nom et le prénom d'une personne, 
ainsi que sur le domaine de l'email. Le format de l'adresse email devrait être prenom.nom@domaine.com. 
Tout doit être en minuscules, même si le nom ou le prénom sont entrés avec des majuscules. 
De plus, si le prénom ou le nom contiennent des espaces ou des tirets (par exemple, "Jean-Pierre" ou "De L'Écluse"),
 ces caractères doivent être remplacés par un point "."

Objectif : Écrivez une fonction generer_email qui prend trois chaînes de caractères : 
prénom, nom, et domaine, et retourne l'adresse email formatée."""


# Vous travaillez sur un système qui gère les informations de contact
# générer une adresse email basée sur le nom et le prénom d'une personne
# ainsi que sur le domaine de l'email
# Le format de l'adresse email devrait être prenom.nom@domaine.com.
# Tout doit être en minuscules, même si le nom ou le prénom sont entrés avec des majuscules
# si le prénom ou le nom contiennent des espaces ou des tirets (par exemple, "Jean-Pierre" ou "De L'Écluse"),ces caractères doivent être remplacés par un point "."

def contact_informations(name, surname, domain):
    correct_name = name.replace("-", ".").lower()
    correct_surname = surname.replace("'", ".").replace(" ", ".").lower()
    full_name_domain = f"{correct_name}.{correct_surname}@{domain}"
    return full_name_domain


name = "Jean-Pierre"
surname = "De L'Écluse"
domain = "exemple.com"
print(contact_informations(name, surname, domain))


# correction

def generer_email(prenom, nom, domaine):
    # Remplacer les espaces et les tirets par des points dans le prénom et le nom
    prenom_formatte = prenom.replace(" ", ".").replace("-", ".")
    nom_formatte = nom.replace(" ", ".").replace("-", ".")

    # Convertir le prénom, le nom et le domaine en minuscules
    prenom_formatte = prenom_formatte.lower()
    nom_formatte = nom_formatte.lower()
    domaine = domaine.lower()

    # Assembler les parties de l'email en utilisant join()
    email = "@".join([".".join([prenom_formatte, nom_formatte]), domaine])

    return email


# Exemple d'utilisation
prenom = "Jean-Pierre"
nom = "De L'Écluse"
domaine = "exemple.com"
print(generer_email(prenom, nom, domaine))
