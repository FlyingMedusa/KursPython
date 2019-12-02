

def inside_checker(line):
    line = basic_checker(line, "**", "<b>", "</b>")
    line = basic_checker(line, "__", "<b>", "</b>")
    line = basic_checker(line, "*", "<em>", "</em>")
    line = basic_checker(line, "_", "<em>", "</em>")
    return line


def basic_checker(line, sign, mark1, mark2):
    occ = line.count(sign)
    if occ > 1:
        if occ % 2 == 0:
            for i in range(0, occ + 1):
                if i % 2 == 0:
                    line = line.replace(sign, mark1, 1)
                else:
                    line = line.replace(sign, mark2, 1)
            return line
        else:
            for i in range(0, occ - 1):
                if i % 2 == 0:
                    line = line.replace(sign, mark1, 1)
                else:
                    line = line.replace(sign, mark2, 1)
            return line
    return line


    return line


def clean(line):
    if "<b></b>" in line:
        line = line.replace("<b></b>","")
    return line