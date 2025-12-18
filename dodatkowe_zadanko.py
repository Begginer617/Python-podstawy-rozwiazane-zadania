# # def cwiczenie1():  # TEGO NIE ZMIENIAJ, TO MUSI BYĆ NA SAMEJ GÓRZE
# #
# #     # TU ROZPOCZNIJ KODOWAĆ
# #     # Samochód na 100 km spala 8 l paliwa.
# #     # Ile spali paliwa po przejechaniu 488 km ?
# #
# #     dystans_do_zrobienia = 488
# #     zuzycie_paliwa_na_100 = 8
# #     dystans_100km = 100
# #
# #     wynik = (dystans_do_zrobienia * zuzycie_paliwa_na_100) / dystans_100km
# #
# #     return round(wynik, 2)  # TEGO NIE ZMIENIAJ, TO MUSI BYĆ NA SAMYM DOLE
# # print(cwiczenie1())
# #
# #
# # def cwiczenie2():  # TEGO NIE ZMIENIAJ, TO MUSI BYĆ NA SAMEJ GÓRZE
# #
# #     bok_figury_geom = 5
# #     a, b, c = 5, 4, 4  # suma = 13
# #
# #     # Pole kwadratu
# #     poleKwadratu = bok_figury_geom ** 2
# #
# #     # Obwód trójkąta
# #     obwodTrojkata = a + b + c
# #
# #     # Pole koła: π = 3.14, promień = 3
# #     pi = 3.14
# #     promien = 3
# #     poleKola = pi * (promien ** 2)
# #
# #     # Pole trójkąta: (podstawa * wysokość) / 2 -> 5 * 21 / 2 = 52.5
# #     podstawa = bok_figury_geom
# #     wysokosc = 21
# #     poleTrojkata = (podstawa * wysokosc) / 2
# #
# #     return (round(poleKwadratu, 2),
# #             round(obwodTrojkata, 2),
# #             round(poleKola, 2),
# #             round(poleTrojkata, 2))
# # print(cwiczenie2())
# #
# #
# # def cwiczenie3():  # TEGO NIE ZMIENIAJ, TO MUSI BYĆ NA SAMEJ GÓRZE
# #
# #     # TU ROZPOCZNIJ KODOWAĆ
# #
# #     cena_chleb = float(1.99)
# #     cena_mleka = float(2.50)
# #     cena_sok = float(6.45)
# #     cena_cukierkow = float(10.25)
# #
# #     # Zamówienie to:
# #
# #     #     5 szt. chleba
# #     #     0.5 l. mleka
# #     #     7 l. soku
# #     #     5 kg. cukierków
# #
# #     zamowienie_chleb = cena_chleb * 5
# #     zamowienie_mleka = cena_mleka * 0.5
# #     zamowienie_soku = cena_sok * 7
# #     zamowienie_cukierkow = cena_cukierkow * 5
# #
# #     wynik = zamowienie_cukierkow + zamowienie_soku + zamowienie_chleb + zamowienie_mleka
# #
# #     return round(wynik, 2)  # TEGO NIE ZMIENIAJ, TO MUSI BYĆ NA SAMYM DOLE
# # print(cwiczenie3())
#
#
# # def cwiczenie4():  # TEGO NIE ZMIENIAJ, TO MUSI BYĆ NA SAMEJ GÓRZE
# #
# #     # TU ROZPOCZNIJ KODOWAĆ
# #
# #     a = float(input("Podaj pierwszą liczbę: "))
# #     print(a)
# #     b = float(input("Podaj drugą liczbę: "))
# #     print(b)
# #     c = float(input("Podaj trzecią liczbę: "))
# #     print(c)
# #     d = float(input("Podaj czwartą liczbę: "))
# #     print(d)
# #     e = float(input("Podaj piątą liczbę: "))
# #     print(e)
# #
# #     insturkcja = [a, b, c, d, e]
# #     print(insturkcja)
# #
# #     srednia = sum(insturkcja) / len(insturkcja)
# #     print("srednia to:" , srednia)
# #     wynik = srednia
# #     print(wynik)
# #     return round(wynik, 2)  # TEGO NIE ZMIENIAJ, TO MUSI BYĆ NA SAMYM DOLE
# #
# # cwiczenie4()
# # print(cwiczenie4())
#
#
# # def cwiczenie5():  # TEGO NIE ZMIENIAJ, TO MUSI BYĆ NA SAMEJ GÓRZE
# #
# #     # TU ROZPOCZNIJ KODOWAĆ
# #
# #     liczba_usera = int(input("podaj liczbe do spotegowania"))
# #     potega = int(input("Do jakiej potęgi chcesz ją podnieść? "))
# #
# #     print(liczba_usera)
# #     print(potega)
# #
# #     wynik = (liczba_usera ** potega)
# #
# #     return wynik  # TEGO NIE ZMIENIAJ, TO MUSI BYĆ NA SAMYM DOLE
# #     print5(cwiczenie)
#
# # def cwiczenie6():  # TEGO NIE ZMIENIAJ, TO MUSI BYĆ NA SAMEJ GÓRZE
# #
# #     # TU ROZPOCZNIJ KODOWAĆ
# #
# #     pierwsza_liczba = int(input("Podaj pierwszą liczbę: "))
# #     druga_liczba = int(input("Podaj drugą liczbę: "))
# #
# #     if pierwsza_liczba > druga_liczba:
# #         print("liczba pierwsza jest wieksza")
# #         wynik = pierwsza_liczba
# #     elif druga_liczba > pierwsza_liczba:
# #         print(" liczba druga jest wieksza")
# #         wynik = druga_liczba
# #
# #     print(wynik)
# #
# #     return wynik  # TEGO NIE ZMIENIAJ, TO MUSI BYĆ NA SAMYM DOLE
#
#
# # def cwiczenie7():
# #     podaj_liczbe = int(input("Podaj liczbę: "))
# #     if podaj_liczbe % 2 == 0:
# #         wynik = "parzysta"
# #         print(wynik)
# #     else:
# #         wynik = "nieparzysta"
# #         print(wynik)
# #     return wynik  # TEGO NIE ZMIENIAJ, TO MUSI BYĆ NA SAMYM DOLE
# #
# # print("Zwrócone:", cwiczenie7())
#
#
#
# # def cwiczenie8():
# #     podaj_wiek = int(input("Podaj swój wiek: "))
# #
# #     if podaj_wiek > 0 and podaj_wiek < 10:
# #         wynik = "dziecko"
# #     elif podaj_wiek >= 10 and podaj_wiek < 18:
# #         wynik = "młodzież"
# #     elif podaj_wiek >= 18:
# #         wynik = "osoba dorosła"
# #     else:
# #         wynik = "niepoprawny wiek"
# #
# #     return wynik
# #
# # print("Zwrócone:", cwiczenie8())
#
#
# def cwiczenie():  # TEGO NIE ZMIENIAJ, TO MUSI BYĆ NA SAMEJ GÓRZE
#
#     # TU ROZPOCZNIJ KODOWAĆ
#     try:
#         podaj_1_liczbe = int(input("Podaj 1 liczbe: "))
#         podaj_2_liczbe = int(input("Podaj 2 liczbe: "))
#     except ValueError:
#         print("To nie jest liczba całkowita!")
#         return "błędna"
#
#     poprawny_iloczyn = podaj_1_liczbe * podaj_2_liczbe
#
#     try:
#         odpowiedz = int(input(f"Jaki jest iloczyn {podaj_1_liczbe} * {podaj_2_liczbe}? "))
#     except ValueError:
#         print("To nie jest liczba całkowita!")
#         return "błędna"
#
#     if odpowiedz == poprawny_iloczyn:
#         wynik = "poprawna"
#     else:
#         wynik = "błędna"
#
#     return wynik  # TEGO NIE ZMIENIAJ, TO MUSI BYĆ NA SAMYM DOLE
from itertools import count

#petle

# for i in range(2):
#     input( f"{i} + podaj imie: "" ")

# for i in range(2):
#         print("a")

for i in range(5):
        print("a")

for i in range(3,10): #print bedzie od 3 do 9 bo 0 tez liczy
        print("a")


for i in range(1,1): #pusty przedział
        print("a")

