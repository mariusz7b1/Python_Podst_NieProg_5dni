"""
Przykładowa relizacja:
Zadanie 5 Laboratorium 03b
"""
from os import system
system('cls')

liczby = []
while True:
    liczba = input("Podaj liczbę (lub 'k' aby zakończyć): ")
    if liczba == 'k':
        break
    else:
        if liczba.isdigit():
            liczby.append(int(liczba))
        else:
            print("! zignorowałem !")
liczby.sort()
print(liczby)
