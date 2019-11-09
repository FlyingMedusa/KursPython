variety_table = ["buenosdias", 13, 7.45, 0, (9,10), True]

for i in range(len(variety_table)):
    try:
        result = 10 / variety_table[i]
        print(result)
    except TypeError as e:
        print("Holly molly! Your exception is:",e)
    except ZeroDivisionError as e:
        print("Holly molly! Your exception is:",e)
