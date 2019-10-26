nat = int(input("Podaj liczbę naturalną nie większą niż 8: "))
silnia = 1

for liczba in range(1, nat+1):
    silnia = silnia * liczba
    if liczba == nat:
        print(liczba, " = ", silnia)
    else:
        print(liczba, end=" * ")

