
from os import system
system("cls")

pol_ang = {
    "kwiat": "flower",
    "woda": "water",
    "gleba": "soil",
    "drzewo": "tree",
    "trawa": "grass"
}


# petla 1
print("")
for zm1, zm2 in pol_ang.items():
    print(f"{zm1}  -> {zm2}")
