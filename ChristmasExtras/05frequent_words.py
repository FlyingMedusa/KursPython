
sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

word_list = []
words_frequency = {}

# Example result:
# 1. "mam" - 12
# 2. "tak" - 5
# 3. "z" - 2

for sentence in sentences:
    words = sentence.split()
    for word in words:
        word_list.append(word)


for word in word_list:
    word = word.lower()
    if word in words_frequency:
        words_frequency[word] += 1
    else:
        words_frequency[word] = 1

print(words_frequency)


list_of_values = words_frequency.values()
list_of_values = sorted(list_of_values)

sorted_list = []

i = 0
for el in list_of_values:
    sorted_list.append(str(i) + ":", el)

