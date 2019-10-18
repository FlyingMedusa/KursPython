krotka = ("Mrówka", 4, "Dom", 3.46, "Mrówka", 5)
print(krotka)
zestaw = set(krotka)
print(zestaw)

print("\nTest 1\n")

num_tuple = (1, 2, 3, 4)
tmp_list = list(num_tuple)
tmp_list.remove(2)
num_tuple = tuple(tmp_list)
print(num_tuple)

print("\nTest2\n")

user = ("Marta", "Sleboda", 1998)
(name, surname, year) = user
print(surname, year)