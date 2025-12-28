# Zadanie 2
# Napisz program wyświetlający liczby podzielne przez 7
# i niebędące wielokrotnością 5 z przedziału 2000 do 3000.
# Liczby te powinny być wyświetlone w jednej linii i oddzielone przecinkami.
# Porada: Wykorzystaj funkcję range()
from operator import index

for index, liczba in enumerate(range(2000, 3001)):
    if liczba % 7 == 0 and liczba % 5 != 0:
        print(index, liczba)

        