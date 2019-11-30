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
        pass
    previous_line = line
    return line, previous_line


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
        else:
            return False


def unord_list_poss(line):
    for k in range(0, len(line)):
        if (line[k] == "+" or line[k] == "*" or line[k] == "-") and line[k+1] == " ":
            return True
        if line[k] == " " and ((line[k+1] == "+" or line[k+1] == "*" or line[k+1] == "-") or line[k+1] == " ")
            continue
        else:
            return False



def into_ord_list(line, previous_line):
    if previous_line[-4:] != "/li>":
        list = "<ol>\n<li>" + line + "</li>"
    else:
        list = "<li>" + line + "</li>"
    return list

# header_types = {
#         "######": "h6",
#         "#####": "h5",
#         "####": "h4",
#         "###": "h3",
#         "##": "h2",
#         "#": "h1",
#     }


