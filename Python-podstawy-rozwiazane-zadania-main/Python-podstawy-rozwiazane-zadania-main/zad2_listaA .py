# Napisz program zawierający funkcję zwracającą silnię liczby podanej jako argument. Wskazówka: Policz silnię iteracyjnie

# nie chciałem kombinoac i chciałem wykorzystac juz funkcje ktora istnieje w pythonie


import math


def silnia_liczby_podanej_jako_argument():
    x = int(input("Podaj liczbę: "))

    math.factorial(x)
    print(math.factorial(x))


silnia_liczby_podanej_jako_argument()
