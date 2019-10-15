wielkosc = int(input("Ile segmentów ma mieć Twoja choinka?"))

for i in range(1, wielkosc+1):
    for j in range(1, i+2):
        print("#" * j)

