
def pobieraj():
        return int(input("Podaj liczbę: \n\t"))

def max_of_2(first, second):
    return first if first > second else second

def max_of(a,b,c):
    return max_of_2(max_of_2(a,b),c)


print("W tym programie wskażę liczbę minimalną ze zbioru 3 liczb")
x = pobieraj()
y = pobieraj()
z = pobieraj()
maksymalna = max_of(x,y,z)
print("Zatem największa liczba to", maksymalna)
