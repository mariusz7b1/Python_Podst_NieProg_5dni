"""
Przykład if - zagnieżdzony 01
"""
from os import system
system('cls')


wiek = int(input("Podaj swoj wiek ? "))
if wiek >= 18:
    print("jestes pelnoletni")
    print("do 100 lat zostało ci ", 100 - wiek)
elif wiek == 18:     # blad logiczny - nigdy sie nie wykona
    print("18 latek Witaj wsrod dorosłych !!!")
else:
    print("dzieciak")
