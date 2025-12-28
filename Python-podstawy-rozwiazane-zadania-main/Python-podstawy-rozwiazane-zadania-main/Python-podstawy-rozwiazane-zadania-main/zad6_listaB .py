# Zadanie 6
# Napisz program zliczający liczbę 4 w podanej liście

def zadanie6b():
    lista_czworek = [
        "4456.44", "234564", "224562", "124563", "4.42344",
        "234", "222", "123", "4.42344", "879789",
        "567", "457", "789", "90", "12", "25", "68", "90"
    ]

    lista_czworek.sort()
    print(lista_czworek.sort())

    licznik = 0

    for i in lista_czworek:
        print(i)
        licznik += i.count("4")

    print("Cyfra '4' występuje:", licznik, "razy")

zadanie6b()