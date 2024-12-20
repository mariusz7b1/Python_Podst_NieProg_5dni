import sys

# wypisuje ścieżki 'sys.path' to lista
print("scieżki ....")
print(type(sys.path))
for p in sys.path:
    print(p)
