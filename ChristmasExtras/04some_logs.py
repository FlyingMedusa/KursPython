some_logs = {
    20 : 'ERROR',
    33 : 'WARNING',
    59 : 'WARNING4',
    74 : 'ERROR',
    99 : 'ERROR',
    81 : 'WARNING',
    62 : 'INFO',
    84 : 'ERROR',
    36 : 'WARNING',
    46 : 'WARNING2',
    85 : 'ERROR',
    64 : 'INFO',
    71 : 'ERROR1',
    7 : 'ERROR',
    37 : 'INFO4',
    90 : 'INFO',
    13 : 'INFO',
    93 : 'INFO',
    68 : 'ERROR',
    47 : 'WARNING'
}

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


start_interv = from_to("start")
end_interv = from_to("end")
print(get_logs(start_interv, end_interv, some_logs))