# Napisz program zawierający funkcję zwracającą silnię liczby podanej jako argument. Wskazówka: Policz silnię iteracyjnie

import math


def silnia_iteracyjna_liczby_podanej_jako_argument():
    #Pobranie liczby od użytkownika
    x = int(input("Podaj liczbę: "))

#Python:
# wyświetli komunikat „Podaj liczbę: ”
#
# poczeka, aż coś wpisze w terminal
#
# input() zwróci tekst (string) - input zawsze zwraca string
#
# int(...) zamieni ten tekst na liczbę całkowitą, bo wcześniej był string

    wynik = 1
#Silnię zaczynamy od 1, bo:
#
# silnia(0) = 1 w moim przypadku zmienna wynik
# i używamy mnożenia, więc 1 jest wartością neutralną
#range(start, stop) generuje liczby od start do stop - 1, czyli nie włącznie ze stop. Dlatego jest x+1. Range nie obejmuje wartości końcowej.

    for i in range(1, x + 1):
        wynik = wynik * i

    print(wynik)


silnia_iteracyjna_liczby_podanej_jako_argument()
