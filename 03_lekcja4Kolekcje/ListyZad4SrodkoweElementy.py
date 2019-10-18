#Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.

elements = int(input("\nStworzę tabelę i sprawdzę czy 2 środkowe elementy są takie same.\nPodaj więc parzystą liczbę elementów:\n\t"))

while elements%2 == 1:
    print("Błąd. Liczba elementów musi być parzysta")
    elements = int(input("Podaj PARZYSTĄ liczbę elementów\n\t"))

print("Dziękuję. Podałeś parzystą liczbę elementów. \n Pierwszy etap za nami.")

print("Teraz podaj po kolei elementy którymi wypełnimy Twoją",str(elements) + "-elementową tabelę")

array = []

for i in range(elements):
    wartosc = input("Podaj element: \n\t")
    array.append(wartosc)

print("\nMamy wszystkie elementy Twojej tablicy. Oto ona:\n", array)
print("Sprawdźmy czy środkowe elementy twojej tabeli są takie same! \n Processing...\n")

srodek = int(len(array)/2)
sr1 = array[srodek-1]
sr2 = array[srodek]

if sr1 == sr2:
    print("Twoje środkowe elementy są takie same! Super!")
else:
    print("Twoje środkowe elementy są różne.")