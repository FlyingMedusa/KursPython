filename = 'wierszyk.txt'

with open(filename, encoding="utf-8") as fopen:
    poem = fopen.read()

poem = poem.lower()
poem = poem.replace(",", "")
poem = poem.split()
print(poem)
words_counter = {}

for w in poem:
    if w in words_counter.keys():
        words_counter[w] += 1
    else:
        words_counter[w] = 1

print(words_counter)


szer = 31
print("-" * szer)
print("|    Word    | How many times |")
print("*" * szer)

for k, v in words_counter.items():
    elem = f"\t{k} \t\t---\t{v}"
    print("| %10s | %14i |" % (k, v))

print("-" * szer)

with open("poem.txt", "w", encoding="utf-8") as fw:
    szer = 31
    fw.write("-" * szer)
    fw.write("\n")
    fw.write("|    Word    | How many times |\n")
    fw.write("-" * szer)
    fw.write("\n")
    for k, v in words_counter.items():
        elem = f"\t{k} \t\t---\t{v}"
        fw.write("| %10s | %14i |\n" % (k, v))
    fw.write("-" * szer)