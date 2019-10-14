# Zadanie 8
#Ulepsz program z zadania 7, tak aby zwrócił ile banknotów
# 50, 20, 10 i 5 euro otrzyma użytkownik.
money = float(input("Podaj kwotę pieniędzy [PLN], którą weźmiesz na wakacje: \n \t \t"))
kurs_euro = 4.30
money_euro = int(money/kurs_euro)
print("Biorąc ze sobą", money , "PLN masz" , money_euro,"Euro." )
ilosc50 = money_euro//50
bez50 = money_euro%50
ilosc20 = bez50//20
bez20 = bez50%20
ilosc10 = bez20//10
bez10 = bez20%10
ilosc5 = bez10//5

print("Wymieniając PLN na Euro dostaniesz prawdopodobnie: \n ",
      ilosc50 , "\tbanknotów o wartości 50Euro, \n \t",
      ilosc20, "\tbanknotów o wartości 20Euro, \n \t",
      ilosc10, "\tbanknotów o wartości 10Euro, \n \t",
      ilosc5, "\tbanknotów o wartości 5Euro.")

print("\n Aby wyjść z programu kliknij ENTER...")

