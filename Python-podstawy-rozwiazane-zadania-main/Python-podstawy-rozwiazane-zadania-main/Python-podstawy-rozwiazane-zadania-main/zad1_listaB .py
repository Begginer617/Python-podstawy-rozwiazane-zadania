# Zadanie 1
# Napisz program przyjmujący serię oddzielonych przecinkami liczb z konsoli,
# a zwróci listę oraz krotkę złożoną z tych wartości.

# Przykładowe wejście: 34,60,55,33,12,98
# Wyjście: ['34', '60', '55', '33', '12', '98'] ('34', '60', '55', '33', '12', '98')

# def zadanie_1_B():
#     wejscie = input("Podaj 5 liczb oddzielonych przecinkami: ")
#     lista = wejscie.split(",")
#     krotka = tuple(lista)
#     print(lista)
#     print(krotka)
#
# zadanie_1_B()

#wersja z warunkiem na true
def zadanie_1_B():
    while True:
        wejscie = input("Podaj dokładnie 5 liczb oddzielonych przecinkami: ")
        lista = wejscie.split(",")

        if len(lista) == 5:
            krotka = tuple(lista)
            print("Lista:", lista)
            print("Krotka:", krotka)
            break  # kończymy program, bo dane są poprawne
        else:
            print("Podałeś złą ilość liczb. Spróbuj jeszcze raz!")


zadanie_1_B()
