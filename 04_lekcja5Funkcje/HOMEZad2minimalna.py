
def pobieraj():
        liczba = int(input("Podaj liczbę: \n\t"))
        return liczba

def min_of(a,b,c):
    if a > b > c or b > a > c or a == b > c:
        mini = c
        return mini
    elif a > c > b or c > a > b or a == c > b:
        mini = b
        return mini
    elif b > c > a or c > b > a or b == c > a:
        mini = a
        return mini
    else:
        print("Jest więcej niż jedna liczba minimalna!")


print("W tym programie wskażę liczbę minimalną ze zbioru 3 liczb")
a = pobieraj()
b = pobieraj()
c = pobieraj()
minimalna = min_of(a,b,c)
print("Zatem najmniejsza to.....\n")
print(min_of(a,b,c))
