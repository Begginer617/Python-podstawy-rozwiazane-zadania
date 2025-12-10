# Zadanie 6
# Napisz program sprawdzający, czy podane słowo jest palindromem.

def palindrom():
    slowo = input("Podaj słowo: ")
    slowo = slowo.lower()
    reversed_word = slowo[::-1]

    if slowo == reversed_word:
        print("To jest palindrom!")
    else:
        print("To nie jest palindrom.")


palindrom()
