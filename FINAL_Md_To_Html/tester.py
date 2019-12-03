def ordered_list(line):
    line = line.lstrip("\t")
    line = line.lstrip(" ")
    for el in line:
        if el.isnumeric():
            line = line[1:]
        elif el == ".":
            return line


def giving_numbers()


list = [" 1. I just love <b>bold text</b>." ,
        " 2. I just love <em>italic text</em>.",
        " 2. I just love <b>bold text</b>.",
        " 2. I just love <em>italic text</em>.",
        " 3. Love<b>is</b> bold."]


for i in list:
    line = ordered_list(i)
    print(line)

