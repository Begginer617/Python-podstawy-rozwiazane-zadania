# Zadanie 7
# Napisz program rysujący histogram (w konsoli) dla podanej listy liczb
# całkowitych

def zadanie7():
    liczby = [3, 7, 1, 4, 9, 2, 5, 3, 8, 6,
              4, 4, 7, 2, 1, 9, 3, 5, 8, 6,
              10, 2, 2, 7, 3, 4, 6, 8, 9, 1]

    # słownik: liczba → liczba powtórzeń
    histogram = {}

    for n in liczby:
        if n in histogram:
            histogram[n] += 1
        else:
            histogram[n] = 1
            print(histogram.keys())

    # sortowanie po kluczu (liczbie)
    for liczba in sorted(histogram.keys()):
        print(liczba, ":", "*" * histogram[liczba])

zadanie7()