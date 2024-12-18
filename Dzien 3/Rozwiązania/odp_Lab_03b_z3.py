"""
Przykładowa relizacja:
Zadanie 3 z Laboratorium 03b
"""
from os import system
system('cls')

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()
