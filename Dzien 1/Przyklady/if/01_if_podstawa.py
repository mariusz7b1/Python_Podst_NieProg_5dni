"""
Przykład if - podstawowy
"""
# czyszczenie ekranu
from os import system
system('cls')


x = 15
if x > 10:			    # warunek jest True
    print("x > 10")
    print("jestem w instrukcji if")

print("a teraz juz za if ")


text = input("Podaj tekst: ")
if len(text) > 10:  # len – funkcja sprawdzająca długość….
    print(len(text))
    print("Napis jest dłuższy niż 10 znaków.")

x = 5
if x > 10: 			# False
    print("x > 10")
else:               # w przeciwnym wypadku
    print(x, " jest mniejsze od 10")


print("koniec :):)")
