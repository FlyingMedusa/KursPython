
def in_factorial(x):
    if x == 1:
        return 1
    else:
        return x * in_factorial(x-1)


nat = int(input("Podaj liczbę naturalną:"))
print(in_factorial(nat))