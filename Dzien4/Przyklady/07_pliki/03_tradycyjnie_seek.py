"""
pliki - tradycyjna obsługa otwórz zamknij
"""
# przykald z seek zdecydowanie dokonczyc
from os import system

system("cls")

# odczyt z pliku

in_file_name = "testowy.txt"
out_file_name = "slowa_z_pliku.txt"
file_path = "d:\\dane\\"

try:
    # otwarcie pliku do odczytu
    f_in = open(file_path+in_file_name, "rt", encoding="utf-8")
except IOError:
    print("Nie udało się otworzyć pliku do odczytu")
    exit()

try:
    # otwarcie pliku do zapisu
    f_out = open(file_path+out_file_name, "wt", encoding="utf-8")
except IOError:
    print("Nie udało się otworzyć pliku do zapisu")
    f_in.close()  # nie jest to konieczne
    exit()

ilosc_lini = 1
while True:
    # odczyt za posrednictewm readline
    linia = f_in.readline()

    ilosc_lini += 1
    if ilosc_lini == 3:
        f_in.seek(2)   # przesuwa na pozcyje bajty

    if len(linia) == 0:
        break
    else:
        # przykład
        tab_slow = linia.split()
        for slowo in tab_slow:
            # zapis za posrednictwem write
            f_out.write(slowo+"\n")

f_in.close()
f_out.close()
