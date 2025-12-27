# Zadanie 4
# Napisz program liczący silnię podanej liczby.
# Np. dla 8 – 40320
# Porada:
# Postaraj się wykonać zadanie w sposób rekurencyjny

kroki = []  # globalna lista na kroki

def silnia(n):
    kroki.append(str(n))  # zapisz krok jako tekst

    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia(n - 1)

def zadanie4b():
    liczba = int(input("Podaj liczbę: "))
    wynik = silnia(liczba)

    # wypisz obliczenia
    print(" * ".join(kroki), "=", wynik)

zadanie4b()