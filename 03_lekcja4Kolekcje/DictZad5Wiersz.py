wiersz = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""
m_wiersz = wiersz.lower()
m_wiersz = m_wiersz.replace(',', '')
split_wiersz = m_wiersz.split()
split_wiersz = list(dict.fromkeys(split_wiersz))
print(split_wiersz)
array = []
for i in range(10):
    array.append(m_wiersz.count(split_wiersz[i]))
    i += 1
print(array)
