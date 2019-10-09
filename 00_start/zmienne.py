(dystans, spalanie, cena) = (120, 0.064, 5.04)
koszt = dystans * spalanie * cena
print(koszt)
print("--------------------------------")
dystans = float(input("Podaj dystans: \n"))
spalanie = float(input("Podaj spalanie na 100km: \n"))
cena = float(input("Podaj cenę za litr: \n"))
koszt = dystans * (spalanie/100) * cena
print("Wydasz:", koszt)