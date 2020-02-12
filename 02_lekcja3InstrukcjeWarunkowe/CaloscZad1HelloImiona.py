names = input("Podaj imiona podzielone spacją: ")
names = names.split()
print(names)

for i in names:
    print("Hello ", i, "!")

#-------------------

id = 0
while id < len(names):
    print("Hi", names[id])
    id += 1