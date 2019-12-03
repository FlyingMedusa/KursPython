

def inside_checker(line):
    line = basic_checker(line, "**", "<b>", "</b>")
    line = basic_checker(line, "__", "<b>", "</b>")
    line = basic_checker(line, "*", "<em>", "</em>")
    line = basic_checker(line, "_", "<em>", "</em>")
    line = basic_checker(line, "`", "<code>", "</code>")
    line = clean(line, "<b>", "</b>")
    line = clean(line, "<em>", "</em>")
    line = clean(line, "<code>", "</code>")
    return line


def basic_checker(line, sign, tag1, tag2):
    occ = line.count(sign)
    if occ > 1:
        if occ % 2 == 0:
            for i in range(0, occ + 1):
                if i % 2 == 0:
                    line = line.replace(sign, tag1, 1)
                else:
                    line = line.replace(sign, tag2, 1)
            return line
        else:
            for i in range(0, occ - 1):
                if i % 2 == 0:
                    line = line.replace(sign, tag1, 1)
                else:
                    line = line.replace(sign, tag2, 1)
            return line
    return line


def clean(line, tag1, tag2):
    if str(tag1 + tag2) in line:
        line = line.replace(str(tag1 + tag2),"")
    return line