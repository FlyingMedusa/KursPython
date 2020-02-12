# gra, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5).
# Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

secret_num = 13
zgadywanka = int(input("Zgadnij liczbę ukrytą w programie: "))

while secret_num != zgadywanka:
    print("Liczba", zgadywanka, "nie jest liczbą ukrytą w programie!")
    zgadywanka = int(input("Zgadnij liczbę ukrytą w programie: "))

print('\nTak! To ta liczba!')

