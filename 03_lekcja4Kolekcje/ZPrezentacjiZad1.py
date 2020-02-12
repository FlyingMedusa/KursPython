animals = ["Dog", "Cat", "Fish", "Cat", "Horse", "Dolphin"]

#Metoda, która utworzy kopię listy i shallow vs deep:
print(animals.copy())
list1 = [1, 2, [2, 3], 3, 4]
list2 = list1
list3 = list1.copy()
list4 = list1.deepcopy()

#Metoda, która posortuje elementy na liście:
print(sorted(animals))

#Metoda, która usunie wszystkie elementy z listy
#print(animals.clear())

#Policzy wystąpienia tego samego elementu na liście
print(animals.count("Cat"))

#Zsumuje elementy na liście
numbers = [3, 7, 5, 3, 4, 6, 7]
print(sum(numbers))