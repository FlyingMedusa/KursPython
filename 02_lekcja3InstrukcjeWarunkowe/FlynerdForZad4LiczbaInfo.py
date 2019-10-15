razy = int(input("Wpierw podaj ile liczb masz do sprawdzenia:"))


for i in range(0,razy):
    liczba = int(input("Podaj dowolną liczbę a ja sprawdzę kilka rzeczy:"))
    if liczba % 3 == 0 and liczba % 4 == 0:
        print("Hurra!!")
    elif liczba % 3 != 0 and liczba % 4 != 0:
        print("***")
    else:
        if liczba % 3 == 0:
            print("Liczba jest wielokrotnością 3")
        else:
            print("Liczba nie jest wielokrotnością liczby 3")

        if liczba % 4 == 0:
            print("Liczba jest wielokrotnością 4")
        else:
            print("Liczba nie jest wielokrotnością liczby 4")