a=10
b=3
c=12.1
d=3.3
print(a+b)
print(a+c)
print(a+d)

print(a/b)
print(a*c)
print(a//d)
print(a%b)

print(type(a))
print(type(a+b))
print(type(c+c))
print(type(a%b))

#Zadanie 2
t1 = "tygrys"   #tygrus nie ma żadbego znaku oddzielającego wyraz
t2 = ' zebra'   #zebra ma w ciągu znaków spację

print(t1+t2)
print(t1+t2)
print(t1+t2+t1)
print(3*t1 + 4*t2) #tgrysy zapisywane są bez przerwy, zebry ze spacją

#Zadanie 3
i=input("Podaj i: ")
j=input("Podaj j: ")
print(i)
print(j)
print(i+j)  #zmienne traktowane jako string anie int

i=int(input("podaj i: "))
j=int(input("podaj j: "))
print(i+j)      #zmienne i j traktowane jako integer

#Zadanie 4
kgnalbs = float(2.2)
print(kgnalbs)
waga=float(input("Podaj wage: "))
print(str(waga)+" kg to " + str(waga*kgnalbs) + "lbs") 
print(str(waga)+" lbs to " + str(waga/kgnalbs) + "kg")

#Zadanie 5
x=int(input("Podaj x: "))

y=1/((x+1/(x+1/(x+1/x))))
print(y)
