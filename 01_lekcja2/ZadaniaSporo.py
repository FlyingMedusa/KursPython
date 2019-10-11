print("Zadanaie 1")

tekst = input("Podaj wyraz, który ma więcej niż 7 znaków i jest nieparzysty: ")
print(len(tekst))
middle = len(tekst)//2
print(tekst[middle - 1] + tekst[middle] + tekst[middle + 1])
print(tekst[middle - 1 : middle +2])

print("Zadanie 3")

quote = "Honesty is the first chapter in the book of wisdom."
dlugosc=(len(quote))
print(dlugosc)
print(quote[-7:-1])
print(quote[:dlugosc//2])
print(quote[-1:])
print(quote[dlugosc//2::3])
print(quote[::2])
print(quote[::-1])
print(quote.replace("wisdom", "friendship"))

print("Zadanie 5")
zdanie = input("Podaj zdanie: ")
print(zdanie)
print(zdanie[::-1])
print(zdanie.lower() == zdanie[::-1].lower())
zdanie = zdanie.replace(" ", "")
zdanie = zdanie.lower()
print(zdanie == zdanie[::-1])