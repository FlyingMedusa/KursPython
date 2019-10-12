# Zadanie 2
# Napisz skrypt, ktory pobiera dwie wiadomosci od uzytkownika
# a nastepnie wyswietla je na ekranie poprzedzone ostrzezeniem "UWAGA: ..."
warning = "UWAGA: {0} , {1} !"
wiad1 = input("Podaj pierwszą wiadomość: \n")
wiad2 = input("Podaj drugą wiadomość: \n")
print(warning.format(wiad1,wiad2))