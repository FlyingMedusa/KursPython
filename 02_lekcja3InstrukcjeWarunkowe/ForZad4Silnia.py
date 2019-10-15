l_nat = int(input("Podaj liczbę naturalną nie większą niż 8: "))
silnia = 1

for i in range(1 , l_nat+1):

    silnia = (i) * (silnia)
    print(silnia)
    silnia = silnia + 1