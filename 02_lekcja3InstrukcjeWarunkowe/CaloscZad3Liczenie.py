#W podanym przez użytkownika ciągu wejściowym policz wszystkie:
# małe litery, wielkie litery, cyfry i znaki specjalne.

ciag = input("Podaj dowolny ciąg znaków:\n\t")

counter_lowers = 0
counter_uppers = 0
counter_decimal = 0
counter_extra = 0

for char in ciag:
    if char.islower():
        counter_lowers +=1
    elif char.isupper():
        counter_uppers += 1
    elif char.isdecimal():
        counter_decimal += 1
    elif not char.isalnum():
        counter_extra += 1

print("Małe litery:", counter_lowers,"duże litery:", counter_uppers, "cyrfy:", counter_decimal, "znaki specjalne", counter_extra)


