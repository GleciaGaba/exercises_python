"""Exercice : Validation des Balises HTML
Votre mission est de créer un programme Python qui demande à l'utilisateur d'entrer une chaîne
de texte contenant des balises HTML. Le programme doit ensuite utiliser la méthode index()
pour vérifier si chaque balise ouvrante <tag> a une balise fermante correspondante </tag>.
Pour simplifier, nous allons supposer que les balises ne sont pas imbriquées."""
import datetime


def html_validation():
    user_input = input("Write here your text in html format: ")
    tags_html = ["div", "a", "span", "head", "body"]

    for tag in tags_html:
        try:
            open_tag = f"<{tag}>"
            close_tag = f"</{tag}>"
            open_index = user_input.index(open_tag)

            closed_index = user_input.index(close_tag, open_index + len(open_tag))

            print(f"The tag '{tag}' is correct with open and close tags")


        except ValueError:

            print(f"The tag '{tag}' is not correct, please check your tags")


# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

"""Exercice : Extraction de données de Logs
Description de l'exercice
Vous travaillez avec un système qui enregistre des logs de transactions financières. Chaque entréede log contient une
date, un type de transaction (Dépôt ou Retrait), et un montant, le tout dans une chaîne de caractères.
Votre tâche est d'écrire un programme Python qui extrait et affiche séparément la date, le type de transaction,
et le montant pour chaque entrée de log.

Format des logs
Chaque log suit ce format : "YYYY-MM-DD TransactionType Montant"

Objectifs
Extraire et afficher la date.
Extraire et afficher le type de transaction.
Extraire et afficher le montant de la transaction.

"""


def information_extractor():
    log = input(
        "Enter log information according to the following format (format 'YYYY-MM-DD TransactionType Montant'): ")

    first_space = log.index(" ")
    second_space = log.index(" ", first_space + 1)

    date = log[:first_space]
    type_transaction = log[first_space + 1: second_space]
    total = log[second_space + 1:]

    print("Date:", date)
    print("Type de transaction:", type_transaction)
    print("Montant:", total)


"""Si vous omettez le + 1, index() chercherait à nouveau à partir de l'indice 10 et trouverait le même espace,
 ce qui n'est pas ce que nous voulons. En ajoutant 1, la recherche commence à l'indice 11, ce qui permet de trouver
  le prochain espace dans la chaîne.

En somme, l'utilisation de + 1 est essentielle pour avancer correctement dans la chaîne et pour trouver les
éléments suivants de manière séquentielle sans se retrouver coincé sur le même élément."""

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

"""Exercice : Analyseur de Journal de Bord de Navigation
Description de l'exercice
Imaginez que vous travaillez avec un système qui enregistre des entrées de journal de bord pour un navire. 
Chaque entrée de journal contient une date, une heure, et une description de l'événement. Votre tâche est
d'écrire un programme Python qui extrait et affiche séparément la date, l'heure, et la description
de l'événement pour chaque entrée de journal.

Format des entrées de journal
Chaque entrée de journal suit ce format : "YYYY-MM-DD HH:MM Description"""


# enregistre des entrées de journal de bord
# Chaque entrée de journal contient une date, une heure, et une description
# extrait et affiche séparément la date, l'heure, et la description de l'événement pour chaque entrée de journal

def newspaper():
    paper = input(
        "Enter log information according to the following format (format 'YYYY-MM-DD HH:MM Description'): ")

    first_space = paper.index(" ")
    second_space = paper.index(" ", first_space + 1)
    two_points = paper.index(":")

    date = paper[:first_space]
    hour = paper[first_space + 1:second_space]
    description = paper[second_space + 1:]

    print("Date:", date)
    print("Heure:", hour)
    print("Description de l'événement:", description)

newspaper()
