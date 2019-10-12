# Zadanie 7
# Napisz konwerter walut.
# Program poprosi użytkownika o kwotę pieniędzy, jaką wezmą na wakacje
# a następnie przeliczy tę kwotę w euro oraz w dolarach.
# Zignoruj wszelkie centy, które mogą wyniknąć z konwersji.
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.
money = float(input("Podaj kwotę pieniędzy [PLN], którą weźmiesz na wakacje: \n \t \t"))
kurs_euro = 4.30
kurs_dolar = 3.93
money_euro = money/kurs_euro
money_dolar = money/kurs_dolar
print("Biorąc ze sobą", money , "PLN masz" , int(money_euro),"Euro i", int(money_dolar), "USD." )