"""
Przykład while podstawowy
"""
# czyszczenie ekranu
from os import system
system('cls')


"""
# petla nieskonczona
counter = 1
while True:
    print("Pętla nieskończona ", counter)
    counter += 1
"""

counter = 5
while counter > 2:
    print(counter)
    counter -= 1   # counter = counter-1

print("zakonczylem dzialania")
