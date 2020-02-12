my_tuple = ('a', 3.4 , 77, 3j+4)

tmp_list = list(my_tuple)
tmp_list.remove(77)
print(tmp_list)
my_tuple = tuple(tmp_list)

#Schemat z krotką

numbers = [1, 4, 3, (10,20), 4, 5]
counter = 0

for n in numbers:
    if isinstance(n, tuple):
        break
    else:
        counter += 1

print(counter)
