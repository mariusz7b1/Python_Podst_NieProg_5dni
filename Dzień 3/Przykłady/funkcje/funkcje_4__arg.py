"""
Funkcje - tuple argumentów
"""
from os import system
system('cls')


def pokaz_arumenty(*args):
    print(type(args))
    print(f"Przekazano {len(args)} argumentów")
    for war in args:
        print(war, end=",")
    print()
    # koniec funkcji


pass
pokaz_arumenty("ala", 1, 2.7, "ma", 88, 2.5)
pokaz_arumenty("mariusz", 7)
print()
lst1 = [1, 2, 3]
pokaz_arumenty(lst1)
pokaz_arumenty(*lst1)
