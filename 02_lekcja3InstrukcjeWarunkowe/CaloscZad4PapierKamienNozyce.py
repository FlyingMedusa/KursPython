print("\nWitaj w grze kamień, papier, nożyce! \n")
print("Możliwe zagrania:\n\tk - kamień\n\tp - papier\n\tn - nożyce")
rundy = int(input("Ile rund chcesz zagrać?"))

pkt_u = []
pkt_k = []
for i in range(0, int(rundy)):

    ruch = input("\nWykonaj swój ruch:\t")

    if ruch == "k":
        ruch = "kamień"
    elif ruch == "p":
        ruch = "papier"
    elif ruch == "n":
        ruch = "nożyce"
    else:
        while ruch != "k" and ruch != "p" and ruch != "n":
            print("\nUWAŻAJ!\nPamiętaj by wpisać wybór jako:\n\tk - kamień\n\tp - papier\n\tn - nożyce")
            ruch = input("Wykonaj swój ruch:")
            if ruch == "k" or ruch == "p" or ruch == "n":
                if ruch == "k":
                    ruch = "kamień"
                elif ruch == "p":
                    ruch = "papier"
                else:
                    ruch = "nożyce"
                break

    if ruch == "k":
        print("Wybrałeś", ruch, "!")
    elif ruch == "p":
        print("Wybrałeś", ruch, "!")
    else:
        print("Wybrałeś", ruch, "!\n")

    import random

    k = "kamień"
    p = "papier"
    n = "nożyce"
    wybor = [k, p, n]
    komputer = random.choice(wybor)
    print("Twój przeciwnik wybrał", komputer,"\n")


    if (ruch == "papier" and komputer == "kamień") or (ruch == "kamień" and komputer == "nożyce") or (
            ruch == "nożyce" and komputer == "papier"):
        if ruch == "nożyce":
            print(ruch.capitalize(), "pokonują", komputer, "!\n\tWYGRYWASZ!")
        else:
            print(ruch.capitalize(), "pokonuje", komputer, "!\n\tWYGRYWASZ!")
        pkt_u.append(1)
        pkt_k.append(0)
    elif (ruch == "kamień" and komputer == "papier") or (ruch == "nożyce" and komputer == "komputer") or (
            ruch == "papier" and komputer == "nożyce"):
        if komputer == "nożyce":
            print(komputer.capitalize(), "pokonują", ruch, "...\n\tPRZEGRAŁEŚ!")
        else:
            print(komputer.capitalize(), "pokonuje", ruch, "...\n\tPRZEGRAŁEŚ!")
        pkt_u.append(0)
        pkt_k.append(1)
    else:
        print(ruch.capitalize(), "i", komputer, "nie są w stanie walczyć...\n\tREMIS!")
        pkt_u.append(0)
        pkt_k.append(0)


i += 1
wynik_u = sum(pkt_u)
wynik_k = sum(pkt_k)

v1 = "punkt"
v2 = "punkty"
v3 = "punktów"

if wynik_u == 1:
    print("\nZdobyłeś łącznie", wynik_u, v1)
elif wynik_u == 2 or wynik_u == 3 or wynik_u == 4:
    print("\nZdobyłeś łącznie", wynik_u, v2)
else:
    print("\nZdobyłeś łącznie", wynik_u, v3)

if wynik_k == 1:
    print("A Twój przeciwnik", wynik_k, v1)
elif wynik_k == 2 or wynik_k == 3 or wynik_k == 4:
    print("A Twój przeciwnik", wynik_k, v2)
else:
    print("A Twój przeciwnik", wynik_k, v3)

if wynik_u > wynik_k:
    print("Zatem WYGRAŁEŚ!")
elif wynik_u < wynik_k:
    print("Zatem PRZEGRAŁEŚ!")
else:
    print("Mamy REMIS!")