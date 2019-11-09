variety_table = ["buenosdias", 13+2j ,False , 7.45, 0,"Bonjour", (9,10), True, {3.33 , 2}, "Konnichiwa"]

index = int(input("Gimme an index:\t"))
try:
    value = variety_table[index]
    result = 1/value
    print(result)
except ZeroDivisionError as e:
    result = "Ohhh, do not divide by zero! It's " + str(e)
except TypeError as e:
    result = "Types, types everywhere! It's " + str(e)
print(result)