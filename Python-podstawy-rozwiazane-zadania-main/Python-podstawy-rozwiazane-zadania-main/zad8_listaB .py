# Zadanie 8
# # Napisz program rozwiązujący równanie (x + y) * (x + y)
#
# Przykładowe wejście:
# x = 4, y = 3
# Wyjście :
# (4 + 3) ^ 2) = 49


def zadanie8b():
    x = int(input("Podaj wartość x: "))
    y = int(input("Podaj wartość y: "))

    wynik = (x + y) * (x + y)
    print(f"({x} + {y}) ^ 2 = {wynik}")

zadanie8b()


