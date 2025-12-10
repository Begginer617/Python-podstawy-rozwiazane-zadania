# Zadanie 5
# Napisz program sprawdzający, czy podana liczba jest liczbą pierwszą.

def czy_podana_liczba_jest_liczbą_pierwszą():
    n = int(input("Podaj liczbę, a powiem Ci, czy jest liczbą pierwszą: "))

    if n < 2:
        print("Nie jest liczbą pierwszą")
        return

    for i in range(2, n):
        if n % i == 0:
            print("Nie jest liczbą pierwszą")
            return

    print("Jest liczbą pierwszą")

czy_podana_liczba_jest_liczbą_pierwszą()

