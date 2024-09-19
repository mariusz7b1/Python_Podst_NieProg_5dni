import math


def pierwiastek(liczba, stopien_pierwiastka=2):
    if liczba < 0:
        raise ValueError("Nie można obliczyć pierwiastka z liczby ujemnej")
    else:
        return math.pow(liczba, 1 / stopien_pierwiastka)


# Przykładowe użycie funkcji
try:
    liczba = float(input("Podaj liczbę: "))
    stopien = int(input("Podaj stopień pierwiastka (domyślnie 2): "))
    wynik = pierwiastek(liczba, stopien)
    print("Pierwiastek", stopien, "stopnia z liczby", liczba, "to:", wynik)
except ValueError as e:
    print(e)
