#Znajdź największa wspólny dzielnik (NWD) dwóch liczby. Wykorzystaj algorytm Euklidesa.

def euclidean_al(a, b):
    if a % b == 0:
        NWD = b
        return NWD
    else:
        modulo = a % b
        return euclidean_al(b, modulo)


a = int(input("Give the  bigger number"))
b = int(input("Give the smaller number"))

print(euclidean_al(a,b))