#zadanie 1
liczba=int(input("Podaj cyfrę:"))

if liczba %2==0:
    print("Twoja liczba jest parzysta")
else:
    print("Twoja liczba jest nieparzysta")
    
#zadanie 2

liczba1=int(input("podaj cyfrę:"))
liczba2=int(input("podaj drugą cyfrę:"))
liczba3=int(input("podaj trzecią liczbę:"))
if liczba1 > liczba2 and liczba1 > liczba3:
    print(liczba1, "jest większe niż pozostałe dwie cyfry")
if liczba2 > liczba1 and liczba2 > liczba3:
    print(liczba2, "jest większe niż pozostałe dwie cyfry")
if liczba3 > liczba1 and liczba3 > liczba2:
    print(liczba3, "jest większe niż pozostałe dwie cyfry")


#zadanie 3
#czy user jest pełnoletni?

wiek =int(input("Ile masz lat?"))
if wiek < 18:
    print("jesteś niepełnoletni")
if wiek >= 18:
    print("Jesteś pełnoletni")

#zadanie 4
temperatura=int(input("Jaka jest aktualnie temperatura na zewnątrz?"))
if temperatura <0:
    print("Temperatura jest poniżej 0")
if temperatura >0:
    print("Temperatura jest powyżej 0")
if temperatura == 0:
    print("Temperatura jest równa 0")

#zadanie 6

ocena=int(input("Wprowadź punkty w skali 1-100:"))
if ocena <=20:
    print("Twoja ocena to 1. Będziesz mieć poprawkę")
if ocena >20 and ocena <=40:
    print("Twoja ocena to 2. Postaraj się następnym razem")
if ocena >40 and ocena <=60:
    print("Twoja ocena to 3. Niedużo zabrakło do lepszej oceny")
if ocena >60 and ocena <=80:
    print("Twoja ocena to 4. Dobry wynik")
if ocena >80 and ocena <=100:
    print("Twoja ocena to 5. Doskonale!")

#zadanie 7
l1=int(input("Podaj pierwszą długość trójkąta: "))
l2=int(input("Podaj drugą długość trójkąta: "))
l3=int(input("Podaj trzecią długość trójkąta: "))
if l1==l2 and l2==l3:
    print("Ten trójkąt jest równoboczny")
if l1==l2 or l1==l3 or l2==l3 and l1>l2 or l1<l2 or l1>l3 or l1<l3:
    print("Ten trójkąt jest równoramienny")
if l1<l2 or l1>l2 or l1<l3 or l1>l3 and l2<l3 or l2>l3:
    print("Ten trójkąt jest różnoboczny")

#zadanie 8

dzien=int(input("Podaj cyfrę od 1 do 7: "))
if dzien ==1:
    print("Poniedziałek")
if dzien ==2:
    print("Wtorek")
if dzien ==3:
    print("Środa")
if dzien ==4:
    print("Czwartek")
if dzien ==5:
    print("Piątek")
if dzien ==6:
    print("Sobota")
if dzien ==7:
    print("Niedziela")
if dzien >7:
    print("Miałeś podać zakres do liczby 7")
if dzien <=0:
    print("Miałeś podać zakres od liczby 1 do 7")

#zadanie 9

miesiac=int(input("Podaj cyfrę od 1 do 12: "))
if miesiac ==1:
    print("Styczeń")
if miesiac ==2:
    print("Luty")
if miesiac ==3:
    print("Marzec")
if miesiac ==4:
    print("Kwiecień")
if miesiac ==5:
    print("Maj")
if miesiac ==6:
    print("Czerwiec")
if miesiac ==7:
    print("Lipiec")
if miesiac ==8:
    print("Sierpień")
if miesiac ==9:
    print("Wrzesień")
if miesiac ==10:
    print("Październik")
if miesiac ==11:
    print("Listopad")
if miesiac ==12:
    print("Grudzień")
if miesiac >12:
    print("Miałeś podać zakres do liczby 12")
if miesiac <=0:
    print("Miałeś podać zakres od liczby 1 do 12")
    



    

