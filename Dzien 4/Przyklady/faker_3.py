"""
# pip install faker
Przykładowe wykorzystanie modułu Faker
"""
from faker import Faker


WYBOR = 3
kod_kraju = ("pl_PL", "de_DE", "en_US", "ES_Es")

fake = Faker(kod_kraju[WYBOR])
for i in range(10):
    imie = fake.first_name()
    nazwisko = fake.last_name()
    miasto = fake.city()
    print(f"{imie} {nazwisko} mieszka w {miasto}")
