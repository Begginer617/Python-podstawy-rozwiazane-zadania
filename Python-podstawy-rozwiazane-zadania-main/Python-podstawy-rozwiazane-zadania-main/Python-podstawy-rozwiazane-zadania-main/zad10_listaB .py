# Zadanie 10
# Napisz program fitness obliczający BMI


twoj_wiek = int(input("Podaj swój wiek: "))
twoja_waga = float(input("Podaj swoją wagę w kg: "))
twoj_wzrost = float(input("Podaj swój wzrost w cm: "))

# konwersja wzrostu na metry
wzrost_m = twoj_wzrost / 100

# obliczenie BMI
bmi = twoja_waga / (wzrost_m ** 2)

print("Twoje BMI wynosi:", round(bmi, 2))

# interpretacja BMI
if bmi < 18.5:
    print("Kategoria: Niedowaga")
elif 18.5 <= bmi < 25:
    print("Kategoria: Prawidłowa waga")
elif 25 <= bmi < 30:
    print("Kategoria: Nadwaga")
else:
    print("Kategoria: Otyłość")