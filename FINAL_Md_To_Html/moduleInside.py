

def inside_checker(line):

    line = is_bold1(line)
    line = is_bold2(line)
    line = is_italic1(line)
    line = is_italic2(line)
    return line


def is_bold1(line):
    occ = line.count('**')
    if occ > 1:
        if occ % 2 == 0:
            for i in range(0, occ + 1):
                if i % 2 == 0:
                    line = line.replace("**", "<b>", 1)
                else:
                    line = line.replace("**", "</b>", 1)
            return line
        else:
            for i in range(0, occ - 1):
                if i % 2 == 0:
                    line = line.replace("**", "<b>", 1)
                else:
                    line = line.replace("**", "</b>", 1)
            return line
    return line


def is_bold2(line):
    occ = line.count('__')
    if occ > 1:
        if occ % 2 == 0:
            for i in range(0, occ + 1):
                if i % 2 == 0:
                    line = line.replace("__", "<b>", 1)
                else:
                    line = line.replace("__", "</b>", 1)
            return line
        else:
            for i in range(0, occ - 1):
                if i % 2 == 0:
                    line = line.replace("__", "<b>", 1)
                else:
                    line = line.replace("__", "</b>", 1)
            return line
    return line


def is_italic1(line):
    occ = line.count('*')
    if occ > 1:
        if occ % 2 == 0:
            for i in range(0, occ + 1):
                if i % 2 == 0:
                    line = line.replace("*", "<em>", 1)
                else:
                    line = line.replace("*", "</em>", 1)
            return line
        else:
            for i in range(0, occ - 1):
                if i % 2 == 0:
                    line = line.replace("*", "<em>", 1)
                else:
                    line = line.replace("*", "</em>", 1)
            return line
    return line


def is_italic2(line):
    occ = line.count('*')
    if occ > 1:
        if occ % 2 == 0:
            for i in range(0, occ + 1):
                if i % 2 == 0:
                    line = line.replace("_", "<em>", 1)
                else:
                    line = line.replace("_", "</em>", 1)
            return line
        else:
            for i in range(0, occ - 1):
                if i % 2 == 0:
                    line = line.replace("_", "<em>", 1)
                else:
                    line = line.replace("_", "</em>", 1)
            return line
    return line


def clean(line):
    if "<b></b>" in line:
        line = line.replace("<b></b>","")
    return line