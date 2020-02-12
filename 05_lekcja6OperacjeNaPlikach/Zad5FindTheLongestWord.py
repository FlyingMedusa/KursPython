filename = 'PanTadeusz.txt'

with open(filename, 'r', encoding='utf-8') as fopen:
    lines = fopen.read()

lines = lines.replace(",", "")
lines = lines.replace("\n", " ")
words = lines.split(" ")
print(words)

longest = ''
for word in words:
    if len(word) > len(longest):
        longest = word

print("Najdłuższe:", longest)

