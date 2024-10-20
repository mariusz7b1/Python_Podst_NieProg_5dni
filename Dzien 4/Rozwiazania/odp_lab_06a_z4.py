import os


def rozmiar_pliku(sciezka_do_pliku):
    if os.path.exists(sciezka_do_pliku):
        rozmiar = os.path.getsize(sciezka_do_pliku)
        return rozmiar
    else:
        return "Plik nie istnieje"


# Przykładowe użycie funkcji
sciezka = "E:\\dzien3.zip"
print("Rozmiar pliku:", rozmiar_pliku(sciezka), "bajtów")
