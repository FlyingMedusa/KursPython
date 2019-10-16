# Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.

tabela = []
miejsca = int(input("Ile miejsc chcesz w tabeli?"))

for _ in range(miejsca):
    m = int(input("Podaj liczbę całkowitą do tabeli:"))
    tabela.append(m)

print(tabela)

if tabela[0] == tabela[-1]:
    print("Pierwsze i ostatnie miejsce zajmuje ta sama wartość")
else:
    print("Pierwsze i ostatnie miejsce zajmują różne wartości")

