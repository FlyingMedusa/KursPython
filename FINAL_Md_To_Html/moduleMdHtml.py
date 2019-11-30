def loading_file():

    while True:
        filename = input("\nPlease give me the name of your markdown file\n\t")
        if filename[-3:] == ".md":
            break
        elif "." in filename:
            print("Wrong extension")
        elif "." not in filename:
            filename = filename + ".md"
            break
        else:
            print("It shouldn't have happened")

    return filename


def creating_file():
    while True:
        filename = input("\nPlease give me the name of your new html file\n\t")
        if filename[-5:] == ".html":
            break
        elif "." in filename:
            print("Sorry - wrong extension")
        elif "." not in filename:
            filename = filename + ".html"
            break
        else:
            print("It shouldn't have happened")

    return filename


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
    line = inside_checker(line)
    return line, previous_line


def inside_checker(line):
    if is_bold(line):
        pass


def the_future_mode(previous_line, now):
    if previous_line[-4:] == "/li>" and now[:4] != "\t<li":
        previous_line = previous_line.strip("\t")
        previous_line = previous_line[4:]
        if ord_list_possibility(previous_line):
            now = "</ol>\n" + now
        if unord_list_poss(previous_line):
            now = "</ul>\n" + now

    return now


def deleting_char(line):
    for j in line:
        if j == "#":
            line = line[1:]
        else:
            return line


def into_header(num, line):

    header = "<h"+ str(num) + ">" + line + "</h" + str(num) + ">"
    return header


def ord_list_possibility(line):
    for k in range(0, len(line)):
        if line[k].isnumeric() and line[k+1] == "." and line[k+2] == " ":
            return True
        elif line[k].isnumeric() and line[k+1].isnumeric():
            continue
        elif (line[k] == " " and line[k+1].isnumeric()):
            continue
        elif line[k] == " " and line[k+1] == " ":
            continue
        else:
            return False


def into_ord_list(line, previous_line):
    if previous_line[-4:] != "/li>":
        list = "<ol>\n\t<li>" + line + "</li>"
    else:
        list = "\t<li>" + line + "</li>"
    return list


def unord_list_poss(line):
    for k in range(0, len(line)):
        if (line[k] == "+" or line[k] == "*" or line[k] == "-") and line[k+1] == " ":
            return True
        elif line[k] == " " and ((line[k+1] == "+" or line[k+1] == "*" or line[k+1] == "-") or line[k+1] == " "):
            continue
        else:
            return False


def into_unord_list(line, previous_line):
    if previous_line[-4:] != "/li>":
        list = "<ul>\n\t<li>" + line + "</li>"
    else:
        list = "\t<li>" + line + "</li>"
    return list


def into_paragraph(line):
    list = "<p>" + line + "</p>"
    return list

def is_bold(line):
    if line

