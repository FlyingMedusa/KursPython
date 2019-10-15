a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
c = float(input("Podaj trzecią liczbę: "))

if a > b > c:
    print(a,b,c)
elif a > c > b:
    print(a, c, b)
elif b > a > c:
    print(b, a, c)
elif b > c > a:
    print(b, c, a)
elif c > a > b:
    print(c, a, b)
elif c > b > a:
    print(c, b, a)
else:
    print("UPS! Pewnie liczby mają tę samą wartość. \n Pamiętaj by dać 3 różne wartości.")