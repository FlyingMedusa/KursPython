
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
list_of_values = sorted(words_frequency.values())
sorted_list = list_of_values[-3:]

for key, value in words_frequency.items():
    if value in sorted_list:
        print(f"{key} - {value}")
