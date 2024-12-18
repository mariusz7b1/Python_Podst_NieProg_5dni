"""
Przykładowa relizacja:
Zadanie 1  i 2 z Laboratorium 03b
"""
from os import system
system('cls')

# Zadanie 1
s1 = "Ala ma kota"
lst1 = list(s1)
print(lst1)

for i in range(len(lst1)):
    print(lst1[i], end=" ", sep='')
print()

for ele in lst1:
    print(ele, end=" ", sep='')
print()
print(f"litera 'a' wystapia w ciagu {lst1.count('a')} razy")

# Zadanie 2
s1 = input("Podaj zdanie ")
litera = input("Podaj literę ")
print(f"litera {litera} wystapia w ciagu {s1.count(litera)} razy")


# modyfikacja case insensitive
# zapis jednolinikjkoy
print(f"litera {litera.lower()} wystapia w ciagu \
      {(list(s1.lower())).count(litera.lower())} razy")

# robite na 3 linijki :)
s1 = s1.lower()
litera = litera.lower()
print(f"litera {litera} wystapia w ciagu {(list(s1)). count(litera)} razy")
