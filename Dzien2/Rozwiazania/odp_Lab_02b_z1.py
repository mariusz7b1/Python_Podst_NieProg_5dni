"""
Lista 02b Zadanie   1
"""
from os import system
system('cls')

# zadanie 1C
for ch in "mariusz.kowalski@organizacja.com.pl":
    if ch == "@":
        break
    print(ch, end="")


# zadanie 1E
print()
for x in range(2, 21):
    if x % 2 == 0:
        print(x, end=" ")

print()
for x in range(19, 0, -1):
    if x % 2 == 1:
        print(x, end=" ")

print()
for x in range(1, 11):
    print(x * x, end=" ")

# zadanie 1F
print()
n = int(input("podaj n "))
m = int(input("podaj m "))
for x in range(n, m + 1):
    print(x, end=" ")


# zadanie 1G
print()
n = int(input("podaj n "))
suma = 0
for i in range(1, n + 1):
    suma = suma + i
print(suma)
