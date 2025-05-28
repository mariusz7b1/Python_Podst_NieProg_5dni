import os
os.system("cls")
while True:
    try:
        x = int(input("Wprowadź liczbę: "))
        y = 1 / x
        print(y)
    except ZeroDivisionError:
        print("Nie możesz dzielić przez zero.")
    except ValueError:
        print("Musisz wpisać wartość całkowitą.")
    except KeyboardInterrupt:
        print("Zostało nacisniete Ctrl C")
    except Exception as zmienna:
        print("Pojawił się bład ", zmienna)
    else:
        break

print("KONIEC.")
