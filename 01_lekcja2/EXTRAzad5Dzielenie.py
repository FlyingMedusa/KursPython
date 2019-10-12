# Zadanie 5
# Napisz program, który pyta użytkownika o 2 liczby
# a następnie dzieli jedna przez drugą.
# Pokaż ile razy pierwsza liczba mieści się w drugiej
# oraz jaka jest reszta tego dzielenia. 
num1 = float(input("Porszę podaj pierwszą liczbę:"))
num2 = float(input("Proszę podaj drugą liczbę: "))
equation1 = num1/num2
equation2 = num2//num1
equation3 = num1%num2
print("Wynik dzielenia tych liczb to: \n \t \t", equation1)
print("Pierwsza liczba mieści się", int(equation2) ,"razy w drugiej")
print("Reszta z dzielenia liczby pierwszej przez drugą wynosi: \n \t \t", equation3)
#dodaję tylko po to by konsola poczekała [test]
input("\n Press any key to terminate")