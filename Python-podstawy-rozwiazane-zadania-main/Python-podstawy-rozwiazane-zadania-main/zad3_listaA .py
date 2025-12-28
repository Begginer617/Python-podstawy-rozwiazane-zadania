def silnia_rekurencyjna(n):
    if n == 0 or n == 1:  # przypadek bazowy
        return 1
    else:
        return n * silnia_rekurencyjna(n - 1)  # wywołanie rekurencyjne

# Przykład użycia:
print(silnia_rekurencyjna(0))  #1
print(silnia_rekurencyjna(1))  #1
print(silnia_rekurencyjna(2))  #2
print(silnia_rekurencyjna(3))  #6
print(silnia_rekurencyjna(4))  # 24
print(silnia_rekurencyjna(5))  # 120

#silnia(1) = 1
# silnia(2) = 2 * 1 = 2
# silnia(3) = 3 * 2 = 6
# silnia(4) = 4 * 6 = 24