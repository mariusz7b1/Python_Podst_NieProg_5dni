"""" To jest rozwiazanie """
# importowanie modułow
import sys
from os import system


def get_miasto(adres):
    """"
    Wycina z adresu miasto korzrzystajac z tego ze po przecinku
    zawsze jest kod o stałej dlugości
    Args:
        adres
    Returns:
        miasto
    """
    lst_adres = adres.split(",")
    miasto = lst_adres[1]
    miasto = miasto[7:]

    return miasto


def get_mail(mail):
    """"
    Wycina z adresu @ dostawce,
    używa split traktujac jako separator znaczek @

    Args:
        adres mail
    Returns:
        dostawca
    """
    return mail.split("@")[1]


def get_data_fromfile(pelna_nazwa_pliku):
    """ pobiera dane z liku zwraca listę ktorej elementami jest słownik"""
    try:
        f_in = open(pelna_nazwa_pliku, 'rt', encoding='utf-8')
    except IOError:
        print('Brak pliku z danymi zrodłowymi')
        sys.exit()

    dane = []
    linia = f_in.readline()
    # traktuję pierwszą linię jako wzorcową jeśli chodzi o ilość danych
    # rozdzielonych separatorem, jesli trafi się jakaś linia o innej dlugości
    # bedzie ignorowana
    dane_linia = linia.split(";")
    ilosc_danych = len(dane_linia)

    while linia != '':
        linia = linia.strip()
        dane_linia = linia.split(";")
        if len(dane_linia) == ilosc_danych:  # tylko wlasciwe linie
            imie = dane_linia[0]
            nazwisko = dane_linia[1]
            miasto = get_miasto(dane_linia[4])
            dostawca_mail = get_mail(dane_linia[8])
            # Tworzenie słownika i dodanie do tablicy
            dane.append({"imie": imie,
                        "nazwisko": nazwisko,
                         "miasto": miasto,
                         "dostawca_mail": dostawca_mail})

        linia = f_in.readline()

    f_in.close()
    return dane

# zwraca słownik wystapienia danej wartosci wraz z ilością wystąpien


def get_dic_unique_data(dane, pole):
    slownik = {}
    for ele in dane:
        war = ele[pole]
        if war not in slownik:
            slownik[war] = 1
        else:
            slownik[war] += 1
    return slownik

# zwraca liste z najbardziej popoularna wartoscia
# jesli parametr minmax > 0 to najmniej popularna wartosć


def get_most_popolar(slownik, minmax=0):
    if minmax == 0:
        wartosc = max(slownik.values())
    else:
        wartosc = min(slownik.values())

    lst = []
    for klucz in slownik.keys():
        if slownik[klucz] == wartosc:
            lst.append({klucz: slownik[klucz]})
    return lst

# zwraca ilość wystapien danej wartości


def count_var_in_dic(slownik, var):

    if var in slownik.keys():
        return slownik[var]
    return 0


# czyszczenie ekranu
system("cls")

nazwa_pliku = "dane_10K.txt"
sciezka_do_pliku = "d:\\dane\\"
# pełna nazwa pliku wraz ze scieżką
plik = sciezka_do_pliku + nazwa_pliku

# pobranie danych do tablicy
lst_dane = get_data_fromfile(plik)

# utworzenie slownika z imionami i czestością ich
dic_imion = get_dic_unique_data(lst_dane, 'imie')
dic_nazwisk = get_dic_unique_data(lst_dane, 'nazwisko')
dic_miasto = get_dic_unique_data(lst_dane, 'miasto')
dic_mail = get_dic_unique_data(lst_dane, 'dostawca_mail')

print("Liczba różnych imion to  ", len(dic_imion))
print("Liczba różnych nazwisk to", len(dic_nazwisk))
print("Liczba różnych miast   to", len(dic_miasto))
print("Liczba różnych dostawców @ to", len(dic_mail))


polularne_imie = get_most_popolar(dic_imion)
polularne_nazwisko = get_most_popolar(dic_nazwisk)
polularne_miasto = get_most_popolar(dic_miasto)

print("najbardziej popularne imie/imiona to:", polularne_imie)
print("najbardziej popularne nazwisko/nazwiska to:", polularne_nazwisko)
print("najbardziej popularne miasto/miasta to:", polularne_miasto)


polularne_imie = get_most_popolar(dic_imion, 1)
polularne_miasto = get_most_popolar(dic_miasto, 1)

print("najmniej popularne imie/imiona to:", polularne_imie)
print("najmniej popularne miasto/miasta to:", polularne_miasto)

print(f"w Opolu mieszka {count_var_in_dic(dic_miasto, "Opole")}")
