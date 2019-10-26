txt = input("Podaj dowolny tekst a ja wyświetlę pozycje parzyste: ")
dlugosc = len(txt)

for i in txt:
    if (text.index(sign)+1) % 2 == 0:
        print(sign, end="")
    else:
        continue
i = 0
while i < len(text):
    print(text[i+1], end='')
    i = i + 2