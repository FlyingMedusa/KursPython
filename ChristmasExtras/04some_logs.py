from datetime import datetime


def get_logs(start_interv, end_interv, logs):
    chosen_logs = []
    for i in range(start_interv, end_interv + 1):
        if i in logs:
            value = logs[i]
            chosen_logs.append(value)
    return set(chosen_logs)


def main():
    with open('logs_timestamp.csv', 'r') as fopen:
        content = fopen.read()

    intro = """
        Format: year, month, day, hour, minute, second
        Remember to separate them with SPACES!
        """
    print(intro)
    start = input("Please provide the start time:\t")
    range_start = start.split(" ")
    end = input("Please provide the end time:\t")
    range_end = end.split(" ")

    some_logs = {}

    content = content.split('\n')
    for l in content:
        if l != '':
            line = l.split(',')

            some_logs[line[0]] = line[1].strip().replace("'", "")
            some_logs[datetime.fromtimestamp(int(line[0]))] = some_logs.pop(line[0])

    print(some_logs)

    chosen_logs = get_logs(range_start, range_end, some_logs)
    print(chosen_logs)

if __name__ == '__main__':
    main()