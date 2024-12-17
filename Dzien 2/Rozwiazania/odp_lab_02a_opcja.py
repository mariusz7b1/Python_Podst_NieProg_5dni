"""
Wylicznie czasu do przepełnienia zbiornika retencyjnego
Przykład realizowany dla zbiornika Turawa
Sugestia modyfikacji, można podawać procent napełnienia zbiornika i ewentualnie 
zabezpieczyć program przed podawaniem błednych danych 
"""
# Stała pojemność zbiornika np. Turawa (w m³)
POJEMNOSC_ZBIORNIKA = 108_000_000

# Pobranie danych od użytkownika
stan_napelnienia = int(
    input("Podaj aktualny stan napełnienia zbiornika (w mln m³): "))

stan_napelnienia = stan_napelnienia * 1_000_000

# Instrukcja sprawdzająca poprawność stanu napełnienia
if stan_napelnienia > POJEMNOSC_ZBIORNIKA:
    print(f"Aktualny stan nie może być większy niż {POJEMNOSC_ZBIORNIKA} m³.")
elif stan_napelnienia < 0:
    print("Aktualny stan nie może być mniejszy niż 0.")
else:
    wplyw = int(input("Podaj wpływ (m³/s): "))
    wyplyw = int(input("Podaj wypływ (m³/s): "))
    # Sprawdzenie, czy wpływ jest większy od wypływu
    if wplyw <= wyplyw:
        print("Zbiornik nie zostanie przepełniony, ponieważ wpływ nie jest większy niż wypływ.")
    else:
        # Obliczenie różnicy przepływów
        przeplyw_netto = wplyw - wyplyw

        # Obliczenie pozostałej pojemności zbiornika
        pozostala_pojemnosc = POJEMNOSC_ZBIORNIKA - stan_napelnienia

        # Obliczenie czasu do przepełnienia w sekundach
        czas_sekundy = pozostala_pojemnosc / przeplyw_netto

        # Konwersja czasu na godziny
        czas_godziny = czas_sekundy / 3600

        print(f"Zbiornik przepełni się za {czas_godziny:.1f} godzin.")
