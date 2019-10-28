import random
filename = 'Cytaty.txt'


def random_quotes(lines):
    for i in range(0,3):
        quote = random.choice(lines)
        print(quote)



with open(filename, 'r') as f:
    lines = f.readlines()

quote_for_today = random.choice(lines).strip()
quote_for_today = quote_for_today.split('-')
print("Quote of the day is:")
print("*" * 85)
print(quote_for_today[0].center(85))
print(quote_for_today[1].center(85))
print("*" * 85)

#--------------Wyświetl tylko 5 pierwszych linii

for i in range(0, 5):
    print(lines[i])

#-----3-losowe-cytaty--------------------------
print('*'*20)

print(random_quotes(lines))