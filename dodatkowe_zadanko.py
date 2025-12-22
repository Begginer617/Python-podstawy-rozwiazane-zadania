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

# petle

# for i in range(2):
#     input( f"{i} + podaj imie: "" ")

# for i in range(2):
#         print("a")

# for i in range(5):
#         print("a")
#
# for i in range(3,10): #print bedzie od 3 do 9 bo 0 tez liczy
#         print("a")
#
# for i in range(3,11): #print bedzie od 3 do 10 bo 11 nie wskoczy
#         print("a")
#
# for i in range(1,1): #pusty przedział
#         print("a")


# listy

# dane = ["a", "b", 23, "vd4", "sd", "ee", "ff", "gg", "hh"]
#
# for index, value in enumerate(dane):
#     print(index, value)
#     dane.pop(1)       pop usuwa po indeksie
#     print(dane)


# dane = ["a", "b", 23, "vd4", "sd", "ee", "ff", "gg", "hh", "23"]
#
# for index, value in enumerate(dane):
#     print(index, value)
#     remove.("23")       pop usuwa po wartosci. Ale usuwa 1 napotkana wartosc.
#     print(dane)

# #enumerate(dane) „zapamiętuje” sobie kolejne elementy listy w momencie startu pętli.
# Ty w środku pętli modyfikujesz tę samą listę, więc to, co widzisz na ekranie, jest mieszanką:
# - index, value – idzie po oryginalnej kolejności,
# - print(dane) – pokazuje listę już po usunięciu elementu.
# Przejdźmy to krok po kroku.


# Kopiowanie listy ;)
# a = [1, 2, 3]
# b = a[:]   # kopia
#
# b.append(4)
#
# print(a)  # [1, 2, 3]
# print(b)  # [1, 2, 3, 4]
# a się nie zmieniło — bo b to kopia.

# Kiedy tego używać?
# Gdy chcesz:
# - iterować po kopii listy, a modyfikować oryginał
# - zrobić płytką kopię listy
# - uniknąć błędów typu „modyfikuję listę podczas pętli”
#
# ✅ Uwaga: to jest płytka kopia
# Jeśli lista zawiera listy, to one nie są kopiowane głęboko.


# ista z wykorzystaniem instrukcji warunkowej IF
# dane = ["a", "b", 23, "vd4", "sd", "ee", "ff", "gg", "hh", "23"]
#
# if ("23" in dane):
#     print("jest")
# else:
#     print("ni ma")


# KROTKA sa niemodyfkowalne.

# nawiasy kdwadratowr sa dla list.
# nawiasy okragłe sa dla krotek.

# Krotka (tuple) w Pythonie to uporządkowana, niemodyfikowalna (niezmienna) kolekcja elementów,
# podobna do listy, ale po utworzeniu jej
# zawartości nie da się zmieniać, co czyni ją idealną do stałych danych,

# tuple = ("ania", 12, "kasia")
# print(tuple)
#
# for i, value in enumerate(tuple):
#     print(i, value)


# SŁOWNIKI (dict)
# https://www.algorytm.edu.pl/slowniki-w-python

# lista = [1, 2, 3] # tworzymy listę
# print(lista[0], lista[1], lista[2]) # wypisujemy elementy listy odwołując się poprzez indeksy: 0, 1 i 2.

# Tworzenie, dodawanie i wypisywanie elementów słownika

# slownik = {} # utworzenie słownika
#
# # utworzenie trzech elementów słownika

# slownik["adam"] = 3 # klucz: adam, wartość: 3
# slownik["iwona"] = 3.2
# slownik[122] = "monika" # klucz: 122, wartość: monika
#
# # wypisanie całego słownika
# print(slownik) # {'adam': 3, 'iwona': 3.2, 122: 'monika'}
#
# # wypisanie kluczy i wartości
# for klucz, wartosc in slownik.items():
#     print(klucz, wartosc)
# """
# adam 3
# iwona 3.2
# 122 monika
# """
#
# # wypisanie samych klucz
# for klucz in slownik:
#     print(klucz)
# """
# adam
# iwona
# 122
# """
#
# #wypisanie samych wartości
# for wartosc in slownik.values():
#     print(wartosc)
# """
# 3
# 3.2
# monika
# """

# drugi sposob inicjacji wartosci słownika

# tworznie słownika wraz z wpisaniem trzech elementów
# slownik = {"adam": 3, "iwona":3.2, 122: "monika"}
#
# print(slownik["adam"]) # 3
# print(slownik[122]) # monika
# # print(slownik["ala ma kota"]) błąd, taki klucz nie istnieje

# Sortowanie elementów słownika po kluczu
# Domyślnie elementy słownika nie są sortowane, jak to czasami bywa w tablicach asocjacyjnych w innych językach. Aby uporządkować elementy słownika należy użyć funkcji sorted, która zwróci posortowaną listę krotek zawierających pary klucz-wartość:
#
# # tworznie słownika wraz z wpisaniem trzech elementów
# slownik = {"kamil": 3, "iwona":3.2, "andrzej": 2}
#
# #sortowanie elementów słownika po kluczu
# posortowany_slownik = sorted(slownik.items())
#
# print(posortowany_slownik) # [('andrzej', 2), ('iwona', 3.2), ('kamil', 3)]
# Sortowanie elementów słownika po wartości
# Aby posortować elementy słownika według wartości, możesz użyć funkcji sorted() w połączeniu z parametrem key, który określa funkcję klucza sortującego. Możesz użyć key=lambda x: x[1], aby sortować po drugim elemencie (wartości) w parach klucz-wartość.
#
# # tworznie słownika wraz z wpisaniem trzech elementów
# slownik = {"kamil": 3, "iwona":3.2, "andrzej": 2}
#
# #sortowanie elementów po wartości
# posortowany_slownik = sorted(slownik.items(), key=lambda x: x[1])
#
# print(posortowany_slownik) # [('andrzej', 2), ('kamil', 3), ('iwona', 3.2)]


#  { } — słowniki (dict) i zbiory (set)
# - Najczęściej: słowniki, czyli pary klucz–wartość

# {"imie": "Milosz", "wiek": 25}

# - Mogą też oznaczać zbiory, ale tylko jeśli nie ma par klucz–wartość:
# {1, 2, 3}
# - Uwaga: pusty {} to zawsze słownik, nie zbiór.
# Pusty zbiór robisz tak:
# set()
#
#
#
# 🔸 ( ) — krotki (tuple)
# - Krotka to niezmienna sekwencja wartości:
# (1, 2, 3)
# - Ciekawostka: krotka jednoelementowa musi mieć przecinek:
# (5,)   # to tuple
# (5)    # to tylko liczba 5
#
#
#
# 🔸 [ ] — listy (list)
# - Listy to sekwencje, które można modyfikować:
# [1, 2, 3]
# - Najczęściej używany typ kolekcji w Pythonie.
#
# Podsumowanie w tabeli

# { } dict/set {"a": 1}{1, 2, 3}
# ( ) tuple (1, 2, 3) |
# [ ] list [1, 2, 3] |
# #
#
#
# Jeśli chcesz, mogę Ci też pokazać różnice między listą, krotką i zbiorem w praktyce — np. co jest szybsze, co się do czego nadaje.


# Czy słownik może mieć „więcej wartości w kluczu”?
# Nie, jeden klucz może mieć tylko jedną wartość przypisaną bezpośrednio.
# Ale…
# Ta jedna wartość może być czymkolwiek — listą, krotką, słownikiem, zbiorem, obiektem.
# Czyli możesz „opakować” wiele wartości w jedną strukturę.


