# Zadanie 11
# Napisz program przyjmujący 2 liczby całkowite (X,Y) i tworzy
# dwuwymiarową tablicę o wymiarach (X,Y). Każdy element i-tego wiersza
# i j-tej kolumny powinien mieć wartość i*j.
# Warunek: i=0,1.., X-1; j=0,1,..Y-1.
# Przykładowe wejście :
# 3,5
# Wyjście :
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

def zadanie11B():
    x = int(input())
    y = int(input())

    # Tworzymy pustą listę, do której będziemy dodawać kolejne wiersze
    tablica = []

    # for i in range(x):
    # Zaczynamy tworzyć liste pt. wiersze.
    # Pętla wykona się x razy — czyli powstanie x wierszy. Przykład: jeśli x = 3, to i będzie
    # kolejno: 0, 1, 2.

    tablica = []
    for i in range(x):
        wiersz = []  # ← musi być tutaj!,  inaczej wszystkie wiersze w tablicy będą takie same, jak sie je da pod tablica bezpośrednio.twrzy sir w tym bloku nowa lista.
        for j in range(y):
            wiersz.append(i * j) # dodaje sie tutaj do listy wiersz iloczyn wartosci "i" i "j"
        tablica.append(wiersz)

zadanie11B()
