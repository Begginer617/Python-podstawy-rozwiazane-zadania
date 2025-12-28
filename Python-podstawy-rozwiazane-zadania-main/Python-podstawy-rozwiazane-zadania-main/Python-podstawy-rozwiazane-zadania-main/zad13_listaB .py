# Zadanie 13
# Napisz program obliczający saldo na koncie na bazie logów z
# bankomatu.
# Format logów:
# + 100
# - 200
# Przykładowe wejście :
# + 300
# + 300
# - 200
# + 100
# Wyjście :
# 500

def zadanie13b():
    logi = [
        "+ 300",
        "+ 300",
        "- 200",
        "+ 100"
    ]

    saldo = 0

    for wpis in logi:
        znak, kwota = wpis.split()   # np. "+" i "300"
        print(wpis.split())

        # split() rozdziela tekst po spacji.
        # Przykład:
        # "+ 300".split() → ["+", "300"]
        # Czyli:
        # - znak = "+"
        # - kwota = "300"


        kwota = int(kwota)

        if znak == "+":
            saldo += kwota
        elif znak == "-":
            saldo -= kwota

    print(saldo)

zadanie13b()