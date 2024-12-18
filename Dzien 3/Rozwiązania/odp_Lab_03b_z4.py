"""
Przykładowa relizacja:
Zadanie 4  z Laboratorium 03b
"""
from os import system
system('cls')

liczby = [12, 45, 2, 10, 78, 5, 11]
liczba = int(input("Podaj liczbę: "))
for x in liczby:
    if x > liczba:
        print(x)
