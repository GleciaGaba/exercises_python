mot_de_passe = input("Entrez un mot de passe(min 8 caractères) : ")
mot_len = len(mot_de_passe)
mot_de_passe_is_digit = mot_de_passe.isdigit()
mdp_trop_court = "votre mot de passe est trop court."

if mot_len == 0:
    print(mdp_trop_court)
elif mot_len < 8:
    print(mdp_trop_court.capitalize())
elif mot_de_passe_is_digit is True:
    print("Votre mot de passe ne contient que des nombres.")
else:
    print("Inscription terminée.")
