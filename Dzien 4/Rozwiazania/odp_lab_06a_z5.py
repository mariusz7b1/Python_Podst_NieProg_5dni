import random


def wylosuj_slowo(lista_slow):
    if lista_slow:
        return random.choice(lista_slow)
    else:
        return "Lista słów jest pusta"


# Przykładowe użycie funkcji
lista_slow = ["jabłko", "banan", "gruszka", "śliwka", "mango"]
wylosowane_slowo = wylosuj_slowo(lista_slow)
print("Wylosowane słowo:", wylosowane_slowo)
