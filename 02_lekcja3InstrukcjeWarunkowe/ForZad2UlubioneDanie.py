ingr = ["makaron", "sos", "kurczak", "warzywa", "bazylia"]
activity = ["Ugotuj", "Podgrzej na patelni", "Podsmaż", "Wymieszaj z sosem", "Udekoruj"]


for i in range(len(ingr)):
    print(activity[i], ingr[i])

print("***while***")
counter = 0
while counter < len(ingr):
    print(activity[counter], ingr[counter])
    counter += 1