def suma(N):
    s = 0
    for liczba in range(1, N+1):
        s = s + liczba
        print("ostatni wynik:", s)
    return s

l_nat = int(input("Podal liczbę naturalną: \t"))
print(suma(l_nat))

def suma_while(n):
    s = 0
    while n > 0:
        s = s + n
        n = n -1
    return s

l_nat = int(input("Podal liczbę naturalną: \t"))
print(suma_while(l_nat))

def s_recursion(n):
    if n == 1:
        return 1
    else:
        return n + s_recursion(n-1)

print("Suma rekurencyjnie: ", s_recursion(10))