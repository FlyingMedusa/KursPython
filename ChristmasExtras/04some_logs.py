filename = 'logs.csv'
dict = {}
chosen_logs = []


def get_logs(start_interv, end_interv, dict):
    for i in range(start_interv, end_interv+1):
        if i in dict:
            value = dict.get(i)
            chosen_logs.append(value)
    return chosen_logs


def from_to(y):
    while True:
        try:
            x = int(input("Please provide the " + y + " interval:\t"))
            return x
        except ValueError as e:
            print("Give an INTEGER -", e)


with open(filename, 'r') as fopen:
    content = fopen.read()


with open('dictionary.txt', 'w') as fw:
    turn = 0
    for line in content.split():
        if turn == 0:
            line = line.replace(",", " ")
            fw.write(line)
            turn = 1
        elif turn == 1:
            line = line.replace(",", "")
            fw.write(line + "\n")
            turn = 0


with open('dictionary.txt', 'r') as fopen:
    for line in fopen:
       (key, value) = line.split()
       dict[int(key)] = value




start_interv = from_to("start")
end_interv = from_to("end")

chosen_logs = get_logs(start_interv, end_interv, dict)
list_to_set = set(chosen_logs)
print(list_to_set)