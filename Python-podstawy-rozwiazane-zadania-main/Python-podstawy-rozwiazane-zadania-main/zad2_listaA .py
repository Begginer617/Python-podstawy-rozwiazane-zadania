# Napisz program zawierający funkcję zwracającą silnię liczby podanej jako argument. Wskazówka: Policz silnię iteracyjnie

import math


def silnia_iteracyjna_liczby_podanej_jako_argument():

    x = int(input("Podaj liczbę: "))
    wynik = 1
    for i in range(1, x + 1):
    wynik = wynik * i
    print(wynik)

silnia_iteracyjna_liczby_podanej_jako_argument()
