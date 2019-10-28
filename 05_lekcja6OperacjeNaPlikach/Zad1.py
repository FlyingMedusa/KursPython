filename = 'PanTadeusz.txt'

with open(filename, 'r') as fopen:
    lines = fopen.readlines()

for i in lines:
    print("Linia: ", i.strip(), end="*")
