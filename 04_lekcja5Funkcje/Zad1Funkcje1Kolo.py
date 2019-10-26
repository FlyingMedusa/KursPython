#Napisać funkcję, która oblicza pole koła na podstawie zadanego promienia.

pi = 3.14

def count_kolo(field):
    field = pi * r**2
    return field

r = float(input("Podaj promień koła:"))
field = count_kolo(r)
print(field)