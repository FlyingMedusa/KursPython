num_lis = []
number_frequency = {}


def frequency(num_list):
    for number in num_list:
        if number in number_frequency:
            number_frequency[number] += 1
        else:
            number_frequency[number] = 1
    return number_frequency

while True:
    try:
        num_of_num = int(input("Please give me the number of integers you want to add to the list:\t"))
        print("*"*80)
        break
    except ValueError as e:
        print("Give an INTEGER -", e)

while True:
    try:
        first_elem = int(input("Please add first element:\t"))
        break
    except ValueError as e:
        print("Give an INTEGER -", e)
num_lis.append(first_elem)
for i in range(1,num_of_num):
    while True:
        try:
            elem = int(input("Please add next integer:\t"))
            break
        except ValueError as e:
            print("Give an INTEGER -", e)
    num_lis.append(elem)

number_frequency = frequency(num_lis)
max_freq = max(number_frequency, key=number_frequency.get)
min_freq = min(number_frequency, key=number_frequency.get)
print("*"*45)
print("Word with the highest frequency: \t", max_freq)
print("Word with the lowest frequency: \t", min_freq)