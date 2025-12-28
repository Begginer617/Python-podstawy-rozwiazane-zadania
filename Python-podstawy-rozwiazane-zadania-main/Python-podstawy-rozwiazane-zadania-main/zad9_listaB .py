# Zadanie 9
# Napisz program konwertujący wysokość podaną w stopach i calach na
# centymetry

# 1 stopa = 30.48 cm
# 1 cal = 2.54 cm

def zadanie9b():
    print("Co chcesz podać?")
    print("1 - Stopy")
    print("2 - Cale")

    choice = input("Wybierz 1 lub 2: ")

    if choice == "1":
        feet = float(input("Podaj liczbę stóp: "))
        result_cm = feet * 30.48
        print(f"{feet} stóp = {result_cm} cm")

    elif choice == "2":
        inches = float(input("Podaj liczbę cali: "))
        result_cm = inches * 2.54
        print(f"{inches} cali = {result_cm} cm")

    else:
        print("Niepoprawny wybór!")

zadanie9b()