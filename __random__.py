import random


def num_random():
    a = random.randint(0, 2)
    b = random.randint(0, 2)

    print("a:", a)
    print("b:", b)

    if a > b:
        print("Le nombre a est plus grand que le nombre b.")
    elif b > a:
        print("Le nombre b est plus grand que le nombre a.")
    else:
        print("Le nombre a et le nombre b sont égaux.")


num_random()