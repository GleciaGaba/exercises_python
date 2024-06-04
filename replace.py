# Écrivez une fonction qui prend un texte et une liste de mots à censurer.
# Remplacez chaque mot censuré par des étoiles * de même longueur que le mot.
def censure(texte, mots_censures):
    for mot in mots_censures:
        texte = texte.replace(mot, '*' * len(mot))
    return texte


# Exemple d'utilisation :
# print(censure("Le renard brun saute par-dessus le chien paresseux", ["renard", "chien"]))


"""Imaginez que vous écrivez une fonction pour un système de template de courriels.
La fonction doit remplacer les placeholders dans un template par des valeurs fournies par l'utilisateur.

Les placeholders sont formatés comme suit : {placeholder}.
La fonction prend un template et un dictionnaire de valeurs pour remplacer les placeholders par les valeurs correspondantes.

Voici ce que cela pourrait ressembler :"""


# système de template de curriels.
# replacer placeholders dans un template par des valeurs
# les placeholders sont formatés comme cela: {paceholders}
# la fonction prend un template et un dictionnaire de valeurs pour remplacer les placeholders

def systeme_de_template(template, valeurs):
    for placeholders, valeur in valeurs.items():
        template = template.replace("{" + placeholders + "}", valeur)
    return template


template = "Bonjour {nom} bienvenue sur {site}"
valeurs = {
    "nom": "Alice",
    "site": "notre site Web"
}

# print(systeme_de_template(template, valeurs))

# utilisateur peut ajouter leur propres messages à un script video
# assurer qu'aucun code malveillant ne peut être injecter


# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
"""Exercice : Injection de code sécurisée
Supposons que vous avez un système qui permet aux utilisateurs d'ajouter leurs propres messages à un script de jeu vidéo. 
Vous voulez vous assurer qu'aucun code malveillant ne peut être injecté à travers les messages des utilisateurs.
 Les utilisateurs sont autorisés à utiliser des balises spéciales qui sont encadrées par des crochets [ ], 
 mais tout code Python potentiel doit être désactivé. Votre tâche est de remplacer les crochets par des parenthèses
 ( ), et de s'assurer que si les mots exec ou eval apparaissent, ils soient remplacés par _."""


# système qui permet aux utilisateurs d'ajouter leurs propres messages
# sont autorisés à utiliser des balises spéciales qui sont encadrées par des crochets [ ]
# remplacer les crochets par des parenthèses( )
# exec ou eval soient remplacés par _

def systeme_video(message):

    message_replaced = message.replace("[", "(").replace("]", ")")

    mots = ["eval", "exec"]
    for mot in mots:
        message_replaced = message_replaced.replace(mot, "_")

    return message_replaced


message_cliente1 = "Bienvenue, [joueur]! Pour exécuter un sort, écrivez: exec(sorte)."
message_cliente2 = "Bienvenue, [joueur]! Pour exécuter un sort, écrivez: eval(sorte)."
print(systeme_video(message_cliente1))
print(systeme_video(message_cliente2))


# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------

# fonction qui "traduit" un texte en remplaçant certains mots anglais par leur pseudo-équivalent français
# selon un dictionnaire de traduction fourni
# écrire une fonction qui parcourt le texte et remplace chaque occurrence de mot anglais par sa "traduction" française.


def pseudo_traducteur(texte, dictionnaire_traduction):
    for anglais, francais in dictionnaire_traduction.items():
        texte = texte.replace(anglais, francais)
    return texte


dictionnaire_traduction = {
    "cat": "chat",
    "dog": "chien",
    "bird": "oiseau"
}

texte_anglais = "The cat and the dog are friends, but the bird is afraid."
texte_traduit = pseudo_traducteur(texte_anglais, dictionnaire_traduction)
print(texte_traduit)

# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
"""Exercice : Nettoyage de Log
Imaginons que vous avez un fichier log qui contient des informations sensibles comme des adresses IP et des emails. Vous devez écrire une fonction pour nettoyer ces logs en remplaçant les adresses IP par IP-MASQUEE et les emails par EMAIL-MASQUE.

Pour simplifier, supposons que :

Une adresse IP est une séquence de quatre nombres séparés par des points (e.g., 192.168.1.1).
Un email suit le format nom@domaine.com.

Voici comment vous pourriez structurer la fonction :"""

# fichier log qui contient des informations sensibles comme des adresses IP et des emails
# fonction pour nettoyer ces logs en remplaçant les adresses IP par IP-MASQUEE
# et les emails par EMAIL-MASQUE


import re


def nettoyer_log(texte):
    # Masquer les adresses IP
    texte = re.sub(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', 'IP-MASQUEE', texte)

    # Masquer les emails
    texte = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 'EMAIL-MASQUE', texte)

    return texte


# Exemple d'utilisation
log = "L'utilisateur avec l'IP 192.168.1.1 a envoyé un email à admin@example.com."
print(nettoyer_log(log))

"""re.sub(pattern, repl, string): Cette fonction remplace les occurrences du motif pattern trouvées dans string par repl.
Le motif r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b' est une expression régulière qui correspond à une adresse IP standard (IPv4).
\b correspond à une limite de mot, s'assurant que l'adresse IP est un mot entier.
\d{1,3} correspond à un nombre entre 1 et 3 chiffres, ce qui représente un octet d'une adresse IP.
\. est un point littéral. Dans les expressions régulières, un point seul (.) correspond à n'importe quel caractère, donc il doit être échappé (\.) pour représenter un point littéral.
Chaque adresse IP trouvée est remplacée par la chaîne IP-MASQUEE."""
