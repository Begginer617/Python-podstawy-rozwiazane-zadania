# Napisz program suma.py, który wyświetli sumę dwóch liczb podanych przez użytkownika

def dodaj_liczby():
    # Pobierz dwie liczby od użytkownika
    x = input("Podaj pierwszą liczbę: ")
    y = input("Podaj drugą liczbę: ")

    # Zamień na liczby całkowite i dodaj
    suma = int(x) + int(y)

    # Wyświetl wynik
    print("Suma wynosi:", suma)

    # Zwróć wynik (jeśli chcesz go użyć później)
    return suma

    # Wywołanie funkcji
dodaj_liczby()