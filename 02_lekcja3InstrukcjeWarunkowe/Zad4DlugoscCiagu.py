ciag = input("Podaj dowolny ciąg znaków: \n")
dlugosc = len(ciag)
czyMaA = ciag.count("a")
print(czyMaA)

#Sprawdzam czy ciąg jest dłuższy niż 5
if dlugosc > 5:
    print("Ten ciąg znaków ma więcej niż 5 znaków")
elif dlugosc == 5:
    print("Ten ciąg znaków ma dokładnie 5 znaków")
else:
    print("Ten ciąg znaków ma mniej niż 5 znaków")

if czyMaA > 0:
    print("Zamieniam 'a' na 'z'!" , ciag.replace("a","z"))
else:
    print("Twój ciąg nie zawiera 'a'")


