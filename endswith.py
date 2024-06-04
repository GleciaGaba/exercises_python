"""Exercice : Filtrer les Noms de Fichiers
Imaginez que vous êtes en charge de développer une fonction qui filtre une liste de noms de fichiers
pour renvoyer uniquement ceux qui correspondent à certaines extensions de fichiers.
Vous devez écrire une fonction qui prend deux paramètres : une liste de noms de fichiers et un tuple
d'extensions valides, et qui renvoie une nouvelle liste contenant uniquement les fichiers qui se
terminent par une des extensions valides."""


# développer une fonction qui filtre une liste de noms de fichiers
# deux paramètres : une liste de noms de fichiers et un tuple et un tuple d'extensions valides
# renvoie une nouvelle liste contenant uniquement les fichiers qui se
# terminent par une des extensions valides

def filter_files(filenames, extensions):
    # Filtrer et retourner la liste des fichiers qui se terminent par une des extensions valides

    filtered = [file for file in filenames if file.endswith(extensions)]
    return filtered


# Exemple d'utilisation
filenames = ['resume.doc', 'holiday.jpg', 'invitation.pdf', 'report.txt', 'photo.png']
extensions = ('.jpg', '.txt')

filtered_files = filter_files(filenames, extensions)
print(filtered_files)  # Affiche ['holiday.jpg', 'report.txt']

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

"""Exercice : Filtrer les URL
Imaginez que vous devez développer une fonction qui filtre une liste d'URLs pour
renvoyer uniquement celles qui commencent par certains protocoles spécifiques.
Vous allez écrire une fonction qui prend deux paramètres : une liste d'URLs et un tuple de protocoles valides, 
et qui renvoie une nouvelle liste contenant uniquement les URLs qui commencent par un des protocoles valides.
"""


# filter URL's list
# it sends only specific protocol
# two parameters: URL's list and valides protocols
# it returns a new list containing only URLSs with valid protocols

def filter_urls(url_list, protocols):
    filtered_urls = [url for url in url_list if url.startswith(protocols)]
    return filtered_urls


url_list = ['http://example.com', 'https://example.org', 'ftp://example.net', 'mailto:user@example.com']
protocols = ("http", " https")

filtered = filter_urls(url_list, protocols)

print(filtered)
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
"""Exercice : Filtrer les Noms de Fichiers Avancé
Imaginez que vous devez développer une fonction pour filtrer une liste de noms de fichiers basée sur deux critères : 
les extensions et les préfixes spécifiques. Cette fonction devra accepter trois paramètres : 
une liste de noms de fichiers, un tuple d'extensions valides, et un tuple de préfixes valides.
 La fonction renverra une nouvelle liste contenant uniquement les fichiers qui commencent par un des
préfixes valides et se terminent par une des extensions valides."""


# filter a list of names with extensions and specific prefixes
# three parameters: filenames, extensions, prefixes
# the function returns a new of files with valid prefixes and extensions

def filter_prefixes_and_extensions(filenames, extensions, prefixes):
    filtered = [file for file in filenames if file.startswith(prefixes) and file.endswith(extensions)]

    return filtered


filenames = ['report_data.txt', 'log_2024.png', 'data_summary.jpg', 'report_final.doc', 'data_2024.txt', 'note.txt']
extensions = ('.txt', '.png')
prefixes = ('report_', 'data_')

filtered_files = filter_prefixes_and_extensions(filenames, extensions, prefixes)
print(filtered_files)
