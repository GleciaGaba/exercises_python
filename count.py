"""Exercice : Analyseur de Texte
Écrivez un programme en Python qui demande à l'utilisateur d'entrer une phrase ou un paragraphe,
 puis effectue les analyses suivantes pour afficher :

Le Nombre Total de Mots : Comptez combien de mots la phrase ou le paragraphe contient.
Le Nombre d'Occurrences de Chaque Mot : Affichez combien de fois chaque mot apparaît dans le texte.
 Ignorez la casse, c'est-à-dire que "Python" et "python" devraient être comptabilisés ensemble.
Le Mot le Plus Fréquent : Identifiez quel mot apparaît le plus souvent dans le texte.
Le Nombre de Caractères : Comptez le nombre total de caractères (en incluant les espaces).
Le Nombre de Caractères (sans espaces) : Comptez le nombre total de caractères, mais excluez les espaces.
Conseils pour Démarrer :

Vous pouvez utiliser la méthode input() pour lire l'entrée de l'utilisateur.

La méthode split() peut être utile pour transformer la chaîne de caractères en une liste de mots.

Pour ignorer la casse, vous pourriez vouloir convertir toute la chaîne en minuscules avec lower() avant de compter les mots.

Utilisez un dictionnaire pour garder une trace du nombre d'occurrences de chaque mot.

Parcourez la liste des mots pour remplir le dictionnaire et effectuer les comptages nécessaires.

Exemple de Sortie Attendue
Pour le texte "Hello world. Hello Python.", le programme pourrait afficher quelque chose comme :"""


# demande à l'utilisateur d'entrer une phrase ou un paragraphe
# Le Nombre Total de Mots : Comptez combien de mots la phrase ou le paragraphe contient
# Le Nombre d'Occurrences de Chaque Mot : Affichez combien de fois chaque mot apparaît dans le texte.
# Ignorez la casse
# Le Mot le Plus Fréquent : Identifiez quel mot apparaît le plus souvent dans le texte.
# Le Nombre de Caractères : Comptez le nombre total de caractères (en incluant les espaces)


def analyse_texte():
    texte = input("Entrez un texte pour analyse :")

    texte_lower = texte.lower()

    mots = texte_lower.split()

    occurrences = {}

    for mot in mots:
        if mot in occurrences:
            occurrences[mot] += 1
        else:
            occurrences[mot] = 1

    mot_plus_frequent = max(occurrences, key=occurrences.get)
    frequence_max = occurrences[mot_plus_frequent]

    nb_caracteres_avec_espaces = len(texte)
    nb_caracteres_sans_espaces = len(texte.replace(" ", ""))

    print(f"Nombre total de mots: {len(mots)}")
    print("Occurrences par mot :")
    for mot, compte in occurrences.items():
        print(f"{mot}:{compte}")

    print(f"Mot le plus fréquent : {mot_plus_frequent} (apparaît {frequence_max} fois)")
    print(f"Nombre total de caractères (avec espaces) : {nb_caracteres_avec_espaces}")
    print(f"Nombre total de caractères (sans espaces) : {nb_caracteres_sans_espaces}")


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

"""Exercice : Analyseur de Transactions Bancaires

Vous êtes chargé de créer un programme Python qui analyse une liste de transactions bancaires et
 fournit un résumé statistique des activités du compte.

Données
Vous recevrez une liste de transactions sous forme de chaînes de caractères, où chaque transaction 
est représentée par une chaîne contenant le type de transaction ("dépôt" ou "retrait") suivi du 
montant séparé par un espace. Par exemple : ["dépôt 100", "retrait 50", "dépôt 200", "retrait 30"].

Objectifs
Calculer le solde final : Déterminez le solde final du compte après toutes les transactions.
Compter le nombre de transactions : Calculez le nombre total de transactions effectuées.
Identifier le plus grand dépôt : Trouvez le montant du plus grand dépôt effectué.
Identifier le plus grand retrait : Trouvez le montant du plus grand retrait effectué.
Calculer les moyennes : Déterminez la moyenne des montants des dépôts et des retraits."""


def list_of_transaction(transactions):
    solde = 0
    nb_transaction = len(transactions)
    max_depot = 0
    max_retrait = 0
    total_depot = 0
    total_retraits = 0
    nb_depots = 0
    nb_retraits = 0

    for transaction in transactions:
        mots = transaction.split()
        type_transaction = mots[0]
        montant = int(mots[1])

        if type_transaction == "dépôt":
            solde += montant
            total_depot += montant
            nb_depots += 1
            if montant > max_depot:
                max_depot = montant
        elif type_transaction == "retrait":
            solde -= montant
            total_retraits += montant
            nb_retraits += 1
            if montant > max_retrait:
                max_retrait = montant

    moyenne_depots = total_depot / nb_depots if nb_depots > 0 else 0
    moyenne_retraits = total_retraits / nb_retraits if nb_retraits > 0 else 0
    # print(f"Nombre total de transactions : {nb_transaction}")
    # print(f"Solde final : {solde}")
    # print(f"Plus grand dépôt : {max_depot}")
    # print(f"Plus grand retrait : {max_retrait}")
    # print(f"Moyenne des dépôts : {moyenne_depots}")
    # print(f"Moyenne des retraits : {moyenne_retraits}")


transactions = ["dépôt 100", "retrait 50", "dépôt 200", "retrait 30"]
list_of_transaction(transactions)

# ----------------------------------------------------------------------------------------------------------------------

def analyse_de_char():
    type_by_user = input("Please, type here your frase: ").lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for lettre in alphabet:
        compt = type_by_user.count(lettre)
        if compt > 0:
            print(f"Le caractère '{lettre}' apparait {compt} fois")


analyse_de_char()

# -----------------------------------------------------------------------------------------------------------------------
"""
Bien sûr, voici un nouvel exercice qui nécessite l'utilisation de la méthode count() dans un 
contexte un peu différent, en se concentrant sur les listes cette fois-ci.

Exercice : Analyseur de Présence de Mots
Votre mission est de créer un programme Python qui demande à l'utilisateur d'entrer une liste de mots,
 puis un mot spécifique à rechercher dans cette liste. Le programme doit ensuite utiliser la méthode 
 count() pour déterminer combien de fois ce mot spécifique apparaît dans la liste.

Objectifs
Collecter des données utilisateur : Demandez à l'utilisateur d'entrer une séquence de mots séparés par des virgules.
Demander le mot à rechercher : Demandez ensuite à l'utilisateur quel mot il souhaite rechercher 
dans la liste qu'il a fournie.
Compter les occurrences : Utilisez la méthode count() pour trouver et afficher le nombre de fois que
 le mot recherché apparaît dans la liste."""


def words_analyse():
    user_words = input("Write a list of words separates by a comma: ")
    words_list = user_words.split(", ")
    word_list = [word.strip().lower() for word in words_list]
    search_word = input("Write word to research: ").strip().lower()

    repeated_words = word_list.count(search_word)

    print(f"The word '{search_word}' appears {repeated_words} times in the list.")


# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------


