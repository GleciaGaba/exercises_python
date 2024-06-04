"""Exercice : Détecteur de Mot-clé
Votre mission est de créer un programme Python qui demande à l'utilisateur d'entrer une
 phrase et un mot-clé. Le programme doit ensuite utiliser la méthode find()
  pour vérifier si le mot-clé est présent dans la phrase et, si oui,
  indiquer la position de la première occurrence de ce mot-clé dans la phrase.

Objectifs
Collecter une phrase de l'utilisateur : Demandez à l'utilisateur de saisir une phrase.
Demander le mot-clé à rechercher : Demandez à l'utilisateur de saisir un mot-clé.
Utiliser la méthode find() : Trouvez la position de la première occurrence du mot-clé dans la phrase.
Afficher les résultats : Informez l'utilisateur de la présence du mot-clé et de sa position,
 ou indiquez que le mot-clé n'est pas présent."""


def phase_word():
    phrase = input("Type the phrase here: ")
    key_word = input("Type the key word here:")
    find_the_key = phrase.find(key_word)

    if find_the_key != -1:
        print(f"The key-word '{key_word}' was found in the position {find_the_key}.")
    else:
        print(f"The key-word '{key_word}' was not found in the phrase")


# -----------------------------------------------------------------------------------------------------------------------

"""Exercice : Vérificateur de Format d'Email
Votre tâche est de créer un programme Python qui demande à l'utilisateur d'entrer une adresse email.  
Le programme doit ensuite utiliser la méthode find() pour vérifier si l'adresse contient le caractère
 @, essentiel pour une adresse email valide. Si @ est présent, le programme doit également vérifier
  si un point . apparaît après le @.

Objectifs
Collecter une adresse email : Demandez à l'utilisateur de saisir une adresse email.
Vérifier la présence de '@' : Utilisez la méthode find() pour voir si l'adresse 
contient le caractère @.
Vérifier la présence de '.' après '@' : Si @ est trouvé, vérifiez si un . apparaît après.
Afficher les résultats : Informez l'utilisateur si l'adresse email semble
 valide ou non selon les critères ci-dessus."""


def email_form():
    user_email = input("Write your email: ")
    verifie_email = user_email.find("@")
    check_point = user_email.find(".")

    if check_point > verifie_email > -1:
        check_point = user_email.find(".")
        print(f"The user email is {user_email}")
    else:
        print(f"User email is incorect")


email_form()
