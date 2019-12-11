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
        Format: day-month-year hour:minutes
        """
    print(intro)
    start = input("Please provide the start time:\t")
    start_date = datetime.strptime(start, '%d-%m-%Y %H:%M')
    start_timestamp = datetime.timestamp(start_date)
    end = input("Please provide the end time:\t")
    end_date = datetime.strptime(end, '%d-%m-%Y %H:%M')
    end_timestamp = datetime.timestamp(end_date)

    some_logs = {}

    content = content.split('\n')
    for l in content:
        if l != '':
            line = l.split(',')

            some_logs[int(line[0])] = line[1].strip().replace("'", "")

    print(int(start_timestamp))
    print(int(end_timestamp))

    chosen_logs = get_logs(int(start_timestamp), int(end_timestamp), some_logs)
    print(chosen_logs)

if __name__ == '__main__':
    main()