# Użytkownik podaje dowolną liczbę N.
# Napisz, który wygeneruje słownik, wg zasady, że:
# każdej liczbie przyporządkowany jest jej kwadrat (n : n * n).

kwadraty_liczb= {}

ile = int(input("Podaj ile liczb chcesz umieścić w słowniku:"))

for i in range(0 , ile):
    liczba = int(input("Podaj dowolną liczbę:"))
    kwadraty_liczb[liczba] = liczba**2

for k, v in kwadraty_liczb.items():
    print(k, "-", v)

