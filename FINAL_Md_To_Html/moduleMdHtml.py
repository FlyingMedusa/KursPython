import moduleInside as module

def grand_checker(line,previous_line):
    line = line.strip("\n")
    p = previous_line
    if line[0] == "#":
        num = 0
        for i in line:
            if i == "#":
                num += 1
            else:
                line = deleting_char(line)
                line = into_header(num, line)
                break
    elif ord_list_possibility(line):
        line = into_ord_list(line, previous_line)
    elif unord_list_poss(line):
        line = into_unord_list(line, previous_line)
    else:
        line = into_paragraph(line)
    previous_line = line
    line = the_future_mode(p, previous_line)
    line = module.inside_checker(line)
    return line, previous_line


def the_future_mode(previous_line, now):
    now1 = now
    now = now.lstrip("\t")
    if previous_line[-4:] == "/li>" and now[:3] != "<li":
        if ord_list_possibility(previous_line):
            now = "\t</ol>\n" + "\t\t\t" + now
            return now
        if unord_list_poss(previous_line):
            now = "\t</ul>\n" + "\t\t\t" + now
            return now
    return now1


def deleting_char(line):
    for j in line:
        if j == "#":
            line = line[1:]
        else:
            return line


def into_header(num, line):

    header = "\t\t<h"+ str(num) + ">" + line + "</h" + str(num) + ">"
    return header


def ord_list_possibility(line):
    line = line.lstrip("\t")
    line = line.lstrip("<li>")
    for k in range(0, len(line)):
        if line[k].isnumeric() and line[k + 1] == "." and line[k + 2] == " ":
            return True
        elif line[k].isnumeric() and line[k + 1].isnumeric():
            continue
        elif (line[k] == " " and line[k + 1].isnumeric()):
            continue
        elif line[k] == " " and line[k + 1] == " ":
            continue
        else:
            return False


def into_ord_list(line, previous_line):
    if previous_line[-4:] != "/li>":
        line = ordered_list(line)
        list = "\t<ol>\n\t\t\t<li>1" + line + "</li>"
    else:
        line = ordered_list(line)
        list = "\t\t\t<li>" + line + "</li>"
    return list


def unord_list_poss(line):
    line = line.lstrip("\t")
    line = line.lstrip("<li>")
    for k in range(0, len(line)):
        if (line[k] == "+" or line[k] == "*" or line[k] == "-") and line[k+1] == " ":
            return True
        elif line[k] == " " and ((line[k+1] == "+" or line[k+1] == "*" or line[k+1] == "-") or line[k+1] == " "):
            continue
        else:
            return False


def into_unord_list(line, previous_line):
    if previous_line[-4:] != "/li>":
        line = unordered_list(line)
        list = "\t<ul>\n\t\t\t<li>" + line + "</li>"
    else:
        line = unordered_list(line)
        list = "\t\t\t<li>" + line + "</li>"
    return list


def into_paragraph(line):
    list = "\t\t<p>" + line + "</p>"
    return list


def ordered_list(line):
    line = line.lstrip("\t")
    line = line.lstrip(" ")
    for el in line:
        if el.isnumeric():
            line = line[1:]
        elif el == ".":
            line = line[1:]
            return line

def unordered_list(line):
    line = line.lstrip("\t")
    line = line.lstrip(" ")
    for el in line:
        if el == "*":
            line = line[1:]
        elif el == "+":
            line = line[1:]
        elif el == "-":
            line = line[1:]
        elif el == " ":
            return line