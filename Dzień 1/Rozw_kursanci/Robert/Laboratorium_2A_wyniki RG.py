print("Zadanie 1")
liczba = int(input("Podaj liczbę: "))
if liczba %2 == 0:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

print()
print("Zadanie 2")
a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
c = int(input("Podaj liczbę c: "))
print("największa to: " + str(max(a,b,c)))
if b<a>c:
    print("liczba a jest największa")
elif a<b>c:
    print("liczba b jest największa")
elif a<c>b:
    print("liczba b jest największa")

print()
print("Zadanie 3")
wiek = int(input("Podaj swój wiek: "))
if wiek >=18:
    print("Jesteś pełnoletni");
else:
    print("Jesteś niepełnoletni");

print()
print("Zadanie 4")
temp = float(input("Podaj temperaturę: "))
if temp == 0.0:
    print("Temperatura równa zero")
elif temp < 0:
    print("Temperatura mniejsza od zera")
else:
    print("Temperatura wyższa od zera")



print()
print("Zadanie 5")
rok = int(input("Podaj rok "))
if rok % 4 == 0:
    print("Rok przestępny")
else:
    print("Rok nieprzestępny")

print()
print("Zadanie 6")
punkty = int(input("Podaj liczę punktów: "))
if 85 <= punkty <= 100:
    print("Ocena 5") 
elif 70 <= punkty < 85:
    print("Ocena 4")
elif 55 <= punkty < 70:
    print("Ocena 3")
elif 40 <= punkty < 55:
    print("Ocena 2")
else:
    print("Test nie zaliczony")

print()
print("Zadanie 7")
a = int(input("Podaj bok a: "))
b = int(input("Podaj bok b: "))
c = int(input("Podaj bok c: "))
if a==b==c:
    print("Trójkąt równoboczny")
elif a==b or a==c or c==b:
    print("Trójkąt równoramienny")
else:
    print("Trójkąt różnoboczny")

print()
print("Zadanie 8")
try :
    tydzien = int(input("Podaj numer dnia tygodnia od 1-7: "))
    match tydzien:
        case 1:
            print("Poniedziałek")
        case 2:
            print("Wtorek")
        case 3:
            print("Środa")
        case 4:
            print("Czwartek")
        case 5:
            print("Piątek")
        case 6:
            print("Sobota")
        case 7:
            print("Niedziela")
        case _:
            print("Błędny numer tygodnia")
except:
    print("Błąd danych")

print()
print("Zadanie 9")
try :
    miesiac = int(input("Podaj numer miesiąca od 1-12: "))
    match miesiac:
        case 1:
            print("Styczeń")
        case 2:
            print("Luty")
        case 3:
            print("Marzec")
        case 4:
            print("Kwiecień")
        case 5:
            print("Maj")
        case 6:
            print("Czerwiec")
        case 7:
            print("Lipiec")
        case 8:
            print("Sierpień")
        case 9:
            print("Wrzesień")
        case 10:
            print("Październik")
        case 11:
            print("Listopad")
        case 12:
            print("Grudzień")
        case _:
            print("Błędny numer miesiąca")
except:
    print("Błąd danych")

