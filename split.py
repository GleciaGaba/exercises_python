"""
La méthode split() en Python est utilisée pour diviser une chaîne de caractères en une liste de sous-chaînes
 en fonction d'un séparateur spécifié. Si aucun séparateur n'est spécifié,
  la méthode utilise par défaut un espace blanc (' ') comme séparateur, divisant la chaîne en mots."""

text = "Bonjour le monde"
resultat= text.split()
print(resultat)

"""Spécification d'un séparateur : """

text = "Bonjour,le,monde"
resultat = text.split(",")
print(resultat)

"""Utilisation de maxsplit : Dans cet exemple, split() ne divise la chaîne
 que deux fois, laissant le reste de la chaîne intact comme le dernier élément de la liste."""

text = "un deux trois quatre"
resultat = text.split(" ", maxsplit=2)
print(resultat)

"""Exercises:"""

"""Écrivez une fonction qui prend une chaîne de caractères et retourne 
le nombre de mots dans cette chaîne. Un mot est défini comme une séquence 
de caractères séparée par des espaces."""

#fonction qui prend une chaîne de caractères et retourne le nombre de mots dans cette chaîne
#Un mot est défini comme une séquence de caractères séparée par des espaces

def nombre_de_mots(chaine):
    chaine1 = chaine.split()
    mot = len(chaine1)

    return mot
print(nombre_de_mots("Ceci est un exemple de texte"))

"""Pour résoudre l'exercice 1, vous devez écrire une fonction qui compte le nombre de mots dans une chaîne de caractères.
 Un mot est défini comme une séquence de caractères séparée par des espaces. 
 Vous pouvez utiliser la méthode split() pour diviser la chaîne en une liste de mots,
puis retourner la longueur de cette liste. Voici comment cela peut être fait :"""
"""Dans cet exemple, la chaîne "Ceci est un exemple de texte" est divisée en une liste contenant les mots
 ['Ceci', 'est', 'un', 'exemple', 'de', 'texte']. La fonction len() 
 est ensuite utilisée pour compter le nombre d'éléments (mots) dans la liste, 
 qui est retourné comme résultat de la fonction compter_mots."""
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------

"""Exercice 2 : Extraire des données
Supposons que vous ayez une chaîne de caractères représentant des données d'un formulaire sous forme "nom:
John, âge:22, ville:Paris". Écrivez une fonction qui extrait ces données dans un dictionnaire."""

#vous ayez une chaîne de caractères représentant des données d'un formulaire
#"nom:John, âge:22, ville:Paris"
#Écrivez une fonction qui extrait ces données dans un dictionnaire.

def data_extract(form):
    data = {}

    elements = form.split(", ")

    for element in elements:
        key, value = element.split(":")

        data[key] = value

    return data
print(data_extract("nom:John, âge:22, ville:Paris"))


#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
"""Exercice 3 : Le plus long mot
Écrivez une fonction qui trouve le plus long mot dans une 
chaîne de caractères. Si plusieurs mots ont la même longueur maximale,
 retournez le premier rencontré."""

#fonction qui trouve le plus long mot dans une chaîne
#Si plusieurs mots ont la même longueur maximale,retournez le premier rencontré

def find_long_words(words):
    find_word = words.split()

    for word in find_word:
        count_long_word = len(word)

    return count_long_word

print(find_long_words("Trouvez le mot le plus long dans cette phrase"))