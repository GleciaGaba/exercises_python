"""
Écrivez le programme permettant de détruire les montagnes pour pouvoir attérir.
Pour cela, tirez sur la montagne la plus haute.


Au début de chaque tour de jeu, vous recevez en entrée la hauteur de chaque montagne de gauche à droite.
Avant la fin du tour de jeu, vous devez indiquer la montagne la plus haute pour tirer dessus.

Tirer sur une montagne ne fera qu'en détruire une partie. Votre vaisseau descend à chaque passe.

"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
while 1:
    max = 0
    imax = 0
    for i in range(8):
        mountain_h = int(input("Entrez un numéro: ")) # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
        if mountain_h > max:
            max = mountain_h
            imax = i

    print(imax)