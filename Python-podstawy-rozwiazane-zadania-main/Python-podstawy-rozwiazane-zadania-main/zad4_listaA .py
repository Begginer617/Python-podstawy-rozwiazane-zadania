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
    h = (max_gwiazdek + 1) // 2        # obliczamy wysokość choinki, Klasyczna choinka w konsoli ma nieparzystą liczbę gwiazdek w każdym wierszu: 1, 3, 5, …, największa liczba = 2*h - 1 = czyli 15
    for i in range(1, h + 1):           # zapętlenie + atrybuty pętli
        spacje = " " * (h - i)          # liczba spacji z lewej strony 15-i=7 daje 8
        gwiazdki = "*" * (2 * i - 1)    # liczba gwiazdek w tym wierszu
        print(spacje + gwiazdki)        # print zmiennych, żeby powstała choinka

choinka()


#
# | i (wiersz) | spacje (`h - i`) | gwiazdki (`2*i - 1`) | wizualizacja      |
# | ---------- | ---------------- | -------------------- | ----------------- |
# | 1          | 7                | 1                    | `       *`        |
# | 2          | 6                | 3                    | `      ***`       |
# | 3          | 5                | 5                    | `     *****`      |
# | 4          | 4                | 7                    | `    *******`     |
# | 5          | 3                | 9                    | `   *********`    |
# | 6          | 2                | 11                   | `  ***********`   |
# | 7          | 1                | 13                   | ` *************`  |
# | 8          | 0                | 15                   | `***************` |

