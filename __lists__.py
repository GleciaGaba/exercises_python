# Indice négatif, pour insérer un élément en partant de la fin de la liste

villes = ['Paris', 'Lille', 'Lyon']
villes.insert(-1, 'Strasbourg')
villes.insert(-2, 'Nice')
print(villes)

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

# Ajouter et enlever des elements dans une liste

liste = [5]
liste.append(3)  # [5, 3]
liste.extend([20, "Python"])  # [5, 3, 20, "Python]
liste.remove("Python")  # [5, 3, 20]

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

# D'autres methodes pour enlever des éléments

employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]
element = employes.pop(
    -1)  # retire le dernier élément de la liste (ici, "Alex") et le retourne dans la variable 'element'
print(employes)  # ['Carlos', 'Max', 'Martine', 'Patrick']
print(element)  # Alex

employes.clear()  # supprime tous les éléments de la liste

print(employes)

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

# D'autres methodes sur les listes

employes = ["Carlos", "Max", "Martine", "Patrick", "Alex", "Max"]
print(employes.index("Alex"))  # 4
print(employes.count("Max"))  # 2
employes.sort()  # Trie la liste en la modifiant directement : ["Alex", "Carlos", "Martine", "Max", "Max", "Patrick"]
print(sorted(employes))  # Trie la liste mais ne modifie pas la liste d'origine !

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
nombres = [10, 1, 5, 15]
nombres.reverse()  # Inverse l'ordre de la liste : [15, 5, 1, 10]
print(nombres)

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

liste = ["Python", "est", "une", "langage", "incroyable"]
print(" ".join(liste))  # 'Python est un langage incroyable'
print("-".join(liste))  # Python - est - un - langage - incroyable
print("".join(liste))  # Pythonestunlangageincroyable

resultat = "\n".join(liste)
print(resultat)

# Python
# est
# un
# langage
# incroyable

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

# Listes imbriques

liste = ["Python", ["Java", "C++", ["C"]], ["Ruby"]]

print(liste[0])  # Python
print(liste[-1][0])  # Ruby
print(liste[0][0:2])  # Py
print(liste[1][1])  # C++
print(liste[1][:2])  # ['Java', 'C++]



