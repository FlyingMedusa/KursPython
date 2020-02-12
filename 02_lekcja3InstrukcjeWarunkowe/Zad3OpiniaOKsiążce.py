opi1 = float(input("Użytkowniku nr1 podaj swoją opinię o książce [od 1 do 10]: "))
opi2 = float(input("Użytkowniku nr2 podaj swoją opinię o książce [od 1 do 10]: "))
opi3 = float(input("Użytkowniku nr3 podaj swoją opinię o książce [od 1 do 10]: "))
srednia = (opi1 + opi2 + opi3)/3

if srednia > 7:
    print("Bardzo dobry!")
elif 7 > srednia > 5:
    print("Przeciętna")
else:
    print("Nie warta uwagi")