# Zadanie 4
# Napisz program rysujący choinkę o zadanej wysokości:
# *
# ***
# *****
# *******
# *********
# ***********
# *************
# ***************
# from itertools import count
from itertools import count


def policz():
    wiersz = "***************"  # najwiesza liczba gwiazd w ostatnim wierszu 15
    liczba_gwiazdek = wiersz.count("*") # liczy gwiazdki
    return liczba_gwiazdek

def choinka():
    max_gwiazdek = policz()            # liczba gwiazdek w największym wierszu przypisana do zmiennej max_gwiazdek
    h = (max_gwiazdek + 1) // 2        # obliczamy wysokość choinki, Klasyczna choinka w konsoli ma nieparzystą liczbę gwiazdek w każdym wierszu: 1, 3, 5, …, największa liczba = 2*h - 1.
    for i in range(1, h + 1):           # zapetlenie + atrybuty petli
        spacje = " " * (h - i)          # liczba spacji z lewej strony
        gwiazdki = "*" * (2 * i - 1)    # liczba gwiazdek w tym wierszu
        print(spacje + gwiazdki)        # print zmiennych zeby powstała choinka

choinka()

