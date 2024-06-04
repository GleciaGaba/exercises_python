chaine = "Pierre, Julien, Anne, Marie, Lucien"
chaine_split = chaine.split(", ")
chaine_split.sort()

chaine_en_ordre = ", ".join(chaine_split)


print(chaine_en_ordre)