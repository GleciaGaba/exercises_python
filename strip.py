"""Écrivez une fonction qui prend une chaîne de caractères contenant des espaces supplémentaires
 avant et après le texte et retourne la chaîne nettoyée."""

def nettoyer_chaine(chaine):

    chaine = chaine.strip()
    return chaine
#print(nettoyer_chaine("   Python est amusant! "))

"""Considérez une chaîne de caractères représentant plusieurs mots séparés par des virgules et des espaces.
 Écrivez une fonction qui extrait les mots de cette chaîne dans une liste,
  en s'assurant qu'il n'y a pas d'espaces avant ou après chaque mot."""

def extrait_de_mot(chaine):
    chaine = chaine.strip()
    chaine_list = chaine.split(",")
    return chaine_list



#print(extrait_de_mot(" pomme, orange , banane , kiwi "))


"""Exercice 3: Suppression de caractères spécifiques
Écrivez une fonction qui enlève des caractères spécifiques (par exemple, # et $)
 du début et de la fin d'une chaîne de caractères."""


def enlever_caracteres(chaine):

    chaine = chaine.strip(" #$")

    return chaine

print(enlever_caracteres("###Ceci est un test$$$# #$"))


"""Exercice 4: Nettoyage d'URL
Imaginez que vous récupérez des URL d'une source de données, mais certaines d'entre elles ont des 
espaces ou des barres obliques / au début ou à la fin. Écrivez une fonction qui nettoie ces URL."""

def nettoyer_url(url):
    url = url.strip(" / ")
    return url
print(nettoyer_url("   https://exemple.com/ "))


"""Exercice 5: Traitement de lignes de fichier
Supposons que vous lisez un fichier ligne par ligne, mais chaque ligne commence et se termine par 
des tabulations et des retours à la ligne. Écrivez une fonction pour nettoyer ces lignes."""

def nettoyer_ligne(ligne):
    ligne = ligne.strip(" \t \n")

    return ligne

ligne = "\tCeci est une ligne d'un fichier.\n"
print(nettoyer_ligne(ligne))

#----------------------------------------------------------------------------------------------------------------------

var = " bonjour".lstrip(" ujor")
print(var)
