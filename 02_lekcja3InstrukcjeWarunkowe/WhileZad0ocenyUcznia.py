counter = 1


while (counter != 3):
    subject = input("Podaj przedmiot: ")
    grade = input("Podaj ocenę w skali 1-6: ")
    print(subject, ":", grade)
    counter += 1

# druga wersja
przedmioty = input("Podaj przedmioty podzielone myślnikiem: ")
oceny = input("Podaj oceny podzielone myślnikiem: ")

przedmioty = przedmioty.split("-")
oceny = oceny.split("-")

licznik = 0

while licznik < 3:
    print(przedmioty[licznik], "-", oceny[licznik])
    licznik = licznik + 1