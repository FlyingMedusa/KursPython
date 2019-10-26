import random
komputer = random.randint(1,100)

print("To gra w ciepło-zimno. Zgadnij ukrytą cyfrę w zakresie 1 - 100")
guess1 = int(input("Podaj Twoje podejrzenie:"))
podejrzenia = [guess1]

if guess1 != komputer:
    print("Nie trafiłeś. Ale nie martw się!\nMasz 6 szans a ja podpowiem Ci czy jest ciepło czy zimno!")
    for i in range(6):
        guess2 = int(input("Podaj Twoje kolejne podejrzenie:"))
        podejrzenia.append(guess2)
        if guess2 != komputer:
            if abs(komputer - podejrzenia[i]) > abs(komputer - podejrzenia[i + 1]):
                print("Ciepło!")
            elif abs(komputer - podejrzenia[i]) < abs(komputer - podejrzenia[i + 1]):
                print("Zimno!")
            else:
                print("Jesteś tak samo daleko od odpowiedzi jak byłeś")
            while i == 5:
                print("Przegrałeś: odpowiedzią było:",komputer)
                break
        else:
            print("Brawo! Zgadłeś!")
            break
        i += 1
else:
    print("Niewiarygodne! Zgadłeś za pierwszym razem!")



