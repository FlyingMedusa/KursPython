#Zadanie drugie
print("Zadanie drugie: wsadzanie zdania s2 w zdanie s1 \n")
s1 = input("Podaj pierwsze zdanie: \n")
s2 = input("Podaj drugie zdanie: \n")
middle = len(s1)//2
print(s1[:middle] +s2 + s1[middle:])