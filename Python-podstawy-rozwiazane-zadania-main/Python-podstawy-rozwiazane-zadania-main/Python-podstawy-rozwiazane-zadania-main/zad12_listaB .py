# Zadanie 12
# Napisz program przyjmujący ciąg znaków i obliczający ile jest w nim liter,
# a ile liczb
# Przykładowe wejście :
# hello world! 123
# Wyjście :
# LITERY 10
# CYFRY 3

def zadanie12b():
    tekst = "hello world! 123"
    litery = 0
    cyfry = 0

    for znak in tekst:
        if znak.isalpha():
            litery += 1
        elif znak.isdigit():
            cyfry += 1

    print("LITERY", litery)
    print("CYFRY", cyfry)

zadanie12b()
