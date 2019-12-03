

def ordered_list(line):
    line = line.lstrip("\t")
    line = line.lstrip(" ")
    for el in line:
        if el.isnumeric():
            line = line[1:]
        elif el == ".":
            return line


def reading_numbers(prev):
    prev = prev.lstrip("\t")
    prev = prev.lstrip("<ol>")
    prev = prev.lstrip("\n")
    prev = prev.lstrip("\t")
    prev = prev.lstrip("<li>")
    prev = prev.lstrip(" ")
    number = ""
    for i in range(0, len(prev)):
        try:
            elem = int(prev[i])
            number = number + str(elem)
        except:
            break
    return number


def giving_numbers(number,line):
    number = int(number)
    new_number = number + 1
    line = str(new_number) + line
    return line
