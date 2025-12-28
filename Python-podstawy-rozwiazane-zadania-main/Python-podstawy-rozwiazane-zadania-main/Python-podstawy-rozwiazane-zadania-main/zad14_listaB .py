# Zadanie 14
# Robot porusza się po płaszczyźnie począwszy od punktu (0,0). Może się
# on poruszać do góry, na dół, w lewo oraz w prawo dla podanej liczby kroków.
# Napisz program obliczający odległość od punktu (0,0) po wykonaniu
# sekwencji kroków podanych z klawiatury. Program powinien zwracać
# liczbę całkowitą (zaokrągloną).
# Przykładowe wejście :
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# (cyfry za kierunkiem oznaczają liczbę kroków)
# Wyjście :
# 2

import math

x = 0
y = 0

while True:
    try:
        line = input().strip()
        if not line:
            break
        direction, steps = line.split()
        steps = int(steps)

        if direction.upper() == "UP":
            y += steps
        elif direction.upper() == "DOWN":
            y -= steps
        elif direction.upper() == "LEFT":
            x -= steps
        elif direction.upper() == "RIGHT":
            x += steps
    except EOFError:
        break

distance = round(math.sqrt(x**2 + y**2))
print(distance)



